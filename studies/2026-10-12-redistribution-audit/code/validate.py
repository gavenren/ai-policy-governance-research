"""Validate retained outputs, planned controls, and optional original source bytes."""
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def require(condition, description):
    if not condition:
        raise ValueError(description)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--local-source-root", type=Path)
    args = parser.parse_args()
    run = json.loads((ROOT / "results/run.json").read_text())
    digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
    require(digest(ROOT / "data/design.json") == run["input_sha256"], "Design hash mismatch")
    require(digest(ROOT / "code/analyze.py") == run["code_sha256"], "Analysis code hash mismatch")
    for name, expected in run["output_sha256"].items():
        require(digest(ROOT / "results" / name) == expected, "Output hash mismatch: " + name)
    planned = {"affine.csv": 72, "consumption.csv": 120, "random_checks.csv": 200,
               "ces.csv": 2187, "local_approximation.csv": 4, "input_paths.csv": 24,
               "income_covariance.csv": 4, "log_index.csv": 1, "worked_examples.csv": 8}
    tables = {}
    for name, count in planned.items():
        rows = list(csv.DictReader((ROOT / "results" / name).open()))
        require(len(rows) == count, "Missing planned rows: " + name)
        require(len({tuple(r.values()) for r in rows}) == count, "Duplicate complete rows: " + name)
        for row in rows:
            for value in row.values():
                try:
                    number = float(value)
                except ValueError:
                    continue
                require(math.isfinite(number), "Nonfinite result: " + name)
        tables[name] = rows
    for row in tables["affine.csv"]:
        require(abs(float(row["cv2_formula_error"])) < 1e-12, "Affine variance formula failed")
        require(abs(float(row["gini_formula_error"])) < 1e-12, "Affine Gini formula failed")
    for row in tables["consumption.csv"]:
        for key in ["cv2_formula_error", "gini_formula_error"]:
            require(abs(float(row[key])) < 1e-12, "Rebate formula failed")
        for key in ["budget_residual", "individual_budget_max_error"]:
            require(abs(float(row[key])) < 1e-9, "Budget balance failed")
        require(abs(float(row["before_mean"]) - float(row["after_mean"])) < 1e-9, "Rebate mean changed")
        require(abs(float(row["no_rebate_cv2"]) - float(row["before_cv2"])) < 1e-12, "No-rebate scaling control failed")
    for row in tables["random_checks.csv"]:
        for key in ["affine_cv2_error", "affine_gini_error", "consumption_cv2_error"]:
            require(abs(float(row[key])) < 1e-12, "Seeded implementation check failed")
        require(abs(float(row["budget_residual"])) < 1e-9, "Seeded budget failed")
    for row in tables["ces.csv"]:
        require(abs(float(row["share_sum_error"])) < 1e-12, "CES shares fail to sum")
        require(abs(float(row["euler_level_error"])) < 1e-12, "Euler level control failed")
        require(float(row["elasticity_max_error"]) < 1e-8, "Finite-difference elasticity control failed")
    require(sum(abs(float(r["log_residual"])) > 1e-10 for r in tables["ces.csv"]) == 1944, "CES residual count changed")
    local = [abs(float(r["error"])) for r in tables["local_approximation.csv"]]
    require(all(a > b for a, b in zip(local, local[1:])), "Local approximation did not improve")
    for row in tables["input_paths.csv"]:
        require(abs(float(row["share_K_formula_error"])) < 1e-12, "Path share formula failed")
        if row["path"] == "constant_ratio":
            require(abs(float(row["share_K"]) - 0.5) < 1e-12, "Constant-ratio control failed")
    for name in ["income_covariance.csv", "log_index.csv"]:
        require(all(abs(float(r["formula_error"])) < 1e-12 for r in tables[name]), "Covariance control failed")
    examples = {r["case"]: r for r in tables["worked_examples.csv"]}
    require(float(examples["high_income_saves"]["after_cv2"]) > float(examples["high_income_saves"]["before_cv2"]), "Heterogeneous boundary disappeared")
    require(float(examples["low_income_saves"]["after_cv2"]) < float(examples["low_income_saves"]["before_cv2"]), "Reverse boundary disappeared")
    source_rows = list(csv.DictReader((ROOT / "sources/manifest.csv").open()))
    require(len(source_rows) == 6, "Expected six source representations")
    require(len({r["capture_id"] for r in source_rows}) == 6, "Duplicate capture ID")
    checked = 0
    if args.local_source_root:
        for row in source_rows:
            for kind, pathkey in [("original", "retained_original"), ("extracted", "retained_extraction")]:
                path = args.local_source_root / row[pathkey]
                require(digest(path) == row[kind + "_sha256"], "Source hash mismatch: " + row["capture_id"])
                require(path.stat().st_size == int(row[kind + "_bytes"]), "Source length mismatch")
                checked += 1
    print(json.dumps({"status": "pass", "output_hash_checks": len(run["output_sha256"]),
                      "planned_tables": len(planned), "planned_rows": sum(planned.values()),
                      "source_representation_records": len(source_rows), "local_source_hash_checks": checked,
                      "tolerances": {"formula": 1e-12, "budget": 1e-9, "finite_difference": 1e-8}}, indent=2))


if __name__ == "__main__":
    main()
