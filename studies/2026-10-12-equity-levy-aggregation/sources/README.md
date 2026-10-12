# Sources, access and rights

The [JSON ledger](manifest.json) and [CSV ledger](manifest.csv) contain the same 13 records. P1 is the essay; G1 is its code repository's revision metadata; F1, H1 and M1 are close prior work; V1–V8 are unchanged source-repository files. The [evidence extract](evidence.md) is a narrow record of passages and limitations, not a full snapshot of the essay or research papers.

**Evidence cutoff: 2026-10-12T17:46:29.147619Z.** This is the last completed network retrieval among the material source captures in this ledger. The source checkout was already retained at 2026-10-12T17:42:24.388523Z. The clone start and end were not separately timed. The later source-package creation time is not presented as a retrieval time. The [acquisition log](../logs/source-acquisition.json) preserves those distinctions. The separate feasibility search ended at 2026-10-12T17:48:45Z; see [the search record](../reviews/search.md).

## Licensed source code and documents

The `vendor/` directory contains an unchanged, partial copy of `spitis/who-owns-ai-economy` at commit `1573447e94b21f0da8fbaa1e9cf78823a5e2663e`. Copyright (c) 2026 Silviu Pitis. The original [MIT licence](vendor/LICENSE) is included. It permits the copy subject to its notice conditions. This upstream licence applies to the copied files. It does **not** select a licence for the new study.

The copied files are the repository README and requirements, the licence, and the Figure 3 model and its README, DATA, SOURCES and BURDEN documents. This is a partial evidence copy, not a full upstream checkout. Links in those unchanged documents may refer to Figure 4, rendering files, or image assets not copied here. Use each ledger record's pinned upstream URL for the complete original context. Do not edit the vendor files to repair those links. No upstream model was executed during preparation of this evidence package.

## Other originals and extraction

Full essay HTML, GitHub API JSON, and research PDFs remain in ignored `.local-sources/` storage. Public availability was not treated as a redistribution licence. The ledger records original and extracted-text hashes separately. PDF text was extracted with pypdf 6.10.0, page by page, with `=== PDF PAGE N ===` markers and no OCR. HTML extraction used Python's `html.parser`, omitted script and style text, and does not preserve rendered layout.

To obtain those files, use the ledger's requested URL with an ordinary HTTPS client, keep the returned bytes, and compare their SHA-256 values. Record redirects and retrieval times. A changed file must be kept as a new capture, not used to replace the pinned version silently. The source repository can be obtained from its recorded HTTPS clone URL and checked out at the stated commit. No network access is needed for the study's saved inputs or the public-copy check below.

## Validation

From the repository root:

```text
python3 studies/2026-10-12-equity-levy-aggregation/code/check_sources.py
python3 studies/2026-10-12-equity-levy-aggregation/code/check_sources.py --repository .
```

The first command checks the two ledger formats, all eight public vendor files, required metadata, and quotation bookkeeping. The second also checks retained local source bytes, extracted texts, acquisition logs, the exact essay quote and the captured revision. It does not fetch or execute source code. Missing local originals are an explicit error in that mode, not a failed offline model reproduction.

[quotations.json](quotations.json) records one nine-word essay quotation. No prose from F1, H1 or M1 is quoted. The main paper should paraphrase those sources. Any later quotation must be counted across the paper and evidence extract; keep each non-code copyrighted source within 25 words. The full MIT-licensed vendor files are separately authorized copies, with their licence retained.
