# Protocol: supplied-field preservation in pinned FLARE exports

**State:** protocol. **Recorded:** 2026-10-09 UTC. Fixtures were written at 23:51:50.001466Z. A separate reviewing agent observed diagnostic output already present by 23:52:03Z; the exact first-execution time was not recorded in this design log. The results file's observed modification time of 23:53:34.524371Z was a later write, not evidence of first creation. This prose protocol was first saved at 23:53:43.697527Z. File modification times are audit observations, not substitutes for execution timestamps. **Design timing:** exploratory source inspection preceded fixture selection, and diagnostic output preceded completion of this prose protocol. This is not a preregistration, a pre-outcome protocol, a random sample, or a blinded audit. Freeze the final fixture/protocol/mapping hashes before a confirmation rerun. **Review:** AI-authored protocol, with a separate AI design challenge; independent result review and human review had not occurred when the initial prose was written.

## Question and contribution

For a selected set of source-valid synthetic FLARE reports, which distinctions survive the actual pinned client export functions in named fields, elsewhere as narrative, and in retained raw content? Do any output properties present a different source concept under the expected target name?

The contribution target is a reproducible engineering case study of one implementation revision, with minimal-pair inputs and explicit recovery boundaries. Crosswalks, missingness, provenance, reconstruction, and query preservation are established ideas. Read the programme's `docs/PRIOR_ART_GATE.md`, `docs/SCHEMA_FEASIBILITY.md`, and `docs/BENCHMARK_DESIGN_GATE.md` for prior work and the reason the generic OECD/ETSI loss hypothesis was rejected. The result may be limited or negative; no broad novelty, legal compliance, practitioner utility, or incident-prevalence claim is planned.

## Implementation and outputs

Pin `ai-flaw-reporting/ai-flaw-reporting` to commit `f51514d4b999fa7988e05d44b9bf18ea0aa98031` (upstream commit date 2026-08-22T22:28:53Z). Exact retained file hashes and dependency versions belong in the execution manifest.

Use these upstream files:

- `client/src/entities/ai-flaw-report/model/schema.ts`, including `createAiFlawReportSchema` with options derived from each record's actual classification flags.
- `client/src/entities/ai-flaw-report/lib/jsonld-converter.ts` and `cert-converter.ts`, executed as pinned rather than reimplemented.
- `client/src/entities/ai-flaw-report/model/hooks/useDownloadReport.ts`, inspected for bundle context; any executed extraction or composition harness must disclose precisely which lines and behavior it exercises.
- The native form configuration files and `widgets/ai-flaw-report/reporter-details-step/ai-system-info.tsx`, used to establish what the fields ask reporters.

The formats under test are native FLARE form JSON, its JSON-LD serialization, and its CERT/VINCE-style standalone JSON. The last name follows the implementation. No independently verified acceptance by CERT/VINCE or conformance to a current recipient API is claimed. The public service and server submission paths are outside scope. No reports are sent.

## Corpus and selection

`data/fixtures.json` defines a common base record, 13 atomic supplied-field queries, 16 pair definitions, and 32 expanded records. Each pair changes exactly one native leaf; other common context is held fixed within the pair. P13 uses a common context with optional disclosure schedule strings absent, appropriate to `no` versus `undecided` intent. Each pair is independent: it is not a sequence of reports or a sample of incidents.

Fields were selected after inspecting the converters for projection and omission paths. This is a targeted counterexample/regression suite, not an unbiased exporter score. Both suspected omissions and positive preservation controls were selected. A generic issue description deliberately does not duplicate every specialized field; supplying a fact in its intended native field is sufficient input for the test. This does not claim that reporters never repeat information.

All entities, events and people in records are fictional. The reserved `.invalid` domain prevents a real contact/address from being used. The report flags represent facts *inside* the hypothetical scenario, not claims that a real incident occurred. `selectedStakeholders` is serialization input only. Attachments are empty; actual browser File contents are excluded from the core result.

