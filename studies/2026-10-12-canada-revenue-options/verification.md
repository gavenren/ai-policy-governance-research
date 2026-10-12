# Verification record

Date: 12 October 2026. These are checks before publication, not proof of a GitHub update.

## Release scope

This release adds the revenue-options paper, source ledger, inputs, a compact consumption extract, calculation code, result tables, three separate AI reviews, and this record. It adds links in the repository README and the earlier Canada study README. It leaves the earlier Canada paper, brief, model, results, and source studies unchanged. Working research notes and unrelated candidate studies are excluded.

## Checks completed

- The model ran with Python 3 and the standard library. Repeating the run produced byte-identical result files.
- The result set contains 12 package cases, 21 stress cases, four single-source cases, three funding thresholds, three public-fund asset cases, and ten borrowing-year rows.
- The six-row consumption extract parses as CSV. Its four 2025 quarterly values sum to C$1,761.235bn, the value used only as a scale comparison.
- Input and source hashes match. The inherited C$1,100.12195433bn target reconciles to the prior paper's revenue, expense, and permitted deficit.
- The [arithmetic review](reviews/arithmetic-review.md) used exact rational arithmetic, without calling the model functions. All 756 numerical comparisons passed within its stated tolerance. The review also checked case coverage and manuscript tables.
- The [tax review](reviews/tax-review.md) identified a retained-credit definition issue. The final model deducts a selected C$20bn retained GST credit and rebate allowance separately from collection losses and new rebates. It includes a C$40bn sensitivity. The reviewer confirmed the repair and checked all 33 package and stress cases.
- The [policy review](reviews/policy-review.md) checked the wealth, property, resource, public-fund, and borrowing comparisons. It independently checked the main stock-flow and borrowing arithmetic. No required correction remained within that scope.
- All local links in the release resolve. The publication scope contains only the new study and two navigation edits.

Reviewers also helped collect evidence or discuss accounting. These are separate checks within an AI-assisted project, not independent external or human peer review.

## Checked file hashes

SHA-256:

| File | Hash |
| --- | --- |
| paper.md | `0e45ffab93a3104d15424e7270ce40fbf3397c7c9ad8caf21f89fca04deded06` |
| data/inputs.json | `8ebdad9873a4e9ef5c1645642677897902355dff5732328739f22004ce245ddb` |
| code/analyze.py | `b70637ff4300dd1ce081f1331a3d4c4ee46c9ff3273877b2e805393b9c5ab8ad` |
| results/summary.json | `1225f9099a7855a2dff5b52005a8d07bbfa02bed17e0839c7ce4f25372eaaf14` |

The input file also records the unchanged source-paper and source-result hashes at repository commit `f606abcaba65fc9d222fa2b0dc0318bbd20c17e6`.

## What these checks do not establish

The checks confirm arithmetic and bounded source use. They do not establish feasible tax rates, adequate rebates, a measured future tax base, growth, legal authority, provincial fiscal coverage, public consent, or a sufficient living standard. The C$20bn retained-relief allowance is a selected assumption, not a cost estimate of statutory entitlements. No wealth, resource, or public-fund yield is added to the tax-package totals.
