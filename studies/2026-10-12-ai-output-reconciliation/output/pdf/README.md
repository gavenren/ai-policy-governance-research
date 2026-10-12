# S016 PDF reading copy

`paper.pdf` is a seven-page reading copy of the unchanged, published manuscript. It keeps the source's complete-study draft and no-human-review disclosures. It does not change the study's review status or conclusions.

The source is pinned to commit `49131a42f9c92820d2146701e31b3f348c39276e`. Its SHA-256 is `e45fb9bdce6b0d5f4bd6796118ac0e09eeb0ea08c1266014d8916c73aeca20e8`. `source-pin-check.json` records an exact-byte comparison with that public file. The PDF source link and relative manuscript links use that commit.

## Reproduction

Run from the repository root with Python 3.12, ReportLab 4.4.9, pypdf 6.10.0 and pdfplumber 0.11.9. Supply the fonts locally; the repository does not distribute font files. The four font hashes are in `notation-link-check.json`.

```sh
python scripts/render_s016_reading_copy.py \
  studies/2026-10-12-ai-output-reconciliation/paper.md \
  studies/2026-10-12-ai-output-reconciliation/output/pdf/paper.pdf \
  --link-base https://github.com/gavenren/ai-policy-governance-research/blob/49131a42f9c92820d2146701e31b3f348c39276e/studies/2026-10-12-ai-output-reconciliation/paper.md \
  --font-regular '/System/Library/Fonts/Supplemental/Times New Roman.ttf' \
  --font-bold '/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf' \
  --font-italic '/System/Library/Fonts/Supplemental/Times New Roman Italic.ttf' \
  --font-bold-italic '/System/Library/Fonts/Supplemental/Times New Roman Bold Italic.ttf'

python scripts/verify_s016_reading_copy.py \
  studies/2026-10-12-ai-output-reconciliation/paper.md \
  studies/2026-10-12-ai-output-reconciliation/output/pdf/paper.pdf \
  --link-base https://github.com/gavenren/ai-policy-governance-research/blob/49131a42f9c92820d2146701e31b3f348c39276e/studies/2026-10-12-ai-output-reconciliation/paper.md \
  --font-dir /System/Library/Fonts/Supplemental \
  --output studies/2026-10-12-ai-output-reconciliation/output/pdf/notation-link-check.json
```

The S016 wrapper uses the unchanged prose renderer. It changes only the five-column table widths and makes bare reference URLs clickable. Appendix A keeps its original plain notation, including underscores, carets, brackets and Unicode minus signs. No LaTeX or mathematical typesetting was added. A second local build produced identical PDF bytes.

## Verification

The checker compares every paragraph, heading and table cell in source order. It removes only whitespace and applies Unicode NFC; punctuation stays unchanged. All 115 units passed, including 53 table cells. All 19 link occurrences have annotations; two wrapped links use extra annotations, for 21 in total. The 14 distinct targets and 14 bookmarks passed. Text lies within the page and horizontal margins. All manuscript fonts are embedded. ReportLab declares an unused Helvetica resource.

The authoring AI agent inspected all seven Poppler PNG renders at full size and in two contact sheets. It checked the three tables and plain-text appendix closely. It found no cut text, overlap, missing glyphs or table defects. `layout-verification.json` records the 130-dpi render hashes and observations. These checks do not cover every viewer or printer. Each remote link destination was not reopened. The PDF does not claim PDF/UA or semantic math support.

`authoring-log.json` records versions, the identical second build, one resolved record-generation failure, and byte checks for the four earlier reading copies. `release-manifest.json` pins the source, scripts and output records. The Markdown, base renderer and earlier PDFs were not changed. The root agent will perform the separate release review and publication.
