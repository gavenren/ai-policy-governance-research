# Who Can Rely on an International AI Dividend?
## Cooperation, payment promises, and income security after human labor

> **State:** Complete-study draft — analysis and separate internal AI review complete; no human peer review.
> **Study ID:** S009, `2026-10-11-international-dividend`. **Date:** 11 October 2026.
> **Evidence cutoff:** 2026-10-11T21:28:20Z for retained sources. Later reading and review use those captures unless recorded separately.
> **Method:** A repeated-game model and deterministic synthetic examples. No country calibration, forecast, or estimate of actual policy effects.
> **Disclosure:** Codex developed the study, wrote the text, and ran the analysis. No human peer review, affiliation, or endorsement is claimed. Human funding and conflicts were not supplied. No reuse licence has been selected.

### Abstract

A country may use advanced AI while its residents own little of the capital that produces it. International transfers could then support an income floor, but a promise to share future gains is not a secure income source. This paper studies one possible agreement between an AI provider country and a recipient country. The recipient provides an observable service that benefits the provider. The provider pays after that service has been supplied. Both countries can end the agreement. A simple test identifies the income floor that this arrangement can support in every modeled state. The relevant backing is the provider's future gain from continued cooperation, not its total AI wealth. The test also separates payment incentives from a domestic spending requirement. In an example with unchanged average gains, more persistent adverse states reduce the largest supported floor from 7.80 to 5.23 resource units. A financed deposit can restore a floor of six, but only within a bounded range. An excessive deposit can make continued participation unattractive. These results apply established contract theory to a specific question of post-labor income security. They support agreements that report their payment conditions, outside options, and failure provisions before households become dependent on them.

### 1. From a promise of shared gains to a dependable income

Consider two countries. One hosts a large share of productive AI capital. The other can buy AI services, but has few claims on the resulting profits. Suppose that competitive wages no longer provide a reliable income for most residents. This is a planning assumption throughout the paper. It is not a prediction that all employment will disappear, or a claim that current AI exposure measures establish such an outcome.

The two governments propose an agreement. The recipient country supplies a service that the provider values. For example, it could maintain agreed public infrastructure and provide verified incident information that improves safe international operation. The provider contributes to the recipient's income programme. The transfer covers the service's resource cost and part of the household income shortfall. The agreement repeats each year.

This arrangement has an attractive feature. It can give each government a reason to participate even when the provider gives little weight to foreign welfare. However, its payment sequence creates a problem. Once the recipient has supplied the year's service, the provider has received the benefit. It can save money by withholding the transfer. A household income programme built on that payment needs more protection than a statement that cooperation is beneficial on average.

The problem becomes more severe when the recipient has several difficult years in succession. Transfers may be largest when local income is low. Those same years may also reduce the provider's benefit from cooperation. Even if normal years make the agreement profitable in the long run, the provider can prefer to leave during a prolonged adverse state. The household floor then fails precisely when it is most needed.

This paper asks a limited question: what floor can the specified agreement sustain without a central authority that can compel the ordinary transfer? The answer depends on three separate conditions. The provider must prefer continued participation to exit. After receiving the current service, it must prefer payment to default. Its remaining current resources must also meet a stated domestic spending minimum. A low-cost, enforceable deposit can relax the payment constraint, but it creates a continuing financing burden and cannot be enlarged without limit.

The principal contribution is an explicit audit of those conditions for a state-dependent income floor. The analysis does not introduce a new theory of repeated games, international transfers, or escrow. It places a simple floor rule inside that existing theory and reports the resulting limits. The numerical examples show why total AI output, average treaty gains, and a large deposit can each give a misleading impression of payment security.

The distinction matters for economic governance. A discretionary foreign transfer can improve living standards even when it cannot support a dependable floor. A country can accept such a transfer while keeping it outside the budget for its most basic obligations. Conversely, an enforceable entitlement with independent funding can support a stronger promise. Policy should identify which of these arrangements it has actually created.

### 2. What previous work already provides

