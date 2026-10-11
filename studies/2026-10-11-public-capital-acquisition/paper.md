# Buying a Public Stake Without Buying a Guarantee
## Acquisition Finance for a Social Dividend After Human Labor

> **State:** Complete-study draft — separate internal AI review and local release checks are complete.
> **Study ID:** S008 (`2026-10-11-public-capital-acquisition`). **Date:** 11 October 2026.
> **Evidence cutoff:** 2026-10-11T21:14:06Z, meaning source collection and selected close reading completed by that time.
> **Method:** Two-date finite-state analysis and deterministic synthetic cases. No country forecast or investment advice.
> **AI assistance:** Codex wrote and executed the study. No human review, affiliation, or endorsement is claimed. Funding and human conflicts were not supplied.
> **Rights:** No repository reuse licence has been selected. Source rights are separate.

## Abstract

Public ownership of AI capital can distribute future income, but a government must first obtain that ownership. This paper asks what a fairly priced, debt-financed purchase can fund when wages no longer support households. A two-date model separates the purchase payment, debt repayment, outside fiscal resources, and a minimum social dividend. Positive state prices give an accounting identity: a fair purchase changes the distribution of public resources across states but creates no additional state-price value. An exact certificate gives the initial fiscal contribution needed to meet a floor in every modeled state. A positive expected equity premium is insufficient. In one example, a fully debt-financed asset has expected net proceeds of 50 but loses 40 in the adverse state. A floor of 15 then requires 55 of initial fiscal capital if the whole asset must be held. A positive counterexample also matters: an asset that pays when existing tax receipts are low can raise the worst-state floor from zero to 15 without new initial capital. The tax claim already supplies the value. Common losses remove this benefit. The contribution is a small, reproducible acquisition audit for post-labor policy, not a new asset-pricing theorem or a general rejection of public investment.

## 1. The missing acquisition step

A social dividend requires a claim on output. A public fund can hold that claim. However, an analysis that starts with public assets has already passed an important fiscal step. Someone supplied the assets, paid for them, or gave up a competing claim. The source of that contribution changes who gains and who carries the risk.

This paper studies a conditional post-labor economy. Competitive wages are not a reliable source of household support. The government wants an aggregate payment of at least $F$ at the final date. This premise is not a forecast of AI deployment or labor demand. Nor does the paper establish how much income would meet people's needs.

The question is narrower: can a purchase of public equity finance that floor, and what additional contribution is required? A fair purchase transfers ownership to the government and cash to the seller. The seller does not lose equivalent wealth merely because the buyer is public. If borrowing pays the purchase price, the public asset comes with a liability.

The earlier studies in this programme test income access, liquidity, and other post-labor policy constraints. S005, for example, begins with an existing public asset and cash reserve. This study instead starts before acquisition. It has no payment calendar within the horizon and no real-goods allocation model. A successful financing certificate cannot establish service access or permanent support.

## 2. Prior work and the bounded contribution

Dynan, Elmendorf, and Sheiner [S1] directly ask how a public fund's equity purchases would be financed. Their public-ownership discussion identifies debt-financed acquisition as a leveraged investment and warns about expected returns that enter budgets without risk adjustment. Thus, the distinction between a public asset and a free fiscal resource is already present in current AI policy research.

Belda, Rojas, and Zoi [S2] provide even closer formal work. Their two-date economy has a fund that borrows to buy risky stocks. Its gains and losses pass to the treasury, whose tax revenues support the fund's debt. Their model can produce fiscal and welfare benefits through lower tax distortions, with increased macroeconomic volatility. Its public-sector budget equations explicitly include both purchase finance and repayment. This is a direct precedent, not an overlooked exception.

Korinek and Lockwood [S3] discuss public equity as a means of sharing AI returns and adapting public finance as labor income declines. That broader policy purpose is compatible with this paper's financing constraint. Public control, broad ownership, better tax enforcement, and reduced distortions can matter even when a fair asset purchase has zero initial net value.

The present contribution is a compact guarantee test that states the missing fiscal contribution for a chosen ownership share. It separates physical probabilities from state prices, includes a beneficial fiscal hedge, and prices a defaulting debt claim consistently. These steps apply familiar budget and no-arbitrage logic. No mathematical priority is claimed. The selected search cannot establish that this exact example or certificate has never appeared elsewhere.

