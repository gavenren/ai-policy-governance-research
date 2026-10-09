# Study 2 source pilot — working notes

Status: source feasibility notes only. No study analysis, sample estimates, paper, or compliance assessment has been completed. This note was prepared by a Codex AI research subagent. It has not had human or independent critical review. Evidence cutoff: 2026-10-09 UTC. Source bytes, HTTP headers, PDF text, and rendered pages are retained locally under ignored `.local-sources/study2/`. Public retrieval metadata and SHA-256 hashes are in [STUDY2_SOURCE_MANIFEST.json](STUDY2_SOURCE_MANIFEST.json). The hashes identify the retrieved editions; they do not prove that the same content existed on an earlier date.

## Feasibility decision

Proceed only to protocol design and a search for dated historical evidence. The sources support an audit of which lifecycle dates a public reader can establish. They do not yet support a measure of the evaluation time actually available to a government buyer. They also do not support a vendor compliance league table. No duration was calculated in this pilot.

The proposed unit is one lifecycle event for a named model, endpoint, service platform, and buyer context. A model family alone is too broad. The proposed researcher measure is:

`R = max(N, A, Q)` and `W = max(0, D - R)`

Here, `N` is the time the buyer receives actionable notice; `A` is the time an eligible successor becomes available to that buyer; `Q` is the time usable documentation becomes available; and `D` is when access to the old service ends for that buyer. These are study definitions, not words or a formula in either policy source. Define what makes notice actionable, a successor eligible, and documentation usable before selecting events. A dated public notice, a general model release, a current documentation link, and a scheduled retirement are different evidence types. Missing values must remain missing.

## GSA source: edition, status, and scope

