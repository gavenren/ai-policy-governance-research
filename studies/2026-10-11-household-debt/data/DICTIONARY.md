# Data and output dictionary

The input is the Board of Governors' **public** 2025 SCF summary extract, released 9 October 2026. Attribution and source hashes are in [the manifest](../sources/manifest.json). The study selects 18 existing fields without changing the number of records. There are 21,800 records for 4,360 families, with five imputations (implicates) per family. These are de-identified public survey records, not private case files. All dollar values are in 2025 dollars.

| Field | Definition and use |
| --- | --- |
| YY1 | Public family identifier. |
| Y1 | Public record identifier. Y1 divided by ten with integer rounding down equals YY1; the last digit is implicate 1–5. |
| WGT | Summary-extract survey weight, already divided by five. Means use relative weights. Totals restore the factor of five within each implicate. |
| INCOME | Official annual family income, based on the previous calendar year and including pension-account withdrawals under the macro. Before tax; not disposable cash income. |
| WAGEINC | Annual wage and salary income removed in the main experiment. |
| BUSSEFARMINC | Annual business, self-employment, farm and related property income component. Removing positive values is a wider-flow sensitivity, not a pure labor-income measure. |
| KGINC | Annual capital-gain income component; positive values removed only in the wider-flow sensitivity. |
| PENACCTWD | Annual pension-account withdrawals added under the official income construction; positive values removed only in the wider-flow sensitivity. |
| TPAY | Estimated monthly debt-service burden. Includes reported and constructed payments, including balance-based credit-card and buy-now-pay-later assumptions. Some mortgage amounts can include taxes or insurance. This is not a complete list of legal minimum payments. |
| RENT | Official monthly rent estimate, included only in the explicit rent sensitivity. |
| LIQ | Transaction-account assets: checking, saving, money-market, call and prepaid accounts, under the official construction. It is narrower than all potentially saleable financial assets. |
| DEBT | Total debt balance; used for descriptive validation, not as monthly spending. |
| AGE | Age of the reference person; used for the under-65/65-plus comparison. |
| MARRIED, KIDS | Retained context fields. Not used to infer household size or a needs scale. |
| HHOUSES | Homeownership indicator, 1 or 0; not a direct measure of housing need. |
| NETWORTH | Assets less liabilities; descriptive check only. |
| NORMINC | Official usual-income measure; retained context, not substituted for INCOME. |

The original macro and codebook are the controlling definitions. [D3](../sources/snapshots/D3.md) and [D4](../sources/snapshots/D4.md) retain relevant method passages. Annual income and interview-period payments are measured at different times. Negative remaining income is set to zero in both stress cases. No family is excluded.

## Truncation and conversion checks

The numbers of families with a negative wage-only remainder, before clipping, are **98, 97, 96, 86, 92** in implicates 1–5. Wider-flow counts are **300, 311, 295, 266, 304**. Each denominator is 4,360. Weighted shares are reported in `results/diagnostic.csv`; the average wage-only share is 2.1541%, and the wider-flow share is 6.5169%. Counts were independently checked from the source and selected data.

CSV serialization introduces floating-point differences below one millionth of a dollar in checked fields. It does not create a new data release. Source and selected-data hashes are separate. No missing value remains in the selected fields. Missing replicate-weight and multiplicity entries for unselected cases are set to zero as the codebook requires. The full join is complete.

## Experiments and outputs

The main grid has three income scenarios, three thresholds, three payment factors, and five uniform transfers: 135 cases. A further five cases add rent. `results/grid.csv` and `results/rent.csv` contain the results. The `estimate` column contains proportions for shares, monthly dollars for shortfalls, or the unit stated by the metric. Multiply a proportion by 100 to display percent. `standard_error` is in the same unit; blank means not estimated for that row.

`gross_pass` compares gross resources with the chosen floor. `after_pass` subtracts the payment estimate first. `classification_gap` is the paired indicator that passes the former and fails the latter. `shortfall` is the nonnegative amount below the after-payment floor. `gap_shortfall` is that shortfall for gross-pass families, with zeros for all others. `negative_after` identifies negative after-payment resources before the positive floor. `bridge_3` and `bridge_12` identify families with a positive shortfall whose LIQ covers that many months. Their denominator is all families in the specified group, not only families with a shortfall.

`results/topup.csv` compares two targeted programmes. It is a separate policy comparison from a uniform transfer. Payment totals are gross annual dollars; recipient outcomes are proportions. Existing transfer income remains in resources. The experiment includes no tax recapture, cuts to existing programmes, or administrative cost.

`results/groups.csv` gives nine central-case groups; each denominator is recorded by implicate in `group-counts.csv`. `influence.csv` caps TPAY at each implicate's weighted 99th percentile (9,190; 9,300; 9,300; 9,500; 9,500 dollars). Ties use the first sorted value at which cumulative weight reaches 99%. The uncapped results remain primary. `descriptive.csv` contains sample-weighted means and population totals. `official-benchmarks.csv` checks two official public-data cells at published rounding precision.

`all-estimates.csv` holds all 1,345 estimands. `implicate-estimates.csv` retains each of five estimates before pooling. `replicate-estimates.csv` contains 999 estimates for each of 225 statistics with sampling uncertainty. It contains aggregate estimates, not individual replicate-weight rows. `run.json` records inputs, versions, join checks, and invariant checks. See Appendix A of the paper for the variance formula and the README for separate full and saved-estimate reproduction routes.