The distinction from [S2] is the policy target and scope. This model fixes asset payoffs, state prices, and outside tax receipts. It asks for a minimum payment in every listed state. It does not optimize expected social welfare or model how public ownership changes prices, output, or tax distortions. Its negative result cannot refute the benefits that [S2] obtains through those omitted channels.

## 3. Two dates and explicit financing

There are two dates, 0 and 1, and finitely many states $s$ at date 1. Each state has a strictly positive state price $m_s$. This is the date-0 price of one unit delivered only in that state. Define the safe gross return

$$R_f=\frac{1}{\sum_s m_s}.$$

Physical probabilities $p_s$ also sum to one. They describe expected outcomes, but need not be proportional to state prices. A bad-state unit can be valuable even when that state has a low physical probability.

One unit of equity pays $y_s\geq0$. This includes all modeled final cash, including any terminal liquidation value. No residual asset is counted after date 1. Its fair purchase price is

$$P=\sum_s m_s y_s.$$

The government buys a fraction $a\in[0,1]$ at cost $aP$. The seller receives that payment at date 0. The government obtains an outside initial fiscal contribution $C\geq0$. This can be an explicit tax, grant, or transfer of existing public cash. It is a resource taken from someone or another public use, not income produced by the transaction.

If $C<aP$, the government borrows $D=aP-C$. If $C>aP$, it places the excess in a safe deposit $S=C-aP$. In general,

$$D=\max\{aP-C,0\},\quad S=\max\{C-aP,0\},\quad C+D=aP+S. \tag{1}$$

The borrowing and deposit have the same safe return. This is an explicit benchmark. The debt has full public recourse and must be repaid before the social dividend. Its safety requires adequate fiscal backing; a negative final balance reveals that the stated backing is insufficient.

At date 1, the government also collects outside fiscal resources $T_s\geq0$. These are net receipts available for this payment after other public duties. Taxpayers or donors supply them. They are not dividends from the purchased asset counted a second time. Their availability is assumed and must be tested in a real application.

Final resources after debt service are

$$Z_s(a,C)=ay_s+R_fS-R_fD+T_s
=T_s+a(y_s-R_fP)+R_fC. \tag{2}$$

When $Z_s<0$, the stated sources cannot repay debt. The number is a financing gap, not a negative payment to households. A positive floor requires $Z_s\geq F$ in every state. There is no default, emergency contribution, or unrecorded tax within this guarantee test.

## 4. Value, guarantees, and risk allocation

### Proposition 1. Fair acquisition preserves state-price value

Under the stated pricing and financing assumptions,

$$\sum_s m_s Z_s=C+\sum_s m_s T_s. \tag{3}$$

Therefore, a guarantee of $F\geq0$ requires

$$C+\sum_s m_sT_s\geq\frac{F}{R_f}. \tag{4}$$

**Proof.** The purchased asset has value $aP$. The debt-financing term has value $aR_fP\sum_s m_s=aP$, so these terms cancel. The safe contribution has value $R_fC\sum_s m_s=C$. This proves (3). Multiply each inequality $Z_s\geq F$ by its positive state price and sum to obtain (4). ∎

Equation (4) is necessary, but may be insufficient for the restricted portfolio. Resources can have adequate total value and still arrive in the wrong state. Complete insurance markets could permit other trades, but the policy here permits only this equity share and safe financing.

With no initial contribution and no outside fiscal resources, no positive floor is possible. A strictly positive expected premium does not change that conclusion. The premium can compensate exposure to unfavorable states. It is not a separate deposit available with certainty.

### Proposition 2. Exact initial contribution

For a fixed share $a$, the smallest nonnegative initial fiscal contribution that guarantees $F$ is

$$C^*(a)=\max\left\{0,\max_s\frac{F-T_s-a(y_s-R_fP)}{R_f}\right\}. \tag{5}$$

**Proof.** Rearrange each condition in (2), using $R_f>0$. The contribution must exceed every displayed threshold and zero. Their maximum is sufficient. If positive, any smaller contribution fails in a state that attains it. ∎

The function is convex and piecewise linear in $a$. The maximum floor with no initial contribution is

$$G(a)=\min_s[T_s+a(y_s-R_fP)]. \tag{6}$$

It is concave and piecewise linear. Evaluate the endpoints and all intersections of its state lines to find a maximum on $[0,1]$. The code does this exactly. It selects the smallest share if several shares attain the same maximum. Maximizing $G$ also minimizes (5), although a zero-contribution floor can allow further tied choices. The reported share is the floor-maximizing share, not necessarily the smallest share that meets a lower target.

