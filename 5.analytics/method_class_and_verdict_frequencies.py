"""Method-class frequency and termination-verdict-flip stats per surface.

Side-by-side counts of every primary method class and every termination
verdict observed on the three open-ended generation tasks, plus the
within-test verdict-flip incidence per surface. Method-name granularity
is intentionally NOT tracked: it is noisier than method class (LPO /
RPO / lexicographic-measure variants etc.) and obscures the load-bearing
signal.

Surfaces (each on its own kernel):
  * Schema A         (n=108,  4 sessions per model, duplicating kernel)
  * SANS             (n=108,  4 per model, non-duplicating control)
  * Test 01 KO7      (n=162,  6 per model, KO7 original names)
  * Test 01 Fruit    (n=162,  6 per model, fruit-renamed control)
  * Test 01 combined (n=324, 12 per model, both Test 01 conditions)

Source CSVs:
  * schema-test-A-tests.csv             (turn1_*)
  * schema-test-A-new-system-tests.csv  (turn1_*)
  * test-01-kernel-tests.csv               (sn_verdict, prompt_variant)

Sections produced:

  1. Method-class frequency: every method class observed on any surface,
     with count and rate side-by-side across the five surfaces.
  2. Termination-verdict frequency: yes / no / unclear, side-by-side
     across the five surfaces.
  3. Within-test verdict-flip incidence: per surface, how many of the 27
     models produce at least two distinct non-blank termination verdicts
     across their repeated sessions on that surface. The pair-wise rerun
     normalization (two distinct values out of N reruns) follows the
     same definition used in `within_test_method_consistency.py`.

The output denominators per surface are the session counts above.
Verdict-flip denominators are 27 (the model panel).
"""
from __future__ import annotations

from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

from _common import assert_n, canonical_model, load_csv, md_table, pct

OUTPUT_PATH = Path(__file__).with_suffix(".md")
N_MODELS = 27


def distinct_nonempty(values: list[str]) -> set[str]:
    return {v for v in values if (v or "").strip()}


def class_counts(rows: list[dict[str, str]], col: str) -> Counter:
    return Counter((r.get(col, "") or "").strip() for r in rows)


def verdict_flip_count(rows: list[dict[str, str]], verdict_col: str) -> int:
    """Number of models whose verdicts vary across their sessions on this surface."""
    by_model: dict[str, list[str]] = defaultdict(list)
    for r in rows:
        by_model[canonical_model(r["model"])].append(r.get(verdict_col, ""))
    return sum(
        1 for model_rows in by_model.values()
        if len(distinct_nonempty(model_rows)) > 1
    )


def class_change_count(rows: list[dict[str, str]], class_col: str) -> int:
    """Number of models whose primary method class varies across sessions on this surface."""
    by_model: dict[str, list[str]] = defaultdict(list)
    for r in rows:
        by_model[canonical_model(r["model"])].append(r.get(class_col, ""))
    return sum(
        1 for model_rows in by_model.values()
        if len(distinct_nonempty(model_rows)) > 1
    )


