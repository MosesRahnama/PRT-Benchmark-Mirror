"""Regenerate the three Schema B tables and Schema B body numbers.

This single script reproduces:
  * `tab:schema-b-per-method`: the compact 5-row method summary
    (gold status, both axes correct, yes/yes accepted, interpretation
    text). The interpretation text is editorial and not regenerated.
  * `tab:schema-b-method-sets`: the accepted method-set distribution
    with a tail collapse to "Other" for sets with <=3 sessions.
  * `tab:schema-b-variant`: regular vs. control prompt-variant split,
    n=54 each.
  * Body 6.2 numbers: the modal accepted set count, the 104 D-correct
    sessions, and the various method-axis acceptance counts.

Source CSV:
  * schema-test-B-tests.csv  (n=108: regular=54,
                                                 control=54)

Field mapping:
  * `method_X_terminates` for X in {A,B,C,D,E}: per-method
    termination-success axis, in {yes, no, unclear}.
  * `method_X_in_boundary` for X in {A,B,C,D,E}: per-method
    boundary-admissibility axis, in {yes, no, moot, unclear}.
  * `prompt_variant`: regular (n=54) or control (n=54).
  * `norm_both_methods_count`, `norm_both_methods_has_X`: the six-tuple
    encoding the session's final accepted method set.

Schema B answer-key gold values:
  * A: terminates=yes, in_boundary=no
  * B: terminates=no,  in_boundary=no
  * C: terminates=no,  in_boundary=no
  * D: terminates=yes, in_boundary=yes
  * E: terminates=no,  in_boundary=no
  * Final accepted set: {D} alone.
"""
from __future__ import annotations

from collections import Counter
from datetime import date
from pathlib import Path

from _common import assert_n, load_csv, md_table, pct


OUTPUT_PATH = Path(__file__).with_suffix(".md")

GOLD = {
    "A": ("yes", "no"),
    "B": ("no", "no"),
    "C": ("no", "no"),
    "D": ("yes", "yes"),
    "E": ("no", "no"),
}


def both_axes_correct(row: dict[str, str], method: str) -> bool:
    gold_t, gold_b = GOLD[method]
    return (row[f"method_{method}_terminates"] == gold_t
            and row[f"method_{method}_in_boundary"] == gold_b)


def yes_yes_accepted(row: dict[str, str], method: str) -> bool:
    return (row[f"method_{method}_terminates"] == "yes"
            and row[f"method_{method}_in_boundary"] == "yes")


def method_set(row: dict[str, str]) -> str:
    members = [m for m in "ABCDE" if row[f"norm_both_methods_has_{m}"] == "1"]
    if not members:
        return "{} (empty)"
    return "{" + ", ".join(members) + "}"


