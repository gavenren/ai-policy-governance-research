# Funding a Post-Labor Floor When AI Is Imported
## A Joint Test for Transfer Income and Domestic Consumption

> **State:** Complete-study draft. Executed analysis and separate internal AI review are complete.
> **Study:** S006, `2026-10-11-automation-imports`. **Date:** 11 October 2026.
> **Evidence cutoff:** 2026-10-11T21:00:53Z for the five retained source captures. Later reading checked those captures. This is not a full literature census.
> **Method:** Analytical model and deterministic synthetic experiments. No country calibration, forecast, or causal estimate.
> **AI disclosure:** Codex developed the analysis, wrote this text, and ran the code. The parent agent completed a separate critical review and an independent resource-accounting check. No human or journal peer review is claimed. No author affiliation or external endorsement is claimed. Funding and conflicts of a responsible human author have not been established.
> **Rights:** No repository reuse licence has been selected. Source rights are separate.

## Abstract

A country can use AI widely while it owns little of the AI supply. A levy on imported AI can raise public receipts, but this does not establish that it funds a sustainable income floor. The levy can also reduce domestic production rents and the public revenue already drawn from them. This paper derives a joint test for higher transfers and no fall in aggregate domestic consumption. In a static economy without wages, the test depends on price pass-through, collection resource costs, and existing public claims on domestic rents. A closed-form bound gives the largest increase in transfer funding that meets both conditions. A second result tests one levy across several adverse states. In 1,296 synthetic policy-state cases, 597 positive levies increase transfer funding while domestic consumption falls. In 168 cases, levy payments are positive while net public funding falls. Full pass-through rules out every positive levy under the no-loss condition. All positive levies reduce global surplus in this benchmark. The contribution is a compact decision test within established tax-incidence theory, with explicit fiscal displacement and uncertain states. It is not a new general theory of digital taxation or a recommendation for a national tax rate.

## 1. The question

Suppose AI can perform all economic tasks more cheaply than human workers. People still need claims on output. Their income can come from asset ownership, public services, or transfers. An importing country faces a further problem: the productive AI service can be available locally while its supplier income goes abroad.

The question here is narrow. **How much extra transfer income can a levy on imported AI provide without reducing total domestic consumption?** This is a conditional planning question. It does not predict that wages will disappear. It also does not treat present AI exposure as proof of job loss.

The test has two separate objectives. First, people without assets must receive a specified increase in consumption. Second, the country must retain at least its previous aggregate consumption. The second condition is an explicit policy constraint, not a complete ethical rule. A society can reasonably accept an aggregate loss to reduce severe poverty. Conversely, an aggregate gain can conceal large losses for some people. The model reports both group and aggregate effects so that one cannot stand in for the other.

The model also reports the foreign effect. A domestic gain from a better import price is partly a transfer from foreign suppliers. It is not a gain for the world. This matters for international governance. A policy process that considers only one country's receipts can select a policy that makes joint cooperation harder.

The unit of analysis is one synthetic economy under one levy. The target of inference is the stated model. Numerical values are illustrations in common units. They do not identify an optimal tax rate for any jurisdiction.

## 2. Prior work and the limited contribution

Wossnig separates domestically owned automation from imported AI rents [A1]. His stock-flow-consistent simulation studies source taxation, foreign ownership, behavioral responses, and safety-net funding. It already establishes that ownership location changes the relevant fiscal question. Its limitations identify welfare analysis and strategic enforcement as unfinished areas. This paper does not reproduce its dynamics or validate its quantitative results. It adds a small static consumption test to the import-country question.

Becker is the closest tax-theory source [A2]. He studies output taxation when profit taxes, foreign ownership, tax avoidance, and pass-through interact. His results include public-revenue effects from changing profits and a distinction between national and global welfare. Thus, neither tax incidence nor the interaction of tax bases is a new idea here. This paper fixes an inherited domestic public claim and makes a floor-feasibility problem explicit. It then gives a closed form and a common-policy test across states.

Korinek and Lockwood distinguish different fiscal stages of transformative AI [A3]. They also distinguish final use, intermediate use, normal returns, rents, and public equity. Their analysis cautions against treating all visible AI activity as one tax base. Our levy applies to an intermediate input and therefore has a production cost. We do not treat it as a general substitute for a tax on final consumption.

