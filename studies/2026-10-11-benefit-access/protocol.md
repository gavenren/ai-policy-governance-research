# S007 study protocol and decision record

State: Working notes. Recorded 2026-10-11T21:01:00Z, before model execution. This is an exploratory design record, not a preregistration.

Question: When an automated benefit system denies eligible claims, what review capacity and public cash cover are needed to prevent payment gaps? Compare payment after review with automatic advances to all unresolved denied claims. The model concerns the administration of a funded transfer, not whether the economy produces enough goods or raises sufficient underlying revenue.

Unit: a one-period benefit claim of fixed amount. Arrivals are distinct person-period claims; a person can have more than one claim over time. Keep queue delay exposure separate from unique persons and measured consumption deprivation. Inputs will be synthetic, without empirical calibration. Ineligible claims include errors and mistaken applications; intent to defraud is not inferred.

Planned model: a deterministic finite-horizon FIFO queue of eligible and ineligible denied claims. Review has finite per-period capacity and gives a correct final decision. A common outage can increase false denials and reduce review capacity. Both payment rules use the same queue. Advances remove eligible withholding but require cash for ineligible claims, with a specified recovery share. Derive exact cash-flow identities and a finite reserve test. Separate replenishable working cash from permanent public losses. Include terminal arrears and unresolved advances.

Planned checks: analytical boundaries with zero denials, zero ineligible claims, zero capacity, full same-period review, and complete recovery; independent small-case accounting; short and long outages; lower false-denial accuracy paired with faster review; stable-queue counterexample; exhaustive finite stress grid. End-period netting will be explicit. A conservative gross-before-recovery requirement will be reported separately. No inference will be made about actual fraud prevalence, real error rates, benefit adequacy, or legal compliance.

Search scope: public primary research and official delivery-system or audit documents. Search queueing access, take-up, administrative burden, automated welfare, advance payments, and processing delays with several formulations. Read the closest model. Keep short inspectable extracts and hashes of local original captures. Search snippets are discovery aids only. Stop source expansion when the main prior-work overlaps and needed institutional mechanisms have primary support; this is not an exhaustive review.

Contribution boundary before analysis: benefit queueing, advance payments, and administrative burden already have prior work. The proposed increment is a transparent joint queue-and-payment rule with exact reserve accounting, matched rules, and a counterexample to using queue stability as a sufficient payment-guarantee test.

S004 studies equilibrium consumption floors, fiscal capture, and scarce essential goods. S007 conditions on a funded benefit and holds goods prices and supply fixed. It examines denial, review, and payment time. S005 and S006 are concurrent separate studies; S007 does not claim priority over them.

No jurisdiction-specific legal recommendation is tested. The payment guarantee and review rules are research proposals. Existing reports are cited for their stated findings and dates only, not as proof of current law. No full source redistribution or reuse licence is authorized by this record.

The stopping rule is a manuscript, fully executed reproducible model, all planned results, provenance and source comparisons, and independent AI review with responses. Complete-study status requires all programme gates. Git changes and publication are handled by the lead agent.

## Changes after this record

- By 2026-10-11T21:05:14Z: distinguish eligible funds already due from extra reserves for ineligible advances. An appeal-only spending comparison includes unpaid eligible entitlements, but the fully funded reserve test excludes that double count.
- By 2026-10-11T21:05:14Z: add Rule J, which advances only claims still open at arrival-period end. This was an exploratory adverse check on blanket initial advances. It has equal measured end-period payment and weakly lower net cash exposure under the model assumptions.
- By 2026-10-11T21:05:14Z: remove duplicate expanded paths from the initial 729-row grid. Inactive surge sizes under zero outage created duplicates. Final analysis contains 567 distinct path/recovery settings. Initial analysis was exploratory; the change is not outcome-based case exclusion.
- By 2026-10-11T21:07:50Z: add the stable positive-backlog named case and explicit within-period, funding-knowledge, and metric-timing limits after early independent feedback. Results remain synthetic. Twelve tests and twelve named cases are final at this stage.
- 2026-10-11T21:07:50Z: record seven-source cutoff at 2026-10-11T21:05:14Z. Historical web-search event timestamps were not exposed by the tool. Exact capture times are retained; missing search-second precision is disclosed in the search log.

The model was not changed to fit empirical values. No primary outcome was dropped after an unfavorable result. The manuscript reports the case where blanket advances add losses without improving measured access, and the timing case where separated shocks cause more observed delay than overlapping shocks.
