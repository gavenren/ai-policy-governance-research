# Allocating a Universal Compute Floor
## Demand limits, budget changes, and the meaning of priority

**State:** Complete-study draft. **Study:** S014. **Date:** 12 October 2026. This technical comment passed separate AI critical review and release checks. It has not received human or journal peer review. The analysis concerns a pinned proposal, not an operating public compute system.

**Evidence cutoff:** 2026-10-12T17:32:18.596817Z. This is the completion time of the retained source and version-context captures, not a claim to all literature published by that time.

**Release source check:** On 12 October 2026 at 17:44:39 UTC, the target PDF still matched the retained v2 bytes. The latest-version endpoint returned the same record. This later check does not extend the literature search cutoff.

## Abstract

A public compute guarantee could give people access to AI when wages no longer provide a reliable claim on production. Its allocation rule must nevertheless specify what people receive and how their claims change when capacity changes. This comment examines the rule in version 2 of Galipeau's *Universal Basic Compute Under a Joule Ceiling*. The rule exhausts a positive budget and preserves relative priority for fixed demands. Its worked example also reproduces. Three qualifications matter. An award can exceed declared demand even when total demand exceeds supply. The stated floor rule leaves capacity unassigned when all residual demands vanish. Finally, allocating a budget in stages after updating claims can produce different awards from allocating it once. The last result is already established in the claims literature; it should not be imported as a favorable property of the compute rule. An existing capped weighted proportional rule supplies a demand-bounded alternative, but changes the meaning of fulfillment priority and does not remove the composition problem. These are limited corrections with a practical implication: a compute guarantee needs an explicit account of demand, unused capacity, and the treatment of prior awards.

## 1. What a compute guarantee promises

Suppose AI becomes cheaper than human labor across the work needed to produce goods and services. A household might then need a claim on production that does not depend on selling its labor. Cash transfers and public ownership are familiar responses. A public compute entitlement offers another route: people could use AI directly or authorize an institution to use it for them. This paper takes that economic condition as a scenario. It does not predict when or whether it will occur.

The appeal of a compute entitlement does not settle its design. An authority could guarantee a basic amount to each resident, set a total capacity limit, and distribute the remainder according to public priorities. But a formula needs more than a budget identity. Does a request state the most a user can employ, or a score that determines a tradable right? If capacity arrives in two installments, should the second allocation use the original request or the unmet part? If every request has been met, must the authority still assign all remaining capacity?

These questions arise in a concrete proposal. Galipeau's July 2026 preprint reserves a universal floor and divides the remaining compute in proportion to weighted demands [C1, sections 3–5]. This comment checks a small set of its formal claims. It preserves the valid budget calculation and example, identifies conditions under which other claims need qualification, and applies an established capped alternative. It does not evaluate the proposed energy standard, the selection of political weights, or the merits of compute instead of cash.

## 2. Contribution, sources, and method

This is a version-specific correction, not a new allocation theorem. In the claims literature, an award is normally bounded by the claimant's claim. Thomson's 2006 working paper explicitly defines capped weighted proportional awards and gives examples showing failure of both standard composition properties [C2, PDF pp. 8–10 and 14]. Harless's accepted manuscript separates budget additivity from composition and places the capped formula in a broader family [C3, PDF pp. 6–9]. Those results already establish the central mathematical distinctions used here.

The contribution is to apply them to an inspectable compute proposal, state the relevant domains, and show the policy meaning of each difference. The source's Section 3.3 invokes inherited allocation properties without spelling out those distinctions. The present analysis asks whether that transfer is valid. It is separate from this programme's income-redistribution audit, S012: the object here is a rationed service entitlement and the revision of its claims.

The target is Zenodo record 21305645, version 2, published on 11 July 2026. We read its full 16-page PDF and the relevant portions of the two primary allocation papers. At the recorded version check, the Zenodo latest-version endpoint returned that same record. One author page links the July version; another labels the title August 2026 without supplying a distinct revision there. We therefore pin the actual PDF and do not claim to have ruled out every version at every venue. The source ledger and search log record this conflict and the exact capture times.

