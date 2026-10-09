# <Study title>

> **State:** Protocol | Working notes | Complete-study draft | Superseded/withdrawn — select one.
> **Study ID:** `<stable-id>` · **Version/date:** `<version; actual UTC timestamp>`
> **Evidence cutoff:** `<actual UTC timestamp and coverage definition; unset until established>`
> **AI assistance:** `<actual roles/tools; no invented model identity>`
> **Review:** `<not yet reviewed / independent AI critical review completed on specified version; actual human-review state>`
> **Reuse licence:** No programme reuse licence selected. Third-party source rights are recorded separately.

Remove instructional placeholders only after replacing them with verified information. Until completion gates pass, label any results preliminary and do not describe this document as a finished paper. Do not invent author names, affiliations, funding, conflicts, interviews, reviewers, or acknowledgments.

## Abstract

For a protocol: state the question, rationale, planned corpus/method, and what would constitute an informative result; label it a protocol abstract. For a complete-study draft: summarize the actual question, observed sample and cutoff, executed method, principal results (with denominators/uncertainty as appropriate), contribution, and chief limitation. No planned analysis presented as a finding.

## 1. Question and contribution

- Research question and why it matters:
- Unit of analysis and target of inference:
- Primary hypotheses or descriptive questions; exploratory questions:
- Proposed contribution and closest known alternative explanation:
- What evidence could falsify or materially narrow the claim:
- Distinctness from this programme's other studies and the separate public programme:

### Closest prior work

| Source ID / citation | Corpus, cutoff, method | What it already establishes | Exact incremental contribution proposed here | Search/read limitations |
| --- | --- | --- | --- | --- |
| `<verified original research>` | | | | |

**Search log:** `<path with services, exact queries, UTC retrievals, filters, citation tracing and screening decisions>`.

**Bounded novelty statement:** `<what appears unaddressed in the work actually searched; no universal originality claim>`.

## 2. Policy setting and legal status at cutoff

Explain the institutional context using public primary sources. Keep proposals, enacted law, applicable obligations, enforcement activity, and voluntary instruments separate.

| Instrument/provision and jurisdiction | Authoritative source/locator | Status at cutoff | Adoption / official publication / entry into force / applicability | Scope, exemptions, unresolved interpretation |
| --- | --- | --- | --- | --- |
| `<one row may be needed per provision>` | | | `<separate dates; unknown if unresolved>` | |

**Pre-publication status recheck:** `<actual UTC time, authoritative sources, changes and impact>`.

## 3. Corpus, provenance, and collection

Describe the population/sample frame, collection window, search coverage, inclusion/exclusion rules, deduplication, versions, missingness, and stopping rule. Identify systematic blind spots and why each source is appropriate.

- Evidence manifest: `sources/manifest.csv`
- Public snapshots/extracts and rights checks: `<paths; full capture versus extract clearly distinguished>`
- Input data and dictionary: `<paths>`
- Collection/search/access-failure logs: `<paths>`
- Retained and excluded counts with reasons: `<actual counts or not yet collected>`
- Source conflicts, translation/OCR issues, and unresolved evidence gaps:

Each source manifest entry must include source ID, title, issuing body, canonical/final URLs, source/version type, actual publication/update dates, relevant legal dates, UTC retrieval, acquisition method, retained-byte SHA-256 and size, snapshot media type/path, claim locator, rights basis, and coverage. Preserve original and transformed bytes separately with transformation provenance.

## 4. Methods and decision record

Describe a method another researcher can execute. Specify variables/constructs, codebook, units, denominators, transformations, model/test assumptions (if any), missing-data handling, exclusions, uncertainty, and sensitivity checks. For qualitative work, specify how evidence is selected, coded, compared, and used to test alternative readings.

| Decision | Prespecified at UTC / commit | Implementation | Deviation and reason | Effect on interpretation |
| --- | --- | --- | --- | --- |
| `<primary outcome, scope or coding rule>` | | | | |

**Coder/analyst roles:** `<actual human or AI roles, independence and checks; no implied human coding>`.

