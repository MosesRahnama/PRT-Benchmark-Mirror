"""Within-test method-class and termination-verdict consistency.

Per-test analysis (no cross-test pooling). For each test surface
independently, measures how often a model produces varying primary method
classes or termination verdicts across its repeated sessions on the SAME
kernel. Method-name granularity is intentionally NOT tracked here:
method-name choices are noisier than method-class choices (LPO / RPO /
lexicographic-measure variants etc.) and obscure the load-bearing signal.

Surfaces analysed (each on its own kernel):
  * Schema A         (108 sessions,  4 per model, duplicating kernel)
  * SANS             (108 sessions,  4 per model, non-duplicating control)
  * Test 01 KO7      (162 sessions,  6 per model, KO7 original names)
  * Test 01 Fruit    (162 sessions,  6 per model, fruit-renamed control)
  * Test 01 combined (324 sessions, 12 per model, both Test 01 conditions)

'Changes' = the model produced at least two distinct non-blank values for
that field across its sessions on that surface. Blank or missing values
are excluded from the distinct-value sets.

Output:
  1. one headline aggregate table summarising all five surfaces;
  2. one per-model table per surface, listing each of the 27 models with
     their session count and distinct-value counts for the termination
     verdict and the primary method class.
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


def most_common_nonempty(values: list[str]) -> str:
    counts = Counter(v for v in values if (v or "").strip())
    return counts.most_common(1)[0][0] if counts else "(none)"


def per_model_for_surface(rows: list[dict[str, str]],
                          verdict_col: str,
                          class_col: str) -> dict[str, dict]:
    """Return per-model statistics for one surface slice."""
    by_model: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        by_model[canonical_model(r["model"])].append(r)

    out: dict[str, dict] = {}
    for model, sessions in by_model.items():
        verdicts = distinct_nonempty([r.get(verdict_col, "") for r in sessions])
        classes  = distinct_nonempty([r.get(class_col, "")   for r in sessions])
        out[model] = {
            "sessions": len(sessions),
            "distinct_verdicts": len(verdicts),
            "distinct_classes":  len(classes),
            "dominant_class":    most_common_nonempty(
                [r.get(class_col, "") for r in sessions]
            ),
            "dominant_verdict":  most_common_nonempty(
                [r.get(verdict_col, "") for r in sessions]
            ),
        }
    return out


def aggregate_for_surface(per_model: dict[str, dict]) -> dict[str, int]:
    return {
        "changes_verdict": sum(1 for s in per_model.values() if s["distinct_verdicts"] > 1),
        "changes_class":   sum(1 for s in per_model.values() if s["distinct_classes"]  > 1),
        "gt2_classes":     sum(1 for s in per_model.values() if s["distinct_classes"]  > 2),
    }


def main() -> None:
    schema_a = load_csv("schema-test-A-tests.csv")
    assert_n(schema_a, 108, "Schema A")

    sans = load_csv("schema-test-A-new-system-tests.csv")
    assert_n(sans, 108, "SANS")

    test01 = load_csv("test-01-kernel-tests.csv")
    assert_n(test01, 324, "Test 01")

    ko7_rows   = [r for r in test01 if r.get("prompt_variant") == "regular"]
    fruit_rows = [r for r in test01 if r.get("prompt_variant") == "control"]

    surfaces = [
        ("Schema A",       schema_a,   "turn1_sn_verdict",
         "turn1_norm_primary_method_method_class", 4),

        ("SANS",           sans,       "turn1_sn_verdict",
         "turn1_norm_primary_method_method_class", 4),

        ("Test 01 KO7",    ko7_rows,   "sn_verdict",
         "norm_primary_method_method_class", 6),

        ("Test 01 Fruit",  fruit_rows, "sn_verdict",
         "norm_primary_method_method_class", 6),

        ("Test 01 combined", test01,   "sn_verdict",
         "norm_primary_method_method_class", 12),
    ]

    # Compute per-model and aggregate for each surface.
    surface_stats = []
    for label, rows, v_col, c_col, sessions_per_model in surfaces:
        per_model = per_model_for_surface(rows, v_col, c_col)
        agg = aggregate_for_surface(per_model)
        surface_stats.append({
            "label": label,
            "n_sessions": len(rows),
            "sessions_per_model": sessions_per_model,
            "per_model": per_model,
            "agg": agg,
        })

    # ── markdown ──
    lines: list[str] = []
    lines.append("# Within-test method-class and verdict consistency")
    lines.append("")
    lines.append(f"- Generated: {date.today().isoformat()}")
    lines.append(f"- Panel: {N_MODELS} models")
    lines.append(
        "- Source CSVs: Schema A (n=108, 4/model), SANS (n=108, 4/model), "
        "Test 01 (n=324, 12/model = 6 KO7 + 6 Fruit)."
    )
    lines.append("")
    lines.append(
        "Each surface is analysed independently on its own kernel. 'Changes' "
        "means the model produced at least two distinct non-blank values for "
        "the field across its repeated sessions on that surface. Blank or "
        "missing values are excluded from the distinct-value sets. "
        "Method-name granularity is not tracked: it is noisier than method "
        "class and obscures the load-bearing signal."
    )
    lines.append("")

    lines.append("## Source fields")
    lines.append("")
    lines.append(
        "- `model`: canonical model identifier used to group each surface's "
        "sessions into 27 per-model pools; normalised through "
        "`canonical_model()` from `_common.py`.\n"
        "- `turn1_sn_verdict` (Schema A, SANS) / `sn_verdict` (Test 01): "
        "session-level termination verdict. The per-model count of distinct "
        "non-blank values is the verdict-flip signal in the headline table.\n"
        "- `turn1_norm_primary_method_method_class` (Schema A, SANS) / "
        "`norm_primary_method_method_class` (Test 01): canonical primary "
        "method-class label. The per-model count of distinct non-blank values "
        "is the method-class-change signal; counts above 2 feed the "
        "'>2 distinct method classes' column.\n"
        "- `prompt_variant` (Test 01 only): `regular` for KO7-named sessions, "
        "`control` for fruit-renamed sessions. Used to split the Test 01 "
        "CSV into the KO7 (n=162) and Fruit (n=162) condition slices."
    )
    lines.append("")
    lines.append(
        "Blank or whitespace-only values are excluded from every "
        "distinct-value set so missing data is never counted as a verdict "
        "or method choice."
    )
    lines.append("")

    # Aggregate headline
    lines.append("## Aggregate headline")
    lines.append("")
    agg_rows = []
    for s in surface_stats:
        agg_rows.append([
            f"{s['label']} (n={s['n_sessions']}, {s['sessions_per_model']}/model)",
            s["agg"]["changes_verdict"], pct(s["agg"]["changes_verdict"], N_MODELS),
            s["agg"]["changes_class"],   pct(s["agg"]["changes_class"],   N_MODELS),
            s["agg"]["gt2_classes"],     pct(s["agg"]["gt2_classes"],     N_MODELS),
        ])
    lines.append(md_table(
        ["Surface",
         "Change termination verdict", "%",
         "Change method class", "%",
         ">2 distinct method classes", "%"],
        agg_rows,
    ))
    lines.append("")

    # Per-model tables, one per surface
    for s in surface_stats:
        lines.append(f"## Per-model: {s['label']}")
        lines.append("")
        lines.append(
            f"Each row is one model's pool of {s['sessions_per_model']} "
            f"sessions on this surface. **Distinct termination verdicts** "
            f"and **distinct method classes** count distinct non-blank "
            f"values across the pool. Dominant class / verdict is the most "
            f"frequent non-blank value."
        )
        lines.append("")
        rows = []
        for model in sorted(s["per_model"].keys()):
            d = s["per_model"][model]
            rows.append([
                model,
                d["sessions"],
                d["distinct_verdicts"],
                d["distinct_classes"],
                d["dominant_class"],
                d["dominant_verdict"],
            ])
        lines.append(md_table(
            ["Model", "Sessions",
             "Distinct termination verdicts",
             "Distinct method classes",
             "Dominant method class", "Dominant termination verdict"],
            rows,
        ))
        lines.append("")

    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
