"""Offline, standard-library audit. All populations are synthetic and equally weighted."""
import argparse
import csv
import hashlib
import itertools
import json
import math
from pathlib import Path
import platform
import random
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]


def mean(x):
    return math.fsum(x) / len(x)


def covariance(x, y):
    mx, my = mean(x), mean(y)
    return math.fsum((a - mx) * (b - my) for a, b in zip(x, y)) / len(x)


def measures(x):
    if not x or any(not math.isfinite(v) or v < 0 for v in x) or mean(x) <= 0:
        raise ValueError("A nonnegative finite population with a positive mean is required")
    mu = mean(x)
    variance = covariance(x, x)
    gini = math.fsum(abs(a - b) for a in x for b in x) / (2 * len(x)**2 * mu)
    return {"mean": mu, "variance": variance, "cv2": variance / mu**2, "gini": gini}


def affine(x, a, b):
    return [a * v + b for v in x]


def consumption(x, saving, tax):
    """Solve y_i=(x_i+b)/d_i and n*b=sum((d_i-1)*y_i)."""
    if tax < 0 or len(saving) != len(x) or any(s < 0 or s > 1 for s in saving):
        raise ValueError("Invalid tax or saving rates")
    d = [1 + tax * (1 - s) for s in saving]
    b = (math.fsum(x) - math.fsum(v / c for v, c in zip(x, d))) / math.fsum(1 / c for c in d)
    y = [(v + b) / c for v, c in zip(x, d)]
    revenue = math.fsum((c - 1) * v for c, v in zip(d, y))
    return y, b, revenue, revenue - len(x) * b


def ces(k, h, ai, alpha, beta, theta, omega):
    s = (beta * h**omega + (1 - beta) * ai**omega)**(1 / omega)
    y = (alpha * k**theta + (1 - alpha) * s**theta)**(1 / theta)
    pk = alpha * (k / y)**theta
    ph = (1 - alpha) * beta * (s / y)**theta * (h / s)**omega
    pa = (1 - alpha) * (1 - beta) * (s / y)**theta * (ai / s)**omega
    return s, y, (pk, ph, pa)


