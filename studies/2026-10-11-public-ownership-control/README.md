# S010 — Who Governs the People's Capital?

**State: Complete-study draft.** Separate AI review is complete, with no blocking issue within the stated scope. Release checks are complete. No human review or peer review is claimed.

The [paper](paper.md) studies who controls income, portfolio votes, and requests to change a decision in three public fund systems. Its contribution is a narrow audit of whether a promised remedy reaches the body that can provide it. It does not claim to invent social ownership or prove which system is best.

The cases have different purposes: Alaska supports a resident dividend and public services; Norway supports the state budget; New Zealand helps fund future pension costs. The study does not treat them as equivalent citizen entitlements. Its policy argument applies to the stated scenario in which paid work no longer provides enough income.

## Read the evidence

- [Protocol](protocol.md): question, scope, exploratory status, and changes.
- [Codebook](codebook.md): decision rules, ambiguous cases, and inference limits.
- [Coded relations](data/coding.csv): 18 provision-linked relations, with source fact and author interpretation in separate fields.
- [Decision routes](data/decision_routes.csv): three decision questions for each case.
- [Source manifest](sources/manifest.json), [instrument ledger](sources/instruments.csv), and [short extracts](sources/extracts.csv).
- [Search log](logs/searches.md) and [access log](logs/access-and-decisions.md).
- [Generated case matrix](results/case-matrix.md), [route table](results/decision-routes.md), [sensitivity](results/sensitivity.json), and [run record](results/run.json).

The evidence cutoff is **2026-10-11T21:35:44Z**: collection and the final discovery check ended by this time. Later edits do not extend the evidence period. Fourteen sources have original downloaded bytes. Six institutional sources use separately hashed primary-page reader text. Two more entries are discovery-only records, which do not support institutional claims. Full third-party documents and incidental contact details are outside the public files.

## Reproduce the public audit

From this study directory, run:

```sh
python3 code/validate.py
```

The command uses only the Python standard library. It checks the evidence graph, the 18 coded relations, the nine decision routes, quote limits, relative document links, and agreement between inputs and generated tables. It requires no network connection. To regenerate the descriptive tables and run record:

```sh
python3 code/validate.py --write
```

If the ignored local source directory is available, also verify the retained source bytes, extraction hashes, and text anchors:

```sh
python3 code/validate.py --with-local
```

The scanned Alaska investment-policy quote is a visual transcription. The byte checks cover its source and rendered images, but do not certify the transcription. No test certifies legal correctness or search completeness.

`code/acquire.py` records the original network acquisition recipe. It uses Python `urllib`, `html.parser`, and `pypdf==6.10.0`. It is separate from the offline audit. It refuses to overwrite an existing source capture; new retrievals must use a new ID and a reviewed manifest entry. Some endpoints return blocked or empty responses, so running the recipe cannot guarantee the original source contents. Reader-produced captures were collected through the research browser tool and are identified as such. No full source archive is republished or promised.

## Scope limits

The Norwegian mandate's English text is government-hosted but expressly not official or authorised. Norwegian legal authenticity has not been independently checked. Current New Zealand statutory downloads failed; its findings therefore use official fund descriptions and one information decision. Discovery metadata does not resolve pending amendments. Unknown legal routes are left unknown.

The sensitivity check assumes that every unknown further remedy might exist. It preserves the positive division of authority without asserting that a remedy is unavailable. It is a logical boundary check, not a statistical estimate.

The [independent review](reviews/critical-review.md) and [author response](reviews/author-response.md) record all three resolved issues. The programme maintainer completed the release checks recorded in `completion-gates.json`. Empty snapshot and survey directories are omitted because no full third-party snapshots or survey data are published. No release licence, author affiliation, funding award, or journal submission is implied.
