# Source capture and offline verification

`scripts/snapshot.py` uses only the Python standard library (Python 3.9 or later). Run it from the repository root. It captures only URLs explicitly passed to it; it does not crawl, publish, authenticate, consult browser state, or assess a source's legal status or reuse rights.

```sh
python3 scripts/snapshot.py capture https://example.org/public-document.pdf
python3 scripts/snapshot.py verify .local-sources/manifest.jsonl
python3 -m unittest discover -s tests -v
```

The URL above is illustrative, not a programme source. Use an actual public primary-source URL after checking access and terms. Never provide passwords, access tokens, signed private links, or other credentials. HTTPS, public IP/DNS targets, and public HTTPS redirects are required. User information in URLs and common credential-like query parameters are rejected. Environment proxy settings and authentication are not used. These checks reduce accidental local/private requests; they are not a security boundary against a hostile server or DNS rebinding. Use trusted public-source domains.

## What is retained

The default `.local-sources/` directory is ignored by Git. `--output-dir PATH` selects a different local directory; the caller must ensure that any custom location is also ignored if its contents have not been cleared for publication. The utility never stages, commits, pushes, or copies captures to a public directory.

- `objects/<sha256>.bin` holds the response body exactly as returned by the HTTP client, without parsing, text normalization, decompression, or OCR. This is the body, not a wire-level TLS/HTTP capture. Identical bodies share an object; a changed body gets a new object.
- `manifest.jsonl` appends one JSON record per attempt, including the actual UTC attempt/retrieval times, requested/final URLs, HTTP status, declared media type/content encoding, byte size, SHA-256, relative object path, and `success` or `failed` status.
- Every source starts with `rights` and `legal_status` set to `unassessed`. A researcher must separately record the authoritative rights/status assessment, assessor, time, reasoning, and source locator in the study evidence ledger. A successful HTTP request does not establish authenticity, legal force, source completeness, or redistribution permission.

Successful capture requires a completed 2xx response (excluding partial-content responses) and successful byte storage. HTTP/transport errors, interrupted bodies, rejected URLs, partial content, incomplete declared lengths, and oversized bodies are recorded as failures, without a successful snapshot path/hash/retrieval time. Rejected credential-bearing URLs are omitted from the log. Local inability to write the ledger is reported as an error; it cannot yield a durable failure record. The process exits nonzero if any requested capture fails. Each request has a 30-second socket timeout and a 50 MiB body limit by default; change them with `--timeout SECONDS` and `--max-bytes BYTES` only when needed. The socket timeout is not an overall download deadline.

The utility does not infer publication/adoption/effective dates, instrument versions, source authorship, claim locations, or legal status. Add those fields to the study's evidence ledger following [the research protocol](RESEARCH_PROTOCOL.md). Retain extracts and extracted text separately with their own hashes and transformation records. Do not mistake a login, error, or bot-challenge page returned with HTTP 200 for the intended source: inspect the captured content before using it.

## Verification and limits

`verify` operates offline. It checks each successful record against the retained file's byte count and SHA-256, rejects paths escaping the manifest directory, and reports failed acquisitions separately. It returns nonzero if any verification error occurs or no snapshot verifies. Recorded failed acquisitions remain failures even when verification of other snapshots succeeds. Verification demonstrates consistency of retained bytes with the ledger, not correctness of the source or authenticity of the ledger; independent publication/review of hashes can provide a separate reference.

The manifest uses relative object paths and can be moved with its `objects/` directory. Keep a single writer per manifest. Preserve prior records; corrections and updated source captures should have a dated study-ledger entry. Before publishing any evidence, inspect content and URLs for private information and confirm source-specific redistribution rights. Do not force-add `.local-sources/` as a way to bypass that assessment.

Tests use mocked HTTP responses and DNS resolution only. They cover byte-for-byte preservation, metadata, same-length corruption, truncation, HTTP/transport failure, incomplete/oversized bodies, rejected targets/redirects, and manifest path confinement. They do not contact or validate any live source and do not certify the validity of a study's research conclusions.