| Pair | Native field changed | Source distinction | Role |
|---|---|---|---|
| P01 | system `version` | Two supplied build strings, fixed model | Version projection witness |
| P02 | system `version` | Omitted versus explicit unknown text | Missingness versus narrative uncertainty |
| P03 | system `accessMethod` | Web App versus Official API | Native option preservation |
| P04 | `expectedBehavior` | Omit unauthorized entries versus refuse request | Dedicated narrative preservation |
| P05 | `actualBehavior` | Initial allegation versus explicitly withdrawn allegation | Update preserved as text |
| P06 | `harmNarrative` | Confirmed no privacy impact versus uninvestigated privacy impact | Assessment distinction in narrative; separate financial harm held fixed |
| P07 | `severityOfHarm` | Omitted versus native `not_sure` | Uncertainty control |
| P08 | `severityOfHarm` | Native `low` versus `high` | Preservation control |
| P09 | `prevalence` | Omitted versus native `not_sure` | Uncertainty control |
| P10 | `prevalence` | Native `rare` versus `common` | Preservation control |
| P11 | `documentedHarmCwe` | Native `cwe-20` versus `cwe-200` | Weakness classification preservation |
| P12 | `detectionMethod` | Supplied method versus unknown-method statement | Dedicated narrative preservation |
| P13 | `publicDisclosureIntent` | Native `no` versus `undecided` | Negative versus undecided choice |
| P14 | `disclosureDatepicker` | Two supplied planned dates | Public-disclosure date preservation |
| P15 | `embargoDetails` | Initial versus updated coordination requirement | Update preserved as text |
| P16 | `mitigationNotes` | Coordination contact supplied versus disputed | Dispute preserved as text |

The fixture state's labels such as `disputed`, `updated`, and `uninvestigated` are research annotations. They do not add typed fields to FLARE or change source data. `not_sure`, `no`, and `undecided` are native choices. An absent optional property is not a negative finding. Native schema-validity is necessary, but the study does not claim every fixture was created through the browser UI. In particular, an omitted slider field may display as `not_sure` in the UI without the stored value being identical.

## Exact query and mapping contract

Each query in `fixtures.json` specifies an exact source JSON pointer, expected supplied value/state, candidate target JSON pointers, native UI label, evidence URL and interpretation limit. `mapping.csv` is the readable mapping ledger. Query values are exact strings/omissions, not automated judgments about the fictional event's truth.

Classify output locations as follows:

- **Named field:** a dedicated output property exists. Its value can still be prose. This label does not certify semantic correctness or a shared external ontology.
- **Narrative:** the fact occurs within a composite descriptive output string, requiring a format-specific parser or a reader. Composite CERT descriptions are included here.
- **Unmapped:** no named or composite mapping for the source field was identified in the pinned converter. Full-output comparisons can still reveal unexpected preservation.
- **Raw:** the full supplied JSON-serializable record appears in `flare:raw`.

The standalone CERT `product_version` is a flattened composite string, so it is classified as narrative/composite for these tests, even though it has a named target property. The JSON-LD `aiSystem[0].version` is a named property but must be checked against the separately supplied source version. A property name and a changed output are not proof of a faithful answer.

No JSON-LD remote context is dereferenced by the offline field tests. JSON equality and pointer access are the interface being evaluated; RDF expansion, graph equivalence and recipient inference are not evaluated.

## Execution and comparisons

