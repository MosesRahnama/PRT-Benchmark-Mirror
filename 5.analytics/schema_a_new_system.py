"""Regenerate `tab:schema-a-new-detail` and the SANS body numbers.

Schema A New System (SANS) is the matched non-duplicating control:
identical prompt template with the extra-payload occurrence of $y$
removed from the recursive RHS. On this variant direct whole-term and
polynomial methods *do* become adequate, so the math-validity gate
expands to the broader acceptable set.

Reproduces the SANS appendix detail table plus the body 6.1 numbers:
74/108 first-turn yes, 73/108 math-valid, 55/108 admissible, 104/108
self-reporting outside-boundary, 91/108 post-audit still-SN, and the
selected method classes.

Source CSV:
  * schema-test-A-new-system-tests.csv  (n=108)

Field mapping is identical to Schema A, but the SANS answer-key rule
broadens the math-validity set to include direct whole-term and
polynomial methods, since those become adequate once the duplicating
wrapper is removed. `turn2_q4_still_sn` records the post-audit
termination verdict after the boundary follow-up.
"""
from __future__ import annotations

from collections import Counter
from datetime import date
from pathlib import Path

from _common import assert_n, load_csv, md_table, pct


OUTPUT_PATH = Path(__file__).with_suffix(".md")


def main() -> None:
    rows = load_csv("schema-test-A-new-system-tests.csv")
    assert_n(rows, 108, "Schema A New System")
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
    direct_measure = method_counts.get("direct_measure", 0)
    structural_descent = method_counts.get("structural_descent", 0)
    polynomial = method_counts.get("polynomial", 0)
    path_order = method_counts.get("path_order", 0)
    structural_induction = method_counts.get("structural_induction", 0)
    transformed_calls = method_counts.get("transformed_calls", 0)

    lines: list[str] = []
    lines.append("# Schema A New System Numbers (PRT manuscript: tab:schema-a-new-detail and body 6.1)")
    lines.append("")
    lines.append(f"- Generated: {date.today().isoformat()}")
    lines.append("- Reproduces: appendix `tab:schema-a-new-detail` plus the SANS body-prose numbers in section 6.1.")
    lines.append("- Denominator: n=108 (matched non-duplicating control variant).")
    lines.append("")
    lines.append("## Source fields")
    lines.append("")
    lines.append(
        "Same column names as Schema A, but the math-validity gate uses the "
        "broader SANS answer key: direct whole-term, polynomial, and KBO "
        "methods are mathematically adequate on the non-duplicating variant. "
        "Boundary-admissibility still requires the rule-extracted route.\n"
        "- `turn2_q4_still_sn` == yes: post-audit SN verdict after the "
        "boundary follow-up."
    )
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
    method_rows = [
        ["direct_measure (now adequate on this non-duplicating variant)",
         direct_measure, pct(direct_measure, n)],
        ["structural_descent", structural_descent, pct(structural_descent, n)],
        ["polynomial", polynomial, pct(polynomial, n)],
        ["path_order", path_order, pct(path_order, n)],
        ["structural_induction", structural_induction, pct(structural_induction, n)],
        ["transformed_calls", transformed_calls, pct(transformed_calls, n)],
    ]
    lines.append(md_table(["Method class", "Count", "Rate"], method_rows))
    lines.append("")

    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
