"""Regenerate `tab:t05` and the Test 05 body / propose-vs-verify numbers.

Test 05 reuses the KO7 kernel unchanged and presents three concrete
additive measures mu_1, mu_2, mu_3 with different per-constructor
weightings. All three fail at `R_rec_succ`. The correct response
rejects all three and localizes to that rule.

Reproduces:
  * appendix `tab:t05` rows (all three rejected, R_rec_succ
    localization, overall correctness).
  * propose-versus-verify numbers in body 6.2: 22/27 models propose a
    direct or lexicographic whole-term measure under an open-ended
    yes verdict in at least one Schema A or Test 01 session; of those
    22, 18/22 reject all three Test 05 candidates in *every* Test 05
    session and 21/22 reject all three in at least one session.

Source CSVs:
  * test-05-candidate-class-reasoning-tests.csv         (n=108)
  * schema-test-A-tests.csv       (n=108) - for proposer set
  * test-01-kernel-tests.csv         (n=324) - for proposer set

Field mapping:
  * `mu1_yes_no`, `mu2_yes_no`, `mu3_yes_no`: per-candidate verdicts
    in {yes, no, unclear}; gold = no for all three.
  * `r_rec_succ_localization_correctness` == "Correct" iff the response
    names `R_rec_succ` (or its renamed equivalent) as the decisive rule.
  * `overall_test05_correctness` == "Correct" iff the response rejects
    all three and localizes to R_rec_succ.
  * Direct/lex proposer set: a model proposes `direct_measure` on
    Schema A (`turn1_norm_primary_method_method_class`) or on Test 01
    (`norm_primary_method_method_class`) under an `sn_verdict` of
    "yes" in at least one session. The paper restricts the proposer
    membership to the canonical direct/lexicographic family rather
    than the broader structural-descent / structural-induction
    cluster.
"""
from __future__ import annotations

from datetime import date
from pathlib import Path

from _common import assert_n, canonical_model, load_csv, md_table, pct


OUTPUT_PATH = Path(__file__).with_suffix(".md")

DIRECT_LEX_FAMILIES = {"direct_measure"}


def main() -> None:
    test05 = load_csv("test-05-candidate-class-reasoning-tests.csv")
    schema_a = load_csv("schema-test-A-tests.csv")
    test01 = load_csv("test-01-kernel-tests.csv")
    assert_n(test05, 108, "Test 05")
    assert_n(schema_a, 108, "Schema A")
    assert_n(test01, 324, "Test 01")
    n = 108

    # Test 05 headline rows
    rejected_all = sum(
        1 for r in test05
        if r["mu1_yes_no"] == "no"
        and r["mu2_yes_no"] == "no"
        and r["mu3_yes_no"] == "no"
    )
    r_rec_succ_localized = sum(
        1 for r in test05
        if r["r_rec_succ_localization_correctness"] == "Correct"
    )
    overall_correct = sum(
        1 for r in test05 if r["overall_test05_correctness"] == "Correct"
    )

    # Propose-vs-verify cross-test
    # 1. proposer models: any session in Schema A or Test 01 with
    #    sn_verdict yes AND method_class in DIRECT_LEX_FAMILIES.
    proposer_models: set[str] = set()
    for r in schema_a:
        if (r["turn1_sn_verdict"] == "yes"
                and r["turn1_norm_primary_method_method_class"] in DIRECT_LEX_FAMILIES):
            proposer_models.add(canonical_model(r["model"]))
    for r in test01:
        if (r["sn_verdict"] == "yes"
                and r["norm_primary_method_method_class"] in DIRECT_LEX_FAMILIES):
            proposer_models.add(canonical_model(r["model"]))

    # 2. for each proposer model, count Test 05 sessions and how many reject all 3
    test05_by_model: dict[str, list[dict[str, str]]] = {}
    for r in test05:
        test05_by_model.setdefault(canonical_model(r["model"]), []).append(r)

    reject_in_every = 0
    reject_in_at_least_one = 0
    for model in proposer_models:
        sessions = test05_by_model.get(model, [])
        if not sessions:
            continue
        all_reject = [
            r["mu1_yes_no"] == "no"
            and r["mu2_yes_no"] == "no"
            and r["mu3_yes_no"] == "no"
            for r in sessions
        ]
        if all(all_reject):
            reject_in_every += 1
        if any(all_reject):
            reject_in_at_least_one += 1

    proposer_n = len(proposer_models)
    panel_n = 27

    lines: list[str] = []
    lines.append("# Test 05 Numbers (PRT manuscript: tab:t05 and body 6.2 propose-vs-verify)")
    lines.append("")
    lines.append(f"- Generated: {date.today().isoformat()}")
    lines.append("- Reproduces: appendix `tab:t05` and the propose-vs-verify cross-test numbers.")
    lines.append("- Denominator: n=108 for Test 05; 27-model panel for cross-test rows.")
    lines.append("")
    lines.append("## Source fields")
    lines.append("")
    lines.append(
        "- `mu1_yes_no`, `mu2_yes_no`, `mu3_yes_no`: per-candidate verdicts "
        "in {yes, no, unclear}; gold = no for all three.\n"
        "- `r_rec_succ_localization_correctness` == Correct iff the response "
        "names `R_rec_succ` as the decisive rule.\n"
        "- `overall_test05_correctness` == Correct iff the response rejects "
        "all three candidates and localizes to `R_rec_succ`.\n"
        "- Direct/lex proposer membership: at least one Schema A or Test 01 "
        "session with `sn_verdict == 'yes'` and `method_class == "
        "'direct_measure'`. The paper restricts proposer membership to the "
        "canonical direct/lexicographic family rather than the broader "
        "structural-descent / structural-induction cluster."
    )
    lines.append("")
    lines.append("## `tab:t05` rows")
    lines.append("")
    table_rows = [
        ["All three mu_i rejected simultaneously", rejected_all, pct(rejected_all, n)],
        ["r_rec_succ_localization_correctness = Correct",
         r_rec_succ_localized, pct(r_rec_succ_localized, n)],
        ["overall_test05_correctness = Correct",
         overall_correct, pct(overall_correct, n)],
    ]
    lines.append(md_table(["Field and value", "Count", "Rate"], table_rows))
    lines.append("")
    lines.append("## Body 6.2: propose-vs-verify cross-test contradiction")
    lines.append("")
    lines.append(
        "Per-model split. Step 1: identify models that ever propose a direct "
        "or lexicographic whole-term measure under a positive verdict in "
        "Schema A or Test 01 (the proposer set). Step 2: among those models, "
        "count those whose Test 05 sessions reject all three candidates in "
        "every Test 05 session, and those who do so in at least one."
    )
    lines.append("")
    panel_rows = [
        ["Direct/lex proposer models (Schema A or Test 01)",
         f"{proposer_n}/{panel_n}",
         pct(proposer_n, panel_n)],
        ["  Reject all three in every Test 05 session",
         f"{reject_in_every}/{proposer_n}",
         pct(reject_in_every, proposer_n)],
        ["  Reject all three in at least one Test 05 session",
         f"{reject_in_at_least_one}/{proposer_n}",
         pct(reject_in_at_least_one, proposer_n)],
    ]
    lines.append(md_table(["Signal", "Comparison", "Rate"], panel_rows))
    lines.append("")

    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
