# A Consumption Floor After Human Labor
## Public Revenue, Scarce Goods, and the Timing of Investment

> **State:** Complete-study draft. **Study:** S004. **Date:** 11 October 2026.
> **Evidence cutoff:** 2026-10-11T20:43:27Z, the end of source collection for this draft. The literature review is selective.

## Abstract

An economy in which AI replaces labor income would need a new way to distribute purchasing power. Yet a transfer that is large enough to buy manufactured goods may still be too small to secure housing or other scarce services. This paper studies that problem in a two-good economy with public ownership, imperfect tax collection, and privately owned essential assets. It derives the public revenue share needed to support a minimum consumption level for people without assets. The essential-goods condition is more demanding than a simple transfer-budget calculation because rental payments return to owners and sustain their demand. The paper also derives a condition under which investment in essential supply improves access despite reducing current transfers. In the main numerical example, recipients can afford the reproducible-goods floor but miss the essential-goods floor. Across 576 synthetic policy-state cases, no tested policy meets both floors in every state. The investment cases show why higher capacity alone may be insufficient: construction costs reduce current income, and delays postpone the additional supply. These results support a policy approach that joins income rights to measures of real access and explicit transition finance. They are conditional model results, not forecasts of labor displacement or estimates of a country's required tax rate.

**Keywords:** AI governance; technological unemployment; public finance; social wealth fund; basic income; scarce goods.

## 1. Introduction

Suppose that AI makes it possible to produce most goods with little human labor. A household that owns none of the productive assets may still have no reliable income. A public transfer can address that problem, but the transfer's purchasing power depends on what the household needs to buy. Software and manufactured goods may become cheaper while housing, local infrastructure, and other constrained services remain scarce. The policy question is therefore about both income and access.

A simple example shows the distinction. In the model's base case, a transfer lets each recipient buy 23.4 units of reproducible goods, more than the assumed floor of 20. The same recipient can buy only 0.498 units of an essential service, below the floor of 0.6. The public budget is sufficient by the first measure and insufficient by the second. Raising the share of output available to the public can close the gap, but so can additional essential capacity. These responses have different costs and timing.

This paper asks how much public revenue is needed to meet both consumption floors, and when investment in essential supply improves the outcome. The analysis combines a public tax-and-equity budget with a market in which essential rents return to private owners. It derives a minimum revenue share, compares policies across adverse states, and tests the tradeoff between current support and new capacity.

The setting is deliberately conditional. No member of the modeled population earns labor income. A share also owns no productive assets and must receive transfers to consume. This is a stronger premise than current evidence of occupational exposure. The ILO's 2025 index studies exposure and expects substantial job change rather than complete replacement [S6]. Task performance alone does not establish that demand for human work will disappear: deployment costs, relative prices, preferences for human services, and legal duties can preserve it. The paper assigns no probability or date to the post-labor case.

The consumption floors are public choices, not quantities derived from a welfare optimum. Each recipient must be able to obtain at least $h$ units of the essential service and $b$ units of the reproducible good. A single essential-service aggregate cannot represent every location, disability, or household need. The framework instead identifies a basic problem that a more detailed policy must address: public revenue and physical supply have to support the same promise.

## 2. Related literature and contribution

The distribution of income after a decline in paid work is already a substantial research topic. Korinek and Juelfs examine capital income and the future of work [S7]. Brollo and co-authors consider fiscal responses to AI disruption [S5], while Growiec, Prettner, and Szkróbka compare transfer and tax instruments in a theoretical preprint [S8]. Basic income and broad capital ownership are established proposals in this literature.

Three works are particularly close to the present analysis. Nayebi derives a public-capture threshold that connects automation gains to broad transfers [S2, Sections 2–6]. Song studies automated output, scarce assets, expenditure, and access in a closed model, and compares allocation systems [S1, Sections 3–6 and appendices]. Korinek and Lockwood place fixed-factor rents and public equity within a wider account of AI public finance [S3, Sections 2.4 and 4]. The claim that automated abundance can coexist with scarcity is thus not new, nor is the use of a public revenue threshold to assess broad transfers.

