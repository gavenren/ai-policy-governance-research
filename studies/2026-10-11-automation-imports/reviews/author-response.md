# Author response to separate AI review

State: Working notes. Response time: 2026-10-11T21:07:33Z.

The reviewer is the parent agent in this task. It did not author the central model. It inspected the model and manuscript and independently checked all 1,296 resource identities and key results. This is AI critical review, not human or journal peer review. The reviewer will save its own scope and record separately.

| Issue | Response and disposition |
| --- | --- |
| Actual levy payments were labelled ambiguously | Corrected. `gross_levy_payments=t*q` and `usable_levy_receipts=e*t*q` are now separate output columns. Public income adds usable receipts once and deducts the fixed cost once. The data dictionary and paper use these definitions. |
| The no-positive-levy proof must cover `e<=lambda`, where the quadratic need not be concave | Corrected in Proposition 1. The identity `Delta W=(e-lambda)*t*q-lambda*t*t/(2*B)-K` proves strict loss for every positive tax in the domain. The proof does not assume concavity in this branch. |
| Domestic gain must not be described as global gain or a Pareto gain | Addressed in Sections 1, 5, 6, and 7. Equation 12 and an independent identity test show negative global surplus for every positive levy. Domestic private owners also lose. An aggregate domestic gain does not imply that every resident gains. |
| Collection losses need an exact economic meaning | Corrected in Section 3.2 and the dictionary. The missing payment share is a real resource cost. It is not evasion, wages, a retained supplier payment, or a domestic transfer. Evasion that removes the price wedge is outside this model. |
| Novelty must be bounded against Becker and Wossnig | Addressed in Section 2. Tax incidence, foreign ownership, interactions between tax bases, and fiscal-versus-welfare maxima are established. The contribution is a compact joint-feasibility test and reproducible synthesis, with only a modest possible extension. No first-ever claim remains. |

All reported outputs were regenerated after the naming change. Eight tests passed. The final review and release decision belong in the separate review record and completion gates. No GitHub publication is claimed by this author agent.
