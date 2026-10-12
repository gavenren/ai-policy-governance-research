# A Smaller Deficit for Which Dividend?
## Payment commitments in a public model of automation finance

**State: Complete-study draft.** Study S018. October 12, 2026. AI-assisted research comment. Source checks, numerical analysis and separate AI critical review are complete. No human or journal peer review has occurred.

## Abstract

A fiscal projection for a public dividend is meaningful only when it names the payment that the government promises to make. We examine this issue in the Four Pillars proposal, whose public simulations connect automation-related taxes to a guaranteed income floor. The ten-year model permits revenue-triggered payment increases. Its twenty-year extension keeps aggregate floor expenditure fixed. Both are legitimate policy cases, but they do not describe the same commitment. The source already acknowledges inconsistent surplus figures. We reproduce its two implementations and compare both payment rules on the same economic paths within each simulation cohort. This separates the spending-rule difference from the different random draws created by extending the horizon. On the ten-year cohort, the year-ten surplus share is 55.65% with the fixed floor and 34.35% with the original trigger rule; the latter spends an average $604.11 billion more on the floor. In year 20 of the longer cohort, both rules retain a positive median gap. The results concern conditional annual budget accounts, not the probability that an actual government can finance the programme. The policy lesson is specific: a fiscal-success statistic should travel with the benefit rule that produces it.

## 1. The promise behind a fiscal number

Suppose a government plans to replace part of lost wage income with a public payment. It publishes a projection showing that new revenue could eventually cover spending. A later projection gives a better chance of reaching an annual surplus. That improvement could have several explanations. Revenue might grow faster, some other expense might decline, or the public payment might be smaller than before. These changes have different meanings for the people who rely on the payment.

This distinction matters for proposals intended to support households during extensive automation. A fixed nominal payment and a payment that rises when public revenue permits are different promises. Both can be considered. But a government cannot use one promise to describe household protection and another to describe the likelihood of a balanced budget without making the change clear.

The Four Pillars project provides a concrete case. Robert DeMaria's April 2026 working paper proposes an income floor alongside changes to taxation, supplementary payments, health coverage and retirement arrangements. The published code allows inspection of the fiscal calculation. Its initial ten-year simulation and extended twenty-year simulation use the same distributions for common growth parameters. They use different rules for the floor payment. The paper's abstract and Section 6.2 also put a negative year-ten median budget gap beside a surplus probability above one-half. Under the released code's definitions, those summaries cannot describe the same year's gap observations. [F1, abstract and Sections 2.1 and 6; M1–M2.]

The source's own post-launch note already asks for reconciliation of inconsistent surplus figures. This comment therefore does not claim to discover that the numbers differ or that the discrepancy was hidden. Its narrower contribution is to identify what each implementation calculates and to compare the two payment rules while holding the economic paths fixed. The [feasibility records](reviews/feasibility-independent.md) and [source guide](sources/README.md) delimit that contribution. A bounded search found no direct reconciliation of these two implementations in the inspected material; it cannot establish worldwide novelty.

## 2. Two coherent policies, one unclear comparison

### 2.1 What the proposal commits to

The source describes a maximum annual floor of $25,000, with an earnings phase-out. Its fiscal models start from aggregate floor expenditure of $4.62 trillion. These are different quantities: the first is a maximum individual payment, while the second is a modeled aggregate expense after the source's coverage and phase-out assumptions. The simulation does not recompute a household distribution each year. We retain its aggregate expense and do not validate its population calibration. [F1, Sections 2.1, 3 and 5; M1–M2.]

Section 2.1 expressly states that the floor is not indexed to inflation and that later increases are discretionary. This is the strongest favorable interpretation of the extended model. Holding the nominal payment fixed is a policy case that the proposal permits. Likewise, identical distributions for growth parameters do not logically require identical spending rules. The problem is attribution of the reported fiscal results, not the existence of a fixed-floor scenario.

