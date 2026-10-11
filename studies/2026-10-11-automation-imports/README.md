# Funding a Post-Labor Floor When AI Is Imported

State: **Complete-study draft**. Study S006. Date: 11 October 2026. Separate internal AI review is complete. No human or journal peer review has occurred.

[Read the paper](paper.md). The study derives a joint limit for extra transfer funding and no loss in total domestic consumption. The model includes foreign supply, price pass-through, lost domestic revenue, and real collection costs. The results are conditional and synthetic.

## Reproduce

From the repository root, with Python 3.9 or later:

```sh
python3 studies/2026-10-11-automation-imports/code/model.py
python3 -m unittest discover -s studies/2026-10-11-automation-imports/code -p 'test_*.py' -v
```

No network or external package is needed. CSV and summary outputs are deterministic. The actual timestamp in `results/run.json` changes on each run.

Source retrieval is separate:

```sh
python3 studies/2026-10-11-automation-imports/code/acquire.py .local-sources/automation-imports/new-capture
```

Use a new output directory. The script refuses to replace existing captures. The PDF can be extracted with `pypdf`; source analysis used version and method recorded in `sources/manifest.json`. One publisher page rejected direct retrieval. The failed attempt is logged; it is not a retained source for the paper.

## Files

- `paper.md`: model, proofs, comparisons, negative cases, and limits.
- `protocol.md`: exploratory design and changes.
- `data/`: complete synthetic inputs and definitions.
- `code/`: offline analysis, eight tests, and optional source retrieval.
- `results/`: nine named cases, 1,296 grid rows, 216 continuous optima, common-policy limits, and run hashes.
- `sources/`: five provenance entries and short evidence extracts; originals remain in ignored local storage.
- `logs/`: search, acquisition, execution, and gate records.
- `reviews/`: separate critique, response, and independent check record.

No separate raw empirical dataset exists. There are no empty snapshot folders. No reuse licence is selected. Source rights do not establish rights for this study's original work.

See [completion gates](completion-gates.md) for the release checks.
