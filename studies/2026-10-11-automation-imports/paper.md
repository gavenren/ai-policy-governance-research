# Funding a Post-Labor Income Floor When AI Is Imported
## Tax Receipts, Domestic Production, and the Cost of Redistribution

> **State:** Complete-study draft. **Study:** S006. **Date:** 11 October 2026.
> **Evidence cutoff:** 2026-10-11T21:00:53Z for the five retained source captures; subsequent reading checked those captures. The review is selective.

## Abstract

A country can use AI extensively without owning the firms that supply it. A tax on imported AI may then appear to offer a way to fund residents who no longer earn wages. But the tax also raises a production cost: domestic output and rents fall, including the public revenue already drawn from those rents. This paper asks how much an import levy can add to transfers without reducing aggregate domestic consumption. A static model gives a closed-form limit determined by tax pass-through, real collection costs, and the public share of domestic rents. It also identifies when a single levy meets the same requirements across different economic states. In 1,296 synthetic policy-state cases, 597 positive levies increase transfer funding while domestic consumption falls; in 168, positive levy payments accompany a fall in net public funding. When the foreign price does not respond and the levy passes fully to domestic users, every positive levy reduces domestic consumption. All positive levies also reduce global surplus in the benchmark. The results distinguish a new source of gross receipts from a net addition to public resources and from a gain to the country as a whole.

## 1. Introduction

The location of AI production matters for the distribution of its gains. A government may wish to support people whose wages have disappeared, yet own little of the technology on which domestic firms depend. Taxing imported AI could provide public receipts. Whether those receipts represent new national resources is a different question: the tax can also make local production more costly and reduce income that was already available to residents and the state.

The distinction appears in a simple example. A levy of two units raises usable receipts of 12.8, but domestic public income from other sources falls by 2.88. Net transfer funding rises by 9.92, and total domestic consumption rises by 1.28. Raising the levy to four increases net transfer funding further, to 14.08 above its baseline. Total domestic consumption, however, is now 1.28 below baseline. A policy that raises more money for recipients can leave the country with less to consume.

This paper asks how much extra transfer income an AI-importing economy can obtain while preserving its previous aggregate consumption. The model contains an imported AI input, local productive assets, foreign supply, and an inherited public claim on domestic rents. Human labor earns no income. The analysis separates actual levy payments, receipts available after collection costs, and the net change in the transfer budget. It then derives the highest funding increase that satisfies both the recipient target and the domestic consumption constraint.

The aggregate constraint is a stated policy choice, not a complete ethical rule. A society may accept some aggregate loss to reduce severe poverty. Conversely, an aggregate gain may conceal substantial losses for particular households. The model therefore reports recipient, owner, and aggregate outcomes separately. It also reports the foreign effect: a better import price for the domestic economy transfers income from suppliers abroad and is not itself a global gain.

The disappearance of wages is a conditional setting, not a forecast. Present exposure to AI does not establish that all jobs will disappear. The unit of analysis is one synthetic economy under one levy, and the numerical values illustrate its mechanisms. They are neither a country calibration nor a recommendation for an actual national tax rate.

## 2. Related literature

Wossnig separates domestically owned automation from imported AI rents [A1]. His stock-flow-consistent simulation studies source taxation, foreign ownership, behavioral responses, and safety-net funding. It already establishes that ownership location changes the relevant fiscal question. Its limitations identify welfare analysis and strategic enforcement as unfinished areas. This paper does not reproduce its dynamics or validate its quantitative results. It adds a small static consumption test to the import-country question.

Becker is the closest tax-theory source [A2]. He studies output taxation when profit taxes, foreign ownership, tax avoidance, and pass-through interact. His results include public-revenue effects from changing profits and a distinction between national and global welfare. Thus, neither tax incidence nor the interaction of tax bases is a new idea here. This paper fixes an inherited domestic public claim and makes a floor-feasibility problem explicit. It then gives a closed form and a common-policy test across states.

Korinek and Lockwood distinguish different fiscal stages of transformative AI [A3]. They also distinguish final use, intermediate use, normal returns, rents, and public equity. Their analysis cautions against treating all visible AI activity as one tax base. Our levy applies to an intermediate input and therefore has a production cost. We do not treat it as a general substitute for a tax on final consumption.