The present paper brings these elements together in a two-group cash-transfer model. Its contribution is an explicit joint threshold for two consumption floors, a budget-costed test of supply investment, and a reproducible set of cases in which the proposed policies fail. The essential-asset market includes the return of rents to owners, so the access threshold reflects both their private production income and their rental income. The investment test then asks whether the added supply offsets the transfer income used to finance it. These are limited extensions using standard economic methods; the selected search does not establish mathematical priority.

Foreign ownership creates a further constraint. Wossnig distinguishes countries that own automation rents from those that pay foreign suppliers [S4]. The domestic model below does not resolve that problem. Residents' use of AI does not itself give their government a claim on its foreign revenue.

The review retained eight sources through the stated cutoff. The three closest works were read beyond their abstracts; some background sources were available only at the abstract or official-summary level. The evidence ledger records those limits, and the [search log](logs/search.md) records search terms and excluded leads. This is a selected review, not a systematic one. The earlier repository paper concerns incident-record exports, while the separate AI-safety programme concerns incidents and evaluation methods; those studies address different questions.

## 3. The economy

### 3.1 Production and household income

The population consists of two groups. Recipients have neither wages nor assets; their consumption depends on public transfers. Owners receive the private income from production and essential services. Total population is normalized to one, and recipients make up a share $n$, with $0 < n < 1$. Members within each group are identical.

The distinction between reproducible output and scarce services is central. The economy supplies two annual outputs:

- $\Pi  > 0$: units of a reproducible good, after operating costs and replacement of worn capital. Its price is one. Ownership claims distribute this output.
- $Q > 0$: units of an essential service. Its price $p$ adjusts to clear its market. Private owners hold all rights to this service in the base model.

$\Pi$ is an output endowment, not total GDP, firm sales, or a forecast of pure monopoly profit. The model holds both outputs fixed within a period. It omits investment incentives in the automated sector. Thus, a change in taxation does not reduce $\Pi$ inside this model. Any such response must enter as a different scenario.

Recipient preferences are Cobb–Douglas, with essential expenditure share $\alpha$, where $0 < \alpha  < 1$. A recipient with transfer $d$ consumes:

$$x = \frac{\alpha d}{p}, \qquad z=(1-\alpha)d. \tag{1}$$

Owners have essential expenditure share $\beta$, where $0 < \beta  < 1$. These shares describe preferences, not minimum needs. A household may meet one floor and miss the other. That is why both floors must be checked.

All money values are annual units of the reproducible good per total resident, unless stated otherwise. $d$, $x$, and $z$ are per recipient. $n d$ is the total transfer per total resident.

### 3.2 Public revenue

The public sector owns share $s$ of claims on $\Pi$. It taxes the private share at rate $\tau$. Collection efficiency is $e$. All three lie between zero and one. The effective public share is:

$$\phi=s+(1-s)e\tau. \tag{2}$$

This formula avoids counting tax receipts on the public share a second time. Uncollected tax remains private income. The model imposes no separate tax on essential rents.

Public spending on other uses is $G \ge  0$, measured in the reproducible good. Spendable transfer revenue is:

$$R=\phi\Pi-G, \qquad nd=R. \tag{3}$$

Equation (3) distributes all remaining revenue. For positive floors, $R$ must be positive. A policy with $R \le  0$ fails the test. The base model has no deficit finance. Public ownership is inherited at the start of the period. Its acquisition is not free in a real transition; Section 5 tests an added debt-service cost.

### 3.3 Prices and the return of rents

Owners receive private reproducible income $(1-\phi )\Pi$ and essential rents $pQ$. Their total essential expenditure is:

$$\beta[(1-\phi)\Pi+pQ]. \tag{4}$$

Market clearing requires:

