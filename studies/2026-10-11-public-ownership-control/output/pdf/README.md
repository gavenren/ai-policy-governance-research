# S010 PDF reading copy

This is a reading copy of the unchanged [manuscript](../../paper.md). It adds typography, running page labels, page numbers, section bookmarks and clickable links. The first-page link points to the [exact source version](https://github.com/gavenren/ai-policy-governance-research/blob/40a4eab496feace4373374a43a34a5e5144798d5/studies/2026-10-11-public-ownership-control/paper.md). Relative manuscript links use that same commit. Source punctuation is preserved.

The copy has 11 letter-size pages. Body text is 11-point Times New Roman with 14.4-point line spacing. Tables use 9.4-point text and remain on one page. The title page and footers keep the AI-draft disclosure visible. Font subsets are embedded; font files are not included in the repository.

## Rebuild

From the repository root, use Python with the versions in `scripts/requirements-reading-copy.txt`. Supply locally available, licensed font files. The command below uses the macOS font filenames used for this copy. A different font or package version can change the layout and PDF hash.

```sh
READING_FONT_DIR='/System/Library/Fonts/Supplemental'
python3 scripts/render_reading_copy.py \
  studies/2026-10-11-public-ownership-control/paper.md \
  studies/2026-10-11-public-ownership-control/output/pdf/paper.pdf \
  --study-id S010 \
  --link-base 'https://github.com/gavenren/ai-policy-governance-research/blob/40a4eab496feace4373374a43a34a5e5144798d5/studies/2026-10-11-public-ownership-control/paper.md' \
  --font-regular "$READING_FONT_DIR/Times New Roman.ttf" \
  --font-bold "$READING_FONT_DIR/Times New Roman Bold.ttf" \
  --font-italic "$READING_FONT_DIR/Times New Roman Italic.ttf" \
  --font-bold-italic "$READING_FONT_DIR/Times New Roman Bold Italic.ttf"
python3 scripts/verify_reading_copy.py \
  studies/2026-10-11-public-ownership-control/paper.md \
  studies/2026-10-11-public-ownership-control/output/pdf/paper.pdf \
  --study-id S010 \
  --link-base 'https://github.com/gavenren/ai-policy-governance-research/blob/40a4eab496feace4373374a43a34a5e5144798d5/studies/2026-10-11-public-ownership-control/paper.md' \
  --output studies/2026-10-11-public-ownership-control/output/pdf/text-check.json
```

The builder supports only the simple Markdown used by these two papers. It is not a general Markdown or mathematics renderer. The PDF uses fixed internal creation metadata for repeatable builds. The actual check time is in the verification files.

## Verification

The [text check](text-check.json) records an exact comparison after whitespace removal and Unicode NFC normalization. It checks every heading, paragraph, disclosure and table cell in source order. A separate plain-source conversion checks the parser. It also checks link targets, bookmarks and embedded manuscript fonts. The [layout record](layout-verification.md) reports the page inspection and its limits.

- Manuscript SHA-256: `758973b40876822fd759fa8a7adb40518d23cd574d55a30c279375357d5a735f`
- PDF SHA-256: `4461a42c1a44cfd0254048b842a59cf9c8f770a2937f7d9fe3bc4550a7d1122e`
- Source commit: `40a4eab496feace4373374a43a34a5e5144798d5`

No manuscript text, study result or source evidence was changed for this copy.
