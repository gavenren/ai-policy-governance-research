# S013 — Buying Backup AI for Essential Public Services

Primary state: **Complete-study draft**. Separate AI review and independent enumeration are complete. This is a small selected case audit, not a validated procurement plan.

Read [the paper](paper.md). Its four documented deployments give six pairs. Three pairs pass the defined model/platform exclusions for an incumbent buyer. Two remain for a new buyer under a documented Legacy restriction. One remains under the specified support-horizon condition. Capacity, task performance, switching and other readiness conditions remain unknown.

The study uses a conditional economy without a reliable wage fallback. It does not forecast that economy or claim that the selected AI products are suitable for public benefits.

## Reproduce the offline analysis

From this study directory, with Python 3.13.7 (the executed version; standard library only):

```sh
python3 code/analyze.py
python3 -m unittest discover -s code -p 'test_*.py' -v
python3 code/check.py
```

The first command rewrites generated tables and records the actual run time. Numeric and categorical results are deterministic. The run timestamp can change on a rerun.

If the ignored original captures are present, also run:

```sh
python3 code/check.py --with-local
```

This verifies all original and extracted byte hashes, short quotations, and retained search-response hashes. A public checkout alone cannot make that private-byte check. Public sources, retrieval recipes and narrow extracts remain inspectable in the ledger; short extracts are not full snapshots.

## Source acquisition and curation

Acquisition used Python urllib.request and pypdf 6.10.0. Each call takes a new source ID and a public URL:

```sh
python3 code/acquire.py NEW_SOURCE_ID PUBLIC_URL
```

The command refuses to overwrite an existing capture. Originals are placed in the repository's ignored `.local-sources/supplier-continuity/` directory. HTML extraction uses Python's HTMLParser, omits script/style, and normalizes whitespace. It is not browser rendering. Use the URLs and actual timestamps in `sources/captures.jsonl`; a fresh network request may return a different version. `code/build_ledger.py` records the explicit source-level curation and builds the manifest and short extracts from the retained corpus.

## Package and limits

- `protocol.md` fixes the exploratory sample and initial tests. `logs/design-clarification.md` and `logs/coding-correction.md` record later decisions.
- `data/deployments.csv` and `data/codebook.md` hold the coded corpus and unknown conditions.
- `sources/manifest.json`, `sources/extracts.csv`, and `sources/policy-status.csv` record provenance, short evidence and source status.
- `results/` holds all 36 pair/scenario rows, underlying exclusions and run metadata.
- `logs/searches.json` records the bounded search and exclusions. `logs/superseded-first-run.json` preserves the incorrect exploratory run.
- `reviews/` contains the separate AI critique, independent 36-row enumeration, author response and final disposition. Both requested revisions were resolved. No human review is claimed.

No full third-party source is republished. No reuse licence for original work has been selected. No credentials, customer records, paid API calls, contract awards, or load tests are part of the study. The authoring agent did not publish the study. The parent maintainer handles release verification separately.


The independent reviewer used Python 3.12.14. To repeat the offline independent check, run `python3 reviews/review_check.py`. Its optional network comparison needs the ignored original captures; see the review code and saved execution records. Without those originals, the offline command still checks all 36 rows and reports zero private-source hash checks. The [completion record](completion-gates.json) and [release check](reviews/parent-release.md) state the final scope.