$$pQ=\alpha R+\beta[(1-\phi)\Pi+pQ].$$

Therefore:

$$p=\frac{\alpha R+B}{(1-\beta)Q}, \qquad B=\beta(1-\phi)\Pi. \tag{5}$$

The term $pQ$ in owners' income matters. Dropping it would overstate recipients' access. With $R>0$, recipients receive:

$$x=\frac{\alpha(1-\beta)QR}{n(\alpha R+B)}, \qquad z=\frac{(1-\alpha)R}{n}. \tag{6}$$

Both goods markets clear: total essential consumption equals $Q$, while reproducible consumption and public spending together equal $\Pi$. Appendix A gives the accounting check.

Output is given within each period. The model therefore describes allocation at a point in time, rather than growth, production decisions, or the formation of asset prices.

## 4. Financing a minimum consumption level

### 4.1 The public revenue required for both goods

Let the required amounts per recipient be $h>0$ for the essential service and $b>0$ for the reproducible good. First define the capacity margin:

$$\Delta=(1-\beta)Q-nh.$$

For $\Delta >0$ and $\Pi >G$, the recipient group meets both floors if and only if:

$$\phi\geq\phi_{\rm req}=\max\left\{
\frac{G+nb/(1-\alpha)}{\Pi},
\frac{\alpha\Delta G+nh\beta\Pi}{\Pi(\alpha\Delta+nh\beta)}
\right\}. \tag{7}$$

The first term is the reproducible-goods condition. The second is the essential-access condition. If the required value exceeds one, the selected floor is infeasible under the model's cash policy.

The two terms have a direct interpretation. Public revenue must buy enough reproducible output, but it must also let recipients compete for the essential service. The second condition accounts for the rental income that flows back to owners. Appendix A provides the proof.

If $\Delta <0$, no cash policy in this model meets $h$, even with full public ownership of $\Pi$. If $\Delta =0$, the essential floor can be met only at $\phi =1$, with positive $R$. The reproducible floor must still pass. These edge cases are implemented and tested.

The strong capacity condition is specific to private essential-asset ownership and owner demand. It is not a physical impossibility theorem. A different allocation system could assign essential goods directly. Any such system still needs at least $nh$ physical units for recipients. The present cash policy needs more because owners continue to consume essential services from their rental income.

These conditions establish feasibility within the market model. Delivering a public guarantee also requires correct eligibility records, accessible payments, service delivery, and an appeal process.

### 4.2 Taxes and public ownership

For fixed $\Pi,Q,G,n,\alpha,\beta$, any two pairs $(s,\tau )$ that give the same $\phi$ produce the same allocation. This follows directly from (3)–(6). Public equity has no additional one-period benefit inside this model once effective capture is equal.

The equivalence does not include acquisition costs, voting rights, tax avoidance responses, risk, or future investment. It therefore cannot establish that a social wealth fund and a tax law are interchangeable institutions. Both can also lose revenue when the same underlying output falls.

## 5. Numerical examples and adverse states

The calculations use synthetic annual units rather than a country calibration. The base values are $n=0.8$, $\alpha =0.4$, $\beta =0.3$, $\Pi =100$, $Q=1.4$, $G=8$, $s=0.2$, $\tau =0.3$, and $e=0.8$. The floors are $h=0.6$ and $b=20$ per recipient. All inputs are retained in [design.json](data/design.json).

### 5.1 Why the transfer budget can pass while access fails

| Scenario | Effective capture | Essential units | Reproducible units | Both floors met? |
| --- | ---: | ---: | ---: | :---: |
| Base | 0.392 | 0.498 | 23.400 | No |
| Taxes only, same capture | 0.392 | 0.498 | 23.400 | No |
| Low supply: $Q=0.8$ | 0.392 | 0.284 | 23.400 | No |
| Low supply, public share $s=0.5$ | 0.620 | 0.458 | 40.500 | No |
| Supply expansion: $Q=1.8$ | 0.392 | 0.640 | 23.400 | Yes |
| Low output: $\Pi =80$ | 0.392 | 0.478 | 17.520 | No |
| Weak collection: $e=0.6$ | 0.344 | 0.428 | 19.800 | No |
| Public share $s=0.35$ | 0.506 | 0.655 | 31.950 | Yes |
| Same public share, extra cost of 15 | 0.506 | 0.523 | 20.700 | No |

