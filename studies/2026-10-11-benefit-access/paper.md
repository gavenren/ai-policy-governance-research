# When a Funded Benefit Still Does Not Arrive

## Review queues and automatic payment in a post-labor economy

**Study S007 · State: Complete-study draft · 11 October 2026**

**Evidence cutoff:** 2026-10-11T21:05:14Z. This cutoff covers the seven retained source captures and the passages checked for this paper. **Method:** a theoretical accounting model and synthetic stress tests. **Review:** separate internal AI critical review is complete. No human peer review has occurred.

### Abstract

A public benefit can have full funding and still fail to reach eligible people on time. This risk matters in an economy where people cannot replace missing transfers with earnings. We compare three payment rules using the same review queue: payment after appeal, payment at initial denial, and payment by the due date for claims still unresolved. We derive an exact cash-cover condition. If eligible benefits are funded when due, delayed eligible payments remain earmarked public cash. They must not be counted again as a new reserve need. Additional cover is needed for open ineligible advances and losses on resolved ineligible advances. A stable review queue does not bound this need when new losses continue. Under reliable settlement at the deadline, advances only for unresolved claims need no more end-period cash than advances at initial denial. The two rules have the same measured payment timeliness. In 567 synthetic cases, a reserve of 30 benefit units covers 396 initial-advance paths and 413 end-of-period-advance paths. These are design checks, not estimated success rates. The contribution is a limited payment-accounting test, not a new theory of administrative burden or queueing.

### 1. A payment right has an operating requirement

Consider a future economy in which AI can perform all paid tasks at lower cost than people. This is a conditional setting. The paper does not estimate its probability or date. Public transfers could become a main source of household purchasing power. A wrong denial could then remove income that a person cannot replace through work.

There are at least three separate requirements for a useful transfer. The public authority needs revenue. The economy needs available goods. The person needs access to the payment. This paper examines the third requirement, while holding the first two fixed. The companion study S004 examines fiscal capture and scarce essential goods. This study assumes that all eligible payments have funding when due. It does not establish that those payments are sufficient for a consumption floor.

The main question is operational: **which payment rule can meet a stated deadline with finite review capacity and finite additional cash?** A legal right to appeal does not itself answer this question. Neither does an aggregate error rate. Payment time depends on when errors occur, how claims reach review, and how funds move while review remains open.

The analysis uses three rules. Rule A pays an initially denied eligible claim after a correct review. Rule P pays every initially denied claim immediately, then recovers part of an ineligible payment after review. Rule J waits for the reviews available within the period, then pays every claim still open at that period end. Ineligible claims include mistakes and misunderstandings. Ineligibility is not evidence of fraud.

The comparison yields a conditional design choice. If the payment route works at the deadline, Rule J avoids some unnecessary advances without increasing end-period delay. If that route can fail, its dominance result does not apply. Earlier payment can then buy time for settlement failure. Such failures require a separate payment-network model.

### 2. What previous research already establishes

