# AI policy and governance research protocol

Version: 1.0 · Established: 2026-10-09 UTC · Status: programme protocol

This programme aims to produce publication-quality research; that aim is not a certification of quality, originality, peer review, or acceptance. Every study must distinguish observed evidence, researcher coding, inference, and speculation. A null, negative, or inconclusive result is an acceptable outcome.

## 1. Scope and authority

- Use public sources and public, permissible data only. Do not incorporate private correspondence, course materials, personal information, credentials, or confidential documents. Public availability alone does not establish redistribution permission.
- Publish only in the newly authorized `gavenren/ai-policy-governance-research` repository after its identity and public visibility are verified. Do not modify `gavenren/ai-safety-research` or any other existing repository. Read-only duplicate checks may inform the queue.
- No journal submission, external messaging, publication elsewhere, account changes, new credentials, paid APIs, paid compute, or paid publication. No reuse licence has been selected; do not add one. Record third-party rights separately from rights in original work.
- Use normal supported task execution. Stop and report an actual usage/quota limit, a paid-use requirement, or an access/authorization barrier; do not evade it. Otherwise continue with the next justified study. Do not infer unlimited entitlement from successful calls, impose an artificial paper quota, or promise uninterrupted execution.

## 2. Study lifecycle and labels

Use exactly one primary state in each study's metadata and opening manuscript block:

1. **Protocol:** question, prior-work search, planned corpus, methods, and decision rules; no completed-study claim.
2. **Working notes:** collection, analysis, or writing in progress; preliminary results may change.
3. **Complete-study draft:** all completion gates below passed; independent AI critical review and its disposition are public. This does not mean human-reviewed, peer-reviewed, legally endorsed, or publication-ready by external assessment.
4. **Superseded or withdrawn:** retain the earlier evidence and state the reason, replacement, and affected claims.

Record transitions with UTC timestamps and Git commit references. A protocol is prospective only for decisions recorded before the relevant analysis. Disclose exploratory choices and deviations; do not retrospectively call them preregistered. Protocols and working notes may be committed when accurately labeled, but must not be counted or promoted as completed papers.

## 3. Choose a contribution before expanding the corpus

Maintain a queue containing: study ID, question, unit of analysis, proposed contribution, nearest prior work, distinctness rationale, necessary data, feasibility, state, and reason to proceed or defer. Select questions whose answer could change after observing evidence. Prefer a tractable, defensible contribution over a broad descriptive survey presented as novelty.

Before committing to a contribution:

- Search the closest scholarly work, official analyses, preprints, and relevant repositories using multiple query formulations and citation/reference following. Log search service, exact query, retrieval time, date filters, inclusion rules, and candidates screened. Search limitations must be explicit.
- Read the closest work rather than relying on titles or search snippets. Record what each already establishes, its corpus/cutoff/method, and the proposed study's incremental contribution.
- Compare against this programme and the separate public research programme when accessible. A new jurisdiction, date window, or metric alone does not establish a distinct study. Closely related results should normally become one study or a transparent update.
- Write a bounded novelty statement: what appears unaddressed in the searched literature as of the cutoff. Never claim proof that no prior research exists.
- Fix the primary question, inclusion/exclusion rules, unit of analysis, expected output, and stopping rule. Distinguish confirmatory hypotheses from exploratory questions. Change them only with a dated reason and impact assessment.

## 4. Evidence ledger and snapshots

Every material factual claim must resolve to a source identifier and a locatable passage, table, provision, dataset field, or executed result. Use fresh public primary sources for current policy facts: official legislation, gazettes, court decisions, regulator/government publications, standards bodies, or original datasets. Use original research for prior-work claims. Secondary sources may aid discovery or interpretation but cannot silently substitute for the underlying authority. Search-engine snippets and AI-generated text are not evidence.

For each source record at least:

