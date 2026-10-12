# Measuring the AI Dividend
## A consistency audit of equal transfers, production shares and tax rebates

**Study S012 · Complete-study draft · 12 October 2026**

This is an AI-assisted technical comment on one identified preprint version. All numerical populations are synthetic. It is not an estimate of future inequality or a general ranking of economic policies. Separate AI feasibility and critical reviews, independent arithmetic checks and an author response are available. No human or journal peer review has occurred. Source retrievals used for the initial analysis were completed by **2026-10-12T09:54:33Z**. Later version checks are recorded separately.

### Abstract

Debates about an economy with little paid human work often ask whether a universal cash payment can distribute the gains from AI. The answer depends in part on the definition of inequality and on how the payment is financed. This comment audits four selected claims in Growiec, Prettner and Szkróbka's *Redistributive Policies for the Times of Transformative AI*, arXiv:2609.14750v1. Two claims require correction. An equal addition leaves income variance in currency units unchanged, but reduces the variance of income divided by its new mean. A factor-share-weighted sum of log inputs is also not an exact identity for the paper's nested CES production function. Two other results survive with their conditions made explicit. The capital share tends to one when cognitive input grows without bound relative to physical capital, a condition supported by the cited growth model. A consumption tax returned through an equal rebate reduces relative inequality under a common saving rate and fixed pre-policy incomes. We provide algebra, reproducible examples, tests that support the source, and repairs that preserve useful parts of its framework. The contribution is a version-specific audit, not a new theory of inequality.

### 1. Why the measure matters

Suppose two people receive incomes of 1 and 3. The second person receives three times as much as the first. Now give each person 1. Their incomes become 2 and 4. The gap is still 2, but the second person now receives twice as much. An analysis that measures gaps in currency units can therefore reach a different result from one that measures incomes relative to the population mean.

This distinction is central to a debate about AI dividends. If human labor earns little income, a common payment may become a large part of many people's resources. Calling that payment neutral for inequality can lead readers to miss its direct effect on relative incomes. Yet showing that it reduces relative inequality does not show that it is affordable, sufficient for basic needs, or desirable after its tax and price effects are included. Those are further questions.

Growiec, Prettner and Szkróbka [1] provide a useful organizing framework for this debate. Their paper compares redistribution through income, capital ownership and several tax bases in possible AI economies. We examine four selected mathematical claims in version 1. The selection followed close reading and suspected inconsistencies; it was not a random sample of propositions. This comment should therefore be read as a focused audit, not as a score for the whole paper.

The central distinction between absolute and relative inequality is established. Cowell [2] sets out the relevant families of measures and distinguishes properties of inequality orderings from stronger requirements that index values remain unchanged. We use explicit definitions below to avoid ambiguity. Our contribution is to apply those definitions to this preprint, retain the claims that withstand scrutiny, and provide a small reproducible record of the checks.

| Audited item in [1] | Finding | Repair or condition |
|---|---|---|
| Section 3.1: an equal UBI addition and normalized variance | Error as stated | Separate variance in currency units from variance divided by the new mean squared. |
| Section 2.2.1, equation 4: exact factor-share log identity | Error as stated for the nested CES example | Use a local log approximation, or explicitly define a fixed-share log index. |
| Section 2.5, equation 15: capital's limiting share is one | Conditional, with a supporting model | State that cognitive input becomes unbounded relative to physical capital. The cited growth model supplies this condition. |
| Section 3.6: consumption tax returned equally | Valid under the stated common-saving setup | Solve the rebate and the income mean jointly. Retain fixed pre-policy income and the common saving rate. |

The table separates correction from clarification. In particular, a successful critique of the first two items does not disprove the last two or establish that public capital ownership is inferior to cash transfers.

### 2. Cash can change relative inequality without changing the currency gap

Let each of n people have nonnegative income x_i. Let μ be the mean and V the population variance. We require μ > 0. The source defines normalized income as income divided by its cross-sectional mean. The corresponding variance is

\[
I(x)=\operatorname{Var}(x_i/\mu)=V/\mu^2.
\tag{1}
\]

This is the squared coefficient of variation. It is a relative measure: doubling everyone's income leaves its value unchanged. The ordinary variance V is different. It is measured in squared currency units and increases fourfold when every income doubles.

Section 3.1 of [1] states that “UBI alone is neutral for inequality,” then applies that claim to the variance of normalized income. Its partial-equilibrium experiment adds the same amount b to every person's income. The variance in currency units is unchanged, but the mean rises from μ to μ+b. Thus

