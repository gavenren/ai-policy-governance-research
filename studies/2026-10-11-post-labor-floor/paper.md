# A Consumption Floor After Human Labor
## Public Revenue, Scarce Goods, and the Timing of Investment

> **State:** Complete-study draft — executed analysis and independent AI review complete.
> **Study ID:** `2026-10-11-post-labor-floor` (S004). **Date:** 11 October 2026.
> **Evidence cutoff:** 2026-10-11T20:43:27Z. This is the end of source collection for this draft, not a claim of full coverage.
> **Method:** Analytical model and deterministic synthetic experiments. No country forecast or observed displacement estimate.
> **AI assistance:** Codex conducted research, wrote the model and text, and ran the checks. A separate AI agent searched prior work. No human review has been completed. No author affiliation or external endorsement is claimed.
> **Rights:** No repository reuse licence has been selected. Source rights are separate.

## Abstract

If AI can replace human labor in all fields, wages may no longer provide a reliable income base. Public policy must then distribute claims on output and maintain access to essential goods. This paper asks when a cash transfer can meet both needs. A two-good model includes public ownership, imperfect tax collection, fixed essential supply, and payments that return to asset owners. It gives an explicit test for a minimum consumption level. The test links the required public revenue share to both goods. It also gives a condition under which investment in essential supply improves access despite its immediate cost. Nine named scenarios, 576 policy-state cases, and 36 investment cases test the results. In the base case, the transfer funds the reproducible-goods floor but misses the essential-goods floor. Public equity and taxes give the same allocation when their effective revenue share is equal. No tested policy passes all 36 stress states. A construction delay can worsen both consumption measures. These are model results, not forecasts. The contribution is a small, auditable extension of existing fiscal and scarcity models. It supports a policy sequence: secure income rights, measure real access, and finance supply investment without withdrawing current support.

**Keywords:** AI governance; technological unemployment; public finance; social wealth fund; basic income; scarce goods.

## 1. Question and scope

The question is conditional: how should an economy operate if humans cannot obtain adequate pay through competitive work? The paper does not predict that outcome or assign it a date. AI superiority at tasks does not alone establish zero labor demand. Deployment costs, relative prices, preferences for human services, and legal duties can preserve paid work. Current occupational exposure is also different from actual job loss. The ILO's 2025 index studies exposure and expects substantial job change, rather than complete replacement [S6].

The stress scenario is stronger. No member of the modeled population receives labor income. A share owns no productive assets. That group must receive a transfer to consume. People can still study, care for others, create art, take part in public decisions, and choose work. Their right to material support does not depend on winning a productivity contest with a machine.

The policy objective is explicit. Each person in the asset-poor group must be able to consume at least `h` units of an essential service and `b` units of a reproducible good. These floors are public choices. The model does not derive them from a welfare optimum. Essential services can represent a local housing or energy constraint. A single aggregate cannot represent every need, location, or disability.

Three questions guide the analysis:

1. What public revenue share makes both floors possible under a cash policy?
2. When does spending on essential supply improve access more than keeping the same funds in transfers?
3. What fails when revenue, supply, or collection is worse than expected?

The unit of analysis is a synthetic policy-state combination. The target of inference is the stated model. No result estimates a national tax rate, investment return, or probability of economic collapse.

## 2. Prior research and bounded contribution

Income without paid work is an established research topic. Korinek and Juelfs examine declining work and the distribution of capital income [S7]. Brollo and co-authors discuss fiscal responses to AI disruption [S5]. Growiec, Prettner, and Szkróbka compare several transfer and tax instruments in a recent theoretical preprint [S8]. These works establish the policy context. This study does not claim to invent basic income or broad capital ownership.

Three sources are especially close:

| Source and inspected material | Existing contribution | Added element in this study |
| --- | --- | --- |
| Nayebi [S2], version 4, Sections 2–6 | A public-capture threshold connects automation gains to broad transfers. | A separate essential-goods floor, with price and asset-income feedback. |
| Song [S1], Sections 3–6 and appendices | A closed model links automated output, scarce assets, expenditure, and access. It compares allocation systems. | A two-group cash-floor threshold linked to a tax-and-equity budget, plus a budget-costed supply test. |
| Korinek and Lockwood [S3], Sections 2.4 and 4 | Public finance analysis includes fixed-factor rents, public equity, and policy stages. | An executable floor test with explicit collection losses and a short-run investment tradeoff. |

