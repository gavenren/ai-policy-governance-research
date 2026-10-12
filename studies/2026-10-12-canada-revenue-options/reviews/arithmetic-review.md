# Independent arithmetic review

**Date:** 12 October 2026  
**Reviewer:** separate AI reviewer  
**Result:** all tested calculations pass for the revised model with explicit retained GST relief. This is not human peer review or an official revenue estimate.

## Method and scope

The reviewer read the input file and output tables. The check did not import or call the model's functions. It used Python `Fraction` arithmetic to form exact rational numbers. It reconstructed the full federal revenue and expense account, then calculated the difference from the starting deficit. It checked the borrowing results with the closed-form compound-interest equation.

The review checked:

- All 12 package rows and all 21 stress rows, including each row's tax bases, rates, receipts before and after retained GST relief, new resources, gap, total revenue, total expense, and deficit. The expected cases are all present without duplicates.
- All three break-even GDP rows.
- All four single-source rows. Capital-only keeps the old net GST unchanged. GST-only deducts the selected retained relief from its new receipts.
- All three public-fund asset requirements.
- All ten borrowing rows, including interest on opening debt.
- The source target, retained receipts, and total expense against the prior Canada study.
- The input-file hash, source-paper hash, and source-result hash.
- The two wealth scale comparisons in the result summary.

There were 756 numerical comparisons. The tolerance was C$1e-20bn, or the same numerical tolerance for rates. Exact rational calculations and the output's rounded Decimal calculations differ by less than this limit. No arithmetic error was found.

## Correct central results

At twice the starting GDP, the annual net new resources are:

| Case | Net new resources | Margin above the C$1,100.12195433bn target | Federal deficit after the package |
| --- | ---: | ---: | ---: |
| Capital-heavy | C$1,117.384bn | C$17.26204567bn | C$54.53795433bn |
| Mixed | C$1,128.440bn | C$28.31804567bn | C$43.48195433bn |
| Consumption-heavy | C$1,017.384bn | −C$82.73795433bn | C$154.53795433bn |

The source account also balances exactly:

C$1,467.68195433bn expense − C$295.76bn retained revenue − C$71.8bn deficit = C$1,100.12195433bn new revenue needed.

The reform replaces C$165.16bn of capital-related receipts and C$52.8bn of GST receipts. It keeps the other C$77.8bn. The model subtracts each replaced stream once. It deducts the selected C$20bn retained GST relief allowance before replacing the old net GST line. The new rebate and new tax administration cost are each deducted once. The added stress case raises retained GST relief to C$40bn.

## Manuscript check

The reviewer checked the revised manuscript against these results. Its target account, twice-GDP table, four GDP cases, mixed-package stress cases, funding thresholds, single-source rates, public-fund scales, and ten-year borrowing example agree at the stated rounding. No incorrect numeric claim was found.

The manuscript states the funding thresholds as results under fixed assumptions. It does not state that those economic sizes or tax receipts are forecasts. It correctly states that the two packages which pass the target still leave federal deficits.

The revised definitions keep capital tax credits inside the selected average capital charge. The 90% collection factor is applied afterward. GST has a separate selected C$20bn retained-credit allowance, followed by a separate new rebate. This makes the assumed relief visible. It does not prove the allowance is sufficient for current or future obligations.

For the single-source example, 104.4% is the required capital assessment rate before the 10% collection reduction. The manuscript now states that distinction. It remains a warning calculation, not a feasible policy claim.

## Limits of this result

Passing these checks proves the arithmetic for the selected inputs. It does not prove that the tax bases, rates, GDP, collection shares, rebates, or service allowances can be achieved. The model does not measure household effects, provincial funding needs, price changes, or the effect of one tax on another tax base. The manuscript keeps these limits clear.

**Reviewed input SHA-256:** `8ebdad9873a4e9ef5c1645642677897902355dff5732328739f22004ce245ddb`
