# S014 PDF reading copy

[Read the PDF](paper.pdf). This is a reading copy of the [published manuscript](https://github.com/gavenren/ai-policy-governance-research/blob/b5adf467eb27bd37d1d9f265b63c2178308d6657/studies/2026-10-12-compute-allocation/paper.md). Its source bytes were compared directly with that pinned public revision and match. The Markdown was not changed. This PDF does not change the study's complete-study draft status or supply human peer review.

The copy has 6 pages, serif body text, embedded-font vector equations, page numbers, 11 section bookmarks, and 16 unique clickable URLs. The source's disclosures remain visible. Paragraphs with tall inline math have more line spacing so subscripts do not meet the next line. Original punctuation and all literal currency signs are retained.

The dedicated builder is `scripts/render_math_reading_copy.py`; the earlier prose-only renderer and its outputs were not edited. Dependencies are in `scripts/requirements-math-reading-copy.txt`. The author used Python 3.12.14, ReportLab 4.4.9, Matplotlib 3.10.7 and pypdf 6.10.0. Times New Roman files came from the local operating system; STIX files came from Matplotlib. Font hashes are saved in `math-layout.json`. No standalone font files are included.

From the repository root, with the dependencies available:

```sh
python3 scripts/render_math_reading_copy.py studies/2026-10-12-compute-allocation/paper.md studies/2026-10-12-compute-allocation/output/pdf/paper.pdf --study-id S014 --source-commit b5adf467eb27bd37d1d9f265b63c2178308d6657
python3 scripts/verify_math_reading_copy.py studies/2026-10-12-compute-allocation/paper.md studies/2026-10-12-compute-allocation/output/pdf/paper.pdf
```

The builder's default font folder is `/System/Library/Fonts/Supplemental`; `--font-directory` can point to a local folder with the four named Times New Roman font files. It supports the exact Markdown and math subset used by these two papers. Unsupported math syntax stops the build. It does not install or call TeX, use a paid service, or contact the network. Source acquisition is a separate step.

`source-pin-check.json` records the public revision comparison. `text-math-check.json` records strict prose and table-text equality in order, all currency signs, links, bookmarks, embedded fonts, and separate equation checks. Each source formula is retained byte for byte in `math-layout.json`, with its source hash, vector glyph positions, fraction rules and page position. The verifier checks all 210 glyphs and 2 fraction rules in the final PDF, with a 0.0001-point tolerance for PDF coordinate serialization. Four S015 `\tag` commands become visible, right-aligned equation numbers; no other math commands are replaced.

`layout-verification.json` records the final page and equation-image inspection. All pages were rendered at 130 dpi and inspected in contact sheets; all equations were inspected in crops from those pages. The numerical tables in S015 received a full-size check. This authoring check is separate from the root agent's later publication review.

The PDF preserves visible mathematical structure, but copying an equation as text may not preserve its LaTeX syntax or reading order. Use the Markdown or formula ledger for editable equations. It is a reading copy, not a tagged-accessibility or PDF/UA certification.

PDF SHA-256: `1ddccfaedd1269ebd21709c9471d7a0a6248b3266f2b70fa52a5ebef0fd28bb9`.
Source SHA-256: `46361e8733a4ed4a1ce7eb4a4d9ee331e89565dc221c62382067bed9db008b33`.