\[
I(x+b)=\left(\frac{\mu}{\mu+b}\right)^2 I(x).
\tag{2}
\]

If b > 0 and the initial incomes are unequal, the right side is strictly smaller. This is a correction to the stated measure. It does not depend on an assumption that government can obtain free resources. The source first isolates the effect of an addition and then asks how it is financed; equation (2) addresses that same isolated operation. A complete policy must next include the funding mechanism.

The two-person example makes the difference visible. At incomes (1,3), the mean is 2 and the variance is 1, so I=1/4. After an equal addition of 1, the mean is 3 and the variance remains 1, so I=1/9. The relative measure falls by 55.6%. The Gini coefficient also falls, from 1/4 to 1/6. No person's income falls in this arithmetic example.

| Operation on incomes (1,3) | Final incomes | Mean | Raw variance | Relative variance I | Gini |
|---|---:|---:|---:|---:|---:|
| No change | (1,3) | 2 | 1 | 0.2500 | 0.2500 |
| Add 1 to each | (2,4) | 3 | 1 | 0.1111 | 0.1667 |
| Double each income | (2,6) | 4 | 4 | 0.2500 | 0.2500 |
| Equal rebate from the consumption tax in Section 5 | (1.5,2.5) | 2 | 0.25 | 0.0625 | 0.1250 |

*Source: executed synthetic examples in `results/worked_examples.csv`. Units are arbitrary. The final row includes both the tax and its rebate; the equal-addition row does not specify funding.*

The most direct repair is to replace the neutrality statement with equation (2), while retaining the need to analyze funding. Alternatively, neutrality could be stated for raw variance. Holding the pre-policy mean fixed in the denominator would also make the addition neutral, but that would define a different index from the one in [1].

The source's income covariance equation need not be discarded. Its equation 10 divides the covariance of net factor incomes by mean disposable income squared. An equal transfer does not enter the covariance numerator. It does enter the denominator. Updating that denominator restores the direct transfer effect. Our four component examples confirm the covariance calculation, including a case with negative covariance and a case with a zero income component. The zero component is handled in levels, without dividing it by its zero mean.

#### Indexation requires household accounting

The same issue appears when a payment is linked to aggregate income. Let z_i be income before an added payment, and let every person receive b=uμ_x, where μ_x is the final income mean and 0≤u<1. Averaging x_i=z_i+b gives μ_x=μ_z/(1−u). At the individual level, however, the operation remains an equal addition. It yields

\[
I(x)=(1-u)^2 I(z).
\tag{3}
\]

Multiplying every z_i by 1/(1−u) produces the same aggregate income but leaves relative inequality unchanged. An aggregate rearrangement therefore cannot establish that the two distributions are equivalent. With z=(1,3) and u=1/4, an equal indexed payment gives incomes (5/3,11/3) and I=9/64. Proportional scaling gives (4/3,4) and I=1/4. Both means are 8/3. This clarifies the distributional limit of the aggregate rewrite in equation 17 of [1]; it does not supply a financing model for either operation.

### 3. Production shares describe local changes, not a global log identity

The source uses a nested constant-elasticity-of-substitution production function. Physical capital K combines with cognitive input S. Cognitive input in turn combines human input H and AI services. The full equations are in Appendix B.

For a differentiable production function with constant returns to scale, Euler's theorem gives an exact identity in levels: output equals the sum of each input multiplied by its marginal product. Under competitive factor payments, each factor's income share is also its output elasticity. These statements support a local growth-accounting equation. They do not generally imply that the level of log output equals a share-weighted sum of log input levels.

Equation 4 of [1] uses the latter expression as an exact identity. A small example within its own CES specification is sufficient to show the problem. Set both share parameters to one half, the outer exponent to −1, the inner exponent to 1, and let K=1 and H=AI=2. Cognitive input is then 2 and output is 4/3. The three marginal shares are 2/3, 1/6 and 1/6. But

\[
\ln(4/3)\ne\frac{2}{3}\ln 1+\frac{1}{6}\ln 2+\frac{1}{6}\ln 2.
\tag{4}
\]

The left side is approximately 0.287682; the right side is 0.231049. At K=H=AI=1, both sides are zero. A single constant intercept cannot repair the expression at both points while retaining the stated shares.

Two useful repairs are available. First, a local approximation around a specified reference point can use the reference shares to predict a small change in log output. This is ordinary first-order calculus. For larger changes, the shares change along the path and cannot generally be held fixed. Second, a researcher may define a fixed-share weighted log endowment index. The variance of that defined index has an exact covariance decomposition. It must be identified as an index, rather than as an exact CES production identity or a person's actual income.

