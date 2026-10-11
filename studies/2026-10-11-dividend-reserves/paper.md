# Cash Before Capital
## Financing Social Dividends When Public Assets Cannot Be Sold in Time

> **State:** Complete-study draft. **Study:** S005. **Date:** 11 October 2026.
> **Evidence cutoff:** 2026-10-11T21:03:17Z, the end of source collection for this draft. The literature review is selective.

## Abstract

A government can own valuable AI assets and still be unable to pay a social dividend on time. The difficulty is one of liquidity: wealth is not always available as cash when residents need it. This paper studies the initial reserve required to protect a fixed payment when tax receipts and public asset income can fall together. It allows a planned asset sale, a delay before the proceeds arrive, and a loss of income from the assets sold. The minimum reserve is the largest cumulative cash shortfall across all permitted paths and payment dates. In an eight-period example with 8,649 possible joint-shock paths, a cash-only policy requires 21 units. A sale paid in period 2 reduces that reserve to 7.1795, while disposing of 17.9487 units of a 100-unit asset. A sale paid in period 4 arrives too late to help. If income rights transfer before settlement, a larger late sale increases the cash required; this additional penalty disappears when the fund retains income until settlement. The analysis applies established cash-management methods to a work-independent dividend. It shows why the financing plan must specify when resources become available, as well as how much the public owns.

**Keywords:** AI governance; social dividend; public ownership; fiscal reserves; liquidity; sovereign wealth funds.

## 1. Introduction

Public ownership is one way to share the returns from an economy that relies increasingly on AI rather than human labor. A fund can hold productive assets on behalf of residents and use their income to support a regular payment. But ownership and payment capacity are different. Tax receipts may arrive late, companies may suspend distributions, and a valuable asset may take time to sell. A resident's bill can fall due before the public fund receives its cash.

Consider a fund that must pay ten units per period. Normal tax and asset income total twelve, which appears to leave a comfortable surplus. If both revenue streams fall, however, income drops to three. Three such periods at the start create a cash need of twenty-one. An asset sale can reduce this need if its proceeds arrive early enough. If they arrive after the third payment, the fund still needs the full reserve. Under a contract that transfers income rights before settlement, the sale makes the early gap larger by removing income before supplying cash.

This paper asks how much initial cash protects a fixed social dividend across a stated set of revenue paths, and whether a planned sale reduces that amount. The model makes the timing of both receipts and obligations explicit. Its principal result is an exact reserve condition, together with the path and date at which the condition binds. The numerical cases then separate the effects of joint revenue losses, settlement delay, sale price, and income rights.

The post-labor setting is conditional. The paper does not predict complete labor displacement. It takes as given a future in which competitive wages cannot support most people, and in which a regular transfer has become particularly important. The fixed aggregate payment is a prior public choice. The analysis does not determine an adequate individual income, a population rule, a tax rate, or an ownership share.

The distinction from the companion consumption study, S004, is temporal. S004 asks whether public revenue secures access to goods in a static economy. This paper asks whether the promised money is available on every payment date. It therefore does not resolve housing supply, inflation, distribution within the population, or access to the payment system. Its numerical amounts are synthetic, and the share of stress paths passed is not an estimated probability of success.

## 2. Related literature

Cash buffers are established public-finance tools. Hürcan, Koç, and Balıbek [S1] develop practical reserve methods based on stress duration, available financing, cumulative cash flows, and the cost of holding cash. Their Section 4 already distinguishes peak financing needs from average needs. Fainboim, Saxena, and Williams [S2] distinguish temporary cash surpluses from structural wealth and give safety and liquidity priority in treasury investment. Thus, neither matching cash to payments nor separating a reserve from a wealth fund is new here.

Rietveld's APFC Trustees' Paper 10 [S3] is an especially close comparison. It tests depletion of Alaska's Earnings Reserve Account through deterministic, historical-return, and simulated scenarios. Its concern is that available funds can run out while a large fund still exists. The APFC fund-structure page also describes a smoothed market-value draw and variable realized income [S4]. Those sources show that a payout rule and an asset valuation do not by themselves establish spendable resources. This paper does not evaluate Alaska's current legal structure. Its cash account is not a replica of the Earnings Reserve Account, which is an accounting and appropriation category within an invested portfolio.

