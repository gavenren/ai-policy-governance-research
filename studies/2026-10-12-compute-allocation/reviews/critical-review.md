# S014 separate critical review

Final content checks completed: **2026-10-12T17:42:39.930603+00:00**. Reviewer: a separate Codex agent. This is AI review, not human or journal peer review. The reviewer did the earlier feasibility check and shared that note with the author. The review was not blind. The reviewer did not write the central manuscript or implementation.

**Decision:** The corrected paper is suitable as a short, version-specific technical comment. No blocking error remains in the checked scope. It does not establish a new allocation theorem or demonstrate that a public compute scheme would improve welfare.

## Files and execution

The first review used the 18 files in `logs/review-request.json`, frozen at 2026-10-12T17:36:57.149459Z. All 18 hashes matched before the author made the two text corrections below. [reviewed-hashes.json](reviewed-hashes.json) records both sets of hashes. The final manuscript SHA-256 is `e148f45b10dec13e4a22659a5e2f2347019820b6640525e02c25395b426ed61b`. The analysis SHA-256 remains `cc04f06d7e902ecda1bca618e57887895312269ad3988474fc8c25da7cca0cce`.

The reviewer read the full manuscript, protocol, input dictionary and cases, analysis and tests, source manifest and evidence, search and discovery logs, and saved results. Commands run from the repository root were:

```text
python3 -m unittest discover -s studies/2026-10-12-compute-allocation/code -p test_analysis.py -v
python3 studies/2026-10-12-compute-allocation/code/check_sources.py --repository .
python3 studies/2026-10-12-compute-allocation/reviews/independent_checks.py
```

For these commands and the separate reproduction, `python3` denotes the bundled **Python 3.12.14** interpreter actually used by the reviewer. The author's original run used Python 3.13.7.

All **15 tests passed**. The retained-source check passed for **14 files in nine records**, including three quotations and the retained latest-version record. A separate read-only check found no missing target among 18 local Markdown links in the package at that stage.

The reviewer copied the study to a temporary directory and ran `code/analyze.py` there. The grid, named cases and summary matched the original files byte for byte. Original results and run metadata were not rewritten. [reproduction.json](reproduction.json) retains the new run time and output. The first review wrapper used the wrong key for the frozen hash map and stopped before execution; the corrected wrapper then passed. This was a review-wrapper error, not an analysis error.

## Separate mathematical checks

[independent_checks.py](independent_checks.py) does not import the author's code. It uses exact fractions and enumerates possible sets of filled claims to solve the capped allocation. This differs from the author's iterative removal method. [independent-checks.json](independent-checks.json) records the results and checked hashes.

- Every cell of the 486-row grid matches the separate calculation. The counts are 323 raw allocations within all claims and 163 with an excess award. The latter contain 81 surplus cases and 82 cases with capacity no greater than total claims. Repeated normalized weight ratios are retained by design. These are finite checks, not frequency estimates.
- All six named allocation cases and four floor cases match. The source's five-class awards are `(700000, 3600000/7, 1200000/7, 2700000/7, 200000/7)`. The shock multiplies each by `2/3`. These are valid positive controls.
- The demand-bound threshold follows directly from cancelling each positive demand: every award is within its claim exactly when `C <= sum(w*D)/max(w)`. The `(1,9)` case gives raw awards `(5/2,5/2)` and capped awards `(1,4)`.
- With claims `(2,2)` and weights `(2/3,1/3)`, composition down gives `(4/5,1/5)` instead of `(2/3,1/3)`. Composition up gives `(50/39,28/39)` instead of `(52/39,26/39)`. All intermediate caps are inactive. Unchanged-claim additivity and the selected subset-consistency case also pass.
- The zero-residual example leaves one unit unassigned under the source's explicit convention. The paper correctly limits this objection: aggregate scarcity and feasible floors rule out that boundary in the stated restricted domain. It does not invalidate the source's shortage example.

I also checked the argument for the capped algorithm. The sum `sum(min(d_i, lambda*w_i*d_i))` is continuous and strictly increases while some positive claim remains unfilled. It reaches the sum of claims. Thus a target below total claims has a unique award vector; once all claims are filled, several multipliers can give that same vector. Zero claims cause no difficulty. Each pass of the author's algorithm either ends or removes at least one positive claim. Its total-award bound is correctly stated as `max(U_i,D_i)` when a floor can exceed own demand. Demand caps and exhaustion cannot both hold when residual capacity exceeds all residual claims.

## Source interpretation and prior work

The earlier feasibility review read C1's full 16-page text and visually checked its formal floor statement and example on pages 7–8. This review reread its cover and pages 2 and 4–10. The base rule and claims are on pages 5–7. The floor convention and Proposition 5 are on page 7; the worked example and shock are on page 8.

The favorable interpretation in the paper is necessary and supported. C1 page 2 includes exchange as a possible use of entitlements; page 4 permits pooling and delegation; page 8 applies them in the example. Pages 9–10 discuss reclamation, strategic demand and auctions within tiers. An award above own demand therefore does not by itself prove wasted capacity. The reviewed comment preserves this distinction.

For C2, I checked the cover, claims domain on PDF page 8, capped formula on page 9, composition and consistency definitions on pages 9–10, and both composition counterexamples on PDF page 14, printed page 10. These directly establish the prior result. For C3, I checked version information, the domain on PDF page 6, footnote 16 on page 7, and the weighted formula on page 9. The full characterization proofs and the publisher's C3 version were not audited.

The author and date records agree with the retained covers and metadata. The July/August discrepancy on the target author's web listings is disclosed. The comment pins the actual v2 file and does not claim exhaustive knowledge of later or other versions. Full third-party texts remain in ignored local storage. The public evidence contains narrow excerpts and mathematical transcriptions. No reuse licence or legal conclusion is invented.

## Corrections and limits

1. The evidence file originally counted the second C1 quotation as ten words and its total as fourteen. The correct counts are nine and thirteen. The C2 quotation has eight words, not nine. The author fixed these counts; I checked the final file, SHA-256 `ba9be3156c3da703c14a104688d31cc038bbf2937d36b895feb47c3fa53556f0`.
2. Section 6 originally omitted the positive-residual-budget condition from its statement about fulfillment-rate ratios. At zero budget both rates can be zero, so their ratio is undefined. The final paragraph now states the positive-budget and positive-unsaturated-claim conditions, identifies residual rates, and covers the zero case. I checked that text. No code or result changed.

The paper is readable for a technical comment: it introduces each decision before its equation and uses small examples to explain the distinction. Its short form is appropriate to its limited contribution. No broad novelty claim should be added at release. This review does not validate compute-unit comparability, environmental conversion factors, political weights, real operating costs, or welfare effects. The finite grid does not prove all properties for all inputs. The general statements depend on the algebra and the cited definitions, which were checked within the scope above.
