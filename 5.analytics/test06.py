"""Regenerate `tab:t06` and the Test 06 body numbers.

Test 06 supplies a helper strategy whose claimed metric drop is false
on the nested case `kappa_rec_delta_step`. The correct response judges
the strategy unsound and diagnoses the nested-delta branch.

Reproduces the appendix table plus the body 6.2 numbers: 77/108
unsound verdict, 74/108 nested-delta diagnosis, 58/108 overall.

Source CSV:
  * test-06-branch-realism-tests.csv  (n=108)

Field mapping:
  * `strategy_sound_correctness` == "Correct" iff the response judges
    the strategy unsound.
  * `nested_delta_branch_diagnosis_correctness` == "Correct" iff the
    nested-delta branch is correctly named.
  * `kappa_rec_delta_step_correctness` == "Correct" iff the response
    correctly identifies that this step is false.
  * `overall_test06_correctness` == "Correct" iff both the unsound
    verdict and the nested-delta diagnosis match gold.
"""
from __future__ import annotations

from datetime import date
from pathlib import Path

from _common import assert_n, load_csv, md_table, pct


OUTPUT_PATH = Path(__file__).with_suffix(".md")


def main() -> None:
    rows = load_csv("test-06-branch-realism-tests.csv")
    assert_n(rows, 108, "Test 06")
    n = 108

    strategy_correct = sum(
        1 for r in rows if r["strategy_sound_correctness"] == "Correct"
    )
    delta_step_correct = sum(
        1 for r in rows if r["kappa_rec_delta_step_correctness"] == "Correct"
    )
    nested_delta = sum(
        1 for r in rows if r["nested_delta_branch_diagnosis_correctness"] == "Correct"
    )
    overall_correct = sum(
        1 for r in rows if r["overall_test06_correctness"] == "Correct"
    )

    lines: list[str] = []
    lines.append("# Test 06 Numbers (PRT manuscript: tab:t06 and body 6.2)")
    lines.append("")
    lines.append(f"- Generated: {date.today().isoformat()}")
    lines.append("- Reproduces: appendix `tab:t06` and the Test 06 body-prose numbers in section 6.2.")
    lines.append("- Denominator: n=108.")
    lines.append("")
    lines.append("## Source fields")
    lines.append("")
    lines.append(
        "- `strategy_sound_correctness` == Correct iff the response judges "
        "the helper strategy unsound (gold = unsound).\n"
        "- `kappa_rec_delta_step_correctness` == Correct iff the response "
        "correctly identifies that the helper's claimed metric drop on "
        "`kappa_rec_delta_step` is false.\n"
        "- `nested_delta_branch_diagnosis_correctness` == Correct iff the "
        "nested-delta branch is correctly named as the failure point.\n"
        "- `overall_test06_correctness` == Correct iff both the unsound "
        "verdict and the nested-delta diagnosis match gold."
    )
    lines.append("")
    table_rows = [
        ["strategy_sound_correctness = Correct (strategy unsound)",
         strategy_correct, pct(strategy_correct, n)],
        ["kappa_rec_delta_step_correctness = Correct",
         delta_step_correct, pct(delta_step_correct, n)],
        ["nested_delta_branch_diagnosis_correctness = Correct",
         nested_delta, pct(nested_delta, n)],
        ["overall_test06_correctness = Correct",
         overall_correct, pct(overall_correct, n)],
    ]
    lines.append(md_table(["Field and value", "Count", "Rate"], table_rows))
    lines.append("")

    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
