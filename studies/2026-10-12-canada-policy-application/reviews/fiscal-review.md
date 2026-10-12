# Independent fiscal arithmetic review

Date: 12 October 2026.

Status: Arithmetic checked. Policy feasibility is not established. This is a separate AI review, not human peer review. The reviewer also gathered fiscal sources for this study. The calculations below were done separately from the model code.

## Method and result

I read the input file, calculation code, and result tables. I then used decimal arithmetic to reconstruct all 25 transition rows and all 27 full-loss rows. I did not import or run the model functions for that comparison. The independent results matched the result files within C$0.00000001 billion.

| Check | Result |
| --- | --- |
| Central annual funding | Corporate surcharge 16.192 + GST increment 9.504 − extra rebate 3 = **22.696 billion**. |
| First-year financing | Primary spending 8 + reserve addition 12 − half-year resources 11.348 = 8.652 billion. Interest 0.17304 raises borrowing to **8.82504 billion**. |
| Central five-year debt | Closing gross programme debt is **2.562259941 billion**. The cash reserve remains 12 billion. Net debt falls by **9.437740059 billion** relative to the unchanged baseline. |
| Fiscal and cash accounts | Each year's borrowing equals its deficit change plus its reserve addition. Capital grants are expenses. The reserve purchase is a financial asset, not programme expense. |
| Adverse cases | Fifth-year gross debt is 26.6975 billion with lower receipts; 52.8709 billion with twice the recipients; 3.3245 billion with higher interest; and 81.6781 billion in the combined case. |
| Full-loss adult payment | 34,158,557 adults × C$24,000 = **819.805368 billion** each year. |
| Child benefit allowance | Age counts × stated maximum rates = **55.47853265 billion**. Subtracting the 30.9 billion baseline gives **24.57853265 billion** extra. |
| Full-loss extra spending | Adult payment + extra child benefit + services 15 + administration 8.19805368 = **867.58195433 billion**. |
| Revenue loss | Assumed PIT loss: 248.3 × 80% = 198.64 billion. Assumed EI premium loss: 33.9 billion. Total: **232.54 billion**. |
| Required new receipts | To keep the old deficit: **1,100.12195433 billion**. To remove the old 71.8 billion deficit as well: **1,171.92195433 billion**. |
| Whole federal account | Expenses 1,467.68195433 minus remaining baseline revenue 295.76 equals 1,171.92195433 billion before new funding. |
| GDP scale and buffer | The first revenue requirement equals **32.4328%** of the 3,392 billion GDP reference. Two months of adult payments equal **136.634228 billion**. Neither number establishes feasibility. |

## Scope limits and required wording

- The PBO fiscal figures are forecasts for FY2026–27. GDP is a calendar-2026 figure. The constructed multi-year cases hold the reference bases constant. They are not macroeconomic forecasts for the stated years.
- The tax surcharge and receipt discounts are author assumptions. The GST calculation scales existing net receipts. It does not measure the gross taxable base. Existing credits are already reflected in the reference receipts; the new rebate is additional.
- A surcharge on existing corporate liabilities reaches more than large AI firms. The legal base and effects on small firms would need a separate design. It is not the same as adding 20 percentage points to the corporate tax rate.
- Real interest is charged for a full year on opening programme debt and a positive current primary financing gap. This timing assumption is conservative within the annual model. It does not prove sufficient cash on every payment date. The reserve earns zero real return in the case.
- The central case improves the budget relative to its baseline. It does not show that the whole federal budget is balanced. The opening baseline already has a deficit.
- The full-loss case is a separate accounting exercise. Its required receipts are an unfunded residual, not a forecast of achievable tax income. The transition payment and reserve must not be added again unless the scenario is explicitly changed.
- The 80% PIT loss is assumed. Personal income tax also applies to non-work income. The case holds other revenue fixed and does not model provincial tax losses, pension funding, market prices, investment, or tax avoidance under full displacement.
- The child benefit case assumes maximum payments for all counted children. This is a cost allowance, not an estimate of current legal eligibility. The adult payment preserves existing benefits and assumes no tax recovery. Those choices make this an additional-payment case.
- Public asset purchases and an international dividend have no proven yield in this model. Borrowing and cash reserves cannot close a permanent annual gap.

The paper should retain these limits beside the relevant results. A separate human fiscal review and a joint federal-provincial costing remain necessary before policy adoption.

## Final manuscript check

I read `paper.md` after the arithmetic check. Its displayed baseline, programme costs, tax figures, five-year cash table, stress table, and severe-case figures agree with the checked calculations after rounding. The C$18,000 and C$30,000 payment examples also agree. The nine-month reserve comparison is correct for its stated C$16 billion recurring budget. The text keeps the reserve separate from annual expense and identifies the small-business effect of the corporate surcharge.

The manuscript states the fixed-price normalization, fiscal scope, omitted provincial losses, benefit-preservation assumptions, and tax-yield limits. It does not present the C$1.10 trillion residual as secured revenue. It does not count the transition tax package again in the severe case. There is no unresolved arithmetic error or material fiscal presentation error in the reviewed draft.

One wording improvement is recommended in section 3: replace “this programme's current account has a surplus” with “this programme improves the budget balance before the reserve addition.” The table includes capital grants as federal expenses, so “current account” can suggest an accounting distinction the model does not apply.

This pass covers the fiscal text and calculations. It does not validate the service-delivery sources, legal feasibility, tax incidence, construction output, or adequacy of the proposed support.

## Resolution check

The section 3 wording now refers to an improvement in the budget balance before the reserve addition. This resolves the wording issue. The revised paper also states that transition income support is tax-free and does not reduce existing benefits. It identifies the need for legislation and agreements. Planning before April 2027 is assumed to use existing departmental budgets, with any extra appropriation added separately.

I checked the new scope flags in the inputs and code. The transition and full-loss result files have unchanged SHA-256 hashes (`fe4b3121771d1d3dd99d59ea7a23435ec9459b44e81e762b597359c776beae2a` and `779f863364552385d6dd293fd08aaf6bb232d0f01de9362b0bee79b1fb77718f`). The independent arithmetic review therefore still applies. No fiscal correction remains open from this review.
