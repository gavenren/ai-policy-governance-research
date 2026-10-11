# S008 — Buying a Public Stake Without Buying a Guarantee

**State: Complete-study draft.** Separate internal AI review and local release checks are complete. No human review has occurred.

The [paper](paper.md) gives an exact financing test for a social dividend after public equity acquisition. It distinguishes fair market value, physical expected returns, a minimum payment, and outside tax support. It also shows when a fairly priced acquisition improves an existing fiscal hedge.

Run from the repository root with Python 3.9 or later:

```sh
python3 studies/2026-10-11-public-capital-acquisition/code/model.py
python3 -m unittest discover -s studies/2026-10-11-public-capital-acquisition/code -p 'test_*.py' -v
```

The standard library is sufficient. No network or seed is needed for analysis. Six synthetic scenarios produce 31 policy rows and all corresponding state rows. Nine tests pass. Numerical CSV files are deterministic; run timestamps change.

See [protocol](protocol.md), [data dictionary](data/README.md), [source ledger](sources/manifest.json), [search log](logs/searches.md), and [completion gates](completion-gates.md). Full third-party sources remain outside the public study. No observed dataset or legal-instrument comparison is used.
