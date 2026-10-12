# What Does AI Output Growth Measure?
## Reconciling compute, spending and electricity in an AI economy account

**State: Complete-study draft.** Study S016. October 12, 2026. Prepared with AI agents; no human or journal peer review. Numerical checks and a [separate AI critical review](reviews/critical-review.md) are complete. See the [author response](reviews/author-response.md).

Evidence was first collected through **2026-10-12T18:08:07Z**. The closest audit archive was additionally retrieved by **2026-10-12T18:16:02.497761Z**; its inspection and the separate source rechecks are dated in the evidence ledger. The earlier cutoff does not imply that this later work occurred before the analysis plan.

## Abstract

Measures of AI output can rise at different rates because they count different quantities. This paper audits two accounting choices in the public replication of Korinek and McKelvey’s *Measuring the AI Economy*. The reported training production series counts effective physical operations, while the training component of AI GDP can be interpreted as fixed-price rental services adjusted for algorithms. We reconcile both conventions without selecting one as uniquely correct. We also find that the monthly electricity routine generates 182.14 TWh for 2025 while the listed annual input and electricity-cost account use 138 TWh. In the reproduced model, enforcing the stated total lowers the 2025 real AI GDP level by 24.9 percent. Using the operations convention with the released electricity path raises that level by 63.5 percent. The changes partly offset in annual growth but do not identify actual economic welfare or fiscal capacity. The contribution is a reproducible account of what these measures mean and how their inputs fit together, not a new theory of price indexes or a forecast of labor displacement.

## 1. Introduction

A government preparing for an economy with less human work needs measures that it can interpret. A rapid increase in computing capacity may justify more attention to labor displacement. It does not specify the income available for a public dividend. Even before that distinction arises, two measures described as AI output can count different things.

Consider a data center that replaces older chips with newer chips. Rental prices for each chip type can remain fixed while the number of operations obtained per dollar rises. An index that values chip services at those fixed prices will then grow more slowly than an index that counts operations. Neither observation is a contradiction. The two indexes use different weights. Applying the same algorithmic improvement factor to both does not remove that difference.

This paper examines that distinction in Korinek and McKelvey's *Measuring the AI Economy*. Their training production series uses physical operations, adjusted for algorithmic progress. Their AI GDP calculation uses training spending with the algorithmic factor as its price adjustment. Both can support a coherent interpretation. They require a reconciliation if a reader expects the training component to represent the same quantity in both accounts. A second check concerns electricity: the released monthly routine extrapolates the first annual growth rate, while the GDP cost calculation uses the listed annual totals. [Korinek and McKelvey, 2026](https://www.bankofcanada.ca/2026/06/staff-working-paper-2026-20/); [technical appendix](https://pmckelveyboc.github.io/technical_appendix.pdf).

Our contribution is a small, reproducible accounting audit. We preserve both training conventions, trace the electricity quantities through the released implementation, and compare four cases with the remaining assumptions fixed. This is not an estimate of actual AI welfare or a replacement for national GDP. It is a test of how a specific measurement system translates its inputs into its reported quantities.

The closest prior analysis is Bell's sensitivity audit. It already tests alternative inference prices, training progress and allocation between inference and training. His separate review also explains why capability, adoption, output, welfare and public revenue must be measured separately. We do not claim those distinctions as new. Our narrower question concerns the relation between two training quantity definitions and the consistency of annual electricity accounting. The attached audit archive was also inspected. It contains scenario settings and results but no calculation script or notebook; its scenario register does not include either comparison studied here. This does not establish what private calculations the prior author performed. The bounded search and source comparisons are recorded in the study evidence package. [Bell, 2026a](https://doi.org/10.5281/zenodo.20501770); [Bell, 2026b](https://doi.org/10.5281/zenodo.20500501).

## 2. Two valid training quantities

Let V be spending on training compute and X be physical training operations. The source fixes the training share over time. Let a be the annual ratio of compute required to attain a fixed model capability. When a is below one, algorithmic progress makes each physical unit more effective.

One possible volume measure is rental-service spending divided by the cumulative algorithmic requirement factor. Since each GPU type has a fixed rental price in the source model, spending itself is a fixed-price weighted sum of heterogeneous chip services. Its annual quality-adjusted growth factor is spending growth divided by a. A second measure uses physical operations instead of spending. Its annual growth factor is physical-compute growth divided by a.

