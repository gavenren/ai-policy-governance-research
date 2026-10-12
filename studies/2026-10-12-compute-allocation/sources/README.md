# Source access and rights

The manifest records requested and final URLs, actual acquisition times, byte lengths, SHA-256 hashes, retained local paths and extraction details. Local `.local-sources/` paths are ignored and are not a claim that the full files are in GitHub. No source PDF or full webpage is redistributed. The public evidence extract supplies narrow quotations, exact locators and researcher mathematical transcriptions. It is not a substitute for the full paper.

Retrieve C1–C3 from their requested URLs with an ordinary HTTPS client. Keep original bytes, verify their SHA-256 values against the manifest, and extract each page with pypdf 6.10.0 using the marker `=== PDF PAGE N ===` before that page's text. Do not silently overwrite a changed document; retain it as a separate version. The offline analysis needs only the public JSON case file and does not require network access or external PDFs.

C5/C6 are dynamic author pages. Their extracted text uses Python html.parser, excluding script/style text. This may differ from rendered layout. C4 follows the latest-version endpoint; it is a dated check, not a promise of permanent currency. Q1/Q2 are read-only public repository checks. No new reuse licence is selected.
