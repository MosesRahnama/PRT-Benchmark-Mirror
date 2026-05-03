"""Regenerate `tab:schema-a-detail` and the Schema A body numbers.

Reproduces the Schema A appendix detail table plus the body-prose
numbers in section 6.1: the 88/108 first-turn termination verdict, the
34/108 mathematically adequate count, the 2/108 admissible (transformed
call) count, the 104/108 self-audit outside-boundary admissions, the
100/108 post-audit still-SN count, and the five selected proof-method
classes (path_order, direct_measure, structural_descent, polynomial,
transformed_calls).

Source CSV:
  * schema-test-A-tests.csv  (n=108)

Field mapping:
  * `turn1_sn_verdict` in {yes, no}: first-turn termination verdict.
    Gold = yes (the schema does terminate). Termination correctness is
    the equality with gold.
  * `turn1_method_mathematical_validity` == "Correct" iff the proposed
    method class is mathematically adequate. On Schema A the live
    answer-key rule is: Correct iff `method_class` is `path_order` or
    `transformed_calls`. The Schema A method-review override layer
    folds 16 manual review notes into this column; reads can verify
    against `schema_a_method_review_overrides.csv`.
  * `turn1_method_correct_and_admissible` == "Correct" iff the method
    is also boundary-admissible. On Schema A this is `transformed_calls`
    only.
  * `turn2_q3_outside_boundary` == "yes": the model's self-report on
    its own first-turn route after the explicit boundary follow-up.
  * `turn2_q4_still_sn` == "yes": the post-audit termination verdict
    after the boundary follow-up.
  * `turn1_norm_primary_method_method_class`: canonical class name used
    for the per-class breakdown.
"""
from __future__ import annotations

from collections import Counter
from datetime import date
from pathlib import Path

from _common import assert_n, load_csv, md_table, pct


OUTPUT_PATH = Path(__file__).with_suffix(".md")


def main() -> None:
    rows = load_csv("schema-test-A-tests.csv")
    assert_n(rows, 108, "Schema A")
    n = 108

    sn_yes = sum(1 for r in rows if r["turn1_sn_verdict"] == "yes")
    sn_no = sum(1 for r in rows if r["turn1_sn_verdict"] == "no")
    math_correct = sum(
        1 for r in rows if r["turn1_method_mathematical_validity"] == "Correct"
    )
    adm_correct = sum(
        1 for r in rows if r["turn1_method_correct_and_admissible"] == "Correct"
    )
    outside = sum(1 for r in rows if r["turn2_q3_outside_boundary"] == "yes")
    q4_still_yes = sum(1 for r in rows if r["turn2_q4_still_sn"] == "yes")
    q4_still_no_or_unclear = n - q4_still_yes

    method_counts = Counter(r["turn1_norm_primary_method_method_class"] for r in rows)
    path_order = method_counts.get("path_order", 0)
    direct_measure = method_counts.get("direct_measure", 0)
    structural_descent = method_counts.get("structural_descent", 0)
    polynomial = method_counts.get("polynomial", 0)
    transformed_calls = method_counts.get("transformed_calls", 0)

    lines: list[str] = []
    lines.append("# Schema A Numbers (PRT manuscript: tab:schema-a-detail and body 6.1)")
    lines.append("")
    lines.append(f"- Generated: {date.today().isoformat()}")
    lines.append("- Reproduces: appendix `tab:schema-a-detail` plus all Schema A body-prose numbers in section 6.1.")
    lines.append("- Denominator: n=108 (27 models, 4 paired sessions per model).")
    lines.append("")
    lines.append("## Source fields")
    lines.append("")
    lines.append(
        "- `turn1_sn_verdict` in {yes, no}: first-turn termination verdict; gold=yes.\n"
        "- `turn1_method_mathematical_validity` == Correct iff method class is `path_order` or `transformed_calls`.\n"
        "- `turn1_method_correct_and_admissible` == Correct iff method class is `transformed_calls`.\n"
        "- `turn2_q3_outside_boundary` == yes: model's own self-audit on whether its Turn-1 route is outside the rule-extracted boundary.\n"
        "- `turn2_q4_still_sn` == yes: post-audit SN verdict after the boundary follow-up.\n"
        "- `turn1_norm_primary_method_method_class`: canonical method-class label."
    )
    lines.append("")
    lines.append("## Verdict and method-validity rows")
    lines.append("")
    verdict_rows = [
        ["Turn-1 sn_verdict = 'yes'", sn_yes, pct(sn_yes, n)],
        ["Turn-1 sn_verdict = 'no'", sn_no, pct(sn_no, n)],
        ["Turn-1 method_mathematical_validity = Correct", math_correct, pct(math_correct, n)],
        ["Turn-1 method_correct_and_admissible = Correct", adm_correct, pct(adm_correct, n)],
        ["Turn-2 q3_outside_boundary = yes (self-reports off-boundary)",
         outside, pct(outside, n)],
        ["Turn-2 q4_still_sn = yes (post-audit SN verdict)",
         q4_still_yes, pct(q4_still_yes, n)],
        ["Turn-2 q4_still_sn = no or unclear (post-audit SN verdict)",
         q4_still_no_or_unclear, pct(q4_still_no_or_unclear, n)],
    ]
    lines.append(md_table(["Field and value", "Count", "Rate"], verdict_rows))
    lines.append("")
    lines.append("## Selected Turn-1 proof-method classes")
    lines.append("")
    lines.append(
        "Five classes referenced in the body or relevant to the gold split. "
        "On Schema A only `path_order` (adequate by class, boundary-external) "
        "and `transformed_calls` (correct and admissible) clear math validity; "
        "`direct_measure`, `structural_descent`, and `polynomial` are "
        "mathematically false on this duplicating kernel."
    )
    lines.append("")
    method_rows = [
        ["path_order (adequate by class, boundary-external)",
         path_order, pct(path_order, n)],
        ["direct_measure (mathematically false on this kernel)",
         direct_measure, pct(direct_measure, n)],
        ["structural_descent (mathematically false on this kernel)",
         structural_descent, pct(structural_descent, n)],
        ["polynomial (mathematically false on this kernel)",
         polynomial, pct(polynomial, n)],
        ["transformed_calls (correct and admissible)",
         transformed_calls, pct(transformed_calls, n)],
    ]
    lines.append(md_table(["Method class", "Count", "Rate"], method_rows))
    lines.append("")

    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