These measures coincide when spending and physical operations grow at the same rate. Otherwise, their growth factors differ by the change in spending per operation. This is an accounting identity, not a new economic theorem. The issue is the choice of quantity to which the identity is applied. The OECD treatment of R&D measurement makes a related distinction between nominal valuation from costs and a separate assumption about output volume. It does not select operations weights over rental-service weights. [Schreyer and Zinni, 2018, Annex A, paragraphs 57–58](https://doi.org/10.1787/fb3c2e6f-en).

The operations measure is not automatically superior. Two chips with the same operation count can differ in memory, bandwidth or suitability for a task. Their rental-service values can reflect features that a simple operation count omits. Conversely, fixed rental-price weights need not track the number of operations that produce a chosen benchmark result. The choice must follow the intended use of the account and the evidence available to value quality.

Suppose the analyst chooses the effective-operations measure for training investment. Then the associated training price ratio must equal the algorithmic ratio multiplied by spending growth divided by physical-compute growth. This makes price times quantity reproduce nominal spending. If the analyst instead chooses the rental-service convention, the original GDP training deflator can be retained, and the reported training production series can be expressed in those same service units. Both routes are coherent.

The ratio of spending to operations is a unit value. It can change because the mix of chips changes, even if no GPU-specific rental price changes. We therefore call our alternative an operations-consistent convention. We do not describe it as a measured change in pure market prices or as the uniquely correct GDP deflator.

The AI-island boundary addresses another question: which outputs and imported inputs belong in the account. Changing that boundary can explain why total production differs from value added. It does not, by itself, select the quantity index for the training investment component. Appendix A separates the component identity from the aggregate Fisher calculation.

## 3. Data and design

The study uses a frozen public replication package and the corresponding paper and appendix. The package contains the inputs needed for the power-based calculation. We use these as model inputs, not independently verified observations of the whole AI economy. The provenance record distinguishes the Bank of Canada paper, two appendix captures, the package, and the closest prior analyses.

The analysis plan was recorded after source reading and informal hand calculations, but before the numerical runs. It is prospective for the four-case design and its checks. Selection of the two accounting questions was exploratory. A separate AI agent had already identified the favorable fixed-price interpretation. These limits are stated in the [protocol](protocol.md).

The first case retains the released electricity rule and training deflator. The second changes only the training convention. The third preserves each stated annual electricity total while retaining the original training convention. The fourth combines those two changes. All cases retain the source's allocation shares, GPU characteristics, rental prices, inference adjustment, service margins, labor assumptions and accounting boundary.

For the electricity alternative, we multiply every month in a given year by the same factor: the listed annual total divided by the sum generated for that year. This preserves the original relative monthly pattern and chip composition. It does not estimate actual monthly electricity demand. It isolates the effect of honoring the stated annual totals.

The unchanged power-based program ran offline from a fresh private extraction. Its original whole-US GDP output was retained only as part of that baseline run; we did not extend that calculation to the alternative cases. A documented adapter changed the monthly totals or the training price lookup for the four AI-island cases. Our separate public reconstruction then rebuilt the signed component ledger and Fisher calculation from aggregate inputs. All 96 comparisons of components, nominal values, chained indexes and real levels matched the source-function calculations. The execution record preserves software versions, source hashes, warnings and setup failures. Two unchanged source runs produced identical aggregate exports. The public reconstruction passed 21 tests. The printed-table comparison passed 52 of 54 direct display checks; its two retained exceptions are discussed below.

The source model’s 2024 Fisher index is 2,699.4876 and its growth rate is 2,599.4876 percent. The paper prints 2,700 and 2,600 percent. Those two cells fail a literal nearest-integer check by one unit; the difference is small and does not affect the substantive result. We retain it rather than silently adjusting either the model or the reported values. An explanation based on intermediate rounding is possible but unverified. Our tables round the full-precision executed values directly.

## 4. Results

### 4.1 Electricity used and electricity charged

The monthly routine exactly reproduces the stated totals for 2023 and 2024, apart from floating-point error. It then extends their growth rate into 2025. The resulting annual total is 182.14 TWh, or 32.0 percent above the stated 138 TWh. The program issues a warning but continues to use the extrapolated electricity to calculate spending, operations and data-center labor. Its GDP calculation charges for 138 TWh. This is a discrepancy between quantities used within the same run, not evidence about actual electricity consumption.

| Year | Stated input, TWh | Generated monthly sum, TWh | Annual-preserving multiplier |
| --- | ---: | ---: | ---: |
| 2023 | 28.70 | 28.70 | 1.0000 |
| 2024 | 72.30 | 72.30 | 1.0000 |
| 2025 | 138.00 | 182.14 | 0.7577 |

The alternative multiplies every 2025 month by 0.7577. Earlier years do not materially change. At the source’s electricity price, charging for the generated 2025 quantity would cost $15.700 billion instead of $11.896 billion, a difference of $3.804 billion. That cost ledger is a diagnostic, not a fifth modeled GDP case. Our four cases instead retain the stated electricity cost and compare output paths that do or do not honor its associated annual quantity. [Power ledger](results/power-ledger.csv).

### 4.2 Training growth depends on the chosen unit

Under the released electricity path, operations grow faster than fixed-price rental spending. Dividing both by the same algorithmic ratio therefore produces different training growth rates.

| Year | Rental-service volume growth, % | Operations volume growth, % | Operations-consistent training price ratio |
| --- | ---: | ---: | ---: |
| 2024 | 593.0 | 782.1 | 0.277787 |
| 2025 | 585.3 | 787.7 | 0.272926 |

The original GDP training price ratio is 0.353553 in each year. Selecting the operations convention requires the smaller ratios in the table. Both price–quantity pairs recover the same nominal training spending. The operations growth factor is 1.273 times the rental-service factor in 2024 and 1.295 times it in 2025. These compare gross growth factors, not percentage growth rates. By 2025, the cumulative operations index is 1.649 times the rental-service index when both start at 100 in 2023.

Enforcing the 2025 electricity total reduces both spending and operations by the same factor. It therefore leaves their relative growth and the operations-consistent price ratio unchanged. Their absolute 2025 volume growth rates fall to 419.2 percent for rental services and 572.6 percent for operations. This is a useful separation: the energy choice changes activity, while the training convention changes which activity index the GDP component follows. [Training reconciliation](results/training-reconciliation.csv).

### 4.3 The two changes act in opposite directions

The complete four-case comparison is shown below. “Rental services” names our favorable interpretation of the source’s training convention. “Operations” uses the price ratio consistent with its physical training series. Real GDP here is the source’s quality-adjusted AI-island measure.

| Electricity rule | Training convention | 2024 real growth, % | 2025 real growth, % | 2025 Fisher index, 2023 = 100 |
| --- | --- | ---: | ---: | ---: |
| Released extrapolation | Rental services | 2,599.5 | 2,657.8 | 74,445.2 |
| Released extrapolation | Operations | 3,292.5 | 3,488.0 | 121,725.1 |
| Preserve stated annual totals | Rental services | 2,599.5 | 1,972.3 | 55,941.2 |
| Preserve stated annual totals | Operations | 3,292.5 | 2,596.3 | 91,471.0 |

Changing only the training convention raises the 2025 real level by 63.5 percent under the released electricity path. This direction is expected: physical operations grow faster than spending, so the operations convention uses a lower training price ratio. With the nominal ledger fixed and the required Fisher factors positive, that lowers the aggregate price adjustment and raises measured real growth. It leaves nominal AI GDP unchanged.

Preserving the stated annual energy totals lowers the 2025 real level by 24.9 percent under the source training convention. Nominal AI GDP falls from $250.725 billion to $187.086 billion, or 25.4 percent. These are model-implied values. They do not revise observed business revenues or official statistics.

With both changes, 2025 annual growth is close to the baseline, but the 2025 index level remains higher. The difference comes from the larger growth already accumulated in 2024. Similar annual headline rates can therefore conceal different quantity conventions and paths. None of the four cases makes the source’s quality-adjusted growth ordinary in scale. That retained result is conditional on the unchanged quality assumptions; it does not validate them. [All cases](results/cases.csv); [paired effects](results/factorial-effects.csv).

### 4.4 Checks and scope of the comparison

The independent reconstruction matches all four source-function cases, not only the baseline. All reported nominal value-added amounts and required Fisher factors are positive. Price-only changes leave the nominal ledger unchanged. Both training conventions satisfy the price-times-volume identity, and the annual-preserving rule leaves relative monthly profiles unchanged.

The 21 public tests include adverse and favorable cases. Identical spending and operations growth makes the two training conventions coincide. A change of currency or operation units leaves the relevant growth comparison unchanged. A change in chip mix produces different growth measures even when each chip’s rental price is fixed. The tests also reject nonpositive Fisher factors as undefined. A separate source-function control confirms that the original monthly rule preserves geometrically consistent annual electricity totals. Its execution is recorded in [the control log](logs/numerical-private-control.json). These controls show where the reconciliation matters and where it disappears. They do not establish the empirical validity of the underlying inputs.


## 5. Implications for economic governance

An AI output index is useful only if a decision maker can identify what grows. Effective physical operations can inform an assessment of technical capacity. A fixed-price service measure can describe a different aspect of the production system. Nominal receipts, profits and ownership determine different parts of the fiscal question. The present calculation does not supply the missing links between them.

A practical reporting rule follows from the audit: give the training component one stated volume definition, show the price ratio that makes it consistent with spending, and reconcile energy used to produce output with energy charged as an input. A report can publish more than one convention. It should explain why they differ and which decision each can support.

For a government considering income support after extensive automation, this means that an output growth estimate cannot determine a dividend budget on its own. The relevant fiscal evidence includes cash receipts, taxable profits, public ownership claims and the costs of essential services. This wider caution is already central to Bell's review. Our contribution is to identify two specific reconciliation steps that can be checked before such an output index enters that policy discussion.

## 6. Limitations

The four cases are deterministic comparisons. They are not confidence intervals, a probability distribution over future economies, or evidence for a displacement date. They leave the source's inference quality adjustment and other uncertain inputs fixed. A large quality-adjusted index remains conditional on the link between the selected capability measure and economic output.

The electricity alternative enforces stated inputs; it does not establish that those inputs are correct. The operations alternative enforces one quantity convention; it does not establish that operations measure all economically relevant chip quality. The results therefore support clearer measurement practice, not a general verdict on the source's research program.

No human researcher has reviewed this manuscript. AI agents performed the source work, numerical analysis, drafting and separate critical review. The reviewer did not author the central analysis and disclosed its earlier feasibility and wording role. It reproduced the public results and made 579 separate numerical comparisons. The author resolved the one reporting correction; the review and response remain public. Human funding and conflict information was not supplied, and no affiliation or endorsement is claimed. The source package has no redistribution licence that we could establish, so its full bytes remain outside the public repository. The study provides acquisition instructions, source hashes, narrow evidence, aggregate numerical ledgers and its own analysis code.

## Appendix A. Component and aggregate accounting

Let g_V = V_t/V_(t−1), g_X = X_t/X_(t−1), and a > 0. Under the rental-service convention, g_Q^R = g_V/a and the price ratio is a. Under the operations convention, g_Q^X = g_X/a and the price ratio is a g_V/g_X. Both satisfy g_V = g_P g_Q. Their quantity-growth ratio is g_Q^X/g_Q^R = g_X/g_V. These identities apply here because the training share is constant. A changing allocation would require training-specific spending and operations.

Let v_(j,t) denote positive nominal component amounts and s_j equal +1 for an output and −1 for an imported input. Nominal value added is Y_t = sum_j s_j v_(j,t). Given component price ratios p_(j,t), the Laspeyres factor is [sum_j s_j v_(j,t)/p_(j,t)]/Y_(t−1), and the Paasche factor is Y_t/[sum_j s_j v_(j,t−1)p_(j,t)]. The Fisher factor is their geometric mean when both factors and required denominators are positive. Chaining begins at 100 in 2023.

Because imported inputs enter with negative signs, an aggregate result cannot be read directly from the change in one component. The analysis records both Fisher factors and all component values. A change in the training price convention leaves nominal GDP unchanged; a change in the electricity used to produce output can change nominal components as well as real quantities.

For a directional check, hold all nominal components fixed and let pi be the training price ratio. The square of the Fisher factor is proportional to (V_training,t/pi + B)/(V_training,previous pi + C), where B and C collect the other components. Within the region where both required expressions are positive, lowering pi raises the numerator and lowers the denominator. The Fisher factor therefore rises. This explains why an operations convention can increase measured real GDP growth even though the audit is intended to clarify its interpretation.

## References

Bell, Peter. 2026a. *How Robust Is 2,600% AI GDP Growth? A First-Pass Sensitivity Audit of Korinek and McKelvey's AI Economy Estimate*. Version 02, June 1. https://doi.org/10.5281/zenodo.20501770.

Bell, Peter. 2026b. *Measuring the AI Economy Before GDP Can See It: A Review and Extension of Korinek and McKelvey*. Version 03, June 1. https://doi.org/10.5281/zenodo.20500501.

Korinek, Anton, and Patrick McKelvey. 2026. *Measuring the AI Economy*. Bank of Canada Staff Working Paper 2026-20, June version. https://www.bankofcanada.ca/2026/06/staff-working-paper-2026-20/.

McKelvey, Patrick, Leopold Brown, Yuval Rhymon, and Anton Korinek. 2026. *Measuring the AI Economy: Conceptual Framework and Implementation*. Technical appendix, April 27 author-hosted version. https://pmckelveyboc.github.io/technical_appendix.pdf.

Schreyer, Paul, and Belen Zinni. 2018. *Productivity Measurement, R&D Assets and Mark-ups in OECD Countries*. OECD Statistics Working Papers 2018/06. Revised document dated October 25. https://doi.org/10.1787/fb3c2e6f-en.