Benefit access is an established research field. Giannella, Homonoff, Rino, and Somerville report a large field experiment on SNAP interviews. Flexible interview access increased approval and participation. Their author abstract establishes a relevant mechanism: process design can affect receipt. We read that abstract, not the full working paper. We do not use its effect sizes as parameters. [B02](https://www.nber.org/papers/w31239)

Bennett, Currie, and Podoletz study automated Universal Credit through 44 participants. Their qualitative analysis identifies time, financial, and emotional costs. It also examines payment errors and attempts to resolve them. Their findings support attention to the delivery process. They do not supply a population error rate for this model. The article appeared online in 2024 and in a 2026 journal issue. [B03](https://www.cambridge.org/core/journals/journal-of-social-policy/article/universal-credit-administrative-burdens-of-automated-welfare/6304AF71E445EF4A97ED47C0413331B8)

The closest technical work is Daw, Pache, and Zhou's 2026 preprint on SNAP call centers. It models repeat calls, abandonment, and endogenous congestion. It connects service design with meaningful access. We read its introduction, related work, model, and operational comparison. We do not claim that queues cause access problems as a new result. Our queue is simpler: every disputed claim enters automatically and remains until review. The added object is a matched comparison of payment timing and public cash accounts. [B01](https://arxiv.org/html/2605.15165v1)

Anunrojwong, Iyer, and Manshadi model congested social services and users with different outside options. Their analysis already includes users who have no viable alternative. It studies information design and strategic entry. Our model instead fixes entry and compares payment rules after initial denial. [B05](https://arxiv.org/html/2005.07253v3)

Advances during review also predate this study. Vethaak and colleagues use Rotterdam application data from 2013–2019. They study processing time and benefit prepayments through caseworker variation. Their paper describes advances, later offsets, and outstanding claims after rejection. Its labor-market outcomes cannot be transferred to a setting without viable paid work. We use it to locate the institutional mechanism, not to claim that an advance rule is new. [B07](https://docs.iza.org/dp17839.pdf)

Official documents further limit the novelty claim. The World Bank links registries, payment systems, case management, and grievance channels. Integration is already a stated delivery-system objective. [B04](https://www.worldbank.org/en/brief/2025/09/19/digital-delivery-systems) A July 2026 DWP assessment describes machine-learning referrals for Universal Credit advances. It reports a one-day median additional delay for referred requests later approved. That report concerns a defined group and period; a median is not a maximum waiting-time guarantee. [B06](https://www.gov.uk/government/publications/effectiveness-assessment-including-statistical-analysis-of-the-universal-credit-advances-machine-learning-model-1-april-2025-to-31-march-2026/effectiveness-assessment-of-universal-credit-advances-model)

The bounded contribution is therefore a transparent accounting result. We separate eligible arrears, open ineligible advances, and permanent losses within the same finite review path. We then test two automatic-payment timings against an appeal-only rule. The searched sources do not establish this exact comparison. That observation does not prove universal novelty. The search was targeted, English-language, and incomplete.

### 3. Model, funding, and measurement

Time has periods \(t=1,\ldots,T\). Each eligible claim has amount \(b>0\). There are \(n_t\) eligible claims due in period \(t\). The initial system denies \(e_t\leq n_t\) of them. Another \(i_t\) claims are ineligible and initially denied. The other eligible claims receive payment without review. We exclude initially approved ineligible claims to isolate the effect of advancing denied claims.

All denied claims enter review automatically. Capacity is \(m_t\) claims per period. Review serves earlier arrival cohorts first. Within a cohort, it serves eligible and ineligible mass in proportion to their shares. This is a fluid model. Fractional claims represent group mass, not a partially adjudicated named person. Correct review is assumed. The authority does not know each claim's true type before review; the analyst uses that type for accounting.

Let \(Q^E_t\) and \(Q^I_t\) be eligible and ineligible claims still open after period \(t\). Let \(R^E_t,R^I_t\) be cumulative reviewed claims of each type. Let \(I_t=\sum_{s\leq t}i_s\). Conservation gives

\[
Q^E_t=\sum_{s\leq t}e_s-R^E_t,\qquad Q^I_t=I_t-R^I_t.
\]

The total queue follows

\[
Q_t=\max\{0,Q_{t-1}+e_t+i_t-m_t\}.
\]

An outage can increase denials and reduce capacity at the same time. No assumption of independent errors is needed. Capacity can represent computation, trusted evidence access, adjudication, or staff time. A post-labor setting does not require human reviewers to outperform AI. It still requires a process that can inspect disputed evidence and authorize changes.

The public authority receives \(b n_t\) when eligible payments become due. Review spending is separately funded. The same capacity cost applies under all three rules, so it cancels in the main comparison. This is a conditional, fully funded benchmark. It does not give administrators knowledge of true individual or total eligibility. Actual aggregate funding uncertainty needs a separate test. If only approved claims receive budget authority, a further appropriation rule is necessary.

Under Rules P and J, an eligible advance replaces the payment owed for that claim. It does not create a second payment or a deduction from a later, separate entitlement. A reviewed ineligible advance returns fraction \(r\in[0,1]\) of its amount immediately. The rest is a permanent public loss. Recovery cost, interest, collection delay, and hardship from recovery are absent. Thus the model does not select a socially optimal recovery rate.

We measure delay as

\[
D_A=\sum_{t=1}^{T}Q^E_t.
\]

Its unit is **eligible claim-periods awaiting payment**. If each person has one claim, this also counts person-periods of exposure to an unpaid entitlement. With repeated claims, it can count the same person more than once. It is not a count of unique people without food. A linear delay cost \(hD_A\) is possible, but \(h\) is not estimated here.

We also report claims first unpaid at their due date and claims still unpaid two periods later. The code parameter `deadline=2` controls this later measurement only. It does not defer Rule J payment for two periods: that payment occurs at the end of the arrival period. The latter outcome excludes late cohorts whose two-period deadline lies beyond the horizon. All terminal arrears remain in the accounts. A final payment can remove arrears without removing delay already experienced. Rules P and J have zero measured payment delay only when their required cash and payment routes are available.

### 4. Three payment rules and their cash accounts

Write \(F_t=b\sum_{s\leq t}n_s\) for cumulative eligible funding. Omit the common review budget in this section. Under Rule A, cumulative outflow is

\[
C^A_t=F_t-bQ^E_t.
\]

Thus \(bQ^E_t\) remains earmarked cash. Calling this amount a saving would confuse nonpayment with a lower obligation.

Under Rule P, cumulative net outflow is

\[
C^P_t=F_t+bI_t-rbR^I_t.
\]

**Proposition 1: exact additional cover.** Relative to fully funded eligible entitlements, Rule P requires

\[
L^P_t=C^P_t-F_t=bQ^I_t+b(1-r)R^I_t.\tag{1}
\]

Its spending difference from Rule A is

\[
C^P_t-C^A_t=bQ^E_t+L^P_t.\tag{2}
\]

**Proof.** Substitute \(I_t=Q^I_t+R^I_t\) in the Rule P outflow. Then subtract the Rule A outflow. No distributional or equilibrium assumption is needed. The result is an accounting identity. The important choice is the funding baseline. Equation (2) compares spending rules. Equation (1) measures additional cover beyond funding already owed to eligible claims.

A reserve \(K\), without new contributions, covers end-period cash exactly when

\[
K\geq\max_{t\leq T}L^P_t.\tag{3}
\]

With cumulative new contributions \(Z_t\), replace this with \(K+Z_t\geq L^P_t\) at each date. These are cash tests, not tests of sovereign solvency. They assume the authority can use the funds for their specified purpose.

For Rule J, let \(U_t\) be cumulative ineligible claims that were still open at their payment deadline and received advances. Let \(R^{I,J}_t\) count those advanced claims later reviewed. Ineligible claims resolved within their arrival period receive no advance. Every claim still open has an advance, so

\[
Q^I_t=U_t-R^{I,J}_t,\qquad
L^J_t=bQ^I_t+b(1-r)R^{I,J}_t.\tag{4}
\]

**Proposition 2: deadline timing weakly reduces cover.** Under reliable deadline payment and identical review paths,

\[
L^J_t\leq L^P_t
\]

at every period end. Both rules have zero measured eligible delay when funded.

**Proof.** The two rules have the same \(Q^I_t\). Reviewed ineligible claims that previously received an end-of-period advance form a subset of all reviewed ineligible claims. Therefore \(R^{I,J}_t\leq R^I_t\). Multiply by nonnegative \(b(1-r)\) and apply equations (1) and (4). Both rules pay eligible claims no later than the defined deadline.

This is a limited dominance result. It ignores welfare gains from receiving money before the period end. Equal payment by period end does not imply equal access within that period. It also assumes review results and payment instructions can be processed at that deadline. It does not recommend delaying emergency support until an arbitrary administrative date.

Cash-flow order matters. If advances must leave before the period's recoveries arrive, Rule P needs gross cover

\[
G^P_t=b(I_t-rR^I_{t-1}).
\]

For Rule J, a conservative corresponding order gives \(G^J_t=b(U_t-rR^{I,J}_{t-1})\). The code reports both peak net and peak gross cover. Net cover alone is sufficient only when the assumed settlement order permits the offset.

### 5. A stable queue can still exhaust a reserve

Consider constant arrivals of ten eligible denied claims and two ineligible claims per period. Set \(b=1\), \(r=1/2\), and capacity to twelve. The first period has zero capacity; each later period reviews the previous cohort. The queue then stays at twelve claims forever. Eligible arrears stay at ten. There is no growing review backlog.

Every current cohort remains open at its deadline. Both advance rules therefore pay its two ineligible claims. At the end of period \(t\), two ineligible claims remain open and \(2(t-1)\) advanced ineligible claims have completed review. Equations (1) and (4) yield

\[
L_t=2+\tfrac12[2(t-1)]=t+1.
\]

A reserve of thirty fails in period thirty, despite the constant queue. The required flow contribution is one benefit unit per period after the initial setup. A loan facility alone cannot absorb these losses indefinitely. General revenue, a loss budget, fewer ineligible advances, or a higher net recovery rate must change the arithmetic.

The counterexample also separates speed from loss. Faster review can reduce open advances. It cannot recover the unrecoverable share of advances already paid under the fixed recovery assumption. Once all such cases close, cumulative loss equals \(b(1-r)\) times their count. Queue stability and review accuracy are therefore insufficient conditions for a permanent payment guarantee.

The opposite boundary is equally useful. If no ineligible claims exist, additional reserve is zero even during a severe eligible-denial outage. The authority releases earmarked benefit cash. A large difference from appeal-only spending does not imply a new fiscal cost. This result fails if the authority spent the earmarked money elsewhere or never funded the entitlement when due.

### 6. Executed synthetic cases

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

### 7. What an economic governance plan should specify

First, state when the entitlement's funding becomes available. A budget based only on completed approvals can create an administrative incentive to delay. Under due-date funding, unpaid eligible balances should remain reserved for those entitlements. A payment dashboard should show those balances separately from freely available public cash.

Second, specify a payment deadline and a route that can meet it. A right to review needs an operating design for intake, evidence, decision, and payment. The guarantee in this paper starts after claims enter the system. It does not protect an eligible person who cannot register, lacks an accepted identity, or is removed before the queue exists. Independent intake and a way to correct identity records remain separate requirements.

Third, fund both temporary exposure and recurring losses. Report open ineligible advances, recovered amounts, and losses as separate stocks and flows. A falling queue can hide rising cumulative losses. A rising queue can also coexist with adequate payment access if advances are funded. Neither queue length nor cash alone is a complete performance measure.

Fourth, compare review investment with payment timing on the same cases. The relevant output is successful access by the due date, with a transparent loss account. A mean review time or classifier accuracy can miss a long tail. An appeal process must also remain meaningful after an advance. Payment does not resolve a disputed eligibility label or protect future claims by itself.

These points become more important if people have no earnings fallback. They do not imply unlimited unconditional payments to every submitted identifier. Claim authentication, eligibility rules, and duplicate prevention remain outside this model. The proposed guarantee concerns claims admitted to a specified review process. Its social value depends on who can reach that process.

### 8. Limits, checks, and next evidence

The model deliberately omits strategic applications, endogenous repeat contacts, review error, and group-specific barriers. It does not estimate claimant behavior after an advance rule changes. The number of ineligible claims could rise under easier payment. Recovery could itself create hardship or costly disputes. These omitted responses can change the preferred policy.

The fluid service rule hides within-cohort inequalities. Equal average shares do not prove equal treatment for named people. Recovery fractions are fixed and immediate. Real collections can have long delays. Borrowing cost and the opportunity cost of public funds are zero. Benefit amounts are equal, prices are fixed, and goods are available. No claim about aggregate consumption, inflation, or political feasibility follows.

The finite horizon also matters. Terminal arrears and open advances are retained, not forgiven. Eventual loss is reported only under eventual review with the stated recovery rate. It is not a forecast that the queue will actually clear. The two-period deadline statistic has right-censored late cohorts, while the delay statistic counts all observed unpaid exposure.

Twelve tests check boundaries, a hand-calculated ledger, conservation, settlement order, the stable-backlog counterexample, and the end-of-period-rule inequality. A separate scalar queue recurrence checks total backlog. A catch-up case verifies that zero final arrears do not erase earlier delay. Internal assertions also reconcile funds and claims at every date. These checks validate the stated model, not the realism of its assumptions.

An empirical extension would need dated claim arrivals, initial decisions, review completions, payment receipts, recoveries, and corrected eligibility. It would also need evidence on eligible people absent from administrative records. Without those data, a calibrated reserve recommendation would be false precision. A suitable pilot would compare payment rules on common service paths and measure both access and net public losses.

The result is a small but actionable restriction on policy claims. Fully funded entitlements can fail through delay. Automatic advances can remove that delay under clear operating conditions. Their extra funding need depends on the correct budget baseline and on losses, not only on review backlog.

### Disclosure and references

AI assisted with source search, model design, code, checking, and writing. No interviews, new human data collection, or human review were performed for this study. No affiliation, endorsement, funding source, or conflict status is asserted. The repository owner has not certified the conclusions. Independent checks remain necessary before policy use.

References B01–B07 appear beside their claims. Full titles, authors, versions, retrieval times, local capture hashes, short extracts, and rights notes are in `sources/manifest.csv` and `sources/snapshots/`. No source full text is distributed with this study. See [critical review](reviews/critical-review.md), [author response](reviews/author-response.md), and [completion gates](completion-gates.md). The study remains an AI-assisted draft.
