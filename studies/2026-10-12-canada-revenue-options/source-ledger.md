# Sources and assumptions

Checked on 12 October 2026. Official sources describe observed accounts, existing rules, or dated proposals. None forecasts a Canadian economy with no wages. Live statistical tables can be revised. The inherited fiscal benchmark is kept fixed for comparison.

## Inherited account

The [Canada policy application](../2026-10-12-canada-policy-application/paper.md) and its [results](../2026-10-12-canada-policy-application/results/summary.json) were read at repository commit `f606abcaba65fc9d222fa2b0dc0318bbd20c17e6`. The input file records their hashes.

That case assumes an additional tax-free C$24,000 for all 34,158,557 counted adults, excluded from other benefit tests. It retains existing benefits, expands child support to the stated maximum-coverage case, adds C$15bn in services, and sets benefit administration at 1% of adult cash. It loses 80% of personal income tax and all EI premiums. It requires C$1,100.12195433bn in new annual revenue while keeping the C$71.8bn starting deficit. The full underlying eligibility, population, benefit, and price assumptions remain in that paper. This follow-up does not treat the residual as an official need estimate.

| Primary source | Date and location | Use and limit |
| --- | --- | --- |
| [PBO, Economic and Fiscal Outlook](https://www.pbo-dpb.ca/en/publications/RP-2627-002-S--economic-fiscal-outlook-june-2026--perspectives-economiques-financieres-juin-2026) | 4 June 2026; Table 3, Appendices A, C, D; information to 8 May. | Calendar-2026 GDP C$3,392bn. FY2026-27 company tax C$101.2bn, personal tax C$248.3bn, non-resident tax C$14.3bn, GST C$52.8bn, and baseline deficit C$71.8bn. These are forecasts, not final accounts. The retained personal tax C$49.66bn is 20% of the source amount, an inherited assumption. |
| [CRA, corporation tax rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/corporation-tax-rates.html) | Page dated 30 May 2025; checked live. | General federal rate 15%, small-business rate 9%, with other cases. All receipts cannot be divided by 15% to infer a uniform tax base. Scenario rates are not these statutory rates. |
| [Finance Canada, tax-expenditure report, part 5](https://www.canada.ca/en/department-finance/services/publications/federal-tax-expenditures/2026/part-5.html) | 2026 report, released 26 February; dividend gross-up and credit entry. | Explains coordination of corporate and personal tax on distributed profit. Supports one integrated model rather than addition of independent headline yields. |
| [Finance Canada, tax-expenditure report, part 1](https://www.canada.ca/en/department-finance/services/publications/federal-tax-expenditures/2026/part-1.html) | 2026 report; interpretation of estimates. | Estimates are static, omit behavioural responses, and interact. They cannot be added as a joint repeal yield. |
| [CRA, administered financial statements](https://www.canada.ca/en/revenue-agency/corporate/about-canada-revenue-agency-cra/departmental-performance-reports/2024-25-departmental-results-report/2024-25-financial-statements/cra-fs-administered-activities.html) | 2024-25; page dated 27 October 2025; notes 11 and 14. | Federal GST is net of input credits, rebates, and low-income credits. Provincial HST is separately accounted for. CRA-only figures exclude GST on imported goods collected by CBSA and are not substituted for the PBO federal line. |
| [Excise Tax Act, section 165](https://laws-lois.justice.gc.ca/eng/acts/e-15/section-165.html) | Checked live. | Starting federal GST rate 5%. Proposed 10%, 15%, and 20% rates are scenarios, not law. |

## Dated comparisons

| Primary source | Date and value | Use and limit |
| --- | --- | --- |
| [Statistics Canada, Table 36-10-0124-01](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3610012401); [CSV](https://www150.statcan.gc.ca/n1/tbl/csv/36100124-eng.zip) | Released 28 August 2026. Canada, current prices, unadjusted household final consumption, vector v62700569. 2025 quarters: C$409,636m, 447,771m, 448,267m, 455,561m. Sum C$1,761.235bn. | Dated scale comparison only. The [six-row extract](data/household-consumption-extract.csv) also retains two 2026 quarters, which are not used as an annual forecast. |
| [Statistics Canada, consumption methods](https://www150.statcan.gc.ca/n1/pub/13-017-x/2008001/themes/ch07/5213362-eng.htm) | National accounts methods guide. | Household consumption includes sales taxes and imputed housing services. It is not a tax-exclusive GST base. |
| [PBO, wealth-tax proposal](https://www.pbo-dpb.ca/en/epc-estimates--estimations-cpe/45/EL-45-1023246-P); [PDF](https://distribution-a617274656661637473.pbo-dpb.ca/096751f2078bd924b74f770709a309369a927c981ea10381a76b3a5150456dbf) | 19 April 2025. Estimated FY2026-27 budget improvement C$23.042bn. | Proposal rates: 1% on net wealth C$10m-50m, 2% on C$50m-100m, 3% above C$100m. Excludes lottery wealth. Assumes 35% hidden wealth, administration at 2% of gross receipts, and a 0.15% lottery exemption cost. Uses 2023 household evidence. Not enacted revenue or additive to new capital taxes. |
| [Statistics Canada, national balance sheet release](https://www150.statcan.gc.ca/n1/daily-quotidien/260911/dq260911a-eng.htm) | 11 September 2026; Q2 2026 household net worth about C$19.1trn; residential real estate C$8,523.3bn. | Asset stocks, not annual receipts. Housing is already in net worth. Residential real estate is not a land-only base. Rounded wealth is used only for the 5.8% scale ratio. |
| [Finance Canada, Fiscal Reference Tables 2025](https://www.canada.ca/en/department-finance/services/publications/fiscal-reference-tables/2025/part-7.html) | Page dated 7 November 2025; Table 42. Local property taxes C$84.417bn in reference year 2024. | Existing local receipts, including the stated Aboriginal-government coverage in the source. Not new federal revenue or a 2026 forecast. |

## Institutions and policy design

- [IMF, Broadening the Gains from Generative AI](https://www.imf.org/en/Publications/Staff-Discussion-Notes/Issues/2024/06/11/Broadening-the-Gains-from-Generative-AI-The-Role-of-Fiscal-Policies-549639), 17 June 2024. Supports study of capital-income and excess-profit taxes and social protection. Does not support this paper's chosen Canadian rates or yield.
- [CRA, provincial corporate taxes](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/corporations/provincial-territorial-corporation-tax.html). Provinces and territories set their own provisions. New federal receipts cannot be combined with provincial receipts without a sharing agreement.
- [CRA, cross-border digital supplies](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/digital-economy-gsthst/charge-collect/cross-border.html). Certain foreign suppliers and platforms collect GST/HST on taxable Canadian sales. This is not a right to all global profits.
- [CRA, Income Tax Audit Manual, chapter 15](https://www.canada.ca/en/revenue-agency/services/tax/technical-information/income-tax-audit-manual-domestic-compliance-programs-branch-dcpb-15.html), sections 15.2.10 and 15.6.1. Permanent-establishment and treaty limits require case-specific legal review.
- [CRA, global minimum tax](https://www.canada.ca/en/services/taxes/excise-taxes-duties-and-levies/global-minimum-tax/about.html). Existing qualifying-group rules do not give Canada a 15% claim on all world AI profits. Existing measures cannot be counted again as new revenue.
- [Constitution Act, section 92A](https://laws-lois.justice.gc.ca/eng/const/section-92A.html). Provincial resource powers matter. No claim is made that all federal powers are absent or that this source resolves Indigenous rights.
- [Canada Pension Plan Investment Board Act, section 5](https://laws-lois.justice.gc.ca/eng/acts/C-8.3/section-5.html), and [Retraite Québec, QPP](https://www.retraitequebec.gouv.qc.ca/en/programs/quebec-pension-plan). Pension assets support existing duties and are excluded from new general funding.

## Selected assumptions are not source facts

The [input file](data/inputs.json) specifies GDP multiples, taxable-base shares, tax rates, collection factors, retained GST relief, new rebates, administrative cost, fund withdrawal rates, and borrowing terms. These are chosen assumptions. No source supplies a verified future base or an official yield for these packages.

The C$20bn retained GST relief allowance is separate from collection shortfalls and from the C$100-200bn new rebate. It is not an estimate of current legal entitlements. Its C$40bn stress case shows sensitivity to this uncertainty. Capital rates are average integrated federal charges after credits, before collection losses.

No wealth, land, resource, or public-fund yield is added to the package totals. The contribution of this study is a consistent comparison of new revenue, replaced receipts, relief, and costs. It does not claim a new tax instrument or an optimal policy.
