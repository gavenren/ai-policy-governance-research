# Search and source record

Recorded on 11 October 2026. Search window: this task, ending at the evidence cutoff `2026-10-11T20:43:27Z`. Exact per-query request timestamps were not retained. The acquisition timestamps in `sources/manifest.json` are exact download times, not search times. This distinction limits reconstruction of search order.

## Method

The lead agent used the web search tool and direct public-source reads. A separate AI agent made a bounded search for close prior work. Include original economic research and official research summaries. Exclude social posts, press claims of universal job loss, and sources dated after the cutoff. Prefer the latest inspected version of a preprint. Follow references from close works to background research. Do not treat a search snippet as evidence for a central claim.

These exact queries were submitted by the lead agent. No publication-date filter was set:

1. `site.nber.org AI automation capital ownership singularity economics work redistribution 2025 2026`
2. `site.imf.org generative AI fiscal policies 2024 2025 social protection capital taxation`
3. `site.nber.org "Artificial Intelligence and Its Implications for Income Distribution"`
4. `site.ilo.org "Generative AI and Jobs" "2025" refined global index`
5. `site.nber.org "universal" "Alaska" "Jones" "Marinescu"`

The delegated search supplied the 2026 Song, Nayebi, Growiec et al., and Korinek–Lockwood leads. Its exact query strings were not retained here. The lead agent then opened the retained sources. The source ledger states which full texts, sections, abstracts, and official summaries were read. This is not an exhaustive or systematic review.

## Screening and changes

| Candidate | Decision and reason |
| --- | --- |
| Song, arXiv 2609.13801v1 | Retain S1. Closest access and scarce-asset model. Narrow the contribution accordingly. |
| Nayebi, arXiv 2505.18687v4 | Retain S2. Use the revised title and version, not the earlier title returned in some search results. Closest public-capture threshold. |
| Korinek and Lockwood, January 2026 Brookings PDF | Retain S3. Inspect fixed-factor and public-equity sections. Cite the inspected version. |
| Wossnig, arXiv 2606.20649v1 | Retain S4. Model and limits inform the international boundary. |
| IMF 2024 fiscal note | Retain S5 only for claims supported by the official summary. Do not claim a full-note review. |
| ILO Working Paper 140 | Retain S6 only for the exposure-versus-job-loss distinction from its official summary. |
| Korinek and Juelfs, NBER 30172 | Retain S7 as abstract-level background. |
| Growiec et al., arXiv 2609.14750v1 | Retain S8 as abstract-level background. Do not claim a full-method comparison. |
| Korinek and Stiglitz, NBER 34994 and 24174 | Useful discovery leads. Direct web reads returned 403. Do not use for a manuscript finding or claim full-text inspection. |
| Alaska Permanent Fund research | Exclude from the manuscript. A present-day transfer experiment is not evidence of a fully automated economy. |
| Social-media results | Exclude from evidence. |

The reference list in Song's paper also led to existing automation, income-distribution, and land-rent research. This study does not claim full-text review of those referenced works.

## Acquisition

The repository snapshot utility attempted the six initial URLs at about `2026-10-11T20:38:48Z`. Each failed with `URLError`; no successful snapshot was recorded by that tool. A curl download of the same public sources, plus S7 and S8, then succeeded with HTTP 200 and TLS verification enabled. There was no authentication or change to account settings. The exact cause of the first transport failure was not established.

The source manifest gives requested and final URLs, version, publication date, download time, original byte count and hash, and public-extract hash. The original files remain in the ignored local source directory. HTML text was extracted with Python's standard `HTMLParser` and whitespace normalization. Each published HTML quote was matched against that text. The S3 quote was checked in the web tool's PDF extraction. No OCR was used. Full originals are not included in the GitHub release.

## Duplicate scope

The policy repository was cloned at `9be88c60eb8c57d75a4bfb372a96fa089b1d08e5`. Its existing paper concerns FLARE-AI record preservation. The separate public `gavenren/ai-safety-research` README was read at the cutoff; it lists incident counts, test dependence, and judge correction. Those topics do not duplicate this economic model. No file in that separate repository was changed.

## Legal status

No source is used to assert an applicable legal duty. The instruments proposed in the paper are research proposals. Adoption, entry into force, and applicability dates are not applicable. Research publication dates must not be read as legal dates.
