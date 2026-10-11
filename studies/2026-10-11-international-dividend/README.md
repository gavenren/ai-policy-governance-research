# S009: Who Can Rely on an International AI Dividend?

**State: Complete-study draft.** The analysis and separate AI review are complete, with all three issues resolved. This is not a human-reviewed paper. The parent release record identifies the final manuscript and the reviewed earlier version.

Read [the paper](paper.md). The main question is whether a recurring international payment can support a household floor after wages cease to be reliable. The model distinguishes total provider wealth from the cooperation gains actually lost after default. A financed deposit can help, but it can also make continued participation unattractive.

The contribution is a bounded application of relational contract theory. See [prior-work comparison](sources/PRIOR_WORK.md), [protocol](protocol.md), [source ledger](sources/manifest.json), and [short evidence extracts](sources/evidence-extracts.md). The method is theoretical and all numerical inputs are synthetic. No country forecast, legal-status finding, or calibrated policy rate is supplied.

## Reproduce offline

Run from the repository root with Python 3.10 or later. The main analysis and tests use only the standard library.

```sh
python3 studies/2026-10-11-international-dividend/code/model.py
python3 -m unittest discover -s studies/2026-10-11-international-dividend/code -p 'test_*.py' -v
```

The first command writes nine named cases, 648 grid cases, 101 persistence cases, state-level detail, and run metadata. The second command runs 12 tests. See [data dictionary](data/DICTIONARY.md) for every input and output field. Generated CSVs can use CRLF line endings through Python's CSV writer.

## Source acquisition

The original source bytes and extracted full text are private local research captures under the repository's ignored `.local-sources/international-dividend/` directory. Their redistribution rights were not established. They are not needed to run the model. The public ledger records exact retrieval times, byte counts, hashes, source locations, methods, and failed routes. Short attributed extracts make the limited cited claims inspectable.

For a new capture, install or use an existing `pypdf` runtime and run:

```sh
python3 studies/2026-10-11-international-dividend/code/acquire_sources.py
```

The original extraction used pypdf 6.10.0 and Python 3.12. The recipe creates a new timestamped private folder. It does not replace the evidence ledger or original bytes. Sources can change, become inaccessible, or return a different format. A hash mismatch is a new version to inspect, not proof that the earlier claim is false.

## Files and limits

- `paper.md`: main text, proofs, references, and disclosure.
- `data/design.json`: all synthetic inputs.
- `code/`: offline analysis, tests, and separate source recapture.
- `results/`: generated row-level outputs, summary, and actual run metadata.
- `sources/`: provenance, short extracts, and closest-prior-work comparison.
- `logs/`: search record, design changes, and execution log.
- `reviews/`: separate review, author response, reviewed hashes, and independent exact-arithmetic checks.

There is no raw empirical data directory because no empirical data were collected. There is no instrument ledger because every treaty and deposit rule is a model proposal. This draft does not state that any present government must or can legally implement it. The decisive assumptions include credible termination, perfect observation, an enforceable loan and trustee in the deposit extension, and household delivery by the recipient government.
