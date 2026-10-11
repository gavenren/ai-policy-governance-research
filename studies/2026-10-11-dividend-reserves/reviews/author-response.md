# S005 response to independent AI review

Date: 2026-10-11. Respondent: study author AI agent. Reviewer: separate coordinating AI agent, which did not write the central analysis. This is not human peer review. State remains **Working notes** until the coordinator completes release checks and records the review.

## 1. When do sold assets stop paying income?

**Issue:** A sale does not always remove income before settlement. The late-sale penalty could depend on that assumption.

**Response:** Accepted. Section 3 makes the main contract assumption explicit: income rights stop in period 1, while sale cash arrives later. Section 6.4 reports the alternative in which rights continue until receipt. `results/timing.csv` retains all 12 family/receipt/timing cases. For the joint set with receipt in period 4, a sale of the whole asset requires 24 units under early loss and 21 under retained rights. The paper states that the increase in required reserve disappears under retained rights. The early cash gap remains. `test_income_rights_timing_is_material` checks this distinction.

## 2. Finite horizon versus lasting solvency

**Issue:** A minimum reserve over eight periods does not establish a permanent income guarantee. Disposal also reduces future public income and control.

**Response:** Accepted. The abstract, Sections 6.4 and 8, and README limit the result to the stated horizon. The paper says a reserve can be spent only once and cannot be reset for free. Initial capital and cash are given without acquisition finance. The disposal-weight cases show that minimizing reserve cash is not a welfare criterion; at weight 1, no sale is preferred. Terminal asset and reserve requirements are proposed extensions, not completed tests.

## 3. Novelty and close prior work

**Issue:** Maximum-gap cash accounting, liquidity matching, and fund reserve-depletion tests already exist.

**Response:** Accepted. Section 2 identifies IMF cash-buffer guidance and APFC Trustees' Paper 10 as close prior work. Proposition 1 is explicitly called a budget identity, not a new finance theorem. The proposed contribution is limited to the reproducible combination of two revenue streams, permitted shock overlap, settlement delay, and foregone asset income. The main Prativadi manuscript was not retrieved; the comparison is limited to the accessible original model specification and README. Search coverage is selective, and per-query timestamps were not retained. These limits remain public.

## 4. Shock sets and correlation

**Issue:** The three shock families must not be presented as measured correlations or probability distributions.

**Response:** Accepted. Sections 3 and 5 call them uncertainty sets with no probabilities. The unrestricted set does not imply statistical independence. The paper explains that the sets overlap, and the 11,979 family/path rows are not 11,979 distinct economic histories. No pass rate or confidence level is reported. `test_no_overlap_certificate_fails_joint_path` demonstrates failure when the smaller set excludes a material state.

## Independent check reported by the reviewer

The reviewer reported a separate reconstruction of all 11,979 retained path rows, with a maximum difference of approximately 4.93e-10 due to CSV rounding. The reviewer also derived both base-case intersections and the late-sale lower bound by hand. These actions belong to the review, not to the author-run test suite. The separate critical-review file records its scope, content hashes, tools, and limitations.

No blocking mathematical or numerical error was reported in the review message. This does not replace the remaining evidence and release checks or human peer review.
