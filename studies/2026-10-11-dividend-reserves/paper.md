# Cash Before Capital
## A Reserve Test for Social Dividends After Human Labor

> **State:** Complete-study draft — executed analysis and separate internal AI review complete. No human peer review.
> **Study ID:** S005 (`2026-10-11-dividend-reserves`). **Date:** 11 October 2026.
> **Evidence cutoff:** 2026-10-11T21:03:17Z. This is the end of source collection, not a claim of full literature coverage.
> **Method:** Conditional analytical model and complete deterministic enumeration of synthetic cash flows. No country forecast.
> **AI assistance:** Codex conducted the research, analysis, code, and writing. No human review has occurred. No affiliation or endorsement is claimed.
> **Rights:** No repository reuse licence has been selected. Third-party source rights are separate.

## Abstract

An economy can own valuable AI assets and still miss a payment to its residents. This paper asks how much cash protects a fixed social dividend when taxes and public fund income can fall together. The model has a finite payment horizon, an initial productive asset, and one planned sale. Sale cash arrives after a stated delay. Sold assets cease to pay income. An exact reserve test checks every payment date and every permitted shock path. Its maximum of affine cash gaps makes the required reserve a convex function of the sale amount. The study enumerates 8,649 joint-shock paths and two smaller uncertainty sets. In the base example, a cash-only reserve needs 21 units. A sale with proceeds in period 2 reduces the reserve to 7.1795 units, but requires disposal of 17.9487 units from a 100-unit asset. Proceeds in period 4 arrive too late to reduce the cash-only reserve. Under the main income-rights assumption, a larger late sale makes the reserve need worse. This penalty disappears if income rights remain until settlement. The contribution is a reproducible application of established cash-management methods to a work-independent dividend. It is not a new theory of liquidity or proof of permanent fiscal solvency.

**Keywords:** AI governance; social dividend; public ownership; fiscal reserves; liquidity; sovereign wealth funds.

## 1. The payment question

Consider a future in which competitive wages cannot support most people. The premise is conditional. This paper does not predict complete labor displacement. It studies one financing problem that would remain even if AI output were high: a resident must receive an income payment when it is due.

A public claim on productive capital can support such payments. It does not automatically provide cash on the correct date. Tax collection can be delayed. Companies can suspend distributions. Private equity can have a high reported value but a long sale process. If taxes and public asset income depend on the same production system, both can fall at once. A payment plan must therefore specify amounts, dates, and access to funds.

The paper asks: for a stated social dividend, how much initial cash is enough across a defined set of revenue paths? It also asks whether a planned asset sale reduces that requirement. The answer depends on when the sale is paid and when the public fund loses the sold asset's income.

The objective is deliberately narrow. The model treats a fixed aggregate payment as a prior public choice. It does not choose an adequate individual income, tax rate, population rule, or ownership share. It tests whether the payment can be made in full. Housing supply, food access, inflation, and payment-system access remain separate conditions. Study S004 in this programme tests real consumption access in a static economy. This study tests payment timing over several periods.

The unit of analysis is a policy and a complete revenue path. The results concern that model. The number of paths passed is not a probability, and synthetic amounts are not recommended national reserve levels.

## 2. Closest work and limited contribution

Cash buffers are established public-finance tools. Hürcan, Koç, and Balıbek [S1] develop practical reserve methods based on stress duration, available financing, cumulative cash flows, and the cost of holding cash. Their Section 4 already distinguishes peak financing needs from average needs. Fainboim, Saxena, and Williams [S2] distinguish temporary cash surpluses from structural wealth and give safety and liquidity priority in treasury investment. Thus, neither matching cash to payments nor separating a reserve from a wealth fund is new here.

Rietveld's APFC Trustees' Paper 10 [S3] is an especially close comparison. It tests depletion of Alaska's Earnings Reserve Account through deterministic, historical-return, and simulated scenarios. Its concern is that available funds can run out while a large fund still exists. The APFC fund-structure page also describes a smoothed market-value draw and variable realized income [S4]. Those sources show that a payout rule and an asset valuation do not by themselves establish spendable resources. This paper does not evaluate Alaska's current legal structure. Its cash account is not a replica of the Earnings Reserve Account, which is an accounting and appropriation category within an invested portfolio.

AI public-finance work already considers public capital ownership. Korinek and Lockwood [S5] place public equity among the tools for sharing AI returns and discuss policy in economies with declining labor income. Dynan, Elmendorf, and Sheiner [S6] assess multiple fiscal scenarios. Their discussion of public ownership includes acquisition finance, private placements, diversification, management, and the risk of treating expected equity returns as certain budget revenue. These are central constraints on any dividend fund.

