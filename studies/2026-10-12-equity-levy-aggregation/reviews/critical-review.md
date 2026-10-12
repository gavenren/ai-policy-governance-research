# Separate AI critical review of S015

Frozen-version review recorded at **2026-10-12T18:03:29.613705Z**. This date is separate from the source-capture cutoff and the author's first run. This is an AI review, not human peer review.

## Review role and scope

The reviewer is a separate AI agent that did not author the central model, analysis script, numerical outputs, protocol or manuscript. The reviewer previously prepared the factual source package, source hash checker and feasibility assessment. The reviewer also discussed the hand-derived receipt set with the author before the numerical plan. This was a review with shared context, not a blind review. The review now includes execution of the author's model in a separate output directory and new calculation code that imports neither the author model nor the vendor model.

I read the full frozen manuscript, README, protocol and dated addendum, central code and tests, input file, output schema, saved witnesses and execution records. I checked all four output tables with separate exact calculations. I read the pinned source cap functions and constants again, read its DATA file in full, and checked the retained essay's Figure 3 footnote and caption again. The prior source-reading scope remains as recorded in the source ledger: the relevant essay sections, required source documentation, Loretz Sections 3.2.3–3.2.4 and conclusion with supporting passages, Hines's introduction and Section 3, and the first five PDF pages of Bertsimas–Popescu. I do not claim to have read all pages of those three research papers or to have verified their cited financial datasets.

## Finding

**No blocking error was found in the numerical results or proof.** The note has a valid, limited contribution as a quantitative information-limit extension to the pinned Figure 3 model. Two small text issues need correction before the release record is closed. The author accepted both at review time; this frozen-version record does not yet certify the later edits.

1. **Clarify full participation in Section 5.** The paragraph says that global participation still leaves recipient allocation unresolved. Under the note's value-weighted-mean assumptions, it fixes each member's receipt as well as the total: when no destination is outside the club, each firm's member receipt is its sales share. The unresolved recipient issue is real-world measurement and implementation outside those assumptions. State that distinction so this paragraph does not appear to weaken Equation (2) or Appendix A.
2. **Date the reviewer-role statement in the README.** It says the separate agent did not execute the central model. This was true before critical review. It is no longer true after the reproduction reported below. State that the agent did not execute it *before critical review*, and link the completed review scope. This is a disclosure correction, not an analysis change.

The initial research-state labels correctly say that review is pending. The author must change those labels and provide an issue-by-issue response when the review closes. Those release changes were not part of this frozen version.

## Mathematical and numerical assessment

The receipt-set argument is correct under its stated domain. For cap multiple at least one, each firm's positive-exposure member multiplier lies between one and the cap. This gives the individual lower and upper restrictions; the total charge gives the joint capacity restriction. The constructive converse preserves every destination mean, including all nonmember destinations. Its cases for zero member receipt, no nonmember sales and an empty coalition avoid division by zero. The construction requires arbitrary latent firm values and profiles; the paper states that restriction. It is not a bound for seven firms with seven known, fixed values.

The separate upper bound for a member follows by assigning all other members their minimum receipts and respecting both its cap restriction and remaining capacity. The source's coalition point is the total upper endpoint, but need not be a member's upper endpoint. The US-group example makes this distinction correctly: the US and EU separate uppers are 0.87 and 0.39, while their sum of 1.26 is infeasible. Both saved alternative firm populations reproduce all six original destination means exactly. They do not purport to attain both uppers at once.

The global coalition and cap-one cases have no aggregation gap under the fixed mean assumptions. The destination-only population attains all coalition-total lower endpoints with one fixed population. The common-profile population does the same for all upper endpoints. Marginal member endpoints for different coalitions need not share one population. The text states this distinction. Separate group constraints remain necessary for joint recipient choices after groups are added.

The membership claims compare the same firms before and after entry. Total collection weakly increases and an incumbent's receipt weakly decreases. The independent checks verified all saved entry rows and the identity that the total gain equals the joiner's receipt less incumbent losses. These claims do not establish a country's net incentive to join, treaty stability, or welfare.

The revenue-to-value weighting identity is correct for the positive-revenue population with positive total value. The covariance uses revenue weights. The two-firm examples give value-weighted exposures of one quarter and three quarters from the same revenue-weighted mean of one half. Positive-value, zero-revenue firms need the separate population described in the appendix. The optional ratio bounds require the stated positive lower and upper limits; they are not confidence intervals for the source inputs.

The separate arithmetic confirms the central broad US–EU interval of **$653.645–1,133.080 billion** per levy year. It also confirms all selected totals, the member intervals, the cap sensitivity and both global totals. The $126.71 trillion broad value is the source code's rounded input, not a substitution for its more precise documentary anchor. The $22 trillion tech basket is separate and overlaps the broad universe. No output adds them together.

## Checks actually run