Hand calculations found the candidate issues before the protocol was written. The later software plan was recorded before execution. We use exact rational arithmetic to reproduce the source example, test selected counterexamples, and enumerate 486 two-claimant cases. The enumeration checks implementation over a specified finite set; its counts do not estimate how often a public compute system would encounter a problem. The examples are illustrative, with no observations of users, task quality, or actual energy use.

## 3. A budget limit is not a demand limit

Let total capacity be $C>0$, demands be $D_i>0$, and positive priority weights be $w_i$. Normalizing weights to sum to one is convenient but does not change awards. The source's base rule is

$$
R_i(D,w,C)=C\frac{w_iD_i}{\sum_j w_jD_j}.
$$

The sum of awards is exactly $C$. For fixed demands, the award also changes in direct proportion to the budget. These results follow by summing or scaling the expression. The fulfillment ratio is $R_i/D_i=\lambda w_i$, where $\lambda=C/\sum_jw_jD_j$. Thus, before any cap is imposed, the ratio between two fulfillment rates equals the ratio between their weights [C1, Propositions 1–3].

A different condition is needed if declared demand is the largest useful award. Consider two claimants asking for 1 and 9 units. Their weights are 9/10 and 1/10. The weighted demands are equal, so a budget of 5 gives each claimant 2.5 units. Total demand is 10, twice the available budget. Yet the first claimant receives more than its request while the second remains below its request.

There is no violation of the total capacity limit. The problem is with a demand-bounded interpretation of the award. Write $W=\sum_iw_iD_i$. Since each demand is positive, $R_i\leq D_i$ holds exactly when $Cw_i\leq W$. All demand limits therefore hold if and only if

$$
C\leq \frac{W}{\max_i w_i}.
$$

This condition can fail even when $C\leq\sum_iD_i$. With equal weights it reduces to that familiar aggregate condition. Unequal weights create the difference.

The interpretation matters. The source permits pooling and delegation of floor entitlements and discusses exchange [C1, pp. 2, 4 and 8–10]. If awards are transferable rights, receiving more than one's own use does not necessarily strand capacity. A recipient might transfer the right to another user. But demand then cannot simultaneously be treated as an upper bound on the recipient's entitlement. The rule may still be usable; it promises a different object. We do not infer wasted energy from a mathematical award above declared demand.

## 4. What happens after every residual request is met?

The floor version gives claimant $i$ an unconditional amount $U_i\geq0$. Let $U=\sum_iU_i$, and let residual demand be $d_i=\max(D_i-U_i,0)$. The source applies the base rule to the residual budget $C-U$, then adds the floors. It also says to set the residual term to zero if all weighted residual demand vanishes [C1, Equation 4].

That convention requires a small correction to the exhaustion statement in Proposition 5. Suppose two people each have a floor of 1 and a total demand of 1. Capacity is 3. Both residual demands are zero, so the rule awards the two floors and leaves 1 unit unassigned. The floors fit within capacity, but the awards do not exhaust it.

For the formula as written, floor protection and budget exhaustion hold together when $U\leq C$ and either some residual demand is positive or $U=C$. When residual demand is positive, summing the residual term gives $C-U$. When it is zero, the sum is simply $U$. If $U>C$, no allocation can both protect every floor and stay within the total capacity limit.

This is a boundary qualification. The source motivates its scheme through aggregate scarcity. If the intended domain is restricted to $U_i\leq D_i$ and $\sum_iD_i>C$, then positive residual demand follows whenever the floor is feasible. The source's usual shortage example is unaffected. A policy or implementation should either state that restricted domain or define what it does with surplus capacity. A rule that admits zero residual demand should not promise exhaustion without that additional condition.

## 5. Allocating in stages can change the result

A budget can change without a rule becoming inconsistent in every sense. Three distinct questions are often grouped together.

