# S012 protocol: measuring the AI dividend

State: Working notes. Design recorded 2026-10-12T13:49:06Z, before numerical code or results. This is an exploratory consistency audit. The algebraic concerns and the favorable interpretation of the consumption tax were known before this record. This is not a preregistration of their discovery.

## Question and contribution

Do four selected claims in Growiec, Prettner and Szkróbka, *Redistributive Policies for the Times of Transformative AI*, arXiv:2609.14750v1, follow from the equations and assumptions that support them? The units are a named claim and a fully specified mathematical example. The contribution is a version-specific, reproducible comment with constructive repairs and positive controls. The underlying inequality identities and CES calculus are established mathematics, not new theorems.

The four claims concern equal transfers, the exact factor-share log equation, the capital-share limit, and a consumption tax with an equal rebate. These were selected after reading the source, not by a random sample of its propositions. The audit does not assess the whole paper, forecast inequality, rank policies in general equilibrium, or establish an optimal tax. It does not infer misconduct or contact the authors. The related income covariance equation is a positive control. An aggregate indexation example clarifies the first claim. Heterogeneous saving is an explicitly separate extension outside the common-saving assumption.

## Source plan

Use the pinned arXiv PDF and its original TeX to verify equations; compare HTML where useful. Record the unversioned submission history. Read the cited Growiec growth paper before judging the capital limit. Use Cowell's author manuscript to establish that relative and absolute inequality are old distinctions. Publish short, locatable extracts and mathematical transcriptions with source hashes and retrieval instructions. Keep full third-party originals in ignored storage. Do not add a reuse licence. Recheck arXiv history before release.

Closest work is the audited paper itself. The cited growth paper supplies a strong supporting condition for its asymptotic result. Cowell supplies measurement background. S004 used the audited paper's abstract as background, explicitly without a full method comparison; no earlier study executed this audit. S011 concerns a real survey and debt payments, not inequality identities. A bounded correction search found no correction, which is not proof of priority.

## Numerical design fixed here

Use only Python standard-library analysis, no network access during analysis, no fitted data, no stochastic forecast, and no empirical standard errors. All inputs are synthetic, with equally weighted individuals and population variance (denominator n).

1. Six income vectors: (1,3), (1,9), (0,2,4), (2,2,2), (1,2,4,8,16), and (0,0.01,1,1000). Apply all 72 combinations of three positive scale factors (0.25,1,2) and four equal additions (0,0.1,1,10). Report mean, raw variance, squared coefficient of variation and Gini. Include zero incomes and equality; exclude a zero mean because relative indices are undefined.
2. For each vector, compute all 120 consumption-tax cases: saving rates (0,0.25,0.8,1) and tax rates (0,0.1,0.5,1,2). Solve the equal rebate from budget balance; also retain the no-rebate common-scaling control. Check individual budgets, aggregate balance, and the analytical reduction factors.
3. Use 200 seeded positive-income cases (seed 20261012, eight lognormal draws per case) as implementation checks of the affine and rebate formulas. These cases are not evidence for a theorem or a population.
4. Retain exact two-person examples for equal transfers, an indexed transfer with u=1/4, a common-saving rebate, and heterogeneous saving. For heterogeneous saving use incomes (1,9), tax 1, and saving vectors (0,1) and (1,0). Treat these as boundary examples, not refutations of the common-saving claim.
5. Check the source's nested CES at all 2,187 combinations: alpha and beta in (0.25,0.5,0.75), theta in (-2,-1,-0.25), omega in (-1,0.5,1), and each of K,H,AI in (0.5,1,2). Report the log-identity residual and verify shares add to one, Euler's level identity, and local elasticities by a centered log-input finite difference. Include the exact counterexample K=1,H=AI=2,alpha=beta=0.5,theta=-1,omega=1 and the equal-input control.
6. Show the local log approximation at that counterexample, in log-input direction (0.2,-0.1,0.3), for step sizes 0.1,0.01,0.001,0.0001. Do not use a local approximation as a global identity.
7. Use three relative-input paths with K=exp(t), H=1, beta=alpha=0.5,theta=-1,omega=1 and AI=2S-1. Let S/K be 1, 1+t, and exp(t), at t=(0,1,2,5,10,20,50,100). These are input paths, not solved household equilibria. They show why labor disappearance and relative cognitive abundance differ; the unbounded paths support the original limit.
8. Check the linear income covariance formula in four named component arrays, including negative covariance and a zero component, using net component multipliers (0.6,0.8,0.4) and a common addition 1.25. Check the fixed-share log-index variance repair in one four-person positive-endowment array. These controls must remain even if they weaken the critique.

## Decision rules and completion

Classify each source claim as an error as stated, valid under stated assumptions, or conditional with a supporting interpretation. A numerical counterexample can disprove a universal identity; a grid cannot prove one. Use algebra for general statements and numerical outputs to detect implementation mistakes. Report the numerical tolerance and residuals, not an unexplained pass label. Keep all planned examples and controls. Log any material change before rerunning.

Stop expansion when these checks, source provenance, manuscript, separate AI critical review, author response and release checks are complete. A critical unresolved algebra or source problem blocks complete-study status. The final paper must distinguish established mathematics, the source's result, our correction, and our extension. No human or journal peer review is claimed.
