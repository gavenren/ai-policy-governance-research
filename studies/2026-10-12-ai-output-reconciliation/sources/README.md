# Source access, versions, and rights

This folder describes the exact sources used for S016. It does not contain their full text or implementation. `manifest.json` is the detailed record; `manifest.csv` gives the same main fields in a table. Original source bytes remain in ignored local storage. Capture times are not publication dates or reading times.

| ID | Source and version | Reading scope |
| --- | --- | --- |
| B1 | Korinek and McKelvey, Bank of Canada WP 2026-20. Outer cover updated 18 June 2026; inner paper dated 8 May. | Definitions, main Tables 1–4 and notes, methods and accounting sections, selected discussion. |
| B2 | McKelvey, Brown, Rhymon and Korinek, author-hosted technical appendix, 27 April 2026. | Boundary and flow sections; 6.6, 7.3–7.5, 8.2–8.3. |
| P2 | The publisher appendix to PIIE WP26-9, 11 May 2026. | Relevant formulas, table notes and selected implementation details. |
| C1 | Publisher-linked replication ZIP. Internal release date not stated; README has an older title. | README, defaults, relevant power, spending, quantity and GDP functions. Read only by the evidence agent. |
| O1 | Schreyer and Zinni, OECD Statistics Working Papers 2018/06. Document dated 25 October 2018; replaces 24 October. | Introduction and Annex A paragraphs 55–61, especially 57–58 and footnote 14. |
| Z1 | Bell, sensitivity audit, cover 1 June 2026, version 02; posted 2 June. | All eight pages before the protocol. See the later Z1C check. |
| Z1C | The attached supporting package for Z1. | All 11 members listed and hashed; README, metadata, CSVs and interpretation read. No script or notebook. No execution. |
| Z3 | Bell, review and extension, cover 1 June 2026, version 03; posted 2 June. | All eight pages. The associated ZIP was not checked. |
| Z2 | Bell, *Beyond Task Exposure*, July 2026; posted 20 July. | Metadata, opening pages 1–4, page 24 accounting passage, and keyword search. Not the full paper. |

B2 and P2 have different hashes and cover dates. The relevant formulas and reported table cells agree in the sections read. No full-text equivalence is claimed. The latest-version API link associated with Z1 points to Z2, a paper with a different title and scope. This link does not establish that Z2 replaces the sensitivity audit.

The original screen's acquisition cutoff is 12 October 2026 at 18:08:07 UTC. The pivotal-source recheck at 18:14:59–18:15:00 UTC returned matching bytes for B1, B2, P2 and C1. Z1C was first captured at 18:15:59–18:16:02 UTC, after the protocol. It has no code to inspect or execute. Its parameter register lacks the quantity-bridge and annual-power cases. Its PDF matches Z1. This does not establish what unpublished calculation code the author used.

The OECD source is Paul Schreyer and Belen Zinni (2018), *Productivity measurement, R&D assets and mark-ups in OECD countries*, OECD Statistics Working Papers 2018/06, [DOI](https://doi.org/10.1787/fb3c2e6f-en). Annex A, paragraph 57, starts with an own-account R&D nominal value measured by costs. Paragraph 58 requires a separate assumption to divide that value into price and volume. Input-volume measurement implies zero measured productivity growth; footnote 14 allows an independent volume or price measure. This is prior accounting method. It does not select H100-operation weights over rental-service weights.

The source holds GPU-specific rental prices fixed. Spending can therefore be read as a fixed-price measure of heterogeneous rental services. Physical operations use different weights. Both can define a coherent training quantity after an algorithmic adjustment. The study compares these choices; the physical-price bridge is not an unconditional correction.

## Rights

The ZIP has no licence-named member. A text scan of all UTF-8 archive members, except resource forks, compiled Python and images, found no licence, copyright, permission or redistribution statement. That is not legal clearance. The third-party implementation and input datasets remain private. The public study contains original analysis code, numerical facts, source metadata, and short evidence extracts.

Zenodo metadata for Z1, Z2 and Z3 states CC BY 4.0. Their original PDFs remain private here. No redistribution licence was established for the other retained PDFs. Only short quotations are published in `../evidence/shortquotes.csv`. The quote check combines B2 and P2 as versions of one work. No original-work licence is added by this evidence package.

## Acquisition and checks

From the repository root, a fresh pivotal-source check can be made with:

```sh
python3 studies/2026-10-12-ai-output-reconciliation/code/source_retrieve.py --output .local-sources/s016-fresh-check
```

The output folder must be new. This retrieves B1, B2, P2 and C1 using normal public HTTPS requests and compares their bytes with the frozen manifest. Add `--ids O1 Z1 Z2 Z3` to retrieve the prior-work PDFs instead. The script does not run downloaded code. A changed source fails the comparison and must be recorded as a later version; it does not replace the frozen source.

The public metadata check uses `python3 studies/2026-10-12-ai-output-reconciliation/code/source_check.py`. Add `--local` in the original workspace to check all retained PDF/text bytes, archive members and quotes. The local check expects the manifest's private paths. It is an evidence check, not a numerical replication.

Root extracted B1/B2 with pypdf 6.10.0 under Python 3.12.14 and `=== PDF PAGE n ===` markers. The exact extraction time was not logged. Both existing text hashes are retained. The independent evidence agent extracted O1/P2/Z1/Z2/Z3 with the same pypdf version and `--- PDF PAGE n ---` markers; their original acquisition records preserve the times. Some font warnings appeared in the first capture batch. The selected passages were readable; no full visual page review is claimed.