Two further comparisons prevent a broader novelty claim. Richter's publisher abstract describes digital-import taxation and a possible international profit-sharing response [A5]. Full text was not accessible in this run; no theorem-level comparison is claimed. Pujolas and Rossbach distinguish tariff-revenue maxima from domestic-welfare maxima in a quantitative trade model [A6]. Sections 4.2 and Appendix A explicitly count the return of tariff revenue to residents. The present paper does not claim that the gap between fiscal and welfare objectives is new.

The paper brings these issues together by asking how much a levy can add to transfers for people without assets after accounting for the domestic public revenue it displaces. It derives a closed-form limit under a domestic no-loss condition and tests whether a single levy can meet that condition across adverse states. The derivations use standard quadratic surplus analysis. The searched work does not establish whether an equivalent formula exists elsewhere. The contribution is therefore a limited application and synthesis of established incidence analysis.

This study differs from S004, *A Consumption Floor After Human Labor*. S004 holds domestic output fixed and studies scarcity in an essential-goods market. This study has a traded AI input, responsive output, a foreign supply price, and a domestic-versus-global consumption comparison. It does not add a new jurisdiction to S004's model.

The search log records multiple query forms and reference following. The review is selected, not systematic. The retained primary sources are linked to short extracts and exact capture hashes. No current tax-law status is used as a premise.

## 3. The model

### 3.1 Imported AI and domestic production

Population is one. A share $n$, with $0<n<1$, owns no assets and receives a public transfer. The other residents own local productive assets. No resident earns wages. All residents consume one final good, whose traded price is one. Utility is linear in this good. Aggregate consumption is therefore also an unweighted domestic welfare measure in this model.

Domestic firms buy $q$ units of an imported AI service. They produce net final output

$$V(q)=Aq-\frac{b}{2}q^2,\qquad A>c\geq0,\quad b>0.$$

The decreasing marginal product represents a fixed local complement. It could represent land, local infrastructure, or a fixed customer base. No human labor is required. The function applies only over the analyzed range. It is not a technological forecast.

Foreign supply has inverse price $p(q)=c+dq$, with $d\ge 0$. This is competitive supply with increasing marginal resource cost, not an assumed monopoly pricing rule. Foreign suppliers can earn inframarginal producer surplus when $d>0$. The input need not be a literal model token. Its unit must be stable for a per-unit levy to be meaningful.

A levy creates an actual user-price wedge $t\ge 0$. Domestic firms are price takers. Their first-order condition is $A-bq=p+t$. Define

$$B=b+d,\quad m=A-c,\quad q_0=\frac{m}{B},\quad \lambda=\frac{b}{B}.$$

For $0\le t\le m$, equilibrium imports and domestic profit are

$$q(t)=q_0-\frac{t}{B},\qquad \pi(t)=\frac{b}{2}q(t)^2. \tag{1}$$

The user price rises by $\lambda t$; the foreign price falls by $(1-\lambda )t$. Thus $\lambda$ is the pass-through of the wedge to the domestic user. A genuinely small country with a fixed foreign price has $d=0$ and $\lambda =1$. We do not call an economy price-taking abroad when the model gives it a terms-of-trade effect.

### 3.2 Public receipts and household consumption

The public sector receives an inherited share $\theta$ of domestic profit, with $0\le \theta <1$. It can represent a nondistortionary rent tax or a pre-existing equity claim. Private domestic owners receive the rest. The share is fixed across the levy comparison. Because it multiplies all profits by the same positive factor, it does not alter the firm's input choice. Acquisition costs, investment responses, and avoidance of this claim are outside the model.

Actual levy payments are $tq$. The share $e$, with $0<e\le 1$, is usable public revenue. The remainder $(1-e)tq$ is a **real resource cost** of collection and compliance. It is not an unpaid tax, a transfer to domestic employees, or money that remains with the supplier. Evasion that reduces the actual price wedge needs a different model. When the levy is active, the system also uses a fixed real resource cost $K\ge 0$. At $t=0$, this cost is zero.

For $t>0$, the transfer budget is

$$R(t)=\theta\pi(t)+etq(t)-K. \tag{2}$$

All of $R$ goes to recipients. Consumption per recipient is $x(t)=R(t)/n$. Total owner consumption is $(1-\theta)\pi(t)$. No extra government consumption is added. Their sum is

