# Verification record

Date: 12 October 2026. These are checks before publication. They do not by themselves prove a GitHub update.

## Scope

The release contains the Canada paper, source ledger, compact data, calculation code, results, three AI review records, this check record, and a repository README link. Working notes and unrelated candidate studies are excluded. The combined policy paper and the 15 underlying economic studies are unchanged.

The paper applies an existing policy synthesis to Canada. It does not claim a new causal finding, an official costing, a proved tax yield, or an adequate payment level. No human or external peer review has occurred.

## Checks completed

- The model ran successfully with Python 3 and the standard library. A second run produced byte-identical result files. CSV output uses LF line endings so that published file checksums also match. This format adjustment leaves every numeric cell unchanged.
- The result files contain three funding cases, 25 transition-year rows, and 27 severe-case rows.
- The population extract has 14 selected rows. Its 2026 adults, children, and child age groups match the input file. Adult and child partitions reconcile to the total population.
- The summary's input checksum matches the input file. All four built-in reconciliation checks pass.
- A separate AI reviewer rebuilt all 25 transition rows and all 27 severe-case rows with decimal arithmetic, without importing model functions. Values agreed within $0.00000001 billion.
- A second reviewer rebuilt all 27 severe-case rows and checked population, CCB, payment definitions, and scope.
- The delivery review checked Canadian roles, service assumptions, legal status, urgent relief, and the order of work. Its required clarification was applied: the limited top-up is tax-free and does not reduce other benefits in this cost case, subject to laws and agreements.
- Fiscal wording was revised to describe the budget balance before the reserve addition. The paper now states that pre-April 2027 planning uses existing departmental budgets. Neither change alters the numerical results.
- All local links in the release resolve. No new source studies are imported into the release. The original combined-paper hash still matches its prior version.

The [fiscal review](reviews/fiscal-review.md), [cost review](reviews/cost-review.md), and [policy review](reviews/policy-review.md) state their own scope. Reviewers also helped collect inputs; these are separate checks within an AI-assisted project, not independent external certification.

## File checksums

SHA-256 checksums identify the checked contents. The source tables can later be revised by their publishers.

| File | SHA-256 |
| --- | --- |
| paper.md | `af4a481c547aec1bfa8d897bc437202407ba3971d8106e8340cc32f2af2e2af9` |
| data/inputs.json | `c2f1e82d94d91dcefe0826cfbbee26bb9202c2e229bf462fa99b900592bb555b` |
| data/population-extract.csv | `8d68fb759bef980add1b44d58b98dafeca7e2de05b0cbac17acccb0bae2d6442` |
| data/pt-income-tax-2024.csv | `684f537760139b597e8fb8519f484c4a0d9d8830ccfcc1dd379ea052d262af7d` |
| code/analyze.py | `fc4f3f98de581dba810375f16bd12c623982de5dcf0c098e94bf6f7b05cae32a` |
| results/funding.csv | `12c168307053efc0f9ca47fb2c6402175de2536b1abe86fa71218e5c47676f1d` |
| results/transition.csv | `17bddc4723055be0147d1afa6cf3e59aab8075229d6fe022814f2459d3f649bf` |
| results/full_loss.csv | `054271675b174400c55ada65a316f112dc50fe8af27b9e6cc2a3f0b91dcdfe7a` |

Original combined paper SHA-256: `536518d8ceafaf05c18a76ab4c206f204bedf28399afdd2bf9f2e50bb3e59498`.

## Remaining work before policy adoption

Official tax costing, household tax-benefit modelling, provincial and territorial accounts, pension actuarial work, Indigenous participation, project costs, legal review, and monthly cash tests remain necessary. Selected stress assumptions do not set confidence bounds. The permanent universal promise remains unfunded in this study; the model states the revenue it would require.