International distribution is already central to the economics of AI. Korinek and Stiglitz (2021) analyze how automation and concentrated digital rents can harm developing economies. Their discussion of global governance includes tax allocation, competition policy, intellectual property, and data. They emphasize that a tax-allocation formula can change distribution across countries. That work supplies the international context; it does not provide the recurring payment test used here. [S1]

Dennis and colleagues (2025) distinguish sharing AI resources, access to systems, and financial proceeds. Their report discusses transfers through governments, a multilateral fund, domestic political constraints, and the difficulty of credible international commitments. Thus neither a global AI fund nor concern about its reliability is a new proposal in this paper. The present study selects a narrow financial arrangement and makes its incentive conditions explicit. [S2]

The formal foundation is relational contract theory. Levin (2003) shows how the value of a continued relationship restricts promised compensation when payments cannot be fully enforced. The provider's payment constraint below is a direct application of this logic. Our simpler model removes hidden information and endogenous effort intensity. It adds an externally chosen household floor, a public spending requirement, and observable persistent states. These changes support a policy calculation; they do not establish a new general enforcement theorem. [S3]

International transfer timing also has close precedents. Kerr, Lippert, and Lou (2018) compare several payment sequences in a climate-cooperation model. Their preliminary working paper also studies a credible third party that receives funds before performance and pays after compliance. That comparison rules out a claim that this paper first identifies the value of precommitment or payment timing. Here the deposit remains a separate stock that supports a recurring transfer, and its financing cost enters the floor test. [S6]

AI-specific work likewise studies credible sharing commitments. Bova, Müller, and Harack (2021) model how a windfall clause changes firms' safety and participation incentives. Their implementation discussion distinguishes a desire to commit from the problem of honoring that commitment. The present model concerns repeated transfers between governments after production, rather than competition among firms before a transformative breakthrough. [S8]

Verification is a further, separate issue. Harack and colleagues (2025) discuss verifying international cash transfers and the financial information on which they might depend. This paper assumes that the relevant state, action, and payment are observable. That assumption permits an incentive analysis. It does not establish that a particular treaty could verify these facts cheaply or accurately. [S5]

The search was bounded. Six primary documents were retained, and relevant sections were read beyond their abstracts. Other candidates, including research on productivity shocks in relational contracts, were identified but not fully retrieved. The public source ledger records the successful captures and failed routes. The incremental claim is therefore modest: a reproducible application that joins a state-dependent income floor to participation, payment, and domestic-budget conditions. No claim of exhaustive literature coverage or universal originality follows from this search.

The study also differs from the earlier papers in this repository. The import-levy paper, S006, asks how a unilateral charge changes domestic resources. The present paper takes the gains from cooperation as inputs and asks whether a promised payment will occur. It does not calculate a tariff or describe the gains from a specific tax treaty. The public-capital paper, S008, examines how a government finances ownership. Here the deposit is collateral for a transfer promise and creates no new public net wealth at entry.

### 3. A simple agreement with an explicit failure outcome

The model contains a provider government and a recipient government. The recipient can also represent a group with one decision rule, although the model does not solve internal coalition problems. Time continues indefinitely. Each period has a publicly observed state. A transition matrix gives the probability of next period's state conditional on the current state. These probabilities are model inputs, not estimated probabilities of actual AI futures.

The recipient has population $n$ and existing household-support resources $y_s$ in state $s$. Those resources continue if the agreement ends. A proposed floor $f$ requires aggregate support of at least $nf$. The recipient's service costs $c_s$. This is an incremental resource cost of cooperation. It is not a wage paid to households and must not be counted as household support.

The provider obtains an incremental gain $K_s$ when the recipient supplies the service. The provider also has outside resources $A_s$, which it retains without the agreement. These can include AI profits, tax revenue, or other income. The distinction between $K_s$ and $A_s$ is essential. Losing the agreement removes $K_s$; it does not remove the provider's entire economy.

The smallest transfer that pays for the service and meets the household floor is

$$
T_s(f)=c_s+\max\{0,nf-y_s\}. \tag{1}
$$

After paying the service cost, recipient resources equal the larger of existing support and the proposed floor. Existing income above the floor is not taken away. The model assumes that the recipient government passes the remaining transfer to households. It does not model corruption, benefit administration, prices of scarce goods, or differences in need within the population. A national aggregate floor is not sufficient evidence of individual access.

