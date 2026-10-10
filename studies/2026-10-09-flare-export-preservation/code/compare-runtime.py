#!/usr/bin/env python3
"""Compare complete benchmark outputs, allowing only two runtime metadata fields."""
import argparse
import copy
import datetime
import hashlib
import json
from pathlib import Path
import re


def digest(data):
    return hashlib.sha256(data).hexdigest()


def differences(a, b, pointer=""):
    if type(a) is not type(b):
        return [{"pointer": pointer, "baseline": a, "candidate": b}]
    if isinstance(a, dict):
        result = []
        for key in sorted(set(a) | set(b)):
            child = pointer + "/" + key.replace("~", "~0").replace("/", "~1")
            if key not in a or key not in b:
                result.append({"pointer": child, "baseline_present": key in a, "candidate_present": key in b})
            else:
                result.extend(differences(a[key], b[key], child))
        return result
    if isinstance(a, list):
        if len(a) != len(b):
            return [{"pointer": pointer, "baseline": a, "candidate": b}]
        return [item for i, (left, right) in enumerate(zip(a, b))
                for item in differences(left, right, pointer + "/" + str(i))]
    return [] if a == b else [{"pointer": pointer, "baseline": a, "candidate": b}]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("baseline", "candidate", "test-log", "execution-log", "acquisition", "out"):
        parser.add_argument("--" + name, type=Path, required=True)
    args = parser.parse_args()
    baseline_bytes, candidate_bytes = args.baseline.read_bytes(), args.candidate.read_bytes()
    baseline, candidate = json.loads(baseline_bytes), json.loads(candidate_bytes)
    acquisition = json.loads(args.acquisition.read_text())
    execution = json.loads(args.execution_log.read_text())
    test_bytes = args.test_log.read_bytes()
    counts = {name: int(re.search(r"^# " + name + r" (\d+)$", test_bytes.decode(), re.M).group(1))
              for name in ("tests", "pass", "fail", "cancelled", "skipped", "todo")}
    if counts != {"tests": 8, "pass": 8, "fail": 0, "cancelled": 0, "skipped": 0, "todo": 0}:
        raise ValueError("Expected all eight existing tests to pass without skips.")
    if execution["result_sha256"] != digest(candidate_bytes):
        raise ValueError("Execution ledger does not match candidate result bytes.")
    if acquisition["version"] != candidate["metadata"]["runtime"]["node"]:
        raise ValueError("Acquired runtime version does not match candidate result metadata.")
    allowed = ["/metadata/runtime/in_declared_range", "/metadata/runtime/node"]
    actual = differences(baseline, candidate)
    unexpected = [item for item in actual if item["pointer"] not in allowed]
    normalized = copy.deepcopy(candidate)
    for key in ("node", "in_declared_range"):
        normalized["metadata"]["runtime"][key] = baseline["metadata"]["runtime"][key]
    equal = normalized == baseline
    report = {
        "status": "completed_equal_outputs" if equal else "completed_output_difference",
        "comparison_recorded_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "runtime_acquisition": acquisition,
        "execution": execution,
        "tests": {**counts, "tap_log_sha256": digest(test_bytes), "runtime": acquisition["version"]},
        "comparison": {
            "baseline_result_sha256": digest(baseline_bytes),
            "candidate_result_sha256": digest(candidate_bytes),
            "baseline_runtime": baseline["metadata"]["runtime"],
            "candidate_runtime": candidate["metadata"]["runtime"],
            "allowed_difference_pointers": allowed,
            "actual_differences": actual,
            "unexpected_differences": unexpected,
            "all_other_result_data_equal": equal,
            "normalized_result_sha256": digest(json.dumps(normalized, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()),
            "scope": "Complete result objects compared, retaining all fixture/source/harness/dependency hashes, validation results, converter outputs and pair/query results. Execution timestamps are stored in a separate ledger and not present in these result objects.",
        },
        "limitations": "Two local runtimes on the same macOS arm64 host; no full-application/UI, binary-attachment, downstream acceptance or deployment test. Primary results file was read only.",
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2) + "\n")
    if not equal or unexpected:
        raise SystemExit(2)
    print(json.dumps({"status": report["status"], "tests": counts, "actual_differences": actual}, indent=2))


if __name__ == "__main__":
    main()
