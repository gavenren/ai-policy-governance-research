# Converter execution harness

This runner executes the original client `convertToJsonLd`, `convertToCert`,
`aiFlawReportSchema`, and `createAiFlawReportSchema` at upstream Git commit
`f51514d4b999fa7988e05d44b9bf18ea0aa98031`. It does not reproduce their logic.
Every listed upstream source file is checked byte for byte against that commit.
No upstream source file is modified.

## Reproduce

Run from this research repository's root. The recorded execution used
Node **24.14.1** and npm **11.11.0**. Node 24 is outside the upstream client's
declared Node 20–22 range. A subsequent sensitivity run using official Node
**22.23.3** passed the same eight tests and reproduced every result field except
the Node version and declared-range metadata. Production UI behavior is untested.
Node's native TypeScript stripping and synchronous `registerHooks` API are required.

```sh
mkdir -p .local-sources/prior-art .local-tools/flare-harness
git clone --no-checkout https://github.com/ai-flaw-reporting/ai-flaw-reporting.git .local-sources/prior-art/flare-code
git -C .local-sources/prior-art/flare-code checkout --detach f51514d4b999fa7988e05d44b9bf18ea0aa98031
cp studies/2026-10-09-flare-export-preservation/code/package.json .local-tools/flare-harness/package.json
cp studies/2026-10-09-flare-export-preservation/code/package-lock.json .local-tools/flare-harness/package-lock.json
npm ci --prefix .local-tools/flare-harness --ignore-scripts --no-audit --no-fund
node --test studies/2026-10-09-flare-export-preservation/tests/harness.test.mjs
node studies/2026-10-09-flare-export-preservation/code/run.mjs --out studies/2026-10-09-flare-export-preservation/results/results.json --execution-log studies/2026-10-09-flare-export-preservation/results/execution.json --summary-csv studies/2026-10-09-flare-export-preservation/results/summary.csv --source-manifest studies/2026-10-09-flare-export-preservation/results/source-manifest.json
```

For an existing source checkout, verify its location and pinned revision rather
than repeating `git clone`. `--source-root` and `--dependencies-root` override the
default paths. The CLI returns exit code 2 if a fixture fails either actual source
validator; invalid cases are recorded and are not converted.

The four direct dependency versions match the upstream root `yarn.lock`:
Zod 4.3.6, Next 16.1.6, React 19.2.4 and React DOM 19.2.4. The client-specific
`yarn.lock` is stale with respect to its Zod dependency. The supplied npm lock
pins this harness's resolved transitive dependencies; it is not a claim to
reconstruct the full upstream application environment. Installation scripts are
disabled. The original schema imports a field configuration which imports
`next/dynamic`; the actual dependency is loaded without rendering the UI.

The original `constants.ts` is imported before `schema.ts` to accommodate their
ES-module cycle. Hooks resolve the original `~/` aliases and omitted extensions.
The source files remain unchanged, with no validator or UI-module stubs.

## Interpretation boundaries

- Both validators inspect the same original fixture record. Conversion uses
  that record, not the parsed object with Zod defaults or unknown-key stripping.
  Validation metadata reports when the parsed representation differs.
- `Date` is frozen synchronously for both converters and restored afterward.
  The same fixed metadata timestamp is supplied to JSON-LD. Thus an incidental
  export time cannot create a false distinction between paired inputs.
- Pairs must have the same query and declared source path, and differ at exactly
  that one JSON leaf. All records are explicitly synthetic; no report is sent.
- Full JSON-LD and its actual `flare:raw` property are tested independently of a
  named-field projection which excludes only `flare:raw`. The projection is an
  analytical view, not a separate upstream export or destructive conversion.
- `exact_source_representation_equal` is literal equality, not semantic answer
  correctness. For example, the supported `no` to `No` label conversion yields
  false. Narrative output is not interpreted automatically or scored as a typed
  answer. Pair discrimination and answer fidelity are different properties.
- Raw round-trip means extraction of `flare:raw` from JSON-serialized output and
  exact equality with the JSON-safe input. It is not an upstream inverse converter.
  All fixtures have empty attachments; binary file preservation is untested.
- The ZIP download hook is inspected and hashed, but not executed. Its source
  writes original non-file fields to `report.json` and adds files separately.
  Standalone CERT collisions therefore do not establish loss from the complete
  download ZIP or from all supported sharing routes.
- No downstream CERT/VINCE schema validation, remote submission, JSON-LD
  expansion/context dereferencing, UI build, or browser interaction is performed.
- The unchanged upstream CERT template contains a claim that the report was
  forwarded to VINCE. For these offline synthetic outputs, that sentence is
  template content and does not indicate any actual transmission.

The source hashes, dependency lock hash, fixture byte hash, harness byte hash,
runtime metadata, full converter outputs, validator outcomes and pair comparisons
are retained in `results/results.json`. Results are deterministic under the stated
inputs and runtime; validation is not a certification of operational fitness.
The separate optional execution log records actual host start/end time, outside
the synthetic clock override, and the result-file hash. These audit timestamps
are intentionally excluded from the deterministic result file.

Upstream code is available under its own MIT license. This harness fetches that
repository with its `LICENSE` intact. No reuse license is granted for this research
repository by the upstream license or by this dependency setup.

## Supported-runtime sensitivity

The runtime archive used was
`https://nodejs.org/dist/v22.23.3/node-v22.23.3-darwin-arm64.tar.gz` with SHA-256
`23b25245dcfb9af7262f8ff142e9e2e0af025368117329e7a7458a51e5922f53`.
The digest was checked against the exact filename entry in the official
`https://nodejs.org/dist/v22.23.3/SHASUMS256.txt`; manifest SHA-256 was
`4fe99a2ba9d552a6f51c13ed68fb11104cfa5df601aec616be689253a8139e7a`.
This is checksum verification over HTTPS, not release-signature verification.
The archive was extracted in ignored `.local-tools/node22-runtime`; no system
installation or settings change was made. URLs, retrieval timestamp, hashes,
test counts and actual execution times are in
[`results/runtime-sensitivity.json`](../results/runtime-sensitivity.json).

With the verified archive extracted, reproduce the separate run from the
repository root without overwriting the primary reviewed results:

```sh
mkdir -p .local-verification/node22-sensitivity
.local-tools/node22-runtime/node-v22.23.3-darwin-arm64/bin/node --test --test-reporter=tap studies/2026-10-09-flare-export-preservation/tests/harness.test.mjs > .local-verification/node22-sensitivity/tests.tap
.local-tools/node22-runtime/node-v22.23.3-darwin-arm64/bin/node studies/2026-10-09-flare-export-preservation/code/run.mjs --out .local-verification/node22-sensitivity/results.json --execution-log .local-verification/node22-sensitivity/execution.json
```

[`compare-runtime.py`](compare-runtime.py) compares the entire primary and
candidate result objects, allowing only `/metadata/runtime/node` and
`/metadata/runtime/in_declared_range` to differ. It checks the candidate execution
ledger hash and all eight TAP test results, and writes the public sensitivity
report. Pass `--baseline`, `--candidate`, `--test-log`, `--execution-log`,
`--acquisition` (runtime provenance JSON) and `--out` explicitly. The provenance
JSON's required `version` field must match the executed runtime; the remaining
acquisition fields are retained verbatim for audit.