**Threats to validity and planned disconfirming checks:** `<coverage, measurement, selection, confounding, time sensitivity and other relevant threats>`.

## 5. Results

For a protocol: write **Not yet executed**. For working notes: label partial results and incomplete checks explicitly. For a complete-study draft: report all prespecified outcomes and material exploratory results, including null, negative, conflicting, and inconclusive evidence.

| Claim/result ID | Observed result and denominator/uncertainty | Generated output / qualitative evidence | Source IDs and locators | Check and outcome |
| --- | --- | --- | --- | --- |
| `<R1>` | | | | |

### Sensitivity, counterexamples, and negative findings

Report what changed under credible alternative assumptions and what did not. Identify failures, counterexamples, unavailable tests, and claims dropped or narrowed. Do not equate absence of retrieved evidence with evidence of absence.

## 6. Discussion and limits

Explain what follows from the observed evidence and what remains uncertain. Separate descriptive findings, causal claims (only if identified), normative judgments, and recommendations. Show how the result compares with the closest prior work. State external validity limits, legal interpretation limits, time dependence, and conditions under which the conclusion would change.

## 7. Conclusion

Answer only the stated question to the extent supported. No promise of acceptance, proof of novelty, invented expert consensus, or claim of human review.

## 8. Reproduction and executed checks

**Environment:** `<OS/runtime/dependency versions or environment file; free local execution>`.

```sh
# Replace with exact commands that were actually run, from the documented directory.
# Keep network acquisition separate from offline reproduction.
```

| Check/run | Command or inspectable procedure | Inputs/hashes | Actual UTC run / exit status | Output and finding |
| --- | --- | --- | --- | --- |
| Acquisition | | | | |
| Offline analysis | | | | |
| Data integrity and claim reconciliation | | | | |
| Independent reproduction/spot-check | | | | |

**Reproduction limits:** `<restricted source redistribution, dynamic pages, unavailable dependencies/data, stochastic variation; identify consequences>`.

## 9. Review and disclosure

- AI assistance: `<actual research, coding, drafting and review roles; responsibility and known limits>`.
- Independent AI reviewer: `<separate agent/reviewer; known identity/version only; reviewed content hashes or commit, UTC date, scope and limitations>`.
- Review report: `<reviews/...>`.
- Author response and disposition: `<reviews/...; one response per issue>`.
- Human review: `<actual state; normally “No human review has been completed” unless verified otherwise>`.
- Funding/conflicts/affiliations: `<known facts only; otherwise omit or explicitly unknown where relevant>`.
- Material unresolved issues: `<state none only after checking>`.

Independent AI critique is not human review or journal peer review. If central evidence, methods, or conclusions remain blocked, retain Protocol or Working notes status.

## References

Include only verified sources actually used. Supply exact title, issuing body/authors, date/version, canonical URL, source ID, and relevant locator. Link each policy claim to primary authority and each claimed result to executed analysis or inspectable qualitative evidence. Put retrievals/hashes and redistribution details in the manifest.

## Completion record

Complete this record only after the study exists and the checks occur. An unchecked or unsupported gate blocks Complete-study draft status.

| Gate | Status | Evidence path / actual command / reviewed version | UTC checked | Remaining issue |
| --- | --- | --- | --- | --- |
| Closest work, bounded contribution and distinctness | Pending | | | |
| Primary evidence, provenance, snapshots/rights, cutoff and legal status recheck | Pending | | | |
| Claimed analyses executed and outputs reconciled | Pending | | | |
| Negative findings, uncertainty and inference limits | Pending | | | |
| Independent AI review and blocking-issue resolution | Pending | | | |
| State, AI assistance and actual human-review disclosure | Pending | | | |
| Staged-file privacy/rights/diff check; no unselected reuse licence | Pending | | | |

**Release verification:** `<repository URL; exact commit SHA/URL; remote branch equality; files verified at revision; actual UTC verification>`.

**Corrections/version history:** `<dated changes, affected claims, preserved earlier versions, protocol deviations>`.