The numerical checks preserve these repairs. Across 2,187 planned CES cases, 1,944 have an absolute log-identity residual above 10^−10. This fraction describes a constructed grid, not the frequency of an error in real economies. The exact example already disproves the universal identity. In contrast, the local output elasticities agree with centered finite differences to within 5.30×10^−11. A fixed-share log-index variance also agrees with its covariance decomposition. These controls identify what is valid in the source's method.

This distinction matters for interpretation of ownership. A decomposition of a declared index can summarize differences in asset holdings. To treat it as a decomposition of actual disposable income requires a payment and ownership model. The source already has a separate income-accounting equation that can serve that purpose. Correcting the log identity therefore need not remove its entire analysis of income distribution.

### 4. The disappearance of labor does not, by itself, identify the remaining rent

When AI replaces human work, it is tempting to infer immediately that physical capital receives all output. In the source's outer CES, however, that conclusion has a precise relative-supply condition. With 0<α<1 and θ<0, the capital share can be written as

\[
\pi_K=\frac{\alpha}{\alpha+(1-\alpha)(S/K)^\theta}.
\tag{5}
\]

It approaches one if and only if S/K grows without bound. Human labor can become negligible while cognitive input and physical capital remain in a fixed ratio. In that case the capital share remains below one, and a positive share can still accrue to AI services.

A simple input path shows the distinction. Use the same CES parameters as Section 3, set K=exp(t), H=1 and AI=2exp(t)−1. Then S=K, output is K, and capital's share stays at one half. The human share falls to zero and the AI share approaches one half. This is a path through the production function, not a solved general-equilibrium path. It establishes only that labor disappearance is insufficient as a mathematical premise.

The strongest supporting interpretation of the source is also available. The growth model it cites, Growiec [3], makes cognitive input asymptotically proportional to A K in its full-automation case, with A growing without bound. That additional condition makes S/K unbounded and supplies the limit used in [1]. It would therefore be incorrect to report that the source has no basis for its capital-share result. The useful clarification is to state the relative-input condition directly when moving from the growth model to policy comparisons.

Nor do equal limiting growth rates prove a fixed input ratio. For example, K=exp(t) and S=(1+t)exp(t) have the same limiting growth rate, but S/K=1+t diverges. Our calculations include this path, the constant-ratio path and an exponential-ratio path. They support the unit capital-share limit for the two unbounded ratios and retain a nonunit share for the constant ratio.

For economic governance, the implication is conditional. A policy that taxes physical capital rents needs an argument that those rents remain the relevant base. A policy that taxes AI services needs an argument about the continued value of those services. The label “full automation” does not itself resolve that allocation. The relative-input condition does so within this CES model; other market structures need their own analysis.

### 5. A consumption tax can reduce relative inequality through its rebate

One possible objection to Section 3.6 of [1] does not survive a full reading. Dividing every income by a common tax factor cannot, by itself, reduce relative inequality. But the section does more than impose a common divisor. It states that the tax proceeds are returned through an equal UBI payment.

Let z_i be fixed pre-policy income, let s be the common saving rate, and let τ be the consumption-tax rate. Define d=1+τ(1−s). The household budget is d x_i=z_i+b. If all tax revenue is returned equally, b=(d−1)μ_x. Taking means gives μ_x=μ_z and therefore

\[
x_i=\mu_z+\frac{z_i-\mu_z}{d},\qquad
I(x)=\frac{I(z)}{d^2}.
\tag{6}
\]

The equal rebate and tax together bring each income closer to the original mean. For z=(1,3), s=0 and τ=1, the rebate is 2 per person, and final incomes are (1.5,2.5). Relative variance falls from 1/4 to 1/16. The tax rate of 1 is deliberately simple arithmetic, not a recommended rate. The common mean remains 2 because this is a balanced transfer within a fixed population with fixed pre-policy resources.

The 120 planned common-saving cases reproduce this result, including the boundaries τ=0 and s=1. In the latter case nobody consumes in the model, the tax raises no revenue, and inequality is unchanged. The matching no-rebate control simply scales every income by 1/d and leaves relative inequality unchanged. The two cases must not be confused. The result in [1] is valid for its tax-plus-rebate setup; this comment does not verify every comparison with capital taxes or its long-run behavioral assumptions.

#### A boundary outside the common-saving assumption

