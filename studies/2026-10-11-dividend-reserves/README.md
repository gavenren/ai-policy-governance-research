# S005 — Cash Before Capital

**State: Complete-study draft.** The model, source checks, and separate internal AI review are complete. No human review has occurred.

The [paper](paper.md) gives a finite-horizon cash test for a fixed social dividend. It includes joint tax and public-asset income shocks, delayed sale proceeds, and lost income from sold assets. The model is synthetic and exploratory.

The cash-only reserve is 21 units in the base joint-shock set. A sale paid in period 2 lowers the needed reserve to 7.1795 units, but disposes of 17.9487 units of the initial 100-unit asset. A period-4 receipt cannot reduce the reserve. Early loss of income rights can make a late sale increase the reserve need.

## Reproduce

Run from the repository root with Python 3.9 or later:

```sh
python3 studies/2026-10-11-dividend-reserves/code/model.py
python3 -m unittest discover -s studies/2026-10-11-dividend-reserves/code -p 'test_*.py' -v
```

The analysis uses only the standard library. It needs no network or seed. The executed environment used Python 3.13.7. The run enumerates all 8,649 joint paths, 3,237 no-overlap paths, and 93 common paths. These sets overlap. It writes 45 policy-environment summaries and 11,979 base-case path rows. Ten tests pass. The numerical output files are deterministic; the timestamp in `results/run.json` changes on rerun.

## Contents

- [Protocol and deviations](protocol.md)
- [Input and output dictionary](data/README.md)
- [Source ledger](sources/manifest.json) and [source notes](sources/README.md)
- [Search log](logs/searches.md), [execution log](logs/execution.txt), and [test log](logs/tests.txt)
- [Completion gates](completion-gates.md)

The `data/` directory contains synthetic inputs. No observed raw dataset exists. Full third-party source bytes are outside the public study because redistribution rights were not established for the full set. Source collection is separate from offline model reproduction. The `reviews/` directory contains the separate review, author response, and independent check record.

The model does not assess income adequacy, country policy, permanent solvency, or a welfare-optimal sale. The public asset and cash reserve are initial endowments with no acquisition finance. All assumptions and tested failures are in the paper.
