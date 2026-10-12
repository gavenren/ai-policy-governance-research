# What Remains After the Payment?

**S011. State: Complete-study draft.** The calculation, manuscript and evidence package have passed separate AI review. Release checks are complete. No human peer review is claimed.

The [paper](paper.md) compares an income floor with the same floor after debt service. It uses the public 2025 Survey of Consumer Finances. It removes wage income in a fixed accounting experiment and tests uniform transfers, payment changes, rent, asset buffers, and two targeted guarantees. It does not estimate future poverty, actual default, optimal benefits, or a future AI equilibrium.

In the central experiment, all families pass the gross-resource test by construction, while an estimated 22.9% fail after the SCF debt-service estimate. The standard error is 0.6 percentage points. That payment estimate combines reported and constructed amounts; it is not a complete record of contractual minimums. The [data dictionary](data/DICTIONARY.md) states the units, denominators, and measurement limits.

## Read and inspect

- [Internally dated protocol](protocol.md), saved before study outcomes; [design hash](logs/design-freeze.json).
- [Source manifest](sources/manifest.json) and [prior-work comparison](sources/PRIOR_WORK.md).
- [Decision log](logs/decisions.md), including the initial failed weight check and its correction.
- [Methods review](reviews/methods-review.md), [final source review](reviews/critical-review.md), [author response](reviews/author-response.md), and [reviewed hashes](reviews/methods-reviewed-hashes.json).
- [All results](results/all-estimates.csv), [run metadata](results/run.json), and [official benchmarks](results/official-benchmarks.csv).

The evidence cutoff is **2026-10-11T21:42:56Z**: the last source retrieval used in this version. Interpretation and review continued after retrieval. The package retains 14 source records, including six prior studies. Two prior papers were accessible only by abstract. Full third-party papers are not redistributed. Selected public SCF data are attributed to the Board of Governors under its stated public-domain policy. No licence for the study's original work is selected.

## Reproduce offline from saved replicate estimates

Use Python 3.12 with `numpy==2.3.5` and `pandas==2.2.3`, the environment used for the release. From this study directory:

```sh
python3 -m unittest discover -s code -p 'test_*.py' -v
python3 code/analysis.py --saved-replicates results/replicate-estimates.csv --output /tmp/scf-saved-check
python3 code/validate_sources.py
```

The saved route recomputes household point estimates from the selected microdata. It reconstructs uncertainty from the saved 999 replicate estimates; it does not independently apply the original replicate weights. Differences at the final floating-point digits are expected. The separate reviewer compared outputs within numerical tolerance. Do not describe this route as a full recomputation of sampling estimates.

## Recompute from original public files

Acquisition is separate from analysis and uses verified HTTPS through `curl`. Choose a new capture directory; the script refuses to overwrite one. From this study directory:

```sh
python3 code/acquire_sources.py --destination /tmp/scf-original-check
python3 code/analysis.py --source-csv /tmp/scf-original-check/SCFP2025.csv --weights /tmp/scf-original-check/p25_rw1.dta --output /tmp/scf-full-check
python3 code/benchmarks.py --workbook /tmp/scf-original-check/D8.xlsx
```

The download script checks the original archive/workbook hashes before extraction. If the official file changes or access fails, it stops and preserves the new capture. Do not substitute a changed file without a new version record. The `--source-csv` option rebuilds the selected public-data copy in `data/`; without it, analysis uses the retained copy. The benchmark command checks two official workbook cells against the retained descriptive table and writes `results/official-benchmarks.csv`.

Full original-weight recomputation was performed and separately repeated. The independent reviewer matched all generated CSV files exactly. This result applies to the retained input and environment versions. Network availability and future byte-for-byte source stability are not guaranteed.

For an existing local source archive with the filenames in the manifest, `python3 code/validate_sources.py --local PATH` verifies retained original and extracted bytes as well. Short public evidence extracts permit inspection without that archive. PDF text was extracted with pypdf 6.10.0; HTML text was extracted with Python's standard HTML parser. No OCR was used for this study.
