"""Separate review calculations; does not import the study's analysis module.

Fractions check income measures and solve the tax system by elimination.
Decimal checks CES levels and marginal products at 60-digit precision.
"""
import csv
from datetime import datetime, timezone
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def stats(values):
    n = len(values)
    mu = sum(values) / n
    variance = sum(v * v for v in values) / n - mu * mu
    gini = sum(abs(a - b) for a in values for b in values) / (2 * n * n * mu)
    return {"mean": mu, "variance": variance, "cv2": variance / (mu * mu), "gini": gini}


def solve_tax(values, savings, tax):
    """Eliminate n household budget equations after substituting equal rebates."""
    n = len(values)
    q = [tax * (1 - s) for s in savings]
    matrix = [[(1 + q[i] if i == j else F(0)) - q[j] / n
               for j in range(n)] + [values[i]] for i in range(n)]
    for j in range(n):
        pivot = next(k for k in range(j, n) if matrix[k][j])
        matrix[j], matrix[pivot] = matrix[pivot], matrix[j]
        scale = matrix[j][j]
        matrix[j] = [v / scale for v in matrix[j]]
        for i in range(n):
            if i != j:
                scale = matrix[i][j]
                matrix[i] = [a - scale * b for a, b in zip(matrix[i], matrix[j])]
    final = [row[-1] for row in matrix]
    rebate = sum(a * b for a, b in zip(q, final)) / n
    assert sum(final) == sum(values)
    assert all((1 + q[i]) * final[i] == values[i] + rebate for i in range(n))
    return final, rebate


def rows(name):
    with (ROOT / "results" / name).open() as stream:
        return list(csv.DictReader(stream))


def check():
    cfg = json.loads((ROOT / "data/design.json").read_text(), parse_float=F, parse_int=F)
    maxima = {}

    def compare(group, actual, expected, tolerance):
        error = abs(float(actual) - float(expected))
        maxima[group] = max(maxima.get(group, 0), error)
        assert error <= tolerance, (group, actual, expected, error)

    counts = {}
    for row in rows("affine.csv"):
        x = cfg["income_vectors"][row["case"]]
        a, b = F(row["a"]), F(row["b"])
        before, after = stats(x), stats([a * v + b for v in x])
        factor = a * before["mean"] / (a * before["mean"] + b)
        assert after["cv2"] == factor**2 * before["cv2"]
        assert after["gini"] == factor * before["gini"]
        for key in after:
            compare("affine_" + key, row["after_" + key], after[key], 1e-9)
    counts["fraction_affine_rows"] = len(rows("affine.csv"))

    for row in rows("consumption.csv"):
        x = cfg["income_vectors"][row["case"]]
        saving, tax = F(row["saving"]), F(row["tax"])
        final, rebate = solve_tax(x, [saving] * len(x), tax)
        compare("tax_rebate", row["rebate_per_person"], rebate, 1e-10)
        after = stats(final)
        assert after["cv2"] == stats(x)["cv2"] / (1 + tax * (1 - saving))**2
        for key in ("mean", "cv2", "gini"):
            compare("tax_" + key, row["after_" + key], after[key], 1e-10)
    counts["fraction_tax_linear_systems"] = len(rows("consumption.csv"))

    worked = {row["case"]: row for row in rows("worked_examples.csv")}
    exact_worked = {}
    for name, savings in [("high_income_saves", [F(0), F(1)]),
                          ("low_income_saves", [F(1), F(0)])]:
        final, rebate = solve_tax([F(1), F(9)], savings, F(1))
        index = stats(final)["cv2"]
        compare("heterogeneous_cv2", worked[name]["after_cv2"], index, 1e-12)
        compare("heterogeneous_rebate", worked[name]["rebate_per_person"], rebate, 1e-12)
        exact_worked[name] = {"incomes": list(map(str, final)), "rebate": str(rebate), "cv2": str(index)}
    exact_worked["indexed_equal_cv2"] = str(stats([F(5, 3), F(11, 3)])["cv2"])
    assert exact_worked["indexed_equal_cv2"] == "9/64"
    compare("indexed_equal", worked["indexed_equal"]["after_cv2"], F(9, 64), 1e-12)

    with localcontext() as context:
        context.prec = 60
        nonzero = 0
        for row in rows("ces.csv"):
            alpha, beta, theta, omega, k, h, ai = (D(row[key]) for key in ("alpha", "beta", "theta", "omega", "K", "H", "AI"))
            inner = beta * h**omega + (1 - beta) * ai**omega
            s = inner**(1 / omega)
            outer = alpha * k**theta + (1 - alpha) * s**theta
            y = outer**(1 / theta)
            marginal_k = alpha * k**(theta - 1) * outer**(1 / theta - 1)
            marginal_s = (1 - alpha) * s**(theta - 1) * outer**(1 / theta - 1)
            marginal_h = marginal_s * beta * h**(omega - 1) * inner**(1 / omega - 1)
            marginal_ai = marginal_s * (1 - beta) * ai**(omega - 1) * inner**(1 / omega - 1)
            products = [marginal_k * k, marginal_h * h, marginal_ai * ai]
            shares = [p / y for p in products]
            assert abs(sum(products) - y) < D("1e-50")
            assert abs(sum(shares) - 1) < D("1e-50")
            residual = y.ln() - sum(p * z.ln() for p, z in zip(shares, [k, h, ai]))
            nonzero += abs(residual) > D("1e-10")
            compare("ces_output", row["Y"], y, 1e-12)
            for field, share in zip(("share_K", "share_H", "share_AI"), shares):
                compare("ces_shares", row[field], share, 1e-12)
            compare("ces_log_residual", row["log_residual"], residual, 1e-12)
        counts["decimal_ces_rows"] = len(rows("ces.csv"))
        counts["decimal_nonzero_ces_residuals"] = nonzero
        assert nonzero == 1944

        for row in rows("input_paths.csv"):
            t = D(row["t"])
            ratio = D(1) if row["path"] == "constant_ratio" else 1 + t if row["path"] == "linear_ratio" else t.exp()
            pk = ratio / (1 + ratio)
            ph = 1 / (2 * t.exp() * ratio * (1 + ratio))
            compare("path_capital_share", row["share_K"], pk, 1e-12)
            compare("path_labor_share", row["share_H"], ph, 1e-12)
            compare("path_ai_share", row["share_AI"], 1 - pk - ph, 1e-12)
        counts["decimal_path_rows"] = len(rows("input_paths.csv"))

    for row in rows("income_covariance.csv"):
        matrix = cfg["components"][row["case"]]
        x = [sum(a * v for a, v in zip(cfg["component_multipliers"], person)) + cfg["component_transfer"] for person in matrix]
        expected = stats(x)["cv2"]
        compare("income_covariance_cv2", row["covariance_cv2"], expected, 1e-12)
    counts["fraction_covariance_rows"] = len(rows("income_covariance.csv"))

    result = {"review_calculation_utc": datetime.now(timezone.utc).isoformat(),
              "status": "pass", "analysis_module_imported": False,
              "methods": ["Fraction second-moment income measures", "Fraction Gaussian elimination of tax budgets", "60-digit Decimal CES levels and separate marginal products", "closed-form relative-input path shares"],
              "counts": counts, "exact_worked_examples": exact_worked,
              "max_absolute_difference_from_retained_float_results": maxima,
              "limits": "Does not independently recalculate the random draw generator, local finite-difference grid or fixed log-index row; the separate full rerun covers their reproduction."}
    (ROOT / "reviews/independent-results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    check()
