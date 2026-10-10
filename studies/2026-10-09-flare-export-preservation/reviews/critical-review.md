# Independent AI critical review

**Initial report recorded:** 2026-10-09T23:58 UTC. **Review scope:** frozen design, full fixture set, pinned native source and field meanings, execution harness and tests, saved outputs, reproduction documentation, and working manuscript. This is a separate AI review, not human review or external peer review. The reviewer performed prior-art research and supplied review challenges; the reviewer did not author the central fixtures, harness, analysis, or manuscript.

**Initial disposition:** the finite findings reproduce and the manuscript's principal conclusions match them. No unresolved numerical or source-validity blocker was found. Before complete-study status, clarify the unchanged upstream transmission boilerplate, reconcile the supported-runtime sensitivity if completed, and update the actual review/run state. This disposition concerns a bounded engineering research note; it does not certify publication quality or novelty.

## Reproduction evidence

The reviewer ran the eight focused harness tests: **8 passed, 0 failed**, exit code 0. The reviewer then executed the unchanged harness independently into an ignored, separate output directory at **2026-10-09T23:56:37.469Z–23:56:38.064Z**. This used the same host and installed dependencies as the author run; it was not a fresh machine or dependency rebuild.

`results.json`, `summary.csv`, and `source-manifest.json` from the reviewer run were byte-identical to the author outputs. The exact execution record and hashes of every reviewed file are in [review-evidence.json](review-evidence.json).

| Artifact | SHA-256 |
|---|---|
| Author and reviewer `results.json` | `02dbf4679217e6956d361718f72df6f57011c7b99699e31e7e1c4207f215e999` |
| `code/run.mjs` | `e1e46d3c8c0cf4a134b3feecc339e086e5c5294552fa5bc0696afbe40b287c30` |
| Initial reviewed `paper.md` | `9b362960e62d5ac8d8349861da60c1fb34597c208fc80fdf0f17e38ed542fcd1` |

A separate Python calculation read the fixture and saved output JSON without importing the harness's comparison functions. It verified all 16 pairs differ at exactly their declared leaf, checked all 32 embedded raw records against their original inputs, and recalculated every pair's full JSON-LD, raw, named-projection, and standalone CERT distinction. The recalculated counts were **16, 16, 6, and 8**, respectively, matching the committed result table. This cross-check does not independently reimplement the converters or substitute for source validation.

The harness independently checked unchanged imported source bytes against Git objects at `f51514d4b999fa7988e05d44b9bf18ea0aa98031`. Every input passed both the base and classification-dependent native validators. The parsed representations matched supplied inputs for this corpus, so schema defaults did not silently supply the observed distinctions.

## Findings and required dispositions

| ID | Issue | Assessment / required disposition |
|---|---|---|
| R1 | Generated attribution can be mistaken for an observed transmission. | The authentic CERT converter inserts a statement that the report was forwarded to VINCE via an API. The experiment did not transmit reports. Keep authentic output bytes, but explicitly describe this line as upstream template boilerplate in the manuscript/reproduction documentation. This is a disclosure correction, not a result change. |
| R2 | Primary runtime is outside the declared upstream range. | The main run uses Node 24.14.1 while the client declares Node 20–22. The manuscript already states this limitation. A supported Node 22 sensitivity is being prepared; if included, pin its provenance, independently inspect its equality claims, and state exactly which output/metadata differences remain. Without it, retain the explicit runtime limitation. |
| R3 | Review status and provisional prose must reflect completed work. | The reviewed manuscript still says independent review and confirmation are pending. Update only after this review's required dispositions are addressed; identify separate AI review and same-host rerun accurately. The reviewer will hash the revised manuscript in an addendum. |

## Scientific and interpretive challenges

**Narrow contribution.** The generic idea of testing preservation is established. Source-guided cases selected where code omits fields do not estimate a population loss rate. The present manuscript accepts those limits and describes an inspectable engineering artifact. It should remain a technical case study, not claim a validated governance intervention or a superior reporting standard.

**Strongest counterexample.** P01 changes only the separately supplied build version while platform/model remain fixed. Both source records validate. The actual complete standalone CERT-style JSON collides; so does the JSON-LD analytical view excluding only raw. The named JSON-LD version contains the model. Under this artifact boundary, equality is sufficient to show that no decoder using only that same artifact can recover both distinct source versions. No recipient semantics or practical harm is required for this finite assertion. It does not establish that the target's property name violates any independently validated external ontology.

**Mandatory negative finding.** All 32 JSON-safe records reconstruct exactly from `flare:raw`, and full JSON-LD distinguishes all 16 pairs. The source download hook also includes original non-file JSON and separately packages files. It was inspected, not executed. The manuscript correctly rejects a broad FLARE download data-loss conclusion and makes no binary attachment claim.

**Valid inputs and native meanings.** Required classification booleans are populated, condition-dependent validators are executed, each pair changes one declared leaf, and actual field labels constrain interpretation. The financial-harm background remains fixed in P06 while a separate privacy assessment changes. Text about dispute, uncertainty, and revisions is not represented as a typed native state. Optional omissions are schema-valid but not proved reachable through the interactive UI.

**Query and narrative boundaries.** Literal representation equality is not semantic answer correctness; the `no`→`No` label change is explicitly not a semantic-loss finding. Complete CERT text counts as part of the artifact, including disclosure narrative that preserves `no` versus `undecided` even where a Boolean alone would not. No natural-language decoder or real response decision is tested. A difference between outputs only establishes discrimination, not correct recovery of arbitrary facts.

