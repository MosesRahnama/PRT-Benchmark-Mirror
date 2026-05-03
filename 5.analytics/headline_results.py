"""Regenerate Table 2 (`tab:headline-results`) of the PRT NeurIPS paper.

This is the body table that organizes the open-ended cascade
(Truth -> Adequate -> Admissible) on Test 01 plus both Schema variants,
the closed-menu Schema B summary, and three diagnostic contrasts.

Source CSVs (all in `../6.extracted-data/csv/`):
  * test-01-kernel-tests.csv             (n=324: 162 KO7 + 162 Fruit)
  * schema-test-A-tests.csv           (n=108)
  * schema-test-A-new-system-tests.csv (n=108)
  * schema-test-B-tests.csv (n=108)
  * test-02-completion-tests-nat-lex.csv             (n=108)
  * test-05-candidate-class-reasoning-tests.csv             (n=108)

Field-level mapping to the manuscript:

  Cascade columns
    * Truth      = `sn_verdict` (Test 01) / `turn1_sn_verdict` (Schema A,
                   Schema A New System) equals "yes". This is the
                   correct termination verdict for every kernel in the
                   cascade.
    * Adequate   = `method_mathematical_validity` (Test 01) /
                   `turn1_method_mathematical_validity` (Schema A,
                   Schema A New System) equals "Correct". The named
                   method is mathematically sound on the kernel.
    * Admissible = `method_correct_and_admissible` (Test 01) /
                   `turn1_method_correct_and_admissible` (Schema A,
                   Schema A New System) equals "Correct". The method is
                   also rule-extracted (boundary-admissible).

  Closed-menu rows (Schema B, n=108)
    * Method D yes/yes = `method_D_terminates`=='yes' AND
                         `method_D_in_boundary`=='yes'
    * Method A yes/yes = `method_A_terminates`=='yes' AND
                         `method_A_in_boundary`=='yes'
    * Method B yes/yes = `method_B_terminates`=='yes' AND
                         `method_B_in_boundary`=='yes'
    * Full five-method answer table correct = all five per-method axes
      match gold AND `norm_both_methods_count`=='1' AND
      `norm_both_methods_has_D`=='1' AND has_A/B/C/E=='0'. Schema B
      gold: A=yes/no, B=no/no, C=no/no, D=yes/yes, E=no/no, set={D}.

  Diagnostic gaps
    * Recognition vs retrieval: Schema B Method D yes/yes (104) vs
      Schema A turn-1 admissible (2). Difference in percentage points.
    * Hidden vs explicit obstruction: Test 02 strict
      (`overall_test02_correctness`==Correct, 14) vs Test 05 strict
      (`overall_test05_correctness`==Correct, 98). Difference in pts.
    * SANS admissible self-audit gap: of the 55 SANS sessions where
      `turn1_method_correct_and_admissible`==Correct, count those whose
      `turn2_q3_outside_boundary`=='yes'. The paper reports 51 of 55.
"""
from __future__ import annotations

from datetime import date
from pathlib import Path

from _common import assert_n, load_csv, md_table, pct


OUTPUT_PATH = Path(__file__).with_suffix(".md")

SCHEMA_B_GOLD = {
    "A": ("yes", "no"),
    "B": ("no", "no"),
    "C": ("no", "no"),
    "D": ("yes", "yes"),
    "E": ("no", "no"),
}


def is_full_schema_b_correct(row: dict[str, str]) -> bool:
    for method, (gold_t, gold_b) in SCHEMA_B_GOLD.items():
        if row[f"method_{method}_terminates"] != gold_t:
            return False
        if row[f"method_{method}_in_boundary"] != gold_b:
            return False
    if row["norm_both_methods_count"] != "1":
        return False
    if row["norm_both_methods_has_D"] != "1":
        return False
    for method in ("A", "B", "C", "E"):
        if row[f"norm_both_methods_has_{method}"] != "0":
            return False
    return True


