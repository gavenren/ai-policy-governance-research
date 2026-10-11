# Buying a Public Stake Without Buying a Guarantee
## Financing Public Ownership of AI Capital

> **State:** Complete-study draft. **Study:** S008. **Date:** 11 October 2026.
> **Evidence cutoff:** 2026-10-11T21:14:06Z, the end of source collection and selected close reading for this draft.

## Abstract

Public ownership of AI capital can distribute future income, but the acquisition itself needs financing. This paper asks what a fairly priced public equity purchase can contribute to a guaranteed social dividend when households no longer rely on wages. A two-date model separates the purchase payment, borrowing, other fiscal resources, and the minimum benefit. A debt-financed purchase changes the distribution of public resources across states without creating additional state-price value. The paper derives the initial fiscal contribution needed to meet the benefit in every listed state. In one example, buying the entire asset with debt produces expected net proceeds of 50 but a loss of 40 in the adverse state. Guaranteeing a payment of 15 while holding that asset requires 55 of initial fiscal capital. Acquisition can nevertheless improve the guarantee when the asset pays in states where tax receipts are weak: in a second example, it raises the worst-state payment from zero to 15 without a new initial contribution. The value is already present in the tax claim; the purchase reallocates its risk. The results clarify the distinction between expected investment returns, fiscal insurance, and resources that can support a firm payment promise.

## 1. Introduction

A proposal for a social wealth fund often begins with the income that public assets could pay to residents. Before that income can be distributed, however, the government must obtain the assets. Someone must contribute shares, pay for them, or give up another claim. A fund financed through borrowing has both an asset and a liability, and its ability to support a basic payment depends on how the two perform together.

Consider an asset that costs forty units and pays either zero or one hundred. Suppose its expected payoff is ninety. Buying it with debt appears to yield an expected surplus of fifty. Yet the government still owes forty when the asset pays nothing. A promise to pay residents fifteen in that state needs another source of funds. The attractive expected return has not supplied a guaranteed income.

The opposite case is also possible. If existing taxes are high when the asset pays little, and low when it pays well, an equity purchase can balance the public revenue stream. The model below gives an example in which a debt-financed purchase raises the minimum available payment from zero to fifteen. The purchase does not create financial value. It makes existing fiscal resources arrive in a more useful pattern.

This paper asks when public acquisition can support a minimum social dividend and how much additional fiscal capital is needed. It uses a two-date model with explicit purchase finance, state-contingent asset income, and outside public resources. Its focus is a payment of at least $F$ in every listed state, rather than the highest expected return. The analysis also examines a common financing shortcut: allowing the fund to default while assuming lenders still provide the full safe-debt amount.

The setting is an economy in which competitive wages are no longer a reliable basis for household support. This is a conditional policy problem, not a forecast of AI deployment or labor demand. The payment floor is taken as a public choice; the model does not establish what income would meet people's needs. It also has no within-horizon payment calendar or market for essential goods. The companion reserve study, S005, starts with an existing public asset and cash reserve. This paper starts one step earlier, with their acquisition.

## 2. Related literature

Dynan, Elmendorf, and Sheiner [S1] directly ask how a public fund's equity purchases would be financed. Their public-ownership discussion identifies debt-financed acquisition as a leveraged investment and warns about expected returns that enter budgets without risk adjustment. Thus, the distinction between a public asset and a free fiscal resource is already present in current AI policy research.

Belda, Rojas, and Zoi [S2] provide even closer formal work. Their two-date economy has a fund that borrows to buy risky stocks. Its gains and losses pass to the treasury, whose tax revenues support the fund's debt. Their model can produce fiscal and welfare benefits through lower tax distortions, with increased macroeconomic volatility. Its public-sector budget equations explicitly include both purchase finance and repayment. This is a direct precedent, not an overlooked exception.

Korinek and Lockwood [S3] discuss public equity as a means of sharing AI returns and adapting public finance as labor income declines. That broader policy purpose is compatible with this paper's financing constraint. Public control, broad ownership, better tax enforcement, and reduced distortions can matter even when a fair asset purchase has zero initial net value.

