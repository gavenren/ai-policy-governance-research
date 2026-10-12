# Canada revenue options after wages

Read the [plain-English analysis](paper.md). It asks how Canada could meet the earlier study's C$1.10 trillion annual new-revenue target.

The paper compares capital-income taxes, consumption taxes and rebates, wealth and land taxes, resource income, public ownership, and temporary borrowing. Two example tax packages cover the target only under demanding assumptions about economic size, tax bases, and collection. Neither is an official costing or a finding of practical feasibility.

- [Sources and dates](source-ledger.md)
- [Inputs and assumptions](data/inputs.json)
- [Calculation code](code/analyze.py)
- [Results](results/summary.json)
- [Verification](verification.md)
- [Separate AI reviews](reviews/)
- [Earlier Canada policy application](../2026-10-12-canada-policy-application/paper.md)

## Reproduce

From this folder, run:

```sh
python3 code/analyze.py
```

Python 3 with the standard library is sufficient. Decimal arithmetic produces 12 package cases, 21 stress cases, four single-source calculations, three funding thresholds, three public-fund asset requirements, and ten borrowing-year rows. CSV files use LF line endings. Decimal values in the summary are strings to preserve precision.

The model replaces existing capital-related receipts and net GST before counting new money. It deducts retained GST relief, new rebates, and added tax administration. It keeps provincial costs and tax claims outside the federal result. It does not solve prices, investment, household demand, or cross-border responses together.

These are separate AI checks within an AI-assisted project. They are not human or external peer review.