The two scripts implement that distinction as follows.

| Feature | Ten-year implementation | Twenty-year implementation |
| --- | --- | --- |
| Initial aggregate annual floor cost | $4.62 trillion | $4.62 trillion |
| Increase from year 5 | A revenue test can raise the floor cost by 12% | None |
| Increase from year 8 | A second revenue test can set the cost at 120% of base | None |
| Carry an increase into the next year automatically | No; each year starts from base | Not applicable |
| Common growth distributions and initial seed | The published choices, seed 42 | The same common distributions and seed 42 |
| Number and length of paths | 2,000 paths of ten years | 2,000 paths of twenty years |

The original rule is not a permanent benefit ratchet. An increase can disappear in the next year because each calculation starts again from the base expense. Nor is the rule price indexation. The code associates its two higher aggregate levels with maximum floors of $28,000 and $30,000, but the audit treats these as the source's aggregate spending rules. It does not infer a household-level distribution for either increase.

The first trigger uses a strict revenue-coverage threshold of 0.95, beginning in year 5. The second uses a strict threshold of 0.98, beginning in year 8, after any first-stage increase has entered the denominator. Both denominators use base supplementary-payment and administration amounts, although those costs grow in the final spending account. We preserve this choice to reproduce the source. Changing it would be a different policy experiment. A threshold parameter listed elsewhere in the original input dictionary is not used by these actual tests. [M1, floor block.]

### 2.2 What the reported probability means

Both scripts count a surplus when revenue exceeds total spending in a particular year. The reported share is a fraction of the 2,000 simulated paths for that year. It is not the probability of having reached surplus at least once by then, the probability of a positive cumulative balance, or a test of debt sustainability.

This definition yields a simple consistency check. If more than half the observations are strictly positive, the source's middle-order observation must be positive. A negative median cannot accompany a positive-gap share of 55.7% in that same array. Separately, the median of revenue minus spending need not equal median revenue minus median spending. We do not treat that ordinary feature of separate distributions as an error.

The source's twenty-year table pairs a positive year-ten median with 55.7%, while the earlier discussion pairs a negative median with the same probability. Its April 19 note identifies an older roughly 34% figure and the later 55.7% figure as needing reconciliation. These are specific source statements. Only execution can establish which statements match the pinned implementations. [F1, Sections 6.2 and 6.4; F3.]

## 3. Reproduction and the matched comparison

We pin the source repository at commit `d0e84f01f7970c6161da874051aafffaefe77f1f`. The original evidence bytes were acquired by October 12, 2026, at 19:00:03 UTC; later reading and package preparation are recorded separately. The complete whitepaper and the two unchanged model scripts are retained under their stated licences. The source is a private policy proposal and working paper, not enacted law or a demonstrated national programme. This audit does not assess its legal implementation.

The design was selected after exploratory reading identified the spending-rule difference. The [protocol](protocol.md) preceded numerical execution. We run both published scripts unchanged, retain their printed output, and preserve each script's own 2,000 economic paths. Within each cohort, we calculate two accounts: the fixed base floor and the original two-stage trigger rule. Revenue and every other expense are identical across those two accounts for a given path and year.

Holding the paths fixed is necessary. The two scripts both use seed 42, but the longer script consumes additional random draws before the next path begins. A seed identifies a stream of draws; it does not establish that the same path number represents the same economy after the program changes how many draws it consumes. We therefore do not subtract the two source probabilities and call the result the effect of the payment rule. Each cohort supplies its own paired comparison.

For the ten-year cohort, the source exposes the original floor and the two large non-floor expense components directly. These provide checks on reconstruction. For the longer cohort, we subtract the fixed floor and the known supplementary-payment and administration expenses from total spending. The remainder is the combined health and federal-operations expense needed by the trigger tests. This recovers a sum already present in the source account; it does not estimate a new behavioral relation.