The base case needs capture of about 0.4651 to meet both floors. The reproducible-goods condition alone needs only 0.3467. A budget check can therefore pass while access fails. The taxes-only case uses $\tau =0.49$ with $e=0.8$. It illustrates the equivalence described in Section 4.2.

The supply-expansion row holds public spending fixed. It is an exogenous capacity comparison, not evidence that supply is free. Section 6 includes investment costs. The last row adds 15 units to $G$ as a hypothetical debt-service burden. It is not an estimated acquisition price. It shows how a public-ownership gain can disappear after financing costs.

### 5.2 How much protection does a stronger public claim provide?

The grid combines three output levels $\{80,100,120\}$, four supply levels $\{0.8,1.1,1.4,1.8\}$, and three collection levels $\{0.6,0.8,1.0\}$. Each of 16 policies faces 36 states, giving 576 cases. Policy shares are $s\in \{0,0.2,0.35,0.5\}$ and rates are $\tau \in \{0.2,0.3,0.4,0.5\}$. All cases are retained in [stress.csv](results/stress.csv).

The base policy passes 5 of 36 states. The policy $s=0.35,\tau =0.3$ passes 17. The strongest pass count is 27, reached by two policies. No tested policy passes all states. The 36 states have no assigned probabilities. A pass count is grid coverage, not a success probability.

For $s=0.5,\tau =0.4$, every tested failure occurs at $Q=0.8$. Conditional on $Q\ge 1.1$, that policy passes all 27 remaining grid states. At the worst output and collection values, it requires $Q\ge 1.06154$. Its floor at $Q=1.1$ is approximately $x=0.62174$ and $z=31.2$. This is a conditional operating boundary. It does not justify choosing a national public-ownership share of 50 percent.

The grid allows low output and weak collection at the same time. It therefore does not assume independent revenue protection from taxes and equity. It does not estimate a joint distribution or test states outside the listed ranges. A wider range can reverse a passing assessment.

## 6. Investment in essential supply

Let public spending include an annual investment cost $I$, so that $G=G_0+I$. Assume completed investment adds $\eta I$ units of annual essential capacity:

$$Q(I)=Q_0+\eta I, \quad R(I)=\phi\Pi-G_0-I.$$

This is a comparison of annual policy configurations. It is not a present-value appraisal of a durable asset. It holds the distribution of essential-asset rights fixed. It can represent a publicly funded supply subsidy whose output remains privately owned. A public housing system would require a different ownership equation.

For $R>0$, fixed $\phi$ and $\Pi$, and $B>0$, differentiate (6):

$$\frac{d\log x}{dI}=\frac{\eta}{Q(I)}-
\frac{B}{R(I)[\alpha R(I)+B]}. \tag{8}$$

### 6.1 The tradeoff between capacity and current income

Completed investment increases recipient essential consumption at the margin if and only if:

$$\frac{\eta}{Q(I)}>\frac{B}{R(I)[\alpha R(I)+B]}. \tag{9}$$

The condition compares the proportionate gain in capacity with the access lost when investment reduces the transfer. The derivative is derived in Appendix A.

This is a local access test, not a welfare ranking. Reproducible consumption always falls by $(1-\alpha )/n$ per extra unit of $I$. A project can pass (9) and still make the joint floor fail. At $B=0$, essential access is independent of transfer size while $R>0$; investment still reduces reproducible consumption.

