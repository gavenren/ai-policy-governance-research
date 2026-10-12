# One-page policy brief: content and PDF checks

Date: 12 October 2026. These are checks before publication, not proof of a GitHub update.

## Files and source

- [Readable brief](POLICY_BRIEF.md): 510 whitespace-separated words.
- [Print-ready PDF](../output/pdf/policy-brief.pdf): one US Letter page, 612 by 792 points.
- Source: [A Secure Living After Wages](POLICY_PAPER.md), at commit `8cae385b76be12f1d32c1eea4411e431f03a3d2e`.
- Source paper SHA-256: `536518d8ceafaf05c18a76ab4c206f204bedf28399afdd2bf9f2e50bb3e59498`.
- Brief SHA-256: `4e510fa5aeb97f8ddceb2b92cb5360b100a01d670bc29896984262a70feb7a01`.
- PDF SHA-256: `23c0c805c161cc994a1e1672da29cdc6c5d9154b1079c7f32e62852af71ac8e2`.

The full paper and its 15 source studies are unchanged. The brief adds no new model, national estimate, or current-law claim.

## Checks completed

The [separate AI content review](reviews/policy-brief-review.md) found no material change needed. It checked the conditional scenario, early parallel work, immediate relief, funding distinctions, and evidence limits. This is not human peer review.

PDF checks confirmed one page and a complete text match with the Markdown, after removing formatting and the page footer. The full-paper link targets the exact source commit. All extracted characters fit inside the page. The rendered page was visually inspected: no clipped text, overlap, missing section, or unreadable symbol was found. The body uses 10.3-point type. The source note uses 8.8-point type.

Navigation links in the release were checked. The source paper hash still matches the approved version. Only the brief, PDF, renderer, check records, and navigation changes belong to this release.

## Build

Run `python3 scripts/render_policy_brief.py` with ReportLab available. The [renderer](../scripts/render_policy_brief.py) reads the brief Markdown and writes `output/pdf/policy-brief.pdf`. PDF text and page checks used pypdf and pdfplumber. The visual check used a Poppler rendering.

The brief is a short policy proposal. It does not establish a national payment amount, tax rate, implementation schedule, or probability of success.