Two further comparisons prevent a broader novelty claim. Richter's publisher abstract describes digital-import taxation and a possible international profit-sharing response [A5]. Full text was not accessible in this run; no theorem-level comparison is claimed. Pujolas and Rossbach distinguish tariff-revenue maxima from domestic-welfare maxima in a quantitative trade model [A6]. Sections 4.2 and Appendix A explicitly count the return of tariff revenue to residents. The present paper does not claim that the gap between fiscal and welfare objectives is new.

The bounded contribution is the following combination: a transfer uplift for people without assets; loss of an existing domestic revenue stream; a closed-form no-loss limit; and an exact interval test for a single levy across adverse states. The derivations use standard quadratic surplus analysis. The searched work does not establish whether an equivalent formula exists elsewhere. The result is best read as an auditable application and synthesis, with a modest possible extension.

This study differs from S004, *A Consumption Floor After Human Labor*. S004 holds domestic output fixed and studies scarcity in an essential-goods market. This study has a traded AI input, responsive output, a foreign supply price, and a domestic-versus-global consumption comparison. It does not add a new jurisdiction to S004's model.

The search log records multiple query forms and reference following. The review is selected, not systematic. The retained primary sources are linked to short extracts and exact capture hashes. No current tax-law status is used as a premise.

## 3. Model and complete accounting

### 3.1 Production without wages

Population is one. A share `n`, with `0<n<1`, owns no assets and receives a public transfer. The other residents own local productive assets. No resident earns wages. All residents consume one final good, whose traded price is one. Utility is linear in this good. Aggregate consumption is therefore also an unweighted domestic welfare measure in this model.

Domestic firms buy `q` units of an imported AI service. They produce net final output

$$V(q)=Aq-\frac{b}{2}q^2,\qquad A>c\geq0,\quad b>0.$$

The decreasing marginal product represents a fixed local complement. It could represent land, local infrastructure, or a fixed customer base. No human labor is required. The function applies only over the analyzed range. It is not a technological forecast.

Foreign supply has inverse price `p(q)=c+dq`, with `d≥0`. This is competitive supply with increasing marginal resource cost, not an assumed monopoly pricing rule. Foreign suppliers can earn inframarginal producer surplus when `d>0`. The input need not be a literal model token. Its unit must be stable for a per-unit levy to be meaningful.

A levy creates an actual user-price wedge `t≥0`. Domestic firms are price takers. Their first-order condition is `A−bq=p+t`. Define

$$B=b+d,\quad m=A-c,\quad q_0=\frac{m}{B},\quad \lambda=\frac{b}{B}.$$

For `0≤t≤m`, equilibrium imports and domestic profit are

$$q(t)=q_0-\frac{t}{B},\qquad \pi(t)=\frac{b}{2}q(t)^2. \tag{1}$$

The user price rises by `λt`; the foreign price falls by `(1−λ)t`. Thus `λ` is the pass-through of the wedge to the domestic user. A genuinely small country with a fixed foreign price has `d=0` and `λ=1`. We do not call an economy price-taking abroad when the model gives it a terms-of-trade effect.

### 3.2 Who receives the income?

The public sector receives an inherited share `θ` of domestic profit, with `0≤θ<1`. It can represent a nondistortionary rent tax or a pre-existing equity claim. Private domestic owners receive the rest. The share is fixed across the levy comparison. Because it multiplies all profits by the same positive factor, it does not alter the firm's input choice. Acquisition costs, investment responses, and avoidance of this claim are outside the model.

Actual levy payments are `tq`. The share `e`, with `0<e≤1`, is usable public revenue. The remainder `(1−e)tq` is a **real resource cost** of collection and compliance. It is not an unpaid tax, a transfer to domestic employees, or money that remains with the supplier. Evasion that reduces the actual price wedge needs a different model. When the levy is active, the system also uses a fixed real resource cost `K≥0`. At `t=0`, this cost is zero.

For `t>0`, the transfer budget is

$$R(t)=\theta\pi(t)+etq(t)-K. \tag{2}$$

All of `R` goes to recipients. Consumption per recipient is `x(t)=R(t)/n`. Total owner consumption is `(1−θ)π(t)`. No extra government consumption is added. Their sum is

$$W(t)=\pi(t)+etq(t)-K. \tag{3}$$

This budget returns usable levy receipts to consumers once. An independent resource identity is

$$W(t)=V(q)-p(q)q-(1-e)tq-K. \tag{4}$$

Domestic output pays foreign suppliers, real collection costs, and domestic consumption. Equations (3) and (4) agree. Counting `tq` as a domestic loss and failing to add the transfer back would overstate the cost. Counting receipts without subtracting the fall in production rents would overstate the gain.