1. Verify source commit and input hashes. Record runtime/dependency versions and any module-loading accommodations. Accommodations must not change the schema, converter logic or fields.
2. Validate every full record using the native dynamic schema. Retain validation results. Convert the supplied record unchanged, rather than silently replacing it with Zod output containing defaults. Record any parse/default differences separately if inspected.
3. Check pair minimality mechanically: both records must differ at exactly the declared source pointer. Check that each query has different source answers. Unexpected fixture invalidity blocks that case; document any repair before rerunning it.
4. Freeze `new Date()` and JSON-LD metadata at `2026-10-09T00:00:00.000Z`. This is synthetic test time, not retrieval or execution time. CERT generates a timestamp internally; metadata control is essential to avoid spurious pair differences. Record actual run time independently.
5. Run both actual converters. Parse their returned JSON strings. Test determinism for repeated conversion of the same input under the fixed clock.
6. Compare pair equality separately for (a) full JSON-LD, (b) named JSON-LD view excluding only `flare:raw`, (c) extracted `flare:raw`, and (d) full standalone CERT JSON. Removing raw is a declared consumer view, not an upstream transformation or a missing transport baseline.
7. Compare the declared target query paths, and record exact source and target answers. Test the system-version target against the actual source version; record model/version substitution even if the target is nonempty. For composite narratives, show the actual text. Pair discrimination is evidence of differing text, not proof of correctly typed or recipient-usable answers.
8. Require deep equality of `flare:raw` and each original JSON-safe record. Call this **raw-payload recovery**. There is no tested native inverse converter, and this is not a universal round-trip theorem.
9. Inspect and, if feasible, exercise bundle composition independently. The native download includes original report JSON with metadata, JSON-LD, CERT JSON, and a separate attachment directory. If the full React/download path or ZIP generation is not executed, state that limitation. Never infer bundle loss from a standalone CERT collision. For the empty-file corpus, original JSON is a preservation control; do not generalize to file bytes, duplicate attachment names or arbitrary File serialization.
10. Reconcile all pair counts and preserve both collisions and successful preservation. A converter crash is an execution outcome, not an information-loss claim. No percentages need be presented; any fraction uses tested pairs as its denominator.

## Sensitivity and limits

Raw recovery is the mandatory negative control against the broad loss hypothesis. Native severity/prevalence controls guard against a test that only selects omitted fields. A minimal optional-field record would test collection, not loss during conversion, and is not a scored control here. A fabricated typed/provenance adapter is deliberately deferred because it would mostly demonstrate a chosen interface, not a property of the authentic implementation.

Do not infer containment completion from `mitigationNotes`, occurrence/discovery/notification times from report creation/public disclosure, actual victim status from potential affected stakeholders, or escalation ownership from reporter identity. The original six workflow questions are narrowed according to `docs/BENCHMARK_DESIGN_GATE.md`; unsupported native questions are coverage notes, not counted failures.

Results describe a pinned client revision and selected inputs. They do not measure operational failures, legal duty satisfaction, reporter behavior, downstream processing, production deployment, server export behavior, real-world prevalence, or the quality of FLARE as a whole. Purely synthetic results cannot establish that a human recipient would miss the information or that an alternative would improve incident response. No external messages or corrective upstream pull request are authorized by this study.

## Completion gate and deviations

Before a complete-study draft: execute and retain every planned case; confirm native schema validity and minimality; reconcile generated tables; retain exact source artifacts/hashes with rights compliance; obtain independent AI critical review of code, inputs, evidence and claims; resolve blocking issues; state the evidence cutoff and actual review state. An independent reviewer must inspect the full raw/bundle context and challenge the provisional contribution.

Keep a dated deviation log below. Negative findings and source limitations are retained rather than replaced with a different success target.

| Date/time UTC | Deviation | Reason and impact |
|---|---|---|
| At protocol creation | Replaced six broad workflow queries and invented OECD/ETSI crosswalk profiles with 13 atomic native-field queries in an actual FLARE exporter audit. | Exploratory source inspection showed free-text preservation and no faithful dedicated encoding for several original queries. Narrows claims to actual implementation behavior. |
| 2026-10-09T23:54 UTC | Recorded that diagnostic output preceded the completed prose protocol. | Parallel implementation proceeded from the written fixtures and agent design messages. Treat all initial results as exploratory; a later frozen confirmation rerun does not retrospectively make the design prospective. |
| 2026-10-09T23:55 UTC | Corrected an earlier chronology statement that mistook a results-file modification time for its first write. | A reviewing agent's tool observation established that output already existed by 23:52:03Z. No result or fixture changed. The exact initial execution time remains unrecorded here. |
