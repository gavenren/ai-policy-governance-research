"""Check source bytes and evidence metadata. This does not import a source model."""
import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalized(value):
    return " ".join(value.split())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--local", action="store_true")
    args = parser.parse_args()
    study = Path(__file__).resolve().parents[1]
    repo = study.parents[1]
    manifest = json.loads((study / "sources/manifest.json").read_text())
    csv_rows = list(csv.DictReader((study / "sources/manifest.csv").open()))
    assert [{k: str(v) for k, v in row.items()} for row in manifest] == csv_rows
    sources = {row["source_id"]: row for row in manifest}
    assert len(sources) == len(manifest)
    public_count = 0
    for row in manifest:
        assert len(row["sha256"]) == 64
        assert row["read_scope"] and row["rights"] and row["retrieval_end_utc"]
        if row["public_path"]:
            path = study / row["public_path"]
            assert path.stat().st_size == row["bytes"], path
            assert digest(path) == row["sha256"], path
            public_count += 1
        if args.local:
            path = repo / row["private_path"]
            assert path.stat().st_size == row["bytes"], path
            assert digest(path) == row["sha256"], path
            if row["text_path"]:
                path = repo / row["text_path"]
                assert path.stat().st_size == row["text_bytes"], path
                assert digest(path) == row["text_sha256"], path
    quotes = list(csv.DictReader((study / "evidence/short-quotes.csv").open()))
    words = Counter()
    for quote in quotes:
        row = sources[quote["source_id"]]
        count = len(quote["quote"].split())
        assert int(quote["words"]) == count
        words[quote["source_id"]] += count
        if args.local:
            path = repo / (row["text_path"] or row["private_path"])
            assert normalized(quote["quote"]) in normalized(path.read_text()), quote
    assert all(count <= 25 for count in words.values())
    assert (study / "vendor/four-pillars/LICENSE-CODE.md").read_bytes() == (
        study / "sources/snapshots/LICENSE-CODE.md"
    ).read_bytes()
    private_count = 0
    if args.local:
        inventory = json.loads((study / "logs/private-file-inventory.json").read_text())
        for row in inventory:
            path = repo / row["path"]
            assert path.stat().st_size == row["bytes"], path
            assert digest(path) == row["sha256"], path
            private_count += 1
    print(json.dumps({
        "status": "pass", "mode": "local" if args.local else "public",
        "source_entries": len(manifest), "public_source_files": public_count,
        "short_quotes": len(quotes), "private_files": private_count,
        "source_models_imported_or_executed": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