AI public-finance work already considers public capital ownership. Korinek and Lockwood [S5] place public equity among the tools for sharing AI returns and discuss policy in economies with declining labor income. Dynan, Elmendorf, and Sheiner [S6] assess multiple fiscal scenarios. Their discussion of public ownership includes acquisition finance, private placements, diversification, management, and the risk of treating expected equity returns as certain budget revenue. These are central constraints on any dividend fund.

Prativadi's 2026 replication package [S7] provides an annual fund module with an accumulation phase and a payout based on a moving average of fund value. Its model specification and README were read. The main manuscript could not be retrieved directly from SSRN. The comparison therefore concerns the accessible package, not every claim in the full paper. That package makes a broad claim that an AI fund can support a universal dividend. This paper does not claim to originate that proposal.

This paper contributes a compact test that combines two revenue streams, permitted shock overlap, a delayed sale, and loss of income from the sold assets. It returns both the required cash and a path that makes the requirement binding. The searched sources do not establish priority for this combination. A close cash-management literature already contains its basic logic. Its main use is to show, in a fully specified example, when an asset sale can reduce cash needs and when it can make them worse.

The search used multiple public-web queries and followed the IMF cash-surplus note to its cash-buffer companion. It also followed APFC's source links and inspected an AI fund's public replication material. No subscription search or exhaustive citation review was completed. [The search log](logs/searches.md) records queries, access limits, and decisions.

## 3. Revenue, asset sales, and payment timing

There are $T$ payment periods. Let $d>0$ be the fixed aggregate social dividend due at the end of each period. The initial public balance sheet contains cash $R\ge 0$ and a productive asset with reference value $A>0$. These are separate endowments. The model does not finance the acquisition of either endowment.

Before the first period, the fund commits to sell an amount $q$, with $0\le q\le A$. The sale is chosen before any shock is observed. Net proceeds are $(1-h)q$, where the sale discount, or haircut, satisfies $0\le h\le 1$. The proceeds arrive in period $L$, before that period's payment. Thus, $L=1$ means cash is available for the first payment; it does not mean funds arrive before time zero.

Under the main contract assumption, the fund loses the income rights on the sold fraction immediately. This can represent a transfer of economic rights before final payment or income held outside the treasury during a sale. It is not a claim that all asset sales work this way. Section 5 tests the alternative in which the fund retains income until settlement.

For a shock path $\omega$, let $\tau_t(\omega)$ be collected taxes and $v_t(\omega)$ be cash income from the full original asset. After the sale, fund income is $(1-q/A)v_t$. Taxes and asset income are distinct cash entries. Taxes are already net collections; $v_t$ is already net distributable income. A tax payment from a publicly owned company must not be counted twice. The model assumes the tax stream does not change with the asset sale.

Cash earns zero interest. No borrowing, further sales, new contributions, or discretionary payment cuts are permitted during the horizon. Surpluses remain in cash. The balance after the payment in period $t$ is

$$B_t(\omega;q,R)=R+\sum_{u=1}^{t}\left[\tau_u(\omega)+(1-q/A)v_u(\omega)-d\right]+(1-h)q\,\mathbf 1_{t\ge L}. \tag{1}$$

Every payment succeeds if and only if $B_t\ge0$ at every date. Income and sale cash arrive before the period's payment. There is no within-period timing model. If receipts arrive after a payment deadline, the accounting period must be shortened or the receipt moved to the next period.

Let $\Omega$ be a finite set of permitted paths. It is an uncertainty set with no probability weights. The same precommitted $q$ and $R$ must work for every member of $\Omega$. This prevents the analyst from selecting a different sale after seeing the future.

## 4. How much cash is enough?

