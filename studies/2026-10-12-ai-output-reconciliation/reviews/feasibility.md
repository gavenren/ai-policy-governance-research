# Candidate screen: public ownership, delegated payments, and AI output measures

**State: Working notes. Independent feasibility record, migrated to S016. This is not the required critical review of S016 results.**

**Evidence cutoff:** 2026-10-12T18:08:07Z. Further static interpretation and source-metadata checks continued before handoff; their migration and fresh-check times are recorded separately. This is a feasibility screen. It had no study number at the original cutoff; it is now preserved as the prior record for S016. No new model, outcome estimate, or numerical replication was run. The algebra below and the code inspection preceded any prospective plan. They must be disclosed as exploratory work in a later study.

## 1. Purpose and selection

This programme studies economic governance under a condition in which people cannot earn competitive wages. It does not predict that this condition will occur. Before adding another paper, this screen asks whether public evidence permits a distinct and useful test. A further synthetic parameter grid is not enough.

The local programme already covers income floors, public funds, benefit delivery, public control, household debt, supplier continuity, and compute allocation. It also has screens on credit, creditor protection, benefit interactions, entry to citizen trusts, payment agents, tax exposure, shared asset sales, and transition hedging. Opening sections of these notes and the relevant parts of the programme gap screen were checked. This was not a new full review of every paper in the repository. The parent agent is developing group-to-firm equity-levy work; another agent is screening monetary policy. Those questions were excluded from this search.

The initial search considered public ownership and competition, delegated consumer payments, and service access after supplier failure. It stopped these paths early when close work or a weak data design became clear. The parent then proposed a more precise question about the training-output measures in Korinek and McKelvey's *Measuring the AI Economy*. The rest of the screen checks that proposal independently.

## 2. Broad candidates not selected

### Public ownership and competition

The local programme gap screen already identifies the public-common-shareholder question. A further close source is John DeVadoss, *Public AI Wealth Funds and the Economics of Shared Ownership*, SSRN 7494040, posted on 22 September 2026. The public abstract covers competition, ownership, and distribution. The full text was not obtained: the direct SSRN request returned 403. This is a reason to withhold a novelty claim, not evidence about the paper's full results.

Murakami's *Automated Public Capitalism*, SSRN 6620040, is another close lead. Search metadata gives a 21 April 2026 manuscript date and a 24 April posting date. Only the public abstract was available in this screen. The direct page returned 403. No claim about the full 48-page argument is made. The parent also has no retained full text. A new ownership model should wait for a full comparison with this work or use a question that does not depend on its absence.

### Delegated payments

Jiang and co-authors' *A Formal Analysis of Agent Payment Protocols*, arXiv 2609.00060, is close to a proposed question about spending limits for AI payment agents. The first four pages and the current AP2 specification page were read through the web reader. This was enough to identify close work on payment authority and protocol composition. It was not a full protocol audit. No new test corpus or distinct welfare question was fixed. This path was stopped.

### Other leads

Searches on supplier insolvency and model escrow found contract material but did not establish an empirical corpus or an unresolved mechanism. The search on personalised prices and basic income did not identify a design that could separate a transfer effect from existing price-discrimination mechanisms. These were discovery passes only. They are not systematic reviews and do not establish that useful work is impossible.

## 3. The selected feasibility question

Can the training-output quantity shown in an AI production table be reconciled with the training component used in the same paper's AI GDP calculation?

This is useful for governance because a statistic used to assess the growth of AI production must have a clear meaning. It cannot, by itself, show the tax base available to replace wages. The proposed audit concerns the internal interpretation of one accounting measure. It would not estimate the date of full work displacement, taxable AI rents, or the cost of a future income guarantee.

Korinek and McKelvey define an AI production boundary, estimate physical compute and its imputed rental value, and distinguish training from inference. Training supports model-capital formation. Their main paper reports separate nominal and physical series and a quality-adjusted training quantity. It then builds AI GDP from output and imported inputs. The paper states important limits about data, quality adjustment, and economic interpretation. These limits are acknowledged, not claimed as new findings here. [B1]

In the appendix, Section 6.6 adjusts physical compute growth for algorithmic progress. Section 7.5 uses that same algorithmic factor as the price ratio for nominal training spending in the GDP index. Section 8.2 describes the production and GDP measures as related. This makes reconciliation a concrete question. It does not by itself prove that both measures were intended to have the same quantity definition. [B2; P2]