If construction takes time, current $Q$ does not rise when the first payment occurs. The positive term in (8) then disappears for that period. Both consumption measures fall when $B>0$. A reserve or separate transition budget can bridge the gap, but it must be funded and stress-tested. The model does not create that reserve by assumption.

### 6.2 Numerical results and construction delay

The experiment tests $I\in \{0,2,4,6,8,10\}$ and $\eta \in \{0.01,0.04,0.08\}$, with both completed and delayed capacity. This gives 36 rows. At the base point, the local threshold is $\eta >0.02664$.

At $\eta =0.01,I=4$, completed investment lowers essential access from about $0.498$ to $0.471$. At $\eta =0.04,I=4$, it increases access to $0.510$, while reproducible consumption falls to $20.4$. At $\eta =0.08,I=8$, essential consumption reaches $0.602$, but reproducible consumption falls to $17.4$. Thus, even a project that meets the essential floor can fail the joint test.

No investment row meets both floors under the base capture policy. This negative result is retained. Investment alone is not a substitute for adequate public revenue. During the modeled delay, every positive investment cost lowers both consumption measures. These comparisons do not include later benefits, depreciation, borrowing, or discounting. They identify a transition funding problem; they do not estimate an optimal investment schedule.

## 7. Implications for economic governance

The model suggests that a post-labor income system should be assessed as a claim on real consumption, rather than solely as a budget commitment. This has implications for income rights, public ownership, investment, and the evidence used to adjust policy. The institutional proposals in this section extend beyond the model's formal results; their political feasibility and legal authority require separate assessment.

An income right that does not depend on employment is the starting point. Clear eligibility, regular payment, and an effective appeal route matter especially when households cannot replace a missing transfer with wages. A broad resident base would also need to address children, disability costs, and people without standard identity documents. A universal payment with tax recovery from high-income owners is one possible design. The model uses a net transfer to the asset-poor group and does not calculate the gross cost or administration of a universal scheme. During partial displacement, retraining, wage insurance, and shorter hours can remain useful, but support should respond to household income and deprivation rather than AI benchmark scores or repeated training requirements when suitable jobs are absent.

The financing of that right depends on public claims that are usable when needed. Taxes, broad asset ownership, and returns negotiated in exchange for public research, procurement, infrastructure, or resource rights can all contribute. Their costs must enter the accounts. A public company's dividend and tax payment are not independent claims on the same output, and a fund's market value is not a cash reserve. Transparent accounts, independent custody, withdrawal rules, and public oversight can protect the purpose of a social wealth fund. Recipients should not have to sell a permanent claim to meet immediate needs, and benefits should not depend on loyalty to a party or company.

Public revenue design also interacts with competition. Preserving monopoly merely to preserve a tax base can raise the cost of access. Rents, normal returns, and sales are different bases, with different incentive effects. Since the model holds $\Pi$ fixed, it cannot determine a welfare-maximizing tax structure. That question requires the wider public-finance analysis discussed by Korinek and Lockwood [S3].

Essential access requires its own measures. Quantity, quality, waiting time, location, and unmet need can reveal failures that a cash total or general price index conceals. Housing, electricity delivery, transport, and care need to be assessed in the local units that constrain households. The investment condition in Section 6 can screen a project, but the joint floors and construction budget must still be checked. Public provision, taxation of essential rents, or rights to a defined service would change the ownership and allocation equations. They may perform differently from this paper's cash policy and require their own accounts. Service provision should preserve choice and a route to appeal, rather than making basic support a means of coercion.

These distinctions also imply three different reasons for policy adjustment:

| Observed problem | Evidence needed | Possible response |
| --- | --- | --- |
| Household income loss | Income after tax, earnings, vacancies, hours, and hardship | Immediate support and removal of unsuitable job-search conditions |
| Public funding gap | Collected revenue, spendable dividends, required transfers, and reserves | Revised funding, an authorized reserve draw, or legislative action |
| Essential access gap | Local quantity, waiting time, prices, and unmet need | Supply expansion or revised access rules, with support during construction |