First, suppose some claimants leave with their awards. If the remaining claimants divide the remaining budget using their original claims and weights, do their awards change? For the raw formula, they do not. Both the remaining budget and the denominator shrink in the same proportion. This is subset consistency.

Second, suppose the authority splits a precommitted budget into installments but uses the same original demands for every installment. The awards add to the one-stage result, because the raw rule is linear in the budget. This is unchanged-claim budget additivity.

Third, suppose the authority updates claims between stages. This is the setting of the standard composition properties. Composition up subtracts the first awards from the original claims before distributing the remaining budget. Composition down treats the larger-budget awards as new claims after the budget is reduced. Harless distinguishes these conditions explicitly [C3, PDF p. 7, footnote 16]. They need not follow from either of the first two properties.

A small example shows the difference. Two users each request 2 units, with weights 2/3 and 1/3. A direct allocation of 2 units gives awards of 4/3 and 2/3.

For composition down, reduce the budget to 1 and treat those awards as the new claims. The result is 4/5 and 1/5. A direct allocation of 1 from the original requests would instead give 2/3 and 1/3.

For composition up, first allocate 1 unit. The awards are 2/3 and 1/3, leaving unmet claims of 4/3 and 5/3. The next unit gives awards of 8/13 and 5/13. Total awards become 50/39 and 28/39, rather than the direct awards of 52/39 and 26/39.

Every intermediate award in this example respects the relevant demand limit. The difference is not caused by over-allocation. It also survives the capped alternative below because none of those caps binds. Unequal weighted proportional rules failing composition is an established result [C2, PDF p. 14]. The correction is to the assertion that the compute proposal inherits composition, not to the allocation literature.

For an administrator, the consequence is straightforward. A procedure that repeatedly deducts delivered service and recalculates priorities can produce a different distribution from a procedure that commits the entire budget using initial requests. That need not make either procedure unacceptable. It means they are different policies. The authority must specify which request remains in the formula after an award.

## 6. An existing demand-bounded alternative

If demand is intended as a cap, the established weighted proportional family supplies a natural alternative [C2, PDF p. 9; C3, PDF p. 9]. For a feasible floor, let $B=C-U$ and allocate residual awards

$$
z_i=\min\{d_i,\lambda w_i d_i\},\qquad
\sum_i z_i=\min\{B,\sum_i d_i\}.
$$

Total awards are $U_i+z_i$. Any unassigned capacity is recorded as $B-\sum_i z_i$. In the earlier 1-and-9 example, the capped awards are 1 and 4, instead of 2.5 each. The claimant whose request is met stops receiving more; the rest goes to the remaining claim.

This is an application of prior work, not a new mechanism. Nor does it preserve every property of the uncapped formula. When the residual budget is positive, the residual fulfillment rates of claimants with positive, unsaturated residual demands still have the same ratio as their weights. With zero residual budget, both rates are zero and their ratio is undefined. Once a claimant is fully served, its fulfillment cannot keep rising in proportion to its weight. In the example, the two fulfillment rates are 1 and 4/9. Their ratio is 9/4, not the weight ratio of 9. A policy should not advertise exact global fulfillment priority after imposing demand caps.

There is a further distinction at the floor. If $U_i>D_i$, the unconditional floor itself exceeds that claimant's demand. Our implementation permits that entitlement interpretation, but its bound on total awards is then $\max(U_i,D_i)$, not $D_i$. A rule that promises total demand bounds must also require $U_i\leq D_i$. If available residual capacity exceeds all residual claims, no rule can both respect those caps and exhaust the capacity: summing the caps proves the conflict. Reporting unused capacity makes that choice visible; it does not imply that physical equipment must consume energy while idle.

The capped rule does not solve strategic demand inflation, select fair weights, or ensure composition. The original preprint already recognizes incentives to inflate requests. Those institutional questions need separate analysis.

## 7. Results that remain valid, and limits of the audit