Wossnig's simulation distinguishes countries that own automation rents from countries that pay foreign owners [S4]. That result limits this paper's domestic model. A country cannot distribute a foreign revenue stream merely because its residents use AI.

The bounded contribution is the combination of an explicit minimum-capture formula, a marginal supply-investment condition, and a reproducible failure test. Each part uses standard economic methods. The search did not establish that no earlier paper contains an equivalent formula. In particular, the general claim that cheap automated goods do not remove scarcity is already present in [S1]. A threshold for publicly funded transfers is already present in [S2].

The search covered primary research and official publications through the cutoff. Eight sources were retained. The three closest works were read beyond their abstracts. Some background sources were read only at the abstract or official summary level. The source ledger records that limit. Search terms and excluded leads are in [the search log](logs/search.md). This is a selected review, not a systematic review. The existing repository study concerns incident-record exports. The separate AI-safety repository concerns incidents and evaluation methods. This paper has a different question and method.

## 3. A two-good economy with no labor income

### 3.1 Goods, people, and units

Normalize total population to one. A share `n`, with `0 < n < 1`, has no labor or asset income. Call this the recipient group. The remaining share owns the private assets. Members within each group are identical.

The economy has two annual outputs:

- `Π > 0`: units of a reproducible good, after operating costs and replacement of worn capital. Its price is one. Ownership claims distribute this output.
- `Q > 0`: units of an essential service. Its price `p` adjusts to clear its market. Private owners hold all rights to this service in the base model.

`Π` is an output endowment, not total GDP, firm sales, or a forecast of pure monopoly profit. The model holds both outputs fixed within a period. It omits investment incentives in the automated sector. Thus, a change in taxation does not reduce `Π` inside this model. Any such response must enter as a different scenario.

Recipient preferences are Cobb–Douglas, with essential expenditure share `α`, where `0 < α < 1`. A recipient with transfer `d` consumes:

$$x = \frac{\alpha d}{p}, \qquad z=(1-\alpha)d. \tag{1}$$

Owners have essential expenditure share `β`, where `0 < β < 1`. These shares describe preferences, not minimum needs. A household may meet one floor and miss the other. That is why both floors must be checked.

All money values are annual units of the reproducible good per total resident, unless stated otherwise. `d`, `x`, and `z` are per recipient. `n d` is the total transfer per total resident.

### 3.2 Public claims and the budget

The public sector owns share `s` of claims on `Π`. It taxes the private share at rate `τ`. Collection efficiency is `e`. All three lie between zero and one. The effective public share is:

$$\phi=s+(1-s)e\tau. \tag{2}$$

This formula avoids counting tax receipts on the public share a second time. Uncollected tax remains private income. The model imposes no separate tax on essential rents.

Public spending on other uses is `G ≥ 0`, measured in the reproducible good. Spendable transfer revenue is:

$$R=\phi\Pi-G, \qquad nd=R. \tag{3}$$

Equation (3) distributes all remaining revenue. For positive floors, `R` must be positive. A policy with `R ≤ 0` fails the test. The base model has no deficit finance. Public ownership is inherited at the start of the period. Its acquisition is not free in a real transition; Section 6 tests an added debt-service cost.

### 3.3 Essential rents return to owners

Owners receive private reproducible income `(1−φ)Π` and essential rents `pQ`. Their total essential expenditure is:

$$\beta[(1-\phi)\Pi+pQ]. \tag{4}$$

Market clearing requires:

$$pQ=\alpha R+\beta[(1-\phi)\Pi+pQ].$$

Therefore:

$$p=\frac{\alpha R+B}{(1-\beta)Q}, \qquad B=\beta(1-\phi)\Pi. \tag{5}$$

The term `pQ` in owners' income matters. Dropping it would overstate recipients' access. With `R>0`, recipients receive:

$$x=\frac{\alpha(1-\beta)QR}{n(\alpha R+B)}, \qquad z=\frac{(1-\alpha)R}{n}. \tag{6}$$

The model closes both goods markets. Essential consumption sums to `Q`. Reproducible consumption plus `G` sums to `Π`. To verify the second identity, use `(1−β)pQ=αR+B`. Owners' reproducible spending then equals `(1−φ)Π+αR`. Add recipient spending `(1−α)R` and public spending `G` to obtain `Π`.

This is a static endowment equilibrium. It is not a growth model. It does not explain how firms create the output or how asset prices form.

## 4. The joint floor test

