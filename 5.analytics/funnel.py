"""Regenerate `tab:funnel` recognition-vs-retrieval rows.

The funnel splits the recognition signal (Schema B Method D, where
dependency pairs is offered as a candidate) from the retrieval signal
(Schema A and Test 01, both open-ended). Reproduces the appendix table
plus the body 7.2 numbers: 105/108 Method D terminates yes, 107/108
in_boundary yes, 104/108 joint yes/yes; Schema A 2/108 transformed
calls; Test 01 KO7 3/162 transformed calls; Test 01 Fruit 0/162.

Source CSVs:
  * schema-test-B-tests.csv  (n=108)
  * schema-test-A-tests.csv             (n=108)
  * test-01-kernel-tests.csv               (n=324: KO7=162, Fruit=162)

Field mapping:
  * Schema B marginals: `method_D_terminates == 'yes'` and
    `method_D_in_boundary == 'yes'` counted independently.
  * Schema A retrieval: `turn1_norm_primary_method_method_class ==
    'transformed_calls'`.
  * Test 01 retrieval: `norm_primary_method_method_class ==
    'transformed_calls'`, split by `prompt_variant`.
"""
from __future__ import annotations

from datetime import date
from pathlib import Path

from _common import assert_n, load_csv, md_table, pct


OUTPUT_PATH = Path(__file__).with_suffix(".md")


def main() -> None:
    schema_b = load_csv("schema-test-B-tests.csv")
    schema_a = load_csv("schema-test-A-tests.csv")
    test01 = load_csv("test-01-kernel-tests.csv")

    assert_n(schema_b, 108, "Schema B")
    assert_n(schema_a, 108, "Schema A")
    assert_n(test01, 324, "Test 01")

    schema_b_term_yes = sum(1 for r in schema_b if r["method_D_terminates"] == "yes")
    schema_b_bdy_yes = sum(1 for r in schema_b if r["method_D_in_boundary"] == "yes")
    schema_a_transformed = sum(
        1 for r in schema_a
        if r["turn1_norm_primary_method_method_class"] == "transformed_calls"
    )
    ko7 = [r for r in test01 if r["prompt_variant"] == "regular"]
    fruit = [r for r in test01 if r["prompt_variant"] == "control"]
    ko7_transformed = sum(
        1 for r in ko7 if r["norm_primary_method_method_class"] == "transformed_calls"
    )
    fruit_transformed = sum(
        1 for r in fruit if r["norm_primary_method_method_class"] == "transformed_calls"
    )

    lines: list[str] = []
    lines.append("# Recognition vs Retrieval Funnel (PRT manuscript: tab:funnel)")
    lines.append("")
    lines.append(f"- Generated: {date.today().isoformat()}")
    lines.append("- Reproduces: appendix `tab:funnel`. The Schema B rows are marginal counts (one axis at a time); the joint count of yes on both axes appears in `headline_results.md`.")
    lines.append("")
    lines.append("## Source fields")
    lines.append("")
    lines.append(
        "- Schema B Method D: `method_D_terminates == 'yes'` (recognition of "
        "method-level termination) and `method_D_in_boundary == 'yes'` "
        "(recognition of boundary admissibility), counted independently as "
        "marginals.\n"
        "- Schema A retrieval: `turn1_norm_primary_method_method_class == "
        "'transformed_calls'` on n=108.\n"
        "- Test 01 retrieval: `norm_primary_method_method_class == "
        "'transformed_calls'` on n=162 each for the KO7 (`prompt_variant == "
        "'regular'`) and Fruit (`prompt_variant == 'control'`) conditions."
    )
    lines.append("")
    table_rows = [
        ["Schema B: Method D terminates = yes (matches gold)",
         schema_b_term_yes, pct(schema_b_term_yes, 108)],
        ["Schema B: Method D in_boundary = yes (matches gold)",
         schema_b_bdy_yes, pct(schema_b_bdy_yes, 108)],
        ["Schema A: turn-1 method class = transformed_calls",
         schema_a_transformed, pct(schema_a_transformed, 108)],
        ["Test 01 KO7: method class = transformed_calls",
         ko7_transformed, pct(ko7_transformed, 162)],
        ["Test 01 Fruit: method class = transformed_calls",
         fruit_transformed, pct(fruit_transformed, 162)],
    ]
    lines.append(md_table(["Signal", "Count", "Rate"], table_rows))
    lines.append("")

    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
