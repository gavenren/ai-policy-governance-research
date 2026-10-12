# Execution record

The initial central run completed at 2026-10-12T13:56:51Z with Python 3.13.7. Its exact design, code and output hashes are retained in `results/run.json`. The command was `python3 code/analyze.py` from this study directory. It exited successfully and produced all nine planned CSV tables plus `summary.json` and the run record. The immediately following command, `python3 -m unittest discover -s code -p 'test_*.py' -v`, passed all 15 tests. No separate exact timestamp for that first test command was retained.

The root source/output validation used `python3 code/validate.py --local-source-root ../..`. It passed 10 output hashes, nine tables, 2,620 planned rows, six source records and 12 original/extraction hashes. The public validator also checks formula residuals, budget balance, positive controls, missing rows, nonfinite results and the full expected grid count. A successful program exit alone is not the interpretation test.

The separate reviewer ran the same checks, generated outputs in a different directory, and compared all ten numerical file hashes. All matched. The independent output run used Python 3.12.14; the original retained run used 3.13.7. The reviewer also used independent exact fraction and 60-digit decimal arithmetic. Its public files give the actual checked scope, time, discrepancies and limitations. See `reviews/reproduction.json`, `reviews/independent_checks.py` and `reviews/independent-results.json`.

The public acquisition script was tested against the pinned source PDF, source archive and cited growth article. All three downloaded originals matched their recorded hashes. `logs/acquisition-reproduction.json` records the later retrievals. A separately captured arXiv version history still listed only v1; its receipt is `logs/version-recheck.json`.

Text fixes from the review did not change central code, inputs or outputs. No unnecessary numerical rerun was used to imply extra independent evidence. There are no omitted planned result tables, unexplained failed model runs or empirical uncertainty estimates.