$$W(t)=\pi(t)+etq(t)-K. \tag{3}$$

This budget returns usable levy receipts to consumers once. An independent resource identity is

$$W(t)=V(q)-p(q)q-(1-e)tq-K. \tag{4}$$

Domestic output pays foreign suppliers, real collection costs, and domestic consumption. Equations (3) and (4) agree. Counting $tq$ as a domestic loss and failing to add the transfer back would overstate the cost. Counting receipts without subtracting the fall in production rents would overstate the gain.

The baseline is $R_0=\theta bq_0^2/2$ and $W_0=bq_0^2/2$. The floor target is an increase $D\ge 0$ in total recipient funding. It means $x\ge x_0+D/n$, not an arbitrary currency amount that is held fixed across economies with different baseline resources. The positive-target feasible set below has nonnegative transfer budgets. Algebraic configurations with a negative budget are not implementable consumption policies.

## 4. The limits to additional funding

Let $L(t)=π_0-π(t)$ be lost domestic profit. For a positive levy,

$$\Delta R=etq-\theta L-K,\qquad
\Delta W=etq-L-K. \tag{5}$$

Gross tax payments, usable receipts, and net transfer funding are different quantities. The levy displaces domestic public revenue by $\theta L$; there is no deliberate cut in $\theta$. Private owners lose $(1-\theta )L$. Hence

$$\Delta R-\Delta W=(1-\theta)L. \tag{6}$$

A transfer gain can exceed the aggregate gain because it also redistributes domestic income from owners. This is not necessarily undesirable. It must be named correctly.

For $u\in \{\theta ,1\}$, define

$$a_u=(e-u\lambda)q_0,\qquad
b_u=\frac{e-u\lambda/2}{B}.$$

Then $\Delta R=a_\theta t-b_\theta t^2-K$ and $\Delta W=a_1t-b_1t^2-K$.

### 4.1 The funding limit

Assume $K=0$. If $e\le \lambda$, no positive levy preserves $W_0$. The maximum feasible funding increase is zero. If $e>\lambda$, define

$$t_W=m\frac{e-\lambda}{e-\lambda/2},\qquad
t_R=m\frac{e-\theta\lambda}{2e-\theta\lambda},\qquad
t^*=\min\{t_W,t_R\}. \tag{7}$$

The largest increase in recipient funding consistent with $\Delta W\ge 0$ is

$$D^*=a_\theta t^*-b_\theta(t^*)^2. \tag{8}$$

A nonnegative target $D$ is feasible if and only if $D\le D^*$.

The result follows from two quadratic relationships: one describes transfer funding and the other describes total domestic consumption. The largest permitted levy may arrive before the peak of the funding curve. Appendix A.1 gives the proof.

For the revenue peak itself to pass the no-loss condition, the parameters must satisfy

$$2e^2-3e\lambda+\theta\lambda^2\geq0. \tag{9}$$

This follows by multiplying $t_R\le t_W$ by the positive denominators. Equation (9) is a useful diagnostic, not an optimal-tax rule. A low existing public claim leaves more private domestic income available for redistribution. This can make the transfer peak occur beyond the domestic no-loss boundary.

The result gives a strong negative case. With full pass-through, $\lambda =1$ and $e\le 1$, so a positive levy always reduces total domestic consumption. It can still raise recipients' income. Its benefit then comes from domestic redistribution, not from a free foreign revenue source.

### 4.2 A policy that must work in more than one state

A government rarely knows the future supply response and collection cost with certainty. A levy that works under the central estimate may fail when foreign suppliers absorb less of it, collection becomes more costly, or local productivity is lower. The analysis therefore also requires the same levy to meet a specified transfer increase and preserve domestic consumption in every state in a stated set. It assigns no probabilities to those states.

Each state's conditions define an interval of acceptable levy rates. A common policy exists only where all those intervals overlap. A fixed collection cost can remove small levies from the acceptable set because their receipts are too small to cover that cost. At the other end, the consumption loss places an upper bound. Appendix A.2 gives the exact roots and interval-intersection condition. Including even one state with full pass-through rules out a positive levy under the no-loss requirement.

A verified supplier-access limit can narrow the permitted interval further. This is a constraint on the policy, not a model of suppliers' strategic threats or a prediction of withdrawal. The numerical analysis varies such a limit as a sensitivity case.

