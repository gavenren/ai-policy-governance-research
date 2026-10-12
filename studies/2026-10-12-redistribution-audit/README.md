# S012 — Measuring the AI Dividend

**State: Complete-study draft.** A consistency audit of four selected claims in a pinned AI redistribution preprint. The [paper](paper.md) starts with simple income examples. Equations and numerical details are in its appendices. The [protocol](protocol.md) discloses that algebraic concerns were identified before the numerical design was recorded.

The audit corrects equal-transfer normalization and an exact CES log identity, retains the balanced consumption-tax result under a common saving rate, and states the condition supporting the capital-share limit. These are established mathematical tools applied to one source version, not new inequality theorems or a forecast. All numerical inputs are synthetic. No human peer review is claimed.

## Reproduce offline

Use Python 3.10 or later. The retained first run used Python 3.13.7. Analysis needs only the standard library and no network calls. From this directory:

```sh
python3 code/analyze.py
python3 -m unittest discover -s code -p 'test_*.py' -v
python3 code/validate.py
```

The analysis writes CSV tables, summary statistics and a timestamped run record under `results/`. To preserve those files during an independent run:

```sh
python3 code/analyze.py --output /tmp/s012-reproduction
```

The run timestamp and software version can change; deterministic numerical outputs can be compared independently. The [data dictionary](data/DICTIONARY.md) explains the inputs, units, complete output scope and tolerances. See [results/run.json](results/run.json) for hashes and [reviews/feasibility.md](reviews/feasibility.md) for the separate initial AI review. The [critical review](reviews/critical-review.md) and [author response](reviews/author-response.md) are complete. The reviewer reproduced all numerical files and checked central results with separate arithmetic. Run `python3 reviews/independent_checks.py` to repeat that check. Its output updates only the reviewer calculation receipt, including its time.

## Sources

The [manifest](sources/manifest.csv) records six source representations. The [evidence record](sources/evidence.md) gives narrow source content, exact locators, rights and limits. Full third-party originals remain outside the public study. They are not needed to run the synthetic calculations.

To download originals for checking, install `curl` and choose a folder outside the public study, preferably ignored local storage. From this directory, in the programme checkout:

```sh
python3 code/acquire_sources.py --output ../../.local-sources/s012-reproduction --ids A1P A1T G1
```

Omit `--ids` to request all six representations. The tool verifies TLS and the retained source hashes. It refuses to overwrite changed local files. If a live page changes, it retains the unmatched capture outside the study and stops; a byte mismatch does not itself imply a substantive revision. V1 is an unpinned history page, so byte changes are especially possible. The PDF and TeX are the stable source checks.

To check the already retained originals and extractions on the research host, supply the programme repository root:

```sh
python3 code/validate.py --local-source-root ../..
```

PDF extractions used pypdf 6.10.0. HTML extraction used Python HTMLParser and omitted script/style nodes. The original TeX is a separate equation check; no OCR or rendered-equation inspection is claimed. Public evidence is an original summary and a short quotation, not a complete source snapshot.

## Files and limits

There is no empirical `data/raw/` corpus: `data/design.json` is the complete synthetic input. `results/` contains every planned table, including positive controls and boundary cases. `sources/` contains the inspectable claim ledger rather than restricted full texts. `logs/` records search, design and execution decisions. `reviews/` records separate AI assessment. No source author's incidental contact details or source comments are published. No licence has been selected for this study.