**Authenticity and determinism.** The harness executes original converter functions rather than recreating them. It freezes conversion time, retains all authentic fields, compares complete standalone CERT output, and preserves raw controls. Native TypeScript stripping/module resolution and dependency selection are disclosed. The strongest local result does not depend on deleting fields from the standalone CERT artifact; deleting raw from JSON-LD is clearly a researcher-defined interface boundary.

**Timing and reporting.** Diagnostic output preceded the completed prose protocol. The chronology correction properly distinguishes observed modification from first execution. The recorded confirmation run follows the revised design freeze. No claim of preregistration is acceptable.

**Rights and privacy.** The reviewed corpus contains synthetic narratives and reserved contact domains, with no participant data or real incident disclosures. Full third-party text remains in ignored local snapshots. Upstream code is fetched with its own licence; the project has not acquired a reuse licence by association. The review found no reason for external messages, submissions, or upstream modifications.

## Remaining limits

This is finite, same-host, same-dependency AI verification of one pinned client implementation. It does not independently reproduce the whole app, test the UI or server path, execute ZIP downloads, validate a recipient API, expand JSON-LD, test real recipients, assess legal compliance, or obtain human/practitioner feedback. Those limits are compatible with the bounded result and must remain visible after the working paper is promoted to a complete-study draft.

## Follow-up verification, 2026-10-10 UTC

**R1 resolved:** the manuscript and reproduction documentation now explicitly identify the unchanged generated forwarding statement as template boilerplate rather than an actual transmission. Authentic outputs remain unchanged.

**R2 resolved within the stated scope:** the reviewer independently executed all eight tests and the unchanged harness using portable Node **22.23.3**, within the upstream declared range. The second reviewer run lasted **2026-10-09T23:59:31.327Z–23:59:31.992Z**, and its output hash was `b7e204da653ac806f1487229a8be080cd8aa3f5029d2d0f6cb9980ed878640f8`, byte-identical to the author's Node 22 output. A separate Python comparison found the complete result identical to the Node 24 result after replacing only the runtime version and `in_declared_range` metadata. No validation, converter output, query observation, pair result, source hash, fixture hash, or dependency hash differed.

The reviewer recalculated the archive SHA-256 and matched it to the saved official HTTPS checksum manifest. This did not include release-signature verification or a second independent download. The supported runtime sensitivity still uses the same host and dependencies and does not constitute a full application reproduction. Exact execution data and the sensitivity artifact hashes are retained in `review-evidence.json`.

At this follow-up, R3 and the revised-manuscript hash remained pending. The closing addendum below records their final disposition.


## Closing addendum

**Recorded:** 2026-10-10T00:03:35.162196+00:00. **Disposition:** the research critical review is closed, with R1–R3 resolved and no remaining blocker within this review's scope. Eligibility to publish this version as a complete-study draft remains conditional on the coordinating author's separate PDF and repository-publication gates. This review does not certify publication quality or acceptance prospects.

The reviewer read the entire revised frozen manuscript and author-response record. The final paper accurately describes completed execution, both independent same-host reruns, supported-runtime sensitivity, the unmodified transmission template, exploratory design timing, finite case selection, retained raw data, static-only ZIP inspection, and absent human/practitioner or external peer review. Numerical claims and their interpretation remain unchanged. The author responses accurately correspond to the completed checks. **R3 is resolved.**

The reviewer checked that the protocol, fixtures, mapping, harness, dependency files, tests, primary result, execution ledger, summary and source manifest retain their initially reviewed hashes. No additional numerical rerun was needed for the prose-only revision. The final artifacts reviewed are pinned as follows:

| Artifact | SHA-256 |
|---|---|
| Latest reviewed `paper.md` | `372f205d7f4a343f701496199f4a8783837dc6dcf953f3283063c983bec08a13` |
| `reviews/author-response.md` | `496f197c1c6d09f173baa48cda169139cab3e3c9f63c6704d64c8e03afb1541c` |

The full closing file-hash list and unchanged-input checks are in `review-evidence.json`, under `final_review_closure`. The initial manuscript hash and earlier review history remain preserved rather than overwritten. The reviewer did not inspect a rendered PDF or conduct the final staged-file/publication gate; those are separate outstanding checks outside this disposition.


## Metadata precision addendum

**Recorded:** 2026-10-10T00:05:36.905922+00:00. The evidence scope now states the exact cutoff `2026-10-09T23:59:59Z`, explicitly limits that cutoff to the retrieved public sources and runtime provenance, disclaims an exhaustive census, and records that review continued on 2026-10-10 UTC. The reviewer checked retrieval timestamps against this cutoff. This is a non-result disclosure revision.

Replacing only this paragraph with its previously reviewed wording reproduces the prior manuscript hash `464f096cae1df9e06daf6071ad00962673acac5eeee188cfae2abcccf4619c79` exactly. The latest reviewed manuscript hash is `372f205d7f4a343f701496199f4a8783837dc6dcf953f3283063c983bec08a13`. The author-response hash remains unchanged. The README status update is also hashed in `review-evidence.json`. All previously checked empirical file hashes remain unchanged; no experiment was repeated. The closed R1–R3 disposition remains in force, and separate PDF and repository-publication gates remain outside this review.
