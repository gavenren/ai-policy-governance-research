# S017 PDF reading copy

`paper.pdf` is a seven-page reading copy of the unchanged published manuscript. The source is pinned to commit `1eb10be858df3e0069fa7c7f7722c548d040f865`, with SHA-256 `8585fd496381b90345db63d8b0e40bc67fbe063eb8c0f6456613a69a6b5158a5`. `source-pin-check.json` records an exact-byte comparison with the public file. The PDF source link and relative manuscript links resolve within this commit.

The reading copy retains the complete-study draft and no-human-review disclosures. It does not change the manuscript's review status. A separate S017 wrapper uses the unchanged prose renderer. It gives the two tables suitable column widths and converts the nine Markdown reference-list markers into hanging bullet paragraphs. All reference text is preserved. Plain symbols in the prose remain plain text; no math parser or substitution is used.

## Reproduction

Run from the repository root with Python 3.12, ReportLab 4.4.9, pypdf 6.10.0 and pdfplumber 0.11.9. Supply the four local Times New Roman files; this repository does not distribute font files. Their hashes and software versions are in `authoring-log.json`.

```sh
python scripts/render_s017_reading_copy.py \
  studies/2026-10-12-dividend-health-coverage/paper.md \
  studies/2026-10-12-dividend-health-coverage/output/pdf/paper.pdf \
  --link-base https://github.com/gavenren/ai-policy-governance-research/blob/1eb10be858df3e0069fa7c7f7722c548d040f865/studies/2026-10-12-dividend-health-coverage/paper.md \
  --font-regular '/System/Library/Fonts/Supplemental/Times New Roman.ttf' \
  --font-bold '/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf' \
  --font-italic '/System/Library/Fonts/Supplemental/Times New Roman Italic.ttf' \
  --font-bold-italic '/System/Library/Fonts/Supplemental/Times New Roman Bold Italic.ttf'

python scripts/verify_s017_reading_copy.py \
  studies/2026-10-12-dividend-health-coverage/paper.md \
  studies/2026-10-12-dividend-health-coverage/output/pdf/paper.pdf \
  --link-base https://github.com/gavenren/ai-policy-governance-research/blob/1eb10be858df3e0069fa7c7f7722c548d040f865/studies/2026-10-12-dividend-health-coverage/paper.md \
  --output studies/2026-10-12-dividend-health-coverage/output/pdf/text-check.json
```

A second local build produced identical PDF bytes. To preserve the saved output and check record, use a new local destination when reproducing.

## Verification

The strict ordered-text check covers 95 units: 13 headings, 38 paragraphs, 35 table cells and nine reference items. It removes whitespace and applies Unicode NFC. The only list change is the presentation marker: Markdown hyphens become bullet glyphs. All source words and other punctuation remain unchanged.

All 24 source-link occurrences are represented. Wrapped links produce 26 PDF annotations in total, with 23 distinct targets. All 12 bookmarks match the source heading order. Annotation rectangles and all text characters lie within the page and horizontal margins. All manuscript fonts are embedded; ReportLab declares an unused Helvetica resource.

The authoring AI agent rendered all seven pages to PNG with Poppler at 130 dpi and inspected each page at full size. It checked the three-column status table, the five-column illustrative table and the reference list closely. It found no cut text, table overlap or missing glyphs. `layout-verification.json` records each image hash and the observations. This checks the saved renders, not every PDF viewer or printer. URI targets were checked without reopening every external site. No PDF/UA or semantic-math support is claimed.

`authoring-log.json` retains the resolved preview-build failure, the identical second build and checks of earlier reading-copy bytes. `release-manifest.json` pins the source, scripts and output records. The base renderer, manuscript and prior PDFs were not changed. The study README was changed only to add links to this reading copy and its verification record. The root agent performs the separate release review and publication.
