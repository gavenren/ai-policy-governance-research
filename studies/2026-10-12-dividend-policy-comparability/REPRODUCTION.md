# S018 reproduction

The [execution guide](code/README.md) gives the exact commands, Python version, seed, inputs and output paths. Use separate destinations for a check so the original execution records remain intact. The analysis uses only the Python standard library and the two unchanged licensed source scripts.

Read the [data dictionary](data/DICTIONARY.md) before interpreting the files. The 60,000 paired path-year rows are retained in a compressed CSV; two policies yield 120,000 policy outcomes. The aggregate files include every planned cohort-year-policy result. Source console output, all printed-target comparisons, the initial test failure and the fixture-only repair are retained.

The [numerical manifest](logs/numerical-manifest.json) pins the executed package. The [source guide](sources/README.md) gives separate public and local evidence checks. A successful run confirms the specified arithmetic and file checks; it does not validate the economic assumptions or forecast actual government receipts.

The numerical manifest records the files at execution completion. A later source check required a wording correction to the data dictionary: its old general nominal-dollar label exceeded the verified source convention. The historical manifest is preserved. The [release hash record](reviews/release-changes.json) identifies the old and revised dictionary hashes. No numerical input, result or computational instruction changed.
