# Separate AI design review

**Recorded:** 2026-10-09T23:58 UTC. **Status:** completed design review of an exploratory study; not a prospective protocol approval. This review was performed by a separate Codex AI agent that researched prior art and inspected source semantics, but did not author the fixtures, central harness, or manuscript. No human, practitioner, or external peer review occurred.

**Decision:** the narrow design can support an implementation-specific engineering research note. It cannot support the originally proposed general claim about information loss in AI incident-reporting standards, or an independently validated response-decision benchmark. The completed execution and manuscript still require the separate critical review.

The reviewed design is pinned in [review-evidence.json](review-evidence.json), with SHA-256 hashes of the exact files, including the design gate, protocol, fixture set, mapping, and freeze record. The principal design hashes are:

| File | SHA-256 |
|---|---|
| `protocol.md` | `bcdc808915b9ff528a96c22896228e2dec455f348a74a5ac291529662b7e1b74` |
| `data/fixtures.json` | `6e355a22a4513e167ebe7168c81084647c767bdf1e9048436a9a47ff2d65b79d` |
| `mapping.csv` | `cd4682f7a5c372080fa2a0faebb46e889880b27fd5beefbcc753902e6a0e7549` |

## Design challenges and disposition

1. **A researcher-created lossy adapter would make the result largely tautological.** The final design executes authentic pinned converters and validates native records. It removes `flare:raw` only in an explicitly named analytical view, while retaining the authentic full output and raw recovery control. This resolves the strongest manufactured-loss objection. The projection result remains a modest implementation observation, not a new theory or proof that the format cannot carry the information.
2. **Schema acceptance and UI meaning are separate.** The reviewer checked the native field definitions, including the separate model/version inputs, actual access-method options, prospective severity, prevalence, disclosure fields, detection guidance, and the coordination meaning of `mitigationNotes`. The final cases do not misuse missing required booleans as uncertainty. Each pair changes one declared native leaf. They are schema-valid synthetic records, not demonstrated UI sessions.
3. **Supplied-field recovery is not a response decision.** The 13 queries concern supplied values, omissions, or text. The initial clocks/containment/ownership questions lacked established native encodings and were correctly narrowed or removed. No operational utility or escalation outcome is evaluated.
4. **Raw and package preservation can defeat a general loss claim.** The actual JSON-LD embeds the source under `flare:raw`. Static inspection of the native download hook identifies original JSON and separately packaged attachments. The protocol requires full-output/raw controls and bars package-loss claims without execution. Empty attachments delimit the present result.
5. **Different text is not semantic correctness.** The version target must be checked against the separately supplied version. Capitalization and composite narratives cannot be scored as semantic failure using literal equality. The revised harness names its field `exact_source_representation_equal` and the protocol limits its interpretation. A dedicated field can contain prose.
6. **Selection and timing must remain exploratory.** The suite was selected after source inspection. Diagnostic output already existed by 23:52:03 UTC, before completion of the prose protocol. The earlier claim that a later file modification time established the first execution was corrected. The freeze before a confirmation rerun does not retroactively create preregistration.
7. **Publication rights and privacy require accurate boundaries.** Records use fictional content and `.invalid` contact information. Restricted source snapshots remain local; code is fetched separately from its pinned MIT-licensed repository with the upstream licence intact. No original-project reuse licence is implied. No live report submission is part of the design.

## Contribution assessment

Holeman and colleagues already test detection-relevant preservation under security-log normalization. Database mapping research distinguishes reconstruction from query preservation, and bidirectional-transformation research supplies round-trip laws. FLARE itself discusses semantic exports and raw retention; the contemporary MIT practitioner report explicitly recommends crosswalk testing. This suite therefore contributes a version-specific, inspectable regression artifact and finite counterexamples. The reviewed literature did not establish an identical artifact, but neither this search nor this review proves novelty or predicts publication acceptance.

The most informative anticipated witness is the explicit build version: the authentic JSON-LD named version uses the source model, and the standalone CERT-style converter gathers platform/model rather than the separate version. The full raw record can preserve that same difference. These are compatible observations and must remain together in the manuscript.