### 4.3 The international cost

There is also an international limit. Foreign producer surplus is $dq^2/2$. Add it to domestic consumption and compare with the untaxed baseline:

$$\Delta W_{global}=-\frac{t^2}{2B}-(1-e)tq-K<0\quad(t>0). \tag{12}$$

This follows by subtracting total foreign resource cost $cq+dq^2/2$ from domestic output. Untaxed quantity maximizes the resulting concave surplus. There is no pre-existing externality here for the levy to correct. A domestic no-loss result therefore does not justify a claim of global benefit.

## 5. Numerical results

All inputs are in [design.json](data/design.json). Base values are $A=14,c=4,b=1,d=0.25,\theta =0.25,e=1,K=0,n=0.8$. Thus $q_0=8$, $\lambda =0.8$, baseline public income is $8$, and baseline recipient consumption is $10$. Units are synthetic annual units per total resident unless stated otherwise.

### 5.1 Higher transfers can accompany lower domestic consumption

The following values come from [scenarios.csv](results/scenarios.csv). Each change uses that row's own no-levy baseline.

| Case | Levy | Usable levy receipts | Lost domestic public income | Net funding gain | Domestic consumption change |
| --- | ---: | ---: | ---: | ---: | ---: |
| Base, moderate levy | 2 | 12.800 | 2.880 | 9.920 | 1.280 |
| Base, high levy | 4 | 19.200 | 5.120 | 14.080 | −1.280 |
| Full pass-through | 2 | 16.000 | 4.500 | 11.500 | −2.000 |
| Collection share $e=0.75$ | 2 | 9.600 | 2.880 | 6.720 | −1.920 |
| Public share $\theta =0.8$ | 2 | 12.800 | 9.216 | 3.584 | 1.280 |
| Fixed cost $K=0.5$ | 2 | 12.800 | 2.880 | 9.420 | 0.780 |
| Lower productivity $A=10$ | 2 | 6.400 | 1.600 | 4.800 | 0.000 |
| Flatter foreign supply $d=0.1$ | 2 | 14.545 | 3.719 | 10.826 | −0.331 |

At $t=2$, base recipient consumption rises from $10$ to $22.4$; total domestic consumption rises by $1.28$. Yet global surplus falls by $1.6$. At $t=4$, recipient consumption reaches $27.6$ while total domestic consumption falls by $1.28$. The group and aggregate objectives disagree.

For the base economy, $t_W=3.3333$ and $t_R=4.4444$. The largest no-loss funding uplift is 13.3333, which supports recipient consumption of 26.6667. The unconstrained funding peak is 14.2222. Maximizing funds would exceed the no-loss bound. These are quantities in the model, not percentages for an actual tax instrument.

A higher public share reduces the **additional** funding gain because more baseline domestic income is already public. It does not reduce the level of recipient income in this comparison. At $\theta =0.8$, baseline recipient consumption is $32$; with $t=2$, it is $36.48$. This prevents the false inference that a smaller measured uplift makes public ownership worse.

### 5.2 Results across the full grid

The grid has 216 states: three productivity values, four foreign supply slopes, three public shares, three collection shares, and two fixed costs. Six levy values give 1,296 rows. There are 1,080 positive-levy rows. All are retained in [grid.csv](results/grid.csv).

Among positive levies, 168 have positive levy payments but negative net funding. Another diagnostic finds 597 with positive net funding and negative domestic consumption change. There are 312 with positive net funding and nonnegative domestic consumption change. The second and third counts do not include zero net changes. These are counts over chosen states, not estimated probabilities. The grid is not a representative sample of countries.

Continuous optimization gives positive no-loss funding in 93 of the 216 states. This count is separate from the six tested levy levels. The largest resource-accounting residual is $2.85\times10^{-14}$ in absolute value, within floating-point error.

### 5.3 A single policy across different states

| Required state set | Maximum common uplift | Levy that achieves it |
| --- | ---: | ---: |
| Base only | 13.3333 | 3.3333 |
| Base and flatter foreign supply | 8.6667 | 1.6667 |
| Base and lower productivity | 4.8000 | 2.0000 |
| Base and full pass-through | 0 | 0 |
| Base and collection share $0.75$ | 0 | 0 |
| Base and fixed cost $0.5$ | 12.1871 | 2.9843 |