The recorded checks ran from **2026-10-12T18:02:32.175145Z to 18:02:47.109512Z**, using **Python 3.12.14 and NumPy 2.3.5**. The [machine record](verification-record.json) contains commands, actual times, exit codes, output, input/code hashes and the separate reproduction run. The output-directory argument is normalized to a repository-relative path in the public record; the original record is retained in ignored local storage with its hash. No check was rerun for that path change. The record also confirms that the reviewed files stayed unchanged during execution.

| Check | Actual result |
|---|---|
| Author unit suite | All 15 tests passed. |
| Source checker with ignored local captures | 13 source records; 8 public vendor files and 19 local byte files matched; JSON and CSV ledgers matched. |
| Author analysis in a separate ignored directory | All seven deterministic output files matched the frozen results byte for byte. The original result timestamps were preserved. |
| Positive source replication | 13,824 collection cells and 2,304 ledger cells checked; largest recorded difference was approximately 1.110223×10⁻¹⁶ trillion. Upstream internal checks passed. |
| Author endpoint checks, reproduced | 4,608 total-endpoint populations and 6,912 separate member-upper populations passed. |
| Separate calculation script | All 384 configurations, 2,304 group rows, 1,152 member rows and 2,304 entry rows matched; 21,120 exact/decimal quantity pairs checked. |
| Separate boundary and construction checks | Both saved witnesses, 384 further boundary/interior construction cases and 1,584 single-firm necessity cases passed, including cap one and cap 1.5. |
| Separate weighting checks | Both positive-revenue covariance examples passed exactly. |

The separate [calculation script](independent_checks.py) copies the pinned source constants into review code, computes each firm's total bill first, then divides that bill among members. It does not import the author or vendor model. Its [results](independent-results.json) record the exact scope. The finite checks support the hand proof; they do not replace a proof or validate financial data.

## Source claims, contribution and presentation

The source caption and footnote explicitly say that Figure 3 applies the cap to group sales patterns. The manuscript preserves this favorable evidence and does not accuse the source of concealing aggregation. Its constructed-matrix, geographic-coverage, revenue-weighting, valuation-date and firm-coverage limits agree with the inspected source documentation. The condition needed to turn a source row into the theorem's mean is prominent in the abstract and main text.

The source files are unchanged and have the upstream MIT licence and copyright notice. The new study does not claim that licence for its own text. Nonlicensed full captures remain outside the public package. The narrow public extract uses nine quoted words from the essay and no prose quotations from the three research papers. The source ledger records dates, exact read scope and locators. Source-byte checks establish retained-file identity, not the truth of financial anchors or legal claims.

The prior-work comparison is appropriately limited. Aggregation concerns in apportionment and sharp moment bounds already exist. The new content is the exact receipt-set application, explicit witnesses and quantitative ranges for this one public model. The bounded search and partial close reading do not establish global novelty. An elementary theorem with another small grid would have little independent value; here the measured width of the source-specific ranges and the member-versus-total distinction support a short robustness note.

The introduction explains the mechanism before the notation. The tables, units and uncertainty labels are clear. The paper separates equity charge values from ready cash, conditional ranges from empirical forecasts, and accounting effects from welfare. The two text corrections above will remove the remaining avoidable ambiguity. No extra parameter grid is needed for this scope.

## Frozen content hashes

| File | SHA-256 |
|---|---|
| `paper.md` | `32e42b0419cd94c7647633c1039561816943a98f4bd179d7b472d3675433c6b4` |
| `README.md` | `c33eb622e12d9fd3b701d4ac46786c724ae4e54ad82024dc528e0f0029f46636` |
| `protocol.md` | `e8b0f4f9c8e22d5eac24c2bfc4da044b6324e49d4d70a5059a174219516a97ce` |
| `code/model.py` | `2b75565d45a3b39529d5da0c1460ea7c61ba7cb379316078bc20a07e2343b1b0` |
| `code/analyze.py` | `6ddc131d7680b43f9e9bd938215ccd5d35735a535202194223f326e75ea1b328` |
| `code/test_model.py` | `f310b0f308eb50902064dff5841f42b0c27bb8d836468a7ffc116891cd312811` |
| `data/raw/inputs.json` | `848e8ccb2a756165f085f2b6c023dc20d376b1dac6a04e21d99d52c73a1414c5` |
| `reviews/verification-record.json` | `c6e5148bde8db26743b6d66eb842060c4f35830ae2bf3b94417976f06237e7be` |
| `reviews/independent_checks.py` | `0a91d6b136227f25af28d0bdd007b954c944164c3afc9e2076538d410aa39c34` |
| `reviews/independent-results.json` | `b0e47c48c6e65431e903e1f4f4cfddcfe0e161a59599a7abeb7c50a1ba427773` |

The machine record contains the hashes of all frozen non-review files, including all output and evidence files. The separate feasibility and source-package records retain their earlier dates and scope.

## Limits of this review

This review does not audit original company filings, financial-data vendors, actual firm distributions, market valuation responses, cash conversion, law or treaty behavior. It does not check Figure 4 or render the source figures. It does not prove that no earlier paper has the same result. It does not supply human review or an external publication judgment. The model and its conditional result can be reproducible even when the empirical assumptions required for a policy forecast remain unverified.
