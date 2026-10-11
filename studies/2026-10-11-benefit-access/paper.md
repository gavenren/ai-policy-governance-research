# When a Funded Benefit Still Does Not Arrive
## Review Queues, Advance Payments, and Access to Income After Human Labor

> **State:** Complete-study draft. **Study:** S007. **Date:** 11 October 2026.
> **Evidence cutoff:** 2026-10-11T21:05:14Z, covering the seven retained source captures and the passages checked for this paper.

## Abstract

A public benefit can be fully funded yet fail to reach eligible people when it is due. That failure becomes especially serious if households cannot replace a missing transfer with earnings. This paper compares payment after appeal with two forms of automatic advance: payment at initial denial and payment at the due date for claims still unresolved. The rules face the same review queue. Their cash requirements depend on the funding baseline. When eligible benefits are funded as they become due, unpaid eligible amounts remain earmarked cash; paying them does not require funding them a second time. The additional reserve instead covers unresolved ineligible advances and losses on advances that review has closed. A stable queue does not bound those losses. Under reliable payment at the deadline, advancing only unresolved claims uses no more end-period cash than advancing every initially denied claim, while achieving the same measured timeliness. In 567 synthetic cases, a reserve of 30 benefit units covers 396 initial-advance paths and 413 end-of-period-advance paths. The results clarify the difference between financing an entitlement, maintaining review capacity, and delivering the payment.

## 1. Introduction

An income guarantee is useful only if people receive the money. A government may have sufficient revenue, and the economy may have sufficient goods, while an eligible household still waits through an incorrect denial and a slow appeal. In a setting where labor income is no longer available as a fallback, a payment interruption is a direct threat to the household's means of support.

The financial problem can be less obvious than the delay. Consider a benefit worth one unit, with ten eligible denied claims and two ineligible claims arriving each period. After an initial outage, review clears twelve claims per period, leaving a constant queue of twelve. Suppose the government advances money to unresolved claimants and recovers half of an ineligible advance after review. The queue is stable, but losses continue: two new ineligible advances per period leave one unit permanently unrecovered. An initial reserve of thirty fails in period thirty. Faster review and a stable backlog do not, by themselves, finance those recurring losses.

This paper asks which payment rules can meet a specified deadline with finite review capacity and finite additional cash. It holds eligible benefit funding constant across three rules. Rule A waits for review before paying an initially denied eligible claim. Rule P pays every initially denied claim immediately and recovers part of any ineligible advance after review. Rule J uses the review capacity available within the period, then pays the claims still open at its end. Ineligibility can reflect errors or misunderstandings and is not treated as evidence of fraud.

The comparison yields two main results. First, the extra funding needed for advances must exclude eligible entitlements that are already funded. Those amounts are still owed even under the appeal-only rule. Second, waiting for reviews within the period avoids some ineligible advances without increasing measured period-end delay, provided payment can reliably occur at the deadline. Earlier payment may still matter for hardship within the period or for protection against settlement failure; those benefits are outside the comparison.

The post-labor premise is conditional. The paper does not estimate the date or probability at which AI could make competitive work an inadequate source of income. It examines payment delivery under that assumption. The companion study S004 addresses public revenue and scarce goods. Here, all eligible benefits are funded when due, goods are available, and the benefit's adequacy is taken as a separate question. The analysis therefore isolates one part of an income guarantee rather than establishing the whole guarantee.

## 2. Related literature

