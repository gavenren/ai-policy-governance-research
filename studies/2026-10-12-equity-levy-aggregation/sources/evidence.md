# Narrow evidence extract

This file contains one short quotation and source-linked paraphrases. It is not a full source snapshot. It makes no claim that the underlying filings, valuations, or policy have been independently validated. Source IDs, exact bytes, dates, rights and read scope are in the manifests.

## P1: explicit group-model scope

Locator: essay section *From market access to a global club*, footnote *Assumptions behind Figure 3*, followed by the Figure 3 caption. The retained text places these at lines 154–167.

The footnote says: **“The cap is applied to each group's sales pattern.”** This is a nine-word quotation. The caption likewise describes a regional illustration using constructed group patterns. This supports treating S015 as an information-limit extension. It does not support an accusation that the author hid the level of aggregation.

## V4–V7: the rule and what its inputs mean

| Claim | Exact source locator | Source content, paraphrased |
|---|---|---|
| The cap is applied by listed-market group | V4, `collection_matrix`, lines 32–49; `bucket_ledger`, lines 52–75 | The code first sums member sales within each row. It uses the lesser of the cap multiple and the reciprocal of that sum to allocate receipts. Zero member sales give zero receipts. |
| Country receipts and group collections conserve the same charge | V4, lines 78–94 and `checks()` | Member receipts sum columns of the allocation matrix. The source includes conservation, no-overcharge, and membership checks. This extract records the checks present in the code; it does not claim they have been executed here. |
| Six broad groups are constructed profiles | V4, lines 126–139; V5, Scope and limitations; V6, Sales-destination matrix | The rows use published revenue anchors plus judgment. The source states that the Japan/Korea/Taiwan and rest-of-world rows require particularly large judgments. |
| Equity values are rounded in the executable model | V4, line 118; V6, Covered market values | The code uses `[62.19,11.06,4.40,10.12,16.31,22.63]` trillion dollars. The documentation gives more precise values and a world anchor of 126.693 trillion. The study should preserve the executable inputs. |
| Coverage differs from the full proposal | V5, Scope and limitations; V6, Covered market values | Total listed value approximates the proposed covered base. Private firms and the size-threshold phase-in are absent. Evidence about small-firm coverage is more limited outside the United States. |
| The two universes are separate | V4, lines 141–155; V6, Magnificent Seven calculation | The broad base and the Magnificent Seven use different valuation dates and overlap. They must not be added. The latter is a constructed basket profile, not seven separately modeled firms. |
| Revenue and equity weights differ | V7, Magnificent Seven, paragraph after the geographic-revenue table | The initial blend uses six firms' combined revenue and revenue weights, followed by geographic adjustments and a Tesla-related change. The final vector is not a demonstrated equity-value-weighted mean. |
| Destination measurement is imperfect | V7, Sales destinations and Magnificent Seven | Disclosures mix customer location, billing location, headquarters, broad regions and intermediary sales. Splits among the six model regions require judgment. |
| Collection is not investor burden | V8, opening paragraphs, US ledger and Limits of the ownership data | This separate source note distinguishes destination-based collections from investor-residence exposure. It describes approximate ownership evidence with mismatched definitions and dates. S015 does not validate that burden calculation. |

**Researcher condition, not a source fact:** To derive bounds over unknown firm profiles using the fixed rows, S015 must assume that each row is the mean under the weights used for the levy base. For a common rate on equity, these are equity-value weights. The bounds do not become empirical limits merely because some row anchors use revenue data.

## F1: aggregation is an established concern

Loretz's May 2025 report, Sections 3.2.3–3.2.4 on PDF pages 28–32, compares aggregate and hybrid data approaches. The conclusion on PDF pages 56–57 states that country-pair aggregation can limit firm-level analysis and bias estimates. Sales by destination also require approximation. Thus S015 should not claim to discover aggregation bias. The inspected work concerns profit-tax apportionment and loss consolidation, rather than this capped equity-levy allocation. No prose is quoted.

## H1: factors need not track the tax base

Hines's July 2009 NBER working paper, introduction on PDF pages 3–5 and Section 3 on pages 8–11, studies how formula factors can misattribute profits and change merger incentives. This is prior work on the economic importance of the unit and weighting of apportionment. It is not evidence that the proposed levy has the same behavioral effects. The 2010 journal version was not the text read here. No prose is quoted.

## M1: tight moment bounds are established methods

Bertsimas and Popescu (2005), PDF pages 1–5, define tight bounds over distributions with given moments and formulate an optimization over those distributions. Definitions 1.1–1.2 and Equation 2.1 are the relevant locators. S015's elementary construction is an application of that general type of reasoning, not a new general method. Later proofs were not audited. No prose is quoted.

## Dates and scope

P1 prints 16 July 2026 as its publication date. The dated G1 capture identifies the same repository commit as the retained source checkout. F1 gives May 2025 without an exact day. H1 gives July 2009. M1's first-page footnote gives electronic publication on 8 April 2005. These are publication records, not legal effective dates. This package supports no claim about enacted tax law, investment returns, actual levy receipts, or a stable political agreement.
