# How Much Would an AI Equity Levy Collect?
## Firm-level caps and the limits of group averages

**Study S015 · Complete-study draft · 12 October 2026**

**Research type:** Quantitative robustness note on a pinned public policy model.

**Evidence:** Public sources and constructed scenarios; no observed levy collections. Source-capture cutoff: 2026-10-12T17:46:29.147619Z; the separate feasibility search ended at 17:48:45Z.

**Disclosure:** Codex prepared the analysis and manuscript. Separate AI critical review and reproduction are complete; see the review and author response. No human peer review or external submission is claimed.

## Abstract

An equity levy could give the public a financial stake in an economy where AI replaces labor income. Yet a levy charged to firms cannot always be estimated from the average sales pattern of an industry or region. This note examines the capped, sales-based collection rule in Figure 3 of Silviu Pitis's *Who Owns the AI Economy?* The source explicitly presents a group-level illustration. We ask a further question: which firm-level collections are compatible with its group averages? Conditional on treating those averages as equity-value-weighted sales shares, we derive the full attainable receipt set for a fixed group and participating coalition. The source's group calculation is the highest possible coalition total, while a population of firms selling to single destinations attains the lowest. Using the unchanged source inputs, the broad-company US–EU scenario ranges from $653.645 billion to $1,133.080 billion per levy year. Individual countries have different, jointly constrained ranges. Full global participation removes this aggregation uncertainty from total collections, but does not validate the underlying valuation or sales data. The result identifies a data requirement for fiscal planning; it does not estimate the proposal's actual revenue, welfare effects or legal feasibility.

## 1. Why an average can hide the collection limit

Suppose firms worth $100 in total sell, on average, one quarter of their output to a participating country. A levy charges one percent of equity value, subject to a cap of three times the sales share in participating markets. If every firm has the same quarter-share exposure, the country can collect 75 cents. If firms worth $25 sell only to that country and firms worth $75 sell only elsewhere, it can collect 25 cents. Total value and average exposure are unchanged. The distribution of exposure across firms changes the result.

This matters for proposals that replace some lost labor income with public capital income. A national budget needs a defensible collection base before it can promise a regular payment. A calculation based on regional averages is useful for illustrating a policy, but it cannot by itself reveal the firm distribution hidden inside each region.

Pitis (2026) proposes an annual equity levy allocated according to sales destinations. Countries in a collection club can take part of the charge associated with sales in nonmember markets, up to a cap. Figure 3 evaluates that rule with six listed-market groups and a separate Magnificent Seven example. Both the figure's caption and its assumptions describe the use of group sales patterns. The accompanying files also identify the matrix as constructed. This note therefore extends the illustration rather than treating it as a failed claim to firm-level precision. [P1; V4–V7]

The contribution is narrow. We show exactly what that illustration identifies when its sales rows are interpreted as value-weighted means, and what remains unknown. We then compute the resulting bounds for the source's inputs and give actual firm mixtures that attain them. We do not claim to discover aggregation bias. Work on corporate-tax apportionment already explains why aggregate inputs can lose material firm variation. Loretz (2025, Sections 3.2.3–3.2.4) discusses these data and aggregation limits; Hines (2009, Section 3) examines differences between profits and apportionment factors, including incentives to change corporate ownership. Sharp bounds over distributions with known moments are also an established method (Bertsimas and Popescu, 2005). Our application concerns one specific capped equity rule. [F1; H1; M1]

## 2. The policy rule and what we hold fixed

Consider a group of firms with combined equity value $V$. Firm $f$ has a sales vector $x_f$: its sales shares across destinations are nonnegative and sum to one. Let $M$ denote the participating destinations and let $q_f$ be the firm's total sales share in those markets. With levy rate $\tau$ and cap multiple $k\geq1$, the coalition collects

$$
\tau V_f\min(1,kq_f)
$$

from that firm. Member $i$ receives the fraction

$$
g_i(x_f)=x_{fi}\min(k,1/q_f)
$$

of its full levy charge when $q_f>0$, and zero when $q_f=0$. The rule divides collection among members in proportion to their sales shares. A firm with no participating-market sales contributes nothing under this rule.

