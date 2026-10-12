# Separate critical review: S016

Review started: 2026-10-12T18:22:33.975220+00:00. Review completed: 2026-10-12T18:29:47.308229+00:00.

The frozen paper can proceed after one small reporting correction. I found no unresolved calculation or interpretation error in the stated four-case comparison. This decision covers the files listed in [verification-record.json](verification-record.json). It does not approve later substantive changes.

## Reviewer role and scope

A separate AI agent made this review. The agent had shared task context. Before the numerical work, the agent read selected primary-source material for feasibility and gave wording advice. The agent did not write the central analysis, manuscript, inputs or source-evidence package. This review is not blind or human peer review.

I read the frozen manuscript, dated protocol and addenda, guides, evidence records, raw aggregate inputs, analysis, tests, source adapter and saved results. I then executed the public reconstruction in a private copy. I did not execute the full original model again. I checked its retained source members and aggregate exports against the archive and execution records. My separate calculation imports neither the study analysis nor the original source functions.

The reviewed paper SHA-256 is `3eb26000443b7c6c0b27eea4300e7221892aafd3daaa707174242f836f25a182`. The protocol SHA-256 is `f0d6c33785243a6220af8c9f4ee998b31a6a4eb7964006dc1d1f5c4ebdd6ce60`. The analysis SHA-256 is `bd87f0fb37f5aaaba8a84e5fb1ec2313c0d8e2a9c8a249c40c81afed3faa8b2b`. All 55 file hashes captured at review start still match. All 31 numerical-manifest entries also match. Full hashes are in the machine record.

## Required correction

**R1 — Test coverage, Section 4.4, line 102.** The paragraph starts with “The 21 tests include” and then includes the geometric electricity positive control. That control was executed separately by `code/check_private_controls.py`, as recorded in `logs/numerical-private-control.json`. It is not one of the 21 public tests. Say “21 tests and a separate source-function control,” or separate the two descriptions. The author accepted this change but kept the manuscript frozen during review. No model rerun is needed for this text change.

## Numerical checks

The review used Python 3.12.14. [Public reconstruction](public-reconstruction.json) records the commands, times and output. The copy was under ignored local storage. The reconstruction ran twice, then ran all 21 tests. All tests passed. All nine generated numerical result files were byte-identical to the study results; the result guide also matched. The study's original result files and run logs were not replaced.

The separate [review calculation](independent_checks.py) uses 50-digit Decimal arithmetic. It constructs cumulative component prices, divides nominal values by those prices to get quantities, and uses signed price-times-quantity cross-valuations. This supplies the Laspeyres and Paasche factors without importing either implementation under review. It uses the stated exact algorithm factor, sqrt(1/8), and inference factor 2.2/35. The small difference from stored binary constants is covered by the stated tolerance.

The [saved results](independent-check-results.json) contain 579 comparisons. They cover all 12 annual case rows, all 96 source-export cells, 40 component-price rows, six training rows, 12 paired-effect rows, three electricity-ledger rows and 72 monthly values. The independent monthly calculation derives the third generated annual total as 72.3²/28.7 TWh. It checks the annual scale for spending, operations and datacenter labor. All comparisons passed. Required signed cross-values, nominal GDP amounts and Fisher factors were positive in all four cases.

I checked each number in the three manuscript tables against these independent values, including row order. The main effects are supported: the training-convention change raises the released-power 2025 real level by 63.5096 percent; preserving the stated annual electricity totals lowers the released-training level by 24.8559 percent. These are conditional calculations, not changes to observed revenue.

The independent check of the 54 printed targets returns the same 52 passes and two failures. The 2024 Fisher index and growth rate round directly to 2699 and 2599, while the source prints 2700 and 2600. The manuscript retains both failures. It correctly calls intermediate rounding a possible explanation, not an established fact. The public reconstruction's test success is not presented as proof that all printed cells match.

The first attempt at my review script failed because I used an output field name for a raw input field. I corrected that name and the saved contrast labels in my own script. The second attempt passed. This did not change study code or data; the machine record preserves the failure's scope.

## Source, method and interpretation checks

The [source check](public-reconstruction.json) passed for nine records, 16 retained raw or text files, 40 archive members and six short quotations. The check combined the two appendix versions for the quotation allowance. No full third-party archive or PDF was added to the public study. I checked 22 retained source-code/data members in each private run directly against the ZIP; all match. Both aggregate exports have SHA-256 `ae2291a261c767c846d67b48e4bd00884e8899a6c80d60e5b5136a4a311da458`. See [private-record-check.json](private-record-check.json).

The central source locators are correct. B1 PDF page 9, footnotes 2–3, states fixed rental prices by GPU type and the limitations of FLOP measures for memory and bandwidth. Its pages 12 and 15 supply the production and GDP tables. B2 and P2 page 22 give the operations-based training growth formula and state its use as a spending deflator. Their page 26 gives the signed component account; P2 pages 27–29 give the Fisher equations and results. P2 pages 10 and 24 distinguish stated electricity totals from electricity prices. I inspected these passages and the corresponding source code. The original `calculations.py` lines 23–77 extrapolate one monthly growth rate, emit a warning when later annual totals disagree, and continue. `results.py` lines 247–271 uses stated annual electricity costs and the constant training deflator. Lines 288–303 implement the signed Fisher calculation.

The favorable interpretation is prominent and warranted. Fixed prices for heterogeneous GPU rental services can define a volume measure even when spending per operation changes with chip mix. The operations bridge enforces another quantity definition. The source's accounting boundary does not make those definitions identical. The paper states both points and does not claim that the operations convention is the unique correction. It also retains the source's very large conditional growth result in every case.

OECD Annex A, paragraphs 57–58 and footnote 14 (PDF page 29), support the separation between nominal cost valuation and an additional volume assumption. Paragraphs 59–61 concern asset accumulation and valuation; the paper does not turn those passages into evidence for an observed AI output measure.

I read Bell's eight-page sensitivity audit and eight-page companion review, then inspected the available audit archive's inventory, scenario register and interpretation note. The archive contains tables and documents, with no script or notebook. Its register varies inference adjustment, training adjustment and inference shares; it does not include these two reconciliation cases. Bell already makes the broad sensitivity and fiscal-interpretation points. The manuscript gives that work credit. Its bounded contribution is the quantity reconciliation plus the annual-electricity mismatch in the pinned implementation, not a new general critique of AI measurement or a proof of worldwide novelty.

The chronological record is adequate. It separates initial source inspection from the prospective protocol, preserves the analytical addendum, and identifies the later terminology note and later Bell archive capture. The refused repeat is retained. The full baseline is an unchanged source run; the operations cases use a disclosed single-name in-memory adapter. The manuscript does not call every source-function case an unchanged execution.

## Limits and release decision

The four cases are deterministic. They neither identify the right empirical electricity path nor validate chip coverage, rental prices, algorithmic progress or inference quality. The independent arithmetic accepts the source-derived annual aggregates. It does not reconstruct the underlying GPU microdata. I inspected the prior work listed above; I did not conduct another exhaustive literature search. The six evidence quotes and the cited passages were checked, not every claim in every source.

The manuscript is readable. It gives the favorable interpretation before the numerical comparison. It separates index levels from annual growth, stated power from observed loads, and productive capacity from welfare or a dividend budget. Local file links in the manuscript and both guides resolve. Source-version differences and the full-archive rights limit are explicit.

Release can proceed after R1 is corrected and the release-only diff is checked. No change to the central code, data or results is requested.
