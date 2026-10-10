# Complete-study draft gates

**Local release checks recorded: 2026-10-10T00:07:46Z.** State: complete-study draft. The publication commit is verified separately after upload; this file does not claim an unobserved remote commit. This is an AI-assisted technical case study with separate AI review, not human or external peer review.

| Gate | Actual evidence and disposition |
| --- | --- |
| Contribution and distinctness | `../../docs/PRIOR_ART_GATE.md` and its source manifest compare the closest work. Generic crosswalk, preservation and round-trip novelty was rejected. The retained contribution is an executable regression artifact for one pinned client implementation. The initial OECD/ETSI converter reconstruction was rejected; its notes remain public. |
| Primary evidence and status | `results/source-manifest.json` pins 17 original files to `f51514d4b999fa7988e05d44b9bf18ea0aa98031`; the harness checks bytes against that Git object. Prior-art and standards manifests retain exact retrieval dates and SHA-256 values. Official OECD/ETSI texts and work-item status were inspected on 2026-10-09. These are background frameworks/specifications, not a legal-compliance test. Evidence cutoff is 2026-10-09T23:59:59Z; review continued October 10. |
| Executed analysis | `code/README.md` provides the executed acquisition, dependency, test and harness commands. `results/execution.json` records the confirmation run after the design freeze. All 32 records passed both original validators; all raw records recovered exactly. Full/raw/named/CERT pair distinctions are 16/16, 16/16, 6/16 and 8/16. Every pair and output is retained in `results/results.json`. |
| Sensitivity and negative results | Node 22.23.3 within the upstream declared range reproduces all result data from Node 24.14.1 except the two runtime metadata fields. Both configurations pass eight tests. Full/raw preservation and preserved uncertainty cases remain prominent. Package-level loss, attachment fidelity, operational harm and recipient conformity were not demonstrated. |
| Separate critical review | `reviews/critical-review.md` and `review-evidence.json` record a separate AI agent's same-host reruns on both runtimes, independent Python count reconstruction, source-meaning checks and scope limits. R1–R3 are resolved in `reviews/author-response.md`; the final cutoff clarification was rechecked. No empirical blocker remains within that review's stated scope. |
| Disclosure and inference | Opening manuscript identifies AI assistance, exact cutoff and complete-study draft state. It disclaims human/practitioner validation, external peer review, exhaustive novelty, legal conclusions and population estimates. Source-guided exploratory selection and the post-diagnostic protocol chronology are explicit. |
| Artifact fidelity | `output/pdf/render-manifest.json` records six-page visual inspection, exact normalized source-text reconciliation, 22 HTTPS link annotations and byte-identical deterministic rerender. Artifact QA was by an AI agent and does not certify scientific quality. |
| Privacy and rights | Release-source scan found no private local account paths, personal email addresses, key markers or credential values. The only sensitive-key-name match is the snapshot utility's rejection list. Scenarios and reserved-domain contacts are synthetic. Third-party full articles, standards, clone, packages and local verification images remain ignored. No reuse licence has been added. |
| File hygiene | Forty text artifacts then present were scanned with no trailing whitespace. The snapshot utility has 17 passed offline tests; those validate bookkeeping, not research claims. Browser uploads target only the newly created public repository. No workflow, paid service, external submission, upstream modification or account-setting change is part of release. |

## Principal immutable hashes

| Artifact | SHA-256 |
| --- | --- |
| `paper.md` | `372f205d7f4a343f701496199f4a8783837dc6dcf953f3283063c983bec08a13` |
| `output/pdf/paper.pdf` | `e87ce93650bacc3f6bb5ee974430d0db3049d74a1c01964522c7c485befb9ae3` |
| `data/fixtures.json` | `6e355a22a4513e167ebe7168c81084647c767bdf1e9048436a9a47ff2d65b79d` |
| `code/run.mjs` | `e1e46d3c8c0cf4a134b3feecc339e086e5c5294552fa5bc0696afbe40b287c30` |
| `results/results.json` | `02dbf4679217e6956d361718f72df6f57011c7b99699e31e7e1c4207f215e999` |

Remote verification must fetch the resulting commit, compare expected blobs against the reviewed local files, and confirm the branch SHA. An upload attempt alone is not publication evidence. Subsequent documentation corrections use new commits and preserve prior history.