The source's five-class example is a useful positive control. The contested budget is 1,800,000 units and weighted residual demand totals 630,000. Exact awards reproduce the displayed rounded values. The highest-weight claimant receives its full 700,000-unit request; no claimant exceeds demand. The capped and raw rules therefore agree. When total capacity falls from 2,400,000 to 1,800,000 while the aggregate floor remains 600,000, contested capacity falls from 1,800,000 to 1,200,000. Every raw residual award falls by one third. The source's central illustration of concentrated adjustment is correct [C1, p. 8].

The finite grid contains 486 cases. The raw formula respects every claim in 323 and exceeds at least one in 163. Of the latter, 81 are deliberate surplus-supply cases; 82 have a budget no larger than total demand. The capped implementation respects all tested claim bounds, uses exactly the lesser of capacity and total claims, and records the remainder. These counts are checks on the chosen input set, not empirical failure rates. Fifteen tests cover the worked example, positive properties, counterexamples, impossible floors, zero residual claims, and changes in fulfillment ratios.

The audit holds fixed a common divisible compute unit. It does not establish that one unit provides equivalent useful service across hardware, tasks, or users. It also does not show how energy, water, or other limits should be converted into a single capacity budget. There are no estimates of welfare, political legitimacy, implementation cost, or real-world performance. A correction to a formula cannot settle whether a compute entitlement is preferable to money or public services.

The practical conclusion is narrower. A public compute guarantee should state whether demand is a cap, what happens when claims are filled, and whether previous awards change later claims. Its arithmetic can then be checked against those promises. A protected floor and a total capacity ceiling are compatible with several allocation policies, but they do not by themselves determine one.

## Appendix: implementation and verification

The offline code uses exact fractions. For the capped rule, it allocates in proportion to weighted residual claims, fills any claim that reaches its cap, removes that claim from the active set, and divides the remaining budget among the others. Each pass either finishes the allocation or removes at least one claimant. On a shortage domain with positive weights, the sum of capped awards is a continuous increasing function of the multiplier until all claims are filled. The award vector is unique. The multiplier need not be unique once every claim is filled.

The [protocol](protocol.md) fixes the finite grid and separates exploratory discovery from prospective software checks. The [inputs](data/raw/cases.json), [exact named results](results/named-cases.json), [full grid](results/grid.csv), and [run metadata](results/run-metadata.json) permit inspection without obtaining third-party PDFs. The [source ledger](sources/manifest.json) and [evidence extracts](sources/extracts/evidence.md) identify the actual documents and distinguish their wording from our interpretation. Reproduction commands are in the [README](README.md).

Codex performed source collection, analysis, and drafting. No human participation, institutional affiliation, funding, endorsement, or conflict declaration is invented. The [separate AI review](reviews/critical-review.md) reproduced the outputs and independently checked all 486 cases. Both requested text corrections were verified; the [author response](reviews/author-response.md) records their disposition. The [release record](logs/completion.md) states the completed gates and remaining limits.

## References

[C1] Galipeau, David. 2026. *Universal Basic Compute Under a Joule Ceiling: A Priority-Weighted Allocation Rule for Energy-Bounded Artificial Intelligence*. Version 2, Zenodo record 21305645, 11 July. [Pinned record](https://zenodo.org/records/21305645).

[C2] Thomson, William. 2006. *A characterization of a family of rules for the adjudication of conflicting claims*. Rochester Center for Economic Research, Working Paper 530, version dated 24 April. [Primary working paper](https://www.sas.rochester.edu/eco/rcer/papers/rcer_530.pdf). Read relevant definitions and examples, not the complete characterization proof.

[C3] Harless, Patrick. 2017. “Endowment additivity and the weighted proportional rules for adjudicating conflicting claims.” *Economic Theory* 63(3): 755–781. [DOI](https://doi.org/10.1007/s00199-016-0960-9). Text inspected: [author accepted manuscript](https://eprints.gla.ac.uk/129220/7/129220.pdf), internally dated 11 February 2016 and deposited 30 September 2016; the publisher version may differ.