The reserve must cover the largest cumulative shortfall, wherever it occurs. For each path and date, let $a$ denote that shortfall without a sale and let $b$ denote the change per unit of assets sold. Both quantities follow directly from the cash account; Appendix A gives their definitions. The minimum reserve for a chosen sale is then:

$$R^*(q)=\max\left\{0,\max_{\omega\in\Omega,\,1\le t\le T}(a_{\omega t}+b_{\omega t}q)\right\}. \tag{3}$$

Appendix A derives the formula. Each term is the cumulative gap at one date on one path, so the largest gap determines the cash needed at the start.

The calculation identifies the binding payment date as well as the amount. This distinction matters because sufficient total resources at the end of the horizon cannot prevent an earlier missed payment.

The reserve requirement is a convex, piecewise-linear function of the sale amount. In economic terms, it is the upper envelope of several cash constraints. An early constraint can rise with the sale because the fund loses income before it receives proceeds. A later constraint can fall because the sale cash has arrived. The smallest required reserve can occur where these two constraints meet. The exact calculation compares the interval endpoints with the intersections of those constraints; when several sales attain the same minimum, it chooses the smallest sale.

This logic also identifies when a sale cannot help. Suppose the worst cash gap without a sale occurs before settlement. If the assets being sold would have paid positive income before that date, every positive sale increases that gap under the main contract assumption. The reserve needed therefore exceeds its no-sale level. Appendix A states and proves this sufficient condition. When income rights remain with the fund until settlement, the early gap no longer rises, but cash that arrives late still cannot repair it.

## 5. Numerical results

All numbers are synthetic. The horizon has eight periods. Each period requires 10 units. The initial asset has reference value 100. Full-asset income is 5 in a normal period and 1 in a shock period. Tax receipts are 7 normally and 2 under a tax shock. Thus, normal revenue is 12 and a simultaneous shock reduces it to 3. At most three tax shocks and at most three fund-income shocks occur within the horizon.

There are 93 binary streams with at most three shocks: $1+8+28+56$. Three sets are tested:

| Set | Rule | Number of complete paths |
| --- | --- | ---: |
| Joint shocks allowed | Every pair of the 93 tax and 93 fund streams | 8,649 |
| No overlap | Exclude a shock to both streams in the same period | 3,237 |
| Common shocks only | Tax and fund shock streams are identical | 93 |

These sets represent explicit assumptions about possible co-movement. They are not measured correlation coefficients. The first set includes the other two. Allowing all combinations does not assert statistical independence.

The base sale is paid in period 2 with a 20 percent haircut. Sensitivity analysis tests receipt periods 1 through 5 and haircuts of 0, 20, and 50 percent. Across three sets, this gives 45 policy environments. Each environment uses the complete path set and exact rational arithmetic. The published sale grid is a display check; the optimizer searches all constraint intersections, not only those eight grid points.

Every base-case path is retained, giving 11,979 rows across the three sets. Sets overlap, so these rows are not 11,979 distinct economic histories. There is no sampling error because all specified paths are included. Model error and the choice of uncertainty set remain substantial.

### 5.1 The order of revenue losses

With no sale, the joint set needs 21 units of cash. Three simultaneous shocks at the start each create a seven-unit gap. Later normal surpluses cannot pay an earlier bill. If the same three shocks occur in the last three periods, the reserve need is only 11. Five normal periods first accumulate 10 units, which offset part of the later gap. Both paths have the same total revenue and final no-reserve balance.

The no-overlap set needs 15 units: three tax-only deficits of 3 and three fund-only deficits of 2 can occur before normal periods. The common-shock set needs 21. Merely having two revenue instruments therefore provides no guarantee of independent protection. The set of states that joins them matters.

### 5.2 A sale that arrives in time

The base optimized results are:

| Uncertainty set | No-sale reserve | Planned sale | Minimum reserve |
| --- | ---: | ---: | ---: |
| Joint shocks allowed | 21.0000 | 17.9487 | 7.1795 |
| No overlap | 15.0000 | 17.9104 | 3.8955 |
| Common shocks only | 21.0000 | 17.9487 | 7.1795 |