### Proposition 1. Minimum public capture

Let `h>0` and `b>0`. Define:

$$\Delta=(1-\beta)Q-nh.$$

For `Δ>0` and `Π>G`, the recipient group meets both floors if and only if:

$$\phi\geq\phi_{\rm req}=\max\left\{
\frac{G+nb/(1-\alpha)}{\Pi},
\frac{\alpha\Delta G+nh\beta\Pi}{\Pi(\alpha\Delta+nh\beta)}
\right\}. \tag{7}$$

The first term is the reproducible-goods condition. The second is the essential-access condition. If the required value exceeds one, the selected floor is infeasible under the model's cash policy.

**Proof.** From (6), `z≥b` is equivalent to `φΠ−G≥nb/(1−α)`. For the essential floor, multiply `x≥h` by the positive denominator in (6). Rearrangement gives `αΔ(φΠ−G)≥nhβ(1−φ)Π`. Move terms in `φ` to the left and divide by the positive coefficient. This yields the second term in (7). Each step is reversible. The first inequality also ensures `R>0`. ∎

If `Δ<0`, no cash policy in this model meets `h`, even with full public ownership of `Π`. If `Δ=0`, the essential floor can be met only at `φ=1`, with positive `R`. The reproducible floor must still pass. These edge cases are implemented and tested.

The strong capacity condition is specific to private essential-asset ownership and owner demand. It is not a physical impossibility theorem. A different allocation system could assign essential goods directly. Any such system still needs at least `nh` physical units for recipients. The present cash policy needs more because owners continue to consume essential services from their rental income.

The result also distinguishes technical capacity from a public guarantee. A guarantee requires correct eligibility records, accessible payment systems, actual service delivery, and an appeal process. None is supplied by an equation.

### Corollary 1. Instrument equivalence is conditional

For fixed `Π,Q,G,n,α,β`, any two pairs `(s,τ)` that give the same `φ` produce the same allocation. This follows directly from (3)–(6). Public equity has no additional one-period benefit inside this model once effective capture is equal.

The equivalence does not include acquisition costs, voting rights, tax avoidance responses, risk, or future investment. It therefore cannot establish that a social wealth fund and a tax law are interchangeable institutions. Both can also lose revenue when the same underlying output falls.

## 5. When does supply investment help?

Let public spending include an annual investment cost `I`, so that `G=G₀+I`. Assume completed investment adds `ηI` units of annual essential capacity:

$$Q(I)=Q_0+\eta I, \quad R(I)=\phi\Pi-G_0-I.$$

This is a comparison of annual policy configurations. It is not a present-value appraisal of a durable asset. It holds the distribution of essential-asset rights fixed. It can represent a publicly funded supply subsidy whose output remains privately owned. A public housing system would require a different ownership equation.

For `R>0`, fixed `φ` and `Π`, and `B>0`, differentiate (6):

$$\frac{d\log x}{dI}=\frac{\eta}{Q(I)}-
\frac{B}{R(I)[\alpha R(I)+B]}. \tag{8}$$

### Proposition 2. A local capacity-investment condition

Completed investment increases recipient essential consumption at the margin if and only if:

$$\frac{\eta}{Q(I)}>\frac{B}{R(I)[\alpha R(I)+B]}. \tag{9}$$

**Proof.** Write `log x` as a constant plus `log Q + log R − log(αR+B)`. Use `Q′=η` and `R′=−1`. The last two derivatives sum to `−B/[R(αR+B)]`. The sign gives (9). ∎

This is a local access test, not a welfare ranking. Reproducible consumption always falls by `(1−α)/n` per extra unit of `I`. A project can pass (9) and still make the joint floor fail. At `B=0`, essential access is independent of transfer size while `R>0`; investment still reduces reproducible consumption.

If construction takes time, current `Q` does not rise when the first payment occurs. The positive term in (8) then disappears for that period. Both consumption measures fall when `B>0`. A reserve or separate transition budget can bridge the gap, but it must be funded and stress-tested. The model does not create that reserve by assumption.

## 6. Executed experiments

The experiment uses synthetic annual units. None is a country calibration. Base values are `n=0.8`, `α=0.4`, `β=0.3`, `Π=100`, `Q=1.4`, `G=8`, `s=0.2`, `τ=0.3`, and `e=0.8`. Floors are `h=0.6` and `b=20` per recipient. The parameter file is [design.json](data/design.json).

### 6.1 Named scenarios

