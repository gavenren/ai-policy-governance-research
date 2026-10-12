# Reproduction and numerical checks

This package separates a private run of the acquired source from an independent public calculation. The public calculation uses only aggregate numbers and Python's standard library. It does not contain or require the original cluster records or third-party implementation. The results are four conditional accounting cases, not four estimates of observed welfare or a forecast.

## Public calculation

From the repository root, use Python 3.10 or later:

```sh
python3 studies/2026-10-12-ai-output-reconciliation/code/verify.py
```

This command reconstructs the accounting twice, compares exact output bytes, checks the printed table cells, and runs 21 numerical tests. It writes a new local verification record to `logs/numerical-verification.json`. It does not download data or run the original model. The saved record at the author cutoff used Python 3.12.14 and ended at 18:20:32 UTC on 12 October 2026. A later verification replaces that local record with its own time and hashes; it cannot prove that the original sources remain current.

The aggregate inputs are in `data/raw/`. The file guide there defines their units and provenance. `code/analyze.py` constructs signed output and imported-input components from those inputs. It then computes Laspeyres and Paasche factors, their geometric mean, chained indexes, and real levels. No original source function is imported. All four cases are checked against aggregate exports from the private source-function run. The 96 GDP component and index comparisons have zero difference in this environment. Six additional QA-growth values are checked in the test suite.

Results appear in `results/cases.csv`, `training-reconciliation.csv`, `component-prices.csv`, `factorial-effects.csv`, `power-ledger.csv` and `source-comparison.csv`. Prices and growth factors use full precision. Monetary inputs and levels use dollars, not billions. Tables in the paper may divide these values by one billion. Blank transition fields in 2023 mean that no preceding-year growth rate is defined.

`code/check_printed.py` compares 54 distinct displayed cells against the main paper and both appendix versions. A row can have several source locators because the versions print the same number. The check finds 52 passes and two failures. In 2024, the source returns a Fisher index of 2699.4875656890504 and real growth of 2599.4875656890504 percent. Direct integer rounding gives 2699 and 2599 percent. The main paper and both appendices print 2700 and 2600 percent. The source's own generated Markdown first rounds to one decimal. Further rounding of that intermediate value would explain the printed integers, but this is a conjecture. The failed comparisons remain in the output. A successful numerical test run does not mean that all presentation comparisons passed.

## Private source reproduction

The source archive is C1 in `sources/manifest.csv`. Acquire the ZIP from the public publisher link given there and retain it at `.local-sources/next-design-screen/original-replication.zip`. Its required SHA-256 is `85bf1b23a99f606abf3ab87b39ed9d3bc69a6d53a27d50ee31ff20d1f974ff8c`. Do not place it in the public study. No redistribution licence was found for its implementation and input data.

Use Python 3.12 for the full private run. A local virtual environment with the versions in `code/requirements-private.txt` can run the adapter. The original author run used an ignored environment at `.local-tools/s016-venv`, with inherited bundled packages. Installing these free dependencies does not require a paid service. Complete package versions appear in each execution record.

```sh
python3 -m venv .local-tools/s016-venv
.local-tools/s016-venv/bin/python -m pip install -r studies/2026-10-12-ai-output-reconciliation/code/requirements-private.txt
.local-tools/s016-venv/bin/python studies/2026-10-12-ai-output-reconciliation/code/reproduce_private.py --run-id new-control-01 --export
.local-tools/s016-venv/bin/python studies/2026-10-12-ai-output-reconciliation/code/reproduce_private.py --run-id new-control-02
.local-tools/s016-venv/bin/python studies/2026-10-12-ai-output-reconciliation/code/check_private_controls.py --run-id new-control-01
```

Use a new run identifier each time. The adapter refuses to overwrite an extraction, and it checks the frozen source and current dated protocol hash before source execution. The `--export` option replaces the public aggregate input files with the acquired source's outputs; omit it if only a private comparison is wanted. Re-run the public checks after an export. The default repeat check in `verify.py` compares the author's retained `run-01` and `run-02` if present. A new reader can directly compare the SHA-256 hashes of the two new private `aggregate-export.json` files. The source records alone do not supply its unlicensed microdata; the original source archive is needed for this full check.

The adapter checks archive paths before extraction. It runs the unchanged `main.py` with `runpy`, disables Python bytecode writes, selects the noninteractive Agg plotting backend, and blocks socket connections with an audit hook. It does not replace any source input, function or setting for the full positive control. The original program writes its standard tables and plots. It also calculates its original whole-US baseline and Google-exclusion robustness result. Those outputs remain private; this study does not calculate alternative whole-US results. The adapter then calls the source's existing allocation functions for the annual-preserving power series.

For the operations convention, the adapter makes one explicit change in memory: in the source's `calculate_ai_gdp` function, it replaces the name for the constant training price ratio with a transition-specific lookup. The lookup contains `algorithm_ratio × spending_growth / physical_operations_growth`. The original function's other expressions remain unchanged. This is an AST adapter, not a claim that every case runs an unchanged GDP function. No source file is modified. Source and input hashes before and after each run agree.

The annual-preserving case multiplies each original month's power by listed annual power divided by the generated annual sum. It keeps the original relative monthly pattern. The adapter checks all allocation rows to verify the same dates, entities and composition weights; allocated power, spending, operations and labor scale by the same annual factor. Listed annual electricity costs remain in all four cases. `power-ledger.csv` also reports what the generated energy would cost. That separate cost entry is a ledger, not a fifth accounting case.

## Recorded sequence and limits

The first unchanged source execution began at 18:15:59.939059 UTC on 12 October 2026. It completed at 18:16:21.404935 UTC. The initial protocol and its analytical addendum preceded this execution. A later terminology note changed no inputs or cases. The hash guard rejected the first repeat attempt before extraction or source execution because that note changed the protocol bytes. The failure is saved in `logs/execution-repeat-preflight-failure.json`. The adapter was then pinned to the new snapshot. Original adapter and protocol bytes are retained with the first private run.

Both complete source runs passed, without network attempts. They produced identical aggregate bytes: SHA-256 `ae2291a261c767c846d67b48e4bd00884e8899a6c80d60e5b5136a4a311da458`. Source warnings are retained in both execution records. In 2025, the released monthly rule generates 182.13554006968662 TWh, compared with the listed 138 TWh. The difference is 44.13554006968663 TWh, or 31.982275412816396 percent of the listed total. The source still charges the listed quantity. Preserving that listed total requires a 2025 multiplier of 0.7576774963700111.

The geometric-power positive control uses the same first two annual inputs and places the third on their geometric path. The source then preserves all three totals within floating-point precision and emits no warning. Other tests check price times volume, unit invariance, the signed GDP boundary, positive index factors, unchanged nominal output under price-only changes, and the distinction between level and annual growth. A synthetic two-GPU control shows that fixed GPU-specific rental rates can still give a changing average spending per operation as the mix changes. The code rejects nonpositive or nonfinite index terms instead of reporting a coerced real index.

These checks validate the stated calculations with the retained source. They do not independently validate the source's power assumptions, cluster coverage, hardware data, rental prices, service markup, labor boundary or output-quality measures. The operations bridge is an alternative convention. It is not a unique correction, and operations do not fully describe memory or bandwidth services. No sampling confidence interval is attached to these deterministic cases.