## 4. What the source code establishes

The publisher links a public replication ZIP. It was retained and read, but not run. Its `results.py` contains two paths:

- `print_quality_adjusted_indices` divides physical-compute growth by the algorithmic factor for training.
- `calculate_ai_gdp` constructs nominal training spending from total spending and the training share. It uses the algorithmic factor as the training price ratio in the Fisher calculation.

The second function does not receive the physical-compute series. The call in `main.py` confirms this separation. The package therefore implements the difference found in the text; it is not only a typesetting issue. This establishes two calculation rules, not the correct economic interpretation of either rule. [C1]

The package README uses an older paper title. The main paper captured by the parent is the Bank of Canada June version. The publisher appendix has a May cover date. The publisher and author-hosted appendices have different byte hashes. The formulas and tables relevant to this question agree in the sections read. A later study must freeze these sources separately and test reproduction before it attributes all results to one version.

The full archive member list has no licence file. A text search of its Python, text, and Markdown members found no licence or redistribution grant. Public access is not a grant to publish the package. All third-party code remains private.

A separate source-code check found a further reason to test baseline reproduction first. The monthly-power function uses the first two annual inputs to set one growth rate. It warns if later inputs differ, then extends that rate. The main script supplies three annual totals. The later study should check generated annual sums against supplied totals. No sums or outcome effects were calculated in this screen. This issue must remain separate from the training-quantity comparison.

## 5. The conditional accounting test

Consider a training service that is produced with changing chip technology. Its total rental cost can grow more slowly than the number of physical operations it supplies. Improved training methods can add a further gain. A quantity based on physical operations includes the chip gain before it applies the algorithmic gain. A quantity based on spending includes the chip gain only if its price index removes the corresponding change in cost per physical unit.

Let \(S_t\) be nominal training spending and \(Q_t\) be physical training compute. Let \(a_t\) be the period-to-period factor used to represent algorithmic improvement, with a smaller factor meaning a larger improvement. If the intended quality-adjusted quantity has growth ratio

\[
g^E_t=\frac{Q_t/Q_{t-1}}{a_t},
\]

then the price ratio consistent with that quantity and the given nominal value is

\[
\pi^E_t=a_t\frac{S_t/S_{t-1}}{Q_t/Q_{t-1}}.
\]

Using \(a_t\) alone as the price ratio instead gives quantity growth \((S_t/S_{t-1})/a_t\). These quantities coincide when nominal spending and physical compute have the same growth ratio. This is the usual price-times-quantity identity. It is not a new theorem. For a constant training share, the bridge can use the total series; changing shares require explicit allocation of both nominal and physical compute.

The question remains conditional. The source holds rental prices fixed within each GPU type. Its spending series can therefore also be read as a fixed-price measure of heterogeneous rental services. Those service weights need not be proportional to H100-equivalent operations. Both quantities can be legitimate. The difference can reflect a choice of weights, not a missed price change. This favorable interpretation follows from the main paper's rental-price assumption and the appendix's compute construction. [B1, footnote 2; P2, Sections 4.1 and 9.2]

A rental-service volume and an effective-compute measure can thus be different objects. Under that interpretation, the useful output is a clear statement of each object and its bridge. The implied price above is required if the physical-compute quantity is selected; it is not an automatic correction to a rental-service quantity. If both tables intend the same quantity, the bridge supplies an internal-consistency test. No later table note in the sections read explicitly states this difference in the training quantity. That absence is a limited textual finding, not proof of the authors' intent. The proposed study must allow either outcome.

## 6. Nearest work and the bounded gap

Schreyer and Zinni's OECD paper explains the standard R&D accounting issue. Without market output data, nominal own-account R&D is often measured from costs. A further assumption is needed to split value into price and volume. An input-volume method imposes zero measured productivity growth; an independent volume measure can relax that restriction. This means that an algorithmic adjustment must be tied to a stated output concept. It also means that a cost-based convention cannot be rejected merely because it differs from a physical measure. Annex A was read closely; this screen does not claim a new solution to R&D measurement. [O1]

