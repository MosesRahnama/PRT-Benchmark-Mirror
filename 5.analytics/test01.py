"""Regenerate every Test 01 number reported in the PRT NeurIPS paper.

This single script reproduces:
  * `tab:t01-consolidated` (body Table 3): SN verdict yes/no, the
    "yes with mathematically false method" composite, and the
    transformed-call admissible row split by KO7 / Fruit condition.
  * `tab:t01-overall` (Appendix C): the full SN verdict distribution,
    the two derived verdict columns, and the six selected proof-method
    classes.
  * Body prose numbers in section 6.1.1 not directly tabulated: the
    231/324 in-boundary self-certifications, the 3/231 actually
    admissible among self-certifiers, and the 175/324 false-yes count
    used in the abstract and introduction.

Source CSV:
  * test-01-kernel-tests.csv  (n=324: 162 KO7 regular + 162 Fruit
                                    control)

Field mapping:
  * `prompt_variant`: "regular" => KO7, "control" => Fruit. (162 each.)
  * `sn_verdict` in {yes, no, unclear}: model's termination verdict.
  * `method_mathematical_validity` == "Correct" iff the named method
    class is mathematically adequate (path_order or transformed_calls).
  * `method_correct_and_admissible` == "Correct" iff the method class
    is also rule-extracted (transformed_calls only on this kernel).
  * `norm_primary_method_method_class`: canonical method-class label.
  * `claims_method_in_boundary` == "yes": the Turn-1 self-certification
    that the named method is in-boundary.

The "yes with mathematically false method" composite counts sessions
where `sn_verdict` == "yes" AND `method_mathematical_validity` ==
"Incorrect". This is the abstract's 175/324 (54.0%) figure.
"""
from __future__ import annotations

from collections import Counter
from datetime import date
from pathlib import Path

from _common import assert_n, load_csv, md_table, pct


OUTPUT_PATH = Path(__file__).with_suffix(".md")


