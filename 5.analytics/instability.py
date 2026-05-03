"""Regenerate `tab:instability` and the cross-test incoherence numbers.

This is the per-model panel table for Test 01 plus several cross-test
joins. Reproduces:
  * 12/27 models flip their Test 01 sn_verdict across their twelve
    sessions (six KO7 + six Fruit per model).
  * 18/27 models use at least 2 distinct recoverable proof-method
    classes on Test 01.
  * 14/27 models use at least 3 distinct classes.
  * 18/27 models change their KO7-vs-Fruit axis-count tuple
    (termination / math / admissible / W2-named).
  * 18/27 cross-test incoherent models: Test 01 yes via a
    boundary-external or mathematically-false method, AND raw
    endorsement of an unsound Test 04 measure or Test 06 strategy.
  * 3/27 D-alone models on Schema B (final selection set is exactly
    {D}) and 0/3 of those also retrieve transformed_calls in Schema A.

Source CSVs:
  * test-01-kernel-tests.csv          (n=324)
  * schema-test-A-tests.csv        (n=108)
  * schema-test-B-tests.csv (n=108)
  * test-04-measure-verification-tests.csv          (n=108)
  * test-06-branch-realism-tests.csv          (n=108)

Field mapping:
  * Test 01 verdict flip: per model, the set of distinct values of
    `sn_verdict` across the model's 12 Test 01 sessions has more than
    one element, ignoring blank cells.
  * Recoverable method classes: per model, the count of distinct
    `norm_primary_method_method_class` values from the canonical six
    rewriting families {direct_measure, path_order, polynomial,
    structural_induction, structural_descent, transformed_calls}
    across the model's 12 Test 01 sessions. The non-method label
    `objection` is excluded; that is what the paper means by
    "recoverable proof-method class".
  * KO7/Fruit axis-count tuple: per model, the 4-tuple of session
    counts on KO7 vs Fruit for (sn_verdict==yes,
    method_mathematical_validity==Correct,
    method_correct_and_admissible==Correct,
    flag_w2_method_named==yes). The model "changes" the tuple iff the
    KO7 tuple differs from the Fruit tuple.
  * Cross-test incoherence (per model): exists at least one Test 01
    session with `sn_verdict == 'yes'` AND
    `method_correct_and_admissible != 'Correct'` (Test 01 yes through
    a boundary-external or mathematically false method), AND exists
    at least one Test 04 session with `measure_sound_yes_no == 'yes'`
    OR Test 06 session with `strategy_sound_verdict == 'sound'`
    (raw endorsement of a mechanically broken artifact).
  * Schema B D-alone: norm_both_methods_count==1 AND
    norm_both_methods_has_D==1 AND has_A/B/C/E==0.
"""
from __future__ import annotations

from datetime import date
from pathlib import Path

from _common import assert_n, canonical_model, load_csv, md_table, pct


OUTPUT_PATH = Path(__file__).with_suffix(".md")


