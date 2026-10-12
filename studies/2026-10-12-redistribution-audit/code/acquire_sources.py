"""Retrieve pinned originals with verified TLS; refuse changed bytes or overwrites.

Requires curl. No full third-party source is written to the study directory.
The output directory must be supplied explicitly (use ignored local storage).
"""
import argparse
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--ids", nargs="*")
    args = parser.parse_args()
    destination = args.output.resolve()
    if destination == ROOT or ROOT in destination.parents:
        raise SystemExit("Use a directory outside the public study for full third-party originals")
    destination.mkdir(parents=True, exist_ok=True)
    records = list(csv.DictReader((ROOT / "sources/manifest.csv").open()))
    if args.ids:
        unknown = set(args.ids) - {r["capture_id"] for r in records}
        if unknown:
            raise SystemExit(f"Unknown capture IDs: {sorted(unknown)}")
        records = [r for r in records if r["capture_id"] in args.ids]
    log = []
    for row in records:
        out = destination / row["original_filename"]
        if out.exists():
            if hashlib.sha256(out.read_bytes()).hexdigest() != row["original_sha256"]:
                raise SystemExit(f"Refuse to overwrite changed local file: {out.name}")
            log.append({"capture_id": row["capture_id"], "status": "existing_hash_match"})
            continue
        with tempfile.NamedTemporaryFile(dir=destination, delete=False) as temp:
            temporary = Path(temp.name)
        retrieved = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        result = subprocess.run(["curl", "--fail", "--location", "--silent", "--show-error",
                                 "--max-time", "120", "--output", str(temporary),
                                 "--write-out", "%{http_code}\n%{url_effective}\n%{content_type}",
                                 row["requested_url"]], capture_output=True, text=True)
        data = temporary.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        if result.returncode != 0 or digest != row["original_sha256"]:
            failed = temporary.with_name(row["capture_id"] + "-unmatched-" + retrieved.replace(":", "") + ".bin")
            temporary.rename(failed)
            raise SystemExit(f"Acquisition failed or source bytes changed for {row['capture_id']}; retained unmatched bytes as {failed.name}; exit={result.returncode}; sha256={digest}. No expected source overwritten.")
        temporary.rename(out)
        log.append({"capture_id": row["capture_id"], "retrieved_utc": retrieved, "status": "download_hash_match",
                    "response": result.stdout, "sha256": digest, "bytes": len(data)})
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    (destination / f"acquisition-{stamp}.json").write_text(json.dumps(log, indent=2) + "\n")
    print(json.dumps(log, indent=2))


if __name__ == "__main__":
    main()
