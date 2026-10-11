# S007: When a Funded Benefit Still Does Not Arrive

State: **Complete-study draft**. Date: 11 October 2026. Separate internal AI review is complete. No human peer review has occurred.

[Read the paper](paper.md). This study compares review queues and automatic payment rules in a conditional post-labor economy. It separates earmarked eligible benefits from new cash needed for ineligible advances. A stable queue can still need a continuing loss budget.

The paper contains two accounting propositions, a stable-queue counterexample, 12 named scenarios, 567 distinct stress paths and recovery settings, and 12 tests. All numerical inputs are synthetic. No measured error rates or national policy outcomes are claimed.

## Reproduce the analysis

From the repository root, with Python 3.9 or later:

```sh
python3 studies/2026-10-11-benefit-access/code/model.py
python3 -m unittest discover -s studies/2026-10-11-benefit-access/code -p 'test_*.py' -v
```

The model and tests use only the Python standard library. They need no network, random seed, paid service, or downloaded source text. The CSV and summary outputs are deterministic. The run timestamp changes when the model runs.

## Files and limits

- `paper.md`: model, proofs, results, prior work, and limitations.
- `protocol.md`: initial plan and dated changes. This study was not preregistered.
- `data/design.json` and `data/dictionary.md`: synthetic assumptions, units, and output definitions.
- `code/`: analysis, meaningful checks, and separate optional acquisition tools.
- `results/`: named cases, 144 period rows, 567 stress rows, summary, and input/output hashes.
- `sources/manifest.csv`: seven source records with dates, hashes, rights, scope, and claim locations.
- `sources/snapshots/`: short evidence extracts only. Full captures remain in the ignored local source directory.
- `logs/`: searches, decisions, execution record, and completion gates.
- `reviews/`: separate critical review, author response, and independent check record.

There is no raw empirical dataset. The design JSON is the complete input. No figure or export file is needed to reproduce the stated results. No reuse licence has been selected.

## Optional source acquisition

```sh
python3 studies/2026-10-11-benefit-access/code/acquire.py
python3 studies/2026-10-11-benefit-access/code/build_evidence.py
```

Acquisition needs `curl` and public internet access. HTML extraction uses the standard library. PDF extraction additionally needs `pypdf`; the observed version was 6.10.0. The script does not install it. If it is absent, the PDF remains captured but unextracted. The evidence builder needs all extracted captures and will fail rather than invent a passage. Each new capture has a new dated directory and acquisition log. A new capture can differ from the study's source version; retain the original ledger when comparing versions.

## Measurement note

The code calls the end-of-period rule `deadline_*`. It pays open claims at the end of their arrival period. The argument `deadline=2` controls only the separate count of claims still unpaid two periods later under appeal-only payment. Equal period-end payment does not imply equal access within the period. The funding benchmark assumes enough aggregate funding for eligible benefits; it is not an operational eligibility oracle.

See [completion gates](completion-gates.md) for final release checks.
