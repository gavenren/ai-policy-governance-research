# S014 protocol: compute floors and priority

**State:** Protocol. **Recorded:** 2026-10-12T17:30:10.083514Z. This is prospective for the finite enumeration and software checks, which have not yet run. It is not prospective for discovery: the source and prior allocation literature were already read, hand counterexamples were found, and a separate AI feasibility review was completed.

## Question and bounded contribution

Does the allocation rule in David Galipeau's *Universal Basic Compute Under a Joule Ceiling*, Zenodo record 21305645, version 2, have the allocation properties claimed for it? What changes when demand is an upper bound rather than a transferable entitlement score? The unit is a specified formula/property/domain combination, not a jurisdiction or an observed compute user.

This is a short technical comment on a pinned proposal. It does not introduce a new allocation rule. Thomson (2006) and Harless (2017, accepted manuscript dated 2016) already define capped weighted proportional awards and distinguish the relevant axioms. The new contribution is the explicit application and reproducible correction to this compute proposal. It is distinct from S012's income-normalization audit, S007's payment queue, and S013's supplier-access audit. A bounded search and a read-only comparison with the separate public programme will be recorded.

## Scope and selection

Include Equation 3, Equation 4 and its zero-residual convention, Propositions 1–3 and 5 insofar as they concern budget, fulfillment and floor feasibility, Section 3.3's inherited-properties statement, and the five-class worked example and 25 percent shock. Test subset consistency, standard composition up and down, and unchanged-claim budget additivity separately. Do not audit every energy, legal, welfare, strategic or political claim. Retain source qualifications on demand inflation, exchange and delegation.

The source's physical sum identity and its worked example are expected positive controls. Hand examples already expose over-fulfillment under a demand-cap interpretation, the zero-residual exhaustion exception, and composition failures. The analysis must preserve those distinctions. A negative result for one property is not a rejection of all guarantees.

## Planned offline methods

Use Python standard-library exact Fraction arithmetic. Retain a small JSON file of named cases. Reproduce the source's five residual demands (700000,600000,400000,900000,200000), weights (0.35,0.30,0.15,0.15,0.05), residual budget 1800000, and shock budget 1200000. The source specifies aggregate floor 600000 but no complete individual floor vector; do not invent one.

Enumerate two positive claims independently from {1,2,5} and two positive unnormalized weights independently from {1,2,4}; normalize weights. Use budgets equal to {0,1/4,1/2,3/4,1,5/4} of the sum of claims: 486 rows. Compare raw and capped awards, total awards, each demand bound, unused budget, and the analytic threshold C <= sum(w_i D_i)/max(w_i). This is a finite software check, not a prevalence estimate. Include both shortage and surplus cases and report both; no outcome-based filtering.

For composition, use the explicitly specified positive-claim example D=(2,2), w=(2/3,1/3), and budgets 1 and 2. Check that all intermediate claims remain valid and all caps remain inactive. Separately check unchanged-claim additivity, equal weights, and subset consistency on a three-claimant case. These examples are selected counterexamples, not a representative sample.

Implement the established capped allocation z_i=min(d_i,lambda w_i d_i) for d_i=max(D_i-U_i,0), residual budget B=C-sum(U_i), with sum z=min(B,sum d). Reject B<0 because the protected floor is infeasible. Handle zero budget, zero residual claims, surplus, inactive and active caps. Return unused capacity explicitly. When U_i>D_i, bound total awards by max(U_i,D_i), not D_i; explain the floor-as-entitlement interpretation. The award vector is unique; lambda need not be unique when all claims are filled. Do not claim this repair fixes composition or strategic inflation.

## Validation and interpretation

Write tests with explicit expected vectors and meaningful negative controls. Check formulas with hand proofs. Publish input/code hashes and actual run time; retain all prespecified output rows. A separate AI reviewer must reproduce the most important results independently and examine source wording, domains, novelty and readability. No human review is implied. Do not assign frequencies to real systems from the grid. Hold a common divisible compute unit fixed; do not equate it to homogeneous useful AI service or infer energy efficiency.

## Evidence and completion

Pin source versions, retain originals and extracted text in ignored storage when full redistribution rights are not established, and publish short evidence extracts, precise locators, source hashes and retrieval recipes. Record actual source and search timestamps; do not invent dates for earlier exploratory searches. Recheck the target's latest-version API and author listing before publication. A dated author-site listing is not proof of a separate paper revision. No author contact is authorized. Complete-study status requires the programme gates and disposition of the separate critical review.

Stop expanding after the planned examples, finite grid, proofs and review suffice to answer these questions. Further grids are justified only by a defect or unresolved concern. Keep the paper readable and short; place algorithm details in an appendix.