Prativadi's 2026 replication package [S7] provides an annual fund module with an accumulation phase and a payout based on a moving average of fund value. Its model specification and README were read. The main manuscript could not be retrieved directly from SSRN. The comparison therefore concerns the accessible package, not every claim in the full paper. That package makes a broad claim that an AI fund can support a universal dividend. This paper does not claim to originate that proposal.

The limited contribution is an exact, small design test that combines two revenue streams, permitted shock overlap, a delayed sale, and loss of income from the sold assets. It returns both the required cash and a path that makes the requirement binding. The searched sources do not establish priority for this combination. A close cash-management literature already contains its basic logic. The result should be read as an auditable extension and teaching model, with a specific counterexample to a simple asset-sale response.

The search used multiple public-web queries and followed the IMF cash-surplus note to its cash-buffer companion. It also followed APFC's source links and inspected an AI fund's public replication material. No subscription search or exhaustive citation review was completed. [The search log](logs/searches.md) records queries, access limits, and decisions.

## 3. Model and timing

There are `T` payment periods. Let `d>0` be the fixed aggregate social dividend due at the end of each period. The initial public balance sheet contains cash `R≥0` and a productive asset with reference value `A>0`. These are separate endowments. The model does not finance the acquisition of either endowment.

Before the first period, the fund commits to sell an amount `q`, with `0≤q≤A`. The sale is chosen before any shock is observed. Net proceeds are `(1−h)q`, where the sale discount, or haircut, satisfies `0≤h≤1`. The proceeds arrive in period `L`, before that period's payment. Thus, `L=1` means cash is available for the first payment; it does not mean funds arrive before time zero.

Under the main contract assumption, the fund loses the income rights on the sold fraction immediately. This can represent a transfer of economic rights before final payment or income held outside the treasury during a sale. It is not a claim that all asset sales work this way. Section 6 tests the alternative in which the fund retains income until settlement.

For a shock path `ω`, let `τₜ(ω)` be collected taxes and `vₜ(ω)` be cash income from the full original asset. After the sale, fund income is `(1−q/A)vₜ`. Taxes and asset income are distinct cash entries. Taxes are already net collections; `vₜ` is already net distributable income. A tax payment from a publicly owned company must not be counted twice. The model assumes the tax stream does not change with the asset sale.

Cash earns zero interest. No borrowing, further sales, new contributions, or discretionary payment cuts are permitted during the horizon. Surpluses remain in cash. The balance after the payment in period `t` is

$$B_t(\omega;q,R)=R+\sum_{u=1}^{t}\left[\tau_u(\omega)+(1-q/A)v_u(\omega)-d\right]+(1-h)q\,\mathbf 1_{t\ge L}. \tag{1}$$

Every payment succeeds if and only if `Bₜ≥0` at every date. Income and sale cash arrive before the period's payment. There is no within-period timing model. If receipts arrive after a payment deadline, the accounting period must be shortened or the receipt moved to the next period.

Let `Ω` be a finite set of permitted paths. It is an uncertainty set with no probability weights. The same precommitted `q` and `R` must work for every member of `Ω`. This prevents the analyst from selecting a different sale after seeing the future.

## 4. An exact reserve certificate

Define the cash gap without a sale as

$$a_{\omega t}=td-\sum_{u=1}^{t}[\tau_u(\omega)+v_u(\omega)],$$

and the change in that gap per unit sold as

$$b_{\omega t}=\frac{1}{A}\sum_{u=1}^{t}v_u(\omega)-(1-h)\mathbf 1_{t\ge L}. \tag{2}$$

### Proposition 1. Necessary and sufficient cash

For fixed `q`, the least reserve that protects all payments on all paths is

$$R^*(q)=\max\left\{0,\max_{\omega\in\Omega,\,1\le t\le T}(a_{\omega t}+b_{\omega t}q)\right\}. \tag{3}$$

**Proof.** Equation (1) gives `Bₜ=R−aωt−bωt q`. Thus, every balance is nonnegative exactly when `R` is at least each displayed cash gap and at least zero. The finite maximum is attained. If the maximum is positive, any smaller reserve fails on an attaining path and date. ∎

This is a budget identity expressed as a certificate, not a new theorem about finance. Its value is that the certificate can identify the binding date, not just the final balance. Terminal resources can cover total payments while an earlier payment fails.

### Proposition 2. Sale size and reserve need

