# S007 data dictionary

All inputs are researcher-selected synthetic values. They are not measurements, estimates, forecasts, confidence intervals, or a probability distribution. A period has no calibrated duration. A benefit unit is the amount of one due claim. Claims can belong to repeated persons, so claims and unique persons differ.

## Inputs

| Field | Unit and meaning |
|---|---|
| `horizon` | Number of periods; 12 in reported tables |
| `benefit` | Cash units per claim; 1 |
| `deadline` | Number of periods after arrival for the later unpaid-claim metric; 2; does not change advance timing |
| `reserve` | Additional cash units beyond due eligible funding; 30 for the grid test |
| `eligible_per_period` | True eligible claim mass due; defaults to 100 |
| `base_denials` | Eligible denied claims per ordinary period |
| `ineligible_per_period` | Ineligible denied claims per period; no intent is inferred |
| `capacity` | Review slots per ordinary period |
| `recovery` | Share of each reviewed ineligible advance returned immediately; 0 to 1 |
| `shock_start` | First shock period, indexed from 1; defaults to 4 |
| `shock_length` | Number of shock periods |
| `shock_denials` | Eligible denied claims in a shock period |
| `shock_capacity` | Review slots in a shock period; defaults to 0 |
| `denial_path`, `capacity_path` | Full paths that replace the corresponding generated path |

The optional function input `review_slot_cost` charges each reserved slot, including unused slots. The same review cost is added to funding and spending for both rules. It therefore cancels in additional cash calculations. Reported cases use zero, so a capacity comparison is not a cost-effectiveness comparison.

The raw Cartesian grid has 729 parameter tuples. When `shock_length=0`, surge size does not change a path. The model drops exact duplicate paths with the same recovery setting, leaving 567. Row IDs retain original Cartesian indices and can have gaps. Recovery settings remain distinct even when ineligible arrivals are zero. The reported grid is not a random sample.

## Outputs

`results/trajectories.csv` contains 12 named scenarios times 12 periods, or 144 rows. Each scenario-period pair is unique. `results/scenarios.csv` has one summary per named scenario. `results/stress.csv` has 567 unique path/recovery cases. Floating-point values are retained without display rounding. Internal reconciliation tolerance is 1e-8.

| Output group | Definition |
|---|---|
| `eligible_due`, `eligible_denied`, `ineligible_arrivals`, `capacity` | This period's exogenous claim and service masses |
| `reviewed_eligible`, `reviewed_ineligible` | Period service in trajectory rows; cumulative service in scenario/grid summaries |
| `backlog_eligible`, `backlog_ineligible` | Open claims after the period's review |
| `delay_claim_periods` | Cumulative eligible backlog at period ends; appeal-only rule |
| `late_eligible_claims` | Eligible mass still open at the end of its arrival period, counted once |
| `late_share_all_eligible` | Late eligible claims divided by all eligible claims due in the horizon |
| `deadline_misses` | Eligible mass still open at arrival plus two periods, counted once; cohorts with that date outside the horizon are unobserved |
| `eligible_funding_plus_review` | Cumulative due eligible benefits plus the common review budget |
| `appeal_net_outflow` | Cumulative eligible payments made after initial approval or review, plus review costs |
| `advance_net_outflow` | Initial advances and approved eligible payments, less recoveries, plus review costs |
| `appeal_earmarked_cash` | Due funding minus appeal outflow; exactly eligible arrears |
| `extra_cash_net` | Rule P cumulative net outflow above funded eligible benefits |
| `extra_cash_gross` | Rule P additional exposure after current advances and before current recoveries |
| `spending_gap` | Rule P minus Rule A spending; includes eligible arrears, so it is not the new reserve requirement |
| `permanent_loss_resolved` | Unrecovered share of ineligible advances already reviewed under Rule P |
| `unresolved_ineligible_gross` | Gross amount of open ineligible advances |
| `eventual_loss_all_arrivals` | Rule P loss if every arrived ineligible claim eventually receives review with the same recovery share |
| `deadline_extra_cash_net`, `deadline_extra_cash_gross` | Corresponding additional exposure for Rule J, which advances only claims still open at arrival-period end |
| `deadline_ineligible_advanced` | Cumulative ineligible mass that received a Rule J advance |
| `deadline_ineligible_reviewed_after_advance` | Cumulative reviewed mass within those Rule J advances |
| `deadline_eventual_loss` | Rule J loss after eventual review of all its advances at the same recovery share |
| `terminal_*` | Balance at the horizon; not written off or assumed paid |
| `peak_*` | Maximum over period rows; different peak columns can occur at different dates |

At the 12-period horizon with 100 eligible claims per period, the two-period metric can observe 1,000 eligible claims from the first ten cohorts. It cannot yet observe the final 200 claims at that threshold. No missing empirical observations exist; this is deliberate horizon censoring.

`results/run.json` records Python version, platform family, run time, model and input hashes, and hashes of deterministic result files. It contains no user-specific local path. `results/summary.json` aggregates the stress cases with unweighted case counts.
