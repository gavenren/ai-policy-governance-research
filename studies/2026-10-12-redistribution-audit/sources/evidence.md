# Evidence, rights and claim locations

This is a locatable evidence extract, not a full copy of any source. Mathematical expressions below are transcribed facts. Other text is our summary except the one marked quotation. The manifest records each original and extracted representation, byte count, hash, retrieval time and requested/final URL. Original bytes are retained in ignored local storage. Public readers can obtain the pinned originals with `code/acquire_sources.py`; the analysis itself uses only the synthetic design.

The initial evidence cutoff is 2026-10-12T09:54:33Z: the last retrieval among the original texts used for the analysis. Reading, calculations and review occurred later. A current arXiv history check before release is a separate event, not retrospective coverage of the source search.

## A1 — the audited preprint, version 1

Jakub Growiec, Klaus Prettner and Maciej Szkróbka, *Redistributive Policies for the Times of Transformative AI*, arXiv:2609.14750v1. Submitted 13 September 2026 at 19:32:23 UTC. The PDF cover separately states 15 September 2026; the cover date is not the arXiv submission date. English research preprint. The [pinned abstract](https://arxiv.org/abs/2609.14750v1), [HTML](https://arxiv.org/html/2609.14750v1), [PDF](https://arxiv.org/pdf/2609.14750v1) and [source archive](https://arxiv.org/src/2609.14750v1) identify the version. The archive's internal `ubi_v2.tex` filename does not establish arXiv version 2.

The root reader compared the relevant HTML, PDF text and TeX. The feasibility reviewer also compared these equations with the TeX. No visual PDF equation inspection is claimed; the text and original TeX resolve the audited symbols. The PDF contains 25 pages. Page locators below refer to the PDF viewer pages, which coincide with the paper's numbered pages for the cited sections.

| Locator | Narrow source content | Use and limit |
|---|---|---|
| Sections 2.1–2.2.1, pp. 4–5, equations 2–5 | Nested CES: Y=[αK^θ+(1−α)S^θ]^(1/θ), S=[βH^ω+(1−β)AI^ω]^(1/ω); θ<0. Equation 4 gives lnY=πK lnK+πH lnH+πAI lnAI. Equation 5 gives the three marginal elasticities. | Check the proposed exact log identity against the paper's own example function. The calculus critique concerns that identity, not a claim that CES models are unusable. |
| Section 2.2, pp. 5–6, equations 6 and 9 | The tilde variable is x divided by its cross-sectional mean. | Identifies the mean-normalized measure. Later informal language about de-meaning does not change the explicit ratio. |
| Section 2.2.2, pp. 6–7, equations 8–10 | Income is a sum of net factor-income components and a lump-sum transfer. The variance decomposition has covariance terms and mean disposable income squared in the denominator. | Positive control. The denominator must change with an added transfer. |
| Sections 2.3–2.5, pp. 7–10, especially p. 9, equation 15 | The model leaves preferences and market structures underspecified. The full-automation scenario gives πK→1,πH→0,πAI→0 and cites Growiec's growth model. | We test the relative-input condition; the input paths are not claimed to solve an equilibrium. The cited model supports the condition. |
| Section 3.1, p. 11, paragraph headed UBI and Inequality | Exact six-word quotation: “UBI alone is neutral for inequality”. The following mathematical object is σ²(normalized income). | This conflicts with an equal addition when the measure uses the new mean. Raw variance is unchanged. |
| Section 3.1, pp. 11–12, equation 17 | The aggregate transfer is indexed as T=u Inc and the aggregate budget is rearranged by division by 1−u. | The aggregate rewrite does not identify the household distribution. The comment distinguishes equal and proportional allocations with the same total. |
| Section 3.6, p. 18, equations 22–24 | Consumption C=(1−s)Inc, a common consumption tax and an equal UBI rebate. The budget divisor is s+(1−s)(1+τC). | Positive finding. Full equal rebates and a common saving rate support the claimed relative-variance reduction. Heterogeneous saving is outside this assumption. |

Rights: the arXiv record links a Creative Commons Attribution 4.0 licence. This audit gives full attribution and version links. It publishes only the six-word quote, selected mathematical facts and original analysis. It does not republish author correspondence, incidental TeX comments or full source files. The CC licence of the source does not set a licence for our original work.

## M1 — established measurement distinctions

Frank A. Cowell, *Inequality and poverty measures*, author-submitted chapter, revised December 2014; book citation 2016; LSE deposit available April 2016. [Repository record](https://researchonline.lse.ac.uk/id/eprint/66022/). The capture is the author manuscript, not a verified copy of the final published chapter.

Read locations: sections 3.1.1–3.1.3, manuscript pp. 18–22, PDF pp. 20–24. Equation 3 sets out generalized entropy indices. At parameter 2, the index is one half of squared coefficient of variation. Equation 4 gives the relative Gini with the mean in its denominator. Equation 6 is population variance, and equation 8 is the absolute Gini without that mean denominator. Section 3.1.3 distinguishes invariance of rankings from independence of an index's value under scale or equal-addition changes. The present paper defines its index values directly; it does not attribute a new distinction to this audit.

Rights: the cover states copyright and moral rights remain with the authors or owners. It allows private study or noncommercial research downloads and prohibits further distribution of the material. We retain the PDF privately and publish only bibliographic facts, locators, mathematical definitions and this original summary. No full chapter, page image, contact information or passage is republished.

## G1 — the supporting growth model

Jakub Growiec, *What will drive global economic growth in the digital age?*, DOI [10.1515/snde-2021-0079](https://doi.org/10.1515/snde-2021-0079). The author-hosted copy states online publication 24 June 2022, acceptance 3 June 2022 and receipt 12 August 2021. It is cited as a 2023 journal article in A1. [Author-hosted PDF](https://e-web.sgh.waw.pl/jg23234/Growiec%20SNDE.pdf).

Read locations: section 2.4 and section 3; the key full-automation case is PDF p. 10, equations 15–17. Physical input is asymptotically proportional to K. Cognitive input is asymptotically proportional to A K, with K→∞ and A→∞, holding the positive proportional factors fixed. This makes cognitive input unbounded relative to physical input and supports the capital-share limit discussed in the comment. The source discusses other automation cases too; this audit does not assess them all or reproduce its full dynamic model.

Rights: no permission to republish the full author-hosted publisher copy was established. Only bibliographic facts, the mathematical condition and an original narrow summary are public here. Full bytes and the derived extraction remain in ignored storage. We did not reproduce the author's address or email.

## V1 — version status

The unpinned [arXiv abstract](https://arxiv.org/abs/2609.14750) captured at 2026-10-12T09:45:42Z listed only version 1 in its submission history. This establishes the observed arXiv history at retrieval, not the absence of every other manuscript or correction. The pinned paper remains the unit of this audit even if a later version appears. See the version recheck record for release-time status.

## Inspectability and limits

Each central mathematical claim can be inspected through a source locator, a short public transcription, the pinned PDF or original TeX, and the complete synthetic analysis. Raw source hashes confirm which bytes were retained; they do not prove a substantive claim by themselves. HTML and PDF extraction can alter spacing and equation layout. For the disputed equations the TeX provides an additional representation. No OCR was used. The copyright restrictions of M1 and unverified full-copy rights of G1 are the reason this repository contains narrow evidence summaries rather than full source files.