For a given path and year, the accounting identity is straightforward: the reduction in the budget gap equals the additional floor expense. Because the extra expense is nonnegative, adding the trigger can only leave the annual surplus classification unchanged or remove it. The change in the surplus share nevertheless depends on the distribution of gaps near zero. Reporting only the mean additional expense would miss that part of the comparison.

This is a controlled accounting comparison inside the source model. The revenue process includes a spending boost, but that boost does not adjust to the amount of the floor increase. We preserve that feature. In an economy with behavioral responses, a larger transfer could affect consumption, tax receipts, prices or production. None of those effects is estimated by this exercise.

## 4. Results

### 4.1 The source results describe different payment rules

The unchanged ten-year model produces a year-ten median gap of −$0.554 trillion and a surplus share of 34.35%. The unchanged twenty-year model produces a year-ten median of +$0.214 trillion and a surplus share of 55.70%. Thus the negative median belongs to the original trigger policy, while the later probability belongs to the fixed-floor extension. The source's roughly 34% figure is consistent with the original implementation. The comparison does not require an allegation about intent: the source itself requested reconciliation.

Twenty-seven of the 28 selected printed targets match the appropriate unchanged source model at the printed precision. The remaining target is Section 6.2's 55.7% year-ten surplus figure when tested against the ten-year trigger model discussed there. The retained [printed-value checks](results/printed-checks.csv) identify each target, its source location, the assigned implementation and the result. This is a check of selected statements, not an audit of every number in the whitepaper.

### 4.2 The same-path comparison attributes a substantial difference to the floor rule

The table reports both policies within each cohort. Each row uses all 2,000 paths. Gaps and mean floor expense are in trillions of model dollars. The whitepaper describes the floor as not indexed but also ends with a general convention that figures are in 2026 dollars unless otherwise noted. We preserve the model units without resolving that price-basis convention; the dollar differences below are accounting quantities from the model, not verified real purchasing-power changes. A negative gap means an annual deficit. The fixed and trigger rows within a cohort-year share every revenue and non-floor expense observation.

| Source cohort and year | Payment rule | Median annual gap ($T) | Paths with annual surplus (%) | Mean annual floor cost ($T) |
| --- | --- | ---: | ---: | ---: |
| Ten-year cohort, year 10 | Fixed nominal floor | +0.253 | 55.65 | 4.620 |
| Ten-year cohort, year 10 | Original trigger rule | −0.554 | 34.35 | 5.224 |
| Twenty-year cohort, year 10 | Fixed nominal floor | +0.214 | 55.70 | 4.620 |
| Twenty-year cohort, year 10 | Original trigger rule | −0.567 | 35.50 | 5.215 |
| Twenty-year cohort, year 20 | Fixed nominal floor | +3.729 | 80.55 | 4.620 |
| Twenty-year cohort, year 20 | Original trigger rule | +2.805 | 74.05 | 5.411 |

On the ten-year cohort, switching from the fixed floor to the original trigger adds an average $604.11 billion of floor expenditure in year 10. The same amount reduces the mean gap. The annual surplus classification changes on 426 of 2,000 paths, a decrease of 21.30 percentage points. These are paired changes on the same economies, not a subtraction of unrelated source runs. The difference between the two medians is not the mean paired change; both statistics are retained for their distinct purposes.

The payment side is substantial. In year 10 of that cohort, 522 paths retain the base aggregate floor, 426 use the 12% increase and 1,052 use the 20% increase. These are frequencies of simulated aggregate policies, not numbers of people receiving benefits. The original rule spends more on paths that pass its revenue tests. At the tenth percentile, both year-ten policies still have the same gap, approximately −$1.746 trillion. This lower-tail result is an important control: the fiscal effect does not amount to a uniform shift of every path.