The function `R*(q)` is convex and piecewise linear on `[0,A]`. A minimum can be found among the interval endpoints and intersections of its affine constraints. If several sale amounts minimize the reserve, choose the smallest one.

**Proof.** Equation (3) is the maximum of finitely many affine functions, including zero. Such a maximum is convex and piecewise linear. An interior minimum is at a change in the active constraint or on a flat segment. The ends of a flat segment are intersections or interval endpoints. Evaluating these candidates therefore attains a minimum. ∎

Convexity does not imply that more sales always help. Before receipt, `bωt=Σv/A≥0`: a sale can only remove income at those dates. After receipt, the coefficient can be negative because sale cash reduces the gap. The minimum can occur where an early increasing constraint meets a later decreasing constraint.

### Corollary. A sale can arrive too late

Suppose a path reaches the no-sale reserve `R*(0)>0` at a date `t<L`. If its cumulative asset income through `t` is positive, then every `q>0` requires strictly more reserve than `R*(0)` under the main contract assumption.

**Proof.** The corresponding constraint gives `R*(q)≥R*(0)+qΣv/A>R*(0)`. ∎

This is a sufficient condition, not a general objection to asset sales. A timely sale can reduce the required cash substantially. When rights remain until settlement, the early coefficient is zero. Then late sales need not make the early cash gap worse, although they still cannot repair it.

## 5. Experiment design

All numbers are synthetic. The horizon has eight periods. Each period requires 10 units. The initial asset has reference value 100. Full-asset income is 5 in a normal period and 1 in a shock period. Tax receipts are 7 normally and 2 under a tax shock. Thus, normal revenue is 12 and a simultaneous shock reduces it to 3. At most three tax shocks and at most three fund-income shocks occur within the horizon.

There are 93 binary streams with at most three shocks: `1+8+28+56`. Three sets are tested:

| Set | Rule | Number of complete paths |
| --- | --- | ---: |
| Joint shocks allowed | Every pair of the 93 tax and 93 fund streams | 8,649 |
| No overlap | Exclude a shock to both streams in the same period | 3,237 |
| Common shocks only | Tax and fund shock streams are identical | 93 |

These sets represent explicit assumptions about possible co-movement. They are not measured correlation coefficients. The first set includes the other two. Allowing all combinations does not assert statistical independence.

The base sale is paid in period 2 with a 20 percent haircut. Sensitivity analysis tests receipt periods 1 through 5 and haircuts of 0, 20, and 50 percent. Across three sets, this gives 45 policy environments. Each environment uses the complete path set and exact rational arithmetic. The published sale grid is a display check; the optimizer searches all constraint intersections, not only those eight grid points.

Every base-case path is retained, giving 11,979 rows across the three sets. Sets overlap, so these rows are not 11,979 distinct economic histories. There is no sampling error because all specified paths are included. Model error and the choice of uncertainty set remain substantial.

## 6. Results and counterexamples

### 6.1 Cash-only protection and order

With no sale, the joint set needs 21 units of cash. Three simultaneous shocks at the start each create a seven-unit gap. Later normal surpluses cannot pay an earlier bill. If the same three shocks occur in the last three periods, the reserve need is only 11. Five normal periods first accumulate 10 units, which offset part of the later gap. Both paths have the same total revenue and final no-reserve balance.

The no-overlap set needs 15 units: three tax-only deficits of 3 and three fund-only deficits of 2 can occur before normal periods. The common-shock set needs 21. Merely having two revenue instruments therefore provides no guarantee of independent protection. The set of states that joins them matters.

### 6.2 Timely sale and an interior choice

The base optimized results are:

| Uncertainty set | No-sale reserve | Planned sale | Minimum reserve |
| --- | ---: | ---: | ---: |
| Joint shocks allowed | 21.0000 | 17.9487 | 7.1795 |
| No overlap | 15.0000 | 17.9104 | 3.8955 |
| Common shocks only | 21.0000 | 17.9487 | 7.1795 |

For the joint set, the binding first-period constraint is `7+0.01q`. The third-period constraint is `21−0.77q`. They meet at `q=700/39` and `R=280/39`. The complete enumeration checks that no other path or date requires more at this choice. Cash of approximately 7.1795 protects all 8,649 paths under the assumptions.

The no-overlap set gives `q=1200/67` and `R=261/67`. Its first-period tax-only gap is `3+0.05q`. The later six-period gap is `15−0.62q`. A certificate based on this smaller set fails when simultaneous shocks are allowed. This is a negative result about a design assumption, not an estimate of how often governments face joint shocks.

