# Data dictionary

All inputs are synthetic. There is no sample of countries, observed displacement, or estimated probability distribution.

`design.json` fixes the inputs for `code/model.py`. State 0 is normal; state 1 is adverse. All resource quantities are in a common real numeraire per period. Population is normalized to one in the experiments. A period has no calibrated length.

| Input | Meaning |
| --- | --- |
| `discount` | Provider government's effective one-period discount factor, at least zero and below one. Not equated to the loan interest rate. |
| `persistence` | Probability of staying in the same state. The two-state transition matrix is symmetric: `[[q,1-q],[1-q,q]]`. |
| `gain` | Provider fiscal benefit from the recipient service, relative to no service. This is lost on permanent termination. |
| `cost` | Recipient resource cost of supplying that service. Reimbursed separately from household support. |
| `own_income` | Recipient support resources that remain available outside the agreement. |
| `provider_resources` | Provider resources that remain available outside the agreement. No effect on the payment incentive unless they relax another constraint. |
| `domestic_minimum` | Minimum current provider resources retained after payment and deposit carrying cost. A requirement for the compliant treaty budget. It does not restrict exit/default actions or give domestic spending legal priority over the lender. |
| `population` | Recipient population measured in normalized person units. |
| `target_floor` | Proposed real household resources per normalized person. |
| `bond_cap` | Maximum principal of a financed deposit. Deposit principal is an asset matched by a loan, not new net wealth. |
| `carry_cost` | Per-period provider fiscal cost per unit of deposit; can include interest or funding spread plus real administration. The sum is not assumed to be a global resource cost. |
| `transition` | Optional explicit stochastic matrix for general finite states; used in a one-state test. It replaces `persistence` when supplied. |

`results/named.csv` has nine scenarios. `grid.csv` has 648 parameter combinations. `persistence.csv` has 101 values from 0 to 1 inclusive. The stationary distribution is one half for each state when 0 < q < 1. At q=0 the process alternates; at q=1 each state is absorbing. The all-state test still applies, but these endpoints do not imply convergence to an equal long-run sample frequency from every starting state.

| Output | Meaning |
| --- | --- |
| `maximum_floor` | Supremum feasible floor within the specified stationary agreement and optional deposit class, found by 75-step bisection. Blank/JSON null means no feasible agreement even at zero floor. Values within numerical tolerance of zero should be read as zero. |
| `target_feasible` | Whether the deposit interval is nonempty for the target floor in every state. |
| `least_bond`, `largest_bond` | Bounds on the feasible deposit interval at the target. Blank means no feasible interval. |
| `mean_net_before_bond` | Arithmetic mean of provider cooperation gain minus required transfer before deposit cost. In the symmetric interior cases this is also the stationary mean. |
| `min_provider_value` | Lowest state-specific discounted provider gain at the least feasible deposit, if one exists; otherwise at zero deposit. |
| `min_enforcement_margin` | Lowest current default penalty plus discounted future value minus required transfer, with the same deposit convention. |
| `min_domestic_margin` | Lowest provider resources minus transfer, carrying cost, and domestic minimum, with the same deposit convention. |
| `bond_marginal_enforcement` | Change in payment margin per extra unit of deposit: `1-discount*carry_cost/(1-discount)`. |

`state_details.csv` reports each named case at zero, the cap, and the least feasible deposit when available. Identical deposit choices are deduplicated. `provider_net` is current gain minus transfer and carry cost. `provider_value` is its discounted value. `continuation` is the discounted expected next-period value. `enforcement_margin` is `bond + continuation - transfers`. `domestic_margin` is `provider_resources + gain - transfers - carry_cost*bond - domestic_minimum`. `household_resources` is `own_income + transfers - cost`. `recipient_net` is `transfers - cost`. No value is a calibrated welfare measure.

Floating-point tolerance for feasibility is 1e-9. Reported floor boundaries can exceed an exact theoretical boundary by that numerical tolerance. Tests use 100 pseudo-random cases with fixed seed 901 only to compare numerical methods; those cases are not economic data. Main results contain no random sampling.
