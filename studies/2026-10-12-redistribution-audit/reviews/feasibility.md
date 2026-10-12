# Independent feasibility review

Review completed: 12 October 2026, 10:57 UTC. Reviewer: a separate AI review agent. This note checks the source and algebra. It is not a review of a new study's code or final paper. The reviewer did not write central study code or a manuscript.

## Decision

A bounded technical comment has a valid purpose. It can correct a claim about normalized income variance and an exact log identity, state a needed condition for a factor-share limit, and retain a consumption-tax result that survives the check. These are elementary mathematical checks applied to one identified paper. They are not new inequality theorems, a complete review of AI policy, or evidence that the paper's broad policy conclusion is false.

## Source and version checks

The source is Growiec, Prettner and Szkróbka, *Redistributive Policies for the Times of Transformative AI*, [arXiv:2609.14750v1](https://arxiv.org/abs/2609.14750v1), submitted 13 September 2026. At this check, the unpinned arXiv abstract page showed only version 1. The [lead author's publication page](https://e-web.sgh.waw.pl/jg23234/pub.html) linked that paper. A bounded search for the title, identifier, revision and correction did not find a later version or a correction. This does not prove that no other version exists.

I read the relevant model and policy sections in the [HTML](https://arxiv.org/html/2609.14750v1), PDF text, and original TeX source. I also read the relevant model and full-automation section of the cited [Growiec growth paper](https://e-web.sgh.waw.pl/jg23234/Growiec%20SNDE.pdf). The PDF and TeX agree on the equations at issue. A PDF image check was unavailable; I do not claim visual inspection of the rendered equations.

Private captures were made at 2026-10-12T09:54:33Z. Their SHA-256 values are:

| File | SHA-256 |
|---|---|
| Pinned v1 PDF | `da862941daf8ccd7a1c3809ad55e02824a5e2c18733ceeb198cacd1108520b6d` |
| Pinned v1 source archive | `22b80c7b465fd515f815199e180b025d11a0dbe659b274cd3437ad134760ea44` |
| Author copy of Growiec (2023) | `8557f48153eab670bd1ab59a3e6beb07ad2df725cd10949f77da8889a2ec2732` |

The TeX archive contains a file named `ubi_v2.tex`. That internal filename is not evidence of an arXiv version 2. Acquisition details and full source bytes remain in ignored `.local-sources/redistribution-audit/feasibility-20261012/`. This review does not publish the full source documents.

## 1. Equal UBI and normalized variance: a clear error

The paper defines the tilde variable as income divided by its cross-sectional mean in Section 2.2, pages 5–6. Section 3.1, page 11, then calls an equal addition neutral for that variance. [Source: definitions and UBI discussion](https://arxiv.org/pdf/2609.14750v1#page=11).

Let income be X, with mean μ > 0 and finite variance v. For a common addition b > 0,

\[
\operatorname{Var}\left(\frac{X+b}{\mu+b}\right)
=\frac{v}{(\mu+b)^2}
=\left(\frac{\mu}{\mu+b}\right)^2
\operatorname{Var}\left(\frac X\mu\right).
\]

Thus the stated measure strictly falls if v > 0. For two equally weighted incomes (1, 3), it falls from 1/4 to 1/9 after adding 1 to each income. The raw variance stays 1. This result does not need a claim about how the transfer is funded.

The strongest repair is to distinguish raw variance from normalized variance. Holding a pre-policy denominator fixed would also give neutrality, but it would change the paper's stated measure. The phrase “de-meaned” elsewhere does not resolve the issue: the explicit ratio and scale-free aim identify the measure. Equation 10 can remain valid; the transfer changes its mean-income denominator.

There is a related aggregate-versus-individual issue in equation 17. If x_i = z_i + b and b = u mean(x), with 0 ≤ u < 1, then mean(x) = mean(z)/(1−u), but normalized variance falls by (1−u)². Scaling each z_i by 1/(1−u) gives the same aggregate and a different distribution. An aggregate rewrite alone cannot establish their distributional equivalence.

## 2. Equation 4: not an exact consequence of constant returns

Section 2.2.1, page 5, presents a factor-share-weighted log identity. [Source: equations 4–7](https://arxiv.org/pdf/2609.14750v1#page=5).

Euler's theorem gives Y = Σ_j F_j x_j for a differentiable constant-returns production function. It does not give ln Y = Σ_j π_j ln x_j. The exact local differential is d ln Y = Σ_j π_j d ln x_j.

A counterexample uses the paper's nested CES form: α = β = 1/2, θ = −1, ω = 1, K = 1, H = AI = 2. Then S = 2, Y = 4/3 and the three shares are (2/3, 1/6, 1/6). The proposed right side is (ln 2)/3, whereas the left side is ln(4/3). They differ. At K = H = AI = 1 the residual is zero, so a single fixed intercept does not repair the identity across these points.

A local approximation around a stated reference point is a valid repair. A fixed-share weighted log endowment index is another possible definition. Its variance formula can be exact for that index. Neither repair makes it an exact global CES output identity. The income accounting in equations 8–10 does not depend on accepting equation 4.

## 3. Capital's limit share: conditional, with support in the cited model

Equation 15, Section 2.5, page 9, gives a unit capital-share limit. [Source: the TAI scenario](https://arxiv.org/pdf/2609.14750v1#page=9).

For the stated outer CES with 0 < α < 1 and θ < 0,

\[
\pi_K=\frac{1}{1+[(1-\alpha)/\alpha](S/K)^\theta}.
\]

Therefore π_K tends to 1 if and only if S/K tends to infinity. A vanishing human-labor share alone does not supply that condition. For example, set α = β = 1/2, θ = −1, ω = 1, H = 1, K = exp(t), and AI = 2 exp(t) − 1 for t ≥ 0. Then S = Y = exp(t), π_K = 1/2, π_H = exp(−t)/4 → 0, and π_AI → 1/2. This is a counterexample to an inference from labor disappearance alone, not to a model that also requires S/K → infinity.

The strongest supporting interpretation matters. In Growiec (2023), Section 3, author-copy page 10, equations 15–17, cognitive input is asymptotically proportional to A K. The stated limit has A → infinity. This supplies the relative-input condition. [Source: full automation in the cited growth model](https://e-web.sgh.waw.pl/jg23234/Growiec%20SNDE.pdf#page=10).

The right treatment is to state this condition and test its scope. Do not call the unit limit generally false or claim that the authors give no basis for it. Equal limiting growth rates also do not, by themselves, imply a constant ratio: S = t exp(t) and K = exp(t) give equal limiting growth rates but S/K → infinity.

## 4. Consumption tax with an equal rebate: retain the valid result

Section 3.6, page 18, explicitly combines a common saving rate, a consumption tax and an equal UBI rebate. [Source: equations 22–24](https://arxiv.org/pdf/2609.14750v1#page=18).

Let pre-policy income z_i have mean μ. Write d = 1 + (1−s)τ and x_i = (z_i + b)/d. With the full tax revenue returned equally, budget balance gives b = (d−1) mean(x). Hence mean(x) = μ and

\[
x_i=\mu+\frac{z_i-\mu}{d},\qquad
\operatorname{Var}(x_i/\mu)=d^{-2}\operatorname{Var}(z_i/\mu).
\]

For z = (1, 3), s = 0 and τ = 1, the rebate is 2 and final income is (1.5, 2.5). Normalized variance falls from 1/4 to 1/16. This confirms the tax-plus-rebate mechanism under fixed pre-policy incomes, full rebates and a common saving rate.

With b fixed instead, division by d alone leaves normalized variance unchanged. This scaling fact is a useful control, but it is not a refutation of the stated rebate policy. A comment must show both cases. It must not use heterogeneous saving rates to disprove a claim that assumes a common rate. Such a case would be an extension.

## Scope and next checks

The contribution is a version-specific consistency audit with explicit repairs. A small reproducible study can use exact examples, random positive-income checks, the CES residual, and relative-input paths. It should keep failed objections in the results, particularly the valid rebate case. It should also state that these calculations do not rank policies in general equilibrium, establish an optimal tax, or measure future inequality.

The full paper's references, empirical context, other policy rankings and legal feasibility have not been audited here. No numerical study output was reviewed. A separate reviewer should check the later manuscript and code, including the policy budget and the population weights used for variance. The exploratory protocol must record that these algebraic concerns were known before numerical execution; it must not describe their discovery as preregistered.