| Field | Requirement |
| --- | --- |
| Identity | Stable source ID, title, issuing body/authors, canonical URL, document/version identifier, source type, language |
| Dates | Exact publication/update dates where available; separately record adoption, official publication, entry into force, and applicability dates when relevant; use `unknown` rather than inventing precision |
| Retrieval | Actual retrieval timestamp in UTC (`YYYY-MM-DDTHH:MM:SSZ`), requested and final URLs, acquisition method, and access failures |
| Snapshot | Path, media type, byte length, SHA-256 of the bytes actually retained, and version relationship to other captures |
| Claim location | Page/section/article/table or stable text locator; distinguish source wording from interpretation |
| Rights | Source rights/terms and whether redistribution was checked; attribution requirements and redactions, if any |
| Coverage | Relevant jurisdiction, governed entity/activity, exclusions, and known gaps |

Preserve original bytes separately from extracted or cleaned text. Hash both if both are used; record the extraction tool/version, transformations, OCR uncertainty, and source-to-extraction relationship. Never silently replace a changed web page: retain a new dated version and log the difference. For dynamic pages, capture the actual content supporting the claim and record limitations of the capture.

Retain and commit full snapshots only when redistribution is permissible. Otherwise use a lawful, narrowly scoped evidence extract with provenance and a retrieval recipe; state that it is an extract rather than a full snapshot. A URL and hash alone do not prove what the source said or make it independently inspectable. If a pivotal claim cannot be supported by inspectable evidence, narrow or remove it, or keep the study unfinished. Do not publish restricted bytes merely to improve reproducibility.

Record the study's **evidence cutoff** as an exact date/time and define what it means (for example, documents retrieved and verified by that time). Recheck legal status and pivotal current facts against authoritative sources shortly before publication. Document searches after the cutoff separately; never imply coverage beyond the actual search.

## 5. Legal and policy status discipline

Maintain a separate instrument ledger when comparing legal or policy instruments. Distinguish proposed legislation, adopted but not effective rules, effective law, provisions not yet applicable, binding orders, official guidance, voluntary commitments, draft standards, and withdrawn/superseded instruments. Status applies to a specified provision, jurisdiction, actor, and date; one status label may not describe an entire instrument.

For each material legal claim, identify the authoritative text, relevant provision, status at cutoff, conditions/exemptions, and the dates supporting that status. Separate announced political agreement or proposed delay from enacted amendment. Separate enactment from implementation and enforcement. Verify consolidated texts against amendments when necessary. Flag unresolved translations, jurisdictional interpretations, and source conflicts instead of selecting the convenient reading. Do not infer measured compliance or effectiveness from the existence of a rule.

## 6. Analysis and reproducibility

Use a study directory under `studies/<stable-id>/` with the following logical structure (omit empty directories and explain in the study README):

```text
README.md                 # state, contribution, exact reproduction commands
protocol.md               # dated plan and deviations
paper.md                  # manuscript with opening state and disclosure
sources/manifest.csv      # provenance and evidence ledger
sources/snapshots/         # permissible retained originals/extracts
data/raw/                 # immutable inputs with provenance
data/derived/             # generated tables/coded corpus
code/                     # acquisition, transformations, analysis, validation
results/                  # generated tables/figures and run metadata
reviews/                  # independent AI critique and author response
logs/                     # searches, decisions, executions, changes
```

Keep a documented schema/data dictionary, environment/dependency versions, and exact commands. Prefer a small reproducible dependency set and free local computation. Use fixed random seeds where applicable. Record software versions, input hashes, run timestamp, exit status, and relevant diagnostics. Separate network acquisition from offline analysis so a saved corpus can be rerun. Do not commit secrets, local account paths, or incidental personal data in logs.

Execute every analysis claimed as performed. Tables, plots, and reported numbers must trace to retained input data and executed code or to a fully specified, inspectable qualitative procedure. Provide denominators, missingness, exclusions, and units. Check input and output invariants, joins, duplicates, date logic, source linkage, and numerical reconciliation where relevant. Do not substitute a successful script exit for validation of the method or interpretation.

