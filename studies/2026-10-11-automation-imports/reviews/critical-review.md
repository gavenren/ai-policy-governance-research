# Separate critical AI review

Review recorded UTC: 2026-10-11T21:08:56.174815+00:00.

Study: S006. Reviewer: the coordinating Codex agent, separate from the agent that wrote the central model and paper. The reviewer gave scope feedback during development. This is an internal AI review, not an external blind review or human approval.

## Decision

No blocking mathematical or numerical error was found. The study can proceed to the remaining release checks as a complete-study draft. This conclusion does not establish empirical validity, policy effectiveness, or priority of discovery.

## Checks

Independently checked all 1,296 grid rows from output minus foreign payments minus real collection costs. No model outcome function was used. Maximum residual was 2.85e-14. Confirmed all 597 positive-funding, negative-domestic-consumption rows. Re-derived the base no-loss upper levy 10/3 and maximum funding increase 40/3; also checked the examples at levies 2 and 4. Read the full manuscript, model, tests, design, protocol, ledger, and author response. Checked selected Becker text and all short source extracts. The author's broader full-text comparison was not fully repeated.

The reviewer ran all 8 tests. All passed. A fresh run in a temporary copy reproduced all 7 retained numerical result files byte for byte. Runtime timestamps were excluded from this comparison. Every original capture, extracted text, and short public extract matched its ledger hash. All public quotations matched normalized extracted text. No full third-party source was added to the public release. Exact independent check results are in [independent-check.json](independent-check.json).

## Issues and response

1. **Receipts:** The early output label combined gross levy payments and usable receipts. They are now separate columns. Real resource losses and fixed costs have separate accounting. Resolved.
2. **Negative case:** For e<=lambda, concavity is not assured throughout the domain. The revised proof uses Delta W=(e-lambda)tq-lambda*t^2/(2B)-K, which proves strict loss for every positive levy. Resolved.
3. **Who gains:** Domestic aggregate gain is not a global gain or a Pareto gain. The paper reports foreign losses, owner losses, and the negative global-surplus identity. Resolved.
4. **Collection:** The missing payment share is a real resource cost. It is not unpaid tax or a domestic transfer. The paper states that evasion requires a different model. Resolved as a scope limit.
5. **Prior work:** Becker, Wossnig, and trade-tax work already establish the main incidence and revenue issues. The claimed increment is the narrow joint feasibility test and its reproducible application. Equivalent prior formulas have not been excluded. Resolved as a novelty limit.

The [author response](author-response.md) records the author's disposition. All numerical findings concern synthetic assumptions. Grid counts are not probabilities. Source coverage is selected; no universal originality or current legal-status claim follows. The review does not assess a national implementation.

## Review tools and file state

Used local file reads, independent Python calculations, the study tests, source hash checks, and temporary-copy execution. No central model file was edited by the reviewer. Final status text and release links are integration changes. The final release check records identify the reviewed model, data, manuscript, and source state by SHA-256. Any later substantive change needs a targeted review.