The period has a fixed order. First, the state is observed and the provider decides whether to continue. Second, the recipient supplies the agreed service. Third, the provider chooses whether to pay. The provider's government values its own net fiscal resources linearly and discounts next period by $\delta$, with $0\leq\delta<1$. The recipient also values additional resources and has no gain from receiving less support. It can afford the service's initial resource use; short-term recipient liquidity is outside the model.

After any deviation, the parties stop cooperating permanently. The recipient supplies no service and the provider pays nothing. This is a credible continuation in the specified stage game. Without a binding promise or future cooperation, the provider gains nothing by sending a gift. Anticipating no payment, a recipient with a positive service cost does not supply the service. Neither can improve its payoff through a unilateral change. If the service cost is zero, withholding remains a weak best response.

This punishment does not require the recipient to destroy its own existing income or surrender its basic rights. It simply stops an additional service whose cost is no longer covered. Still, the assumption has limits. If the service gives the recipient large independent benefits, it might continue after default. Then the provider would lose less than the stated $K_s$. If the parties expect to restart the agreement immediately, permanent termination is also not a suitable description. The model establishes an equilibrium under the stated continuation; it does not establish resistance to renegotiation.

The compliant treaty budget must leave the provider with at least $M_s$ for domestic spending each period. This is an imposed design requirement, not a legal priority over the lender. Exit or debt repayment after default can leave domestic resources below that amount. These actions remain available in the model. The requirement is not derived from an election model. A treaty can meet the government's long-run participation condition and still fail this current spending test.

There is no assumption that the provider's preferences settle the moral question. The model deliberately asks what a government motivated by its own fiscal return will honor. A government that values foreign welfare directly could support larger transfers. Such a preference would need to enter the model explicitly and remain credible after a political change.

### 4. The income floor depends on what exit would cost

For a proposed floor, first calculate the provider's net gain in every state: the cooperation benefit minus the required transfer. Then calculate the discounted value of those gains, starting from each state. Call this vector $V$. With no deposit,

$$
V=K-T(f)+\delta PV.
$$

The calculation has an ordinary interpretation. Today's value equals today's net gain plus the discounted value of the possible states tomorrow. Because the discount factor is below one, the associated linear system has a unique solution.

The payment decision comes after the provider has received the service. Paying gives up $T_s$ and preserves future cooperation. Withholding keeps that amount but ends the relationship. Thus the current transfer must not exceed the future value that payment preserves. The complete test is

$$
V_s\geq0,\qquad T_s(f)\leq\delta(PV)_s,
\qquad A_s+K_s-T_s(f)\geq M_s
\quad\text{for every state }s. \tag{2}
$$

**Proposition 1.** Within the specified stationary agreement and termination rule, a floor is feasible if and only if (2) holds for its minimum transfer schedule. A larger transfer in any state cannot rescue a floor that fails this test.

The second statement is useful in practice. A negotiator might try to repair an unreliable promise by increasing the headline transfer. That action raises the amount that can be saved by default. It also reduces the provider's future net return. It therefore makes both sides of the payment comparison less favorable. In this model, a failed floor requires a change in enforcement, cooperation benefits, costs, or the floor itself.

The result concerns a particular agreement class. It does not exclude a different timing of payment, an enforceable entitlement, a history-dependent schedule, a temporary punishment, or a different package of reciprocal benefits. Nor does it claim that the largest feasible floor is the best social choice. Feasibility says that the specified governments can follow the agreement. Welfare assessment also requires the distribution and value of its benefits and costs.

An immediate implication concerns AI wealth. Raising outside resources $A_s$ can ease the domestic spending condition. It leaves the payment incentive unchanged if it also leaves cooperation gains and preferences unchanged. The provider keeps those additional resources after default. They are therefore not part of the stake at risk. A statement that an AI-rich country could easily afford a dividend does not establish that recipients can rely on it.

