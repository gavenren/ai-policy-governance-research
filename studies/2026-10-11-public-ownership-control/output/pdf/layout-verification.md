# S010 PDF layout verification

**Check completed:** 2026-10-12T17:25:14.446177Z

**Reviewer:** The AI agent that built this reading copy. This is the first layout check. It is not independent human review. A separate release inspection can use the saved page images.

The final PDF has 11 pages. Every page was rendered with Poppler `pdftoppm` 26.05.0 at 110 dpi. I inspected all pages in contact sheets. I also inspected full-scale table crops on pages 7. I found no clipped text, overlap, missing glyph, black square, broken table, or heading left without following text. The body, page labels, source links and disclosure remain legible. Paragraphs can continue on the next page; all tables remain whole.

The first S013 layout split two tables across pages and repeated their headers. The strict text check detected the repeated text. The builder was changed to keep these short tables together. The final text check permits no repeated or omitted source text. S010's bytes did not change after that adjustment.

The final check matches 128 source units in order, including 15 table cells. It verifies 20 bookmarks and 27 distinct clickable URLs. All visible glyphs use Times New Roman subsets. A clean second build has exactly the same PDF bytes. The local manuscript bytes also match the source file at the pinned Git commit.

The manuscript's Unicode punctuation was retained to meet the instruction to preserve its content. The selected font renders those characters correctly. The PDF was not tested for PDF/A, accessibility tagging, screen-reader order, print output, or every PDF viewer. Links were checked as PDF annotations; this layout check did not reopen every remote destination. Source assertions retain the manuscript's original evidence cutoff.

The retained page images, contact sheets, table crops, font hashes and layout bounds are in the ignored local directory `.local-verification/pdf-reading-copies/`. They are review material, not a new source corpus. The final public text check is `text-check.json` beside the PDF.

## Exact output

- Manuscript SHA-256: `758973b40876822fd759fa8a7adb40518d23cd574d55a30c279375357d5a735f`
- PDF SHA-256: `4461a42c1a44cfd0254048b842a59cf9c8f770a2937f7d9fe3bc4550a7d1122e`
- Python: 3.12.14; ReportLab: 4.4.9; pypdf: 6.10.0; pdfplumber: 0.11.9.
- Source commit: `40a4eab496feace4373374a43a34a5e5144798d5`.

## Font inputs

No standalone font file is published. These hashes identify the local inputs used for exact reproduction.

| Font file | SHA-256 |
|---|---|
| `Times New Roman Bold Italic.ttf` | `906157e8294fdf168d83002eaabde01c2d30fc3f44977be89e33fa22f262002a` |
| `Times New Roman Bold.ttf` | `50f5b1f27b7d34621090e437e8b1dd4510a22d2823fc876b3286bed327b64bbb` |
| `Times New Roman Italic.ttf` | `7bb99c3a67697fbce15ab66d806d9a2151432ce1dab2eaba4156e1251da486c0` |
| `Times New Roman.ttf` | `f3b4ffff71c2a0c7227d37497683b2498fb2d0a4e8beae26f022e3ccfcaabfa3` |

## Builder inputs

- `scripts/render_reading_copy.py`: `3ca8aa991c31fff407e010fe777697ecbc2fb5bfc931a8de02b80463cc472747`
- `scripts/verify_reading_copy.py`: `754cb6a6b3f09825da99484d4edeb841e2ac0381ece25f44900765830c491ad5`
- `scripts/requirements-reading-copy.txt`: `24f1b57cf10a238b47567905cf4864c28628eb297d1586e5b3004dbcebdaa4c4`
