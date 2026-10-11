# Source provenance

Evidence cutoff: **2026-10-11T21:03:17Z**. Seven primary sources support the paper. The JSON ledger records identity, publication-date precision, exact acquisition time, requested and final URLs, media type, byte count, SHA-256, extraction method and hash, relevant passages, rights, and limits.

`snapshots/` contains selected short attributed extracts, not complete source snapshots. Every quotation was matched against the retained extracted text. Every quote contains fewer than 25 words. Original PDF, HTML, JSON, and ZIP bytes remain in ignored `.local-sources/dividend-reserves/`. No full third-party work is distributed here.

Sources S1, S2, S3, S5, and S6 were downloaded by curl with normal TLS verification. The local text was extracted with pypdf 6.10.0, with a page label before each page. No OCR was used. Source S4 used Python HTMLParser. S7 used Python zipfile to read the README and model-specification members without running their code. No private account access was used.

Run the optional acquisition recipe from the repository root:

```sh
python3 studies/2026-10-11-dividend-reserves/code/acquire_sources.py
```

This needs network access and curl. It saves time-stamped original bytes under the ignored source directory and reports unsuccessful responses. It does not overwrite the evidence ledger or alter the paper. A later capture may differ from the retained hashes. Such a difference needs review before updating the evidence.

The ZIP recipe URL is recorded in S7's ledger entry. That package is the evidence source; the blocked SSRN HTML response is only an access-failure record. The Zenodo metadata says CC BY 4.0, but the package README says its licence is to be set. This rights conflict is unresolved. Only a short attributed extract is published.

This study does not compare binding legal instruments. S4 is an issuer's description. It does not establish independent verification of Alaska law, appropriation authority, or current account balances. Thus, no separate legal instrument ledger is used.