This distinction also clarifies the role of market power. A recipient may initially offer a valuable service or access arrangement. If the provider later develops a cheap substitute, the income it loses on exit falls. The provider can become richer while its promise becomes less secure. The model does not estimate that process, but it identifies the quantity that a review of the agreement should monitor: the incremental value of continued cooperation relative to the available alternative.

### 5. A long adverse period can defeat a profitable agreement

A two-state example makes the payment problem concrete. The states are normal and adverse. The population is one unit. Existing support is four units in the normal state and zero in the adverse state. The recipient's service costs one in either state. A floor of six therefore requires a transfer of three in the normal state and seven in the adverse state.

The provider gains 12 from cooperation in the normal state and six in the adverse state. Its net gain after payment is therefore nine or minus one. It also has 20 units of outside resources and must retain 15 for domestic spending. The discount factor is 0.8. All numbers are synthetic. The period is not calibrated to a year, and the discount factor does not estimate a government's actual patience.

Suppose that next period is equally likely to be normal or adverse, regardless of the current state. The provider then receives an average net gain of four each period. Its expected value before next period's state is known is 20. The discounted future value protected by the current payment is 16. Both transfers, three and seven, are below that amount. The domestic spending rule also holds. The agreement can support the floor of six.

Now change only persistence. Each state has a 95 percent chance of continuing into the next period. The long-run frequency of each state remains one half. The average cooperation gain, transfer, and net gain are therefore unchanged. What changes is the meaning of being in the adverse state today. It now predicts a long interval with little benefit to the provider and a large payment obligation.

Starting from the adverse state, the provider's value falls to 2.143 units. It still prefers participation to immediate exit. However, the future value protected by paying this period is only 3.143. The transfer due is seven. After receiving the service, the provider gains 3.857 by withholding the payment and ending cooperation. Average profitability and initial willingness to participate have not protected the current payment.

The largest floor supported without a deposit falls from 7.80 with independent states to 5.229 with persistent states. Multiplying outside resources by ten leaves the latter result unchanged. Increasing the cooperation benefit by three in each state raises it to 7.629. These comparisons hold the stated domestic rule fixed and isolate the stake that termination removes.

| Synthetic agreement | Largest supported floor | Is a floor of six feasible? |
| --- | ---: | --- |
| Independent states | 7.800 | Yes |
| State persistence of 0.95 | 5.229 | No |
| Same persistence; outside resources rise from 20 to 200 | 5.229 | No |
| Same persistence; cooperation gain rises by three in each state | 7.629 | Yes |
| Same persistence; low-cost deposit available | 6.143 | Yes |
| Same persistence; high-cost deposit available | 5.229 | No |

The comparison is not a claim that persistence always reduces cooperation. It does so here because the adverse state combines a larger transfer with a lower provider gain. Other state patterns can have different effects. A recipient with high needs might provide a service that becomes especially valuable in a crisis. That positive link could support larger payments. The correct analysis uses conditional future gains, rather than treating all volatility as harmful.

There is also no contradiction between the result and risk sharing. The proposed floor transfers more resources to the recipient when its own support is low. It does provide insurance on the intended path. The question is whether the paying government will continue to supply that insurance. If the gains that support cooperation weaken in those same states, the promise needs an additional source of commitment.

### 6. What a deposit can and cannot secure

Suppose that an independent trustee can seize a fixed deposit $B$ after a verified payment default. The deposit is posted before the recipient acts and cannot be removed during the period. It remains the provider's asset during compliance. If the provider ends the agreement before the next service is supplied, the trustee returns it.

To make the financing explicit, the model assumes that the provider borrows the deposit principal. The loan and the deposit enter together. Posting the deposit creates no net public wealth. On an orderly exit, the returned principal repays the loan. After payment default, the trustee transfers the deposit to the recipient, but the provider must still repay its lender. The model assumes that this debt can be enforced and repaid. It does not allow the provider to default on the loan as a second escape route.

Maintaining the arrangement costs $rB$ each period. This can include interest, a net funding spread, and an administration charge. The model treats their sum as a fiscal cost to the provider. It does not count the principal as a recurring expense. It also does not treat every financing payment as a global resource loss. Interest received by a lender is income to someone else; real administration costs and forgone production require separate welfare accounting.