| Scenario | Effective capture | Essential units | Reproducible units | Both floors met? |
| --- | ---: | ---: | ---: | :---: |
| Base | 0.392 | 0.498 | 23.400 | No |
| Taxes only, same capture | 0.392 | 0.498 | 23.400 | No |
| Low supply: `Q=0.8` | 0.392 | 0.284 | 23.400 | No |
| Low supply, public share `s=0.5` | 0.620 | 0.458 | 40.500 | No |
| Supply expansion: `Q=1.8` | 0.392 | 0.640 | 23.400 | Yes |
| Low output: `Π=80` | 0.392 | 0.478 | 17.520 | No |
| Weak collection: `e=0.6` | 0.344 | 0.428 | 19.800 | No |
| Public share `s=0.35` | 0.506 | 0.655 | 31.950 | Yes |
| Same public share, extra cost of 15 | 0.506 | 0.523 | 20.700 | No |

The base case needs capture of about `0.4651` to meet both floors. The reproducible-goods condition alone needs only `0.3467`. A budget check can therefore pass while access fails. The taxes-only case uses `τ=0.49` with `e=0.8`. It confirms Corollary 1.

The supply-expansion row holds public spending fixed. It is an exogenous capacity comparison, not evidence that supply is free. Section 6.3 includes investment costs. The last row adds 15 units to `G` as a hypothetical debt-service burden. It is not an estimated acquisition price. It shows how a public-ownership gain can disappear after financing costs.

### 6.2 Joint stress states

The grid combines three output levels `{80,100,120}`, four supply levels `{0.8,1.1,1.4,1.8}`, and three collection levels `{0.6,0.8,1.0}`. Each of 16 policies faces 36 states, giving 576 cases. Policy shares are `s∈{0,0.2,0.35,0.5}` and rates are `τ∈{0.2,0.3,0.4,0.5}`. All cases are retained in [stress.csv](results/stress.csv).

The base policy passes 5 of 36 states. The policy `s=0.35,τ=0.3` passes 17. The strongest pass count is 27, reached by two policies. No tested policy passes all states. The 36 states have no assigned probabilities. A pass count is grid coverage, not a success probability.

For `s=0.5,τ=0.4`, every tested failure occurs at `Q=0.8`. Conditional on `Q≥1.1`, that policy passes all 27 remaining grid states. At the worst output and collection values, it requires `Q≥1.06154`. Its floor at `Q=1.1` is approximately `x=0.62174` and `z=31.2`. This is a conditional operating boundary. It does not justify choosing a national public-ownership share of 50 percent.

The grid allows low output and weak collection at the same time. It therefore does not assume independent revenue protection from taxes and equity. It does not estimate a joint distribution or test states outside the listed ranges. A wider range can reverse a passing assessment.

### 6.3 Investment and delay

The experiment tests `I∈{0,2,4,6,8,10}` and `η∈{0.01,0.04,0.08}`, with both completed and delayed capacity. This gives 36 rows. At the base point, the local threshold is `η>0.02664`.

At `η=0.01,I=4`, completed investment lowers essential access from about `0.498` to `0.471`. At `η=0.04,I=4`, it increases access to `0.510`, while reproducible consumption falls to `20.4`. At `η=0.08,I=8`, essential consumption reaches `0.602`, but reproducible consumption falls to `17.4`. Thus, even a project that meets the essential floor can fail the joint test.

No investment row meets both floors under the base capture policy. This negative result is retained. Investment alone is not a substitute for adequate public revenue. During the modeled delay, every positive investment cost lowers both consumption measures. These comparisons do not include later benefits, depreciation, borrowing, or discounting. They identify a transition funding problem; they do not estimate an optimal investment schedule.

## 7. Strategies for governing the transition

The following recommendations are institutional proposals. Equations (7)–(9) inform their design but do not prove their political feasibility or legal authority.

### 7.1 Establish an income right that does not require employment

Create a basic transfer with clear eligibility, regular payment, and an appeal route. Use a broad resident base and address children, disability costs, and people without standard identity documents. A universal payment with tax recovery from high-income owners is one option. The model uses a net transfer to the asset-poor group. It does not price the gross cost or administration of a universal scheme.

Keep retraining, wage insurance, and shorter hours available during partial displacement. Do not make repeated retraining a condition for basic support when suitable jobs are absent. Preserve the option to work, but separate that option from the right to eat and remain housed. Measures of household income and material deprivation should determine support needs. AI benchmark scores cannot establish those needs.

