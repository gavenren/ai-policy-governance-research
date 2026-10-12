# S011 protocol: What Remains After the Payment?

State: **Protocol**. Design recorded 2026-10-11T21:31:04Z, before calculation of study outcomes. This is an internally dated analysis plan, not an externally registered protocol. Source acquisition and schema inspection occurred first. Prior-work searching and close reading started before this record.

## Question and contribution

If wage income ends while existing debt payments continue, how often would a uniform family transfer pass a gross-resource floor but fail the same floor after recorded debt payments? What extra transfer would close that gap? The purpose is to distinguish the measured success of an income programme from the cash available after legacy debt service. The paper studies an immediate, fixed-contract transition, not a forecast of an AI economy.

The closest work already studies household financial resilience after income loss, cash support, and debt protection. Helppie-McFall and Hsu (2020) compare savings and rent/debt obligations by occupational vulnerability. Ganong and Noel (2020) distinguish payment relief from principal relief using causal evidence. Bhutta et al. (2020) simulate CARES Act support using SCF data; full text could not yet be obtained, and the comparison must remain limited to its abstract unless access improves. Laing (2023) argues that UBI needs debtor protection; the full PDF is blocked, so no claim about its detailed analysis is justified. Bhutta et al. (2019) estimate delinquency under macroeconomic stress. This study does not introduce income-loss simulation, liquidity risk, or the case for debtor protection.

The proposed addition is a transparent diagnostic of the *difference between two programme success measures*, plus the household distribution of the gross payment needed to remove that difference, under an explicit wage-cessation experiment. The diagnostic treats current contractual payments as a separate policy choice. A new survey vintage alone is not the contribution. The search cannot prove universal novelty. These questions differ from S004's scarcity model, S005's treasury reserves, S006's imported AI, S007's benefit queues, S008's purchase finance, S009's international agreement, and S010's control of public funds.

## Data and unit

Use the Federal Reserve's 2025 Survey of Consumer Finances public summary extract, release page dated 9 October 2026, and its public replicate weights. Unit: SCF family/primary economic unit, not adult or person. Include all public families and all five imputations. Report the wage-positive subgroup separately. Do not infer full household size from marital status and children, and do not present a per-family transfer as an enacted or recommended per-person UBI.

Use official public variables: identifiers YY1 and Y1; WGT; INCOME, WAGEINC, BUSSEFARMINC, KGINC, PENACCTWD; TPAY, RENT, LIQ, DEBT; AGE, MARRIED, KIDS, HHOUSES, NETWORTH, NORMINC. Preserve the official definitions and record missingness. INCOME includes previous-calendar-year income, with the official inflation adjustment; TPAY is monthly debt service near the interview. All money is in 2025 dollars. This mismatch is material. INCOME is not after-tax disposable income. Summary income components need not sum exactly to total income.

## Fixed experiments

1. Wage-only stress: remaining monthly gross resources N = max(0, INCOME - WAGEINC)/12. The zero bound is explicit. Record the weighted/unweighted incidence of truncation. This retains all other recorded flows, including capital gains, pension withdrawals, and transfers; none are promised to persist.
2. Wider-flow stress: N = max(0, INCOME - WAGEINC - max(BUSSEFARMINC,0) - max(KGINC,0) - max(PENACCTWD,0))/12. BUSSEFARMINC includes some property income. This is a broader flow shock, not a clean estimate of labor income.
3. No wage loss: N = INCOME/12 as a benchmark.

Uniform monthly transfer U in {0,1000,2000,3000,4000}. Main residual-resource floor F = 1000 per family per month; sensitivity F in {500,1500}. These are experimental thresholds, not estimates of need or poverty. Main contractual outflow D = TPAY. Sensitivity D in {0.5 TPAY,0}, interpreted as *payment reductions*, with creditor cost outside the household calculation; this is not free debt cancellation. Separately add RENT to TPAY in the main wage-only scenario to expose the omission of tenant obligations; do not claim that debt-only resources measure total housing costs.

## Outcomes

For each combination compute the share with N+U >= F (gross-resource pass), the share with N+U-D >= F (after-payment pass), their paired difference, the mean remaining shortfall max(F+D-N-U,0), and the mean payment reduction required to close the gap among those passing the gross test: max(F+D-N-U,0) times the gross-pass indicator. Report means over all families, not just affected families, with conditional means only when their denominators are explicit.

Compare idealized top-ups T0=max(F-N,0) and T1=max(F+D-N,0): report gross annual programme payments, their difference, and recipient shares. These are accounting costs, not a fiscal feasibility or tax-incidence analysis. No household consumption, default response, creditor losses, price change, or welfare gain is estimated.

For the main F=1000, U=2000 wage-only case, report results by wage-positive status, debt-payment status, reference-person age (<65/65+), and owner status. Subgroups with fewer than 100 first-implicate public families will not receive separate substantive interpretation. Record all subgroup sizes. Report whether LIQ can cover 3 or 12 months of the fixed shortfall; these are finite stock-buffer calculations, not permanent finance. Include paired policy changes, not independent standard errors of differences.

## Uncertainty and validation

Point estimates are the average of five weighted implicate estimates. WGT in the summary extract is already divided by five; multiply by five for totals within one implicate. Do not treat five records as five families. Match first-implicate data to replicate weights by verified identifiers, never row order. Construct 999 weights as WT1B_j * MM_j. Follow the SCF codebook MEANIT method: sampling variance is the sample variance of the 999 replicate estimates; imputation variance is the sample variance of five implicate estimates; total variance is sampling variance + (6/5)*imputation variance. Report standard errors for the central shares and means and important paired differences. Approximate intervals describe survey uncertainty conditional on the scenario, not uncertainty about future AI effects. Do not run causal regressions or assign an AI exposure score.

Check uniqueness, five implicates per family, join completeness, all 999 replicates, finite and nonnegative payments and weights, unit conversion, source hashes, monotonicity in U and D, exact gap decomposition, and reconstruction of official descriptive quantities where an appropriate public benchmark is available. Test at least one hand-worked synthetic family and a nonzero sampling/imputation variance fixture independent of the production calculations. Inspect extreme influence on dollar means and report sensitivity with the top 1% of TPAY capped at the weighted threshold; preserve uncapped primary estimates. If thresholds are tied, document the quantile convention.

## Reproduction, stopping, and review

Save permissible selected public data, all generated tables, code, exact source hashes, acquisition records, and method notes. Retain original downloads separately from extracted text. Keep full replication acquisition separate from offline analysis. Retain replicate estimates so published standard errors can be reconstructed without downloading the weight file; full recomputation from public microdata and weights must remain available through the acquisition recipe. Clearly disclose any part requiring a fresh download.

Stop expansion once the fixed grid, central decompositions, sampling checks, influence sensitivity, primary-source comparison, and independent AI critical review are complete. A small or zero discrepancy is a valid finding. If data or source issues prevent the central comparison, retain working notes instead of a completed paper. All deviations must be dated before or after the relevant result as appropriate. No current law or legal effect is inferred from the experiment.
