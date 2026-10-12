# Source evidence and mathematical transcription

These are narrow excerpts and researcher transcriptions, not full source snapshots. Original files and separate text extractions are retained in ignored storage. The manifest records their hashes and the exact public retrieval URLs. No full redistribution licence was established for the retained works. All discussion below is paraphrase unless marked as a quotation. Equations use a consistent notation rather than the PDF's typography.

## C1: Galipeau v2, 11 July 2026

The full 16-page PDF was read. PDF page numbers equal the printed numbers. Pages 5–7 contain the audited rule and claims; page 8 contains the example. Pages 2, 4 and 8–10 provide relevant qualifications about pooling, delegation, exchange, unused allocations and strategic demand. Other energy and political claims are outside this audit.

| Locator | Researcher transcription or interpretation | Audit use |
|---|---|---|
| p. 5, Equations 2–3 | `A_i = C w_i D_i / sum_j(w_j D_j)`; all demands and weights positive, weights sum to one | Formula reproduced exactly in offline analysis |
| p. 5, Proposition 1 | Awards are positive for positive capacity and sum to capacity | Preserved; not a claim that awards are demand-bounded |
| p. 6, Propositions 2–3 | Fulfillment equals a common multiplier times the weight; fixed-demand awards scale with capacity and are invariant to common weight scaling | Preserved on the positive-budget domain |
| pp. 6–7, Section 3.3 | Invokes inheritance from the proportional allocation family | Subset consistency distinguished from composition |
| p. 7, Equation 4 | `U_i + (C-U) w_i d_i / sum_j(w_j d_j)`, with `d_i=max(D_i-U_i,0)` and `U=sum_i U_i` | Residual formula; zero-denominator convention checked separately |
| p. 7, Proposition 5 | Simultaneous floor protection and full capacity assignment stated as equivalent to `U<=C` | Requires an additional condition when all residual claims are zero |
| p. 8, Table 1 | Residual claims `(700000,600000,400000,900000,200000)`, weights `(.35,.30,.15,.15,.05)`, budget `1800000` | Positive control; source's rounded awards reproduce |
| p. 8, shock paragraph | Capacity falls from `2400000` to `1800000`, aggregate floor stays `600000`, residual budget falls by one third | Positive control; no individual floor vector supplied or invented |

Two short verbatim excerpts supply the precise contested wording:

- Section 3.3, p. 7: “consistency and composition properties” (4 words).
- Equation 4 convention, p. 7: “second term is zero when residual weighted demand vanishes” (9 words).

Total quoted C1 prose in this extract: 13 words. The manuscript does not add a different verbatim passage. The source motivates aggregate excess demand on pp. 4–5; this makes the zero-residual finding a domain/boundary qualification. The source's own useful worked example does not breach demand bounds. Its reference to exchange prevents an inference that every excess individual award is wasted physical capacity.

## C2: Thomson (2006), Working Paper 530

The retained PDF has 34 pages. Read scope: cover, abstract and introduction; claims definitions and axioms on PDF pp. 8–10; the weighted-proportional discussion and two composition counterexamples on PDF p. 14 (printed p. 10). The complete characterization proof was not audited.

PDF p. 8 defines the claims domain and feasible awards. PDF p. 9 defines weighted proportional awards as `min(lambda*w_i*c_i,c_i)`. This is the cap used here, already present in prior work. PDF pp. 9–10 distinguish reduction of the endowment, staged increases, and departing claimants. PDF p. 14 explicitly states the two composition failures and supplies examples. This precludes a claim that S014 discovers a new general failure theorem.

Short quotation from PDF p. 14, with the line break normalized: “they satisfy neither composition down nor composition up” (8 words).

## C3: Harless, author accepted manuscript

The PDF has 29 pages including a repository cover. The cover identifies the 2017 journal article, states accepted-version status and warns that the publisher text may differ. The manuscript is internally dated 11 February 2016; repository deposit is 30 September 2016.

Read scope: cover, abstract, introduction, the claims domain and allocation axioms in Section 2, and the weighted-rule construction and statement of Proposition 1 in Section 3. The entire proof and publisher version were not checked.

PDF p. 7, printed p. 6, footnote 16, distinguishes unchanged-claim endowment additivity from composition up and down. PDF p. 9, printed p. 8, Section 2.2, defines the award `min(lambda*u(i,c_i),c_i)`. Taking `u(i,c_i)=w_i*c_i` gives the existing capped rule. The present finite examples check the particular rule; they do not establish Harless's full characterization theorem. No verbatim prose is quoted here.

## C0/C4–C6: version and date evidence

C0 is the record metadata captured with the original PDF. C4 is the later observed latest-version endpoint, whose final URL and metadata identify the same record 21305645. Metadata publication date is 2026-07-11. C5 is an author listing which gives July 2026 and directly links record 21305645. C6 lists the same title with August 2026. Its title entry supplies no distinct paper revision in the captured HTML. Those dates are not silently reconciled. The analysis targets the retained v2 PDF only.

## Q1/Q2: programme comparison

Read-only GitHub metadata identifies a pinned revision of `gavenren/ai-safety-research`; its README was read. The four listed reports concern incident counts, test dependence, judge transfer and judge ensembles. None of those index descriptions identifies a compute-allocation paper. This is an index-level comparison, not an exhaustive read of all repository history or files. No file in that repository was changed.