### Positive implication: acquisition can hedge fiscal resources

Fair purchase does not create value, but it can change the worst-state payment. A positive equity position can help when the financed payoff $y_s-R_fP$ is high in states where $T_s$ is low. It can hurt when both fall together. No measured correlation coefficient is needed to check a finite set of states.

This is a fiscal portfolio result, not a national welfare result. A higher government floor may transfer risk to sellers, taxpayers, or other investors. Their consumption, existing portfolios, and preferences are outside the model.

## 5. Executed cases

The code uses six synthetic environments, a five-point ownership display grid, and each exact optimum. It retains all state results. State prices, probabilities, payoffs, taxes, and targets are explicit inputs. All arithmetic uses exact fractions. No Monte Carlo simulation or statistical estimation is involved.

### 5.1 Expected profit can coexist with a large funding gap

In the first case, asset payoffs are 0 and 100. State prices are 0.6 and 0.4, so $R_f=1$ and $P=40$. Physical probabilities are 0.1 and 0.9. Expected asset cash is 90. A fully borrowed purchase therefore has expected net cash of 50.

Its state balances are nevertheless $(-40,60)$. The low state cannot even repay debt from the asset. With no outside taxes and full ownership, a floor of 15 requires $C=55$. Equation (1) then gives a purchase of 40 and a safe deposit of 15, with no debt. The adverse state receives only the safe deposit; the favorable state receives 115.

If ownership is optional, the smallest required contribution is 15, attained at zero equity. The additional 40 required at full ownership is protection against the chosen risky position. This does not mean equity is always undesirable. It means that a pure worst-state floor has a different objective from expected return or public control.

Holding state prices fixed, the high-state physical probability is then set to 0.1, 0.5, and 0.9. Expected financed surplus is respectively −30, 10, and 50. The contribution needed at full ownership remains 55. These are alternative synthetic probability assignments, not estimated beliefs.

### 5.2 An acquisition that improves the guarantee

Let equity pay $(0,60)$, with equal state prices of 0.5, so the price is 30. Existing net tax resources are $(30,0)$. Without acquisition, the worst-state floor is zero. A half-unit purchase costs 15 and is fully debt financed. After repayment, total resources are

$$ (30,0)+\tfrac12[(-30,30)]=(15,15).$$

The government can thus guarantee 15 with no new initial contribution. The tax claim already has state-price value 15. Equation (3) still holds exactly. The acquisition transfers resources from the tax-rich state to the tax-poor state. It does not create the value of the guaranteed payment.

If taxes instead equal $(0,30)$, both the tax stream and asset are weak in the same state. The best share is zero. A floor of 15 requires an initial contribution of 15. At full ownership, balances before that contribution are $(-30,60)$, so the requirement is 45.

### 5.3 Additional finite-state checks

| Case | Asset price | Outside tax value | Best share for the worst state | Maximum floor with $C=0$ | Initial contribution for target |
| --- | ---: | ---: | ---: | ---: | ---: |
| Expected risk premium | 40 | 0 | 0 | 0 | 15 |
| Fiscal hedge | 30 | 15 | 1/2 | 15 | 0 |
| Common loss | 30 | 15 | 0 | 0 | 15 |
| Three states | 42 | 18 | 1/3 | 16 | 0 |
| Weak tax capacity | 30 | 7.5 | 1/4 | 7.5 | 7.5 |
| Safe asset | 95.2381 | 0 | 0 | 0 | 14.2857 |

Targets are 15 except in the three-state case, where the target is 16. Contributions use the displayed best share. The three-state case has asset payoffs $(0,60,120)$, state prices $(0.5,0.3,0.2)$, and taxes $(30,10,0)$. At share $1/3$, balances are $(16,16,26)$. This also shows that the minimum payment can be below the state-price value of outside taxes.

The weak-tax case reduces the first fiscal-hedge tax receipt from 30 to 15. Its best floor falls to 7.5. Claiming the old guarantee would require resources no longer present. The safe-asset case uses a gross safe return of 1.05. A fair financed purchase has zero net payoff in each state; the target needs a safe initial contribution of $15/1.05$.

## 6. Default cannot be inserted for free

A tempting calculation gives lenders a fixed promise of 40 in the first case, lets the fund default when the asset pays zero, and allocates the positive residual to residents. The residual becomes $(0,60)$, with physical expectation 54. But the lenders now receive $(0,40)$, whose fair price is only 16. They do not supply the 40 needed for acquisition. The missing 24 is exactly the state-price value of the residual equity.