Different saving rates can change the result. This is an extension, not a refutation of the stated common-saving model. Consider incomes (1,9), a tax rate of 1, and fixed saving rates (0,1). Only the lower-income person consumes. Solving the same balanced-budget equations gives a common rebate of 1/3 and final incomes (2/3,28/3). Relative variance rises from 0.64 to about 0.7511. Reversing the saving rates gives final incomes (4,6) and lowers relative variance to 0.04.

These extreme examples isolate the role of the tax base. They do not model realistic saving decisions, lifetime consumption, borrowing, changes in prices or returns, or a transition to full automation. They show why applying the common-saving result to a heterogeneous population requires more evidence. An equal rebate can coexist with a regressive net transfer if the tax base is concentrated among lower-income recipients in the chosen period.

### 6. What the audit changes, and what it leaves open

The first correction changes the immediate description of a universal cash payment. Equal cash additions reduce the source's chosen relative inequality measure before their funding effects are included. The second correction changes the status of a decomposition: an exact statement about a defined log index or a local approximation cannot silently become an exact global statement about CES output.

Neither correction makes the larger policy problem simple. A low inequality index can coexist with low living standards. A funded nominal payment can buy little if essential goods remain scarce. A transfer can arrive too late to meet a debt payment. Conversely, a policy can raise average income while increasing a relative inequality index. The audit measures none of these additional outcomes. Earlier studies in this programme examine essential supply, payment access, fiscal risk and household debt; they should not be replaced by a single inequality statistic.

For a usable policy model, three pieces of accounting must remain connected. The first is the household distribution before and after the policy. The second is the government budget, including who pays and who receives. The third is the production and price response. This comment checks small parts of the first two and the internal calculus of one production function. A general-equilibrium policy ranking requires the third, with explicit saving, investment, ownership and market assumptions.

Our evidence has deliberate limits. The source is one public preprint version. The audit covers four selected claims and related controls. All numerical cases are synthetic and equally weighted. There is no empirical sample, uncertainty interval, causal estimate or forecast. The search for prior corrections was bounded, and we do not claim first discovery. The useful output is a transparent correction record that another reader can reproduce or challenge.

### Appendix A. Definitions and transfer identities

For nonnegative incomes with μ>0, define

\[
\mu=\frac1n\sum_i x_i,\quad
V=\frac1n\sum_i(x_i-\mu)^2,\quad
I=V/\mu^2,\quad
G=\frac{\sum_i\sum_j|x_i-x_j|}{2n^2\mu}.
\tag{A1}
\]

The variance uses denominator n. There is no sampling correction. For y_i=a x_i+b, with a≥0, b≥0 and aμ+b>0,

\[
\mu_y=a\mu+b,\quad V_y=a^2V,\quad
I(y)=\left(\frac{a\mu}{a\mu+b}\right)^2 I(x),\quad
G(y)=\frac{a\mu}{a\mu+b}G(x).
\tag{A2}
\]

These results follow by subtracting the new mean for variance and subtracting each pair of incomes for Gini. At b=0 and a>0, both relative indices are unchanged. At a=0 and b>0, all incomes are equal. A zero mean is excluded because the relative indices are undefined. The Gini convention here applies to nonnegative incomes; we do not extend it to negative incomes.

For net income x_i=Σ_j c_j z_ij+b, with constant component multipliers c_j,

\[
I(x)=\frac{\sum_j\sum_k c_jc_k\operatorname{Cov}(z_j,z_k)}{\mu_x^2}.
\tag{A3}
\]

This levels expression remains defined when a component mean is zero. It is the direct covariance form behind the source's normalized-component equation 10. A uniform b changes μ_x but not the numerator.

For heterogeneous saving rates, put d_i=1+τ(1−s_i). Solving x_i=(z_i+b)/d_i with n b=Σ_i(d_i−1)x_i gives

\[
b=\frac{\sum_i z_i-\sum_i z_i/d_i}{\sum_i 1/d_i}.
\tag{A4}
\]

This is the equation used for the boundary examples. It also yields the common-saving case when all d_i are equal. Income in these tax examples is the source's tax-exclusive resource concept; it is not pre-tax nominal receipts or consumption alone.

### Appendix B. Production identities and repairs

The audited CES specification is

\[
S=[\beta H^\omega+(1-\beta)AI^\omega]^{1/\omega},\qquad
Y=[\alpha K^\theta+(1-\alpha)S^\theta]^{1/\theta}.
\tag{B1}
\]

With positive inputs, the marginal elasticities are