The source replaces the firms in each listed-market group with one sales profile $s$. It then applies the same cap to that profile. To study the firm-level information limit, we assume that $s$ is the average of the firms' sales shares weighted by equity value:

$$
s_j=\sum_f\frac{V_f}{V}x_{fj}.
$$

This is a substantive condition. Revenue-weighted sales exposure need not equal equity-value-weighted exposure. Several source anchors come from revenue data, and the source's Magnificent Seven construction starts from a revenue-weighted blend before further adjustments. We do not validate that blend as a value-weighted mean. Section 5 explains the difference. Without the weighting condition, the numerical ranges below are not bounds on actual collections. [V6–V7]

Within this conditional exercise, values, average sales, compliance, the levy rate and the cap remain fixed. We allow any latent firm weights and sales profiles that preserve the entire group mean. We impose no separate information about individual company values, sector restrictions or within-group dispersion. The exercise therefore asks what the averages alone permit, not which firm population is likely.

We use the source's six destinations: the United States, European Union, United Kingdom, Japan–Korea–Taiwan, China including Hong Kong, and the rest of the world. These are modeling groups; EU membership is not a claim that there is a single EU tax recipient. The broad listed-market values are the code's rounded end-2024 inputs, totaling $126.71 trillion. Its data note reports a more precise $126.693 trillion anchor. We retain the code values to make the replication exact. The separate Magnificent Seven scenario uses $22 trillion from a different, mid-2026 vintage. The two universes overlap and are never added. The levy rate is one percent. These values are inherited scenario inputs, not new measurements. [V4; V6]

## 3. What the averages identify

Write $S=\sum_{i\in M}s_i$ for the group's average participating-market exposure and $h=1-S$ for its nonmember exposure. Normalize receipts by the group's full levy charge $\tau V$.

**Coalition total.** Every compatible firm population yields a total in the interval

$$
S\ \leq\ r_M\ \leq\ \min(1,kS). \tag{1}
$$

Both endpoints are attainable. If all firms share the mean profile, collection equals the upper endpoint, which is the source's group calculation. If each firm sells only to one destination, with the value of each destination's firms proportional to its mean share, collection equals the lower endpoint. Mixtures of these populations attain every value between the endpoints while keeping the same mean.

The upper bound follows from the concavity of the capped collection function. Averaging before applying this cap produces at least as much total collection as applying the cap to each firm and then adding the results. The lower bound follows because the collected fraction is at least the participating sales fraction when $k\geq1$. The appendix gives the proof.

**Country receipts.** A total bound does not determine each member's share. The complete feasible receipt set for one group and one fixed coalition is

$$
s_i\leq r_i\leq ks_i\quad(i\in M),
\qquad \sum_{i\in M}r_i\leq1. \tag{2}
$$

Consequently, the range for one member considered separately is

$$
s_i\leq r_i\leq\min(ks_i,s_i+h). \tag{3}
$$

The source point can lie below a country's upper bound even though it attains the coalition-total upper bound. Further, different countries cannot each claim the same pool of unallocated collection. Their separate upper bounds need not be attainable together.

For example, the source's US-listed group has mean US sales of 0.58 and EU sales of 0.13. The remaining share is 0.29. With those two members and a cap of three, the source assigns about 0.817 of the full charge to the US and 0.183 to the EU. The US can instead receive 0.87 while the EU receives 0.13; another compatible population gives the EU 0.39 while the US receives 0.58. But the two separate upper bounds sum to 1.26, which exceeds the entire charge. The saved witness file supplies the full six-destination firm profiles, including the sales to nonmembers, for both valid alternatives.

Across listed-market groups, coalition bounds can be added. Each country's separate bounds can also be added, because the unknown populations in different groups are unrestricted. Joint country choices must still respect each group's constraints. One cannot replace them with an unrestricted set of aggregate country intervals. Nor should endpoints calculated for different coalitions be treated as a single observed population. The destination-only and common-profile populations do, however, attain all coalition-total lower and upper bounds, respectively, using the same population across membership choices.

## 4. Results for the source scenarios

Table 1 uses the source's five selected coalitions and cap multiple of three. Amounts are billions of US dollars per levy year. They are values of an equity charge, not evidence of cash available for immediate payment. Every lower and upper entry is sharp under the assumptions above; the values between them have no assigned probability.

