# Benchmark design gate

Status: **protocol/design working notes**, 2026-10-09 UTC. AI-authored design with a separate AI design challenge; no human or practitioner review. No converter outcomes are asserted in this document.

## Decision

**GO for a bounded audit of FLARE's actual client export implementation at `f51514d4b999fa7988e05d44b9bf18ea0aa98031`. NO-GO for the original general information-loss hypothesis.** This is potentially a useful, reproducible engineering case study. Its novelty is provisional and modest. An executable regression artifact can be valuable even if it does not justify a broader publication claim.

The [prior-art gate](PRIOR_ART_GATE.md) establishes that reporting crosswalks, retained versus disclosed evidence, scenario testing, query preservation and reconstruction tests already exist. The [schema feasibility notes](SCHEMA_FEASIBILITY.md) establish that OECD and ETSI provide narrative channels that can retain the proposed facts. Defining a restrictive conversion ourselves and then finding that it loses omitted facts would mainly demonstrate our restriction. The malformed printed ETSI schema would also make a claimed official executable benchmark unsound without substantial researcher choices.

The pinned FLARE implementation gives a less arbitrary target: existing native form fields, existing converters, and an existing bundle composition. The artifact tests their actual behavior rather than a deliberately lossy invented mapping. All choices follow exploratory source inspection; this is not preregistered or a blinded test. The study must say so.

## Minimum defensible design

Use 16 selected pairs of JSON-serializable source records, each differing at exactly one native leaf field. Validate both members using the native condition-dependent Zod schema. Run the actual client JSON-LD and CERT-style converter functions with time frozen. Compare the source record, full JSON-LD, the JSON-LD view with only `flare:raw` excluded, raw recovery, and standalone CERT-style JSON. The download hook's complete ZIP is an essential interpretive control; do not assert execution of that hook unless it is actually exercised. Empty attachment arrays restrict the core audit to non-file content.

The selected source fields cover build/version, access method, expected and actual behavior, harm narrative, prospective severity, prevalence, documented weakness, detection guidance, disclosure intent/date/embargo, and coordination notes. The 13 exact field queries and 16 pair definitions are in [the study fixtures](../studies/2026-10-09-flare-export-preservation/data/fixtures.json). These are supplied-answer preservation queries, not validated legal or operational decision rules.

Native uncertainty options and omission are used where supported. Negative, uninvestigated, disputed, and updated assertions are tested as exact strings in genuine narrative fields. The researcher annotations are not represented as native typed states. No missing-versus-false test is permitted for the required classification booleans. Source `severityOfHarm` asks about prospective harm; `mitigationNotes` asks about coordination; `discoveryNarrative` asks about recurrence. Internal names must not override the actual UI meanings.

The strongest potential witness is a pair with fixed platform/model and a changed native version: source code routes model into JSON-LD's version field and omits the separate version from CERT-style output. Execution may establish a named-field projection limitation. The embedded source record may simultaneously establish successful information transport. These findings are compatible and must appear together.

## Six originally proposed workflow questions

| Initial question | Faithful treatment in this bounded study |
|---|---|
| Which system/version is affected? | Test supplied native model/version/access fields; make no assertion about actual deployment identity. |
| Was harm observed or merely potential? | Required `real_world_harm` is a Boolean; preserve it as a source answer. Do not create invalid unknown/missing Boolean pairs. Prospective severity is separately tested. |
| Was no impact confirmed or has impact not been investigated? | Encode the distinction only in supported harm narrative, with a separate hypothetical financial harm held fixed. No native general investigation-state enum is assumed. |
| What are the occurrence/discovery/notification timestamps? | No native dedicated triple was established. Record as a coverage limitation. `dateCreated` and public-disclosure date are not substitutes. |
| Is containment complete, ongoing, or unknown? | No native containment-state field was established. Do not relabel coordination notes or prospective detection guidance. Not scored as a translation failure. |
| Who owns escalation? | A coordination contact or dispute can be supplied in narrative. The native submitter, developer, and selected recipients do not establish that role. No typed owner claim. |

## Interpretation and stop rules

1. Output inequality only shows discrimination; it does not prove that the answer is correct. Check the version mapping directly, and classify generic text versus dedicated fields separately.
2. Equality of a standalone export for a source pair establishes a collision for that artifact, under the frozen metadata and tested inputs. It does not establish loss in the complete download or in the reporting service.
3. `flare:raw` extraction is raw-payload recovery, not evidence of a supported native inverse converter or universal JSON-LD round-trip correctness.
4. A selected-case count is neither incident prevalence nor a population failure rate. Include preservation controls as well as collisions. Report all planned cases.
5. A minimum-valid form is a collection comparison, not a translation-failure baseline. No absent fact can be described as lost in conversion. A typed research extension would mostly demonstrate a chosen interface contract here, so defer it rather than use it to inflate the contribution.
6. If execution shows preservation in all relevant outputs, retain the negative result. If only an expected subset view omits fields with no promise of exposure, frame the output as a limited artifact audit. No claim of governance harm or operational improvement follows without recipient and practitioner validation.
7. Independent review must check source validity, actual exporter execution, deterministic comparisons, raw controls, fixture semantics, and the bounded claims before complete-study status.

## Separate AI design challenge

A delegated AI reviewer read the local code and challenged this design without editing or executing it. It supported the bounded pivot and identified six risks: confusing subset views with the delivered ZIP, invalid missingness, discrimination without semantic correctness, unverified recipient semantics, overclaiming raw/file preservation, and cherry-picked inputs or uncontrolled timestamps. Those objections are incorporated above. This design review is not the study's later independent result review.