### 6.3 Receipt delay dominates some sale discounts

| Receipt period | Haircut | Best planned sale | Minimum reserve |
| --- | ---: | ---: | ---: |
| 1 | 20% | 27.2727 | 0.0000 |
| 2 | 20% | 17.9487 | 7.1795 |
| 3 | 20% | 8.8608 | 14.1772 |
| 4 | 20% | 0.0000 | 21.0000 |
| 5 | 20% | 0.0000 | 21.0000 |

These rows use the joint set. A period-1 receipt can supply the whole cash bridge, so the separately supplied initial reserve is zero. This does not mean the policy is free: it disposes of over 27 percent of the initial asset.

At period 4, the first three shocks occur before receipt. Their gap is `21+0.03q`. A sale of 25 requires 21.75 units of cash; selling the entire asset requires 24. Across all three tested haircuts, the reserve-minimizing sale is zero. A better sale price cannot repair a payment deadline that precedes the receipt.

For a period-2 receipt, a larger haircut increases the sale required. At haircuts of 0, 20, and 50 percent, the best sale is 14.2857, 17.9487, and 29.1667. The corresponding reserve is 7.1429, 7.1795, and 7.2917. In this parameter range, the first-period bridge is the limiting condition; changing the receipt date has a larger effect on required initial cash than these haircut changes. That ranking is specific to this design.

### 6.4 Income rights and the cost of disposal

If income rights continue until the receipt period, the joint-set reserve falls to exactly 7 for a period-2 sale. With receipt in period 4, the minimum remains 21. Selling all assets then requires 21 rather than 24. Thus, the claim that a late sale makes the bridge worse depends on early loss of income. The claim that late cash cannot pay an earlier obligation survives the alternative contract.

Minimizing initial cash alone ignores the public value of retained assets. A further sensitivity test minimizes `R*(q)+λq`, where `λ` is a stated cost weight on disposal. It is a design preference, not an estimated welfare measure. With `λ=0.2`, the joint-set base choice remains `700/39`. With `λ=1`, no sale is preferred and the reserve is 21. The study cannot select the correct weight or decide whether preserving public control is worth more than a cash saving.

No result establishes permanent solvency. A reserve can be spent only once. If revenue remains below the payment indefinitely and asset proceeds are finite, cumulative deficits eventually exceed all available cash. Restarting the eight-period calculation with a new full reserve would manufacture resources. A long-term policy must finance replenishment, tax capacity, and the retained asset's future income.

## 7. Governance use

The first proposed strategy is to publish a payment calendar with a financing certificate. The certificate should state the protected amount, the horizon, the uncertainty set, the liquid reserve, and the earliest stressed payment date. An aggregate asset-to-payment ratio omits critical timing information. A responsible report should also name the conditions that invalidate coverage.

The second strategy is to separate income adequacy from the optional dividend. A basic entitlement can have a fixed payment schedule. An additional distribution can depend on excess resources after the basic schedule is financed. This paper tests only the fixed component. It does not endorse cuts to an adequate floor when a fund performs poorly. If the test fails, the government must change financing, reserve capital, or the promise through an accountable public process.

Third, use collected revenue and contractually available cash in the liquidity test. Do not treat market appreciation as a deposit. Record tax and dividend exposure to the same underlying firms and markets. Diversification is useful only to the extent that the relevant resources remain available in the permitted stress paths. Evidence that shocks rarely overlap can justify a probabilistic extension; it does not justify silently excluding joint failure.

Fourth, specify asset-sale authority before a crisis. Record which assets can be sold, the legal approval period, settlement time, income rights during settlement, and net proceeds. Count only sales that can occur within the relevant window. In the model, every sale succeeds at its stated price and date. A real treasury should add failed settlement, market closure, and loss of sale authority to its stress set where those events are credible.

Fifth, reconcile the fund with the whole public budget. A ring-fenced reserve can support payment discipline, but it may compete with health, infrastructure, debt service, and emergency spending. Those claims must be included or explicitly financed elsewhere. A fund cannot protect its dividend by assuming every other public duty disappears. Independent custody, clear authorization, public accounts, and an appeal path for missed payments are institutional proposals. Their effectiveness is not tested here.

## 8. Limits and next tests

The model assumes fixed nominal payments, a stable population, zero cash return, no debt access, and no endogenous price response. Real purchasing power can fall even when every nominal payment succeeds. Different groups can face different needs and payment barriers. The model has no evidence about those outcomes.

