#!/usr/bin/env python3
"""
check_paper_b_theory.py
Gate script for the Paper B Lean bridge modules.

Checks:
  1. Every expected theorem name appears in at least one PaperB/*.lean file.
  2. No non-comment line contains a forbidden token (sorry, admit, axiom, unsafe).
  3. No import line references an offline stack (KO7Lib).
  4. Optionally (--build): subprocess lake build KO7Benchmark.PaperB returns 0.

Outputs:
  paper_b_theory_check_report.json
  paper_b_theory_check_report.md

Exit code:
  0  all checks pass
  1  any check fails
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from datetime import datetime

# ── Expected theorems (lean-dev.md §5) ──────────────────────────────────────
EXPECTED_THEOREMS = [
    "no_additive_orients_schema_recursive_root",
    "no_additive_orients_schema_step",
    "schema_dp_rule_extracted_witness",
    "schema_dp_full_adequacy",
    "schema_no_directWhole_witness",
    "schema_has_importedWhole_witness",
    "schema_has_transformedCall_witness",
    "schema_three_kappa_summary",
    "primitive_recursion_schema_witness_partition",
    "schemaMethodStatus_matches_answerKey",
    "schemaMethodStatus_adequate_matches_answerKey",
    "schemaMethodStatus_admissible_matches_answerKey",
    "schema_partition_reflects_answer_key",
    "paperB_schema_pathOrder_boundaryExternal",
    "paperB_schema_dp_ruleExtracted",
    "paperB_schema_false_rivals_refuted",
    "schema_bottleneck_instance",
    "ko7_bottleneck_instance",
    "schema_boundary_gap_skips_importedWhole",
    "ko7_boundary_gap_skips_importedWhole",
    "supports_app_lemma_A6_duplication_obstruction",
    "supports_app_prop_A8_dp_admissible",
    "supports_app_prop_A10_schema_partition",
    "supports_app_theorem_A12_bottleneck",
    "supports_app_corollary_A13_single_step_gap",
    "paperB_theory_core_supported",
]

# ── Forbidden tokens (case-insensitive, on non-comment lines) ────────────────
FORBIDDEN_TOKENS = ["sorry", "admit", "axiom", "unsafe"]

# ── Forbidden import substrings ──────────────────────────────────────────────
FORBIDDEN_IMPORTS = ["KO7Lib"]


def is_comment_line(line: str) -> bool:
    stripped = line.strip()
    return stripped.startswith("--") or stripped.startswith("/-")


def check_files(lean_dir: Path):
    paper_b_dir = lean_dir / "KO7Benchmark" / "PaperB"
    lean_files = sorted(paper_b_dir.glob("*.lean"))

    if not lean_files:
        return {
            "error": f"No .lean files found in {paper_b_dir}",
            "theorem_results": {},
            "forbidden_token_hits": [],
            "forbidden_import_hits": [],
            "files_checked": [],
        }

    # Accumulate all source text for theorem presence checks
    all_text = ""
    forbidden_token_hits = []
    forbidden_import_hits = []
    files_checked = []

    for lf in lean_files:
        text = lf.read_text(encoding="utf-8")
        all_text += text
        files_checked.append(str(lf.name))

        for lineno, line in enumerate(text.splitlines(), 1):
            # Forbidden tokens: skip comment lines
            if not is_comment_line(line):
                for tok in FORBIDDEN_TOKENS:
                    if re.search(r'\b' + tok + r'\b', line, re.IGNORECASE):
                        forbidden_token_hits.append({
                            "file": lf.name,
                            "line": lineno,
                            "token": tok,
                            "content": line.rstrip(),
                        })
            # Forbidden imports: check import lines
            if line.strip().startswith("import "):
                for fi in FORBIDDEN_IMPORTS:
                    if fi in line:
                        forbidden_import_hits.append({
                            "file": lf.name,
                            "line": lineno,
                            "forbidden": fi,
                            "content": line.rstrip(),
                        })

    # Theorem presence: at least one match per name
    theorem_results = {}
    for name in EXPECTED_THEOREMS:
        pattern = r'\b' + re.escape(name) + r'\b'
        theorem_results[name] = bool(re.search(pattern, all_text))

    return {
        "error": None,
        "theorem_results": theorem_results,
        "forbidden_token_hits": forbidden_token_hits,
        "forbidden_import_hits": forbidden_import_hits,
        "files_checked": files_checked,
    }


def run_build(lean_dir: Path) -> dict:
    result = subprocess.run(
        ["lake", "build", "KO7Benchmark.PaperB"],
        cwd=str(lean_dir),
        capture_output=True,
        text=True,
    )
    return {
        "returncode": result.returncode,
        "stdout": result.stdout[-2000:] if result.stdout else "",
        "stderr": result.stderr[-2000:] if result.stderr else "",
    }


def main():
    parser = argparse.ArgumentParser(description="Check Paper B Lean bridge theorems.")
    parser.add_argument(
        "--root",
        default=r"<workspace>\lean",
        help="Path to the lean project root.",
    )
    parser.add_argument(
        "--report-dir",
        default=None,
        help=(
            "Directory where the JSON and Markdown reports are written. "
            "Defaults to the directory containing this script."
        ),
    )
    parser.add_argument(
        "--build",
        action="store_true",
        help="Also run lake build KO7Benchmark.PaperB.",
    )
    args = parser.parse_args()

    lean_dir = Path(args.root)
    if args.report_dir is None:
        report_dir = Path(__file__).resolve().parent
    else:
        report_dir = Path(args.report_dir).resolve()
    report_dir.mkdir(parents=True, exist_ok=True)

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    results = check_files(lean_dir)

    build_result = None
    if args.build:
        build_result = run_build(lean_dir)

    # ── Determine pass/fail ──────────────────────────────────────────────────
    all_theorems_present = all(results["theorem_results"].values())
    theorems_found = sum(1 for v in results["theorem_results"].values() if v)
    theorems_total = len(EXPECTED_THEOREMS)
    no_forbidden_tokens = len(results["forbidden_token_hits"]) == 0
    no_forbidden_imports = len(results["forbidden_import_hits"]) == 0
    build_ok = (build_result is None) or (build_result["returncode"] == 0)

    passed = all_theorems_present and no_forbidden_tokens and no_forbidden_imports and build_ok

    # ── JSON report ──────────────────────────────────────────────────────────
    json_report = {
        "generated": now,
        "passed": passed,
        "files_checked": results["files_checked"],
        "theorem_presence": results["theorem_results"],
        "theorems_found": theorems_found,
        "theorems_total": theorems_total,
        "forbidden_token_hits": results["forbidden_token_hits"],
        "forbidden_import_hits": results["forbidden_import_hits"],
        "build": build_result,
        "error": results.get("error"),
    }

    json_path = report_dir / "paper_b_theory_check_report.json"
    json_path.write_text(json.dumps(json_report, indent=2), encoding="utf-8")

    # ── Markdown report ──────────────────────────────────────────────────────
    lines = [
        f"# Paper B Theory Check Report",
        f"",
        f"Generated: {now}  ",
        f"Overall: {'**PASS**' if passed else '**FAIL**'}",
        f"",
        f"## Files checked",
        "",
    ]
    for f in results["files_checked"]:
        lines.append(f"- `{f}`")

    lines += [
        "",
        f"## Theorem presence ({theorems_found}/{theorems_total})",
        "",
        "| Theorem | Present |",
        "|---|---|",
    ]
    for name, present in results["theorem_results"].items():
        mark = "yes" if present else "**MISSING**"
        lines.append(f"| `{name}` | {mark} |")

    lines += [
        "",
        f"## Forbidden tokens: {len(results['forbidden_token_hits'])} hit(s)",
        "",
    ]
    if results["forbidden_token_hits"]:
        for hit in results["forbidden_token_hits"]:
            lines.append(f"- `{hit['file']}` line {hit['line']}: `{hit['token']}` in `{hit['content']}`")
    else:
        lines.append("None.")

    lines += [
        "",
        f"## Forbidden imports: {len(results['forbidden_import_hits'])} hit(s)",
        "",
    ]
    if results["forbidden_import_hits"]:
        for hit in results["forbidden_import_hits"]:
            lines.append(f"- `{hit['file']}` line {hit['line']}: `{hit['content']}`")
    else:
        lines.append("None.")

    if build_result is not None:
        rc = build_result["returncode"]
        lines += [
            "",
            f"## Build: `lake build KO7Benchmark.PaperB`",
            "",
            f"Exit code: {rc} ({'OK' if rc == 0 else 'FAIL'})",
        ]
        if rc != 0:
            lines.append(f"```\n{build_result['stderr']}\n```")

    md_path = report_dir / "paper_b_theory_check_report.md"
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    # ── Console summary ──────────────────────────────────────────────────────
    print(f"Theorems found:        {theorems_found}/{theorems_total}")
    print(f"Forbidden tokens:      {len(results['forbidden_token_hits'])}")
    print(f"Forbidden imports:     {len(results['forbidden_import_hits'])}")
    if build_result is not None:
        print(f"Build exit code:       {build_result['returncode']}")
    print(f"Overall:               {'PASS' if passed else 'FAIL'}")
    print(f"Report written to:     {report_dir}")

    if not passed:
        missing = [n for n, v in results["theorem_results"].items() if not v]
        if missing:
            print(f"\nMissing theorems:", file=sys.stderr)
            for n in missing:
                print(f"  - {n}", file=sys.stderr)
        if results["forbidden_token_hits"]:
            print(f"\nForbidden token hits:", file=sys.stderr)
            for h in results["forbidden_token_hits"]:
                print(f"  {h['file']}:{h['line']}: {h['token']}", file=sys.stderr)
        if results["forbidden_import_hits"]:
            print(f"\nForbidden import hits:", file=sys.stderr)
            for h in results["forbidden_import_hits"]:
                print(f"  {h['file']}:{h['line']}: {h['content']}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