def main() -> None:
    rows = load_csv("test-01-kernel-tests.csv")
    assert_n(rows, 324, "Test 01")

    ko7 = [r for r in rows if r["prompt_variant"] == "regular"]
    fruit = [r for r in rows if r["prompt_variant"] == "control"]
    assert_n(ko7, 162, "Test 01 KO7 condition")
    assert_n(fruit, 162, "Test 01 Fruit condition")

    n = 324

    # SN verdict distribution
    verdict_counts = Counter(r["sn_verdict"] for r in rows)
    sn_yes = verdict_counts.get("yes", 0)
    sn_no = verdict_counts.get("no", 0)
    sn_unclear = verdict_counts.get("unclear", 0)

    # False-yes composite (abstract / intro headline)
    false_yes = sum(
        1 for r in rows
        if r["sn_verdict"] == "yes"
        and r["method_mathematical_validity"] == "Incorrect"
    )

    # Method-class distribution
    method_counts = Counter(r["norm_primary_method_method_class"] for r in rows)
    direct_measure = method_counts.get("direct_measure", 0)
    path_order = method_counts.get("path_order", 0)
    polynomial = method_counts.get("polynomial", 0)
    structural_induction = method_counts.get("structural_induction", 0)
    structural_descent = method_counts.get("structural_descent", 0)
    transformed_calls = method_counts.get("transformed_calls", 0)

    # Transformed_calls split by condition
    transformed_ko7 = sum(
        1 for r in ko7 if r["norm_primary_method_method_class"] == "transformed_calls"
    )
    transformed_fruit = sum(
        1 for r in fruit if r["norm_primary_method_method_class"] == "transformed_calls"
    )

    # Derived verdict columns
    math_correct = sum(1 for r in rows if r["method_mathematical_validity"] == "Correct")
    adm_correct = sum(1 for r in rows if r["method_correct_and_admissible"] == "Correct")

    # Boundary self-certification (body prose)
    in_boundary_self = sum(1 for r in rows if r["claims_method_in_boundary"] == "yes")
    in_boundary_self_admissible = sum(
        1 for r in rows
        if r["claims_method_in_boundary"] == "yes"
        and r["method_correct_and_admissible"] == "Correct"
    )

    # Build markdown
    lines: list[str] = []
    lines.append("# Test 01 Numbers (PRT manuscript: tab:t01-consolidated, tab:t01-overall, body 6.1.1)")
    lines.append("")
    lines.append(f"- Generated: {date.today().isoformat()}")
    lines.append("- Reproduces: body Table 3 (`tab:t01-consolidated`), Appendix Table (`tab:t01-overall`), and the body-prose numbers in section 6.1.1.")
    lines.append("- Denominators: total n=324 (KO7 regular = 162, Fruit control = 162).")
    lines.append("")

    lines.append("## Body Table 3: consolidated distribution")
    lines.append("")
    lines.append(
        "Headline rows reported in the body. The 'yes with mathematically false method' "
        "composite is the conjunction `sn_verdict == 'yes'` AND "
        "`method_mathematical_validity == 'Incorrect'`. The transformed-call "
        "admissible row splits by condition because the manuscript reports a "
        "directional gap (3 retrievals on KO7, 0 on Fruit)."
    )
    lines.append("")
    consolidated_rows = [
        ["SN verdict 'yes' (truth correct)", sn_yes, pct(sn_yes, n)],
        ["'Yes' verdict with a mathematically false method", false_yes, pct(false_yes, n)],
        ["Primary method: dependency pairs / subterm criterion (W2)",
         transformed_calls, pct(transformed_calls, n)],
        ["  of which KO7 condition", transformed_ko7, pct(transformed_ko7, 162)],
        ["  of which Fruit condition", transformed_fruit, pct(transformed_fruit, 162)],
    ]
    lines.append(md_table(["Signal", "Count", "Rate"], consolidated_rows))
    lines.append("")

    lines.append("## Appendix `tab:t01-overall`: full distribution")
    lines.append("")
    lines.append(
        "The complete verdict and method-class breakdown, n=324. "
        "`method_class` of `path_order` and `transformed_calls` count as "
        "mathematically adequate; only `transformed_calls` is also "
        "boundary-admissible. Polynomial is excluded from the adequate set "
        "on this kernel by the Lean theorem `test1_polynomial_not_adequate` "
        "and the archived TTT2 certificate `KO7_POLY.cpf`."
    )
    lines.append("")
    overall_rows = [
        ["sn_verdict = yes", sn_yes, pct(sn_yes, n)],
        ["sn_verdict = no", sn_no, pct(sn_no, n)],
        ["sn_verdict = unclear", sn_unclear, pct(sn_unclear, n)],
        ["method_mathematical_validity = Correct", math_correct, pct(math_correct, n)],
        ["method_correct_and_admissible = Correct", adm_correct, pct(adm_correct, n)],
        ["direct_measure (W0, mathematically false on this kernel)",
         direct_measure, pct(direct_measure, n)],
        ["path_order (W1, adequate by class, boundary-external)",
         path_order, pct(path_order, n)],
        ["polynomial (W1, mathematically false, boundary-external)",
         polynomial, pct(polynomial, n)],
        ["structural_induction (W0, mathematically false)",
         structural_induction, pct(structural_induction, n)],
        ["structural_descent (W0, mathematically false)",
         structural_descent, pct(structural_descent, n)],
        ["transformed_calls (W2, correct and admissible)",
         transformed_calls, pct(transformed_calls, n)],
    ]
    lines.append(md_table(["Field and value", "Count", "Rate"], overall_rows))
    lines.append("")

    lines.append("## Body 6.1.1: boundary self-report layer")
    lines.append("")
    lines.append(
        "The body claim 'only 3/231 are actually admissible' restricts to "
        "sessions whose Turn-1 `claims_method_in_boundary` equals 'yes', "
        "then counts how many of those carry "
        "`method_correct_and_admissible == 'Correct'`."
    )
    lines.append("")
    self_audit_rows = [
        ["Sessions self-certifying as in-boundary", in_boundary_self, pct(in_boundary_self, n)],
        ["  of which actually admissible",
         in_boundary_self_admissible, pct(in_boundary_self_admissible, in_boundary_self)],
    ]
    lines.append(md_table(["Signal", "Count", "Rate"], self_audit_rows))
    lines.append("")

    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
