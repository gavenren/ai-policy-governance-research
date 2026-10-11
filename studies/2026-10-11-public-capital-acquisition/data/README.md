# Data dictionary

All inputs are synthetic. There is no country calibration, observed sample, missingness, or imputation. All amounts share an arbitrary currency unit.

Each scenario in `design.json` states `prices` (positive state-claim prices), `probabilities` (physical probabilities), `payoffs` (full final asset cash), `taxes` (outside net fiscal receipts), and `floor` (aggregate final payment). The safe gross return is one divided by the sum of state prices. The ownership bound is 0 through 1. Ownership grid values are display points; exact optima also enter the outputs.

`summary.csv` has the six environments and their exact floor-maximizing shares. `policies.csv` has 31 scenario/share choices with required initial capital, no-capital expected and worst cash, debt proceeds, safe deposit, and seller payment. A negative no-capital balance is an unfunded debt-service gap, not a feasible safe-debt policy. `states.csv` gives every underlying state for each policy. `default.csv` prices seven asset-only debt face values and reports missing purchase funds. `probabilities.csv` changes physical beliefs at fixed state prices for the risk-premium case. Fractions are exact.

`run.json` has input, code, and numerical-output hashes, runtime, timestamp, row counts, and exit status. The analysis is deterministic. Acquisition and PDF extraction are separate from model reproduction.
