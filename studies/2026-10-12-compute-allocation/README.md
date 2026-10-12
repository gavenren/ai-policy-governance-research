# S014 — Allocating a Universal Compute Floor

**State:** Complete-study draft. Separate AI critical review, independent calculations and release checks are complete. No human or journal peer review.

This short comment audits a pinned compute-allocation proposal. It preserves its correct budget identities and worked example, qualifies a zero-residual boundary, distinguishes composition from consistency, and applies an existing capped alternative. It does not introduce a new fairness algorithm or assess a deployed service.

- [Manuscript](paper.md)
- [Separate critical review](reviews/critical-review.md), [author response](reviews/author-response.md) and [completion gates](logs/completion.md)
- [Protocol and prior exploratory choices](protocol.md)
- [Source ledger](sources/manifest.json) and [inspectable evidence](sources/extracts/evidence.md)
- [Bounded search](logs/search.md) and [independent feasibility review](reviews/feasibility.md)
- [Named examples](results/named-cases.json), [486-case grid](results/grid.csv), and [schema](data/README.md)

## Reproduce offline

From the repository root, use Python 3.13.7 or another Python version with the standard library features used here. No package installation, network, paid service or source PDF is needed for these calculations.

```sh
python3 studies/2026-10-12-compute-allocation/code/analyze.py
python3 -m unittest discover -s studies/2026-10-12-compute-allocation/code -p 'test_*.py' -v
```

The analysis writes exact fractions and a run record with actual UTC time, software version and hashes. Expected summary: 486 rows; raw claims respected in 323; exceeded in 163, of which 82 have capacity no greater than total claims. All capped bounds and budget checks pass. These counts describe the fixed test set, not observed prevalence. All 15 tests must pass.

## Source verification

Full source files remain in ignored local storage because full redistribution permission was not established. The public metadata, narrow extracts and mathematical transcriptions state the inspectable evidence. A source hash alone is not a reproduction of its content. After obtaining the original files by the retrieval instructions, this optional check verifies their bytes and three short quotations:

```sh
python3 studies/2026-10-12-compute-allocation/code/check_sources.py --repository .
```

This command requires retained originals. Its success confirms hashes and exact quoted phrases; it does not establish all interpretations or prove that the sources remain current. No legal instrument is being audited. No human or journal peer review is claimed.
