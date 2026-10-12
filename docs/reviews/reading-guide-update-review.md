# Review of the S014, S015 and S011 reading-guide update

Final check: **2026-10-12T18:18:33.649841Z**. Reviewer: a separate AI agent. This is a document review, not human peer review or a new review of every study.

## Scope and method

I compared `docs/READING_GUIDE.md` with Git commit `46f3fc3882f5e7c0b1c77649cc4d0e719f4aa347`. The change adds three paragraphs about S014, S015 and the equal-budget S011 extension. It also extends the study range to S015, changes the financing-paper count from three to four, and removes the outdated description of S012 as the final paper.

I read the guide and its full diff. I checked the S014 manuscript's allocation rule, demand limits, budget changes, capped alternative and limits. I checked S015 Sections 1–6, including its weighting condition and full-participation result. I read S011 Section 8 in the controlling manuscript, the retained section draft and the extension README. I also checked the original S011 central-result passages to confirm how the new paragraph follows the old one. The five inspected manuscript/support files listed below were byte-identical to their versions in the comparison commit.

I checked all **14 local Markdown links** in the guide. Every final target file exists. I checked the S011 Section 8 heading against the final fragment identifier. No study code or numerical analysis was run. These checks concern the guide's account of published results, not a new validation of those results.

## Findings and fixes

1. **S011 link:** The first draft linked to `extensions/benefit-unit/paper.md`, which did not exist locally or in the comparison commit. An intermediate edit linked to `section-draft.md`. The extension README identifies that file as a drafting aid and the main S011 manuscript as controlling. The final guide links directly to Section 8 of that manuscript. The file and heading are present.
2. **S011 outcome unit:** The first wording could suggest that the study measured each person's own resources against the threshold. The final wording says that it counts people living in families below the threshold. This agrees with the manuscript, which assigns the family result to its members and does not measure individual consumption. The description of equal gross budgets, a common needs rule and different rankings across outcome measures is supported by Section 8. The guide does not present the assumed needs rule as measured need or one payment rule as universally best.
3. **S015 weighting condition:** The first wording referred only to fixed assumptions. The final paragraph names firm equity values as the weights for the group sales means. It correctly states that full participation then fixes member receipts as well as the total. It also retains the limits on input validity, firm value and behavior. The paper's conditional ranges are not presented as observed revenue or available dividend cash.

The S014 paragraph accurately separates exhausting a total budget from respecting each demand limit. It gives credit to the existing capped rule and does not claim that the study invented it. Its description of changes to earlier allocations is consistent with the manuscript's distinction between unchanged claims and updated claims. It does not infer wasted equipment or energy from an award above demand, or claim that the capped rule solves every allocation issue.

The revised study range and count are correct for this guide version. The introduction still says that the papers are separate models with different assumptions. No new claim of human review or a validated joint policy model was added.

## Decision

**No blocker remains for this guide update.** The author made all three corrections; I did not edit the guide. The final summaries are clear, supported by the cited manuscript sections and appropriately limited.

This decision applies only to the final guide hash below and to the S014, S015 and S011 additions plus the stated introductory edits. It does not substitute for the pending S016 study review. A later S016 guide paragraph requires an addendum. It also does not confirm a later GitHub upload.

## Content hashes

All values are SHA-256.

| Material | Hash |
|---|---|
| Guide before the update, from comparison commit | `37183c534559bf49ff7c380bb1beda2ae7f3151fa170f94129e756e9b7faa843` |
| Intermediate guide after the first link repair, captured at 18:17:50.672060Z | `0ae011283b11925a05d16a3f06199977a55f79086747aefa200c8e1c20723505` |
| Final reviewed guide | `31e631f4e70e9245eacb4bbb6f9796c25346a87bb44c90bd788f7002c1887cc9` |
| S014 `studies/2026-10-12-compute-allocation/paper.md` | `46361e8733a4ed4a1ce7eb4a4d9ee331e89565dc221c62382067bed9db008b33` |
| S015 `studies/2026-10-12-equity-levy-aggregation/paper.md` | `67b37a3c6ff3307f07116bbfef9da460a7296e083c0c55947217bac2c80ba163` |
| S011 `studies/2026-10-11-household-debt/paper.md` | `bd37d56ca09edfc28b053265666e794af0fd2587dd46da3830b5613b01256f15` |
| S011 extension `section-draft.md` | `74e9586116368863a6086ec3c42d24f5507c3828e096937480f114475c8499a7` |
| S011 extension `README.md` | `d6ba5ca375e35d7dba967e8dbad6497e40b5ad1d2207b006aef16fb895c57d98` |

The first guide draft's broken link was observed before a file hash was captured. Its finding is preserved above; the intermediate hash is not described as the initial draft hash. The comparison commit supplies the exact before-update guide version.
