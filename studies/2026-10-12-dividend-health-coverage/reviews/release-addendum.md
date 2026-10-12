# S017 release addendum

Checked at 2026-10-12T18:56:33.121857+00:00. Same separate AI reviewer and role limits as [the critical review](critical-review.md).

**Decision:** R1 is resolved. No remaining blocker to complete-study draft status was found within this review's scope. Publication, repository authority and the final release-hygiene check remain separate tasks.

The release manuscript SHA-256 is `8585fd496381b90345db63d8b0e40bc67fbe063eb8c0f6456613a69a6b5158a5`. The exact [release patch](release-only.patch) changes only the hours-allocation wording and the state/review disclosures. The correction agrees with section 435.552(e)(2)(i). Reversing that patch in an ignored private copy restored the reviewed manuscript SHA-256 `e73447b018a38929bc294a9b6ec2c9b1ce61572accceeb26e39de2fb4fb0ad78`. The study README has only the corresponding state/review paragraph change; reversing it also restored its frozen hash.

All other 34 start-record files are unchanged. All 16 numerical-manifest entries still match. No protocol, code, input, result or source-package bytes changed. The case result remains `3f720fb491584eae82c11923a5fbcabc787737402491d2c43b8e7ee88222e1e7`. The prior execution checks remain applicable; none were repeated.

The author response accurately accepts R1 and retains the legal and inference limits. The completion record describes local completion and explicitly leaves remote publication to a later receipt. The root README and study queue correctly describe 40 constructed rows, ten tests and separate AI review. Their complete-study label is now consistent with this review decision.

The reading guide still has SHA-256 `e37f1586d152e514d4ec550becc6a758d9be43e3e660ba615b9f42a85de85b9d` and matches [its separate editorial review](../../../docs/reviews/reading-guide-s016-s017-review.md). The S017 release condition identified in that guide review is now met within the critical-review scope. The reviewer checked 91 local file-link destinations across the paper, study README, root README, queue and guide. This checks destination existence, not every heading anchor or remote URL.

[The release verification record](release-verification.json) preserves exact hashes, timing and checks. No Git state was changed by this reviewer, and no claim of remote publication is made here. No human review, legal certainty or actual coverage outcome is implied.
