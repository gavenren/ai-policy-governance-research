# S018 PDF reading copy

[Read the PDF](paper.pdf). It preserves the [published Markdown manuscript](https://github.com/gavenren/ai-policy-governance-research/blob/215576a4132b214aeb3e51e1f84168cf354cf8b9/studies/2026-10-12-dividend-policy-comparability/paper.md) at commit `215576a4132b214aeb3e51e1f84168cf354cf8b9`. This is an AI-assisted complete-study draft. No human or journal peer review has occurred.

The seven-page copy has embedded serif fonts, page numbers, clickable source links and 15 bookmarks. The full ordered-text check covers 118 units, including all 56 table cells and six reference items. True minus signs and percentage signs are preserved. All pages were visually inspected. The second build is byte-identical. Source text is unchanged.

## Reproduce

Run from the repository root. Use Python 3.12 with ReportLab 4.4.9, pypdf 6.10.0 and pdfplumber 0.11.9. Supply four legally available Times New Roman font files. They are not redistributed. Environment details and font hashes are in the adjacent records. Replace the local Python and font paths as needed; different font files or library versions can change layout and bytes.

```sh
python scripts/render_s018_reading_copy.py studies/2026-10-12-dividend-policy-comparability/paper.md studies/2026-10-12-dividend-policy-comparability/output/pdf/paper.pdf --link-base https://github.com/gavenren/ai-policy-governance-research/blob/215576a4132b214aeb3e51e1f84168cf354cf8b9/studies/2026-10-12-dividend-policy-comparability/paper.md --font-regular '/System/Library/Fonts/Supplemental/Times New Roman.ttf' --font-bold '/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf' --font-italic '/System/Library/Fonts/Supplemental/Times New Roman Italic.ttf' --font-bold-italic '/System/Library/Fonts/Supplemental/Times New Roman Bold Italic.ttf'
python scripts/verify_s018_reading_copy.py studies/2026-10-12-dividend-policy-comparability/paper.md studies/2026-10-12-dividend-policy-comparability/output/pdf/paper.pdf --link-base https://github.com/gavenren/ai-policy-governance-research/blob/215576a4132b214aeb3e51e1f84168cf354cf8b9/studies/2026-10-12-dividend-policy-comparability/paper.md --output studies/2026-10-12-dividend-policy-comparability/output/pdf/text-check.json
```

Render a second PDF to a different destination and compare its SHA-256. Render all pages with Poppler `pdftoppm -png -scale-to 1300` and inspect them. The strict text check removes whitespace and applies Unicode NFC; it does not replace punctuation. Markdown list markers become bullets. Internal source links resolve against the publication commit. The renderer and verifier use the shared prose utilities without changing them.

`source-pin.json` records the source; `text-check.json` records exact text, table, link, font and bookmark checks; `layout-check.json` records visual checks and limits; `author-build-log.json` records the environment and repeat build; `release-manifest.json` records file hashes. The records do not claim human review or PDF accessibility certification.
