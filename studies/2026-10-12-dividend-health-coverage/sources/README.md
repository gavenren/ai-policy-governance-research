# Source record

[manifest.json](manifest.json) is the full record. [manifest.csv](manifest.csv) is a reading index. The source IDs are stable. The private files remain at their original ignored paths so their initial acquisition times are not lost. The initial capture cutoff is 2026-10-12T18:44:08Z. Later checks are labeled in [the web ledger](../logs/web-captures.json).

Original PDFs and HTML were fetched with a normal HTTPS request. PDF extraction used pypdf 6.10.0 in Python 3.12.14, with page markers and no OCR. HTML text extraction used Python's HTMLParser and omitted script and style text. Retained web-reader responses are explicitly labeled; they are not original server bytes. The eCFR direct responses were challenge pages, and the SSA and NYC direct requests failed. They must not be used as legal captures. Successful web-reader text is retained separately.

P1 and P1A were acquired by the separate feasibility reviewer from public Europe PMC endpoints. P2 was retained in an earlier screen. Original acquisition times and hashes are preserved. The precise original extraction times for these imported texts were not recorded. No paid source, credential bypass or author request was used.

Official US federal texts are public documents. Scholarly and city-authored material has separate rights. The ledger records those limits. Full captures remain private. The public evidence contains only short source-linked quotations, each below 25 words per source. The source check tests the hashes, quote counts and local text matches; it does not decide legal meaning.

Run `python3 code/check_sources.py` from this study folder for the public checks. Add `--local` only where the ignored captures exist. These checks do not execute the illustrative case analysis.