For the joint set, the binding first-period constraint is $7+0.01q$. The third-period constraint is $21-0.77q$. They meet at $q=700/39$ and $R=280/39$. The complete enumeration checks that no other path or date requires more at this choice. Cash of approximately 7.1795 protects all 8,649 paths under the assumptions.

The no-overlap set gives $q=1200/67$ and $R=261/67$. Its first-period tax-only gap is $3+0.05q$. The later six-period gap is $15-0.62q$. A certificate based on this smaller set fails when simultaneous shocks are allowed. This is a negative result about a design assumption, not an estimate of how often governments face joint shocks.

### 5.3 The cost of late sale proceeds

| Receipt period | Haircut | Best planned sale | Minimum reserve |
| --- | ---: | ---: | ---: |
| 1 | 20% | 27.2727 | 0.0000 |
| 2 | 20% | 17.9487 | 7.1795 |
| 3 | 20% | 8.8608 | 14.1772 |
| 4 | 20% | 0.0000 | 21.0000 |
| 5 | 20% | 0.0000 | 21.0000 |

These rows use the joint set. A period-1 receipt can supply the whole cash bridge, so the separately supplied initial reserve is zero. This does not mean the policy is free: it disposes of over 27 percent of the initial asset.

At period 4, the first three shocks occur before receipt. Their gap is $21+0.03q$. A sale of 25 requires 21.75 units of cash; selling the entire asset requires 24. Across all three tested haircuts, the reserve-minimizing sale is zero. A better sale price cannot repair a payment deadline that precedes the receipt.

For a period-2 receipt, a larger haircut increases the sale required. At haircuts of 0, 20, and 50 percent, the best sale is 14.2857, 17.9487, and 29.1667. The corresponding reserve is 7.1429, 7.1795, and 7.2917. In this parameter range, the first-period bridge is the limiting condition; changing the receipt date has a larger effect on required initial cash than these haircut changes. That ranking is specific to this design.

### 5.4 Contract terms and the value of retained assets

If income rights continue until the receipt period, the joint-set reserve falls to exactly 7 for a period-2 sale. With receipt in period 4, the minimum remains 21. Selling all assets then requires 21 rather than 24. Thus, the claim that a late sale makes the bridge worse depends on early loss of income. The claim that late cash cannot pay an earlier obligation survives the alternative contract.

Minimizing initial cash alone ignores the public value of retained assets. A further sensitivity test minimizes $R^*(q)+\lambda q$, where $\lambda$ is a stated cost weight on disposal. It is a design preference, not an estimated welfare measure. With $\lambda =0.2$, the joint-set base choice remains $700/39$. With $\lambda =1$, no sale is preferred and the reserve is 21. The study cannot select the correct weight or decide whether preserving public control is worth more than a cash saving.

No result establishes permanent solvency. A reserve can be spent only once. If revenue remains below the payment indefinitely and asset proceeds are finite, cumulative deficits eventually exceed all available cash. Restarting the eight-period calculation with a new full reserve would manufacture resources. A long-term policy must finance replenishment, tax capacity, and the retained asset's future income.

## 6. Implications for a social dividend

The central implication is that a social dividend needs a payment plan in addition to an ownership plan. Reporting the value of a public fund relative to annual benefits omits the dates on which funds become usable. A financing statement would instead identify the promised amount, the protected horizon, the initial cash, the permitted adverse paths, and the first payment that fails outside those conditions. The model supplies the accounting for such a statement, not evidence that a particular government can meet it.

A fixed basic payment can also be distinguished from an additional dividend paid only when resources permit. This paper examines the fixed component. A failed cash test does not establish that an adequate floor should be cut. It establishes that the existing financing, reserve, and promise are inconsistent under the specified stress. Resolving that inconsistency requires an accountable public choice about resources and obligations.

The relevant resources are collected revenue and contractually available cash. Market appreciation is not a deposit, and taxes and dividends linked to the same firms can weaken together. Diversification helps only to the extent that the required cash survives the relevant states. Evidence that joint losses are rare could support a probabilistic extension, but it would not make those losses impossible. A policy that excludes them should state that limit openly.