def main() -> None:
    schema_a = load_csv("schema-test-A-tests.csv")
    assert_n(schema_a, 108, "Schema A")

    sans = load_csv("schema-test-A-new-system-tests.csv")
    assert_n(sans, 108, "SANS")

    test01 = load_csv("test-01-kernel-tests.csv")
    assert_n(test01, 324, "Test 01")

    ko7   = [r for r in test01 if r.get("prompt_variant") == "regular"]
    fruit = [r for r in test01 if r.get("prompt_variant") == "control"]
    assert_n(ko7,   162, "Test 01 KO7 condition")
    assert_n(fruit, 162, "Test 01 Fruit condition")

    surfaces = [
        ("Schema A",         schema_a, "turn1_sn_verdict",
         "turn1_norm_primary_method_method_class", 4),
        ("SANS",             sans,     "turn1_sn_verdict",
         "turn1_norm_primary_method_method_class", 4),
        ("Test 01 KO7",      ko7,      "sn_verdict",
         "norm_primary_method_method_class", 6),
        ("Test 01 Fruit",    fruit,    "sn_verdict",
         "norm_primary_method_method_class", 6),
        ("Test 01 combined", test01,   "sn_verdict",
         "norm_primary_method_method_class", 12),
    ]

    # ── frequencies ─────────────────────────────────────────────────────
    method_freq: dict[str, Counter] = {}
    verdict_freq: dict[str, Counter] = {}
    for label, rows, v_col, c_col, _ in surfaces:
        method_freq[label]  = class_counts(rows, c_col)
        verdict_freq[label] = class_counts(rows, v_col)

    all_classes = set()
    for c in method_freq.values():
        all_classes.update(k for k in c if k)
    all_verdicts = set()
    for c in verdict_freq.values():
        all_verdicts.update(k for k in c if k)

    # Sort classes by total share across surfaces (Schema A + SANS + Test 01 combined,
    # to avoid double-counting Test 01 KO7/Fruit).
    weight: dict[str, int] = defaultdict(int)
    for label in ("Schema A", "SANS", "Test 01 combined"):
        for k, v in method_freq[label].items():
            if k:
                weight[k] += v
    sorted_classes = sorted(all_classes, key=lambda k: (-weight[k], k))

    verdict_order = ["yes", "no", "unclear"]
    sorted_verdicts = [v for v in verdict_order if v in all_verdicts] + sorted(
        all_verdicts - set(verdict_order)
    )

    # ── markdown ────────────────────────────────────────────────────────
    lines: list[str] = []
    lines.append("# Method-class frequency and termination-verdict-flip stats per surface")
    lines.append("")
    lines.append(f"- Generated: {date.today().isoformat()}")
    lines.append(f"- Panel: {N_MODELS} models")
    lines.append("- Source CSVs: Schema A (n=108), SANS (n=108), Test 01 (n=324, 162 KO7 + 162 Fruit).")
    lines.append("")
    lines.append(
        "Each surface is independently aggregated. Method-name granularity is "
        "not tracked. Blank or missing values are excluded from every share. "
        "The `Test 01 combined` column is the union of `Test 01 KO7` and "
        "`Test 01 Fruit` (n=324)."
    )
    lines.append("")

    # ── method-class frequency ─────────────────────────────────────────
    lines.append("## Primary method class frequency")
    lines.append("")
    lines.append(
        "Counts the canonical primary method class chosen on each session, "
        "side-by-side across the five surfaces. Rates are over the surface's "
        "total session count. Classes are ordered by their pooled count over "
        "Schema A + SANS + Test 01 combined, so the load-bearing rows appear "
        "first. Classes that never appear on a surface show as 0."
    )
    lines.append("")
    surface_headers = [f"{s[0]} (n={len(s[1])})" for s in surfaces]
    headers = ["Method class"] + surface_headers
    rows_out: list[list[object]] = []
    for k in sorted_classes:
        row: list[object] = [k]
        for label, surface_rows, _, _, _ in surfaces:
            count = method_freq[label].get(k, 0)
            row.append(f"{count} ({pct(count, len(surface_rows))})")
        rows_out.append(row)
    # Trailing total-non-blank row
    total_row: list[object] = ["**any non-blank**"]
    for label, surface_rows, _, _, _ in surfaces:
        count = sum(v for k, v in method_freq[label].items() if k)
        total_row.append(f"**{count} ({pct(count, len(surface_rows))})**")
    rows_out.append(total_row)
    blank_row: list[object] = ["(blank)"]
    for label, surface_rows, _, _, _ in surfaces:
        count = method_freq[label].get("", 0)
        blank_row.append(f"{count} ({pct(count, len(surface_rows))})")
    rows_out.append(blank_row)
    lines.append(md_table(headers, rows_out))
    lines.append("")

    # ── termination-verdict frequency ──────────────────────────────────
    lines.append("## Termination-verdict frequency")
    lines.append("")
    lines.append(
        "The session-level termination verdict on each surface (gold = yes "
        "on Schema A, SANS, and Test 01). Side-by-side counts and rates."
    )
    lines.append("")
    v_rows: list[list[object]] = []
    for v in sorted_verdicts:
        row: list[object] = [v]
        for label, surface_rows, _, _, _ in surfaces:
            count = verdict_freq[label].get(v, 0)
            row.append(f"{count} ({pct(count, len(surface_rows))})")
        v_rows.append(row)
    blank_v_row: list[object] = ["(blank)"]
    for label, surface_rows, _, _, _ in surfaces:
        count = verdict_freq[label].get("", 0)
        blank_v_row.append(f"{count} ({pct(count, len(surface_rows))})")
    v_rows.append(blank_v_row)
    lines.append(md_table(["Verdict"] + surface_headers, v_rows))
    lines.append("")

    # ── verdict-flip and class-change incidence per surface ────────────
    lines.append("## Within-surface verdict-flip and method-class-change incidence")
    lines.append("")
    lines.append(
        "Per surface, the number of models (out of 27) whose repeated "
        "sessions on the SAME kernel produce at least two distinct non-blank "
        "termination verdicts (verdict flip) or at least two distinct "
        "non-blank primary method classes (class change). Same definition "
        "as `within_test_method_consistency.py`. Denominator is the 27-model "
        "panel."
    )
    lines.append("")
    flip_rows: list[list[object]] = []
    for label, rows, v_col, c_col, sessions_per_model in surfaces:
        flip = verdict_flip_count(rows, v_col)
        change = class_change_count(rows, c_col)
        flip_rows.append([
            f"{label} (n={len(rows)}, {sessions_per_model}/model)",
            flip, pct(flip, N_MODELS),
            change, pct(change, N_MODELS),
        ])
    lines.append(md_table(
        ["Surface",
         "Models flipping termination verdict", "%",
         "Models changing method class", "%"],
        flip_rows,
    ))
    lines.append("")

    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