This paper contributes a compact test of the additional fiscal contribution needed to guarantee a payment at a chosen ownership share. It separates physical probabilities from state prices, includes a beneficial fiscal hedge, and prices a defaulting debt claim consistently. These steps apply familiar budget and no-arbitrage logic. The selected search does not establish mathematical priority for the result or its examples.

The distinction from [S2] is the policy target and scope. This model fixes asset payoffs, state prices, and outside tax receipts. It asks for a minimum payment in every listed state. It does not optimize expected social welfare or model how public ownership changes prices, output, or tax distortions. Its negative result cannot refute the benefits that [S2] obtains through those omitted channels.

## 3. Acquisition and financing

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

## 4. What can the public fund guarantee?

### 4.1 A purchase changes risk but does not create net financial value

Under the stated pricing and financing assumptions,

$$\sum_s m_s Z_s=C+\sum_s m_s T_s. \tag{3}$$

Therefore, a guarantee of $F\geq0$ requires

$$C+\sum_s m_sT_s\geq\frac{F}{R_f}. \tag{4}$$

The identity follows because the value of the purchased asset is matched by the value of its financing. What remains is the outside initial contribution and the value of the other fiscal resources. The guarantee condition then follows by valuing the minimum payment in every state. Appendix A gives the algebra.

Equation (4) is necessary, but may be insufficient for the restricted portfolio. Resources can have adequate total value and still arrive in the wrong state. Complete insurance markets could permit other trades, but the policy here permits only this equity share and safe financing.

With no initial contribution and no outside fiscal resources, no positive floor is possible. A strictly positive expected premium does not change that conclusion. The premium can compensate exposure to unfavorable states. It is not a separate deposit available with certainty.

### 4.2 The contribution needed to guarantee the payment

For a fixed share $a$, the smallest nonnegative initial fiscal contribution that guarantees $F$ is

$$C^*(a)=\max\left\{0,\max_s\frac{F-T_s-a(y_s-R_fP)}{R_f}\right\}. \tag{5}$$

Each state places a lower bound on the contribution. The largest of those bounds is both necessary and sufficient; any smaller amount leaves a shortfall in at least one state. Appendix A gives the proof.

The function is convex and piecewise linear in $a$. The maximum floor with no initial contribution is

$$G(a)=\min_s[T_s+a(y_s-R_fP)]. \tag{6}$$

It is concave and piecewise linear. Evaluate the endpoints and all intersections of its state lines to find a maximum on $[0,1]$. The code does this exactly. It selects the smallest share if several shares attain the same maximum. Maximizing $G$ also minimizes (5), although a zero-contribution floor can allow further tied choices. The reported share is the floor-maximizing share, not necessarily the smallest share that meets a lower target.

### 4.3 When acquisition can improve the worst-state outcome

Fair purchase does not create value, but it can change the worst-state payment. A positive equity position can help when the financed payoff $y_s-R_fP$ is high in states where $T_s$ is low. It can hurt when both fall together. No measured correlation coefficient is needed to check a finite set of states.

This is a fiscal portfolio result, not a national welfare result. A higher government floor may transfer risk to sellers, taxpayers, or other investors. Their consumption, existing portfolios, and preferences are outside the model.

## 5. Numerical examples

The code uses six synthetic environments, a five-point ownership display grid, and each exact optimum. It retains all state results. State prices, probabilities, payoffs, taxes, and targets are explicit inputs. All arithmetic uses exact fractions. No Monte Carlo simulation or statistical estimation is involved.

### 5.1 Expected profit and an adverse-state shortfall

In the first case, asset payoffs are 0 and 100. State prices are 0.6 and 0.4, so $R_f=1$ and $P=40$. Physical probabilities are 0.1 and 0.9. Expected asset cash is 90. A fully borrowed purchase therefore has expected net cash of 50.

Its state balances are nevertheless $(-40,60)$. The low state cannot even repay debt from the asset. With no outside taxes and full ownership, a floor of 15 requires $C=55$. Equation (1) then gives a purchase of 40 and a safe deposit of 15, with no debt. The adverse state receives only the safe deposit; the favorable state receives 115.