The baseline is `R₀=θbq₀²/2` and `W₀=bq₀²/2`. The floor target is an increase `D≥0` in total recipient funding. It means `x≥x₀+D/n`, not an arbitrary currency amount that is held fixed across economies with different baseline resources. The positive-target feasible set below has nonnegative transfer budgets. Algebraic configurations with a negative budget are not implementable consumption policies.

## 4. The joint funding limit

Let `L(t)=π₀−π(t)` be lost domestic profit. For a positive levy,

$$\Delta R=etq-\theta L-K,\qquad
\Delta W=etq-L-K. \tag{5}$$

Gross tax payments, usable receipts, and net transfer funding are different quantities. The levy displaces domestic public revenue by `θL`; there is no deliberate cut in `θ`. Private owners lose `(1−θ)L`. Hence

$$\Delta R-\Delta W=(1-\theta)L. \tag{6}$$

A transfer gain can exceed the aggregate gain because it also redistributes domestic income from owners. This is not necessarily undesirable. It must be named correctly.

For `u∈{θ,1}`, define

$$a_u=(e-u\lambda)q_0,\qquad
b_u=\frac{e-u\lambda/2}{B}.$$

Then `ΔR=aθt−bθt²−K` and `ΔW=a₁t−b₁t²−K`.

### Proposition 1. Maximum extra funding with no domestic loss

Assume `K=0`. If `e≤λ`, no positive levy preserves `W₀`. The maximum feasible funding increase is zero. If `e>λ`, define

$$t_W=m\frac{e-\lambda}{e-\lambda/2},\qquad
t_R=m\frac{e-\theta\lambda}{2e-\theta\lambda},\qquad
t^*=\min\{t_W,t_R\}. \tag{7}$$

The largest increase in recipient funding consistent with `ΔW≥0` is

$$D^*=a_\theta t^*-b_\theta(t^*)^2. \tag{8}$$

A nonnegative target `D` is feasible if and only if `D≤D*`.

**Proof.** Rewrite the domestic change as

$$\Delta W=(e-\lambda)tq-\frac{\lambda t^2}{2B}.$$

For `e≤λ` and `t>0`, this is negative, including at the choke point. For `e>λ`, `a₁,b₁>0`, so `ΔW≥0` exactly on `[0,tW]`. Also `aθ,bθ>0`. The funding curve is a strictly concave quadratic with its peak at `tR`. Its constrained peak is therefore at the smaller of these two values. Continuity from zero to that peak gives every target between zero and `D*`. No larger target can pass. ∎

For the revenue peak itself to pass the no-loss condition, the parameters must satisfy

$$2e^2-3e\lambda+\theta\lambda^2\geq0. \tag{9}$$

This follows by multiplying `tR≤tW` by the positive denominators. Equation (9) is a useful diagnostic, not an optimal-tax rule. A low existing public claim leaves more private domestic income available for redistribution. This can make the transfer peak occur beyond the domestic no-loss boundary.

The result gives a strong negative case. With full pass-through, `λ=1` and `e≤1`, so a positive levy always reduces total domestic consumption. It can still raise recipients' income. Its benefit then comes from domestic redistribution, not from a free foreign revenue source.

## 5. One policy under several possible states

A government rarely knows the future supply response and collection cost exactly. Let each state `i` have its own parameters, but require one common levy `t`. Each state must meet a funding uplift `Dᵢ` and satisfy `ΔWᵢ≥0`. State probabilities are not needed.

For a state with `e>λ`, a constraint of the form

$$a_ut-b_ut^2-K\geq H$$

has a feasible interval between

$$r_u^{\pm}(H)=\frac{a_u\pm\sqrt{a_u^2-4b_u(K+H)}}{2b_u}, \tag{10}$$

provided the discriminant is nonnegative. Use `u=θ,H=Dᵢ` for funding and `u=1,H=0` for domestic consumption. Intersect both intervals with `0<t≤m`. A fixed cost can create a strictly positive lower bound: a tiny levy can cost more than it provides.

### Proposition 2. Common-policy feasibility

A positive levy meets all state constraints if and only if every state has valid intervals and

$$\max_i\{r_{\theta,i}^{-}(D_i),r_{1,i}^{-}(0),0\}
\leq
\min_i\{r_{\theta,i}^{+}(D_i),r_{1,i}^{+}(0),m_i\}, \tag{11}$$

with a positive upper endpoint. A state with `e≤λ` makes a positive no-loss policy infeasible.

