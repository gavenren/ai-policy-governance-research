# Separate methods review: S011

**Reviewer:** separate internal AI agent. The reviewer did not write the central analysis. This is not human or journal peer review.

**Initial review completed:** 2026-10-11T21:39:29Z. [Exact reviewed hashes](methods-reviewed-hashes.json) identify the files. This is a methods review before the completed manuscript and evidence package were supplied.

## Decision

No error was found in the central estimates or their standard errors. The original-weight run reproduces all generated CSV files exactly. The saved-estimate route reproduces all point estimates; its largest standard-error difference is `1.592e-17`, from numerical round trips. All ten tests pass.

Two issues require a response before release: the description of TPAY must match its constructed definition, and the saved-estimate run must not claim to have checked the original weight join. Other interpretation and reporting points are below. The complete paper still requires a claim check.

## What was read and run

Read the prospective protocol, its design-freeze record, the analysis and test code, selected data, all result schemas, the failed-run note, and the official SCF documentation. The protocol's current hash matches the saved design-freeze hash. This confirms the retained version; it is not external verification of preregistration.

Inspected the official codebook's sampling section and MEANIT procedure, the standard-error guide, the summary-variable macro, the SCF release page, and the official benchmark workbook. The retained original hashes for D1, D2, D3, D4, D5, D6, and D8 match the acquisition record. The selected CSV has 21,800 records for 4,360 public families, with five distinct implicates per family. It matches the corresponding original-source fields within floating-point conversion error; the largest absolute discrepancy is about `1.863e-9` dollars.

Executed these commands with Python 3.12.14, NumPy 2.3.5, and pandas 2.2.3. The portable name `python3` below refers to the runtime used; the system Python without these dependencies could not run the analysis.

```sh
python3 studies/2026-10-11-household-debt/code/analysis.py --weights .local-sources/household-debt/D2/p25_rw1.dta --output .local-verification/s011-review/full
python3 studies/2026-10-11-household-debt/code/analysis.py --saved-replicates studies/2026-10-11-household-debt/results/replicate-estimates.csv --output .local-verification/s011-review/offline
python3 -m unittest discover -s studies/2026-10-11-household-debt/code -p 'test_*.py' -v
python3 studies/2026-10-11-household-debt/reviews/independent-methods-check.py --weights .local-sources/household-debt/D2/p25_rw1.dta --source-csv .local-sources/household-debt/D1/SCFP2025.csv
```

The final command is a separate check that does not import the author's analysis functions. It computes the three central outcomes directly from the original public CSV. It reconstructs all 999 original replicate weights, joins by verified family identifiers, and uses explicit sums of squared deviations. See [check code](independent-methods-check.py) and [check results](independent-methods-check.json).

## Weighting and uncertainty

The official macro sets `WGT=X42001/5`. Multiplication by five within each implicate is therefore correct for population totals. Means are estimated within each implicate, then averaged. The five records are not treated as five independent families.

The official codebook specifies replicate weights multiplied by their matching multiplicities. It also sets missing weights and multiplicities to zero for families not selected in a replicate. The independent check found 1,203,591 such cells, with matching missingness patterns. The first-run correction implements that documented rule and does not drop a family.

The codebook MEANIT example estimates sampling variance on the first implicate using 999 replicate estimates, with denominator 998. It estimates imputation variance across the five implicate estimates, with denominator four, and combines them as sampling variance plus 1.2 times imputation variance. The code and independent check follow this procedure. Standard errors measure survey uncertainty conditional on the scenario; they do not measure uncertainty about AI development or economic adjustment.

## Independent numerical checks

| Outcome | Independent estimate | Independent standard error |
| --- | ---: | ---: |
| Central classification gap | 22.8974226% | 0.5755476 percentage points |
| Central monthly shortfall, mean over all families | $401.668362 | $16.715182 |
| Extra gross annual payment under the debt-adjusted targeted top-up | $1,336,078,529,991 | $34,065,426,626 |

All agree with the saved results. The first two use the uniform monthly transfer of $2,000 and a residual floor of $1,000. The third compares two idealized targeted top-ups; it is not the annual cost of filling the shortfall under that uniform transfer.

The central gross-resource pass rate is one by construction: the transfer exceeds the floor and remaining resources are nonnegative. The empirical result is the distribution of the measured payment burden relative to that margin. The no-loss and wider-flow comparisons keep that scenario dependence visible.

Read the official workbook cells independently. Table 1, cell AI7, reports income in thousands; Table 13, cell H7, reports a percentage. After conversion, the reconstructed mean income and debt-holder share match the published rounded values. All substantive subgroup counts exceed the protocol's 100-family cutoff. The observed grid also passes monotonicity checks for both larger transfers and smaller payment burdens.

## Issues for the manuscript and release

1. **Payment measurement.** TPAY is a constructed monthly payment measure. The official macro assumes credit-card payments of 2.5% of the balance, BNPL payments of 33%, and margin-loan interest at an 8% annual rate; it sets the other-loan payment item to zero. Mortgage inputs use reported payments and can include tax or insurance escrow. Do not describe every dollar as an observed, legally required creditor payment. Holding TPAY fixed is a payment-burden stress test. A 50% reduction is a mechanical outflow sensitivity, not a demonstrated legal debt-relief programme.

2. **Run metadata.** The reviewed code sets `complete_weight_join=True` on both routes. The saved-replicate route does not load or join original weights. It must report that the join was not rerun. The full-weight join itself passed.

