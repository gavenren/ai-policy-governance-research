# Feasibility review: firm aggregation in an equity-levy model

Recorded **2026-10-12 17:49:30 UTC**. Separate Codex feasibility review. No study number is assigned here. No source model, outcome grid, or new central implementation was run. This note records source reading and algebra before a prospective numerical plan.

**Decision: proceed only as a short quantitative robustness note.** The proposed calculation is valid under an explicit equity-value weighting assumption. Its useful contribution would be to state the information limits of one public scenario model. It is not a new general theorem, an empirical estimate of error, or evidence that the levy would fail. A second small parameter grid alone would not be a sufficient contribution.

## Target and favorable interpretation

The target is Silviu Pitis, [Who Owns the AI Economy?](https://silviupitis.com/blog/2026/who-owns-the-ai-economy/), dated 16 July 2026, and the Figure 3 code in [the public repository](https://github.com/spitis/who-owns-ai-economy/tree/1573447e94b21f0da8fbaa1e9cf78823a5e2663e). The current-main API capture on 12 October returned the same commit, `1573447e94b21f0da8fbaa1e9cf78823a5e2663e`.

I read the repository README; the full Figure 3 model, README, DATA, SOURCES and BURDEN files; and the essay's relevant levy, market-access, Figure 3, and ownership paragraphs. The source explicitly calls its sales matrix constructed. The current Figure 3 footnote and caption also say that the cap is applied to group sales patterns. Thus there is no basis to accuse the author of concealing aggregation or to call the regional illustration a failed firm-level estimate.

The source functions `collection_matrix` and `bucket_ledger` apply the cap to each of six listed-market groups. The latter collects the fraction `min(1,k*S)` of a group's levy base, where `S` is its combined sales share in member markets. The construction uses several revenue-data anchors. In the Magnificent Seven appendix, the initial company blend is explicitly revenue-weighted. A six-region pattern interpreted as an equity-value-weighted mean is an additional model assumption.

The code uses rounded market values whose sum is 126.71 trillion dollars. The documentation gives a more precise 126.693 trillion anchor. A replication should preserve the actual code array and explain the rounding. The two corporate universes have different valuation dates and must not be added together. This review does not audit the underlying company filings, Figure 4 valuation model, legal claims, or shareholder-incidence estimates.

## Algebra check

Let a firm have sales fractions `x_j >= 0` with `sum_j x_j = 1`. Fix a member set `M`, a common cap `k >= 1`, and a common levy rate. Write `q = sum_{i in M} x_i`. The member's receipt, per unit of the firm's full levy charge, is

`f_i(x) = x_i * min(k,1/q)` when `q > 0`, and zero when `q = 0`.

Let `s_j = E_V[x_j]` be the mean under normalized equity-value weights, not revenue weights. Let `S = sum_{i in M} s_i`, `h = 1-S`, and `r_i = E_V[f_i(x)]`.

The proposed receipt set for **one group and one fixed member set** is correct:

`s_i <= r_i <= k*s_i` for every member, and `sum_{i in M} r_i <= 1`.

Necessity follows because `1 <= min(k,1/q) <= k` for positive `q`, while the sum of receipts is `min(1,k*q) <= 1`. At `q=0`, all member sales are zero, so the same inequalities hold without division.

The following construction proves sufficiency when `h > 0`. For every member with `r_i > 0`, give a firm type equity mass `r_i`, member-i sales `s_i/r_i`, and zero sales to other members. Allocate its remaining sales across holdouts in proportions `s_j/h`. The member sales fraction lies in `[1/k,1]`, so that type's full levy is collected for member i. Give the remaining mass `1-sum_i r_i` only holdout sales, again in proportions `s_j/h`. Each member mean is `s_i`; each holdout mean is also `s_j`, since its combined sales mass is exactly `h`. All components are nonnegative and each firm type's sales sum to one.

Boundary conditions matter:

- If `r_i=0`, then `s_i=0`; omit the type rather than divide by zero.
- If `h=0`, the constraints force `r_i=s_i`. Every firm has all sales inside the club almost surely, and this receipt vector is exact.
- If the member set is empty or its mean sales share is zero, receipts are zero. The remaining firm type can preserve the holdout means.
- If `k=1`, receipts equal member means for every distribution.

This construction permits arbitrary latent firm value shares. It is not a reconstruction of the actual firms in a group, and it does not preserve separately known firm market values, counts, sales, or sector restrictions. Those extra data could narrow the set.

The sharp club-total interval is `[S,min(1,k*S)]`. The upper bound is the elementary concavity bound for the capped linear function. A homogeneous firm profile attains it. Destination-only firm types attain the lower bound while preserving the full sales-mean vector. For one member, the sharp marginal interval is `[s_i,min(k*s_i,s_i+h)]`. The upper endpoints for different members need not be jointly attainable.

The homogeneous group profile attains the club-total upper bound, but it need not attain each country's upper bound. Do not transfer the scalar Jensen result to individual country receipts. This distinction is the most useful part of the proposed application.

Across source groups, scalar club bounds and each country's separate marginal bounds can be summed because the within-group distributions are unrestricted. A joint cross-group receipt set must retain the group constraints. A box of summed country intervals with one total constraint need not represent the full joint set. Likewise, different country endpoints across different clubs need not describe one common firm population. By contrast, destination-only types attain all club-total lower bounds at once, and the source's homogeneous profiles attain all club-total upper bounds at once.

Conservation and membership monotonicity survive at firm level. Adding a member raises `q`, so total collection cannot fall. The multiplier for an existing member cannot rise, so its receipt cannot rise. A joining country goes from zero collection to a nonnegative receipt. These are gross accounting statements. They do not establish a net fiscal gain, a welfare gain, or a stable international agreement.

## Measurement condition

For firms with positive revenue, set `t=equity value/revenue` and use normalized revenue weights. Then

`mu_V = mu_R + Cov_R(t,x)/E_R[t]`.

The identity confirms that a revenue-weighted exposure generally does not identify the required value-weighted exposure. Positive equity in a firm with zero revenue requires a separate value-mass term; it cannot enter this ratio. With different firm levy rates, the relevant weights would instead be levy-base weights.

The proposed binary sensitivity bound is also correct. If `l <= t <= u`, with `0 < l <= u`, and the revenue-weighted club exposure is `m`, then

`l*m / (l*m + u*(1-m)) <= mu_V <= u*m / (u*m + l*(1-m))`.

Sharpness follows by putting exposure at zero or one and assigning the extreme value/revenue ratios in opposite ways. The ratio limits are new assumptions, not observed uncertainty. This could be a short appendix. It should not displace the main requirement to label the group means correctly. The source's constructed and adjusted rows are not all direct measurements of a single revenue-weighted object either.

## Closest inspected work

**Loretz, May 2025, [Unitary Taxation and Formulary Apportionment](https://www.wifo.ac.at/wp-content/uploads/upload-6465/s_2025_unitary_taxation_53209586.pdf).** I read the cover, relevant literature and methods passages, Sections 3.2.3–3.2.4 on PDF pages 28–32, and the conclusion on pages 56–57. The report already explains that country-pair aggregation can produce biased estimates, that aggregate data omit important firm-level variation, and that sales by destination are difficult to observe. It uses hybrid firm and aggregate data. Thus “aggregation matters” and “destination data are incomplete” are established points. The inspected methods concern profit-tax apportionment and loss consolidation, not this levy-specific cap or its attainable receipt vector.

**Hines, July 2009, [Income Misattribution under Formula Apportionment](https://www.nber.org/system/files/working_papers/w15185/w15185.pdf), NBER Working Paper 15185.** I read the cover, abstract and introduction on PDF pages 1–5 and the formal distortion discussion on pages 8–11. It studies the mismatch between profits and formula factors, including merger incentives. This is a close warning about interpreting aggregate sales as another economic base. It does not supply the proposed capped-equity receipt set in the inspected passages. The journal article is dated 2010; the text read here is the 2009 working paper.

**Bertsimas and Popescu, 2005, [Optimal Inequalities in Probability Theory: A Convex Optimization Approach](https://web.mit.edu/dbertsim/www/papers/MomentProblems/Optimal-inequalities-in-probability-theory-A-convex-optimization-approach-SIAM15.pdf).** I read PDF pages 1–5, including the moment formulation and definition of tightness. Optimizing over distributions with given moments is established mathematics. The proposed argument is a simple special-purpose construction, not an advance on that general method. I did not audit their later proofs.

The bounded searches did not identify a prior quantitative audit of this exact Figure 3 cap. That is not proof of global novelty. The existing literature is sufficient to reject a broad claim that this study discovers aggregation bias or sharp moment bounds.

## Suggested prospective work

Before execution, fix the source commit, source arrays, arithmetic conventions, and all outputs. A useful plan would cover the 64 member sets, both separate corporate universes, and the source's cap choices 2, 3 and 5. It should reproduce the source point calculations first, then report sharp club totals and separate country bounds. The core evidence should include explicit feasible firm mixtures at selected endpoints, not just another grid of numbers.

Tests should check each mixture's complete mean vector, nonnegative value weights, firm-level caps, conservation, empty clubs, zero exposures, `k=1`, and global membership. Comparisons of joining must use the same underlying mixture before and after entry. Test the optional reweighting formula separately and label its assumptions. Retain the source's valid accounting claims and avoid any inference about treaty stability from gross receipts alone.

The final paper should say exactly what is held fixed: the constructed group means, group values, levy rate, cap, and compliance. It should separate latent firm variation from uncertainty in those inputs. The bounds are conditional scenario bounds, not confidence intervals. The contribution is distinct from S009's payment-enforcement model and S008's acquisition finance. It remains small enough for a short paper or a technical note, with no need to expand into legal analysis or a new valuation model.