**Table 1. Coalition collections conditional on the constructed sales means**

| Participating markets | Broad: lower | Broad: source point / upper | Magnificent Seven: lower | Magnificent Seven: source point / upper |
| --- | ---: | ---: | ---: | ---: |
| US | 473.426 | 960.072 | 121.000 | 220.000 |
| US and EU | 653.645 | 1,133.080 | 158.400 | 220.000 |
| US, EU, UK and Japan–Korea–Taiwan | 808.101 | 1,162.716 | 180.400 | 220.000 |
| All modeled destinations except China/Hong Kong | 1,049.509 | 1,177.395 | 206.800 | 220.000 |
| All modeled destinations | 1,267.100 | 1,267.100 | 220.000 | 220.000 |

*Source: executed calculations in `results/configurations.csv`; source values and matrix held fixed. Three decimal places preserve the arithmetic of the constructed inputs and do not imply empirical precision.*

The US–EU broad scenario illustrates the information gap. Its group calculation is $1,133.080 billion, but a different population consistent with the same full matrix collects $653.645 billion. This difference is not an estimated shortfall. It measures how much the aggregate inputs leave unresolved when no further firm information is imposed.

Table 2 shows why the total and the member distribution require separate treatment. For the broad US–EU coalition, the source gives about $799.896 billion to the US and $333.184 billion to the EU. Either country could receive more than its source point under a different compatible population. The two upper entries cannot both hold: their sum exceeds the coalition's upper bound in Table 1.

**Table 2. Separate member ranges in the US–EU coalition, cap three**

| Universe | Member | Lower | Source point | Separate upper |
| --- | --- | ---: | ---: | ---: |
| Broad listed-company proxy | US | 473.426 | 799.896 | 867.285 |
| Broad listed-company proxy | EU | 180.219 | 333.184 | 480.933 |
| Magnificent Seven | US | 121.000 | 168.056 | 182.600 |
| Magnificent Seven | EU | 37.400 | 51.944 | 99.000 |

*Billions of US dollars per levy year. These are marginal intervals, not jointly attainable upper allocations. Exact values appear in `results/members.csv`.*

A higher cap need not improve the worst outcome permitted by the means. For the broad coalition excluding China/Hong Kong, raising the cap from two to three to five raises the upper bound from $1,152.930 billion to $1,177.395 billion to $1,226.325 billion. The lower bound remains $1,049.509 billion. Destination-only firms are either fully inside or entirely outside the coalition, so a higher cap cannot increase their collection. For the separate Magnificent Seven example, all three caps give the same interval, $206.800–220.000 billion. Raising a cap can increase collections for a fixed population without improving this particular guarantee over all unknown populations.

Several favorable properties survive firm variation. Adding a member cannot reduce total collection for a fixed population. It cannot increase an incumbent's collection, because the multiplier on that incumbent's sales share weakly falls. A joining member receives a nonnegative amount. These are accounting results, not conclusions about participation costs, retaliation or net welfare. With all destinations participating, every firm pays its full charge; collection is exactly one percent of the fixed total value. The model's total aggregation uncertainty then disappears. With cap one, collection is also linear in the participating sales share, so the bounds coincide for every coalition.

## 5. The data needed before making a payment promise

The most direct way to narrow these ranges is to match each covered firm's equity value to its sales destinations and apply the cap before aggregation. A portfolio total and an average exposure omit the association between firm value and exposure, as well as the variation around the mean. Better group averages alone do not reveal that variation.

The weighting issue is separate. Let each firm have positive revenue and let $t$ be its equity value divided by revenue. A revenue-weighted mean exposure $\mu_R$ and the required equity-weighted mean $\mu_V$ satisfy

$$
\mu_V=\mu_R+\frac{\operatorname{Cov}_R(t,x)}{E_R[t]}. \tag{4}
$$

