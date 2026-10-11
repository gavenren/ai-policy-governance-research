# Design decisions and deviations

- 2026-10-11T21:25:34Z: Protocol recorded after conceptual development and initial source reading, before offline implementation. Exploratory study; no preregistration claim.
- 2026-10-11T21:27:34Z: Model and first tests had run. The public source extracts and source metadata were prepared. The initial model covers a specified stationary agreement, not all repeated-game equilibria.
- 2026-10-11T21:28:20Z: A final source check added Bova, Müller, and Harack (2021), whose model already treats incentives to join a windfall clause. The manuscript's novelty statement was narrowed accordingly. No numerical input changed because of this source.
- During drafting: the deposit financing was made explicit as a matched loan and escrow asset. On orderly exit, return of the deposit repays the loan. On default, the provider loses the asset but must repay the loan. This is the cash-flow foundation of the code's recurring carry cost and one-time default penalty. No additional principal writeoff enters compliant-period payoffs. The external enforcement assumption is explicit.
- During drafting: carrying cost was separated conceptually from global resource loss. Lender receipts can be someone else's income. The paper makes no quantitative global welfare claim based on subtracting all interest as a resource cost.
- During drafting: source acquisition code was replaced with a non-overwriting recapture recipe. The original captures and published ledger retain their actual dates and hashes. Running the recipe creates a new private timestamped folder and does not rewrite the study's evidence.
- Numerical precision: values within the 1e-9 feasibility tolerance can differ slightly from exact boundaries. The main text rounds results and supplies exact hand fractions for pivotal examples.

The timestamps above identify recorded milestones or actual source acquisition. Untimed drafting decisions are not assigned invented exact times. The model inputs were recorded before the first main grid run; named scenarios were selected as explanatory theory checks, not as a representative sample.