More generally, for an asset-only debt claim with face value $K$, lenders receive $\min(K,y_s)$ and residual equity receives $(y_s-K)^+$. Their fair prices add to $P$. If defaulting debt alone raises the whole purchase price, strictly positive state prices imply that residual equity is zero in every state. Any positive residual would leave a purchase funding gap.

This result assumes no outside guarantee, lender subsidy, or tax backing. Add one explicitly and a different result is possible. The guarantor then carries the cost or risk. The calculation cannot simultaneously assume default, full safe-price debt proceeds, and no other contribution.

## 7. Strategies for policy design

First, prepare an acquisition balance sheet before announcing a dividend. State the seller's payment, borrowing proceeds, initial public contribution, and debt terms. Label contributed shares, taxes paid in equity, voluntary gifts, and purchased shares separately. They have different incidence even when the resulting public portfolio looks the same.

Second, report expected payments and guaranteed payments as different objects. An expected return can inform investment policy. A basic payment promise requires an adverse-state funding plan. Report who supplies any shortfall and whether that source remains usable when AI asset values fall.

Third, compare the purchased asset with the whole fiscal position. The hedge example supports public acquisition when it protects a weak revenue state. The common-loss example warns against concentration in the same firms and economic conditions that support the tax base. A larger public stake is not itself a stronger guarantee.

Fourth, preserve the distinction between investment benefits and financial accounting. Better governance, competition, public control, or lower tax distortions can justify a purchase. Such benefits must be specified and assessed. They cannot be inferred from subtracting a low borrowing rate from a risky expected return. The broader mechanism in [S2] illustrates why a fuller model can support public investment without contradicting the present identity.

Finally, trace the burdens of fiscal support. An initial contribution can reduce current private consumption or another public programme. State taxes can protect residents only if collection is feasible and does not impose unacceptable hardship on the same people. The model takes these resources as net available amounts. It supplies no ethical or legal justification for obtaining them.

## 8. Limits, reproduction, and disclosure

The model holds prices, output, taxes, and the safe borrowing rate fixed. It excludes transaction costs, market power, political control benefits, tax distortions, inflation, international claims, and limits on state-contingent collection. A government may have special borrowing advantages; their source and incidence require a different model. This paper does not assume that market prices capture all social value.

Every state price is positive. Omitting a severe state can make a guarantee look stronger than it is. Physical probabilities are illustrative and do not determine the floor. The final equity payoff includes all asset value; the same capital cannot finance another payment after date 1. A recurring social dividend needs a multi-period accumulation and solvency plan.

Run from the repository root:

```sh
python3 studies/2026-10-11-public-capital-acquisition/code/model.py
python3 -m unittest discover -s studies/2026-10-11-public-capital-acquisition/code -p 'test_*.py' -v
```

Python's standard library is sufficient. Nine tests check transaction balance, state-price reconciliation, exact floor funding, three interior or boundary choices, probability sensitivity, default pricing, and a separate 1,001-point ownership check. Inputs, complete finite-state results, runtime, and hashes are retained. The analysis is exploratory and not preregistered. Short source extracts and exact provenance are public; full third-party files are not redistributed. Separate internal AI review is complete. See [review](reviews/critical-review.md), [response](reviews/author-response.md), and [completion gates](completion-gates.md). No human review or external acceptance is implied.

## References

- **[S1]** Karen Dynan, Douglas Elmendorf, and Louise Sheiner. 2026. *How Might Fiscal Policy Respond to the Rise of Artificial Intelligence?* NBER Working Paper 35437, July, pages 34–36. [Publisher PDF](https://www.nber.org/system/files/working_papers/w35437/w35437.pdf). © 2026 by the authors.
- **[S2]** Pau Belda, Luis E. Rojas, and Sarah Zoi. 2025. *Can a Sovereign Wealth Fund Improve Fiscal Sustainability?* February version, introduction and Section 2, especially public budget equations (1)–(2). [Author PDF](https://pau-belda.eu/wp-content/uploads/Belda_Rojas_Zoi_SWF.pdf).
- **[S3]** Anton Korinek and Lee M. Lockwood. 2026. *Public Finance in the Age of AI: A Primer*. January Brookings version, Section 4. [Inspected PDF](https://www.brookings.edu/wp-content/uploads/2026/01/Korinek-Lockwood-FINAL-for-website.pdf).