### 7.2 Build public revenue claims before wage revenue falls

Use a portfolio of tax administration, broad asset ownership, and enforceable claims on public investment returns. Public procurement, research finance, infrastructure subsidies, or resource rights can include negotiated public return terms. Record their costs. Do not count a state asset's tax payment and dividend as two independent claims on the same output.

A social wealth fund needs transparent accounts, independent custody, rules for withdrawals, and public oversight. Benefits must not depend on loyalty to a party or company. Broad ownership should not require that recipients sell their permanent claim to meet an immediate need. An investment fund is not a cash reserve: asset values and dividends can fall together.

Do not preserve monopoly merely to produce a tax base. Competition can reduce some rents and improve access. Revenue planning must distinguish rents, normal returns, and total sales. This paper holds `Π` fixed, so it cannot choose a welfare-maximizing tax base. Detailed public-finance work is required [S3].

### 7.3 Treat essential access as a separate policy target

Track service quantity, quality, waiting time, location, and unmet need. A cash total or a general price index is insufficient. Expand housing, electricity delivery, transport, care capacity, and other binding services where evidence supports the need. Choose the relevant local unit before aggregating.

Use the investment condition as a screening test. Then check both floors, construction delays, costs, and distribution of asset rights. Public provision, rent taxation, or rights to a defined service can change the allocation. They require their own accounting and can perform differently from this paper's private-asset cash system. Direct provision should preserve choice and an appeal route. It must not become a system that removes support to compel behavior.

### 7.4 Separate three policy triggers

| Trigger | Evidence needed | Proposed response |
| --- | --- | --- |
| Household income loss | Income after tax, earnings, vacancies, hours, and hardship; use several measures. | Increase immediate support and remove unsuitable job-search conditions. |
| Public funding gap | Collected revenue, spendable dividends, required transfer, and reserve balance. | Change funding, draw an authorized reserve, or seek legislative action. |
| Essential access gap | Local service quantity, waiting time, prices, and unmet need. | Expand supply or change access rules; retain support during construction. |

Do not require proof that AI caused each income loss before providing emergency help. A recession, trade shock, and AI displacement can overlap. Diagnosis remains useful for long-term policy, but it should not delay a basic response.

A proposed control rule is to escalate routine measures after a breach in two consecutive quarterly releases. Reduce temporary measures only after four releases above a separate exit margin. Allow immediate action for severe deprivation. These numbers are design examples, not optimized or tested thresholds. Their purpose is to prevent one noisy release from causing repeated policy changes. Publish the chosen rule and each exception.

### 7.5 Preserve human control and address international limits

Elected institutions must choose the floor, tax burden, and distribution of rights. AI can support forecasts and payment checks. It must not be the sole authority for eligibility, budget choices, or appeals. People need a practical route to contest a decision and receive service during a review when basic needs are at risk.

Countries with weak tax capacity or foreign-owned AI suppliers face a different budget. Cooperation on tax collection, access to infrastructure, and transfers can be necessary. A domestic fund cannot collect income it does not own. This paper's `e` parameter represents collection loss, not foreign ownership, currency risk, or an international settlement system. Those issues require a separate open-economy model [S4].

The framework assumes that AI remains subject to effective human governance. It cannot solve loss of control over powerful AI systems. Safety duties must not be relaxed to increase modeled fiscal returns.

## 8. Limits and tests that could reject the design

The results depend on fixed output, competitive allocation of essential services, two representative groups, and constant expenditure shares. Households differ within each group. A passing group average can conceal exclusion. There are no saving choices, asset-price shocks, trade flows, demographic changes, monetary dynamics, or endogenous political decisions. High output does not itself prove adequate demand or financial stability outside this static model.

The study does not assume that broad automation has occurred. It also does not show that transfer systems are sufficient for social purpose, political power, or a meaningful life. Human participation in civic, cultural, and personal activity needs separate institutional support.

The next empirical study should estimate local essential demand, usable supply, and actual revenue collection. It should report subgroup outcomes and the cost of service expansion. The proposed model should be rejected or extended if expenditure shares change sharply, shortages arise from queues rather than prices, suppliers have important market power, or transfer payments do not reach intended recipients. If the taxed output falls with capture, replace fixed `Π` with an estimated response. If investment changes essential ownership, change equation (4).