For document coding, publish the codebook, decision rules, ambiguous cases, and row-level evidence. Disclose who or what coded each item and whether any independent recoding actually occurred. Repeated AI passes are not human inter-rater reliability. Do not report agreement, interviews, surveys, expert validation, statistical tests, or causal identification unless genuinely performed and methodologically justified.

Choose sensitivity, uncertainty, and counterexample checks that could undermine the main result. State the estimand or target of inference, sample frame, coverage limits, and whether the evidence supports description, association, or causation. Report all prespecified outcomes, including null and unfavorable results. Preserve excluded records with reasons when lawful. Log failed analyses and revised interpretations rather than silently deleting contradictory findings.

## 7. Independent critical review

Obtain a separate AI reviewer/agent that did not author the study's central analysis. Give it the actual manuscript, protocol, code, data, and evidence ledger, plus authority to challenge the contribution. Record reviewer type, date, reviewed commit/content hashes, scope, tools/checks actually used, and access limitations. Do not invent a reviewer identity, imply human review, or call this journal peer review. Model/version may be recorded only if known.

The reviewer should examine the closest-prior-work comparison, factual and legal claims, coding assumptions, reproduction, alternative explanations, missing negative evidence, and whether the claimed contribution follows from the executed analysis. Have the reviewer reproduce or independently spot-check the highest-risk results when feasible; explicitly record anything it could not check. A separate agent's agreement is not a guarantee of correctness.

Preserve the critique and an issue-by-issue author response. Fix or narrow unsupported claims. Critical errors, unverified pivotal evidence, non-reproducible central results, and unresolved conclusions that overreach the evidence block complete-study status. Re-review substantive revisions to affected claims; document the final scope actually reviewed. Minor unresolved issues may remain if disclosed and not material to the conclusions.

## 8. Completion and public-commit gates

A complete-study draft requires a dated checklist with paths/commands/results, not merely checked boxes:

1. **Contribution:** closest work searched and read; incremental contribution and distinctness bounded; answerable question and analysis decisions disclosed.
2. **Evidence:** pivotal claims linked to inspectable public primary evidence; actual dates, retrievals, hashes, rights checks, and cutoff present; current legal status rechecked.
3. **Execution:** stated analyses actually run; exact commands and inputs retained; independent rerun or justified review check completed; central results reconciled with manuscript.
4. **Inference:** limitations, uncertainty, missingness, negative findings, counterexamples, and sensitivity checks reported; no unsupported causal, representativeness, novelty, or acceptance claims.
5. **Review:** independent AI critique, reviewed version, author response, and remaining limitations recorded; blocking issues resolved; actual human-review state explicit.
6. **Disclosure:** AI assistance and responsibility statement; current study state; evidence cutoff; funding/conflicts only if known; no invented affiliations, endorsements, or human participation.
7. **Release hygiene:** staged files inspected for private data/secrets, third-party rights, accidental artefacts, and unselected reuse licences; Git diff and generated outputs checked; repository identity verified.

Use normal non-destructive commits and pushes. Record the local commit SHA, verify the remote branch resolves to that exact SHA, and verify expected files at the remote revision. A local commit or attempted push alone is not verified publication. Report the repository URL, commit URL/SHA, study state, salient results, and unresolved limitations. Do not force-push, rewrite shared history, or alter existing unrelated repositories.

## 9. Corrections and continuation

Keep a programme index and queue current. For a changed source or discovered error, record the affected claim/result, evidence, severity, and correction; publish a new commit with a dated correction notice. Preserve prior versions and negative findings. Mark an invalidated complete draft superseded or withdrawn promptly.

After each verified milestone, choose the next genuinely distinct, feasible study from the queue or deepen an incomplete one. Stop with a clear checkpoint when cancellation, a real quota/paid-use requirement, or an access/authorization barrier prevents progress. A checkpoint states what is saved, what is unfinished, and what must happen to resume. Do not represent scheduled intent or an idle session as completed ongoing research.
