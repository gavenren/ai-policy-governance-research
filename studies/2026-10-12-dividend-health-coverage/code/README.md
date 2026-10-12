# S017 arithmetic reproduction

This code executes the protocol's ten illustrative cases under four treatments. It uses only the Python standard library and needs no network access. The recorded version is Python 3.12.14. This is not a Medicaid eligibility engine. It does not determine legal eligibility, enrollment, access to care, or welfare.

The upper ceiling of $1,800 is deliberately illustrative. The $580 lower input is the protocol's $7.25 times 80. The new cash amounts are illustrative and are not estimates of the bill's actual rent-linked payments. The analysis adds no cases or estimated population frequencies.

## Reproduce without changing the first-run record

From the repository root:

```sh
python studies/2026-10-12-dividend-health-coverage/code/check_cases.py \
  --output-dir .local-verification/s017-reproduction \
  --log .local-verification/s017-reproduction/execution.json
python studies/2026-10-12-dividend-health-coverage/code/test_cases.py
cmp studies/2026-10-12-dividend-health-coverage/results/cases.csv \
  .local-verification/s017-reproduction/cases.csv
```

The checker stops if the protocol differs from SHA-256 `4b753984475f33712d617925995ae3e76d8f3c5b1bdca2a9b6b0989418691566`. The saved input rows exactly match that protocol's case table. `logs/numerical-pre-execution.json` records the input and test-code hashes before the first formal run. The ten-case design and the underlying question followed exploratory reading and examples; this is not a preregistered discovery.

The first formal run began at `2026-10-12T18:44:41.245607Z`. It produced all 40 rows in `results/cases.csv`, SHA-256 `3f720fb491584eae82c11923a5fbcabc787737402491d2c43b8e7ee88222e1e7`. The execution and test command records are in `logs/numerical-execution.json`; their raw outputs are retained. `logs/execution.json` records the software version and input and output hashes.

## Focused checks

The ten tests passed. A hand-coded expected outcome table checks all 40 combined results. It was saved before execution and does not reuse legal-source code or a second call to the same decision formula. Additional checks cover the opening and ceiling-crossing arithmetic, baseline preservation under shared disregard, zero-payment equivalence, inclusive boundaries, another verified route, an inapplicable lower requirement, weak inclusion of shared-disregard passes under the proposed split, insufficient cash, and clear rejection of negative amounts. These tests check the illustration. They do not validate a legal interpretation.

Shared disregard leaves the two income inputs and all checks equal to the no-payment baseline in all ten cases. It can therefore leave a potential new lower-income route unopened, but it does not remove a route that this no-payment baseline already met. The proposed split is a conditional policy treatment, not a claim about a state's current legal powers.

Input and output fields are defined in `../data/README.md`. The separate root agent owns the sources, manuscript and legal interpretation. The analysis agent did not change them or the protocol.