def main() -> None:
    test01 = load_csv("test-01-kernel-tests.csv")
    schema_a = load_csv("schema-test-A-tests.csv")
    sans = load_csv("schema-test-A-new-system-tests.csv")
    schema_b = load_csv("schema-test-B-tests.csv")
    test02 = load_csv("test-02-completion-tests-nat-lex.csv")
    test05 = load_csv("test-05-candidate-class-reasoning-tests.csv")

    assert_n(test01, 324, "Test 01")
    assert_n(schema_a, 108, "Schema A")
    assert_n(sans, 108, "Schema A New System")
    assert_n(schema_b, 108, "Schema B")
    assert_n(test02, 108, "Test 02")
    assert_n(test05, 108, "Test 05")

    # Cascade rows
    cascade_rows: list[list[object]] = []

    def cascade_row(label: str, rows: list[dict[str, str]], n: int,
                    col_truth: str, col_math: str, col_adm: str) -> list[object]:
        truth = sum(1 for r in rows if r[col_truth] == "yes")
        math = sum(1 for r in rows if r[col_math] == "Correct")
        adm = sum(1 for r in rows if r[col_adm] == "Correct")
        gap_pts = 100 * adm / n - 100 * truth / n
        return [
            label,
            f"{truth} ({pct(truth, n)})",
            f"{math} ({pct(math, n)})",
            f"{adm} ({pct(adm, n)})",
            f"{gap_pts:+.1f} pts",
        ]

    cascade_rows.append(cascade_row(
        "Test 01 (KO7 + Fruit, n=324)", test01, 324,
        "sn_verdict", "method_mathematical_validity", "method_correct_and_admissible",
    ))
    cascade_rows.append(cascade_row(
        "Schema A (duplicating, n=108)", schema_a, 108,
        "turn1_sn_verdict", "turn1_method_mathematical_validity",
        "turn1_method_correct_and_admissible",
    ))
    cascade_rows.append(cascade_row(
        "Schema A New System (control, n=108)", sans, 108,
        "turn1_sn_verdict", "turn1_method_mathematical_validity",
        "turn1_method_correct_and_admissible",
    ))

    # Closed-menu rows on Schema B
    def both_axes(rows: list[dict[str, str]], method: str) -> int:
        gold_t, gold_b = SCHEMA_B_GOLD[method]
        return sum(1 for r in rows
                   if r[f"method_{method}_terminates"] == "yes"
                   and r[f"method_{method}_in_boundary"] == "yes")

    method_d_correct = both_axes(schema_b, "D")
    method_a_yesyes = both_axes(schema_b, "A")
    method_b_yesyes = both_axes(schema_b, "B")
    full_correct = sum(1 for r in schema_b if is_full_schema_b_correct(r))

    closed_rows = [
        ["Method D accepted yes/yes (terminates, in-boundary; gold)",
         method_d_correct, pct(method_d_correct, 108)],
        ["Method A (path order) accepted yes/yes (gold yes/no)",
         method_a_yesyes, pct(method_a_yesyes, 108)],
        ["Method B (polynomial) accepted yes/yes (gold no/no)",
         method_b_yesyes, pct(method_b_yesyes, 108)],
        ["Full five-method answer table correct",
         full_correct, pct(full_correct, 108)],
    ]

    # Diagnostic contrasts
    schema_a_admissible = sum(
        1 for r in schema_a if r["turn1_method_correct_and_admissible"] == "Correct"
    )
    rec_vs_ret_gap = (method_d_correct - schema_a_admissible) / 108 * 100

    test02_correct = sum(1 for r in test02 if r["overall_test02_correctness"] == "Correct")
    test05_correct = sum(1 for r in test05 if r["overall_test05_correctness"] == "Correct")
    hidden_vs_explicit_gap = (test05_correct - test02_correct) / 108 * 100

    sans_admissible = [r for r in sans
                       if r["turn1_method_correct_and_admissible"] == "Correct"]
    sans_admissible_n = len(sans_admissible)
    sans_admissible_outside = sum(
        1 for r in sans_admissible if r["turn2_q3_outside_boundary"] == "yes"
    )

    diagnostic_rows = [
        ["Recognition vs open-ended retrieval (Schema B Method D / Schema A admissible)",
         f"{method_d_correct} vs {schema_a_admissible}",
         f"{rec_vs_ret_gap:+.1f} pts"],
        ["Hidden vs explicit obstruction (Test 02 strict / Test 05 strict)",
         f"{test02_correct} vs {test05_correct}",
         f"{hidden_vs_explicit_gap:+.1f} pts"],
        ["Schema A New System admissible rows still self-audit outside-boundary",
         f"{sans_admissible_outside} of {sans_admissible_n}",
         pct(sans_admissible_outside, sans_admissible_n)],
    ]

    # Assemble markdown
    lines: list[str] = []
    lines.append("# Headline Results (PRT Table 2)")
    lines.append("")
    lines.append(f"- Generated: {date.today().isoformat()}")
    lines.append(f"- Reproduces: `tab:headline-results` in the NeurIPS manuscript.")
    lines.append("")
    lines.append("## What this table shows")
    lines.append("")
    lines.append(
        "The truth-to-admissibility cascade on the three open-ended surfaces, "
        "the closed-menu Schema B summary, and three diagnostic contrasts. "
        "Each cascade column counts sessions whose stored verdict column "
        "matches gold; rates use fixed denominators (n=324 for Test 01, "
        "n=108 for each Schema task). Recognition-vs-retrieval and "
        "hidden-vs-explicit contrasts are reported as percentage-point gaps."
    )
    lines.append("")
    lines.append("## Source fields")
    lines.append("")
    lines.append(
        "- **Truth**: `sn_verdict` (Test 01) / `turn1_sn_verdict` (Schema A, SANS) == `yes`.\n"
        "- **Adequate**: `method_mathematical_validity` / `turn1_method_mathematical_validity` == `Correct`.\n"
        "- **Admissible**: `method_correct_and_admissible` / `turn1_method_correct_and_admissible` == `Correct`.\n"
        "- **Schema B Method X yes/yes**: `method_X_terminates` == `yes` AND `method_X_in_boundary` == `yes`.\n"
        "- **Full five-method correct**: all 10 per-method axes match gold AND the 6 selection-set fields match `{D}` alone.\n"
        "- **SANS outside-boundary self-audit**: `turn2_q3_outside_boundary` == `yes`, restricted to the 55 admissible SANS rows."
    )
    lines.append("")
    lines.append("## Open-ended cascade")
    lines.append("")
    lines.append(md_table(
        ["Surface", "Truth", "Adequate", "Admissible", "Truth -> adm. gap"],
        cascade_rows,
    ))
    lines.append("")
    lines.append("## Closed-menu task (Schema B)")
    lines.append("")
    lines.append(md_table(["Signal", "Count", "Rate"], closed_rows))
    lines.append("")
    lines.append("## Diagnostic gaps and contrasts")
    lines.append("")
    lines.append(md_table(["Signal", "Comparison", "Rate / gap"], diagnostic_rows))
    lines.append("")

    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
