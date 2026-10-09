"""Network-free behavioral tests for the provenance utility."""

import hashlib
from http.client import IncompleteRead
import importlib.util
import json
from pathlib import Path
import socket
import tempfile
import unittest
from unittest.mock import Mock, patch
from urllib.error import HTTPError, URLError


SPEC = importlib.util.spec_from_file_location("snapshot", Path(__file__).parents[1] / "scripts/snapshot.py")
snapshot = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(snapshot)


class SnapshotTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        self.dns = patch.object(snapshot.socket, "getaddrinfo", return_value=[
            (socket.AF_INET, socket.SOCK_STREAM, 6, "", ("93.184.216.34", 443))])
        self.dns.start()
        self.addCleanup(self.dns.stop)
        # Every opener is mocked, even in URL rejection tests: accidental network is forbidden.
        self.opener_patch = patch.object(snapshot, "build_opener")
        self.build_opener = self.opener_patch.start()
        self.addCleanup(self.opener_patch.stop)
        self.opener = self.build_opener.return_value

    def successful_response(self, body=b"public evidence\x00\xff"):
        response = Mock()
        response.status = 200
        response.headers = {"Content-Type": "application/pdf; charset=binary", "Content-Length": str(len(body))}
        response.geturl.return_value = "https://public.example/final.pdf"
        response.read.return_value = body
        self.opener.open.return_value.__enter__.return_value = response
        return response

    def test_capture_preserves_original_bytes_and_provenance(self):
        body = b"public evidence\x00\xff"
        self.successful_response(body)
        record = snapshot.capture("https://public.example/source", self.directory)
        self.assertEqual(record["status"], "success")
        self.assertEqual((self.directory / record["snapshot_path"]).read_bytes(), body)
        self.assertEqual(record["sha256"], hashlib.sha256(body).hexdigest())
        self.assertEqual(record["byte_size"], len(body))
        self.assertEqual(record["requested_url"], "https://public.example/source")
        self.assertEqual(record["final_url"], "https://public.example/final.pdf")
        self.assertEqual(record["http_status"], 200)
        self.assertEqual(record["media_type"], "application/pdf")
        self.assertTrue(record["retrieved_utc"].endswith("Z"))
        self.assertEqual(record["assessment"]["rights"], "unassessed")
        self.assertEqual(record["assessment"]["legal_status"], "unassessed")
        self.assertEqual(snapshot.verify(self.directory / "manifest.jsonl"),
                         {"verified": 1, "failed_captures": 0, "errors": []})

    def test_same_size_content_corruption_detected(self):
        self.successful_response(b"original")
        record = snapshot.capture("https://public.example/source", self.directory)
        (self.directory / record["snapshot_path"]).write_bytes(b"modified")
        result = snapshot.verify(self.directory / "manifest.jsonl")
        self.assertEqual(result["verified"], 0)
        self.assertEqual(result["errors"][0]["error"], "SHA-256 mismatch")

    def test_truncation_detected(self):
        self.successful_response(b"original")
        record = snapshot.capture("https://public.example/source", self.directory)
        (self.directory / record["snapshot_path"]).write_bytes(b"short")
        self.assertEqual(snapshot.verify(self.directory / "manifest.jsonl")["errors"][0]["error"],
                         "Byte-size mismatch")

    def test_http_failure_is_not_success(self):
        self.opener.open.side_effect = HTTPError("https://public.example/missing", 404, "Not Found", {}, None)
        record = snapshot.capture("https://public.example/missing", self.directory)
        self.assertEqual(record["status"], "failed")
        self.assertEqual(record["http_status"], 404)
        self.assertIsNone(record["retrieved_utc"])
        self.assertIsNone(record["sha256"])
        self.assertIsNone(record["snapshot_path"])
        self.assertFalse((self.directory / "objects").exists())
        logged = json.loads((self.directory / "manifest.jsonl").read_text())
        self.assertEqual(logged, record)
        self.assertEqual(snapshot.verify(self.directory / "manifest.jsonl"),
                         {"verified": 0, "failed_captures": 1, "errors": []})

    def test_transport_failure_is_not_success(self):
        self.opener.open.side_effect = URLError("mock connection failure")
        record = snapshot.capture("https://public.example/source", self.directory)
        self.assertEqual(record["status"], "failed")
        self.assertEqual(record["error_type"], "URLError")
        self.assertIsNone(record["http_status"])
        self.assertIsNone(record["snapshot_path"])

    def test_interrupted_body_is_logged_as_failure(self):
        response = self.successful_response()
        response.read.side_effect = IncompleteRead(b"partial", 20)
        record = snapshot.capture("https://public.example/source", self.directory)
        self.assertEqual(record["status"], "failed")
        self.assertEqual(record["error_type"], "IncompleteRead")
        self.assertIsNone(record["sha256"])
        self.assertEqual(json.loads((self.directory / "manifest.jsonl").read_text()), record)

    def test_partial_content_status_is_not_success(self):
        response = self.successful_response(b"partial")
        response.status = 206
        record = snapshot.capture("https://public.example/source", self.directory)
        self.assertEqual(record["status"], "failed")
        self.assertEqual(record["http_status"], 206)
        self.assertIsNone(record["snapshot_path"])

    def test_missing_content_length_is_allowed_and_encoding_preserved(self):
        response = self.successful_response(b"raw encoded bytes")
        del response.headers["Content-Length"]
        response.headers["Content-Encoding"] = "gzip"
        record = snapshot.capture("https://public.example/source", self.directory)
        self.assertEqual(record["status"], "success")
        self.assertEqual(record["content_encoding"], "gzip")
        self.assertEqual((self.directory / record["snapshot_path"]).read_bytes(), b"raw encoded bytes")

    def test_storage_failure_is_logged_as_failure(self):
        self.successful_response()
        with patch.object(snapshot, "store_bytes", side_effect=OSError("mock disk failure")):
            record = snapshot.capture("https://public.example/source", self.directory)
        self.assertEqual(record["status"], "failed")
        self.assertIsNone(record["sha256"])
        self.assertIsNone(record["retrieved_utc"])
        self.assertEqual(json.loads((self.directory / "manifest.jsonl").read_text()), record)

    def test_partial_or_oversized_body_is_not_success(self):
        response = self.successful_response(b"partial")
        response.headers["Content-Length"] = "100"
        record = snapshot.capture("https://public.example/source", self.directory)
        self.assertEqual(record["status"], "failed")
        self.assertIsNone(record["sha256"])
        self.successful_response(b"too large")
        record = snapshot.capture("https://public.example/source", self.directory, max_bytes=3)
        self.assertEqual(record["status"], "failed")

    def test_non_https_private_and_credential_urls_rejected_before_request(self):
        for url in ("http://public.example/a", "https://127.0.0.1/a", "https://localhost/a",
                    "https://user:secret@public.example/a", "https://public.example/a?token=secret"):
            with self.subTest(url=url):
                record = snapshot.capture(url, self.directory)
                self.assertEqual(record["status"], "failed")
                self.assertNotIn("secret", json.dumps(record))
        self.opener.open.assert_not_called()

    def test_dns_resolution_to_private_address_rejected(self):
        with patch.object(snapshot.socket, "getaddrinfo", return_value=[
                (socket.AF_INET, socket.SOCK_STREAM, 6, "", ("10.0.0.1", 443))]):
            record = snapshot.capture("https://public.example/source", self.directory)
        self.assertEqual(record["status"], "failed")
        self.opener.open.assert_not_called()

    def test_mixed_public_private_dns_rejected(self):
        with patch.object(snapshot.socket, "getaddrinfo", return_value=[
                (socket.AF_INET, socket.SOCK_STREAM, 6, "", ("93.184.216.34", 443)),
                (socket.AF_INET, socket.SOCK_STREAM, 6, "", ("10.0.0.1", 443))]):
            record = snapshot.capture("https://public.example/source", self.directory)
        self.assertEqual(record["status"], "failed")
        self.opener.open.assert_not_called()

    def test_insecure_redirect_rejected(self):
        handler = snapshot.PublicHTTPSRedirects()
        with self.assertRaises(snapshot.UnsafeURL):
            handler.redirect_request(Mock(), Mock(), 302, "Found", {}, "http://public.example/other")

    def test_manifest_path_escape_rejected(self):
        record = {"schema_version": 1, "status": "success", "snapshot_path": "../outside.bin",
                  "byte_size": 0, "sha256": hashlib.sha256(b"").hexdigest()}
        snapshot.append_record(self.directory, record)
        result = snapshot.verify(self.directory / "manifest.jsonl")
        self.assertEqual(result["verified"], 0)
        self.assertTrue(result["errors"])

    def test_verification_is_offline_and_missing_bytes_are_reported(self):
        self.successful_response()
        record = snapshot.capture("https://public.example/source", self.directory)
        self.opener.reset_mock()
        (self.directory / record["snapshot_path"]).unlink()
        with patch.object(snapshot.socket, "getaddrinfo", side_effect=AssertionError("Unexpected DNS")):
            result = snapshot.verify(self.directory / "manifest.jsonl")
        self.assertEqual(result["verified"], 0)
        self.assertEqual(len(result["errors"]), 1)
        self.opener.open.assert_not_called()

    def test_malformed_manifest_and_false_failure_claim_rejected(self):
        (self.directory / "manifest.jsonl").write_text("not JSON\n", encoding="utf-8")
        snapshot.append_record(self.directory, {"schema_version": 1, "status": "failed", "sha256": "false claim"})
        result = snapshot.verify(self.directory / "manifest.jsonl")
        self.assertEqual(result["verified"], 0)
        self.assertEqual(len(result["errors"]), 2)


if __name__ == "__main__":
    unittest.main()
