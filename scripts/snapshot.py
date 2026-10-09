#!/usr/bin/env python3
"""Capture explicitly supplied public HTTPS evidence; never publish it."""

import argparse
import hashlib
from http.client import HTTPException
import ipaddress
import json
import os
from pathlib import Path
import socket
import sys
import tempfile
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qsl, urlsplit
from urllib.request import HTTPRedirectHandler, ProxyHandler, Request, build_opener


SCHEMA_VERSION = 1
SENSITIVE_QUERY_KEYS = {"access_token", "api_key", "apikey", "auth", "authorization",
                        "key", "password", "secret", "signature", "sig", "token"}


def utc_now():
    return datetime.now(timezone.utc).isoformat(timespec="microseconds").replace("+00:00", "Z")


class UnsafeURL(ValueError):
    """The URL is unsuitable for an unauthenticated public-source capture."""


def public_https_url(url, resolve=True):
    """Reject credentials, local addresses, and non-HTTPS targets, including redirects."""
    try:
        parts = urlsplit(url)
        if parts.scheme != "https" or not parts.hostname or parts.fragment:
            raise UnsafeURL("Expected an absolute HTTPS URL without a fragment")
        if parts.username is not None or parts.password is not None:
            raise UnsafeURL("Credentials in URLs are forbidden")
        if any(k.lower() in SENSITIVE_QUERY_KEYS for k, _ in parse_qsl(parts.query)):
            raise UnsafeURL("Credential-like query parameters are forbidden")
        if any(c.isspace() or ord(c) < 32 for c in url):
            raise UnsafeURL("Whitespace and control characters are forbidden")
        port = parts.port or 443
        hostname = parts.hostname
        if hostname.lower().rstrip(".") == "localhost" or hostname.lower().rstrip(".").endswith(".localhost"):
            raise UnsafeURL("Local addresses are forbidden")
        try:
            address = ipaddress.ip_address(hostname)
        except ValueError:
            address = None
        if address is not None and not address.is_global:
            raise UnsafeURL("Non-public addresses are forbidden")
        if resolve:
            addresses = socket.getaddrinfo(hostname, port, type=socket.SOCK_STREAM)
            if not addresses or any(not ipaddress.ip_address(item[4][0]).is_global
                                    for item in addresses):
                raise UnsafeURL("The hostname must resolve only to public addresses")
    except (ValueError, UnicodeError) as exc:
        if isinstance(exc, UnsafeURL):
            raise
        raise UnsafeURL("Malformed HTTPS URL") from None
    return url


def safe_url_for_log(url):
    """Never retain a rejected credential-bearing URL in a failure record."""
    try:
        return public_https_url(url, resolve=False)
    except UnsafeURL:
        return "[rejected URL omitted]"


