# S018 numerical reproduction

The analysis uses Python 3.12.14 and the standard library only. It reads the exact retained vendor scripts and makes no network requests. Source code, seed 42, 2,000 paths per cohort, distributions and horizons are unchanged. The source licences and provenance remain with the vendor and source packages.

From the repository root, reproduce into a fresh ignored folder:

```sh
python studies/2026-10-12-dividend-policy-comparability/code/analyze.py \
  --output .local-verification/s018-reproduction/results \
  --logs .local-verification/s018-reproduction/logs
python -m unittest discover \
  -s studies/2026-10-12-dividend-policy-comparability/code \
  -p test_analysis.py -v
cmp studies/2026-10-12-dividend-policy-comparability/results/summary.csv \
  .local-verification/s018-reproduction/results/summary.csv
cmp studies/2026-10-12-dividend-policy-comparability/results/paired-paths.csv.gz \
  .local-verification/s018-reproduction/results/paired-paths.csv.gz
```

`code/check_source_stdout.py` checks the retained baseline console summaries against the retained public results. Run it from the repository root. It does not execute a source simulation. All 200 checks pass. It does not audit the source's separate LVT scenario or all auxiliary sensitivity text.

The first analysis began at `2026-10-12T19:02:33.529969+00:00`, after the input and printed-target freeze in `logs/numerical-pre-execution.json`. The frozen protocol SHA-256 is `cb4c64b0be1e6da7c453fb329c30161b9ae6b4645dac971ea0db09980eab0fda`. Before execution, automation-tax and VAT medians were added to complete the protocol's printed-value checks. No scenario was added. The final analysis code hash is in `logs/execution.json`.

The ten-year script first runs unchanged as a script. A fresh module load resets its seed to 42, and its published reducer then returns the same source cohort and full-precision statistics. The twenty-year script runs unchanged and retains its `all_results`. The audit replays fixed and triggered floor payments on each cohort's own revenue and non-floor paths. It does not pair draws between cohorts or introduce an economic response to changed payments.

All 60,000 paired path-year rows, 120,000 policy outcomes, 60 aggregate rows and 30 paired year summaries are retained. All 80 comparisons with the ten-year source reducer agree within 1e-8 billion or fraction units, as applicable. All 200 checked printed console fields agree at source display precision. Twenty-seven of 28 whitepaper targets match their assigned source policies; section 6.2's year-10 55.7% claim does not match the ten-year triggered result. The separate twenty-year fixed-policy target does match. These checks establish attribution and reproduction, not real fiscal viability.

The first test run had one failure. Its intended exact 0.98 boundary evaluated slightly above 0.98 in binary floating-point arithmetic. The unchanged strict rule therefore returned the higher payment. Only the test fixture was corrected to use an exactly represented 9800/10000 boundary; its quotient is also checked explicitly. All 11 tests then passed. The initial failed output, repair explanation and patch, final test log, and code hashes remain in `logs/`. The analysis and saved numerical results were not rerun or altered for this repair. The public traceback omits only the absolute local checkout prefix; its original hash and ignored raw-log location are documented.

`data/DICTIONARY.md` defines all inputs and outputs. `logs/numerical-manifest.json` pins the completed numerical package. The source distributions, fiscal bases, retirement arrangements, health assumptions, debt dynamics and legal implementation are outside this audit. Simulation fractions are conditional on those inputs. They are not calibrated probabilities of financing a real programme.