These assumptions give the deposit real force. They also make the extension partly dependent on external enforcement. Calling a trustee independent does not establish that a powerful government could not block seizure. The positive result below is conditional on that commitment technology, the lender's claim, and sufficient repayment capacity. The examples cap the deposit at 12, below the provider's 20 units of outside resources.

Let $V^0$ be the provider's value without deposit costs for the same floor. The financed deposit reduces value in every state by $rB/(1-\delta)$. It also makes default immediately cost $B$. Consequently the change in each payment-enforcement margin is

$$
B\left(1-\frac{\delta r}{1-\delta}\right). \tag{3}
$$

**Proposition 2.** A deposit improves the payment constraint only when its marginal enforcement value in (3) is positive. Even then, its size is bounded by participation, domestic spending, and the available borrowing or collateral limit. Feasibility requires an overlap between the minimum effective deposit and all three upper bounds.

The direct benefit of a larger deposit is clear: withholding payment becomes more costly. The offset is less visible. The provider must pay to maintain the deposit in every future period of cooperation. This reduces the value of staying. A large financed deposit can therefore strengthen the immediate penalty while weakening the relationship that also supports compliance.

Return to the persistent-state example. With a carrying cost of 0.05 per unit of deposit per period, the marginal enforcement effect is 0.8. A floor of six requires at least 4.821 units of deposit. Participation limits the deposit to 8.571. The domestic rule and the cap of 12 are looser. Any deposit inside the resulting interval supports the specified floor. At the lower bound, the adverse-state payment constraint holds exactly.

A deposit of 12 does not work in this case, despite exceeding the required minimum. Its continuing cost makes the provider prefer orderly exit in the adverse state. The agreement can fail before the recipient supplies its service. This is a participation failure rather than a later payment default. The distinction matters because the intended household support disappears in either case, while the deposit is returned on orderly exit.

If the carrying cost rises to 0.30, the marginal enforcement effect becomes minus 0.2. Every additional unit of deposit reduces the payment margin. The best deposit for the floor test is then zero. The availability of a costly deposit does not lower the attainable floor if using it remains optional; requiring one can lower the floor.

For $\delta>0$, the break-even carrying cost is $(1-\delta)/\delta$. At $\delta=0$, a deposit raises the payment margin by its full amount, while current participation and spending conditions can still bind. This is an algebraic condition for the modeled fiscal objective. It is not a market estimate. In particular, the government's effective discount factor need not equal the discount factor implied by the loan's interest rate. If they do satisfy that equality and carrying cost consists only of that interest, the deposit's marginal enforcement effect is zero. The funding arrangement should therefore be stated before a policy analysis assigns a free enforcement benefit to collateral.

A deposit also does not finance a permanent floor after default. It provides a one-time payment and changes incentives before default. A separate reserve, asset endowment, or continuing revenue claim would be needed to support households after the relationship ends. The model should not be read as turning one finite stock into an unlimited stream of benefits.

### 7. Numerical design and checks

The calculation uses two transparent steps. First, it solves the provider's linear value equations. Second, it intersects the lower and upper bounds on the deposit. A proposed floor passes only when every state's participation, payment, and domestic-budget conditions hold. The minimum-transfer schedule makes the feasible set decrease as the floor rises. A 75-step bisection therefore identifies its upper boundary to a precision much greater than the reported decimals require.

The main grid contains 648 parameter cases. It varies the discount factor, state persistence, adverse-state cooperation benefit, domestic spending minimum, deposit cap, and carrying cost. The population, recipient resources, normal-state gain, service costs, and target floor remain fixed. Some cases have the same effective outcome, including different carrying-cost labels when the deposit cap is zero. These are parameter combinations, not independent observations or sampled countries.

A floor of six is feasible in 292 cases. In 356 cases the provider has a positive average net gain before deposit costs, but the target still fails. In 108 cases, the agreement is infeasible even at a zero household floor. That last result does not mean that domestic household support vanishes. It means that the specified service and payment agreement cannot satisfy all conditions, including reimbursement of its cost and the provider's spending minimum.