Two equally revenue-weighted firms, one selling wholly inside the coalition and one wholly outside it, have average exposure one half. If the inside firm has three times the other's value per dollar of revenue, value-weighted exposure is three quarters. Reversing those ratios makes it one quarter. Thus a revenue mean of one half does not identify the relevant value mean. A positive-equity firm with zero revenue requires separate treatment; it cannot be included by dividing its value by zero. The source's constructed rows also involve judgment and mismatched geographical coverage, so they are not all direct estimates of one uniform revenue-weighted object. [V6–V7]

For a public dividend plan, the practical implication is to separate a useful illustration from a funding commitment. Publish the valuation date, covered firm set, weighting convention and destination definition. Show how firm caps are applied and which firm data remain unavailable. If only group means are known, present the resulting conditional range. Under the fixed value-weighted means, a full global coalition fixes both total collection and each member's receipt: every member receives its mean sales share of each group's full charge. For an actual payment plan, valuation, compliance, conversion of shares into cash and measurement of those recipient shares still need to be resolved.

The lower endpoint is not automatically the right budget. It is deliberately permissive about unknown firms and may be too low once their actual values and exposures are known. Conversely, an empirical weighting mismatch can invalidate even that conditional floor. These bounds are most useful as a test of what extra information a stronger fiscal claim requires.

## 6. Method, limits and research status

The prospective numerical plan was recorded after the hand derivation and source reading, but before executing the source model or the enumeration. We evaluated all 64 coalitions for two separate universes and caps two, three and five: 384 configurations. The package retains 2,304 group rows, 1,152 member rows and 2,304 entry checks on unchanged populations. It verifies 4,608 coalition-endpoint populations and 6,912 separate member-upper populations by reconstructing their full means and evaluating the firms directly. Exact rational arithmetic reproduces the unchanged source's floating-point calculations within $1.12\times10^{-16}$ trillion. Its internal checks and 15 additional unit tests pass. These are software and construction checks, not observations sampled from the world.

The central limits are substantial. We do not estimate the actual distribution of firms, independently validate the underlying financial sources, or solve for prices and behavior after a levy. A tax may change company value, sales, incorporation, avoidance and investment. We hold these channels fixed. We also do not establish enforceability, optimality, cash liquidity or a stable international agreement. The source itself discloses important input limits; our analysis makes a particular additional information requirement explicit.

The contribution claim rests on a bounded search and the portions of the nearest work actually read, listed in the source ledger. We found no prior calculation of this exact receipt set for the pinned Figure 3 model. That is not proof of global novelty. Separate AI review reproduced all seven deterministic outputs and independently checked all four tables. Its two text findings were resolved; see [the review](reviews/critical-review.md) and [response](reviews/author-response.md). No affiliation, funding source, conflict declaration or human endorsement is invented.

## References and evidence