**Proof.** Each concave quadratic is at least its target exactly between its real roots. The common levy must belong to every such interval. A finite intersection of closed intervals is nonempty exactly when its largest lower endpoint does not exceed its smallest upper endpoint. The earlier negative-case argument covers `e≤λ`. A zero levy remains feasible when every uplift target is zero. ∎

A verified supplier-access limit `t≤\bar t` can be added to the upper bound. This describes a constraint; it does not explain a supplier's threat or estimate the chance of withdrawal. The experiment varies this limit as a sensitivity case.

There is also an international limit. Foreign producer surplus is `dq²/2`. Add it to domestic consumption and compare with the untaxed baseline:

$$\Delta W_{global}=-\frac{t^2}{2B}-(1-e)tq-K<0\quad(t>0). \tag{12}$$

This follows by subtracting total foreign resource cost `cq+dq²/2` from domestic output. Untaxed quantity maximizes the resulting concave surplus. There is no pre-existing externality here for the levy to correct. A domestic no-loss result therefore does not justify a claim of global benefit.

## 6. Executed results

All inputs are in [design.json](data/design.json). Base values are `A=14,c=4,b=1,d=0.25,θ=0.25,e=1,K=0,n=0.8`. Thus `q₀=8`, `λ=0.8`, baseline public income is `8`, and baseline recipient consumption is `10`. Units are synthetic annual units per total resident unless stated otherwise.

### 6.1 Named counterexamples

The following values come from [scenarios.csv](results/scenarios.csv). Each change uses that row's own no-levy baseline.

| Case | Levy | Usable levy receipts | Lost domestic public income | Net funding gain | Domestic consumption change |
| --- | ---: | ---: | ---: | ---: | ---: |
| Base, moderate levy | 2 | 12.800 | 2.880 | 9.920 | 1.280 |
| Base, high levy | 4 | 19.200 | 5.120 | 14.080 | −1.280 |
| Full pass-through | 2 | 16.000 | 4.500 | 11.500 | −2.000 |
| Collection share `e=0.75` | 2 | 9.600 | 2.880 | 6.720 | −1.920 |
| Public share `θ=0.8` | 2 | 12.800 | 9.216 | 3.584 | 1.280 |
| Fixed cost `K=0.5` | 2 | 12.800 | 2.880 | 9.420 | 0.780 |
| Lower productivity `A=10` | 2 | 6.400 | 1.600 | 4.800 | 0.000 |
| Flatter foreign supply `d=0.1` | 2 | 14.545 | 3.719 | 10.826 | −0.331 |

At `t=2`, base recipient consumption rises from `10` to `22.4`; total domestic consumption rises by `1.28`. Yet global surplus falls by `1.6`. At `t=4`, recipient consumption reaches `27.6` while total domestic consumption falls by `1.28`. The group and aggregate objectives disagree.

For the base economy, `tW=3.3333` and `tR=4.4444`. The largest no-loss funding uplift is `13.3333`, which supports recipient consumption of `26.6667`. The unconstrained funding peak is `14.2222`. Maximizing funds would exceed the no-loss bound. These are quantities in the model, not percentages for an actual tax instrument.

A higher public share reduces the **additional** funding gain because more baseline domestic income is already public. It does not reduce the level of recipient income in this comparison. At `θ=0.8`, baseline recipient consumption is `32`; with `t=2`, it is `36.48`. This prevents the false inference that a smaller measured uplift makes public ownership worse.

### 6.2 Full stress grid

The grid has 216 states: three productivity values, four foreign supply slopes, three public shares, three collection shares, and two fixed costs. Six levy values give 1,296 rows. There are 1,080 positive-levy rows. All are retained in [grid.csv](results/grid.csv).

Among positive levies, 168 have positive levy payments but negative net funding. Another diagnostic finds 597 with positive net funding and negative domestic consumption change. There are 312 with positive net funding and nonnegative domestic consumption change. The second and third counts do not include zero net changes. These are counts over chosen states, not estimated probabilities. The grid is not a representative sample of countries.

Continuous optimization gives positive no-loss funding in 93 of the 216 states. This count is separate from the six tested levy levels. The largest resource-accounting residual is `2.85×10⁻¹⁴` in absolute value, within floating-point error.

### 6.3 Common-policy limits

| Required state set | Maximum common uplift | Levy that achieves it |
| --- | ---: | ---: |
| Base only | 13.3333 | 3.3333 |
| Base and flatter foreign supply | 8.6667 | 1.6667 |
| Base and lower productivity | 4.8000 | 2.0000 |
| Base and full pass-through | 0 | 0 |
| Base and collection share `0.75` | 0 | 0 |
| Base and fixed cost `0.5` | 12.1871 | 2.9843 |