The tax and fund streams are exogenous. Selling public assets can change taxation, investment, voting power, and fiscal credibility. Those effects are excluded. The reference asset value is fixed, the haircut is known, and transaction size does not move the market. A large emergency sale could violate all three assumptions.

The shock cap is not an empirical estimate. A fourth shock to either stream lies outside the base certificate. The horizon is not chosen from a measured recovery process. The initial reserve and public asset are given without an acquisition cost. Thus, lower cash requirements do not establish a cheaper policy after acquisition finance, interest, or future payouts are included.

A practical extension should use actual receipt dates, household payment deadlines, settlement terms, and legal access to funds. It should validate adverse co-movement and report a range of stress sets. A second extension can permit contingent sales, borrowing, or central-bank support with explicit limits. It must enforce decisions based only on information available at the time. A third can require a terminal asset and reserve floor. Those changes can reverse the preferred sale amount.

## 9. Reproduction and disclosure

Run from the repository root:

```sh
python3 studies/2026-10-11-dividend-reserves/code/model.py
python3 -m unittest discover -s studies/2026-10-11-dividend-reserves/code -p 'test_*.py' -v
```

The analysis needs only Python's standard library and no network. [design.json](data/design.json) contains all inputs. [summary.csv](results/summary.csv), [path_cases.csv](results/path_cases.csv), and [timing.csv](results/timing.csv) retain the results. [run.json](results/run.json) records the runtime and hashes. Ten tests check path counts, cash timing, sale limits, the analytic optimum, independent period accounting, late-sale failure, income-rights sensitivity, and a smaller exhaustive grid.

The study is exploratory. Its decisions were recorded during development rather than preregistered. Public evidence consists of short attributed extracts, exact retrieval metadata, and a source acquisition recipe. Full source bytes remain outside the public study. No human participant data were used. AI performed the analysis and writing. Funding and human conflicts were not supplied. Separate internal AI review is complete. See [critical review](reviews/critical-review.md), [author response](reviews/author-response.md), and [completion gates](completion-gates.md). The study remains an AI-assisted draft.

## References

- **[S1]** Yasemin Hürcan, Fatoş Koç, and Emre Balıbek. 2020. *How to Set Up a Cash Buffer: A Practical Guide to Developing and Implementing a Cash Buffer Policy*. IMF How-to Note 20/04, December. [Official PDF](https://www.imf.org/-/media/files/publications/howtonotes/2020/english/htnea2020004.pdf), Section 4, printed pages 10–14.
- **[S2]** Israel Fainboim, Sandeep Saxena, and Mike Williams. 2020. *How to Develop a Framework for the Investment of Temporary Government Cash Surpluses*. IMF How-to Note 20/03, December. [Official PDF](https://www.imf.org/-/media/files/publications/howtonotes/2020/english/htnea2020003.pdf), Sections 2–3.
- **[S3]** Malan Rietveld. 2024. *A Rules-Based Permanent-Endowment Model for Alaska*. APFC Trustees' Paper 10, with Callan addendum. [Official PDF](https://apfc.org/wp-content/uploads/2025/12/2024-APFC-Trustees-Paper-10.pdf), Sections 2 and 6. The hosting path says 2025; the issuing page identifies the paper as published in 2024.
- **[S4]** Alaska Permanent Fund Corporation. Undated. *Fund Structure*. [Official page](https://apfc.org/the-fund/fund-structure/), headings “POMV Calculation” and “Earning Reserve Account.” Retrieved 11 October 2026. This is an issuer description, not an independent legal-status review.
- **[S5]** Anton Korinek and Lee M. Lockwood. 2026. *Public Finance in the Age of AI: A Primer*. January Brookings version. [Inspected PDF](https://www.brookings.edu/wp-content/uploads/2026/01/Korinek-Lockwood-FINAL-for-website.pdf), Section 4.
- **[S6]** Karen Dynan, Douglas Elmendorf, and Louise Sheiner. 2026. *How Might Fiscal Policy Respond to the Rise of Artificial Intelligence?* NBER Working Paper 35437, July. [Publisher PDF](https://www.nber.org/system/files/working_papers/w35437/w35437.pdf), pages 34–36. © 2026 by the authors.
- **[S7]** Arvin Prativadi. 2026. *Replication package for “The AI Sovereign Wealth Fund: A Legal and Economic Framework for Public Capital in an Age of Labor Displacement.”* 21 August. [Zenodo record](https://doi.org/10.5281/zenodo.22036502). Inspected README and model specification, especially Section 3. The main SSRN manuscript was not retrieved.