Asset-sale arrangements deserve particular attention because the contract determines the cash effect. Legal approval, sale authority, settlement time, income rights, and net proceeds all affect whether a sale can protect the next payment. The model assumes the stated sale always succeeds at its stated price. A practical application would include credible risks of failed settlement, market closure, or loss of sale authority. More favorable valuation alone does not address a missed settlement window.

These proposals also need to fit the wider public budget. Reserves set aside for the dividend may compete with health, infrastructure, debt service, and emergency spending. Those obligations cannot be made to disappear by placing them outside the fund's accounts. Independent custody, clear authorization, public reporting, and an appeal path for missed payments are possible institutional supports. Their effectiveness is not established by the cash model.

## 7. Limitations and further research

The model assumes fixed nominal payments, a stable population, zero cash return, no debt access, and no endogenous price response. Real purchasing power can fall even when every nominal payment succeeds. Different groups can face different needs and payment barriers. The model has no evidence about those outcomes.

The tax and fund streams are exogenous. Selling public assets can change taxation, investment, voting power, and fiscal credibility. Those effects are excluded. The reference asset value is fixed, the haircut is known, and transaction size does not move the market. A large emergency sale could violate all three assumptions.

The shock cap is not an empirical estimate. A fourth shock to either stream lies outside the base certificate. The horizon is not chosen from a measured recovery process. The initial reserve and public asset are given without an acquisition cost. Thus, lower cash requirements do not establish a cheaper policy after acquisition finance, interest, or future payouts are included.

A practical extension should use actual receipt dates, household payment deadlines, settlement terms, and legal access to funds. It should validate adverse co-movement and report a range of stress sets. A second extension can permit contingent sales, borrowing, or central-bank support with explicit limits. It must enforce decisions based only on information available at the time. A third can require a terminal asset and reserve floor. Those changes can reverse the preferred sale amount.

## 8. Conclusion

A public fund's ability to support residents depends on the dates at which its wealth becomes spendable. The numerical cases show that a timely asset sale can reduce the initial cash reserve, while a late sale can leave the reserve unchanged or increase it. The difference comes from settlement and income rights, not merely from asset value. A credible social dividend therefore needs a dated account of adverse revenues, available cash, and payment obligations. A finite reserve can bridge a temporary gap; it cannot finance a permanent deficit without replenishment.

## Appendix A. Reserve formulas and proofs

### A.1 Cash gaps

Define the cash gap without a sale as

$$a_{\omega t}=td-\sum_{u=1}^{t}[\tau_u(\omega)+v_u(\omega)],$$

and the change in that gap per unit sold as

$$b_{\omega t}=\frac{1}{A}\sum_{u=1}^{t}v_u(\omega)-(1-h)\mathbf 1_{t\ge L}. \tag{2}$$

### A.2 The minimum reserve

**Proof.** Equation (1) gives $B_t=R-a_{\omega t}-b_{\omega t}q$. Thus, every balance is nonnegative exactly when $R$ is at least each displayed cash gap and at least zero. The finite maximum is attained. If the maximum is positive, any smaller reserve fails on an attaining path and date. ∎

### A.3 The sale choice

The function $R^*(q)$ is convex and piecewise linear on $[0,A]$. A minimum can be found among the interval endpoints and intersections of its affine constraints. If several sale amounts minimize the reserve, the implementation chooses the smallest.

**Proof.** Equation (3) is the maximum of finitely many affine functions, including zero. Such a maximum is convex and piecewise linear. An interior minimum is at a change in the active constraint or on a flat segment. The ends of a flat segment are intersections or interval endpoints. Evaluating these candidates therefore attains a minimum. ∎

### A.4 A sale that arrives too late

Suppose a path reaches the no-sale reserve $R^*(0)>0$ at a date $t<L$. If cumulative asset income through that date is positive, every $q>0$ requires strictly more reserve than $R^*(0)$ under immediate transfer of income rights.