Peter Bell's eight-page sensitivity audit was read in full. It varies the inference and training factors and the inference/training split. It does not fully rebuild the raw inference index and does not present full uncertainty propagation. Its text does not test the nominal-value/physical-compute bridge above. At the original cutoff, its replication ZIP was not downloaded or checked. The later check below narrows that access limit. [Z1; Z1C]

Bell's earlier eight-page review was also read in full. It proposes sensitivity bands and separates capacity, realised production, welfare, and tax receipts. Those are already established cautions for this source. Repeating them, or adding an arbitrary parameter grid, would not support another paper. [Z3]

The Zenodo API's latest-version link from the sensitivity note points to a July paper with a different title, *Beyond Task Exposure*. Its metadata, opening sections, and the selected accounting passage were read. It separates production, GDP, welfare, and fiscal effects. The whole 39-page paper was not read. The version link must not be treated as proof that this is a revised edition of the eight-page audit with the same scope. [Z2]

Within this bounded search, the exact training-price bridge is a distinct test. This is not proof that no earlier source has made it. The gap is narrow enough to check with a frozen public package and standard accounting identities.

## 7. Recommended design before any result run

This was the proposed design at feasibility stage. The parent subsequently fixed the S016 plan in `../protocol.md`; that protocol controls the analysis. The screen proposed these steps:

1. Freeze the main paper, both appendix captures, the original ZIP, and the closest Bell audit. Check the audit package before asserting a code-level novelty gap.
2. State the training quantity, nominal value, allocation rule, unit, and accounting boundary for each table and function.
3. Reproduce the published baseline from the unchanged package. Check generated annual power sums against the supplied annual totals. Keep any version differences and failed reproduction visible. Isolate the power issue from the quantity convention.
4. Rebuild the relevant calculations in separate code. Check the nominal values and both component price/quantity identities before aggregate comparisons.
5. Keep the published method as one arm. Compare a physical-effective-compute arm with its implied price bridge, and a fixed-price rental-service arm with its quantity stated plainly. Explain why the weights differ. Do not select a preferred arm from its numerical result.
6. Keep nominal flows, inference treatment, training allocation, imported-input treatment, and source assumptions fixed for the main comparison. Do not add a broad parameter grid.
7. Compare component quantities and the signed Fisher aggregate. Verify that the required positive denominators hold. A numerical aggregate must not conceal a failed component identity.
8. Use negative tests: equal nominal and physical growth should close the bridge; a pure change in the unit of physical compute should not change the index; changing the compute price should affect the appropriate price/volume split.
9. Report all differences as accounting consequences under stated concepts. Do not call either arm a validated measure of welfare, revenues, or the income available to people after work displacement.
10. Obtain a separate critical review of the frozen analysis. Stop or reduce the output to a clarification note if the version check resolves the difference, a close audit already covers it, or no material interpretation remains.

This design can yield a useful null result: the two measures could be intentionally different and fully documented. It can also yield a reproducible consistency finding. Either is more defensible than assuming an error from the different formulas.

## 8. Evidence and reproduction limits

`../sources/manifest.json` records full captures, dates, read scope, rights, and hashes. `../evidence/shortquotes.csv` contains short supporting quotations. Original PDFs, web responses, the ZIP, and selected code files remain in ignored `.local-sources/`. No third-party paper or code file is published in this folder.

`../logs/source-searches.json` records the actual web calls and their clock readings. Search outputs are discovery records; snippets do not support substantive claims. `../logs/source-acquisitions.json` records retained sources and the parent agent's earlier B1/B2 captures. `../code/source_check.py` checks retained bytes and short quotations. This is an evidence check, not an analysis replication.

The PDF extractor emitted font warnings during the first three-source capture. The selected passages were readable. This screen does not claim a complete visual review of every PDF page. No contact was made with authors, and no paid source was used. No Git action or central index edit was made by this agent.

## Later closest-package check

Z1C was retrieved on 12 October 2026 at 18:15:59–18:16:02 UTC, after the protocol. Its 11-member package contains no script or notebook. The full README, metadata, two supporting CSVs and interpretation note were read. The parameter register has no physical/rental quantity bridge or annual-power-rule case. Its PDF matches the already-read Z1 bytes. Unpublished calculation code remains unknown. No package code was executed.
