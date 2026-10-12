# Independent AI review of the S011 benefit-unit extension

**Decision:** No blocking issue remains in the reviewed extension. The two requested text and source repairs are verified. The author response and release checks remain separate steps.

**Review completed:** 2026-10-12T17:33:29.821021Z

**Reviewer:** A separate AI agent, `/root/large_load`, which did not author this extension. This is not human expert review or journal peer review.

**Reviewed manuscript:** SHA-256 `b5ca8684984462a745ecf029c3382b3e29292a13cf9225d1086aec7052056e10`. This is the Working notes version after the two repairs. [Reviewed hashes](reviewed-hashes.json) identify every extension file in the frozen snapshot. This review covers Section 8, Appendix B, the extension's effect on the abstract and limits, and its data, methods and results. It does not replace the earlier review of the original S011 analysis.

## What I checked

I read the extension protocol, manuscript section, dictionary, source ledger, code, result tables and review fixes. I checked the retained SCF codebook's PEU definition, X7001/X101 top codes, roster ages, dependence flags, X7020 and survey-variance instructions. I read the relevant OECD 2013 scale and unit discussion, Browne and Immervoll's individual-payment and fiscal-comparison sections, and the added OECD 2024 age-definition passage. I did not treat a search snippet as the source for the repaired age claim.

I wrote [separate review code](independent-check.py). It imports no author analysis function. Starting from the full public SCF roster and original replicate-weight file, it reconstructs member and adult counts, joins them to the original financial records, fits all payment rules and calculates every outcome. The full roster agrees with the selected public roster. All 21,800 joins are complete.

The [executed check](independent-check.json) compares all 192 measures in five implicates and 999 survey replicates: 192,768 comparisons. All match within numerical precision. The largest absolute difference, divided by the larger of one and the reported magnitude, is 1.65e-13. All combined estimates and standard errors also match. The separate code checks 6,024 aggregate budgets; its largest relative difference from the target is 4.89e-15. This small difference from the author's round-off bound comes from a different summation order.

I also ran the author's ten tests and the source check with retained local bytes. Both pass. The source check covers five sources, four short extracts and eight local files, and confirms 52 original study files unchanged. The [rerun record](author-check-rerun.json) saves the actual output. An [exact arithmetic check](worked-example-check.json) confirms the two-family example: each rule pays a total of $4,000, one family fails under each rule, and the affected member count changes from four to one.

## Policy comparison and uncertainty

The comparison holds the population, gross payment budget, financial shock, debt measure and threshold fixed across payment rules. If v is the chosen payment basis and w is the family weight, the coefficient is c=2,000 sum(w)/sum(wv). Hence sum(wcv)=2,000 sum(w). This is a proof of equal added gross payments within that sample. It is not a proof of equal net fiscal cost or equal welfare. The text makes that limit clear. The exact and capped populations have separate budgets; the paper does not compare their total spending as if the populations were the same.

The coefficient is fitted again in every implicate and replicate. This is required for the stated target: a payment rule whose rate adjusts to the same aggregate budget. A negative check confirms that fixing a rate from another sample can break the budget constraint. The appendix correctly distinguishes this target from a cash payment fixed outside the sample.

Family outcomes use sum(w) in the denominator. The supplementary person outcome uses sum(w times PEU size). Each PEU member receives the PEU's test outcome; the calculation does not estimate that person's consumption or control of money. This distinction explains why the family and person rankings can differ. The claim remains limited to members of the covered PEUs, rather than all people at the same addresses.

The paired differences are calculated within each implicate and replicate before variance is combined. Thus covariance between the rules is retained. The independent code matches their standard errors, using the codebook's sample variances with divisors 4 and 998 and the 6/5 imputation multiplier. A negative check shows why adding two separate arm variances would be wrong. The reported intervals concern survey uncertainty under the specified rules; they do not include uncertainty about the needs scale, permanent wage loss or policy responses.

## Definitions, prior work and claims

The dependence flags and the spouse/partner field support the PEU membership construction. The masked non-core age bands preserve the split at 18. They cannot recover the split at 14. The two size-12-or-more families are excluded from the primary analysis in each implicate, as specified before outcomes. The weighted exclusion shares of 0.033–0.051 percent reproduce. The capped-roster sensitivity is correctly labeled as an assumption and is not presented as a bound on true needs.

The OECD sources do not validate PEU square-root size as a complete needs measure. In particular, the 2013 framework warns that shared costs can cross family-unit boundaries. The manuscript states that its PEU threshold is a policy assumption and that these costs and within-family control are unmeasured. Browne and Immervoll already use a common fiscal constraint and distinguish individual payments from family support. The extension gives those methods a specific accounting application. It does not claim a new scale or general microsimulation method, and it remains an extension of S011.

The manuscript is readable. The small example explains the denominator issue before the survey table. The table and paired changes agree with the executed results. The text correctly treats the original classification gap as a diagnostic, not a measure to minimize as a general policy objective. It does not claim that the rule with the smallest sample shortfall is the best policy.

## Requested repairs and disposition

| Finding | Requested repair | Verified outcome |
|---|---|---|
| R1: The original README contained a current complete-study sentence below the extension notice. | Make the old review status historical and mark the expanded version Working notes. | Resolved. The README now makes both dates and scopes clear. |
| R2: The retained 2013 OECD text did not establish the precise age-14 boundary named in the draft. | Supply a locatable official source or remove that comparison. | Resolved. E5 retains the relevant OECD 2024 Section 13.2 text. The ledger distinguishes tool text from original HTML, reports the direct-request failure, and dates this addition after analysis. No outcome changed. |

My first independent computation had its own floating-point tie error in the constant-family arm. I corrected it by using the exact $2,000 coefficient required by the identity. The [calculation log](review-calculation-log.md) records the failed run and correction. The final independent calculation uses strict threshold comparisons and agrees with the author's small-tolerance implementation. This was not an error in the author results.

Remaining limits are explicit: PEU pooling, the chosen size rule, fixed debt payments, before-tax resources, top-coded large units, and no behavioral or general-equilibrium response. The review does not certify official data production, actual policy feasibility, causal AI effects, legal entitlement or a preferred welfare criterion.

## Reproduce this review

From the repository root, with the pinned free public inputs already retained:

```sh
python3 studies/2026-10-11-household-debt/extensions/benefit-unit/reviews/independent-check.py \
  --full .local-sources/household-debt/benefit-unit/p25i6.dta \
  --weights .local-sources/household-debt/D2/p25_rw1.dta
```

The script checks the recorded manuscript and extension hashes before calculation. Later release-only text changes will therefore need the reviewed snapshot to reproduce this exact check. The source acquisition recipes remain in the extension README.

- Full SCF data SHA-256: `38926275dfb8f00ea843b80ced7a9412ad4653d39c7fab8fe24c3bdf912902ad`.
- Replicate-weight file SHA-256: `3b452c1728f5f565074745cf60f810e78f75262e533327f0d3d53ce62ecf4d2c`.
- Independent review code SHA-256: `cba1644bbfb934d3fb57be84c4663fe70c8226d145fbbe247ba9568f6a59d2a3`.
- Python 3.12.14; NumPy 2.3.5; pandas 2.2.3.