class PublicHTTPSRedirects(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        public_https_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def append_record(directory, record):
    directory.mkdir(parents=True, exist_ok=True)
    with (directory / "manifest.jsonl").open("a", encoding="utf-8") as stream:
        stream.write(json.dumps(record, sort_keys=True, ensure_ascii=False) + "\n")


def store_bytes(directory, data, digest):
    relative = Path("objects") / (digest + ".bin")
    destination = directory / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        if destination.read_bytes() != data:
            raise OSError("Existing content-addressed object differs from capture")
        return relative.as_posix()
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=destination.parent, delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(data)
        os.replace(temporary, destination)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
    return relative.as_posix()


def capture(url, directory, timeout=30, max_bytes=50 * 1024 * 1024):
    """Append exactly one outcome after an attempted capture; return its record.

    Recording/storage failures propagate: callers must not claim an unlogged capture.
    The byte limit prevents accidental unbounded local downloads.
    """
    directory = Path(directory)
    record = {
        "schema_version": SCHEMA_VERSION,
        "status": "failed",
        "attempted_utc": utc_now(),
        "requested_url": safe_url_for_log(url),
        "final_url": None,
        "http_status": None,
        "media_type": None,
        "content_encoding": None,
        "retrieved_utc": None,
        "byte_size": None,
        "sha256": None,
        "snapshot_path": None,
        "assessment": {"rights": "unassessed", "legal_status": "unassessed",
                       "assessed_by": None, "assessed_utc": None, "notes": None},
    }
    try:
        public_https_url(url)
        # No environment proxies, cookies, authorization headers, or account credentials.
        opener = build_opener(ProxyHandler({}), PublicHTTPSRedirects())
        request = Request(url, headers={"User-Agent": "public-evidence-snapshot/1.0",
                                       "Accept-Encoding": "identity"})
        with opener.open(request, timeout=timeout) as response:
            final_url = response.geturl()
            public_https_url(final_url)
            record["final_url"] = final_url
            record["http_status"] = response.status
            record["media_type"] = response.headers.get("Content-Type", "").split(";", 1)[0].strip().lower() or None
            record["content_encoding"] = response.headers.get("Content-Encoding")
            if not 200 <= response.status < 300:
                raise ValueError("HTTP response was not successful")
            if response.status == 206 or response.headers.get("Content-Range") is not None:
                raise ValueError("Partial content is not a complete source capture")
            body = response.read(max_bytes + 1)
            if len(body) > max_bytes:
                raise ValueError("Response exceeded byte limit")
            length = response.headers.get("Content-Length")
            if length is not None and int(length) != len(body):
                raise ValueError("Content-Length does not match received bytes")
        record["retrieved_utc"] = utc_now()
        digest = hashlib.sha256(body).hexdigest()
        relative = store_bytes(directory, body, digest)
        record.update(status="success", byte_size=len(body), sha256=digest,
                      snapshot_path=relative)
    except HTTPError as exc:
        record.update(http_status=exc.code, final_url=safe_url_for_log(exc.geturl()),
                      error_type="HTTPError", error="HTTP request failed")
        exc.close()
    except (UnsafeURL, URLError, OSError, ValueError, HTTPException) as exc:
        # Do not copy exception strings: they can contain sensitive URLs or local paths.
        record.update(error_type=type(exc).__name__,
                      error="Capture failed; no successful snapshot recorded")
    if record["status"] == "failed":
        record["failed_utc"] = utc_now()
        record["retrieved_utc"] = None
    append_record(directory, record)
    return record


def verify(manifest):
    """Offline verification; failures in the acquisition ledger remain visibly separate."""
    manifest = Path(manifest)
    root = manifest.parent.resolve()
    summary = {"verified": 0, "failed_captures": 0, "errors": []}
    with manifest.open(encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, 1):
            try:
                record = json.loads(line)
                if record.get("schema_version") != SCHEMA_VERSION:
                    raise ValueError("Unsupported manifest schema")
                if record.get("status") == "failed":
                    if record.get("snapshot_path") is not None or record.get("sha256") is not None:
                        raise ValueError("Failed capture must not claim a successful snapshot")
                    summary["failed_captures"] += 1
                    continue
                if record.get("status") != "success":
                    raise ValueError("Unknown capture status")
                relative = Path(record["snapshot_path"])
                if relative.is_absolute() or ".." in relative.parts:
                    raise ValueError("Snapshot path must be relative and stay within the manifest directory")
                path = (root / relative).resolve()
                if root not in path.parents:
                    raise ValueError("Snapshot path escapes manifest directory")
                data = path.read_bytes()
                if len(data) != record["byte_size"]:
                    raise ValueError("Byte-size mismatch")
                if hashlib.sha256(data).hexdigest() != record["sha256"]:
                    raise ValueError("SHA-256 mismatch")
                summary["verified"] += 1
            except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
                summary["errors"].append({"line": line_number, "error_type": type(exc).__name__,
                                           "error": str(exc) if isinstance(exc, ValueError) else "Invalid or unavailable snapshot"})
    return summary


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    subcommands = parser.add_subparsers(dest="command", required=True)
    fetch = subcommands.add_parser("capture", help="Capture explicit public HTTPS URLs locally")
    fetch.add_argument("urls", nargs="+")
    fetch.add_argument("--output-dir", type=Path, default=Path(".local-sources"))
    fetch.add_argument("--timeout", type=float, default=30)
    fetch.add_argument("--max-bytes", type=int, default=50 * 1024 * 1024)
    check = subcommands.add_parser("verify", help="Verify retained bytes offline")
    check.add_argument("manifest", type=Path, nargs="?", default=Path(".local-sources/manifest.jsonl"))
    args = parser.parse_args(argv)
    if args.command == "capture" and (args.timeout <= 0 or args.max_bytes <= 0):
        parser.error("Timeout and byte limit must be positive")
    try:
        if args.command == "capture":
            records = [capture(url, args.output_dir, args.timeout, args.max_bytes) for url in args.urls]
            for record in records:
                print(json.dumps({key: record[key] for key in ("status", "requested_url", "http_status", "sha256")}, sort_keys=True))
            return int(any(record["status"] != "success" for record in records))
        summary = verify(args.manifest)
        print(json.dumps(summary, sort_keys=True))
        return int(bool(summary["errors"]) or summary["verified"] == 0)
    except OSError:
        print("Local storage or manifest access failed; operation not verified", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
