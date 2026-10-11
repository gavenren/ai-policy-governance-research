# A Consumption Floor After Human Labor

State: Complete-study draft; independent AI review complete. Date: 11 October 2026.

[Read the paper](paper.md). The paper derives a joint consumption-floor test and a condition for supply investment. All numerical results are synthetic. No human or external peer review has been completed.

## Reproduce

From the repository root, with Python 3.9 or later:

```sh
python3 studies/2026-10-11-post-labor-floor/code/model.py
python3 -m unittest discover -s studies/2026-10-11-post-labor-floor/code -p 'test_*.py' -v
```

No external packages or network connection are required. CSV outputs are deterministic. The run timestamp in `results/run.json` changes on each run.

## Files

- `paper.md`: manuscript, proofs, findings, limits, and references.
- `protocol.md`: exploratory design and changes.
- `data/design.json`: all inputs; see `data/dictionary.md` for units.
- `code/`: model and six tests.
- `results/`: nine named scenarios, 576 stress cases, 16 policy summaries, and 36 investment cases.
- `sources/`: source ledger and short evidence extracts. Full source bytes are retained locally and are not distributed here.
- `logs/`: search and check records.
- `reviews/`: separate AI review and response.

No separate raw empirical dataset exists. The JSON parameter file is the complete synthetic input. No reuse licence has been selected.
