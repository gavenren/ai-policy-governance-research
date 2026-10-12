# S018 source-claim check

Recorded 2026-10-12T19:07:05.184551+00:00. **Source-lead check.** This is not the separate formal critical review. The source agent prepared the evidence package and did not author or execute the numerical analysis.

## Result

No unresolved source-claim blocker remains at the frozen manuscript hash `a4ebdd280e919296604007fefe95d8b16db8b9df2a6287028c832e0af1d5ec27`. Numerical validation remains with the formal reviewer. The source reviewer did not edit the manuscript.

The first manuscript read had hash `bef5e05ba40ff26e64fc1d7c3864b01bd3c56622cce241c212ebd224b59a5a11`. The full read was complete by 19:04:38 UTC. The source reviewer sent two needed fixes and one precision suggestion. The parent applied them. The repaired hash was checked at 19:06:01.760753 UTC.

## Findings and repairs

1. **Price basis.** The original result table called every amount nominal dollars. The source describes the floor as not indexed, but its final note gives a general 2026-dollar convention. The audit has not resolved that convention for all cash flows. The revised paper reports model dollars and says that they are not verified real purchasing-power changes. The nominal description of the payment policy remains supported by Section 2.1.
2. **Check count.** The first draft stated that 60 original summary-field checks passed. The saved execution record contains 80 entries. The frozen draft now states 80. This was a check of saved record counts, not a numerical rerun.
3. **Aggregate expense.** The abstract now says that the extended model holds aggregate floor expenditure fixed. The main text correctly separates the $25,000 individual maximum from the $4.62 trillion aggregate input. It does not claim to recalculate household eligibility or payments.

## Scope and evidence

The reviewer read the full manuscript and checked its source-facing claims against the pinned whitepaper, both source scripts and the full April 19 post-launch note. The original source scripts were read as text. They were not imported or run. The 28 printed targets were checked for transcription and source location. Their computed values were left for numerical review.

The original code resets the floor each year. The second trigger uses the result of the first trigger in its denominator. Its strict tests and fixed supplementary/admin terms are described correctly. The extended version omits the increase branches. Both use annual positive-gap counts, not a cumulative or first-surplus measure. The paper credits the authors' own discrepancy disclosure and retains a valid fixed-floor interpretation.

The prior-work statements remain within the retained read scope. Hoynes–Rothstein covers the transfer and financing design. OECD 2017 covers policy comparisons under a fiscal condition. Wenger's README distinguishes fixed from indexed transfers and states model limits. Neither a full read of all prior material nor a reproduction of prior estimates is claimed.

The proposal is identified as a non-government working proposal. No enactment, external peer review, author endorsement or measured national effect is claimed. The retained whitepaper and code copies have the stated licences. The source evidence cutoff concerns acquisition by 19:00:03 UTC. It is separate from the 18:59:28.032901 UTC protocol freeze and the numerical run that began at 19:02:33.488136 UTC. Later preparation does not move the original download times.

## Claim map

| ID | Manuscript scope | Result |
| --- | --- | --- |
| C01 | Identity, April 2026 version and proposed policy package | pass |
| C02 | Individual maximum and aggregate floor expense | pass after clarification |
| C03 | Non-indexation and discretionary increases | pass |
| C04 | Annual reset and two-stage trigger | pass |
| C05 | Strict thresholds, start years, base supplementary/admin denominator and unused threshold parameter | pass |
| C06 | Common distributions, seed and path length | pass |
| C07 | Meaning of surplus and median consistency | pass |
| C08 | Printed negative median / greater-than-half probability conflict | pass |
| C09 | Authors already requested reconciliation | pass |
| C10 | Bounded novelty statement | pass |
| C11 | Source cutoff versus execution and later preparation | pass |
| C12 | Pinned source copies and rights | pass |
| C13 | Cost reconstruction and revenue boost description | pass at source level |
| C14 | Twenty-eight selected printed targets | pass for transcription |
| C15 | Unit label for model amounts | pass after required clarification |
| C16 | Number of saved original summary comparisons | pass after count repair |
| C17 | Two hundred printed output checks | pass for metadata linkage |
| C18 | Hoynes–Rothstein prior claims | pass |
| C19 | Wenger prior claims | pass |
| C20 | OECD prior claims | pass |
| C21 | Full work displacement and inference limits | pass |
| C22 | Other tax, retirement, legal and welfare questions excluded | pass |
| C23 | Generated analysis results | outside this check |

The companion [JSON record](source-claim-check.json) gives the exact source locations, input hashes, read limits and dispositions. No new literature search or network acquisition was needed for this check.