3. **Influence cap.** Each implicate uses its own weighted 99th-percentile TPAY cap, ranging from $9,190 to $9,500. The initial influence table's single cap label came from the first implicate. Report the rule and range. The capped mean shortfall is $374.263, while the classification gap remains about 22.8424%; this supports a qualified robustness statement, not proof that tail measurement is harmless.

4. **Unit and resource meaning.** These are SCF families or primary economic units, not people. The transfer is a uniform family amount. Remaining resources are constructed from gross previous-year income and payments near the interview, in a common dollar basis. Income components need not sum to total income. The wider-flow scenario removes mixed business and property income and some asset withdrawals; it is not a clean measure of all labor income. Retained capital gains and withdrawals are not assured recurring resources.

5. **Policy interpretation.** Debt-only residuals do not measure living standards or a sufficient consumption floor. Rent, taxes, care, household size, repayment adjustment, and behavioral responses remain separate. Payment relief has creditor and fiscal effects outside this calculation. Principal repayment can also change household wealth. The gross annual top-up is an accounting flow, not a net fiscal cost, welfare estimate, or estimate of national resources lost to debt.

6. **Paired comparisons.** The classification-gap standard error is computed from the family-level paired outcome. If the paper reports uncertainty for further differences between shock or payment policies, those differences also need paired replicate calculations. Marginal standard errors must not be combined as if policies involved independent samples.

## Review limits

This review checks the implemented accounting experiment and its survey method. It does not validate a future AI economy, estimate causal effects, establish a sufficient income level, or certify the novelty of the full paper. The complete manuscript, literature comparison, rights record, public source package, and release gates were not yet final. No central code was edited by this reviewer. A final claim check and an issue-by-issue author response remain necessary.


## Follow-up: full manuscript and corrected code

**Review time:** 2026-10-11T21:43:03Z. This section extends the initial review; it does not replace the earlier findings.

Read the full manuscript and checked its equations, three main tables, and reported sensitivity results against the retained result files. All table values and stated survey standard errors agree after the stated rounding. The subgroup denominators, rent sensitivity, savings shares, floor sensitivities, payment reduction, influence cap, no-loss comparison, wider-flow comparison, and targeted recipient shares also agree. The hand-worked opening example is correct.

The manuscript now makes TPAY's constructed definition explicit. It separates the uniform-transfer shortfall from the difference between targeted top-ups, states that the 100% central gross pass rate is mechanical, and keeps gross cash flows separate from net fiscal or welfare cost. The limits on family units, income timing, before-tax resources, nonadditive components, retained asset withdrawals, and a debt-only living-standard measure are clear. The conditional policy discussion does not claim that its payment reductions are legally feasible or that a family would default when it fails the test. It does not report unsupported significance tests for differences between policies.

The final code's metadata changes were also checked by fresh runs:

```sh
python3 studies/2026-10-11-household-debt/code/analysis.py --weights .local-sources/household-debt/D2/p25_rw1.dta --output .local-verification/s011-review/final-full
python3 studies/2026-10-11-household-debt/code/analysis.py --saved-replicates studies/2026-10-11-household-debt/results/replicate-estimates.csv --output .local-verification/s011-review/final-offline
python3 -m unittest discover -s studies/2026-10-11-household-debt/code -p 'test_*.py' -v
```

The original-weight run completed at 21:41:27 UTC. Every generated CSV file matches its saved counterpart byte for byte. The saved-estimate run completed at 21:41:25 UTC, with identical point estimates and a maximum standard-error difference of `1.592e-17`. It now correctly reports that it did not repeat the original weight join. All ten tests pass. The influence metadata now names the first-implicate cap and states the separate-cap rule. These changes resolve initial issues 2 and 3; the revised payment description resolves issue 1.

For version clarity, the first runs used analysis SHA-256 `7734819536c4160ec6ab19fcda80889bb134d158f6dd8743c48df63bd1acb93e`. The final runs use `7cd275b422de41bc7c111e9badbce806e860a7193ba0f5dac208b855d87d923b`. The first hash list was saved while the author made the metadata changes, so it already listed the second code hash. The run records establish which version each run used. Both stages are now identified in the hash record.

The prior-work check covered the retained methods and introduction passages in P1, P2, and P4, and the retained publisher abstracts for P3 and P5. A fresh read of [P6 on the FRBSF website](https://www.frbsf.org/research-and-insights/publications/economic-letter/2021/07/how-much-did-cares-act-help-households-stay-afloat/) confirms its SIPP-based calculation of temporary support from nonemployment resources. These sources establish the broader ideas of income-loss simulation, liquidity support, and debtor protection. The paper correctly limits its addition to comparing programme success measures and conditional top-ups in the post-labor setting. The reviewer did not obtain the two blocked full texts, conduct an exhaustive new literature search, or establish universal novelty.

One wording issue was sent to the author: Section 7 said the calculation did not subtract existing programmes. Existing transfer income remains in the residual resources and already lowers the top-up. The intended statement should instead say that the model includes no cuts to those programmes or tax recovery. The author corrected the sentence, and the reviewer checked the new wording. It now states both points clearly. This resolves the issue without a numerical change. The final source package and its links still need to be checked before closing the review.


## Source-review closure

At 2026-10-12T07:52:27Z, the final source review was completed. See [the final critical review](critical-review.md) for its actual checks, four resolved source-record issues, rights scope, and remaining limits. The earlier pending-source statement describes the earlier stage. The central analysis and its numerical results did not change.