Emergency support need not wait for proof that AI caused each loss. A recession, trade shock, and AI displacement can occur together. Diagnosis remains useful for long-term policy, but a household's need can be clear before the cause is settled. To reduce responses to noisy data, one possible rule would expand routine measures after two consecutive quarterly breaches and withdraw temporary measures only after four releases above a separate exit margin. Severe deprivation would permit immediate action. These timings are untested design examples, not optimized thresholds. Their value lies in making the decision rule and exceptions public.

Human institutions remain responsible for choosing the floor, tax burden, and distribution of rights. AI can assist forecasts and payment checks, but should not be the sole authority for eligibility, budget choices, or appeals. A practical route to contest decisions is part of access. Internationally, weak collection capacity and foreign-owned supply may require cooperation over revenue, infrastructure, or transfers. The collection parameter $e$ does not represent foreign ownership, currency risk, or international settlement [S4]. Finally, the framework presumes effective human governance of AI. Fiscal gains do not justify relaxing safety duties, and the model cannot address a loss of control over powerful systems.

## 8. Limitations and empirical development

The analysis depends on fixed output, competitive allocation of essential services, two representative groups, and constant expenditure shares. Real households differ within each group; an adequate group average can conceal exclusion. Saving, asset-price shocks, trade, demographic change, monetary dynamics, and endogenous political decisions are omitted. The static equilibrium also cannot establish financial stability or adequate demand outside its assumptions.

Several observations would require the model to change. Sharp movements in expenditure shares would weaken its demand specification. Queues or supplier market power would require another account of essential allocation. Transfers that fail to reach recipients would invalidate the assumed link from budget to household income. If production falls with the public revenue share, $\Pi$ must be replaced by an estimated response. If investment changes who owns essential services, equation (4) must change as well.

A useful empirical extension would therefore estimate local essential demand, usable capacity, actual collection, subgroup outcomes, and the cost of additional service. The numerical grid provides no national rate recommendation and no empirical causal estimate. It also does not show that transfers alone provide social purpose, political influence, or a meaningful life. Civic, cultural, and personal participation require institutions beyond an income system.

## 9. Conclusion

If wages cease to support households, a public transfer must do more than distribute a share of automated output. It must also let recipients obtain the services that remain scarce. The model makes this distinction explicit: a transfer budget can pass while essential access fails. Supply investment can improve access, but its cost reduces current income and its benefits may arrive later. A credible consumption floor therefore joins income rights, public revenue claims, local access measures, and transition finance. Whether a real economy can sustain such a floor remains an empirical and institutional question.

## Appendix A. Derivations and market accounting

### A.1 Goods-market identities

The model closes both goods markets. Essential consumption sums to $Q$. Reproducible consumption plus $G$ sums to $\Pi$. To verify the second identity, use $(1-\beta )pQ=\alpha R+B$. Owners' reproducible spending then equals $(1-\phi )\Pi +\alpha R$. Add recipient spending $(1-\alpha )R$ and public spending $G$ to obtain $\Pi$.

### A.2 Minimum public revenue share

**Proof.** From (6), $z\ge b$ is equivalent to $\phi \Pi -G\ge nb/(1-\alpha )$. For the essential floor, multiply $x\ge h$ by the positive denominator in (6). Rearrangement gives $\alpha \Delta (\phi \Pi -G)\ge nh\beta (1-\phi )\Pi$. Move terms in $\phi$ to the left and divide by the positive coefficient. This yields the second term in (7). Each step is reversible. The first inequality also ensures $R>0$. ∎

### A.3 Marginal effect of supply investment

**Proof.** Write $\log x$ as a constant plus $\log Q+\log R-\log(\alpha R+B)$. Use $Q'=\eta$ and $R'=-1$. The last two derivatives sum to $-B/[R(\alpha R+B)]$. The sign gives (9). ∎

## Appendix B. Reproduction and research record

Run these commands from the repository root with Python 3.9 or later:

