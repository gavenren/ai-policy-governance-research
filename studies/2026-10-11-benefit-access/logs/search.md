# Search and source-reading record

Recorded 2026-10-11T21:07:50Z. Search service: built-in public web search. No date filter was applied. The search tool did not expose exact UTC event timestamps; they cannot be reconstructed to the second. Searches occurred on 11 October 2026 before the source cutoff. Exact UTC acquisition times for the retained bytes are in the acquisition log and manifest. This timing limitation is disclosed rather than replaced with invented precision.

## Exact search queries

1. `administrative burden benefit take up appeals welfare algorithm automated benefits research original Herd Moynihan`
2. `automatic advance benefits appeals queue benefit payment delay research social protection`
3. `site.nber.org take up welfare programs administrative burden benefit applications experiment`
4. `benefit provisional payment pending appeal automated welfare advance payments model liquidity`
5. `Anunrojwong information design congested queue social services 2023`
6. `site.gov.uk universal credit first payment advances repayment report National Audit Office 2020`
7. `site.arxiv.org benefits advances queue review payment appeals liquidity model`
8. `"dp17839" welfare prepayments`
9. `"benefit" "advance" "queue" "review" payment research liquidity`

Inclusion: primary research or an official document with a direct connection to queue access, automated benefit delivery, or payment during review. Exclusion: search snippets as evidence, press accounts where primary sources were available, forums, generic medical claims billing, and wholesale payment-system research outside household benefit review.

## Candidates and decisions

| Candidate | Decision and reason |
|---|---|
| Daw, Pache, Zhou, arXiv 2605.15165 | Retained B01; nearest benefit-queue model; read introduction, related work, model description, and operational comparison |
| Giannella et al., NBER 31239 | Retained B02; author abstract read; narrow mechanism claim only; full paper not read |
| Bennett, Currie, Podoletz | Retained B03; read abstract, sample/method, findings, discussion; source for automated administrative burden |
| World Bank delivery-system brief | Retained B04; read strategy; already links grievance and payment systems |
| Anunrojwong, Iyer, Manshadi, arXiv 2005.07253v3 | Followed the reference in B01; retained B05; read introduction, model, and stated findings |
| DWP advances model assessment, July 2026 | Retained B06; read assessment and relevant statistical-method sections; official self-report, not an independent validation |
| Vethaak et al., IZA 17839 | Retained B07; read introduction, institutional setting, section 2.3, and data/method discussion; nearest advance-payment study |
| Currie 2004 and Ko/Moffitt 2022/2024 take-up reviews | Screened but not retained; useful broad context, no additional pivotal claim required |
| NAO Universal Credit advances fraud 2020 | Opened official summary; not retained; this paper makes no real fraud-prevalence claim |
| UK and Australian payment-pending-review rules; SSA guidance | Screened; not used; a cross-jurisdiction legal comparison was outside scope |
| Wholesale payments queueing and liquidity papers | Screened; different settlement mechanism and population; not used to claim novelty |
| Forum discussions and media incident accounts | Excluded as evidence |

Search scope was limited, English-language, and not systematic. Citation following focused on B01 and the IZA prepayment paper. No claim of a complete literature census is made. The repository's S004 protocol and README were read for distinctness. The separate research repository was checked by the lead agent for programme scope; S007 does not claim its own new full duplicate audit.

## Access and extraction notes

Web-tool PDF reads failed for both IZA PDF URLs and the NBER PDF. The IZA publisher page was accessible. The independent public HTTPS acquisition then captured all seven selected sources successfully. The NBER retained item is its landing page, not its full PDF. TLS checks remained enabled.

PDF text extraction used pypdf 6.10.0. It emitted ten warnings about incorrect PDF object offsets and repaired the read. Text contains visible ligature and punctuation artifacts. The selected short quotation is present after whitespace normalization. No OCR was performed. No equation or empirical coefficient from the PDF drives the synthetic model.

The capture ledger preserves initial author/date placeholders at acquisition. The verified manifest corrects B03 to three authors and its exact online date, and B06 to 9 July 2026. B04 has no verified visible publication date; its URL date is identified separately. No original capture was replaced.