The counts describe the published grid only. They are not estimates of the probability that real agreements will succeed. The chosen ranges deliberately include strong and weak cooperation benefits, high and low persistence, and cheap and costly deposits. Different ranges would change the counts. The mechanism is carried by the equations and named counterexamples, not by a percentage of arbitrarily selected cases.

The release also includes 101 persistence cases, nine named scenarios, and state-level values for the named policies. All inputs are synthetic and published in `data/design.json`. No hidden calibration, survey, administrative record, or claim of observed behavior is involved. The analysis runs offline with the Python standard library.

Twelve tests cover the single-state enforcement bound, hand calculations for the two main cases, outside-wealth invariance, deposit accounting, costly deposits, monotonicity in the floor, and invalid inputs. An independently specified value iteration checks 100 seeded parameter sets against the linear solver. Direct evaluation of 1,201 deposit sizes in each of 27 cases checks the computed deposit intervals. Those are author checks of the implemented model. The separate AI review also reproduced the outputs and checked all 648 target cases with independent exact arithmetic. Its scope and limits are recorded in the review files.

### 8. Implications for economic governance

The results suggest a useful distinction between an international dividend and an international income guarantee. A dividend can vary with profits, political support, or annual negotiations. It can be valuable without being safe to use for essential recurring spending. A guarantee needs a clear account of which institution must pay, what happens when payment fails, and how households remain supported through that failure.

A provider's first promise should therefore be accompanied by an account of its outside option. What income, access, information, or other benefit would it lose if it stopped paying? Which part of that loss can the recipient actually cause by ending cooperation? A global revenue projection does not answer either question. The loss must follow from a credible response and remain relevant after the recipient has supplied the current service.

This approach should not encourage governments to make basic human needs bargaining instruments. The recipient's modeled response is to stop an additional service, not to expose its population to harm. Real agreements can contain duties that remain binding after a financial dispute. They can also produce public benefits that a recipient should continue for ethical or practical reasons. Those benefits cannot automatically be counted as punishments available to enforce payment.

The second implication is to review the agreement in adverse states. A treaty with unchanged annual average value may become less secure when disruptions last longer. A finance ministry should distinguish a temporary shortfall from a persistent loss of cooperation surplus. The first can sometimes be managed with reserves. The second changes the incentive to continue and may require a different agreement or a stronger independent funding claim.

The third implication concerns the form of commitment. A protected payment reserve, an enforceable claim on receipts, and a default deposit solve different problems. A reserve can make cash available but does not alone make a government willing to release it. A claim on receipts may change who owns the funds, but its strength depends on the legal and operational control of those receipts. A deposit changes the cost of default, but its funding burden and repayment terms still matter. No instrument should be assessed by its name alone.

The fourth implication is distributive. A system based only on reciprocal advantage can exclude people whose governments offer little that a provider values. Their need can be large while their bargaining stake is small. Pooling recipients can increase the benefits at stake, but it also adds coordination problems and does not automatically distribute proceeds fairly within the group. This bilateral model cannot establish the stability or justice of such a coalition.

A needs-based global floor may therefore require more than voluntary exchange. Possible complements include grants supported by durable political commitments, public ownership with international beneficiaries, or institutions that give recipients enforceable claims. This paper does not rank those alternatives. Its result identifies when the chosen reciprocal arrangement is insufficient and shows which assumption an alternative must change.

The provider's domestic constraint also deserves public examination. The model takes a protected spending minimum as an input. A very high minimum can block transfers even when the provider has substantial income. That does not make the constraint morally authoritative. It identifies a domestic distributional choice that an international promise cannot silently ignore. A fuller political model would ask whose consumption is protected and who bears the cost of honoring the agreement.

Finally, a feasible agreement can still be undesirable. The cooperation service might have harmful security effects, burden vulnerable groups, or increase dependence on a single provider. Payments might go to a government that does not deliver household support. The aggregate fiscal test cannot resolve these concerns. It should form one part of evaluation, alongside rights, safety, public participation, and evidence on delivery.

### 9. Limits and evidence that could change the result

