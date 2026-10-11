# Separate critical AI review

Review recorded UTC: 2026-10-11T21:08:56.174140+00:00.

Study: S005. Reviewer: the coordinating Codex agent, separate from the agent that wrote the central model and paper. The reviewer gave scope feedback during development. This is an internal AI review, not an external blind review or human approval.

## Decision

No blocking mathematical or numerical error was found. The study can proceed to the remaining release checks as a complete-study draft. This conclusion does not establish empirical validity, policy effectiveness, or priority of discovery.

## Checks

Independently reconstructed every retained base-case cash ledger, without calling model functions. All 11,979 rows agree within 4.93e-10, the CSV rounding scale. Re-derived the two binding-line intersections: joint sale 700/39 and reserve 280/39; no-overlap sale 1200/67 and reserve 261/67. The period-4 lower bound is 21+0.03q under immediate income-rights loss. Read the full manuscript, model, tests, design, protocol, source ledger, and response. Checked selected local APFC passages and all short source extracts; this was not a second full literature search.

The reviewer ran all 10 tests. All passed. A fresh run in a temporary copy reproduced all 6 retained numerical result files byte for byte. Runtime timestamps were excluded from this comparison. Every original capture, extracted text, and short public extract matched its ledger hash. All public quotations matched normalized extracted text. No full third-party source was added to the public release. Exact independent check results are in [independent-check.json](independent-check.json).

## Issues and response

1. **Sale timing:** The first version needed a clear distinction between loss of income rights and receipt of sale cash. The final model states the distinction and tests retained income rights. The late-sale penalty depends on early loss of income; the earlier funding gap does not. Resolved.
2. **Long-term finance:** A finite reserve is not lasting solvency. The paper retains acquisition, replenishment, terminal wealth, and political-control limits. The disposal weight is a chosen objective, not estimated welfare. Resolved as a scope limit.
3. **Prior work:** IMF cash-buffer methods and APFC reserve-depletion analysis already contain the core logic. The paper now describes an auditable application. It makes no priority claim. The inaccessible SSRN manuscript is not treated as read. Resolved as a novelty limit.
4. **Shock assumptions:** The path families have no probabilities and are not measured correlations. The 11,979 rows include overlapping sets. The smaller set fails when joint shocks are allowed. Resolved.
5. **Source path:** A manifest directory field contained the prose suffix “(ignored)”. The author replaced it with an exact path and a separate Boolean field. All retained file hashes pass. Resolved.

The [author response](author-response.md) records the author's disposition. All numerical findings concern synthetic assumptions. Grid counts are not probabilities. Source coverage is selected; no universal originality or current legal-status claim follows. The review does not assess a national implementation.

## Review tools and file state

Used local file reads, independent Python calculations, the study tests, source hash checks, and temporary-copy execution. No central model file was edited by the reviewer. Final status text and release links are integration changes. The final release check records identify the reviewed model, data, manuscript, and source state by SHA-256. Any later substantive change needs a targeted review.