No numerical rate in this paper is a recommendation for a real jurisdiction. No empirical causal claim follows from a synthetic grid. The novelty claim is limited by the selected search and close prior work.

## 9. Reproduction and disclosure

Run these commands from the repository root with Python 3.9 or later:

```sh
python3 studies/2026-10-11-post-labor-floor/code/model.py
python3 -m unittest discover -s studies/2026-10-11-post-labor-floor/code -p 'test_*.py' -v
```

The analysis uses only the Python standard library. It needs no network, API key, or random seed. All inputs are synthetic and retained. Generated CSV files contain the complete cases, including failures. [run.json](results/run.json) records runtime information and input, code, and output hashes. The tests check both market identities, the threshold against direct market solutions, exact boundary cases, conditional instrument equivalence, and the investment derivative.

The study is exploratory. The numerical grid was selected during model development. It was not preregistered. [protocol.md](protocol.md) records the decisions and changes. Public source records retain short attributed extracts and hashes. Full downloaded source files remain local because redistribution rights were not established for the full collection. Source extraction is separate from model reproduction.

AI assistance covered the literature search, model, code, tests, manuscript, and review. No human review, journal submission, funding declaration, or institutional affiliation is implied. Funding and human conflicts of interest were not supplied. The [independent AI review](reviews/critical-review.md) reproduced the outputs and found no blocking error. The [author response](reviews/author-response.md) records each issue. Independent AI review has narrower evidential value than external peer review.

## 10. Conclusion

When wages cease to support households, economic governance must assign claims on output and maintain access to real services. Within this model, public revenue is necessary but can be insufficient. Essential rents return to owners and limit what recipients can buy. A joint floor test makes that limit explicit. Supply investment can help, but its cost and delivery time can also reduce current consumption. Policy should therefore combine income rights, accountable public revenue claims, local access measures, and financed transition support. The test is an auditable starting point for that work, not proof that any economy can pass it.

## References

- **[S1]** Song Zichen. 2026. *Abundance Is an Expenditure Condition: AI Automation, Scarcity Rents, and Access*. arXiv:2609.13801v1, 12 September. [Full text](https://arxiv.org/html/2609.13801v1).
- **[S2]** Aran Nayebi. 2026. *When Do AI Gains Become Broadly Shareable? A Policy Threshold for AI-Driven Automation*. arXiv:2505.18687v4, 29 July. First submitted in 2025 under an earlier title. [Full text](https://arxiv.org/html/2505.18687v4).
- **[S3]** Anton Korinek and Lee M. Lockwood. 2026. *Public Finance in the Age of AI: A Primer*. January Brookings version, Sections 2.4 and 4. Also NBER Working Paper 34873, February. [Inspected PDF](https://www.brookings.edu/wp-content/uploads/2026/01/Korinek-Lockwood-FINAL-for-website.pdf).
- **[S4]** Leonard Wossnig. 2026. *Simulating a Post-Automation Economy*. arXiv:2606.20649v1, 7 June. [Full text](https://arxiv.org/html/2606.20649v1).
- **[S5]** Fernanda Brollo, Era Dabla-Norris, Ruud de Mooij, Daniel Garcia-Macia, Tibor Hanappi, Li Liu, and Anh D. M. Nguyen. 2024. *Broadening the Gains from Generative AI: The Role of Fiscal Policies*. IMF Staff Discussion Note 2024/002, 17 June. [Official summary](https://www.imf.org/en/Publications/Staff-Discussion-Notes/Issues/2024/06/11/Broadening-the-Gains-from-Generative-AI-The-Role-of-Fiscal-Policies-549639).
- **[S6]** Pawel Gmyrek, Janine Berg, Karol Kamiński, Filip Konopczyński, Agnieszka Ładna, Balint Nafradi, Konrad Rosłaniec, and Marek Troszyński. 2025. *Generative AI and Jobs: A Refined Global Index of Occupational Exposure*. ILO Working Paper 140, 20 May. [Official publication summary](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure).
- **[S7]** Anton Korinek and Megan Juelfs. 2022. *Preparing for the (Non-Existent?) Future of Work*. NBER Working Paper 30172, June. [Primary abstract](https://www.nber.org/papers/w30172).
- **[S8]** Jakub Growiec, Klaus Prettner, and Maciej Szkróbka. 2026. *Redistributive Policies for the Times of Transformative AI*. arXiv:2609.14750v1, 13 September. [Primary abstract](https://arxiv.org/abs/2609.14750v1).
