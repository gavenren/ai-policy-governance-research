# Design, implementation and correction record

## 2026-10-12T13:49:06Z — prospective numerical design, exploratory question

The algebraic concerns and positive consumption-tax interpretation were known before the numerical protocol. The record is prospective for numerical design only. No calculation was represented as preregistered discovery. The cited growth model had already been read and was retained as favorable evidence.

## First execution, 2026-10-12T13:56:51Z

The standard-library analysis produced every planned table. Fifteen tests passed. The random check generator implements lognormal(0,1) incomes and uniform draws for a in [0.1,2], b in [0,10], saving in [0,0.99], and tax in [0,3]. The earlier protocol specified lognormal draws and 200 cases but did not state these distribution parameters or uniform bounds. They were selected in implementation, before this run, and are disclosed here rather than added retrospectively to the original design. These random cases test software identities; they do not estimate an economic distribution or establish the formal results.

The protocol also called for four component arrays without listing their entries and one log-index array. The explicit arrays in `data/design.json` are implementation choices, not previously registered empirical hypotheses. The CES, affine, tax and input-path grids follow the numerical ranges recorded in the protocol. There were no failed numerical runs or omitted planned output tables before review.

## 2026-10-12T16:53:53Z — review corrections and source dates

The separate reviewer found an incorrect third-author given name and initial. The pinned PDF and arXiv record identify Maciej Szkróbka. The manuscript reference and evidence record were corrected. This was a bibliographic error in this audit, not a source change. The manifest already used surnames only.

The PDF cover date is 15 September 2026, whereas the arXiv v1 submission history gives 13 September 2026 at 19:32:23 UTC. These are distinct source dates. The manuscript, evidence record and manifest now state that difference; no explanation for it is inferred.

The reviewer also found that the dictionary referred to random bounds as if they were specified in the protocol. The dictionary now gives the actual implementation bounds and links this disclosure. The original protocol is preserved. No analysis code or retained numerical result changed for these corrections.

The source-acquisition tool was tested in a fresh ignored directory. The pinned PDF, original source archive and cited growth paper matched their retained SHA-256 hashes. The public acquisition log records actual new retrieval times. The unpinned arXiv history was captured again separately; its actual retrieval and observed version are in `version-recheck.json`.