Benefit access is an established research field. Giannella, Homonoff, Rino, and Somerville report a large field experiment on SNAP interviews. Flexible interview access increased approval and participation. Their author abstract establishes a relevant mechanism: process design can affect receipt. We read that abstract, not the full working paper. We do not use its effect sizes as parameters. [B02](https://www.nber.org/papers/w31239)

Bennett, Currie, and Podoletz study automated Universal Credit through 44 participants. Their qualitative analysis identifies time, financial, and emotional costs. It also examines payment errors and attempts to resolve them. Their findings support attention to the delivery process. They do not supply a population error rate for this model. The article appeared online in 2024 and in a 2026 journal issue. [B03](https://www.cambridge.org/core/journals/journal-of-social-policy/article/universal-credit-administrative-burdens-of-automated-welfare/6304AF71E445EF4A97ED47C0413331B8)

The closest technical work is Daw, Pache, and Zhou's 2026 preprint on SNAP call centers. It models repeat calls, abandonment, and endogenous congestion. It connects service design with meaningful access. We read its introduction, related work, model, and operational comparison. We do not claim that queues cause access problems as a new result. Our queue is simpler: every disputed claim enters automatically and remains until review. The added object is a matched comparison of payment timing and public cash accounts. [B01](https://arxiv.org/html/2605.15165v1)

Anunrojwong, Iyer, and Manshadi model congested social services and users with different outside options. Their analysis already includes users who have no viable alternative. It studies information design and strategic entry. Our model instead fixes entry and compares payment rules after initial denial. [B05](https://arxiv.org/html/2005.07253v3)

Advances during review also predate this study. Vethaak and colleagues use Rotterdam application data from 2013–2019. They study processing time and benefit prepayments through caseworker variation. Their paper describes advances, later offsets, and outstanding claims after rejection. Its labor-market outcomes cannot be transferred to a setting without viable paid work. We use it to locate the institutional mechanism, not to claim that an advance rule is new. [B07](https://docs.iza.org/dp17839.pdf)

Official documents further limit the novelty claim. The World Bank links registries, payment systems, case management, and grievance channels. Integration is already a stated delivery-system objective. [B04](https://www.worldbank.org/en/brief/2025/09/19/digital-delivery-systems) A July 2026 DWP assessment describes machine-learning referrals for Universal Credit advances. It reports a one-day median additional delay for referred requests later approved. That report concerns a defined group and period; a median is not a maximum waiting-time guarantee. [B06](https://www.gov.uk/government/publications/effectiveness-assessment-including-statistical-analysis-of-the-universal-credit-advances-machine-learning-model-1-april-2025-to-31-march-2026/effectiveness-assessment-of-universal-credit-advances-model)

The contribution is an accounting comparison of payment rules operating on the same review path. We separate eligible arrears, open ineligible advances, and permanent losses within the same finite review path. We then test two automatic-payment timings against an appeal-only rule. The targeted, English-language search did not establish whether an equivalent comparison exists elsewhere. The contribution is limited to the explicit cash and timing test developed here.

## 3. Claims, review capacity, and funding

Time has periods $t=1,\ldots,T$. Each eligible claim has amount $b>0$. There are $n_t$ eligible claims due in period $t$. The initial system denies $e_t\leq n_t$ of them. Another $i_t$ claims are ineligible and initially denied. The other eligible claims receive payment without review. We exclude initially approved ineligible claims to isolate the effect of advancing denied claims.

All denied claims enter review automatically. Capacity is $m_t$ claims per period. Review serves earlier arrival cohorts first. Within a cohort, it serves eligible and ineligible mass in proportion to their shares. This is a fluid model. Fractional claims represent group mass, not a partially adjudicated named person. Correct review is assumed. The authority does not know each claim's true type before review; the analyst uses that type for accounting.

Let $Q^E_t$ and $Q^I_t$ be eligible and ineligible claims still open after period $t$. Let $R^E_t,R^I_t$ be cumulative reviewed claims of each type. Let $I_t=\sum_{s\leq t}i_s$. Conservation gives

$$
Q^E_t=\sum_{s\leq t}e_s-R^E_t,\qquad Q^I_t=I_t-R^I_t.
$$

The total queue follows

$$
Q_t=\max\{0,Q_{t-1}+e_t+i_t-m_t\}.
$$

An outage can increase denials and reduce capacity at the same time. No assumption of independent errors is needed. Capacity can represent computation, trusted evidence access, adjudication, or staff time. A post-labor setting does not require human reviewers to outperform AI. It still requires a process that can inspect disputed evidence and authorize changes.

The public authority receives $b n_t$ when eligible payments become due. Review spending is separately funded. The same capacity cost applies under all three rules, so it cancels in the main comparison. This is a conditional, fully funded benchmark. It does not give administrators knowledge of true individual or total eligibility. Actual aggregate funding uncertainty needs a separate test. If only approved claims receive budget authority, a further appropriation rule is necessary.

Under Rules P and J, an eligible advance replaces the payment owed for that claim. It does not create a second payment or a deduction from a later, separate entitlement. A reviewed ineligible advance returns fraction $r\in[0,1]$ of its amount immediately. The rest is a permanent public loss. Recovery cost, interest, collection delay, and hardship from recovery are absent. Thus the model does not select a socially optimal recovery rate.

We measure delay as

$$
D_A=\sum_{t=1}^{T}Q^E_t.
$$

Its unit is **eligible claim-periods awaiting payment**. If each person has one claim, this also counts person-periods of exposure to an unpaid entitlement. With repeated claims, it can count the same person more than once. It is not a count of unique people without food. A linear delay cost $hD_A$ is possible, but $h$ is not estimated here.

We also report claims first unpaid at their due date and claims still unpaid two periods later. The code parameter `deadline=2` controls this later measurement only. It does not defer Rule J payment for two periods: that payment occurs at the end of the arrival period. The latter outcome excludes late cohorts whose two-period deadline lies beyond the horizon. All terminal arrears remain in the accounts. A final payment can remove arrears without removing delay already experienced. Rules P and J have zero measured payment delay only when their required cash and payment routes are available.

## 4. Payment rules and their fiscal cost

Before comparing the rules, it is necessary to distinguish an unpaid entitlement from a new loss. An eligible payment remains due while review is open. If its funding arrived on the due date, that cash is already available and must remain reserved for the claim. The equations below use that same funding baseline for all three rules.

Write $F_t=b\sum_{s\leq t}n_s$ for cumulative eligible funding. Omit the common review budget in this section. Under Rule A, cumulative outflow is

$$
C^A_t=F_t-bQ^E_t.
$$

Thus $bQ^E_t$ remains earmarked cash. Calling this amount a saving would confuse nonpayment with a lower obligation.

Under Rule P, cumulative net outflow is

$$
C^P_t=F_t+bI_t-rbR^I_t.
$$

### 4.1 The reserve needed beyond eligible benefit funding

Relative to fully funded eligible entitlements, Rule P requires

$$
L^P_t=C^P_t-F_t=bQ^I_t+b(1-r)R^I_t.\tag{1}
$$

Its spending difference from Rule A is

$$
C^P_t-C^A_t=bQ^E_t+L^P_t.\tag{2}
$$

The identity separates two sources of extra funding: cash still tied up in open ineligible claims and the part of resolved advances that will not be recovered. The algebra is given in Appendix A.1. Comparing expenditure with the appeal-only rule is a different calculation because that rule still holds cash owed to eligible people.

A reserve $K$, without new contributions, covers end-period cash exactly when

$$
K\geq\max_{t\leq T}L^P_t.\tag{3}
$$

With cumulative new contributions $Z_t$, replace this with $K+Z_t\geq L^P_t$ at each date. These are cash tests, not tests of sovereign solvency. They assume the authority can use the funds for their specified purpose.

For Rule J, let $U_t$ be cumulative ineligible claims that were still open at their payment deadline and received advances. Let $R^{I,J}_t$ count those advanced claims later reviewed. Ineligible claims resolved within their arrival period receive no advance. Every claim still open has an advance, so

$$
Q^I_t=U_t-R^{I,J}_t,\qquad
L^J_t=bQ^I_t+b(1-r)R^{I,J}_t.\tag{4}
$$

### 4.2 The effect of waiting for reviews within the period

Under reliable deadline payment and identical review paths,

$$
L^J_t\leq L^P_t
$$

at every period end. Both rules have zero measured eligible delay when funded.

The additional losses under Rule J cannot exceed those under Rule P, because only a subset of the ineligible claims receives an advance. Both rules pay eligible claims by the period-end deadline. Appendix A.2 gives the proof.

This is a limited dominance result. It ignores welfare gains from receiving money before the period end. Equal payment by period end does not imply equal access within that period. It also assumes review results and payment instructions can be processed at that deadline. It does not recommend delaying emergency support until an arbitrary administrative date.

Cash-flow order matters. If advances must leave before the period's recoveries arrive, Rule P needs gross cover

$$
G^P_t=b(I_t-rR^I_{t-1}).
$$

For Rule J, a conservative corresponding order gives $G^J_t=b(U_t-rR^{I,J}_{t-1})$. The code reports both peak net and peak gross cover. Net cover alone is sufficient only when the assumed settlement order permits the offset.

## 5. Why queue stability is not financial stability

Consider constant arrivals of ten eligible denied claims and two ineligible claims per period. Set $b=1$, $r=1/2$, and capacity to twelve. The first period has zero capacity; each later period reviews the previous cohort. The queue then stays at twelve claims forever. Eligible arrears stay at ten. There is no growing review backlog.

Every current cohort remains open at its deadline. Both advance rules therefore pay its two ineligible claims. At the end of period $t$, two ineligible claims remain open and $2(t-1)$ advanced ineligible claims have completed review. Equations (1) and (4) yield

$$
L_t=2+\tfrac12[2(t-1)]=t+1.
$$

A reserve of thirty fails in period thirty, despite the constant queue. The required flow contribution is one benefit unit per period after the initial setup. A loan facility alone cannot absorb these losses indefinitely. General revenue, a loss budget, fewer ineligible advances, or a higher net recovery rate must change the arithmetic.

The counterexample also separates speed from loss. Faster review can reduce open advances. It cannot recover the unrecoverable share of advances already paid under the fixed recovery assumption. Once all such cases close, cumulative loss equals $b(1-r)$ times their count. Queue stability and review accuracy are therefore insufficient conditions for a permanent payment guarantee.

The opposite boundary is equally useful. If no ineligible claims exist, additional reserve is zero even during a severe eligible-denial outage. The authority releases earmarked benefit cash. A large difference from appeal-only spending does not imply a new fiscal cost. This result fails if the authority spent the earmarked money elsewhere or never funded the entitlement when due.

## 6. Numerical results

The main horizon has twelve periods and 100 eligible claims per period. The benefit is one account unit. The reference path has ten false denials, two ineligible claims, and fifteen review slots per period. Recovery is one half. In the common-outage case, periods four through six have sixty false denials and zero review capacity. All inputs are assumptions, not estimates.

Table 1 reports selected cases. Delay applies to Rule A. The two advance rules remove that measured delay if their cash tests pass. All cash columns use benefit units and net period-end settlement. Values are rounded; full precision is retained in the result files.

| Case | Rule A delay, claim-periods | Terminal eligible arrears | Peak additional cover, P | Peak additional cover, J |
|---|---:|---:|---:|---:|
| Fast review throughout | 0.00 | 0.00 | 12.00 | 0.00 |
| Stable positive backlog | 120.00 | 10.00 | 13.00 | 13.00 |
| Capacity ten throughout | 130.00 | 20.00 | 14.00 | 11.50 |
| Common outage | 1,345.16 | 152.90 | 19.55 | 16.55 |
| Common outage; full recovery | 1,345.16 | 152.90 | 15.10 | 15.10 |
| Common outage; no ineligible claims | 1,335.00 | 150.00 | 0.00 | 0.00 |
| Common outage; forty slots outside outage | 846.24 | 15.00 | 14.83 | 11.83 |

Source: executed `results/scenarios.csv`; exact inputs in `data/design.json`.

The fast-review case is a negative result for blanket early advances. Every eligible claim already meets its deadline under Rule A. Rule P still creates twelve units of unrecovered ineligible payments. Rule J avoids those payments and requires no extra reserve. The model therefore does not support initial-denial advances as a general default.

The common outage produces 240 eligible claims unpaid at their due dates under Rule A. This is 20% of 1,200 eligible claims. There are 220 observed misses of the two-period threshold among 1,000 eligible claims whose threshold falls within the horizon. Terminal arrears are 152.90 units. Rule P's peak spending difference from Rule A is 189 units, but its extra reserve beyond due funding is only 19.55. These peaks occur at dates determined separately. They must not be subtracted as if they were simultaneous balances.

More review capacity reduces delay and open advances. It does not prevent the payment interruption during the zero-capacity periods. Nor does the test include the extra cost of buying capacity. Forty slots outside the outage are a physical alternative, not a proved cost-effective policy.

Timing changes outcomes even with the same aggregate arrivals and available capacity. Spreading the common-outage totals evenly produces 949.13 delay claim-periods, compared with 1,345.16 under the outage. Moving the denial surge to the first three periods, before the capacity outage, produces 1,646.13. Thus overlapping shocks are not always the worst arrangement. Earlier arrival of errors gives them more time to accumulate delay within this horizon. No general correlation ranking follows from these examples.

The stress grid varies base denials, surge size, outage duration, review capacity, ineligible arrivals, and recovery. It contains 567 distinct paths and recovery settings. An earlier 729-row Cartesian grid repeated cases when surge size was inactive. Those duplicates were removed before the reported totals. There are no random draws or empirical probabilities.

At a reserve of thirty, Rule P passes the net test in 396 cases and the gross test in 389. Rule J passes in 413 and 406 cases respectively. Rule A has no late eligible claims in 45 cases. The largest Rule A delay is 3,300 claim-periods. The largest additional cover is 120 units. These counts describe the selected grid only. They do not establish a 73% chance of policy success or a recommended reserve for any country.

## 7. Implications for benefit administration

The results point to a need for separate accounts of entitlement funding, review activity, and payment delivery. The first account establishes when money becomes available. A budget based only on completed approvals can create an incentive to postpone recognition of a claim. With funding at the due date, unpaid eligible balances should remain reserved for those entitlements and be shown separately from cash that is free for other public uses. The model's reserve result depends on that separation.

The second account concerns the route from a claim to a usable payment. A right to review requires intake, evidence, a decision, and settlement. The guarantee studied here begins only after a claim enters the system. It does not protect eligible people who cannot register, lack accepted identity documents, or are excluded before review. Independent intake and correction of identity records remain separate institutional requirements. Even after an advance is paid, a meaningful appeal is necessary because a disputed eligibility label can affect later claims.

The third account distinguishes temporary exposure from recurring losses. Open ineligible advances may be recovered, while the unrecovered share of resolved advances needs a continuing source of finance. A falling queue can coincide with growing cumulative loss. A rising queue can also coexist with timely payment when advances are properly funded. Neither queue length nor the cash balance alone is a complete measure of access.

These distinctions affect the comparison between review investment and payment design. Extra capacity can shorten waits, but payment at the deadline may provide access before every dispute is settled. The relevant comparison uses the same claim paths and reports both successful payment and net public loss. Average review time or classifier accuracy can conceal a long tail of delay, so the distribution of waiting times also matters. The model does not establish which combination is least costly once the cost of capacity and claimant behavior are included.

These are administrative implications of the accounting results, not evidence that every submitted claim should be paid without conditions. Claim authentication, eligibility rules, and duplicate prevention are outside the model. The value of a guarantee depends on who can reach the review process, how accurately that process works, and what hardship recovery creates. A society without an earnings fallback would have particular reason to examine those conditions closely.

## 8. Limitations and further evidence

The model deliberately omits strategic applications, endogenous repeat contacts, review error, and group-specific barriers. It does not estimate claimant behavior after an advance rule changes. The number of ineligible claims could rise under easier payment. Recovery could itself create hardship or costly disputes. These omitted responses can change the preferred policy.

The fluid service rule hides within-cohort inequalities. Equal average shares do not prove equal treatment for named people. Recovery fractions are fixed and immediate. Real collections can have long delays. Borrowing cost and the opportunity cost of public funds are zero. Benefit amounts are equal, prices are fixed, and goods are available. No claim about aggregate consumption, inflation, or political feasibility follows.

The finite horizon also matters. Terminal arrears and open advances are retained, not forgiven. Eventual loss is reported only under eventual review with the stated recovery rate. It is not a forecast that the queue will actually clear. The two-period deadline statistic has right-censored late cohorts, while the delay statistic counts all observed unpaid exposure.

Twelve tests check boundaries, a hand-calculated ledger, conservation, settlement order, the stable-backlog counterexample, and the end-of-period-rule inequality. A separate scalar queue recurrence checks total backlog. A catch-up case verifies that zero final arrears do not erase earlier delay. Internal assertions also reconcile funds and claims at every date. These checks validate the stated model, not the realism of its assumptions.

An empirical extension would need dated claim arrivals, initial decisions, review completions, payment receipts, recoveries, and corrected eligibility. It would also need evidence on eligible people absent from administrative records. Without those data, a calibrated reserve recommendation would be false precision. A suitable pilot would compare payment rules on common service paths and measure both access and net public losses.

## 9. Conclusion

Funding a benefit and delivering it on time are different achievements. The model shows how an appeal process can delay fully funded payments, and how advances can remove that delay under stated operating conditions. It also shows why the required reserve depends on the correct baseline: eligible arrears are money still owed, while ineligible advances create additional exposure and possible loss. A stable review queue controls neither those cumulative losses nor access by itself. A credible payment guarantee therefore requires an account of deadlines, settlement, reserved funds, and the continuing cost of mistakes.

## Appendix A. Accounting proofs

### A.1 Additional cover and the comparison with appeal-only payment

**Proof.** Substitute $I_t=Q^I_t+R^I_t$ in the Rule P outflow. Then subtract the Rule A outflow. No distributional or equilibrium assumption is needed. The result is an accounting identity. The important choice is the funding baseline. Equation (2) compares spending rules. Equation (1) measures additional cover beyond funding already owed to eligible claims.

### A.2 The reserve effect of end-of-period advances

**Proof.** The two rules have the same $Q^I_t$. Reviewed ineligible claims that previously received an end-of-period advance form a subset of all reviewed ineligible claims. Therefore $R^{I,J}_t\leq R^I_t$. Multiply by nonnegative $b(1-r)$ and apply equations (1) and (4). Both rules pay eligible claims no later than the defined deadline.

## Appendix B. Reproduction and research record

The [study README](README.md) gives the reproduction commands. The parameter file, complete scenario results, and stress grid are retained in the study directory. Source titles, authors, versions, retrieval times, capture hashes, short extracts, and rights notes are recorded in `sources/manifest.csv` and `sources/snapshots/`. Full third-party source texts are not distributed.

## Research disclosure

AI assisted with source search, model design, code, checks, and writing. The separate internal AI [critical review](reviews/critical-review.md), [author response](reviews/author-response.md), and [completion gates](completion-gates.md) document the substantive checks. No interviews, new human data collection, or human peer review were performed. No affiliation, endorsement, funding source, or conflict status is asserted, and the repository owner has not certified the conclusions. The study remains an AI-assisted draft. The [editorial revision record](reviews/editorial-revision.md) records the subsequent presentation changes.

## References

- **[B01]** Andrew Daw, Chloe Pache, Angela Zhou. *[Due Process on Hold: A Queueing Framework for Improving Access in SNAP](https://arxiv.org/html/2605.15165v1)*. arXiv:2605.15165v1. Publication date: 2026-05-14.
- **[B02]** Eric Giannella, Tatiana Homonoff, Gwen Rino, Jason Somerville. *[Administrative Burden and Procedural Denials: Experimental Evidence from SNAP](https://www.nber.org/papers/w31239)*. NBER Working Paper 31239 landing page. Publication date: 2023-05; exact day unknown.
- **[B03]** Hayley Bennett, Morgan Currie, Lena Podoletz. *[Universal Credit: administrative burdens of automated welfare](https://www.cambridge.org/core/journals/journal-of-social-policy/article/universal-credit-administrative-burdens-of-automated-welfare/6304AF71E445EF4A97ED47C0413331B8)*. doi:10.1017/S0047279424000175 publisher HTML. Publication date: 2024-09-18 online; 2026-01 journal issue.
- **[B04]** World Bank. *[Delivery Systems for Social Protection](https://www.worldbank.org/en/brief/2025/09/19/digital-delivery-systems)*. public brief captured 2026-10-11. Publication date: unknown; URL contains 2025-09-19, no visible date verified.
- **[B05]** Jerry Anunrojwong, Krishnamurthy Iyer, Vahideh Manshadi. *[Information Design for Congested Social Services: Optimal Need-Based Persuasion](https://arxiv.org/html/2005.07253v3)*. arXiv:2005.07253v3. Publication date: 2022-10-21.
- **[B06]** Department for Work and Pensions. *[Effectiveness Assessment of Universal Credit Advances Model](https://www.gov.uk/government/publications/effectiveness-assessment-including-statistical-analysis-of-the-universal-credit-advances-machine-learning-model-1-april-2025-to-31-march-2026/effectiveness-assessment-of-universal-credit-advances-model)*. assessment for 1 April 2025 to 31 March 2026. Publication date: 2026-07-09.
- **[B07]** Heike Vethaak, Ernst-Jan de Bruijn, Marike Knoef, Pierre Koning. *[Deter and Deteriorate: The Effects of Application Processing Times on Welfare Receipt and Employment](https://docs.iza.org/dp17839.pdf)*. IZA Discussion Paper 17839. Publication date: 2025-04; exact day unknown.
