# Verification record

Date: 12 October 2026. These are checks before publication. They do not by themselves prove a GitHub update.

## Scope

The release contains the Canada paper, source ledger, compact data, calculation code, results, three AI review records, this check record, and a repository README link. Working notes and unrelated candidate studies are excluded. The combined policy paper and the 15 underlying economic studies are unchanged.

The paper applies an existing policy synthesis to Canada. It does not claim a new causal finding, an official costing, a proved tax yield, or an adequate payment level. No human or external peer review has occurred.

## Checks completed

- The model ran successfully with Python 3 and the standard library. A second run produced byte-identical result files.
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
| code/analyze.py | `dde838cb2325fd890a8c2838c43250781848b452d2d8cd37c7e3897d78779d6b` |
| results/funding.csv | `ff1945b43d1be127e0b0af3576df54529938624418fafeddedf8027b775be069` |
| results/transition.csv | `fe4b3121771d1d3dd99d59ea7a23435ec9459b44e81e762b597359c776beae2a` |
| results/full_loss.csv | `779f863364552385d6dd293fd08aaf6bb232d0f01de9362b0bee79b1fb77718f` |

Original combined paper SHA-256: `536518d8ceafaf05c18a76ab4c206f204bedf28399afdd2bf9f2e50bb3e59498`.

## Remaining work before policy adoption

Official tax costing, household tax-benefit modelling, provincial and territorial accounts, pension actuarial work, Indigenous participation, project costs, legal review, and monthly cash tests remain necessary. Selected stress assumptions do not set confidence bounds. The permanent universal promise remains unfunded in this study; the model states the revenue it would require.
