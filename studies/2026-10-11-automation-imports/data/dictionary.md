# Inputs and output units

All inputs are synthetic. They are not sampled from country data. No probability or confidence level attaches to a grid count.

| Field | Definition and unit |
| --- | --- |
| `A` | Marginal domestic output from the first AI input unit; final-good units per AI unit |
| `c` | Foreign marginal cost intercept; final-good units per AI unit |
| `b` | Decline in domestic marginal product per extra AI unit |
| `d` | Increase in foreign marginal cost per extra AI unit |
| `theta` | Inherited public share of domestic profits; fraction in [0,1) |
| `efficiency` | Usable public share of actual levy payments; fraction in (0,1]; missing share is real resource cost |
| `fixed_cost` | Annual real resource cost when a positive levy operates; zero at no levy |
| `recipients` | Share of residents who own no assets; 0.8 in all reported experiments |
| `tax` | Actual wedge per AI input unit; final-good units per AI unit; not a percentage |
| `funding_targets` | Additional transfer budget per total resident relative to each state's no-levy baseline |
| `withdrawal_tax_caps` | Hypothetical maximum permissible wedge; no strategic withdrawal estimate |
| `robust_search_iterations` | Bisection iterations on the common funding target; no random sampling |

`q0=(A-c)/(b+d)` and `pass_through=b/(b+d)`. An input unit is stable within a case; it is not a token definition. `code/model.py` restricts levies to [0,A-c]. A levy above this choke point is not analyzed.

`scenarios.csv` has nine named rows. `grid.csv` has all 216 states at all six tax levels (1,296 rows). `state_boundaries.csv` has the continuous optimum for each state. `robust.csv` has the largest common uplift and a common tax for each named state set. `feasible_intervals.csv` reports 30 set-target comparisons. `withdrawal_caps.csv` has four imposed access limits. `summary.json` contains manuscript counts. `run.json` records software, actual run time, and hashes.

Important output fields:

- `gross_levy_payments = tax * imports`: payments made by domestic AI users.
- `usable_levy_receipts = efficiency * gross_levy_payments`: after variable collection costs, before fixed cost and other revenue displacement.
- `displaced_domestic_revenue`: public share of lost domestic profits.
- `public_income`: all funds available to recipients, after both cost terms.
- `net_funding`: change in public income from the same state's no-levy baseline.
- `recipient_consumption`: public income divided by recipient share; units per recipient.
- `owners_total_consumption`: private domestic owner's consumption per total resident.
- `domestic_consumption`: sum of recipient and owner consumption per total resident.
- `domestic_change`: change in that sum. It is not the same as a recipient's change.
- `foreign_producer_surplus`: foreign receipts minus foreign resource cost.
- `global_change`: change in domestic consumption plus foreign producer surplus.
- `resource_residual`: output minus foreign payment, real costs, and domestic consumption. It should be approximately zero.

Amounts are annual final-good units per total resident, except prices, tax, input quantity, and the explicitly per-recipient field. Boolean interval fields distinguish a positive levy from the zero-levy option. Empty endpoints mean no positive-tax interval. There are no missing empirical observations. Python float rounding uses 1e-9 comparisons in interval and count routines. A computed boundary can exceed an exact endpoint by less than this tolerance; tables round to four decimals.

A higher public-share state has a different baseline transfer. Comparing net uplifts alone is not a comparison of final recipient living standards. Negative funding changes in the grid mean a smaller positive transfer, not negative consumption. The reported grid's minimum public income is zero.