If ownership is optional, the smallest required contribution is 15, attained at zero equity. The additional 40 required at full ownership is protection against the chosen risky position. This does not mean equity is always undesirable. It means that a pure worst-state floor has a different objective from expected return or public control.

Holding state prices fixed, the high-state physical probability is then set to 0.1, 0.5, and 0.9. Expected financed surplus is respectively −30, 10, and 50. The contribution needed at full ownership remains 55. These are alternative synthetic probability assignments, not estimated beliefs.

### 5.2 A purchase that protects a weak tax state

Let equity pay $(0,60)$, with equal state prices of 0.5, so the price is 30. Existing net tax resources are $(30,0)$. Without acquisition, the worst-state floor is zero. A half-unit purchase costs 15 and is fully debt financed. After repayment, total resources are

$$ (30,0)+\tfrac12[(-30,30)]=(15,15).$$

The government can thus guarantee 15 with no new initial contribution. The tax claim already has state-price value 15. Equation (3) still holds exactly. The acquisition transfers resources from the tax-rich state to the tax-poor state. It does not create the value of the guaranteed payment.

If taxes instead equal $(0,30)$, both the tax stream and asset are weak in the same state. The best share is zero. A floor of 15 requires an initial contribution of 15. At full ownership, balances before that contribution are $(-30,60)$, so the requirement is 45.

### 5.3 Further examples

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

## 6. Default and the purchase price

A tempting calculation gives lenders a fixed promise of 40 in the first case, lets the fund default when the asset pays zero, and allocates the positive residual to residents. The residual becomes $(0,60)$, with physical expectation 54. But the lenders now receive $(0,40)$, whose fair price is only 16. They do not supply the 40 needed for acquisition. The missing 24 is exactly the state-price value of the residual equity.

More generally, for an asset-only debt claim with face value $K$, lenders receive $\min(K,y_s)$ and residual equity receives $(y_s-K)^+$. Their fair prices add to $P$. If defaulting debt alone raises the whole purchase price, strictly positive state prices imply that residual equity is zero in every state. Any positive residual would leave a purchase funding gap.

This result assumes no outside guarantee, lender subsidy, or tax backing. Add one explicitly and a different result is possible. The guarantor then carries the cost or risk. The calculation cannot simultaneously assume default, full safe-price debt proceeds, and no other contribution.

## 7. Implications for public ownership policy

The analysis supports a clear separation between the case for public ownership and the claim that ownership supplies free fiscal resources. Public control, competition, governance, or lower tax distortions can justify an acquisition. Those benefits require their own evidence. They cannot be inferred simply by subtracting a safe borrowing rate from a risky expected return. The broader mechanism in Belda, Rojas, and Zoi [S2] illustrates why public investment can be valuable without contradicting the financing identity developed here.

A proposal for a dividend fund should therefore begin with an acquisition balance sheet. The seller's payment, borrowing proceeds, initial fiscal contribution, and debt terms reveal where its resources come from. Contributed shares, taxes paid in equity, gifts, and purchased shares can produce similar public portfolios but have different distributional effects. A fair purchase transfers cash to the seller in exchange for the asset; it does not remove the seller's equivalent wealth merely by changing ownership.

Expected payments and guaranteed payments also need separate accounts. Expected returns are relevant to investment decisions, but a basic payment promise requires finance in adverse states. The proposal must identify who supplies a shortfall and whether that source remains available when AI asset values fall. Full public recourse shifts a debt obligation onto the wider fiscal position; it does not eliminate the obligation.

The fiscal-hedge example shows why that wider position matters. Acquisition can protect a weak tax state when the purchased asset pays well in it. Concentration in the same firms and conditions that support tax receipts can instead weaken the guarantee. A larger public stake is therefore not, by itself, a stronger minimum payment. The suitable share depends on the state's other resources and the policy objective.