```sh
python3 studies/2026-10-11-post-labor-floor/code/model.py
python3 -m unittest discover -s studies/2026-10-11-post-labor-floor/code -p 'test_*.py' -v
```

The analysis uses only the Python standard library. It needs no network, API key, or random seed. All inputs are synthetic and retained. Generated CSV files contain the complete cases, including failures. [run.json](results/run.json) records runtime information and input, code, and output hashes. The tests check both market identities, the threshold against direct market solutions, exact boundary cases, conditional instrument equivalence, and the investment derivative.

The study is exploratory. The numerical grid was selected during model development. It was not preregistered. [protocol.md](protocol.md) records the decisions and changes. Public source records retain short attributed extracts and hashes. Full downloaded source files remain local because redistribution rights were not established for the full collection. Source extraction is separate from model reproduction.

## Research disclosure

Codex assisted with the literature search, model, code, tests, and manuscript. A separate AI agent searched prior work, and the [independent AI review](reviews/critical-review.md) reproduced the outputs and found no blocking error; the [author response](reviews/author-response.md) records the issues. No human review or journal peer review has occurred. No affiliation or endorsement is claimed; funding and human conflicts were not supplied. No repository reuse licence has been selected, and third-party source rights remain separate. The [editorial revision record](reviews/editorial-revision.md) documents the later changes in presentation.

## References

- **[S1]** Song Zichen. 2026. *Abundance Is an Expenditure Condition: AI Automation, Scarcity Rents, and Access*. arXiv:2609.13801v1, 12 September. [Full text](https://arxiv.org/html/2609.13801v1).
- **[S2]** Aran Nayebi. 2026. *When Do AI Gains Become Broadly Shareable? A Policy Threshold for AI-Driven Automation*. arXiv:2505.18687v4, 29 July. First submitted in 2025 under an earlier title. [Full text](https://arxiv.org/html/2505.18687v4).
- **[S3]** Anton Korinek and Lee M. Lockwood. 2026. *Public Finance in the Age of AI: A Primer*. January Brookings version, Sections 2.4 and 4. Also NBER Working Paper 34873, February. [Inspected PDF](https://www.brookings.edu/wp-content/uploads/2026/01/Korinek-Lockwood-FINAL-for-website.pdf).
- **[S4]** Leonard Wossnig. 2026. *Simulating a Post-Automation Economy*. arXiv:2606.20649v1, 7 June. [Full text](https://arxiv.org/html/2606.20649v1).
- **[S5]** Fernanda Brollo, Era Dabla-Norris, Ruud de Mooij, Daniel Garcia-Macia, Tibor Hanappi, Li Liu, and Anh D. M. Nguyen. 2024. *Broadening the Gains from Generative AI: The Role of Fiscal Policies*. IMF Staff Discussion Note 2024/002, 17 June. [Official summary](https://www.imf.org/en/Publications/Staff-Discussion-Notes/Issues/2024/06/11/Broadening-the-Gains-from-Generative-AI-The-Role-of-Fiscal-Policies-549639).
- **[S6]** Pawel Gmyrek, Janine Berg, Karol Kamiński, Filip Konopczyński, Agnieszka Ładna, Balint Nafradi, Konrad Rosłaniec, and Marek Troszyński. 2025. *Generative AI and Jobs: A Refined Global Index of Occupational Exposure*. ILO Working Paper 140, 20 May. [Official publication summary](https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure).
- **[S7]** Anton Korinek and Megan Juelfs. 2022. *Preparing for the (Non-Existent?) Future of Work*. NBER Working Paper 30172, June. [Primary abstract](https://www.nber.org/papers/w30172).
- **[S8]** Jakub Growiec, Klaus Prettner, and Maciej Szkróbka. 2026. *Redistributive Policies for the Times of Transformative AI*. arXiv:2609.14750v1, 13 September. [Primary abstract](https://arxiv.org/abs/2609.14750v1).