def main() -> None:
    rows = load_csv("schema-test-B-tests.csv")
    assert_n(rows, 108, "Schema B")

    regular = [r for r in rows if r["prompt_variant"] == "regular"]
    control = [r for r in rows if r["prompt_variant"] == "control"]
    assert_n(regular, 54, "Schema B regular")
    assert_n(control, 54, "Schema B control")

    n = 108

    # ----- per-method compact summary ------------------------------------
    per_method_rows: list[list[object]] = []
    interpretations = {
        "A": "path-order recognized but boundary overaccepted",
        "B": "polynomial false rival accepted",
        "C": "KBO mostly rejected",
        "D": "correct method recognized when supplied",
        "E": "direct-measure false rival accepted",
    }
    gold_status_text = {
        "A": "method succeeds, boundary no",
        "B": "method fails, boundary no",
        "C": "method fails, boundary no",
        "D": "method succeeds, boundary yes",
        "E": "method fails, boundary no",
    }
    for method in "ABCDE":
        both = sum(1 for r in rows if both_axes_correct(r, method))
        yy = sum(1 for r in rows if yes_yes_accepted(r, method))
        per_method_rows.append([
            method,
            gold_status_text[method],
            both,
            yy,
            interpretations[method],
        ])

    full_correct = sum(
        1 for r in rows
        if all(both_axes_correct(r, m) for m in "ABCDE")
        and r["norm_both_methods_count"] == "1"
        and r["norm_both_methods_has_D"] == "1"
        and all(r[f"norm_both_methods_has_{m}"] == "0" for m in "ABCE")
    )
    per_method_rows.append([
        "Full five-method answer table correct",
        "all method rows correct",
        full_correct,
        "-",
        "exclusion discipline fails globally",
    ])

    # ----- method-set distribution ---------------------------------------
    set_counts = Counter(method_set(r) for r in rows)
    main_sets: list[list[object]] = []
    other_total = 0
    other_count = 0
    for label, count in set_counts.most_common():
        if count > 3 or label == "{D}":
            verdict = "correct" if label == "{D}" else "off-gold"
            main_sets.append([label, verdict, count, pct(count, n)])
        else:
            other_total += count
            other_count += 1
    if other_total:
        main_sets.append([
            f"Other method sets (each count <= 3, n={other_count} sets)",
            "off-gold",
            other_total,
            pct(other_total, n),
        ])

    # ----- variant split -------------------------------------------------
    def variant_row(label: str, key_fn) -> list[object]:
        reg = sum(1 for r in regular if key_fn(r))
        con = sum(1 for r in control if key_fn(r))
        return [label, reg, pct(reg, 54), con, pct(con, 54)]

    variant_rows = []
    for method in "ABCDE":
        variant_rows.append(variant_row(
            f"{method} both axes correct",
            lambda r, m=method: both_axes_correct(r, m),
        ))
    variant_rows.append(variant_row(
        "Selection = {D} alone",
        lambda r: (
            r["norm_both_methods_count"] == "1"
            and r["norm_both_methods_has_D"] == "1"
            and all(r[f"norm_both_methods_has_{m}"] == "0" for m in "ABCE")
        ),
    ))
    variant_rows.append(variant_row(
        "All five methods correct",
        lambda r: all(both_axes_correct(r, m) for m in "ABCDE"),
    ))

    # ----- assemble ------------------------------------------------------
    lines: list[str] = []
    lines.append("# Schema B Numbers (PRT manuscript: tab:schema-b-per-method, tab:schema-b-method-sets, tab:schema-b-variant)")
    lines.append("")
    lines.append(f"- Generated: {date.today().isoformat()}")
    lines.append("- Reproduces: the three Schema B appendix tables plus body 6.2 numbers.")
    lines.append("- Denominators: n=108 total, regular=54, control=54.")
    lines.append("")
    lines.append("## Source fields")
    lines.append("")
    lines.append(
        "- `method_X_terminates` for X in A..E: method-level termination-success axis "
        "(does the named method itself soundly prove SN of the schema?).\n"
        "- `method_X_in_boundary` for X in A..E: method-level boundary-admissibility "
        "(is the method admissible under the rule-extracted contract?).\n"
        "- `norm_both_methods_count` and `norm_both_methods_has_X`: the final "
        "accepted-set encoding.\n"
        "- `prompt_variant` in {regular, control}: regular = primary prompt; "
        "control = boundary-clarified rewording.\n"
        "- Gold: A=yes/no, B=no/no, C=no/no, D=yes/yes, E=no/no; final set = {D}."
    )
    lines.append("")
    lines.append("## Per-method compact summary (`tab:schema-b-per-method`)")
    lines.append("")
    lines.append(
        "**Both axes correct**: session matches gold on both `terminates` and "
        "`in_boundary`. **Yes/yes accepted**: session said yes/yes regardless "
        "of gold; for D this is the gold joint-recognition count, for "
        "A/B/C/E it is a false-rival acceptance count."
    )
    lines.append("")
    lines.append(md_table(
        ["Method", "Gold status", "Both axes correct", "Yes/yes accepted", "Interpretation"],
        per_method_rows,
    ))
    lines.append("")
    lines.append("## Accepted method-set distribution (`tab:schema-b-method-sets`)")
    lines.append("")
    lines.append(
        "Final selection counts. Only `{D}` matches gold. Sets with at most "
        "three sessions are aggregated into the `Other` row."
    )
    lines.append("")
    lines.append(md_table(["Method set", "Verdict", "Count", "Rate"], main_sets))
    lines.append("")
    lines.append("## Regular vs. control prompt variant (`tab:schema-b-variant`)")
    lines.append("")
    lines.append(
        "Regular prompt presents the five-method menu under the benchmark "
        "contract; control prompt is a clarified-boundary rewording that does "
        "not change the gold answer."
    )
    lines.append("")
    lines.append(md_table(
        ["Signal", "Regular", "Rate", "Control", "Rate"],
        variant_rows,
    ))
    lines.append("")

    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
