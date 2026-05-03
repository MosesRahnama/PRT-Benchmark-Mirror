"""Regenerate `tab:t02` and the Test 02 body numbers.

Test 02 supplies a natural-number lexicographic measure scaffold on
KO7. The scaffold is mathematically broken at the recursive successor
rule, so the correct `completion_claim` is "no" and the correct
`rec_succ_obstruction_diagnosis` cites `R_rec_succ`.

Reproduces the appendix table plus the body 6.2 numbers: 67/108
endorse, 27/108 partial, 14/108 reject; 15/108 localize the
obstruction; 0/67 among scaffold acceptors localize it.

Source CSV:
  * test-02-completion-tests-nat-lex.csv  (n=108)

Field mapping:
  * `completion_claim` in {yes, partial, no}: model's claim about
    whether the scaffold can be completed. Gold = no.
  * `rec_succ_obstruction_diagnosis_correctness` == "Correct" iff the
    response correctly localizes the obstruction to `R_rec_succ`.
  * `overall_test02_correctness` == "Correct" iff both the rejection
    and the localization match gold.
"""
from __future__ import annotations

from collections import Counter
from datetime import date
from pathlib import Path

from _common import assert_n, load_csv, md_table, pct


OUTPUT_PATH = Path(__file__).with_suffix(".md")


def main() -> None:
    rows = load_csv("test-02-completion-tests-nat-lex.csv")
    assert_n(rows, 108, "Test 02")
    n = 108

    claim_counts = Counter(r["completion_claim"] for r in rows)
    claim_no = claim_counts.get("no", 0)
    claim_partial = claim_counts.get("partial", 0)
    claim_yes = claim_counts.get("yes", 0)

    obstruction_correct = sum(
        1 for r in rows if r["rec_succ_obstruction_diagnosis_correctness"] == "Correct"
    )
    overall_correct = sum(
        1 for r in rows if r["overall_test02_correctness"] == "Correct"
    )

    # Among scaffold acceptors (`completion_claim` = yes), how many localize?
    acceptors = [r for r in rows if r["completion_claim"] == "yes"]
    acceptors_localizing = sum(
        1 for r in acceptors if r["rec_succ_obstruction_diagnosis_correctness"] == "Correct"
    )

    lines: list[str] = []
    lines.append("# Test 02 Numbers (PRT manuscript: tab:t02 and body 6.2)")
    lines.append("")
    lines.append(f"- Generated: {date.today().isoformat()}")
    lines.append("- Reproduces: appendix `tab:t02` and the Test 02 body-prose numbers in section 6.2.")
    lines.append("- Denominator: n=108.")
    lines.append("")
    lines.append("## Source fields")
    lines.append("")
    lines.append(
        "- `completion_claim` in {yes, partial, no}: gold = no.\n"
        "- `rec_succ_obstruction_diagnosis_correctness` == Correct iff the "
        "session names `R_rec_succ` (or its renamed equivalent) as the obstruction.\n"
        "- `overall_test02_correctness` == Correct iff both the rejection and "
        "the localization match gold."
    )
    lines.append("")
    table_rows = [
        ["completion_claim = no (rejects broken scaffold)",
         "correct", claim_no, pct(claim_no, n)],
        ["completion_claim = partial",
         "off-gold", claim_partial, pct(claim_partial, n)],
        ["completion_claim = yes (endorses broken scaffold)",
         "off-gold", claim_yes, pct(claim_yes, n)],
        ["rec_succ_obstruction_diagnosis_correctness = Correct",
         "correct", obstruction_correct, pct(obstruction_correct, n)],
        ["overall_test02_correctness = Correct",
         "correct", overall_correct, pct(overall_correct, n)],
    ]
    lines.append(md_table(["Field and value", "Verdict", "Count", "Rate"], table_rows))
    lines.append("")
    lines.append("## Body claim: 0/67 acceptors localize the obstruction")
    lines.append("")
    lines.append(
        "Restricting to the subset of sessions whose `completion_claim` "
        "equals `yes` (the scaffold acceptors), how many also satisfy "
        "`rec_succ_obstruction_diagnosis_correctness == 'Correct'`."
    )
    lines.append("")
    sub_rows = [
        ["Scaffold acceptors", len(acceptors), pct(len(acceptors), n)],
        ["  of which localize R_rec_succ",
         acceptors_localizing,
         pct(acceptors_localizing, len(acceptors)) if acceptors else "-"],
    ]
    lines.append(md_table(["Signal", "Count", "Rate"], sub_rows))
    lines.append("")

    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
