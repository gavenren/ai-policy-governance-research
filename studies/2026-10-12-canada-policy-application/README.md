# Canada: costs, funding, and timeline

Read the [policy paper](paper.md). It applies the repository's combined policy plan to Canada. For a short version, use the [one-page brief](policy-brief.md) or its [print-ready PDF](output/pdf/canada-policy-brief.pdf). The [brief checks](brief-verification.md) record its content and page checks.

The central limited programme costs $21bn a year before interest and a separate GST rebate. The proposed tax package supplies $22.696bn after that rebate under selected assumptions. A separate severe case finds that an additional $24,000 annual payment to all counted adults costs $819.805bn in cash alone. With the stated additions and tax losses, it needs $1,100.122bn in new annual revenue to keep the starting federal deficit unchanged.

These are conditional calculations. They are not official costings, measured tax yields, a finding of benefit adequacy, or an AI forecast.

- [Sources, dates, and limits](source-ledger.md)
- [Inputs: official values and selected assumptions](data/inputs.json)
- [Population extract](data/population-extract.csv) and [historical provincial tax extract](data/pt-income-tax-2024.csv)
- [Calculation code](code/analyze.py)
- [Funding cases](results/funding.csv), [five-year cases](results/transition.csv), [severe cases](results/full_loss.csv), and [summary](results/summary.json)
- [Verification](verification.md) and [separate AI reviews](reviews/)

## Reproduce

From this folder, run:

```sh
python3 code/analyze.py
```

Python 3 and its standard library are sufficient. The script writes three funding cases, 25 transition-year rows, and 27 severe-case rows. The checks reconcile cash, debt, spending, revenue, and population totals. The funding and severe cases are separate scenarios; they are not added together.

Future-year figures hold population and real tax bases fixed. The nominal FY2026–27 fiscal baseline serves as an approximate 2026-price benchmark. The model does not forecast inflation, tax behaviour, household eligibility, service capacity, or provincial finances. Reviews by other AI agents are not human or external peer review.
