# S011 benefit-unit extension

State: **Complete-study draft extension**. Analysis, source checks, separate AI review and release checks are complete. This is an addition to S011, not a separate paper. The original code, selected data and results are unchanged.

The extension compares three payment rules with equal aggregate gross payments: equal per family, equal per adult, and proportional to square-root family size. All face the same size-adjusted threshold. The main result is that the choice of outcome matters: adult-based payments increase the family failure share but reduce the person-weighted failure share and the mean dollar shortfall. The original coverage gap is useful as a diagnostic; it is not a general policy objective.

The [prospective protocol](protocol.md) was saved before outcomes. The main manuscript contains the extension in Section 8 and Appendix B. [The dictionary](data/DICTIONARY.md) defines the public roster fields and outputs. [Source records](sources/manifest.json) include the full public SCF file, reused SCF codebook, and two closely read methods sources. Full third-party originals stay in ignored storage. Only narrow attributed extracts are published. This package does not include a new theory of equivalence scales, measure of need, tax-benefit model or AI forecast.

## Reproduction

Run commands from the repository root. The environment used Python 3.12.14, NumPy 2.3.5 and pandas 2.2.3. Install the original S011 requirements for analysis. PDF text extraction also used pypdf 6.10.0; it is not needed for the saved-data analysis.

Validate all saved public estimates, the protocol, joins, public evidence and preservation of original files:

```sh
python3 studies/2026-10-11-household-debt/extensions/benefit-unit/code/check.py
python3 -m unittest discover -s studies/2026-10-11-household-debt/extensions/benefit-unit/code -p 'test_*.py' -v
```

The public check recalculates estimates and standard errors from the saved five implicate and 999 replicate estimates. It does not independently apply the original replicate weights.

For a complete new analysis, obtain the pinned original S011 weight file through its existing acquisition tool in a new ignored folder:

```sh
python3 studies/2026-10-11-household-debt/code/acquire_sources.py --destination .local-verification/s011-unit-weights --ids D2
python3 studies/2026-10-11-household-debt/extensions/benefit-unit/code/analyze.py --weights .local-verification/s011-unit-weights/p25_rw1.dta --output .local-verification/s011-unit-results
```

This uses the published selected roster and the unchanged original financial data, refits payment rates in every implicate and replicate, and saves results outside the published output folder. If the destination exists, select a new name for acquisition. Do not overwrite retained downloads.

To obtain and verify the full public roster source:

```sh
python3 studies/2026-10-11-household-debt/extensions/benefit-unit/code/acquire.py --destination .local-verification/s011-unit-full --ids E1
python3 studies/2026-10-11-household-debt/extensions/benefit-unit/code/check_feasibility.py --full .local-verification/s011-unit-full/p25i6.dta --selected studies/2026-10-11-household-debt/data/scf2025-selected.csv --output .local-verification/s011-unit-full/feasibility.json
```

The analysis tool accepts `--full` only to create a missing `data/roster.csv`; it refuses to overwrite an existing roster. The optional `--local-evidence` flag on `check.py` also checks original and text hashes and narrow quotations, when the retained ignored source files are available at the paths in the ledger. A reader without those local files can download pinned originals and inspect the listed passages.

## Scope and files

The primary sample has 4,358 families per implicate. Two top-coded families are excluded before outcomes. A capped-roster sensitivity includes all 4,360. Aged 18 or above means adult; no zero-adult family is present. PEU resources are assumed pooled. The size floor is an explicit rule, not observed need. No tax, benefit offset, behavioral response, local price or creditor balance-sheet effect is estimated.

All 192 statistics, paired contrasts, group counts, original-case checks and run hashes are retained. The maximum relative budget discrepancy was below 3.4e-16. Ten tests passed. The source check confirmed 52 original files unchanged, apart from permitted manuscript/README integration. The original paper remains available in Git history; the original-file hashes were recorded before integration.

`section-draft.md` retains the inserted section as a drafting aid; the full manuscript is the controlling paper. `logs/design-freeze.json` records the prospective time and hash. `logs/original-file-hashes.json` preserves the starting state. `logs/searches.json` records the bounded methods screen. The [separate review](reviews/critical-review.md), [author response](reviews/author-response.md), and [completion record](logs/completion.md) report their scope. No human peer review is claimed.

