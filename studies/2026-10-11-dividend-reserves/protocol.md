# S005 protocol and development record

Recorded: 2026-10-11T21:03:17Z. **State: Working notes.** This is an exploratory record written during development. It is not a prospective registration.

## Question and contribution

How much initial cash protects a fixed work-independent social dividend over a finite horizon when taxes and public-fund income can fall together? When does sale of a public asset reduce or increase that cash requirement?

The intended contribution is a small, exact cash-flow certificate with a complete synthetic stress set and an explicit asset-sale decision. The study does not originate social dividends, wealth funds, liquidity buffers, or maximum-gap accounting. It is distinct from S004, which tests static real consumption access. This study contains no goods-market equilibrium.

## Units, inputs, and methods

The unit is a precommitted sale policy and complete eight-period revenue path. All numerical inputs are synthetic. There are no observed records, missing data, imputations, or estimated country parameters.

The main design uses taxes 7 or 2, full-asset income 5 or 1, payment 10, asset reference value 100, and at most three shocks per stream. All permitted binary sequences are included. Joint-allowed, no-overlap, and common-only sets are separately labeled. No probabilities are assigned. Complete enumeration is used; no seed is needed.

The policy is one sale chosen at time zero. Main-case income rights cease from period 1. Cash arrives before the payment in a stated receipt period. The proceeds include a fixed haircut. Cash has zero interest. No borrowing, further sales, new funding, or payment cuts are allowed.

The output includes the necessary and sufficient reserve, the reserve-minimizing sale, every base-case path, binding path examples, a sale grid, and sensitivity to receipt time, haircut, disposal weight, and income-rights timing. Exact rational arithmetic determines the main outputs. CSV decimals are rounded to nine places.

## Search and evidence rules

Include public primary research, official technical guidance, official fund descriptions, and original replication material that addresses public cash reserves, payout smoothing, AI revenue sharing, or fund liquidity. Exclude media reports as substantive evidence. Inspect close material beyond the search result. Record unavailable full texts and limit claims to the material read.

Short quotes must contain fewer than 25 words per source. Record original and extraction hashes. Do not redistribute the full third-party collection. Source collection ends at 2026-10-11T21:03:17Z. This is not an exhaustive coverage claim.

## Decisions and deviations

1. The dynamic reserve question was selected before implementation. S004 was read to avoid a second static floor study.
2. The early literature search found close IMF cash-buffer methods and APFC reserve-depletion analysis. Novelty was narrowed to the specified post-labor application. No mathematical-priority claim is made.
3. The base numerical choices and shock caps were selected during model development. They were not preregistered or calibrated.
4. After the first run, an alternative income-rights timing case was added. This tests whether the late-sale penalty is an artifact of immediate income loss. It is: the penalty disappears if rights remain until receipt, although the early gap persists.
5. Disposal weights were included to show that minimizing cash is not a welfare criterion. No weight is selected as correct.
6. The Prativadi main manuscript was inaccessible from SSRN. The original Zenodo package was acquired. Only its README and model specification support the comparison; its code was not executed.
7. Source searches and reading happened before this written protocol. Search issue times were not retained per query; the log states this limitation. Acquisition times of retained original bytes are exact.

## Validation and stopping rule

Ten tests check combinatorial counts, early and late shock orders with equal totals, stock limits, receipt accounting, analytic interior choices, all joint paths through a separate cash loop, income-rights timing, zero sale proceeds, failure of the no-overlap certificate under a common shock, and an independent smaller exhaustive grid.

Stop this study after its finite model, evidence package, and separate critical review are complete. A failed result is retained. A blocking review issue must be fixed or the study must remain Working notes. Final release requires source and output reconciliation, privacy and rights checks, and verification of the intended repository by the coordinating agent.
