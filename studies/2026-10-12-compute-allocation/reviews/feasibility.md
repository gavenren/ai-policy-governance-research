# Independent feasibility review: compute allocation

**Decision:** a short technical comment is justified. It should correct the claims made for one pinned preprint and apply an established capped rule. It should not claim a new general theorem or a new allocation mechanism. This review does not approve a later manuscript, numerical code or source package that does not yet exist.

**Reviewer:** a separate AI agent that did not write the proposed study's central code or paper. **Review time:** 2026-10-12, ending after the 17:25:33 UTC version check. No human review is claimed. The parent supplied candidate concerns before this review; the reviewer independently read and checked the relevant source.

## Source and scope

The target is David Galipeau's *Universal Basic Compute Under a Joule Ceiling*, version 2, Zenodo record [21305645](https://zenodo.org/records/21305645), dated 11 July 2026 in the repository. The PDF cover says July 2026. I read the extracted text of all 16 pages and visually checked PDF pages 7 and 8. The paper's equations, propositions, worked example, qualifications and references were inspected. I did not validate every substantive reference, energy claim, metering claim or policy comparison in the source.

A direct web-reader request for the record and latest page failed. A separate request to the record's observed latest-version API succeeded at 2026-10-12T17:25:33.037449+00:00 and returned record 21305645. The returned metadata and its acquisition record are retained separately in ignored storage. Thus, version 2 was the latest returned version at this check, not a claim that no future update will appear.

For prior definitions, I read Patrick Harless's accepted manuscript, printed pp. 5–8 (PDF pp. 6–9), including the claims domain, Section 2.1 and footnote 16, and the definition in Section 2.2. The publication is *Endowment additivity and the weighted proportional rules for adjudicating conflicting claims*, Economic Theory 63(3), 755–781 (2017), [author accepted manuscript](https://eprints.gla.ac.uk/129220/7/129220.pdf). Its internal date is 11 February 2016. This is not a claim to have read the complete proof or the publisher version.

