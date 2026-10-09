# Reporting schema feasibility

Status: **working notes**, prepared by a Codex AI research agent on 2026-10-09. No human review or standards-body confirmation has occurred. These notes support a study design gate; they are not a finished paper or a claim of conformity.

## Gate result

**Conditional GO** for tests of named collection, mapping, and query profiles. **NO-GO** for a claim that either format necessarily discards the proposed response facts. Both have text fields that can retain those facts. Test raw retention separately from the ability to answer a structured query.

The ETSI printed schema cannot be used unchanged as executable JSON. A study can use a clearly named, researcher-authored profile based on the prose. Its tests must be called **profile validation**, not official schema validation. Do not claim a unique correction of the standard. Several defects need a semantic choice, not a punctuation fix.

## Editions, dates, and status

- OECD, *Towards a common reporting framework for AI incidents*, Artificial Intelligence Papers No. 34. The [publisher record](https://www.oecd.org/en/publications/towards-a-common-reporting-framework-for-ai-incidents_f326d4ac-en.html) gives **2025-02-28**. The [PDF](https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/02/towards-a-common-reporting-framework-for-ai-incidents_8c488fdb/f326d4ac-en.pdf) gives February 2025. This is a policy reporting framework. Its required criteria are requirements within the framework, not universal statutory reporting duties.
- ETSI, [TS 104 158-2 V1.1.1](https://www.etsi.org/deliver/etsi_ts/104100_104199/10415802/01.01.01_60/ts_10415802v010101p.pdf), cover month **2026-03**. The [official work item](https://portal.etsi.org/webapp/WorkProgram/Report_WorkItem.asp?WKI_ID=75426) gives publication **2026-03-16**, latest version 1.1.1, and harmonised-standard status **No**. The [technical group page](https://www.etsi.org/technical-groups/sai/) lists this edition as published. It is a technical specification. This evidence does not establish legal conformity or a reporting duty.
- ETSI Part 2 cites Part 1 as a normative reference. A full conformity assessment would therefore need Part 1 too. These notes inspect Part 2's common-container fields only.

Source bytes, retrieval times, and SHA-256 hashes are recorded in [STANDARDS_SOURCE_MANIFEST.json](STANDARDS_SOURCE_MANIFEST.json). Full PDFs, extracted text, and page images remain in ignored `.local-sources/`. They must not be committed. The OECD paper has a CC BY 4.0 notice with exclusions for third-party material. ETSI states reproduction restrictions. These notes contain field facts and analysis, not a copy of either publication.

## Required information and native representations

OECD has 29 criteria. Table B.1 on printed pp.23-24 marks seven as required: criteria **1, 2, 3, 4, 7, 10, 11**. These cover title, narrative, system relationship, submitter, supporting material, severity, and harm category. The rest are optional. Page 15 allows implementations to change the required set for their context. The PDF defines answer formats rather than a complete JSON schema. It does not specify JSON keys, null handling, string length minima, or a universal validation algorithm.

ETSI adds a container-version field. Annex A's required list on printed pp.18-19 has eight names: `AICIECCversion`, `AICIECCtitle`, `AICIECCincidentDescription`, `AICIECCsystemRelationship`, `AICIECCsubmitterInformation`, `AICIECCincidentMaterial`, `AICIECCseverity`, and `AICIECCharmType`. Clause 4.1 also calls them required. The record has 30 named data fields in the prose.

Use non-empty synthetic required values in fixtures. Do not claim that this is the only minimum-valid record definition. For multi-choice fields, do not silently convert multiple selections into one category. ETSI prose permits multiple values and free content in several fields, while Annex A often expresses a single enumerated string. This difference must be resolved in the profile and disclosed.

| Proposed fact | OECD native location | ETSI Part 2 native location | Consequence for the benchmark |
|---|---|---|---|
| System and version | Optional criterion 8; text | Optional `AICIECCaiProduct`, 4.1.10; string in Annex A | Native text can preserve both. Splitting name and version into separate typed fields is a researcher convention. Do not count preserved text as absent information. |
| Observed versus possible harm | Required criterion 10 has hazard and incident classifications; criterion 11 gives harm categories | Required `AICIECCseverity`, 4.1.12, has hazard and incident classifications; required `AICIECCharmType`, 4.1.13 | Truthful native classifications must change when their meaning requires it. Keeping severity fixed merely to create a collision is invalid. Event classification does not necessarily type every individual consequence. |
| Confirmed absence of impact versus no investigation | No general dedicated assessment-state field. Criterion 15 is a rights-impact checkbox, not a general impact assessment | No general dedicated assessment-state field. `AICIECChumanRightsImpact`, 4.1.17, concerns rights only | Text can state either condition. An unchecked or omitted rights box is not evidence of a completed general investigation. |
| Occurrence, discovery, notification | Optional criterion 5 provides one date, for first known occurrence | Optional `AICIECCdateFirstOccurred`, 4.1.7; prose specifies a UTC calendar date | Do not rename occurrence as discovery or notification. No separate native fields for those two events were found. Their times can remain in narrative or added information. Time of day is also not a stated requirement for this date field. |
| Containment complete, ongoing, unknown | Optional criterion 27 provides action categories and text | Optional `AICIECCactionTaken`, 4.1.29, provides action categories and free content in prose | An action category alone does not establish its completion. The text can preserve completion state; a typed state is a profile addition. |
| Person or team responsible for escalation | Criterion 4 concerns the submitter; criterion 9 concerns developers/deployers | `AICIECCsubmitterInformation`, 4.1.6, and `AICIECCaiSystemDeveloper`, 4.1.11 | These roles do not necessarily identify an escalation owner. Do not infer ownership from them. A named owner can be retained in narrative. |

The field absence statements above concern dedicated fields in these editions. They are not claims that the formats prohibit the information.

## Missing, unknown, negative, disputed, and updated values

Neither document supplies a common typed state system for these five conditions. Optional omission can mean that information was not supplied. It must not be interpreted as a negative finding. Generic null values and empty-string semantics are not defined by the OECD criteria. Annex A's string declarations do not by themselves allow JSON null.

OECD checkbox criteria include 13, 15, 19, 21, 22, and 24. A researcher must specify how an unanswered checkbox differs from an explicit negative response. The document does not justify converting all unselected boxes into confirmed negatives. ETSI's prose describes indicator flags for several related fields, but Annex A does not give an executable flag encoding.

Narrative may record uncertainty, disagreement, provenance, or an update. Neither inspected common record supplies a general versioned assertion or update-history mechanism. `AICIECCversion` is a format-version field, not an incident revision number. Do not use it as the latter.

## Narrative, attachments, and extensions

OECD criteria 2 and 29 accept text; criterion 7 accepts text, URLs, and upload. Criterion 27 also has text. ETSI 4.1.4 and 4.1.31 give unconstrained incident-description and additional-information values. Clause 4.1.9 provides a location/link for supporting material. It does not itself guarantee that linked content travels with a record.

Thus, an honest conversion can retain every synthetic source fact as text in `AICIECCadditionalInfo`. An attachment-preserving profile must package actual bytes or verify a stable attachment, not merely preserve a URL that may fail. An exact serialized source object stored in a text field is a valid research baseline for transport retention. Its structured decoder is an added convention, not a native query capability.

Annex A does not set `additionalProperties` to false. A standards-compliant JSON Schema interpretation would normally leave extra properties allowed, but the printed document does not identify an executable dialect and is malformed. Do not silently add a closed-world restriction and attribute resulting loss to ETSI. Include an explicitly named extension-friendly sensitivity condition, or use the clear text channels.

## ETSI implementation defects verified from page images

The PDF was rendered locally with macOS PDFKit. The researcher inspected printed pp.9, 11, and 15-19. The following issues are visible in the pages; they are not merely text-extraction artefacts.

| Location | Verified issue | Smallest defensible implementation treatment |
|---|---|---|
| p.15, schema metadata | Dialect and schema-identifier URLs are placeholders | Choose a supported dialect and a new researcher-owned identifier. Label both as additions. |
| p.15, system-relationship and submitter enumerations; p.16, harm-category enumeration | Commas are missing between some adjacent values | Add separators for parsing, with a correction log. This does not resolve the prose's multi-value/free-content semantics. |
| p.15, first-occurrence date | A string type is followed by a malformed day/month/year block with missing values | No unique punctuation-only correction exists. A profile may choose the date string described in 4.1.7, and disclose that choice. |
| p.16, harm-consequence entry | Trailing comma after the string type | Remove the trailing comma for strict JSON parsing. |
| pp.16-18, flag-bearing entries | Boolean literals in braces are followed by a separate string token | Define a new flag-plus-explanation representation or avoid these entries in the core test. Do not call the choice an official fix. |
| p.18, autonomy and action entries | Closing quotation marks are missing | Add the closing quotation marks for parsing. |
| p.16, severity | An incident category is repeated | Remove a duplicate only in the researcher validator. Do not infer that its intended replacement is disaster. The prose on p.11 also repeats it. |
| p.18, multiple-system property | Its name has an extra initial A compared with 4.1.26 | Record both spellings; any alias or chosen canonical spelling is a profile choice. |
| p.9 versus p.15 | Prose specifies initial format version 1.0.0; Annex A identifies 1.0.1 | Pin both document edition and selected profile interpretation. Do not equate either number with TS version 1.1.1. |

There are semantic differences as well. For example, Annex A's description of incident supporting material refers instead to developers/deployers. The appropriate meaning for this study comes from 4.1.9, not that mismatched description. Some enumerations omit the free-content mechanism allowed by prose. A punctuation-repaired copy would still not resolve these differences.

The official [edition directory](https://www.etsi.org/deliver/etsi_ts/104100_104199/10415802/01.01.01_60/) lists only the PDF. The [parent directory](https://www.etsi.org/deliver/etsi_ts/104100_104199/10415802/) lists only edition 1.1.1. Targeted searches of ETSI and ETSI Forge did not locate a separate official schema or a post-publication erratum on 2026-10-09. This is a search result, not proof of absence. The work-item history records a corrected draft before publication; that entry is not evidence of a later repair.

## Study constraints derived from this check

1. Name each researcher profile and publish every mapping rule before interpreting outcomes. Preserve native text and support material in a required positive-control baseline.
2. Score transport retention, native-field availability, and structured query success separately. Store an explicit reason when a fact was not collected.
3. Test truthful populated native fields first. A zero-loss result on those tests is a finding, not a reason to delete fields.
4. Count synthetic record pairs and mapping configurations only. Do not interpret those counts as incident prevalence or operational benefit.
5. Treat ambiguous native syntax and semantic interpretation as a separate result. Do not count parser failure as decision-information loss.
6. Do not claim that the six workflow questions are legal notification rules. Practitioner validation remains outstanding.

