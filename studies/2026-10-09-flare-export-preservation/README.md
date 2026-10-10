# FLARE-AI export preservation study

**State: Complete-study draft, 2026-10-10 UTC.** Separate AI critical review and
same-host reproduction completed; no human or external peer review.
Evidence cutoff: **2026-10-09T23:59:59Z**, meaning sources acquired by that time.

This study executes pinned FLARE-AI client export functions on **32 explicitly
synthetic, schema-valid records arranged in 16 selected minimal pairs**. It
compares the actual full JSON-LD export, its embedded raw record, a named-field
analytical projection and the standalone CERT-shaped JSON export. It does not
estimate incident frequency or certify publication quality or legal compliance.

| Observed comparison | Distinguishable pairs / selected pairs |
| --- | ---: |
| Actual full JSON-LD export | 16 / 16 |
| Embedded `flare:raw` record | 16 / 16 |
| JSON-LD projection excluding only `flare:raw` | 6 / 16 |
| Standalone CERT-shaped JSON export | 8 / 16 |

Every input passes both original upstream Zod validators, and all 32 JSON-safe
records are recovered exactly from `flare:raw`. Thus these selected results
support a limited distinction between transport preservation and named-field
coverage. They do **not** establish that the full JSON-LD export or full download
package inherently loses these records. A CERT output difference is not
necessarily a typed answer: several fields are concatenated narrative text.

## Research and evidence

- [Complete-study draft](paper.md) and [six-page PDF](output/pdf/paper.pdf), with actual review state and limitations.
- [Exploratory protocol](protocol.md); not a preregistered study.
- [Frozen design record](data/design-freeze.json), recorded after the initial
  diagnostic run and before the confirmation rerun.
- [Synthetic paired records and queries](data/fixtures.json) and
  [source-to-output mapping](mapping.csv).
- [Machine-readable complete results](results/results.json),
  [compact pair table](results/summary.csv),
  [source commit and byte hashes](results/source-manifest.json), and
  [actual confirmation run timing](results/execution.json).
- [Supported-runtime sensitivity comparison](results/runtime-sensitivity.json):
  official Node 22.23.3, all eight tests passed, identical complete results except
  for two runtime metadata fields.
- [Executed harness tests](tests/harness.test.mjs).
- [Separate AI critical review](reviews/critical-review.md),
  [author responses](reviews/author-response.md), and
  [completion gates](completion-gates.md).

## Reproduction

Follow the exact clone, commit pin, dependency installation, test and execution
commands in [the harness instructions](code/README.md). They use the original
upstream source without edits, exact direct dependencies from the upstream root
lockfile, and the committed [npm dependency lock](code/package-lock.json).
No paid service, account change, API credential or report submission is required.
The upstream source and dependency installation remain in ignored local folders.

The primary recorded runtime is Node **24.14.1**, outside the upstream application's
declared Node 20–22 range. A sensitivity run under official Node **22.23.3**, within
that range, passed all eight tests and produced the same complete results except
for the Node version and declared-range metadata. Its archive checksum matched
the official HTTPS release manifest. Results describe these local harness runs.
The UI, complete application environment, actual ZIP packaging, binary attachment
fidelity, downstream CERT acceptance and JSON-LD context expansion were not tested.
The ZIP control is source inspection only: the original hook also includes a
non-file original record and separately packages attachments.

All scenarios, descriptions and reporter contact values are synthetic and were
never submitted. The unchanged upstream CERT template says the report was
"forwarded to VINCE"; in these offline outputs that is template text, **not evidence
of transmission**. The study and code were produced with AI assistance; no human
participant validation or journal acceptance is claimed. Upstream third-party
licensing does not grant a reuse license for this research repository.
