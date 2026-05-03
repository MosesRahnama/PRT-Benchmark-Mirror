"""Regenerate `tab:t03` and the Test 03 body numbers.

Test 03 replaces the broken nat-lex scaffold with an ordinal-valued
one. The scaffold is viable but reduces to two hard residual
obligations on `R_rec_succ` and `R_eq_diff`. The correct posture
delivers the ordinal arithmetic at those rules.

Reproduces the appendix table plus the body 6.2 numbers: 88/108
overall correct, 93/108 hard-case-delivery correct.

Source CSV:
  * test-03-completion-tests-ordinal.csv  (n=108)

Field mapping:
  * `hard_case_delivery_correctness` == "Correct" iff the response
    delivers the ordinal arithmetic at the hard cases.
  * `overall_test03_correctness` == "Correct" iff the overall
    submission addresses the viable scaffold correctly.
"""
from __future__ import annotations

from datetime import date
from pathlib import Path

from _common import assert_n, load_csv, md_table, pct


OUTPUT_PATH = Path(__file__).with_suffix(".md")


def main() -> None:
    rows = load_csv("test-03-completion-tests-ordinal.csv")
    assert_n(rows, 108, "Test 03")
    n = 108

    hard_correct = sum(
        1 for r in rows if r["hard_case_delivery_correctness"] == "Correct"
    )
    overall_correct = sum(
        1 for r in rows if r["overall_test03_correctness"] == "Correct"
    )

    lines: list[str] = []
    lines.append("# Test 03 Numbers (PRT manuscript: tab:t03 and body 6.2)")
    lines.append("")
    lines.append(f"- Generated: {date.today().isoformat()}")
    lines.append("- Reproduces: appendix `tab:t03` and the Test 03 body-prose numbers in section 6.2.")
    lines.append("- Denominator: n=108.")
    lines.append("")
    lines.append("## Source fields")
    lines.append("")
    lines.append(
        "- `hard_case_delivery_correctness` == Correct iff the response delivers "
        "ordinal arithmetic at the hard residual obligations (`R_rec_succ`, "
        "`R_eq_diff`).\n"
        "- `overall_test03_correctness` == Correct iff the overall submission "
        "addresses the viable scaffold correctly."
    )
    lines.append("")
    table_rows = [
        ["hard_case_delivery_correctness = Correct", hard_correct, pct(hard_correct, n)],
        ["overall_test03_correctness = Correct", overall_correct, pct(overall_correct, n)],
    ]
    lines.append(md_table(["Field and value", "Count", "Rate"], table_rows))
    lines.append("")

    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
