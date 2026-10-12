# S013 PDF reading copy

This is a reading copy of the unchanged [manuscript](../../paper.md). It adds typography, running page labels, page numbers, section bookmarks and clickable links. The first-page link points to the [exact source version](https://github.com/gavenren/ai-policy-governance-research/blob/40a4eab496feace4373374a43a34a5e5144798d5/studies/2026-10-12-supplier-continuity/paper.md). Relative manuscript links use that same commit. Source punctuation is preserved.

The copy has 8 letter-size pages. Body text is 11-point Times New Roman with 14.4-point line spacing. Tables use 9.4-point text and remain on one page. The title page and footers keep the AI-draft disclosure visible. Font subsets are embedded; font files are not included in the repository.

## Rebuild

From the repository root, use Python with the versions in `scripts/requirements-reading-copy.txt`. Supply locally available, licensed font files. The command below uses the macOS font filenames used for this copy. A different font or package version can change the layout and PDF hash.

```sh
READING_FONT_DIR='/System/Library/Fonts/Supplemental'
python3 scripts/render_reading_copy.py \
  studies/2026-10-12-supplier-continuity/paper.md \
  studies/2026-10-12-supplier-continuity/output/pdf/paper.pdf \
  --study-id S013 \
  --link-base 'https://github.com/gavenren/ai-policy-governance-research/blob/40a4eab496feace4373374a43a34a5e5144798d5/studies/2026-10-12-supplier-continuity/paper.md' \
  --font-regular "$READING_FONT_DIR/Times New Roman.ttf" \
  --font-bold "$READING_FONT_DIR/Times New Roman Bold.ttf" \
  --font-italic "$READING_FONT_DIR/Times New Roman Italic.ttf" \
  --font-bold-italic "$READING_FONT_DIR/Times New Roman Bold Italic.ttf"
python3 scripts/verify_reading_copy.py \
  studies/2026-10-12-supplier-continuity/paper.md \
  studies/2026-10-12-supplier-continuity/output/pdf/paper.pdf \
  --study-id S013 \
  --link-base 'https://github.com/gavenren/ai-policy-governance-research/blob/40a4eab496feace4373374a43a34a5e5144798d5/studies/2026-10-12-supplier-continuity/paper.md' \
  --output studies/2026-10-12-supplier-continuity/output/pdf/text-check.json
```

The builder supports only the simple Markdown used by these two papers. It is not a general Markdown or mathematics renderer. The PDF uses fixed internal creation metadata for repeatable builds. The actual check time is in the verification files.

## Verification

The [text check](text-check.json) records an exact comparison after whitespace removal and Unicode NFC normalization. It checks every heading, paragraph, disclosure and table cell in source order. A separate plain-source conversion checks the parser. It also checks link targets, bookmarks and embedded manuscript fonts. The [layout record](layout-verification.md) reports the page inspection and its limits.

- Manuscript SHA-256: `a6d2016d06fcfe7f271544f87cf301dd1f002acb007e447e476bacb268d3265d`
- PDF SHA-256: `912777cbe8fb2743e0fb9a465ccd6dbd54829ccfa9d5d3052f4ea7c3eef5909e`
- Source commit: `40a4eab496feace4373374a43a34a5e5144798d5`

No manuscript text, study result or source evidence was changed for this copy.
