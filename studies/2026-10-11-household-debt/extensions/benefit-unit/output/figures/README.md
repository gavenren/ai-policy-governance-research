# S011 equal-budget figure

`equal-budget-outcomes.png` is the 400-dpi image. The PDF and SVG files are vector copies of the same figure. `caption-draft.md` is a proposed caption; it has not been inserted into the manuscript. The figure uses three aligned panels, direct value labels, three distinct marker shapes, and dark gray, blue and vermilion colors. Color is not the sole way to identify a rule.

Only nine rows from the already published `results/outcomes.csv` are plotted. No financial microdata, weights, replicates or analysis model are loaded. The source file SHA-256 is `cbc9cca343d5d50ed82c1ba03b25eccfa37321d9b453f3c2e5cbe946b90484a2`. `published-source-check.json` records exact-byte comparisons of the manuscript, results and dictionary with publication commit `a3b7399ed0764f712d7de19b922f037670684b57`.

`plotted-data.csv` retains each selected source key, source estimate, standard error, saved interval endpoints, plotted values, unit and transformation. Percentages are scaled by 100. Family failure is one minus the saved family pass rate; the complemented interval uses the reversed source endpoints. Dollar values are unchanged. The saved normal 95% bounds support the displayed intervals. No new confidence interval, paired-difference test or model-uncertainty measure is created.

From the repository root, with Python 3.12 and Matplotlib 3.10.7:

```sh
python studies/2026-10-11-household-debt/extensions/benefit-unit/code/plot_equal_budget.py \
  --output .local-verification/s011-equal-budget-reproduction
```

The plotting script guards the two source hashes and checks all nine numerical labels against the published Section 8 table. It records software and font hashes, drawing bounds, and output hashes. The three panels have different horizontal scales, as stated on the figure and in the caption. PDF fonts are embedded; SVG text is stored as vector outlines. The font files themselves are not distributed.

`visual-check.json` records inspection of the PNG and the PDF render. `authoring-log.json` retains the first layout guard failure and its repair. `figure-manifest.json` pins the final figure package. Existing source data, analysis code, manuscript and other outputs were not changed.