def main() -> None:
    test01 = load_csv("test-01-kernel-tests.csv")
    schema_a = load_csv("schema-test-A-tests.csv")
    schema_b = load_csv("schema-test-B-tests.csv")
    test04 = load_csv("test-04-measure-verification-tests.csv")
    test06 = load_csv("test-06-branch-realism-tests.csv")

    assert_n(test01, 324, "Test 01")
    assert_n(schema_a, 108, "Schema A")
    assert_n(schema_b, 108, "Schema B")
    assert_n(test04, 108, "Test 04")
    assert_n(test06, 108, "Test 06")

    panel_n = 27

    # Group Test 01 by model
    test01_by_model: dict[str, list[dict[str, str]]] = {}
    for r in test01:
        test01_by_model.setdefault(canonical_model(r["model"]), []).append(r)
    models = sorted(test01_by_model.keys())
    if len(models) != panel_n:
        raise AssertionError(f"Expected 27 models on Test 01, found {len(models)}.")

    # Verdict flip (across all 12 sessions)
    verdict_flip = 0
    for model in models:
        verdicts = {r["sn_verdict"] for r in test01_by_model[model]
                    if (r["sn_verdict"] or "").strip()}
        if len(verdicts) > 1:
            verdict_flip += 1

    # Distinct recoverable method classes per model. The paper's
    # "recoverable" filter restricts to the canonical six rewriting
    # families and excludes the `objection` label (which marks sessions
    # that did not propose a method at all).
    RECOVERABLE = {
        "direct_measure", "path_order", "polynomial",
        "structural_induction", "structural_descent", "transformed_calls",
    }
    classes_two_plus = 0
    classes_three_plus = 0
    for model in models:
        classes = {r["norm_primary_method_method_class"]
                   for r in test01_by_model[model]
                   if r["norm_primary_method_method_class"] in RECOVERABLE}
        if len(classes) >= 2:
            classes_two_plus += 1
        if len(classes) >= 3:
            classes_three_plus += 1

    # KO7-vs-Fruit axis-count tuple change
    axis_tuple_changed = 0
    for model in models:
        ko7_rows = [r for r in test01_by_model[model] if r["prompt_variant"] == "regular"]
        fruit_rows = [r for r in test01_by_model[model] if r["prompt_variant"] == "control"]

        def axis_tuple(rows: list[dict[str, str]]) -> tuple:
            return (
                sum(1 for r in rows if r["sn_verdict"] == "yes"),
                sum(1 for r in rows if r["method_mathematical_validity"] == "Correct"),
                sum(1 for r in rows if r["method_correct_and_admissible"] == "Correct"),
                sum(1 for r in rows if r["flag_w2_method_named"] == "yes"),
            )

        if axis_tuple(ko7_rows) != axis_tuple(fruit_rows):
            axis_tuple_changed += 1

    # Cross-test incoherence
    test04_by_model: dict[str, list[dict[str, str]]] = {}
    for r in test04:
        test04_by_model.setdefault(canonical_model(r["model"]), []).append(r)
    test06_by_model: dict[str, list[dict[str, str]]] = {}
    for r in test06:
        test06_by_model.setdefault(canonical_model(r["model"]), []).append(r)

    cross_incoherent = 0
    for model in models:
        # T01 yes through a boundary-external or mathematically false
        # method = sn_verdict yes AND admissible != Correct. This is
        # broader than "math validity Incorrect" because it also
        # catches path_order rows (boundary-external but math-Correct).
        t01_yes_via_bad = any(
            r["sn_verdict"] == "yes"
            and r["method_correct_and_admissible"] != "Correct"
            for r in test01_by_model[model]
        )
        # Raw endorsement of a mechanically broken artifact: the model
        # says the supplied T04 measure is sound or the T06 strategy is sound.
        t04_unsound_endorsed = any(
            r["measure_sound_yes_no"] == "yes"
            for r in test04_by_model.get(model, [])
        )
        t06_unsound_endorsed = any(
            r["strategy_sound_verdict"] == "sound"
            for r in test06_by_model.get(model, [])
        )
        if t01_yes_via_bad and (t04_unsound_endorsed or t06_unsound_endorsed):
            cross_incoherent += 1

    # Schema B D-alone models
    schema_b_by_model: dict[str, list[dict[str, str]]] = {}
    for r in schema_b:
        schema_b_by_model.setdefault(canonical_model(r["model"]), []).append(r)
    d_alone_models: set[str] = set()
    for model, sessions in schema_b_by_model.items():
        for r in sessions:
            if (r["norm_both_methods_count"] == "1"
                    and r["norm_both_methods_has_D"] == "1"
                    and all(r[f"norm_both_methods_has_{m}"] == "0" for m in "ABCE")):
                d_alone_models.add(model)
                break

    # Of D-alone models, how many ever retrieve transformed_calls in Schema A?
    schema_a_transformed_models: set[str] = set()
    for r in schema_a:
        if r["turn1_norm_primary_method_method_class"] == "transformed_calls":
            schema_a_transformed_models.add(canonical_model(r["model"]))
    d_alone_and_retrieve = len(d_alone_models & schema_a_transformed_models)

    lines: list[str] = []
    lines.append("# Per-Model Instability and Cross-Test Incoherence (PRT manuscript: tab:instability)")
    lines.append("")
    lines.append(f"- Generated: {date.today().isoformat()}")
    lines.append("- Reproduces: appendix `tab:instability` and the cross-test incoherence numbers in section 7.")
    lines.append("- Denominator: 27-model panel.")
    lines.append("")
    lines.append("## Source fields and definitions")
    lines.append("")
    lines.append(
        "- **Verdict flip**: per model, the set of distinct nonblank `sn_verdict` "
        "values across the model's 12 Test 01 sessions has more than one element.\n"
        "- **>=k recoverable method classes**: per model, count of distinct "
        "`norm_primary_method_method_class` values from the canonical six "
        "rewriting families {direct_measure, path_order, polynomial, "
        "structural_induction, structural_descent, transformed_calls} >= k. "
        "The non-method label `objection` is excluded; that is what the paper "
        "means by 'recoverable proof-method class'.\n"
        "- **KO7-vs-Fruit axis tuple change**: 4-tuple of session counts "
        "(sn_verdict yes, math Correct, admissible Correct, "
        "`flag_w2_method_named` yes) differs between the model's 6 KO7 sessions "
        "and 6 Fruit sessions.\n"
        "- **Cross-test incoherent**: exists Test 01 session with "
        "`sn_verdict == 'yes'` AND `method_correct_and_admissible != 'Correct'` "
        "(yes through a boundary-external or mathematically false method), "
        "AND exists Test 04 session with `measure_sound_yes_no == 'yes'` "
        "OR Test 06 session with `strategy_sound_verdict == 'sound'` "
        "(raw endorsement of a mechanically broken artifact).\n"
        "- **D-alone Schema B model**: at least one Schema B session whose "
        "final selection set is exactly `{D}` (norm_both_methods_count == 1, "
        "has_D == 1, has_A/B/C/E == 0)."
    )
    lines.append("")
    lines.append("## Instability rows")
    lines.append("")
    table_rows = [
        ["Models whose Test 01 sn_verdict flips across 12 sessions",
         verdict_flip, pct(verdict_flip, panel_n)],
        ["Models using at least 2 distinct recoverable method classes",
         classes_two_plus, pct(classes_two_plus, panel_n)],
        ["Models using at least 3 distinct recoverable method classes",
         classes_three_plus, pct(classes_three_plus, panel_n)],
        ["Models whose KO7-vs-Fruit axis-count tuple changes",
         axis_tuple_changed, pct(axis_tuple_changed, panel_n)],
        ["Cross-test incoherent (T01 yes via bad method AND T04 or T06 endorses unsound)",
         cross_incoherent, pct(cross_incoherent, panel_n)],
        ["Models ever isolating {D} alone in Schema B",
         len(d_alone_models), pct(len(d_alone_models), panel_n)],
        [f"Of the {len(d_alone_models)} D-alone models, retrieve transformed_calls in Schema A",
         d_alone_and_retrieve,
         pct(d_alone_and_retrieve, len(d_alone_models)) if d_alone_models else "-"],
    ]
    lines.append(md_table(["Statistic", "Count", "Rate"], table_rows))
    lines.append("")

    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
