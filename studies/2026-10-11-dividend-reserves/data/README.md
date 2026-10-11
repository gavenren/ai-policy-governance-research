# Input and output dictionary

`design.json` is a synthetic design, not observed economic data. All monetary values use a common arbitrary currency unit. A period has no assigned calendar duration.

- `horizon`: number of payments.
- `tax_normal`, `tax_shock`: collected tax cash in each state.
- `fund_income_normal`, `fund_income_shock`: net cash income from the full original asset in each state.
- `obligation`: aggregate payment due per period.
- `initial_asset_value`: maximum reference-value amount that can be sold.
- `max_tax_shocks`, `max_fund_shocks`: horizon-wide counts, not maximum consecutive runs.
- `base_receipt_period`: period in which sale cash arrives before payment.
- `base_haircut`, `haircuts`: lost fraction of reference sale value, represented by exact rational strings.
- `families`: joint allowed, no simultaneous shock, and identical shock streams.
- `sale_grid`: display values only. Optimization uses exact line intersections.
- `loss_weights`: coefficients in `reserve + weight * sale`; no welfare interpretation.

## Results

`summary.csv` has one row per family, receipt period, and haircut. `paths` is that family's complete denominator. `sale_opt_exact` and `reserve_opt_exact` are exact fractions. Decimal columns use nine places. The no-sale, sale-25, and sale-100 columns are comparator reserve needs.

`path_cases.csv` has every base-case path in each family. Shock strings have eight entries; 1 means the low-revenue state. `path_id` is unique within its family. Common paths can appear in more than one family. `chosen_path_reserve` is the minimum cash for that single path at the family's chosen sale. `min_cash_at_robust_reserve` and `terminal_cash` use the family's common reserve. A critical period of 0 means no positive cash requirement attained within the horizon. The code can also identify a zero-gap date, so 0 is not the only representation of a zero requirement.

`frontiers.csv` contains the eight stated sale amounts in each of 45 environments. `objectives.csv` contains the three stated disposal weights for each base family. `timing.csv` compares immediate loss of asset income with loss starting in the receipt period. `witnesses.csv` gives one binding path per base family, with exact post-payment cash each period. Ties are resolved by deterministic enumeration order.

`run.json` records source-code, input, and numerical-output hashes, runtime, and execution date. It contains no stochastic seed because the method does not use random sampling.
