# Case data dictionary

The unit of output is one of ten fixed illustrative cases under one of four treatments. There are 40 rows, with no missing values, exclusions, weights or population data. Currency fields use whole monthly US dollars. Their labels describe the simplified comparison only.

## Inputs

`raw/cases.csv` is a direct transcription of the frozen protocol's case table. `raw/settings.json` records the two thresholds, units, scope and frozen protocol hash.

| Field | Type | Meaning |
| --- | --- | --- |
| case_id | text | Unique protocol case name |
| y | nonnegative integer | Other countable household income, held fixed across treatments |
| d | nonnegative integer | Illustrative new cash amount; no-payment treatment pays zero |
| A | boolean | Whether the lower requirement applies in this case |
| E | boolean | Whether another independently verified route satisfies the lower requirement |
| purpose | text | Protocol reason for retaining the case |
| upper_ceiling | nonnegative integer | Illustrative upper input, fixed at 1,800; not an actual Medicaid threshold |
| lower_threshold | nonnegative integer | Protocol lower input, fixed at 580; not an individual eligibility finding |

## Treatments

| treatment | Cash received | Income for upper check | Income for lower route |
| --- | ---: | ---: | ---: |
| no_payment | 0 | y | y |
| counted_cash | d | y + d | y + d |
| shared_disregard | d | y | y |
| proposed_split | d | y | y + d |

The proposed split is a proposed federal treatment for comparison. The code does not establish authority to implement it. Cash counted in an income test is not a claim that the recipient worked any hours.

## Additional output fields

`../results/cases.csv` repeats each case's inputs and includes its treatment and thresholds. CSV booleans are lowercase `true` and `false`.

| Field | Type | Meaning |
| --- | --- | --- |
| cash_received | integer | Zero in the no-payment case; otherwise d |
| income_for_upper | integer | Input to the illustrative upper check |
| income_for_lower | integer | Input to the lower-income route |
| upper_pass | boolean | Income for upper check is at most upper_ceiling |
| lower_income_route_pass | boolean | Income for lower route is at least lower_threshold |
| lower_requirement_pass | boolean | The requirement is inapplicable, another route is verified, or the income route passes |
| combined_pass | boolean | Both upper_pass and lower_requirement_pass are true |

`lower_income_route_pass` can be false while `lower_requirement_pass` is true. This occurs if the requirement is inapplicable or another route is verified. Another route does not remove the separate upper check. `combined_pass` is only the conjunction of these two simplified checks. It is not legal eligibility or enrollment.