I also inspected the publisher's [front matter for Thomson's 2019 book](https://assets.cambridge.org/97811071/94625/frontmatter/9781107194625_frontmatter.pdf). The figure list identifies the failure of both composition axioms for unequal weighted proportional rules (Figure 6.8, book p. 142). I did not read that full chapter. The local Thomson 2006 manuscript was identified but only its front matter was read in this review. Harless provides the exact definitions used below.

## 1. Claims bounds and the meaning of demand

Equation 3 on source p. 5 exhausts the physical budget for positive demand and weights. That identity is valid. It does not imply that each award is no larger than its declared demand.

A simple hand example has demands D=(1,9), weights w=(9/10,1/10), and budget C=5. The weighted demands are (9/10,9/10). Equation 3 assigns (5/2,5/2), so the first award exceeds the first claim even though total demand is 10 and the budget is only 5.

More generally, with W=sum_i(w_i D_i), the raw rule respects all demand bounds exactly when C <= W/max_i(w_i), for strictly positive demands. This condition is stronger than C <= sum_i D_i when weights differ. This algebra is elementary; it is not a new characterization theorem.

**Charitable interpretation:** the source permits entitlements to be pooled, delegated or exchanged (pp. 2, 4 and 8). If demand is a priority score and awards are transferable rights, an award above declared own use need not be waste. But that interpretation differs from a claims problem in which the claim is an upper bound. A comment must state the distinction. It must not report that Proposition 1 violates its own sum identity, or that every excess award is wasted.

The source's worked example on p. 8 reaches the boundary for its highest-priority claimant. It does not itself over-allocate. Its weighted residual total is 630,000 and its contested budget is 1,800,000. The health award is exactly 700,000. The other displayed rounded awards and the shock arithmetic are consistent with the stated rule. Preserve this example as a positive control.

## 2. The zero-residual exception is real, but bounded

Equation 4 and its convention appear on p. 7. When all residual demands vanish, the second term is zero. Awards therefore sum to U, not necessarily C. With D=U_vector=(1,1) and C=3, the convention gives awards (1,1), total 2, and unused capacity 1. The stated condition U<=C holds, but the exhaustion clause of Proposition 5 does not.

For the formula as written, floor compliance and exhaustion hold together exactly when U<=C and either the weighted residual demand is positive or U=C. This describes the stated convention; it does not add a rule for surplus supply.

**Charitable interpretation:** the text motivates an economy with aggregate excess demand. If the domain were restricted to U_i<=D_i and sum D_i>C, positive residual demand follows whenever U<=C. In that narrower shortage domain, the exception cannot occur. The source does not include those restrictions in Proposition 5 and explicitly gives a zero-residual convention, so a domain correction is warranted. This is a boundary error, not evidence that the ordinary shortage example fails.

## 3. Consistency survives; composition does not

The source's Section 3.3 (pp. 6–7) says that properties from the proportional family carry over without new proofs. It does not define which composition property is intended.

Subset consistency holds for the raw rule when a subset departs with its awards and the remaining budget is the sum of the remaining awards. Renormalizing the retained weights does not change that result. Fixed-claim endowment additivity also holds because Equation 3 is linear in C when D and w stay fixed.

Those statements are different from standard composition up and composition down. Harless's footnote 16 on printed p. 6 makes the difference explicit. Composition up updates claims by subtracting the first awards. Composition down uses the larger-budget awards as the new claims. The same political weights are held fixed in these tests.

Here is a hand calculation in which no claim bound is breached. Let D=(2,2), w=(2/3,1/3), and the total budget be 2.

- Direct awards at budget 2 are (4/3,2/3).
- For composition down, reduce the budget to 1. Applying the rule to the previous awards gives (4/5,1/5). Applying it directly to D gives (2/3,1/3). The vectors differ.
- For composition up, first allocate budget 1. The awards are (2/3,1/3), leaving claims (4/3,5/3). Allocating the second unit gives (8/13,5/13). The sum is (50/39,28/39), whereas the direct budget-2 allocation is (52/39,26/39).

All intermediate problems remain in the claims domain. Thus this failure is not caused by the separate over-allocation issue. Capping awards will not change this particular counterexample because the caps are inactive.

**Charitable interpretation:** the source may have meant additivity with the original claims kept fixed. That property is valid and useful for splitting a precommitted budget. It must be named and separated from the standard composition axioms. Neither the failure nor its general form is new to the allocation literature. The contribution is to correct the transfer of those properties to this compute proposal.

## 4. The capped repair is prior work

Harless's Section 2.2 defines weighted proportional awards as min{lambda u(i,c_i), c_i}. Set u(i,c_i)=w_i c_i. This is precisely the proposed capped weighted-fulfillment rule for a shortage problem. Credit this established family.

For a separate floor, write residual demand d_i=max(D_i-U_i,0) and residual budget B=C-sum U. On a floor-feasible domain, the cap can allocate min(B,sum d) and record any unused capacity. If a demand bound applies to total awards, require U_i<=D_i as well. If a floor instead defines a transferable right that can exceed own use, say so and do not assert that total awards are demand-capped.

The cap preserves the original weighted fulfillment ratios only among unsaturated claimants. Once a claimant's demand is filled, its award cannot continue to grow in exact proportion to its weight. For the (1,9), (9/10,1/10), C=5 example, capped awards are (1,4). Their fulfillment ratios are 1 and 4/9, which do not have the original weight ratio of 9. The uncapped algebra cannot be retained globally by renaming the rule.

The scalar lambda need not be unique when every claim is filled. The award vector can still be unique. A proof or implementation should state the correct object of uniqueness.

## Recommended scope and quality gate

Proceed only as a bounded technical comment with four tasks: state the domains; distinguish the allocation properties; reproduce the source's valid example; and show a credited capped implementation with its changed guarantees. The comment is distinct from S012's income-normalization audit because it concerns the content and revision of a rationed public entitlement. The research contribution remains corrective and limited.

A prospective protocol should precede any broad numerical enumeration. It should separate hand-selected counterexamples, positive controls and any later finite grid. A grid measures the selected parameter set; its failure frequency is not a prevalence estimate for real compute systems. Exact rational arithmetic is suitable for these cases. Tests should cover the stated zero-residual convention, equal weights, inactive and active caps, no residual capacity, excess supply, and every domain restriction used in a proof.

Do not add claims about democratic legitimacy, optimal welfare, strategy-proofness, task quality or energy efficiency without separate analysis. The original source already recognizes strategic demand inflation; the capped rule does not in itself solve it. Do not infer that one accelerator-hour is a uniform useful service across hardware and tasks. The allocation audit can hold a common divisible unit fixed and state that limitation.

This review performed hand algebra, source reading and a version check. It did not execute a numerical grid, write central analysis code, or review a finished new paper. The source hashes below pin what was read. A later independent review is still required.

[Reviewed source hashes](feasibility-hashes.json).