The common uplift is the minimum gain across included states. It does not mean the final income level is equal in each state. The code uses the interval test and bisection on the funding target. It does not replace the analytical feasible set with a coarse tax grid.

A supplier-access cap also matters. With base parameters, caps of $1$, $2$, and $3$ limit no-loss funding to $5.68$, $9.92$, and $12.72$. The uncapped limit is 13.3333. No claim is made that these caps describe actual supplier conduct.

## 6. Implications for policy

The first implication is a matter of fiscal measurement. A government considering an AI import levy needs to report actual payments, usable receipts, and the net addition to funding after other public revenue is lost. In this model, the last adjustment is automatic: the input becomes more expensive, domestic rents fall, and so does the state's share of those rents. A transfer promise based only on gross receipts therefore overstates what the instrument can supply.

The distributional purpose should be stated just as clearly. People without assets can gain even as owners and the country as a whole lose consumption. That may be a defensible choice, but it is a domestic redistribution with an aggregate cost, rather than a costless claim on foreign wealth. Even a policy that preserves total domestic consumption is not a Pareto improvement here, since domestic owners lose under every positive levy. The model helps identify those tradeoffs; it does not supply the social weights needed to resolve them.

Uncertain incidence is especially important for an importing country. If the government cannot establish that its levy reduces the foreign price, full pass-through is a relevant adverse state. Under the paper's no-loss condition, including that state removes the positive-levy option. The remaining choices could include a smaller transfer promise, another domestic funding base, or a negotiated external transfer. Calling domestic tax revenue an international contribution does not change who bears its cost.

International revenue sharing would be a different policy. An actual transfer from abroad could raise both recipient income and domestic resources without taxing this intermediate input at the border. But its donor cost, legal basis, allocation rule, enforcement, and investment effects would still require analysis. Nothing in the present model establishes that such an agreement will be offered or sustained. The global loss in equation (12) instead explains why a unilateral levy, even when it helps the importing country, cannot by itself provide a global welfare strategy in this benchmark.

These conclusions identify the accounts and comparisons needed to assess a proposal. They do not recommend a particular tax. A credible income floor needs a claim on resources, a record of the claims it displaces, and a clear account of the countries and groups that carry the burden.

## 7. Limitations

Supply is competitive and linear; monopoly pricing, quality changes, bundled services, and prices that rise by more than the tax are excluded. The model is static and omits AI innovation, capital accumulation, retaliation, and exchange rates. It has one final good, so cash does not face a separate housing or essential-supply limit. Fixed local assets earn rents, but their ownership does not change. Public claims are inherited and nondistortionary. Collection losses are real resources by assumption. None of these quantities has been estimated for a post-labor economy.

The two objectives are also narrower than a complete social evaluation. Aggregate consumption gives each unit the same weight regardless of its recipient, while the transfer target imposes a separate distributional condition. A model with unequal marginal welfare weights could accept an aggregate loss that the present constraint excludes. Likewise, externalities or pre-existing distortions could change the global comparison. They are absent from this benchmark, so the paper draws no conclusion about levies designed to address them.

## 8. Conclusion

Imported AI can generate local output while its supplier income flows abroad. Taxing that input can fund transfers, but the resulting receipts do not measure the policy's net fiscal or economic gain. Domestic production rents and existing public revenue can fall at the same time. The joint funding test makes that tradeoff explicit and shows when a recipient gain exceeds what the economy can obtain without an aggregate loss. Its strongest negative case is full pass-through: a positive levy can redistribute domestic income, but cannot meet the no-loss condition by extracting new resources from foreign suppliers.

## Appendix A. Derivations

### A.1 The maximum funding increase

**Proof.** Rewrite the domestic change as

$$\Delta W=(e-\lambda)tq-\frac{\lambda t^2}{2B}.$$

For $e\le \lambda$ and $t>0$, this is negative, including at the choke point. For $e>\lambda$, $a_1,b_1>0$, so $\Delta W\ge 0$ exactly on $[0,t_W]$. Also $a_\theta,b_\theta>0$. The funding curve is a strictly concave quadratic with its peak at $t_R$. Its constrained peak is therefore at the smaller of these two values. Continuity from zero to that peak gives every target between zero and $D^*$. No larger target can pass. ∎

