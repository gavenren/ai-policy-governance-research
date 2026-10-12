# S018 numerical data dictionary

All cash amounts are billions of model US dollars. The source describes its floor as not indexed but also gives a general 2026-dollar convention. This audit preserves the source values without resolving that price-basis convention; it does not establish real purchasing power. These are generated model paths, not observed government revenue or claimant records. No source parameters are recalibrated. No confidence interval or probability calibration is supplied.

## Inputs

`source-hashes.json` pins the two unchanged vendor scripts. They come from Four Pillars commit `d0e84f01f7970c6161da874051aafffaefe77f1f`. The source ledger gives attribution and the retained MIT code licence. `printed-targets.json` contains 28 claims fixed before execution: eight year-1/year-10 values from whitepaper section 6.2, and four values in each of five rows from section 6.4. Each record states the source text, section, cohort, policy, field, scale and display format. A minus glyph and currency notation are normalized only for numerical comparison; the source wording is retained in `source_printed_text`.

## Paired path audit

`../results/paired-paths.csv.gz` contains all 60,000 cohort-path-year rows: 2,000 ten-year paths and 2,000 twenty-year paths. Each row holds the two policy outcomes, for 120,000 policy outcomes. Gzip metadata uses a zero timestamp. There are no missing records or exclusions.

| Field | Meaning |
| --- | --- |
| cohort | `ten` or `twenty`, identifying the source script and simulation cohort |
| path | One-based path number within that cohort; not a matching identifier across cohorts |
| year | One-based source year, 1–10 or 1–20 |
| revenue_billion | Same retained source revenue for both policies |
| nonfloor_billion | Source total outflows less its actual floor payment |
| health_federal_billion | Combined healthcare and federal-operations costs recovered by also removing grown pillar and administration costs |
| source_floor_billion | Actual source floor: triggered in `ten`, fixed at 4,620 in `twenty` |
| fixed_floor_billion | 4,620 under the fixed nominal policy |
| trigger_floor_billion | The original two-stage rule replayed on the same source inputs |
| fixed_gap_billion | Revenue minus non-floor costs and the fixed floor |
| trigger_gap_billion | Revenue minus non-floor costs and the triggered floor |
| additional_floor_billion | Triggered floor minus 4,620; equal to the reduction in the budget gap |

The trigger starts again at 4,620 each year. From year 5, coverage strictly above 0.95 raises it by 12%. From year 8, coverage strictly above 0.98, recomputed after the first stage, sets it to 120% of base. The denominators retain the source's base pillar-plus-administration amount of 850 rather than the grown amounts used in total outflows. A prior year's increase is not carried forward. The source code and the audit use the same floating-point arithmetic.

## Aggregate outputs

`summary.csv` has 60 rows: two policies for each of ten and twenty cohort-years. `paths` is 2,000 in every row. `revenue_p50_billion`, `outflow_p50_billion`, `auto_tax_p50_billion`, and `vat_p50_billion` are upper-middle order statistics. `gap_p10_billion`, `gap_p50_billion` and `gap_p90_billion` use sorted index `int(n*p)` with zero-based indexing. They are distribution quantiles, not confidence bounds. For n=2,000, the median is the 1,001st sorted value.

`surplus_fraction` counts gaps strictly greater than zero, divided by 2,000. `mean_floor_billion` is the arithmetic mean floor payment. `base_count`, `level28_count` and `level30_count` count the three floor levels 4,620, 5,174.4 and 5,544. The latter two field names follow the source's comments about $28,000 and $30,000 benefit levels; they are counts of model paths, not people. Divide by `paths` to obtain their frequencies.

`paired-summary.csv` has 30 cohort-year rows. `mean_extra_floor_billion` is the mean additional payment under the trigger; `mean_gap_reduction_billion` is the mean of fixed gap minus trigger gap. `crossing_count` counts paths with a fixed-policy surplus and a trigger-policy gap at or below zero. `fixed_to_trigger_surplus_reduction_pp` is 100 times this count divided by 2,000. `reverse_crossing_count` is zero under the checked accounting rule. These are within-cohort comparisons. A shared seed does not pair corresponding path numbers across different source horizons.

`printed-checks.csv` adds the full-precision computed value, formatted value and match flag to every preselected printed target. The section 6.2 year-10 55.7% target is compared with the ten-year trigger policy. The separate section 6.4 year-10 55.7% target is compared with the twenty-year fixed policy. The one mismatch is retained; no source claim is replaced.

The unchanged extended script also prints its existing land-value-tax scenario. That console text is preserved to keep the source execution complete. It is not a selected policy in this audit and has not been validated here.
