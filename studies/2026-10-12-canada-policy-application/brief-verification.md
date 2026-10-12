# Canada policy brief: content and page checks

Date: 12 October 2026. These checks were completed before publication. They do not by themselves prove a GitHub update.

## Source and files

- [Brief](policy-brief.md): 543 whitespace-separated words.
- [Print version](output/pdf/canada-policy-brief.pdf): one US Letter page, 612 by 792 points.
- Source: [Canada analysis](paper.md), at commit `3edc96d95770b48dcc81c37af85c9064ef32a743`.
- Source paper SHA-256: `af4a481c547aec1bfa8d897bc437202407ba3971d8106e8340cc32f2af2e2af9`.
- Brief SHA-256: `4a19be01b376469aa21cd4670ab31e0e7ef8c2eac5776d143c1a7e0abbcee383`.
- PDF SHA-256: `b472c53a0944841af90cc22e1f1760576f8678cdf1701999740b050e86d82597`.

The full Canada paper, inputs, calculation model, results, and prior reviews are unchanged. The brief adds no new estimate or current-law claim.

## Completed checks

The [separate AI content review](reviews/brief-review.md) found no required change. It checked the cost totals, proposed taxes, receipt assumptions, payment rules, dates, reserve, emergency route, and limits. This is not human peer review or an official costing.

The PDF has exactly one page. Its full body text matches the Markdown after removing markup and normalizing whitespace. The page footer was excluded from that comparison. The source link points to the exact published source commit. All text characters fall within the page boundary.

The rendered page was visually inspected. No clipped text, overlap, missing section, broken symbol, or unreadable line was found. The body uses 10.3-point type. The source note uses 8.8-point type. The title, section labels, numbered actions, and footer have clear spacing.

Local navigation links were checked. The source paper still has the recorded hash. Only the brief, PDF, renderer, new review, this record, and two README links belong to this release.

## Rebuild

From this study folder, run `python3 code/render_brief.py` with ReportLab installed. The renderer reads the brief Markdown and writes the final PDF. It uses stable PDF metadata for repeatable output. Page and text checks used pypdf and pdfplumber. The visual check used a Poppler rendering.

The brief retains a fixed 2026 benchmark and proposed dates. It does not establish achievable tax receipts, an adequate benefit level, delivery readiness, or a date for widespread wage loss.