### A.2 Feasibility across states

For a state with $e>\lambda$, a constraint of the form

$$a_ut-b_ut^2-K\geq H$$

has a feasible interval between

$$r_u^{\pm}(H)=\frac{a_u\pm\sqrt{a_u^2-4b_u(K+H)}}{2b_u}, \tag{10}$$

provided the discriminant is nonnegative. Use $u=\theta ,H=D_i$ for funding and $u=1,H=0$ for domestic consumption. Intersect both intervals with $0<t\le m$. A fixed cost can create a strictly positive lower bound: a tiny levy can cost more than it provides.

### Proposition 2. Common-policy feasibility

A positive levy meets all state constraints if and only if every state has valid intervals and

$$\max_i\{r_{\theta,i}^{-}(D_i),r_{1,i}^{-}(0),0\}
\leq
\min_i\{r_{\theta,i}^{+}(D_i),r_{1,i}^{+}(0),m_i\}, \tag{11}$$

with a positive upper endpoint. A state with $e\le \lambda$ makes a positive no-loss policy infeasible.

**Proof.** Each concave quadratic is at least its target exactly between its real roots. The common levy must belong to every such interval. A finite intersection of closed intervals is nonempty exactly when its largest lower endpoint does not exceed its smallest upper endpoint. The earlier negative-case argument covers $e\le \lambda$. A zero levy remains feasible when every uplift target is zero. ∎

A verified supplier-access limit $t\le\bar t$ can be added to the upper bound. This describes a constraint; it does not explain a supplier's threat or estimate the chance of withdrawal. The experiment varies this limit as a sensitivity case.

## Appendix B. Reproduction and research record

Eight tests check direct production accounting, transfer cancellation, the quadratic formulas, full pass-through, collection failure, root endpoints, common-policy failure, global loss, invalid inputs, and access caps. A dense direct search with 20,001 tax values in each of six cases checks the computed optima. The tests and analysis use only the Python standard library. They verify the implementation and selected implications, not the realism of the model.

The [study README](README.md) provides the reproduction commands. [design.json](data/design.json) contains the inputs, and the results directory retains the scenarios, full grid, and common-policy calculations. The selected source record includes short extracts and exact capture hashes. No current tax-law status is a premise of the analysis.

## Research disclosure

Codex developed the analysis, wrote the manuscript, and ran the code. A separate coordinating AI agent completed the [critical review](reviews/critical-review.md) and an independent resource-accounting check; the [author response](reviews/author-response.md) and [completion gates](completion-gates.md) document their disposition. No human or journal peer review has occurred. No affiliation or endorsement is claimed, and funding and human conflicts have not been established. No repository reuse licence has been selected; source rights remain separate. The [editorial revision record](reviews/editorial-revision.md) records the later changes in presentation.

## References

- **[A1]** Wossnig, L. (2026). [Simulating a Post-Automation Economy](https://arxiv.org/html/2606.20649v1). arXiv:2606.20649v1. Read Sections 6.6, 6.15, 6.17, 10, and Appendix A.
- **[A2]** Becker, J. (2026). [When are digital services taxes optimal? Output taxes and profit shifting](https://doi.org/10.1007/s10797-026-09987-z). *International Tax and Public Finance*. Read Sections 2, 3, 5, and 6; selected appendix discussion.
- **[A3]** Korinek, A., and Lockwood, L. M. (2026). [Public Finance in the Age of AI: A Primer](https://www.brookings.edu/wp-content/uploads/2026/01/Korinek-Lockwood-FINAL-for-website.pdf). Brookings working-paper release, January 2026; manuscript dated 30 December 2025. Read Sections 2.4 and 4.2.
- **[A5]** Richter, W. F. (2021). [The Taxation of Digital Services as a Rent-Extracting Policy](https://www.mohrsiebeck.com/en/article/the-taxation-of-digital-services-as-a-rent-extracting-policy-101628fa-2021-0012/). *FinanzArchiv* 77(3), 225–246. Publisher abstract only.
- **[A6]** Pujolas, P., and Rossbach, J. (2026). [Fiscal Limits to Protectionism: The 2025 U.S. Tariff Laffer Curve](https://arxiv.org/html/2602.18938v1). arXiv:2602.18938v1. Read model overview, Section 4.2, and Appendix A.