The strongest limitation is the fixed agreement class. Transfers depend on the current state, and default leads to permanent noncooperation. More flexible contracts can use payment history, reserves, delayed obligations, alternative reciprocal services, or different punishments. The maximum floor reported here is the maximum within the stated design. It is not the maximum attainable through every possible international institution.

The state process is also external. In practice, investment, migration, tax policy, competition, and AI deployment can change both countries' resources and outside options. The model can accept a different transition matrix, but it does not explain how that matrix arises. The persistence example is a controlled comparison of mechanisms, not evidence that adverse states will become more persistent after AI displaces labor.

Perfect observation removes a major source of dispute. A government could misreport need, service performance, revenue, or compliance. Verification can be costly, incomplete, or politically contested. Mistakenly treating a compliant payment as default could destroy a useful agreement. The trustee in the deposit extension must also act reliably. These problems would generally require a larger model and could weaken the simple feasibility result.

Government fiscal payoffs are not full social welfare. Households can be risk averse and have sharply different needs. The provider may value recipient welfare, security, migration, or diplomatic standing in ways not captured by fiscal gains. Those values can be included in an extended payoff, but they should not be invented to make a proposed agreement pass. Financing payments should also be traced to their recipients before any claim about global resource loss is made.

Several observations could change a practical assessment. Evidence that the provider can replace the recipient's service cheaply would reduce the estimated gain at risk. Evidence of a genuinely independent revenue claim would weaken the relevance of discretionary-payment constraints. A history of prompt restoration after default would challenge the permanent-termination assumption. Reliable evidence that a government values the recipient's floor directly could support a larger transfer than this narrow fiscal model permits.

The next empirical step would be to study a specific proposed agreement with public documentation. That study would need a credible outside-option comparison, an identified payment authority, financing terms, a verification process, and household delivery data. It should estimate uncertainty in these inputs and test the agreement across plausible states. The present draft supplies an inspectable starting calculation; it does not substitute synthetic values for that work.

### 10. Conclusion

An international AI dividend can provide useful income while remaining a weak basis for an essential spending promise. In the agreement studied here, payment depends on the future cooperation value that the provider would lose after default. Average gains and total AI wealth do not measure that value. Persistent high-need states can defeat an otherwise profitable arrangement. A financed deposit can help, but only when its deterrent effect exceeds its continuing cost and the provider still prefers to participate. A credible post-labor floor therefore requires explicit payment rules, realistic outside options, and support that survives the failure of the underlying bargain.

### Appendix A. Feasibility proof

Let $P$ be a finite stochastic matrix and let $d=\delta<1$. For a fixed floor and deposit, define $g=K-T-rB\mathbf{1}$. The unique provider value is

$$V=(I-dP)^{-1}g=\sum_{j=0}^{\infty}d^jP^jg.$$

The inverse is entrywise nonnegative. The provider can exit before the period and settle the matched loan and deposit at zero incremental value. Participation therefore requires $V_s\geq0$. After the service, compliance gives $K_s-T_s-rB+d(PV)_s$. Default gives $K_s-rB-B$: the deposit is seized and the lender is repaid. The difference is $B+d(PV)_s-T_s$. Thus payment requires that difference to be nonnegative. The domestic rule requires $A_s+K_s-T_s-rB\geq M_s$.

The recipient receives $T_s-c_s\geq0$ from supplying the service and obtains nonnegative continuation gains. A refusal to supply it yields no transfer and ends the relationship. Therefore its action is a best response. The zero-service, zero-transfer continuation is a stage-game equilibrium. Together these conditions support the stated strategies after every history. Conversely, failure of any provider condition gives an allowed deviation or violates the imposed budget rule.

Suppose another stationary schedule pays at least the floor and reimburses the service. It has $\widetilde T\geq T$. Nonnegativity of the inverse implies $\widetilde V\leq V$. Both the payment margins and domestic margins weakly fall. Therefore the minimum schedule is sufficient to test existence in this class. At $B=0$, these conditions give Proposition 1.

### Appendix B. Deposit bounds

For the same floor, let $V^0=(I-dP)^{-1}(K-T)$. Since $P\mathbf{1}=\mathbf{1}$,