Finally, the burdens of fiscal support remain part of the policy choice. Initial capital may reduce current private consumption or another public programme. Future taxes can support residents only if they are collectible and do not impose unacceptable hardship on the same population. The model takes those resources as net available amounts. It provides neither an ethical justification nor legal authority for obtaining them. These institutional questions remain essential even when the financial accounts balance.

## 8. Limitations

The model holds prices, output, taxes, and the safe borrowing rate fixed. It excludes transaction costs, market power, political control benefits, tax distortions, inflation, international claims, and limits on state-contingent collection. A government may have special borrowing advantages; their source and incidence require a different model. This paper does not assume that market prices capture all social value.

Every state price is positive. Omitting a severe state can make a guarantee look stronger than it is. Physical probabilities are illustrative and do not determine the floor. The final equity payoff includes all asset value; the same capital cannot finance another payment after date 1. A recurring social dividend needs a multi-period accumulation and solvency plan.

## 9. Conclusion

A public equity purchase can change when and where the state receives income. It does not, at a fair price, create additional financial value merely because the buyer is public. A positive expected surplus can coexist with an adverse-state shortfall, while a well-chosen purchase can improve a payment guarantee by offsetting weak tax receipts. The distinction turns on financing and the whole fiscal portfolio. A credible social dividend therefore requires an explicit account of the contribution, debt, outside resources, and risks that stand behind it.

## Appendix A. Proofs

### A.1 State-price value and the necessary guarantee condition

**Proof.** The purchased asset has value $aP$. The debt-financing term has value $aR_fP\sum_s m_s=aP$, so these terms cancel. The safe contribution has value $R_fC\sum_s m_s=C$. This proves (3). Multiply each inequality $Z_s\geq F$ by its positive state price and sum to obtain (4). ∎

### A.2 The exact initial contribution

**Proof.** Rearrange each condition in (2), using $R_f>0$. The contribution must exceed every displayed threshold and zero. Their maximum is sufficient. If positive, any smaller contribution fails in a state that attains it. ∎

## Appendix B. Reproduction and research record

Run from the repository root:

```sh
python3 studies/2026-10-11-public-capital-acquisition/code/model.py
python3 -m unittest discover -s studies/2026-10-11-public-capital-acquisition/code -p 'test_*.py' -v
```

Python's standard library is sufficient. Nine tests check transaction balance, state-price reconciliation, exact floor funding, three interior or boundary choices, probability sensitivity, default pricing, and a separate 1,001-point ownership check. Inputs, complete finite-state results, runtime, and hashes are retained. The analysis is exploratory and not preregistered. Short source extracts and exact provenance are public; full third-party files are not redistributed.

## Research disclosure

Codex wrote and executed the study. The separate internal AI [critical review](reviews/critical-review.md), [author response](reviews/author-response.md), and [completion gates](completion-gates.md) record the substantive checks. No human or journal peer review has occurred. No affiliation or endorsement is claimed; funding and human conflicts were not supplied. No repository reuse licence has been selected, and third-party source rights remain separate. The [editorial revision record](reviews/editorial-revision.md) records the later changes in presentation.

## References

- **[S1]** Karen Dynan, Douglas Elmendorf, and Louise Sheiner. 2026. *How Might Fiscal Policy Respond to the Rise of Artificial Intelligence?* NBER Working Paper 35437, July, pages 34–36. [Publisher PDF](https://www.nber.org/system/files/working_papers/w35437/w35437.pdf). © 2026 by the authors.
- **[S2]** Pau Belda, Luis E. Rojas, and Sarah Zoi. 2025. *Can a Sovereign Wealth Fund Improve Fiscal Sustainability?* February version, introduction and Section 2, especially public budget equations (1)–(2). [Author PDF](https://pau-belda.eu/wp-content/uploads/Belda_Rojas_Zoi_SWF.pdf).
- **[S3]** Anton Korinek and Lee M. Lockwood. 2026. *Public Finance in the Age of AI: A Primer*. January Brookings version, Section 4. [Inspected PDF](https://www.brookings.edu/wp-content/uploads/2026/01/Korinek-Lockwood-FINAL-for-website.pdf).
