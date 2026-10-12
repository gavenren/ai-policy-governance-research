# Policy and asset-funding review

Date: 12 October 2026.

Reviewer: a separate AI agent. This agent also collected the asset sources used in this study. This check is not an independent human or external peer review.

## Scope and result

I read the paper, input file, and result summary. I checked the wealth, property, resource, public-ownership and borrowing sections against the official sources recorded in `notes/asset-sources.md`. I also reviewed the proposed order of action and the stated limits of the tax packages.

**Result:** no necessary correction was found within this scope. The paper distinguishes its arithmetic cases from official costings. It does not claim that the current Canadian tax system can collect the target amount.

## Checks completed

- The wealth-tax amount matches the PBO proposal dated 19 April 2025: C$23.042 billion for 2026–27. The paper does not confuse it with the different proposal dated 9 April. It does not treat the amount as collected revenue or add it unchanged to the capital-tax packages.
- The C$19.1 trillion household net-worth figure matches the Statistics Canada release for Q2 2026. The paper treats it as an asset stock. It does not add residential property a second time.
- The historical C$84.417 billion in local property-tax receipts matches Table 42 of the Fiscal Reference Tables 2025. The paper correctly treats it as existing local revenue, not new federal money.
- The resource section assigns no unsupported new royalty amount. It states that corporate and resource tax claims can overlap. It calls for treatment of provincial powers and Indigenous rights and agreements.
- The public-fund section counts the need to acquire assets. It separates asset transfers, cash receipts and annual returns. It requires income after taxes, fees and financing costs. It excludes assets committed to pension claims.
- The borrowing case identifies its fixed real interest rate, new debt only, and interest on opening debt. It does not present borrowing or reserves as permanent annual revenue.
- The action sequence includes joint federal and provincial accounting, measurement of tax bases, collection and payment capacity, and an explicit emergency budget. It does not require people in hardship to prove that AI caused an income loss.
- The paper warns that a cash account can balance while the payment fails to preserve a living standard. It also states that provincial fiscal losses and costs remain outside the model.

## Separate arithmetic checks

I used Python's decimal arithmetic in a separate calculation. I did not call the study model for these checks.

| Check | Recomputed result | Paper result |
| --- | ---: | ---: |
| C$23.042bn wealth-tax estimate / C$1,100.12195433bn target | 2.0945% | About 2.1% |
| Target / C$19,100bn household wealth | 5.7598% | About 5.8% |
| Fund assets at 2% net real withdrawal | C$55.0061trn | C$55.01trn |
| Fund assets at 3% net real withdrawal | C$36.6707trn | C$36.67trn |
| Fund assets at 4% net real withdrawal | C$27.5030trn | C$27.50trn |
| New debt after ten annual gaps, at 3% real interest | C$12.6117trn | C$12.61trn |
| Interest on opening new debt in year ten | C$335.2877bn | C$335.29bn |

The debt check used `closing debt = opening debt × 1.03 + annual gap` for each of ten years. Each value agrees after rounding.

## Limits of this review

This check does not validate legal feasibility, future asset prices, household responses, a safe fund withdrawal rate, or the assumed capital and consumption bases. It is not a complete audit of all sources or the tax model. The absence of a necessary correction does not establish that the proposed tax rates can collect the stated revenue. Official joint costing and household analysis remain necessary.

For easier reading, a future short brief could replace “unlevered fund” with “fund with no debt” and explain “net real withdrawal” as an amount available after costs and inflation. These are optional wording changes, not corrections to the account.