$$V(B)=V^0-\frac{rB}{1-d}\mathbf{1}.$$

Write $m_s^0=d(PV^0)_s-T_s$ and $h=1-dr/(1-d)$. Deposit feasibility is exactly

$$0\leq B\leq\bar B,\quad V_s^0-\frac{rB}{1-d}\geq0,
\quad m_s^0+hB\geq0,
\quad A_s+K_s-T_s-M_s-rB\geq0.$$

All bounds are affine. If $h>0$, payment gives lower bounds $B\geq-m_s^0/h$. With $r>0$, participation gives upper bounds $B\leq(1-d)V_s^0/r$, and domestic spending gives upper bounds $B\leq(A_s+K_s-T_s-M_s)/r$. Their intersection with $[0,\bar B]$ is the reported interval. If $h<0$, payment instead gives an upper bound and cannot repair a failed zero-deposit payment condition. The code handles $r=0$ and $h=0$ without division by zero.

### Appendix C. Two-state calculation

For symmetric persistence $q$, write the normal and adverse net gains as $g_N$ and $g_A$. Their mean is $\bar g=(g_N+g_A)/2$. Without a deposit,

$$V_A=\frac{\bar g}{1-d}-\frac{g_N-g_A}{2[1-d(2q-1)]}.$$

At the target floor six, $g_N=9$, $g_A=-1$, and $d=4/5$. At $q=1/2$, $V_A=15$. At $q=19/20$, $V_A=15/7$. The adverse payment margin equals $V_A-K_A$ without a deposit, giving $15/7-6=-27/7$. In the relevant range $f\geq4$, both transfers rise one for one with the floor. The adverse margin falls by $1/(1-d)=5$ per unit of floor. Its zero occurs at $f=183/35=5.228571\ldots$.

With $r=1/20$, the deposit effect is $4/5$. The minimum deposit at floor six is $(27/7)/(4/5)=135/28$. Participation gives the upper bound $(1/5)(15/7)/(1/20)=60/7$. These exact fractions provide independent hand checks of the main numerical results.

### References

- **[S1]** Korinek, Anton, and Joseph E. Stiglitz. 2021. [*Artificial Intelligence, Globalization, and Strategies for Economic Development*](https://www.nber.org/papers/w28453). NBER Working Paper 28453. February version.
- **[S2]** Dennis, Claire, Sam Manning, Stephen Clare, Boxi Wu, Jake Okechukwu Effoduh, Chinasa T. Okolo, Lennart Heim, and Katya Klinova. 2025. [*Options and Motivations for International AI Benefit Sharing*](https://cdn.governance.ai/Options_and_Motivations_for_International_AI_Benefit_Sharing.pdf). Centre for the Governance of AI.
- **[S3]** Levin, Jonathan. 2003. [“Relational Incentive Contracts.”](https://web.stanford.edu/~jdlevin/Papers/RIC.pdf) *American Economic Review* 93(3): 835–857.
- **[S5]** Harack, Ben, Robert F. Trager, Anka Reuel, David Manheim, Miles Brundage, and coauthors. 2025. [*Verification for International AI Governance*](https://aigi.ox.ac.uk/wp-content/uploads/2025/07/Verification_for_International_AI_Governance.pdf). Oxford Martin AI Governance Initiative. Section 4.2.3.1.
- **[S6]** Kerr, Suzi, Steffen Lippert, and Edmund Lou. 2018. [*Financial Transfers, Compliance Technology and Climate Cooperation*](https://www.biz.uiowa.edu/saet/wp-content/uploads/sites/18/gravity_forms/1-0eb242c25464f1b25dc5136cf190c7a3/2018/02/FinTransClimate_006c.pdf). Preliminary and incomplete working paper, February 16.
- **[S8]** Bova, Paolo, Jonas Emanuel Müller, and Benjamin Harack. 2021. [*Safe Transformative AI via a Windfall Clause*](https://arxiv.org/abs/2108.09404v2). arXiv:2108.09404v2, August 28.

Source numbers S4 and S7 identify failed acquisition routes in the manifest. They are not used as substantive evidence. Code, row-level results, source provenance, and review records accompany this manuscript.