def write_csv(path, rows):
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def run(output):
    design_path = ROOT / "data/design.json"
    cfg = json.loads(design_path.read_text())
    output.mkdir(parents=True, exist_ok=True)
    tables = {}
    rows = []
    for name, x in cfg["income_vectors"].items():
        m = measures(x)
        for a, b in itertools.product(cfg["scale_factors"], cfg["additions"]):
            p = measures(affine(x, a, b))
            ratio = a * m["mean"] / (a * m["mean"] + b)
            rows.append({"case": name, "n": len(x), "a": a, "b": b,
                         **{f"before_{k}": v for k, v in m.items()},
                         **{f"after_{k}": v for k, v in p.items()},
                         "cv2_formula_error": p["cv2"] - ratio**2 * m["cv2"],
                         "gini_formula_error": p["gini"] - ratio * m["gini"]})
    tables["affine.csv"] = rows
    rows = []
    for name, x in cfg["income_vectors"].items():
        m = measures(x)
        for saving, tax in itertools.product(cfg["saving_rates"], cfg["tax_rates"]):
            y, b, revenue, residual = consumption(x, [saving] * len(x), tax)
            p = measures(y)
            d = 1 + tax * (1 - saving)
            no_rebate = measures([v / d for v in x])
            rows.append({"case": name, "n": len(x), "saving": saving, "tax": tax, "d": d,
                         "rebate_per_person": b, "total_revenue": revenue, "budget_residual": residual,
                         "before_mean": m["mean"], "after_mean": p["mean"],
                         "before_cv2": m["cv2"], "after_cv2": p["cv2"],
                         "before_gini": m["gini"], "after_gini": p["gini"],
                         "cv2_formula_error": p["cv2"] - m["cv2"] / d**2,
                         "gini_formula_error": p["gini"] - m["gini"] / d,
                         "no_rebate_cv2": no_rebate["cv2"],
                         "individual_budget_max_error": max(abs(c + b - d * v) for c, v in zip(x, y))})
    tables["consumption.csv"] = rows
    rng = random.Random(cfg["random_seed"])
    rows = []
    for i in range(cfg["random_cases"]):
        x = [rng.lognormvariate(0, 1) for _ in range(cfg["random_individuals"])]
        a, b, saving, tax = rng.uniform(0.1, 2), rng.uniform(0, 10), rng.uniform(0, 0.99), rng.uniform(0, 3)
        m = measures(x)
        p = measures(affine(x, a, b))
        ratio = a * m["mean"] / (a * m["mean"] + b)
        y, rebate, revenue, residual = consumption(x, [saving] * len(x), tax)
        d = 1 + tax * (1 - saving)
        rows.append({"case": i, "income_json": json.dumps(x), "a": a, "b": b, "saving": saving, "tax": tax,
                     "affine_cv2_error": p["cv2"] - ratio**2 * m["cv2"],
                     "affine_gini_error": p["gini"] - ratio * m["gini"],
                     "consumption_cv2_error": measures(y)["cv2"] - m["cv2"] / d**2,
                     "rebate_per_person": rebate, "total_revenue": revenue, "budget_residual": residual})
    tables["random_checks.csv"] = rows
    rows = []
    c = cfg["ces"]
    for alpha, beta, theta, omega, k, h, ai in itertools.product(c["alpha"], c["beta"], c["theta"], c["omega"], c["inputs"], c["inputs"], c["inputs"]):
        s, y, shares = ces(k, h, ai, alpha, beta, theta, omega)
        inputs = [k, h, ai]
        rhs = math.fsum(p * math.log(v) for p, v in zip(shares, inputs))
        errors = []
        eps = c["difference_step"]
        for j in range(3):
            plus, minus = inputs.copy(), inputs.copy()
            plus[j] *= math.exp(eps)
            minus[j] *= math.exp(-eps)
            logplus = math.log(ces(*plus, alpha, beta, theta, omega)[1])
            logminus = math.log(ces(*minus, alpha, beta, theta, omega)[1])
            errors.append((logplus - logminus) / (2 * eps) - shares[j])
        # Euler's theorem in levels: marginal products = share * output / input.
        euler = math.fsum((p * y / v) * v for p, v in zip(shares, inputs)) - y
        rows.append({"alpha": alpha, "beta": beta, "theta": theta, "omega": omega,
                     "K": k, "H": h, "AI": ai, "S": s, "Y": y,
                     "share_K": shares[0], "share_H": shares[1], "share_AI": shares[2],
                     "log_Y": math.log(y), "weighted_log_inputs": rhs, "log_residual": math.log(y) - rhs,
                     "share_sum_error": math.fsum(shares) - 1, "euler_level_error": euler,
                     "elasticity_max_error": max(abs(v) for v in errors)})
    tables["ces.csv"] = rows
    rows = []
    base = [1, 2, 2]
    base_y = ces(*base, 0.5, 0.5, -1, 1)
    gradient = math.fsum(a * b for a, b in zip(base_y[2], c["local_direction"]))
    for eps in c["local_steps"]:
        moved = [v * math.exp(eps * d) for v, d in zip(base, c["local_direction"])]
        change = math.log(ces(*moved, 0.5, 0.5, -1, 1)[1] / base_y[1])
        rows.append({"step": eps, "actual_log_change": change, "local_prediction": eps * gradient,
                     "error": change - eps * gradient, "error_over_step_squared": (change - eps * gradient) / eps**2})
    tables["local_approximation.csv"] = rows
    rows = []
    for path in ["constant_ratio", "linear_ratio", "exponential_ratio"]:
        for t in cfg["path_times"]:
            k = math.exp(t)
            ratio = 1 if path == "constant_ratio" else 1 + t if path == "linear_ratio" else math.exp(t)
            s_target = ratio * k
            ai = 2 * s_target - 1
            s, y, shares = ces(k, 1, ai, 0.5, 0.5, -1, 1)
            rows.append({"path": path, "t": t, "K": k, "H": 1, "AI": ai, "S": s, "S_over_K": s / k,
                         "Y": y, "share_K": shares[0], "share_H": shares[1], "share_AI": shares[2],
                         "share_K_formula_error": shares[0] - ratio / (1 + ratio)})
    tables["input_paths.csv"] = rows
    rows = []
    coeff = cfg["component_multipliers"]
    for name, matrix in cfg["components"].items():
        columns = list(zip(*matrix))
        x = [math.fsum(a * v for a, v in zip(coeff, row)) + cfg["component_transfer"] for row in matrix]
        m = measures(x)
        numerator = math.fsum(coeff[j] * coeff[k] * covariance(columns[j], columns[k]) for j in range(3) for k in range(3))
        rows.append({"case": name, "n": len(x), "income_mean": m["mean"], "direct_cv2": m["cv2"],
                     "covariance_cv2": numerator / m["mean"]**2, "formula_error": m["cv2"] - numerator / m["mean"]**2})
    tables["income_covariance.csv"] = rows
    logmatrix = [[math.log(v) for v in row] for row in cfg["log_endowments"]]
    weights = cfg["log_weights"]
    columns = list(zip(*logmatrix))
    index = [math.fsum(a * v for a, v in zip(weights, row)) for row in logmatrix]
    direct = covariance(index, index)
    bycov = math.fsum(weights[j] * weights[k] * covariance(columns[j], columns[k]) for j in range(3) for k in range(3))
    tables["log_index.csv"] = [{"n": len(index), "direct_variance": direct, "covariance_variance": bycov, "formula_error": direct - bycov}]
    rows = []
    examples = [
        ("baseline", [1, 3], [1, 3], 0, "none"),
        ("equal_addition", [1, 3], [2, 4], 1, "external_resources_unspecified"),
        ("common_scale", [1, 3], [2, 6], 0, "proportional_growth"),
        ("indexed_equal", [1, 3], [1 + 2/3, 3 + 2/3], 2/3, "u=1/4_of_final_mean"),
        ("indexed_proportional", [1, 3], [4/3, 4], 0, "same_total_as_indexed_equal"),
    ]
    for name, saving in [("common_saving_rebate", [0, 0]), ("high_income_saves", [0, 1]), ("low_income_saves", [1, 0])]:
        x = [1, 3] if name == "common_saving_rebate" else [1, 9]
        y, b, revenue, residual = consumption(x, saving, 1)
        examples.append((name, x, y, b, f"tax=1;saving={saving};budget_residual={residual}"))
    for name, x, y, b, note in examples:
        rows.append({"case": name, "before_income_json": json.dumps(x), "after_income_json": json.dumps(y),
                     "rebate_per_person": b, **{f"before_{k}": v for k, v in measures(x).items()},
                     **{f"after_{k}": v for k, v in measures(y).items()}, "note": note})
    tables["worked_examples.csv"] = rows
    for filename, table in tables.items():
        write_csv(output / filename, table)
    def maxabs(table, field):
        return max(abs(r[field]) for r in tables[table])
    summary = {
        "rows": {name: len(table) for name, table in tables.items()},
        "max_affine_cv2_error": maxabs("affine.csv", "cv2_formula_error"),
        "max_affine_gini_error": maxabs("affine.csv", "gini_formula_error"),
        "max_common_rebate_cv2_error": maxabs("consumption.csv", "cv2_formula_error"),
        "max_common_rebate_budget_residual": maxabs("consumption.csv", "budget_residual"),
        "max_ces_elasticity_error": maxabs("ces.csv", "elasticity_max_error"),
        "max_ces_log_residual": maxabs("ces.csv", "log_residual"),
        "ces_nonzero_residuals_above_1e_10": sum(abs(r["log_residual"]) > 1e-10 for r in tables["ces.csv"]),
        "max_income_covariance_error": maxabs("income_covariance.csv", "formula_error"),
        "all_input_data_synthetic": True,
    }
    (output / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    manifest = {
        "run_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "python": platform.python_version(), "dependencies": "Python standard library only",
        "seed": cfg["random_seed"], "command": "python3 code/analyze.py", "exit_status": 0,
        "input_sha256": hashlib.sha256(design_path.read_bytes()).hexdigest(),
        "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "output_sha256": {name: hashlib.sha256((output / name).read_bytes()).hexdigest() for name in [*tables, "summary.json"]},
    }
    (output / "run.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "results")
    run(parser.parse_args().output)