The common uplift is the minimum gain across included states. It does not mean the final income level is equal in each state. The code uses the interval test and bisection on the funding target. It does not replace the analytical feasible set with a coarse tax grid.

A supplier-access cap also matters. With base parameters, caps of `1`, `2`, and `3` limit no-loss funding to `5.68`, `9.92`, and `12.72`. The uncapped limit is `13.3333`. No claim is made that these caps describe actual supplier conduct.

Eight tests check direct production accounting, transfer cancellation, the quadratic formulas, full pass-through, collection failure, root endpoints, common-policy failure, global loss, invalid inputs, and access caps. A dense direct search with 20,001 tax values in each of six cases checks the computed optima. The tests and analysis use only the Python standard library. They verify the implementation and selected implications, not the realism of the model.

## 7. Policy use and limits

The first practical rule is to publish three budget measures: actual levy payments, usable receipts, and net funding after displaced revenue. A transfer promise based on the first measure can fail even before it reaches questions about delivery. In this model, the displacement is automatic: a more costly AI input reduces local rents and the public share of those rents.

The second rule is to specify the protected group and the aggregate constraint separately. An asset-poor consumption floor can improve while owners and the country lose resources. That can be a defensible distributional choice. It cannot be described as a costless claim on foreign wealth. Conversely, a policy that preserves total consumption is not a Pareto improvement. Domestic owners lose consumption for every positive levy here.

The third rule is to test a fixed policy against unfavorable joint states. If an importer cannot establish that its action reduces the foreign price, it should include full pass-through. Under the paper's no-loss criterion, that one state removes the positive-levy option. The response can be a smaller promise, a different domestic funding base, or a negotiated external transfer. Relabeling domestic revenue as an international grant does not add resources.

International revenue sharing is a separate governance choice. A true external transfer could raise both recipient income and domestic resources without taxing this input at the border. Its donor cost, legal authority, distribution rule, enforcement, and investment effects still need analysis. This paper supplies no proof that such a transfer will be offered or that countries can sustain cooperation. Equation (12) explains why the present unilateral mechanism is insufficient as a global welfare strategy.

Several limits are material. Supply is competitive and linear; monopoly pricing, quality changes, bundled services, and prices that rise by more than the tax are excluded. The model is static and omits AI innovation, capital accumulation, retaliation, and exchange rates. It has one final good, so cash does not face a separate housing or essential-supply limit. Fixed local assets earn rents, but their ownership does not change. Public claims are inherited and nondistortionary. Collection losses are real resources by assumption. None of these quantities has been estimated for a post-labor economy.

The policy lesson is therefore a test to perform, not a tax to adopt. A credible post-labor floor needs both a claim on income and a record of which other claims it displaces. In an AI-importing economy, the same record must show which country bears the cost. The joint test makes those conditions explicit and exposes cases where a visible new revenue stream does not meet them.

Review records: [critical review](reviews/critical-review.md), [author response](reviews/author-response.md), and [completion gates](completion-gates.md).

## References

- **[A1]** Wossnig, L. (2026). [Simulating a Post-Automation Economy](https://arxiv.org/html/2606.20649v1). arXiv:2606.20649v1. Read Sections 6.6, 6.15, 6.17, 10, and Appendix A.
- **[A2]** Becker, J. (2026). [When are digital services taxes optimal? Output taxes and profit shifting](https://doi.org/10.1007/s10797-026-09987-z). *International Tax and Public Finance*. Read Sections 2, 3, 5, and 6; selected appendix discussion.
- **[A3]** Korinek, A., and Lockwood, L. M. (2026). [Public Finance in the Age of AI: A Primer](https://www.brookings.edu/wp-content/uploads/2026/01/Korinek-Lockwood-FINAL-for-website.pdf). Brookings working-paper release, January 2026; manuscript dated 30 December 2025. Read Sections 2.4 and 4.2.
- **[A5]** Richter, W. F. (2021). [The Taxation of Digital Services as a Rent-Extracting Policy](https://www.mohrsiebeck.com/en/article/the-taxation-of-digital-services-as-a-rent-extracting-policy-101628fa-2021-0012/). *FinanzArchiv* 77(3), 225–246. Publisher abstract only.
- **[A6]** Pujolas, P., and Rossbach, J. (2026). [Fiscal Limits to Protectionism: The 2025 U.S. Tariff Laffer Curve](https://arxiv.org/html/2602.18938v1). arXiv:2602.18938v1. Read model overview, Section 4.2, and Appendix A.
