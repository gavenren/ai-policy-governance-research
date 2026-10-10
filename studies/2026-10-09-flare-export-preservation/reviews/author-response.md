# Author response to separate AI critical review

Recorded 2026-10-10 UTC. These responses concern the executed technical case study; they do not claim human or external peer review.

| Review item | Disposition | Evidence and change |
| --- | --- | --- |
| R1: generated forwarding statement | Resolved | Section 3 and both reproduction READMEs now identify the authentic CERT converter's VINCE forwarding line as unchanged template boilerplate. No report was transmitted. Original converter outputs remain unedited. |
| R2: runtime outside upstream range | Resolved within scope | Section 6 now reports portable Node 22.23.3 sensitivity, which lies within the declared range, alongside the original Node 24.14.1 run. The entire result object differs only at runtime version and in-range metadata. Both runtimes passed all eight harness tests; a separate reviewer reproduced both result hashes. `results/runtime-sensitivity.json` records acquisition URLs, checksums, execution and complete-object comparison. Same-host/dependency and absence of release-signature verification are disclosed. |
| R3: actual review/run status | Resolved in revised manuscript | Working/provisional language is replaced by completed execution and separate AI-review descriptions. Section 7 gives actual confirmation times and links the review and responses. Human/practitioner validation, fresh-environment replication, UI/ZIP/recipient testing and external peer review remain explicitly absent. Final manuscript hash is recorded by the reviewer in its closing addendum. |

No numerical result changed in response to review. The complete JSON-LD/raw preservation findings remain prominent, and counts are diagnostic cases rather than population estimates. The contribution remains a pinned implementation regression artifact; general crosswalk, information-preservation and round-trip methods are established prior art.

Promotion to complete-study draft also depends on the repository publication checklist and PDF inspection, which are separately recorded in `completion-gates.md`.