\[
\pi_K=\alpha(K/Y)^\theta,\quad
\pi_H=(1-\alpha)\beta(S/Y)^\theta(H/S)^\omega,\quad
\pi_{AI}=(1-\alpha)(1-\beta)(S/Y)^\theta(AI/S)^\omega.
\tag{B2}
\]

They sum to one. Euler's level identity and the exact local differential are

\[
Y=F_KK+F_HH+F_{AI}AI,\qquad
d\ln Y=\pi_Kd\ln K+\pi_Hd\ln H+\pi_{AI}d\ln AI.
\tag{B3}
\]

For a finite movement along a smooth input path, integrate the differential with the changing shares. A fixed-share first-order approximation has a local remainder. In the planned direction (0.2,−0.1,0.3) in log inputs, the approximation error falls from 5.60×10^−5 at step 0.1 to 5.56×10^−11 at step 0.0001. This is a numerical check of the local repair, not a bound for every path.

Alternatively, define L_i=Σ_j p_j ln x_ij with fixed p_j. Then Var(L)=Σ_jΣ_k p_jp_k Cov(ln x_j,ln x_k) exactly. Subtracting the log of a common normalization constant does not change this variance. The defined index does not assert that household output or factor income follows that same formula.

### Appendix C. Execution and reproducibility

The design was recorded before numerical execution, after the algebraic issues had been identified. The public [protocol](protocol.md) makes that exploratory order explicit. The first run used Python 3.13.7 and only its standard library. It produced 72 affine cases, 120 common-saving tax cases, 200 seeded implementation checks, 2,187 CES cases, four local-approximation steps, 24 input-path points, four income covariance controls, one log-index control and eight worked examples. All planned outputs are retained. The seed is 20261012.

Maximum absolute formula errors were 4.44×10^−16 for the affine relative-variance identity, 8.88×10^−16 for the common-saving rebate identity and 5.56×10^−17 for the income covariance controls. The largest aggregate tax-budget residual was 2.27×10^−13 in arbitrary income units. These are floating-point errors. The 15 unit tests include exact rational benchmarks, zero-mean rejection, zero consumption, negative covariance, and the preserved capital-limit and tax-rebate results. A grid does not prove a theorem; the algebra supplies the general claims.

Run `python3 code/analyze.py` and `python3 -m unittest discover -s code -p 'test_*.py' -v` from this study directory. [The README](README.md) gives validation and source-check commands. Input and output hashes, software version and actual run time are in [the run record](results/run.json). Source versions, rights and locators are in [the evidence record](sources/evidence.md) and [manifest](sources/manifest.csv). The independent [feasibility review](reviews/feasibility.md) records both objections and supporting interpretations. The [critical review](reviews/critical-review.md) and [author response](reviews/author-response.md) record the completed checks and five corrected issues. The separate run reproduced all ten numerical files; independent fraction and high-precision checks covered the central affine, tax, CES, path and covariance results.

### References

1. Growiec, J., Prettner, K., and Szkróbka, M. (2026). *Redistributive Policies for the Times of Transformative AI*. arXiv:2609.14750v1, submitted 13 September 2026; PDF cover dated 15 September 2026. [Pinned paper](https://arxiv.org/abs/2609.14750v1), [PDF](https://arxiv.org/pdf/2609.14750v1). The claims above refer to this version.
2. Cowell, F. A. (2016). *Inequality and poverty measures*. In M. D. Adler and M. Fleurbaey (eds.), *The Oxford Handbook of Well-Being and Public Policy*. We consulted the author manuscript revised December 2014 and deposited in April 2016, particularly manuscript pages 18–22. [LSE repository record](https://researchonline.lse.ac.uk/id/eprint/66022/). The repository cautions that this version can differ from the published chapter.
3. Growiec, J. (2023). *What will drive global economic growth in the digital age?* *Studies in Nonlinear Dynamics & Econometrics*, 27, 335–354. DOI [10.1515/snde-2021-0079](https://doi.org/10.1515/snde-2021-0079). We consulted the author-hosted published-ahead-of-print copy, published online 24 June 2022, Section 3, PDF page 10, equations 15–17. [Author copy](https://e-web.sgh.waw.pl/jg23234/Growiec%20SNDE.pdf).

### Disclosure

Codex performed source retrieval, analysis, drafting and AI review. The paper has no asserted human authorship, institutional affiliation or endorsement. The commissioning user's funding and conflicts have not been independently established; no declaration is invented. No contact with the source authors, journal submission or human review has occurred. Errors remain possible. Third-party sources retain their own rights; no reuse licence is selected for this study.
