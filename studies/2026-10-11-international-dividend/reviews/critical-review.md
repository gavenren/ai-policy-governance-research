# Separate critical review: S009

**Reviewer:** a separate internal AI agent that did not write the study's central model or manuscript. This is not human or journal peer review.

**Completed:** 2026-10-11T21:35:22Z. **Manuscript SHA-256:** `bb784c3dd8c6253d433abbacbaa9b97f2bc95314abb525611b20e5dcad8ba0c3`. [Reviewed hashes](reviewed-hashes.json) identify the actual files. The manuscript was still labeled Working notes during this review.

## Decision

No blocking analytical or reproducibility error remains in the reviewed version. The study can proceed to its final release checks after the author records a response. Its contribution should remain a limited application of established contract theory. The review does not establish universal novelty, legal enforceability, or empirical policy effects.

## Actual scope and checks

Read the complete manuscript, protocol, source comparison, evidence extracts, data dictionary, search and decision records, model, and tests. Examined the stated payment sequence and both governments' deviations. Checked the direct compliance and default payoffs, the termination continuation, the nonnegative inverse argument, and the deposit bounds.

Ran the documented analysis command and all 12 tests. Both exited successfully. The four CSV files and summary JSON reproduced byte for byte. The run metadata changed only because the analysis was executed again. No source acquisition code was executed.

Ran [a separate exact-fraction check](independent-check.py). It does not import the author's model. It uses the two-state mean and contrast formula, direct compliance-minus-default payoffs, and candidate roots and midpoints of the deposit constraints. All 648 target cases agree with the saved grid: 292 pass and there are no mismatches. It independently checks the floor boundaries `39/5`, `183/35`, and `43/7`; the persistent adverse-state value `15/7`; the payment margin `-27/7`; and the floor-six deposit interval `[135/28, 60/7]`. It also confirms that a deposit of 12 fails participation and that matched loan discounting removes the deposit's marginal enforcement gain. The result is saved in [independent-check.json](independent-check.json).

Checked the original and extracted byte hashes for all six retained sources. All match. Each short public quotation occurs in the retained extracted text after joining layout breaks. Read the relevant passages of Levin on payment and outside-option constraints, Kerr and co-authors on third-party precommitment, the GovAI report on sharing and enforcement, the windfall-clause implementation section, and the verification report's cash-transfer section. These passages support the bounded comparisons. The paper and README have no broken explicit local Markdown links.

## Findings and disposition

1. **Domestic spending scope.** The original prose could be read to protect the domestic minimum even after exit or forced loan repayment. The model applies that minimum only to the compliant treaty budget. This distinction matters because debt repayment after default can breach the stated domestic amount. The author now says this explicitly in Section 3 and the data dictionary. The revised text was checked. Resolved without a numerical change.

2. **Search-record count.** The earlier search record listed five retained sources, while the final paper used six. The author preserved the earlier stage and added the later S8 capture, with its actual time and reading limits. The record now explains the final count. Resolved.

3. **Zero discount factor.** The break-even cost formula divided by the discount factor, although the model permits zero. The author now restricts that expression to a positive discount factor and states the zero-discount case. The implementation already handles that case. Resolved.

## Interpretation and remaining limits

The payment constraint depends on the value lost after termination. The model correctly excludes outside wealth that survives default. The no-deposit punishment is a stage-game equilibrium under the stated service cost and observability assumptions. It is not shown to resist renegotiation. The recipient's service must be dispensable after nonpayment; independent recipient benefits would change that conclusion. These limits are explicit.

The deposit result requires two enforceable arrangements: trustee seizure and a loan that is repaid even after treaty default. It does not solve commitment without institutions. Deposit principal is matched by debt at entry, not counted as new wealth or as a recurring compliant expense. The fiscal carrying cost is not asserted to be a global resource loss. An affordable deposit still cannot supply a permanent income stream after termination. The paper states each of these limits.

The source review supports an application and synthesis, not a new general theorem. Levin already supplies the dynamic-enforcement logic, and Kerr and co-authors already compare payment timing and external commitment. The manuscript acknowledges the prior work and inaccessible close candidates. A fuller review of stochastic relational contracts could further reduce its novelty claim.

This reviewer did not perform an exhaustive new literature search, independently fetch current versions, verify any present treaty's legal status, inspect the separate public repository for duplicates, or estimate real country parameters. The independent arithmetic is specific to the two-state experiments; the general finite-state result was checked algebraically, not through an independent general-state solver. Neither passing code nor this AI review proves policy feasibility. The parent must complete repository identity, rights, release hygiene, and remote publication checks.