- **P1.** Pitis, Silviu (2026). [*Who Owns the AI Economy?*](https://silviupitis.com/blog/2026/who-owns-the-ai-economy/), 16 July; captured 12 October. Relevant scope: market-access levy, Figure 3 caption and assumptions.
- **V1–V8.** Pitis, Silviu (2026). [Figure 3 code and documentation](https://github.com/spitis/who-owns-ai-economy/tree/1573447e94b21f0da8fbaa1e9cf78823a5e2663e/figure3-club), revision `1573447e94b21f0da8fbaa1e9cf78823a5e2663e`. Unchanged required files are included under the upstream MIT licence. That licence does not apply to this new study. The source README discloses AI assistance in its own preparation.
- **F1.** Loretz, Simon (2025). [*Unitary Taxation and Formulary Apportionment*](https://www.wifo.ac.at/wp-content/uploads/upload-6465/s_2025_unitary_taxation_53209586.pdf). WIFO, May. Relevant read scope: Sections 3.2.3–3.2.4 and conclusion, with supporting methods passages.
- **H1.** Hines, James R., Jr. (2009). [*Income Misattribution under Formula Apportionment*](https://www.nber.org/system/files/working_papers/w15185/w15185.pdf). NBER Working Paper 15185, July. The inspected version is the working paper, not the 2010 journal text.
- **M1.** Bertsimas, Dimitris, and Ioana Popescu (2005). [“Optimal Inequalities in Probability Theory: A Convex Optimization Approach.”](https://web.mit.edu/dbertsim/www/papers/MomentProblems/Optimal-inequalities-in-probability-theory-A-convex-optimization-approach-SIAM15.pdf) *SIAM Journal on Optimization*, 15(3), 780–804. Read scope: first five PDF pages; later proofs not audited.

The [source ledger](sources/manifest.json), [feasibility review](reviews/feasibility.md), [search record](reviews/search.md), [protocol](protocol.md), and [reproduction instructions](README.md) provide the evidence trail. Full nonlicensed source captures remain outside the published package.

## Appendix A. Proof of the receipt set

Let expectation use normalized firm equity values. For a positive coalition sales share $q\leq1$, the multiplier $\min(k,1/q)$ lies between one and $k$. If $q=0$, each member's sales share is zero. Therefore $s_i\leq E[g_i(x)]\leq ks_i$. Summing firm receipts gives $\min(1,kq)\leq1$, proving that every attainable vector obeys (2).

To prove that these conditions suffice, take any vector $r$ satisfying (2) and suppose $h>0$. For each member with $r_i>0$, create a firm type with value weight $r_i$. Give it sales share $s_i/r_i$ in member $i$, no sales in other member markets, and allocate the remaining share to nonmembers in proportions $s_j/h$. Because $1/k\leq s_i/r_i\leq1$, that type pays its full charge to member $i$. Give the remaining value weight $1-\sum_i r_i$ only nonmember sales, in those same proportions.

All weights and sales shares are nonnegative. Member $i$ has mean sales $r_i(s_i/r_i)=s_i$ and receipt $r_i$. The total nonmember sales mass is

$$
\sum_{i\in M}(r_i-s_i)+1-\sum_{i\in M}r_i=1-S=h,
$$

so nonmember $j$ has mean sales $s_j$ as required. If $r_i=0$, then $s_i=0$ and that type is omitted. If $h=0$, the constraints force $r_i=s_i$ and the common profile attains that vector. Empty coalitions and zero member exposures have zero receipts under the same convention. This establishes the complete set for a single group and fixed coalition.

The individual upper bound follows by combining $r_i\leq ks_i$ with $r_i\leq1-\sum_{j\in M,j\ne i}s_j=s_i+h$. It is attained by setting all other members at their lower bounds and applying the construction. For the total, $\min(1,kq)\geq q$ gives the lower bound, while concavity gives the upper bound $E[\min(1,kq)]\leq\min(1,kE[q])$. The destination-only and common-profile populations attain the respective bounds. Convex mixtures preserve the mean and interpolate their receipts.

## Appendix B. Weighting and membership

Let $R_f>0$, $t_f=V_f/R_f$, and let $E_R$ weight firms by $R_f/\sum R_f$. Then

$$
E_V[x]=\frac{E_R[tx]}{E_R[t]}
=E_R[x]+\frac{\operatorname{Cov}_R(t,x)}{E_R[t]},
$$

which proves (4). If positive-value, zero-revenue firms exist, write the overall value mean as the value-weighted combination of this positive-revenue population and a separate zero-revenue population. The identity alone supplies neither that population's value share nor its exposure.

With the additional assumptions $0<\ell\leq t\leq u$ and revenue-weighted coalition exposure $m$, one can bound the value-weighted exposure by

$$
\frac{\ell m}{\ell m+u(1-m)}
\leq \mu_V \leq
\frac{um}{um+\ell(1-m)}.
$$

For the upper bound, $E_R[tx]\leq um$ and $E_R[t(1-x)]\geq\ell(1-m)$; the ratio of the first quantity to their sum is increasing in the first and decreasing in the second. Reversing these inequalities gives the lower bound. Exposure-zero and exposure-one firms with extreme ratios attain both endpoints. The two-firm example in Section 5 verifies the case $m=1/2$, $\ell=1$, $u=3$. These ratio bounds are extra assumptions, not an empirical interval for the source data.

Finally, adding a member raises each firm's $q$, so $\min(1,kq)$ cannot fall. For an incumbent with unchanged $x_i$, its multiplier $\min(k,1/q)$ cannot rise; firms with initial $q=0$ also have $x_i=0$. Summation with the same nonnegative firm weights proves the total and incumbent monotonicity statements. Comparing different endpoint populations before and after entry would not prove them.