The twenty-year cohort gives a similar year-ten comparison. The trigger adds a mean $594.96 billion and reduces the surplus share by 20.20 percentage points. In year 20, it adds a mean $790.94 billion and reduces the surplus share by 6.50 points. The latter result leaves 74.05% of paths in annual surplus and a positive median gap. Applying the payment increases therefore does not erase every favorable long-horizon result. Those favorable results remain conditional on the source's revenue and expense assumptions.

### 4.3 Controls and limits of attribution

Before year 5, the two payment rules are identical on every path within each cohort. All 60,000 paired path-year rows satisfy the expense/gap identity within the stated numerical tolerance. All original ten-year floor choices are reproduced, and 80 original summary-field comparisons pass. Two hundred printed baseline output fields also match their corresponding calculated summaries. The complete [aggregate results](results/summary.csv), [paired results](results/paired-summary.csv) and [compressed path-year audit](results/paired-paths.csv.gz) retain the earlier years and both tails, not only the selected endpoints. There are no excluded paths.

Only ten of the 20,000 same-index revenue observations in the two cohorts' first ten years are identical: the first path's ten years. The shared seed therefore does not make the published cohorts paired. The within-cohort results show the effect of the floor rule under fixed cash flows. They do not establish that all differences between the two source tables come from that rule. The twenty-year extension also introduces a displacement path after year 10, which we retain without recalibration.

Eleven focused tests check the trigger boundaries, activation dates, sequence, annual reset and summary conventions. A first test fixture failed because the intended 0.98 ratio rounded slightly above that boundary in binary arithmetic. The record preserves the failure and the replacement with an exactly represented boundary fixture. The source rule and generated numerical results did not change. [Reproduction guide](REPRODUCTION.md).


## 5. What follows for policy design

The comparison does not show that the fixed payment is a worse policy. A legislature might choose it to limit fiscal exposure. It might also choose to increase payments when resources permit, accepting a different budget path. The result that matters is the joint outcome: what households receive and what the government must finance under that rule.

A clear fiscal presentation would label the fixed nominal case separately from the revenue-triggered case. Each table would use a single cohort and a single benefit rule for its median, tail values and surplus frequency. A statement about an extended horizon would identify any policy change made at the same time. That is sufficient to preserve the legitimate fixed-floor interpretation without treating the two commitments as interchangeable.

The same discipline applies to the meaning of success. A positive annual balance does not establish that deficits in earlier years can be financed. A fixed nominal payment does not protect a constant quantity of essential goods when prices rise. And a modeled aggregate floor cost does not show how payments reach households or interact with other benefits. Those questions require additional accounts and evidence, rather than a stronger label on the annual surplus statistic.

For a post-labor dividend, the payment rule should therefore be part of the fiscal claim itself. A useful statement specifies whether the payment is fixed in nominal terms, indexed to prices, linked to revenue, or subject to discretionary increases. It also specifies whether a granted increase persists. That last distinction is especially important here because the original code resets the floor every year. An automatic permanent increase would create another spending path, not merely another description of this one.

## 6. Prior work and limits

Hoynes and Rothstein already show why a basic-income proposal must specify its guarantee, phase-out, eligible population, financing and treatment of existing benefits. The OECD's 2017 technical note already constructs policy comparisons by varying benefit amounts or tax rates under fiscal constraints. Wenger's public AGI-economy model documentation also distinguishes fixed nominal transfers from indexed transfers and states the model's calibration limits. The present paper does not claim these distinctions as new. [P1–P3.]

The contribution is smaller: it reconciles a named public projection with its executed payment rules and quantifies the change on the same source paths. Its scope is suitable for a short research comment. It does not establish a new economic theorem, estimate a national basic-income reform, or decide whether automation taxes are desirable.

The inherited simulation distributions are assumptions. Reproducing their outputs is not evidence that they describe future GDP, displacement, tax enforcement or health costs. The original scripts retain wage-related revenue and do not model humans being outcompeted in every field. Their results cannot be relabeled as a forecast for complete labor displacement. They provide a case about how a future-support proposal reports its commitments.

