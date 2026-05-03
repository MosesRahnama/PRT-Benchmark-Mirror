"""Regenerate `tab:t04` and the Test 04 body numbers.

Test 04 supplies an unsound (phase, cost) lexicographic measure whose
actual failure is on the non-recursive `R_merge_void_left` rule via a
phase-exposure (wrapper-removal) branch. The recursive successor rule
`R_rec_succ` actually decreases the supplied measure on nested
`delta (delta void)`, so it is a salience decoy.

Reproduces the appendix table plus the body 6.2 numbers: 84/108 get
the unsound verdict right, 75/108 localize phase exposure, 74/108 get
both, and the decoy-only count of 33/108 (cite `R_rec_succ` without
phase exposure).

Source CSV:
  * test-04-measure-verification-tests.csv  (n=108)

Field mapping:
  * `measure_sound_correctness` == "Correct" iff the response correctly
    judges the supplied measure unsound.
  * `phase_exposure_localization_correctness` == "Correct" iff the
    response localizes the failure to the phase-exposure branch.
  * `overall_test04_correctness` == "Correct" iff both the unsound
    verdict and the phase-exposure localization match gold.
  * The decoy-only count uses the conjunction
    `r_rec_succ_cited == 'yes'` AND
    `phase_exposure_localization_correctness != 'Correct'`.
"""
from __future__ import annotations

from datetime import date
from pathlib import Path

from _common import assert_n, load_csv, md_table, pct


OUTPUT_PATH = Path(__file__).with_suffix(".md")


def main() -> None:
    rows = load_csv("test-04-measure-verification-tests.csv")
    assert_n(rows, 108, "Test 04")
    n = 108

    measure_sound = sum(
        1 for r in rows if r["measure_sound_correctness"] == "Correct"
    )
    phase_exposure = sum(
        1 for r in rows if r["phase_exposure_localization_correctness"] == "Correct"
    )
    overall_correct = sum(
        1 for r in rows if r["overall_test04_correctness"] == "Correct"
    )
    decoy_only = sum(
        1 for r in rows
        if r["r_rec_succ_cited"] == "yes"
        and r["phase_exposure_localization_correctness"] != "Correct"
    )

    lines: list[str] = []
    lines.append("# Test 04 Numbers (PRT manuscript: tab:t04 and body 6.2)")
    lines.append("")
    lines.append(f"- Generated: {date.today().isoformat()}")
    lines.append("- Reproduces: appendix `tab:t04` and the Test 04 body-prose numbers in section 6.2.")
    lines.append("- Denominator: n=108.")
    lines.append("")
    lines.append("## Source fields")
    lines.append("")
    lines.append(
        "- `measure_sound_correctness` == Correct iff the response correctly "
        "judges the supplied measure unsound.\n"
        "- `phase_exposure_localization_correctness` == Correct iff the "
        "response localizes to the wrapper-exposure (phase-exposure) branch.\n"
        "- `overall_test04_correctness` == Correct iff both axes match gold.\n"
        "- Decoy-only conjunction: `r_rec_succ_cited == 'yes'` AND "
        "`phase_exposure_localization_correctness != 'Correct'`. This is the "
        "33/108 (30.6%) figure in the body."
    )
    lines.append("")
    table_rows = [
        ["measure_sound_correctness = Correct (measure is unsound)",
         measure_sound, pct(measure_sound, n)],
        ["phase_exposure_localization_correctness = Correct",
         phase_exposure, pct(phase_exposure, n)],
        ["overall_test04_correctness = Correct",
         overall_correct, pct(overall_correct, n)],
        ["Decoy-only (R_rec_succ cited without phase exposure)",
         decoy_only, pct(decoy_only, n)],
    ]
    lines.append(md_table(["Field and value", "Count", "Rate"], table_rows))
    lines.append("")

    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
