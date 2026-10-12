# Tax review

**Reviewer:** separate AI agent. **Date:** 12 October 2026. **Scope:** tax definitions, accounting, source support, and clarity. This is not an official costing or human peer review.

## Initial review

The draft explains the C$1.10 trillion target correctly. It is extra revenue after a selected tax-loss shock. The target permits the original deficit. It does not balance the entire federal budget. The draft also explains that provincial losses and some future costs are outside the account.

The principal source claims are supported by the official sources recorded in `notes/tax-sources.md`. The 2025 consumption total agrees with the six-row Statistics Canada extract. The draft correctly avoids using that total as a GST base. It treats company and owner taxes as a combined charge, subtracts the replaced baseline receipts once, distinguishes total rates from rate increases, and excludes unverified wealth and royalty receipts from the package results.

The independent account check agrees with the mixed package before any required revision: 6,784 × 0.4 × 0.4 × 0.9 + 6,784 × 0.6 × 0.15 × 0.9 − 217.96 − 150 − 10 = C$1,148.44bn. The capital-only and GST-only calculations replace only their relevant existing tax receipts. The results remain conditional on bases that are not measured future Canadian tax bases.

## Required repair before publication

**Make retained credits and rebates explicit.** The draft describes the consumption base as taxable purchases before tax, and the 90% factor as tax collection. It then says existing credits are inside the base and collection assumptions. These definitions do not specify how retained fixed credits and rebates are costed when rates change. The old GST receipt of C$52.8bn is already net of relief. Subtracting it from new receipts before retained relief is accounted for can overstate new revenue.

Preferred repair: state a separate retained-relief allowance, with its date or explicit scenario status, subtract it before calculating net new resources, and update all results. This allowance must be separate from the new rebates. The capital charge also needs a clear statement that it is an effective combined federal charge after retained credits, or a separate allowance for those credits.

An alternative is to define 90% as a selected net-receipt factor after all retained relief and collection shortfalls. Then remove claims that it measures compliance or that 90% of gross legal liability is collectible. Explain that the factor is a simplifying net-revenue assumption, has not been calibrated, and can vary with tax rates and relief policy. This alternative is less transparent than a separate allowance.

## Other findings

- The paper states that the new rebates do not prove adequate buying power. It also states that protecting a fixed living standard can raise the spending target. Keep these points in the final paper.
- The capital and consumption bases are different tax stages of economic flows. They need not be disjoint pools. Do not interpret their shares adding to 100% of GDP as proof that they are independent.
- The federal capital rates exclude provincial taxes. The paper says so. Keep the need for a joint federal and provincial account clear beside the rates.
- The public-fund comparison is a scale check. State the withdrawal assumption as after tax, fees, and capital preservation; acquisition and debt costs remain separate. Replace “unlevered” with “without debt” for clearer English.
- The overall result does not establish a feasible economy-wide tax package. This limit is stated adequately. No verified source establishes the selected future base shares, receipt factors, rebates, or revenue thresholds.

**Initial conclusion:** one material definition and accounting issue requires repair. Source treatment and the other accounting boundaries are sound within the stated static scope. A follow-up check is needed after the repair.

## Final check after revision

The required repair is complete. The revised model subtracts a separate C$20bn annual allowance for retained GST credits and rebates. The paper identifies this amount as a selected assumption, not an official estimate. The old net GST receipt is then replaced once. The extra rebate remains separate. A sensitivity case raises retained relief to C$40bn. The capital charge is now defined as an average combined federal charge after tax credits and before collection losses, not a statutory rate.

An independent Decimal calculation checked all 12 package rows and all 21 stress rows. It recalculated capital receipts, GST before and after retained relief, net new resources, and the link to the federal deficit. All 33 rows agree. The separate checks of the funding thresholds and GST-only rates also agree.

| Twice-GDP case | Net new resources, C$bn | Amount above / below target, C$bn |
| --- | ---: | ---: |
| More from capital | 1,117.384 | +17.262 |
| Mixed package | 1,128.440 | +28.318 |
| More from consumption | 1,017.384 | -82.738 |

The revised GDP thresholds are about 1.97644, 1.96290, and 2.11293 times the starting level. The GST-only rates are about 75.50% at starting GDP and 37.75% at twice GDP. Capital-only rates are unchanged because that case retains the existing GST system.

**Final conclusion:** no remaining material tax-source or accounting issue was found within this review's scope. The current tables are valid as conditional arithmetic. They are not evidence that the assumed bases can coexist under these tax rates. The paper states the main limits, including uncertain relief costs, reduced buying power, provincial claims, and the absence of a household or whole-economy model.

Reviewed file hashes (SHA-256):

- `paper.md`: `0e45ffab93a3104d15424e7270ce40fbf3397c7c9ad8caf21f89fca04deded06`
- `data/inputs.json`: `8ebdad9873a4e9ef5c1645642677897902355dff5732328739f22004ce245ddb`
- `code/analyze.py`: `b70637ff4300dd1ce081f1331a3d4c4ee46c9ff3273877b2e805393b9c5ab8ad`
- `results/summary.json`: `1225f9099a7855a2dff5b52005a8d07bbfa02bed17e0839c7ce4f25372eaaf14`