We do not audit the wider proposal's tax bases, retirement transition, disability protection, household phase-out effects or political implementation. Separate scripts and draft documents discuss some of those matters, but neither their presence nor this reproduction establishes that all obligations enter the simulated federal account. The extended script's printed land-value-tax scenario is retained as source output and lies outside the selected comparison. No additional policy or seed is introduced to search for a preferred result.

Finally, the constructed paths are not observations from a population. Their frequencies describe the selected model and seed. Sampling precision within that simulation would not resolve uncertainty about the model itself. The matched design isolates an accounting change under the retained assumptions; it does not turn those assumptions into empirical facts.

## Research record and disclosure

AI agents conducted source research, programming, drafting and checks. A separate AI agent reproduced the numerical package and checked the path and summary arithmetic without importing author functions. The [critical review](reviews/critical-review.md) and [author response](reviews/author-response.md) record its scope and the correction to the data dictionary's unit label. No numerical result changed. The reviewer had an earlier feasibility role and did not author the central analysis. The source's own discrepancy note, the favorable interpretation of a fixed payment, unchanged positive results and failed reproduction targets must remain in the record. No human review, author contact, affiliation, funding claim or endorsement has been supplied. Third-party licences apply only to the identified source material; no reuse licence has been selected for this original comment.

## References and source map

- **F1.** DeMaria, Robert. 2026. *The Four Pillars: A Comprehensive Economic Framework for Universal Basic Income in the Age of Automation*. Working Paper v2.0, April. [Pinned whitepaper](https://github.com/saccasolutions/fourpillarsproject/blob/d0e84f01f7970c6161da874051aafffaefe77f1f/docs/Four_Pillars_Whitepaper.md). The unchanged CC BY 4.0 copy is in [source snapshots](sources/snapshots/whitepaper.md).
- **M1–M2.** DeMaria / The Four Pillars Project. [Ten-year source](https://github.com/saccasolutions/fourpillarsproject/blob/d0e84f01f7970c6161da874051aafffaefe77f1f/models/monte_carlo_tax.py) and [twenty-year source](https://github.com/saccasolutions/fourpillarsproject/blob/d0e84f01f7970c6161da874051aafffaefe77f1f/models/extended_monte_carlo.py). Exact copies with the MIT notice are in [the vendor directory](vendor/four-pillars/).
- **F3.** The Four Pillars Project. 2026. [Post-launch findings](https://github.com/saccasolutions/fourpillarsproject/blob/d0e84f01f7970c6161da874051aafffaefe77f1f/launch/post_launch_findings.md), dated April 19. Section on whitepaper numbers that need updating.
- **P1.** Hoynes, Hilary, and Jesse Rothstein. 2019. *Universal Basic Income in the US and Advanced Countries*. [NBER Working Paper 25538](https://www.nber.org/system/files/working_papers/w25538/w25538.pdf), February. Selected transfer-design, cost and research-limit sections.
- **P2.** Wenger, Albert, with Claude credited in the source. 2026. *The AGI Economy: A General Equilibrium Model*. [Repository documentation](https://github.com/albertwenger/agi_economy/blob/d71e1756773a9ca9334e1c62f40fa605f5d4d510/README.md), pinned June 10 revision. README only; code not executed.
- **P3.** OECD. 2017. *Basic income as a policy option: Technical Background Note. Illustrating costs and distributional implications for selected countries*. [Official note](https://www.oecd.org/content/dam/oecd/en/topics/policy-sub-issues/income-support-redistribution-and-work-incentives/basic-income-policy-option-2017-brackground-technical-note.pdf), May. Sections 1 and 4. Prior estimates were not reproduced.

Other acquired material is listed for provenance and scope. It does not expand the selected claims. The [source guide](sources/README.md) records rights and access limits, and the [reproduction guide](REPRODUCTION.md) records the generated results and checks.