**Proof.** The corresponding constraint gives $R^*(q)\ge R^*(0)+q\sum v/A>R^*(0)$. ∎

## Appendix B. Reproduction and research record

Run from the repository root:

```sh
python3 studies/2026-10-11-dividend-reserves/code/model.py
python3 -m unittest discover -s studies/2026-10-11-dividend-reserves/code -p 'test_*.py' -v
```

The analysis needs only Python's standard library and no network. [design.json](data/design.json) contains all inputs. [summary.csv](results/summary.csv), [path_cases.csv](results/path_cases.csv), and [timing.csv](results/timing.csv) retain the results. [run.json](results/run.json) records the runtime and hashes. Ten tests check path counts, cash timing, sale limits, the analytic optimum, independent period accounting, late-sale failure, income-rights sensitivity, and a smaller exhaustive grid.

The study is exploratory. Its decisions were recorded during development rather than preregistered. Public evidence consists of short attributed extracts, exact retrieval metadata, and a source acquisition recipe. Full source bytes remain outside the public study.

## Research disclosure

Codex conducted the research, analysis, code, and writing. Separate internal AI review is recorded in the [critical review](reviews/critical-review.md) and [author response](reviews/author-response.md); the [completion gates](completion-gates.md) record the release checks. No human participant data or human peer review were involved. No affiliation or endorsement is claimed, and funding and human conflicts were not supplied. No repository reuse licence has been selected; third-party source rights remain separate. The [editorial revision record](reviews/editorial-revision.md) records the subsequent changes in presentation.

## References

- **[S1]** Yasemin Hürcan, Fatoş Koç, and Emre Balıbek. 2020. *How to Set Up a Cash Buffer: A Practical Guide to Developing and Implementing a Cash Buffer Policy*. IMF How-to Note 20/04, December. [Official PDF](https://www.imf.org/-/media/files/publications/howtonotes/2020/english/htnea2020004.pdf), Section 4, printed pages 10–14.
- **[S2]** Israel Fainboim, Sandeep Saxena, and Mike Williams. 2020. *How to Develop a Framework for the Investment of Temporary Government Cash Surpluses*. IMF How-to Note 20/03, December. [Official PDF](https://www.imf.org/-/media/files/publications/howtonotes/2020/english/htnea2020003.pdf), Sections 2–3.
- **[S3]** Malan Rietveld. 2024. *A Rules-Based Permanent-Endowment Model for Alaska*. APFC Trustees' Paper 10, with Callan addendum. [Official PDF](https://apfc.org/wp-content/uploads/2025/12/2024-APFC-Trustees-Paper-10.pdf), Sections 2 and 6. The hosting path says 2025; the issuing page identifies the paper as published in 2024.
- **[S4]** Alaska Permanent Fund Corporation. Undated. *Fund Structure*. [Official page](https://apfc.org/the-fund/fund-structure/), headings “POMV Calculation” and “Earning Reserve Account.” Retrieved 11 October 2026. This is an issuer description, not an independent legal-status review.
- **[S5]** Anton Korinek and Lee M. Lockwood. 2026. *Public Finance in the Age of AI: A Primer*. January Brookings version. [Inspected PDF](https://www.brookings.edu/wp-content/uploads/2026/01/Korinek-Lockwood-FINAL-for-website.pdf), Section 4.
- **[S6]** Karen Dynan, Douglas Elmendorf, and Louise Sheiner. 2026. *How Might Fiscal Policy Respond to the Rise of Artificial Intelligence?* NBER Working Paper 35437, July. [Publisher PDF](https://www.nber.org/system/files/working_papers/w35437/w35437.pdf), pages 34–36. © 2026 by the authors.
- **[S7]** Arvin Prativadi. 2026. *Replication package for “The AI Sovereign Wealth Fund: A Legal and Economic Framework for Public Capital in an Age of Labor Displacement.”* 21 August. [Zenodo record](https://doi.org/10.5281/zenodo.22036502). Inspected README and model specification, especially Section 3. The main SSRN manuscript was not retrieved.