Primary source: [GSA Class Deviation RGO-2026-01](https://www.acquisition.gov/sites/default/files/page_file_uploads/RGO-2026-01.pdf). The retrieved PDF contains 230 pages. The initial memorandum is dated 2026-01-15. Clause 552.239-7001 has the edition label September 2026. These are different dates. The URL is an updated compilation, so the initial memorandum date does not date every clause now in the file.

Attachment A lists **2026-10-19** as the effective date for Part 552; its signature-date column shows 2026-07-16. Attachment A permits immediate use of its text before the listed mandatory start date. Thus, on 2026-10-09, the Part 552 mandatory start date is prospective. This does not show that no contract has already used the clause. The deviation addresses GSA acquisition activity. It is not evidence that the clause applies to every federal contract or every commercial API customer. Actual contract incorporation and applicable exceptions must be checked for any compliance claim.

The prescription at 539.71 and clause paragraph (a) cover the specified LLM systems when LLM capability is a material feature and government data is directly submitted to or produced by the LLM. Examples include assistants, chatbots, agentic systems, and LLM-enabled document or productivity tools. Exceptions cover specified internal contractor uses and incidental LLM features in products whose primary purpose is not AI, subject to the stated conditions. For those exceptions, paragraph (a) makes the clause self-deleting unless the contracting officer identifies otherwise. A lifecycle event on a general developer platform does not establish this scope.

Page anchors use **one-based PDF page numbers**:

| Item | PDF page | Printed page or location |
|---|---:|---|
| Deviation memorandum and application | 1–2 | Initial memorandum |
| Earlier use allowed | 4 | Attachment A introduction |
| Part 552 effective-date row | 6 | Attachment A table |
| 539.71 prescription | 53 | 47 of 224 |
| 552.239-7001 title and scope | 135 | 129 of 224 |
| Paragraph (i)(1)–(3) | 148 | 142 of 224 |
| Paragraph (i)(4)–(5) | 149 | 143 of 224 |

The date table, prescription, scope, and paragraph (i) were checked against local PDFKit renders as well as extracted text. A zero-based PDF tool uses page indexes one less than those above.

Paragraph (i) has distinct branches that a temporal study must preserve:

| Provision | Rule and material qualification |
|---|---|
| (i)(1) | Written notice to the contracting officer at least 30 calendar days before the listed material changes to models or actors, government-data services or controls, or specified foreign-law-driven modifications that materially affect outputs. |
| (i)(1)(iv) | Advance notice is not required for model changes when concurrent access is supplied under (i)(2). Do not impose an independent 30-day notice requirement on that branch. |
| (i)(2), ordinary branch | Before discontinuing or replacing a model used under the contract, order, or BPA, the contractor must use reasonable efforts to provide concurrent access to a successor and associated documentation. The minimum evaluation periods stated are 30 calendar days for major versions and 15 for minor versions. The effort qualification matters. |
| (i)(2), third-party branch | For a commercial provider's deprecation outside the contractor's control, the contractor must instead notify the contracting officer within five business days of receiving the provider's notice, and make best efforts to provide successor access as soon as it becomes available. Provider publication is not contractor receipt. |
| (i)(3) | Seven calendar days after identifying the specified material safety or performance degradation; the notice must describe the change and evaluation-related information. |
| (i)(4) | For the specified unplanned or emergency changes, notice is due as soon as practicable after learning of the change, with available remediation or rollback information. |
| (i)(5) | Notice content includes the change, affected parties and systems, limits and adverse effects, evaluation approach, remediation, and applicable flowdown confirmation, to the extent known at notification. |

A single public notice-to-retirement interval does not test these branches. The major/minor classification, the responsible contractor, its control over the change, its notice receipt, contract scope, and efforts are not established by lifecycle pages.

## OMB source: status and exact claim

Primary sources: [M-25-22](https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-22-Driving-Efficient-Acquisition-of-Artificial-Intelligence-in-Government.pdf) and the [official OMB memorandum index](https://www.whitehouse.gov/omb/information-resources/guidance/memoranda/). The issuance date is **2025-04-03**, as shown on PDF page 1 and the index. The `2025/02` URL path is not the issuance date. M-25-22 rescinds and replaces M-24-18. It is executive-branch acquisition guidance with requirements for covered agencies, not a general private-market statute. A targeted official-source check found no rescission of M-25-22. That check is not an exhaustive legal-status certification.

Section 2 covers agencies defined in 44 U.S.C. 3502(1), with some requirements limited to CFO Act agencies, and excludes Intelligence Community elements. It covers AI acquired by or for covered agencies. It has exclusions for specified common commercial products, regulatory and enforcement assessments, general testing methods, certain research, incidental contractor AI use, and national security systems. Section 2(c) applies to contracts awarded under solicitations issued on or after 180 days following issuance, and to renewal or extension options exercised on existing contracts after that period. Scope and timing are on PDF pages 2–4.

Section **4(d)(iii)E**, PDF page 10, addresses ongoing testing and monitoring. Its introductory contract-term requirement on page 9 is qualified by consistency with law and government-wide policy and by applicability. Subpart E requires contract terms that enable regular agency monitoring and evaluation. Its three subparts address agency-defined test data; vendor provision of access and time for independent evaluation, with an agency-permitted vendor-testing alternative and oversight conditions; and documented vendor test procedures with internal disclosure rights. It specifies no universal 30-day or 15-day period. Nearby subpart F encourages performance controls for new versions and rollback. Subpart G asks agencies to consider advance feature-notification terms where relevant. These different modal terms must not be merged into one strict deadline. Pages 1, 2, and 10 were visually checked.

## Lifecycle page pilot

The following are source examples, not a sampled dataset or measured results. Dates after the cutoff are scheduled dates, not observed removals. Sources were retrieved on 2026-10-09.

| Source and exact event | Dated facts present | Evidence still missing for the proposed buyer measure |
|---|---|---|
| [OpenAI API deprecations](https://developers.openai.com/api/docs/deprecations), `gpt-5.3-codex` | Heading 2026-10-01; scheduled shutdown 2027-04-01; current replacement `gpt-6-sol`. | Buyer receipt, eligible successor access date, historical usable-documentation date, and eventual actual shutdown. |
| [Anthropic model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations), `claude-sonnet-4-5-20250929` on Claude API | Deprecation 2026-09-30; scheduled retirement 2026-11-30; replacement `claude-sonnet-5-5`. [Release notes](https://platform.claude.com/docs/en/release-notes/overview) dated 2026-09-28 announce the successor's release. | Buyer receipt and eligibility, historical documentation completeness, and eventual actual retirement. A release announcement supports general availability, not access in a particular government deployment. |
| [Google Cloud model lifecycle](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-versions), `gemini-3.6-flash` on Gemini Enterprise Agent Platform | Release 2026-07-21; scheduled retirement 2026-11-19; replacement `gemini-3.8-flash`, listed as released 2026-09-02. | The specific retirement-announcement date, buyer receipt and eligibility, historical usable documentation, and actual access termination. |

OpenAI distinguishes legacy status from deprecation and shutdown. Its stated notice periods vary by model class, with safety and compliance exceptions. It also mentions possible continued access through dedicated capacity. Public shutdown dates therefore do not prove the termination date for every buyer. A conflict needs resolution before data extraction: the current page places `gpt-4-1106-preview` under both a 2026-03-26 past shutdown and a 2026-10-23 scheduled shutdown. Do not choose one silently.

Anthropic separates active, legacy, deprecated, and retired status. Its dates cover the stated Anthropic-operated platforms; partner-operated Bedrock and Google Cloud schedules can differ. A minimum future retirement date is a lower bound, not a fixed event date. Its general customer-notice policy and statement that developers were notified do not prove a named buyer's receipt.

Google's table gives release, retirement, and current replacement fields. The page reports an update date of 2026-10-09. Its short-term policy does not supply the date of each retirement announcement. Platform retirement must remain distinct from availability through another Google service. Current recommendations cannot reconstruct past alternatives: the table recommends `gemini-2.5-flash-lite` for `gemini-1.5-flash-001`, retired 2025-05-24, while the replacement's listed release is 2025-07-22, also confirmed on its [model page](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/2-5-flash-lite). This does not prove that no other successor was available before retirement.

## Required gate before analysis

1. Search the closest prior research and define a contribution distinct from a notice-period comparison. This pilot does not establish novelty.
2. Register event inclusion rules, platform boundaries, planned versus actual dates, documentation criteria, and the treatment of revised or conflicting dates before computing outcomes.
3. Seek dated primary release notes, migration guides, version history, and public contract records. A current source can report an earlier date, but it does not prove all current recommendations or links existed then. Preserve that distinction in provenance.
4. Keep separate fields for public announcement, provider claim of sending notice, contractor receipt, and buyer receipt. Also separate public release from contract-, region-, authorization-, and configuration-specific eligibility. Do not use a private record in this public programme.
5. Report missing or interval-valued dates without substituting zero, the retrieval date, or a policy minimum. Bounds require explicit assumptions: private notice or access can precede a public announcement, so the public interval is not automatically an upper or lower bound on buyer time.
6. Treat any public-data measure as an observability or public-opportunity measure, unless every buyer-level input is established. Neither source provides a complete test of contract compliance from public lifecycle dates alone.
7. Obtain independent critical review before any complete-study draft. Do not conduct live paid API evaluations or contact vendors or officials under this source-pilot authorization.

No fees, API inference, account changes, external messages, or external writes were used in this pilot. The remaining barrier is historical and buyer-specific evidence, not source download access.
