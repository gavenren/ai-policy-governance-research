# Benefit-unit extension data dictionary

The extension joins the public full SCF file E1 to the unchanged S011 selected summary data by YY1 and Y1. It has 21,800 records and 4,360 families, each in five implicates. These are de-identified public survey data. No private case file is used.

`roster.csv` retains 42 public fields. YY1 and Y1 are family and implicate-record identifiers. X7001 is primary-economic-unit size; 12 means 12 or more. X101 is the number of household-listing members under the codebook rule, with the same top code. X7020 indicates whether a spouse or partner is in the PEU (2=yes, 1=no). X42001 is the full-file weight, retained for a check. The analysis uses the original summary WGT times five, as in S011. The maximum full-file versus reconstructed-weight difference is 0.0000025, due to numeric storage and conversion.

The roster's ordered positions and variable names are:

| Position | Relationship | Public age | Financial dependence |
| --- | --- | --- | --- |
| 1 | X8020 | X8022 | X8098 |
| 2 | X102 | X104 | X107 |
| 3 | X108 | X110 | X113 |
| 4 | X114 | X116 | X119 |
| 5 | X120 | X122 | X125 |
| 6 | X126 | X128 | X131 |
| 7 | X132 | X134 | X137 |
| 8 | X202 | X204 | X207 |
| 9 | X208 | X210 | X213 |
| 10 | X214 | X216 | X219 |
| 11 | X220 | X222 | X225 |
| 12 | X226 | X228 | X231 |

A dependence value of 1 includes a person in the PEU; 5 means independent; 0 means inapplicable. The code checks that included persons have nonzero relationships and ages, that the reference person is included, and that position 2 agrees with X7020. Position 2 is reserved for a spouse or partner. Public relationship groupings are not used to decide adult status.

For positions 3–12, the public age scheme groups ages through 3, 4–6, 7–12, 13–17, and 18–25, then rounds older ages. This preserves the under-18 versus adult split. It does not preserve the age-14 boundary. Reference and spouse ages are top-coded at 95. No included person has a missing age, and no family has zero adults. PEU_SIZE is the count with dependence=1; it matches X7001 in all records. ADULTS counts included persons with public age at least 18. The number of children in this extension is PEU_SIZE minus ADULTS; it is not the summary KIDS field.

The primary `exact` sample excludes two top-coded families per implicate. The `capped` sensitivity uses all records but interprets size and adult count as the published roster, not the unknown true number for top-coded units. It is not a lower or upper bound on any national result.

All financial inputs, the wage-only stress and the debt-payment measure retain [the original dictionary](../../../data/DICTIONARY.md). No original fields or results are changed.

## Outputs

`outcomes.csv` reports family-weighted gross pass, after-payment pass, their paired difference, and monthly dollar shortfall. The supplementary `person_failure` weights each family outcome by its PEU members as well as its survey weight. `contrasts.csv` gives left minus right for all three arm pairs. Signs depend on the metric: a higher pass rate is better under the stated test; a higher shortfall is worse. The classification gap is a diagnostic and has no general welfare ranking.

`allocation.csv` reports the monthly dollar coefficient per allocation unit and annual gross transfers. Coefficients are fitted separately in all five implicates and all 999 replicates. Equal budgets apply within each estimation sample, not across the exact and capped populations. The annual totals are additional gross payments, not net fiscal costs.

`counts.csv` records each group's unweighted and weighted family and member counts. All means include zero outcomes in the stated denominator. `implicate-estimates.csv` and `replicate-estimates.csv` retain all 192 estimands. Standard errors use the original SCF variance rule. The normal 95% intervals are unbounded approximations; they can extend outside a share's [0,1] range because they are not probability models.

`run.json` records versions, input and code hashes, joins, exclusions, the maximum relative budget error across all runs, and reproduction of four unchanged original central-case statistics.

