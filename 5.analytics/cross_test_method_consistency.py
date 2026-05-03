"""Cross-test primary-method-class and verdict consistency: Schema A + SANS + Test 01.

Analyzes how the 27-model panel varies primary method class and termination
verdict across the three open-ended generation tasks. Method-name
granularity is intentionally NOT tracked here: it is noisier than method
class (LPO / RPO / lexicographic-measure variants etc.) and obscures the
load-bearing signal.

Source CSVs (all private consolidation copies):
  * schema-test-A-tests.csv            (n=108, Schema A, duplicating)
  * schema-test-A-new-system-tests.csv (n=108, SANS, non-duplicating)
  * test-01-kernel-tests.csv              (n=324, Test 01 KO7 + Fruit)

Total pooled sessions: 108 + 108 + 324 = 540.
Each model contributes ~20 sessions: 4 Schema A, 4 SANS, 12 Test 01.

Column name mapping (the three CSVs use different prefixes):

  Schema A / SANS                       Test 01
  -----------------------------         -----------------------------
  turn1_sn_verdict                      sn_verdict
  turn1_norm_primary_method_method_class  norm_primary_method_method_class

Blank values and cells that read exactly as the empty string are excluded from
the "distinct values" counts to avoid counting missing data as a method choice.

Per-model statistics produced:
  - distinct_sn_verdicts:      number of distinct termination verdicts seen
                               across the model's pooled sessions
  - distinct_method_classes:   number of distinct primary method classes
  - changes_verdict:           True if distinct_sn_verdicts > 1
  - changes_method_class:      True if distinct_method_classes > 1
  - method_class_per_test:     dominant method class in each of the 3 tests
                               (most-frequent non-blank value per test)
  - cross_test_class_drift:    True if the dominant class differs across tests

Aggregate statistics reported:
  - Models changing termination verdict across the pooled 20-session set (n / 27)
  - Models changing primary method class across the pooled 20-session set (n / 27)
  - Paper-facing within-task checks used by the manuscript abstract / appendix:
      * models switching primary method class within at least one open-ended task
      * models switching primary method class within Test 01 only
      * models using > 2 primary method classes within Test 01 only
      * models flipping the termination verdict within Test 01 only
  - Models with > 2 distinct method classes across the pooled 20-session set
  - Full distribution of distinct-class counts
  - Cross-test dominant-class drift count
"""
from __future__ import annotations

from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

from _common import assert_n, canonical_model, load_csv, md_table, pct


OUTPUT_PATH = Path(__file__).with_suffix(".md")


# helpers ────────────────────────────────────────────────────────────────

def most_common_nonempty(values: list[str]) -> str:
    """Return the most frequent non-blank value, or '' if none."""
    counts = Counter(v for v in values if v.strip())
    return counts.most_common(1)[0][0] if counts else ""


def distinct_nonempty(values: list[str]) -> set[str]:
    return {v for v in values if v.strip()}


# load ───────────────────────────────────────────────────────────────────

def load_pool() -> list[dict[str, str]]:
    """
    Load and normalise the three source CSVs into a single list of dicts,
    each guaranteed to have keys:
      model, source_test, sn_verdict, method_class
    """
    pool: list[dict[str, str]] = []

    schema_a = load_csv("schema-test-A-tests.csv")
    assert_n(schema_a, 108, "Schema A")
    for r in schema_a:
        pool.append({
            "model": canonical_model(r["model"]),
            "source_test": "schema_a",
            "sn_verdict": r.get("turn1_sn_verdict", ""),
            "method_class": r.get("turn1_norm_primary_method_method_class", ""),
        })

    sans = load_csv("schema-test-A-new-system-tests.csv")
    assert_n(sans, 108, "Schema A New System")
    for r in sans:
        pool.append({
            "model": canonical_model(r["model"]),
            "source_test": "sans",
            "sn_verdict": r.get("turn1_sn_verdict", ""),
            "method_class": r.get("turn1_norm_primary_method_method_class", ""),
        })

    test01 = load_csv("test-01-kernel-tests.csv")
    assert_n(test01, 324, "Test 01")
    for r in test01:
        pool.append({
            "model": canonical_model(r["model"]),
            "source_test": "test01",
            "sn_verdict": r.get("sn_verdict", ""),
            "method_class": r.get("norm_primary_method_method_class", ""),
        })

    return pool


# analysis ───────────────────────────────────────────────────────────────

def per_model_stats(pool: list[dict[str, str]]) -> dict[str, dict]:
    by_model: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in pool:
        by_model[row["model"]].append(row)

    stats: dict[str, dict] = {}
    for model, rows in sorted(by_model.items()):
        verdicts = distinct_nonempty([r["sn_verdict"] for r in rows])
        classes = distinct_nonempty([r["method_class"] for r in rows])

        # Per-source-test dominant class
        dom_class: dict[str, str] = {}
        for src in ("schema_a", "sans", "test01"):
            src_rows = [r["method_class"] for r in rows if r["source_test"] == src]
            dom_class[src] = most_common_nonempty(src_rows)

        dom_class_values = [v for v in dom_class.values() if v]
        cross_test_class_drift = len(set(dom_class_values)) > 1 if len(dom_class_values) > 1 else False

        stats[model] = {
            "sessions": len(rows),
            "verdicts": sorted(verdicts),
            "distinct_verdicts": len(verdicts),
            "method_classes": sorted(classes),
            "distinct_method_classes": len(classes),
            "changes_verdict": len(verdicts) > 1,
            "changes_method_class": len(classes) > 1,
            "dom_class_schema_a": dom_class["schema_a"],
            "dom_class_sans": dom_class["sans"],
            "dom_class_test01": dom_class["test01"],
            "cross_test_class_drift": cross_test_class_drift,
        }
    return stats


# main ───────────────────────────────────────────────────────────────────

def main() -> None:
    pool = load_pool()
    n_sessions = len(pool)
    stats = per_model_stats(pool)
    n_models = len(stats)

    # aggregate counts
    changes_verdict = sum(1 for s in stats.values() if s["changes_verdict"])
    changes_class = sum(1 for s in stats.values() if s["changes_method_class"])
    drift_cross = sum(1 for s in stats.values() if s["cross_test_class_drift"])
    gt2_classes = sum(1 for s in stats.values() if s["distinct_method_classes"] > 2)

    class_dist = Counter(s["distinct_method_classes"] for s in stats.values())

    # paper-facing within-task checks
    by_model_source: dict[str, dict[str, list[dict[str, str]]]] = defaultdict(lambda: defaultdict(list))
    for row in pool:
        by_model_source[row["model"]][row["source_test"]].append(row)

    def source_distinct(model: str, source: str, field: str) -> set[str]:
        return distinct_nonempty([r[field] for r in by_model_source[model][source]])

    sources = ("schema_a", "sans", "test01")
    any_within_task_class_change = sum(
        1 for model in stats
        if any(len(source_distinct(model, source, "method_class")) > 1 for source in sources)
    )
    test01_class_change = sum(
        1 for model in stats
        if len(source_distinct(model, "test01", "method_class")) > 1
    )
    test01_gt2_classes = sum(
        1 for model in stats
        if len(source_distinct(model, "test01", "method_class")) > 2
    )
    test01_verdict_flip = sum(
        1 for model in stats
        if len(source_distinct(model, "test01", "sn_verdict")) > 1
    )

    # markdown output
    lines: list[str] = []
    lines.append("# Cross-test method-class and verdict consistency: Schema A + SANS + Test 01")
    lines.append("")
    lines.append(f"- Generated: {date.today().isoformat()}")
    lines.append(f"- Source CSVs: Schema A (n=108), SANS (n=108), Test 01 (n=324)")
    lines.append(f"- Total pooled sessions: {n_sessions}")
    lines.append(f"- Model panel: {n_models} models (~{n_sessions // n_models} sessions per model)")
    lines.append("")

    lines.append("## What this analysis measures")
    lines.append("")
    lines.append(
        "For each model, all sessions across the three open-ended generation tasks "
        "are pooled (Schema A duplicating, SANS non-duplicating control, Test 01 KO7 + Fruit). "
        "Two fields are tracked: the termination verdict and the normalised primary method "
        "class. 'Changes' means the model produced at least two distinct non-blank values "
        "for that field across its pooled sessions. 'Dominant class per test' is the most "
        "frequent non-blank method class within each test's sessions for that model; "
        "'cross-test class drift' is True when the dominant class differs across at least "
        "two of the three tests. Method-name granularity is intentionally not tracked: "
        "it is noisier than method class and obscures the load-bearing signal."
    )
    lines.append("")

    lines.append("## Source fields")
    lines.append("")
    lines.append(
        "- `model`: canonical model identifier used for cross-CSV grouping; "
        "`canonical_model()` from `_common.py` normalises the o3 entry so all "
        "three CSVs join on the same key.\n"
        "- `turn1_sn_verdict` (Schema A, SANS) / `sn_verdict` (Test 01): "
        "per-session termination verdict; tracked for distinct-value counts "
        "and for the within-Test-01 verdict-flip rate reported below.\n"
        "- `turn1_norm_primary_method_method_class` (Schema A, SANS) / "
        "`norm_primary_method_method_class` (Test 01): canonical primary "
        "method-class label; tracked for distinct-value counts, "
        "dominant-class-per-test, and cross-test class drift.\n"
        "- `source_test`: synthetic in-memory key (`schema_a` / `sans` / "
        "`test01`) added at load time to tag each pooled row with its origin "
        "CSV; never touched in the source CSVs."
    )
    lines.append("")
    lines.append(
        "Blank or whitespace-only values are excluded from every distinct-value "
        "set so missing data is never counted as a method choice."
    )
    lines.append("")

    # summary table
    lines.append("## Aggregate: models that change across the three tests")
    lines.append("")
    lines.append(
        "Each row counts models whose value for that field varies across their "
        f"{n_sessions // n_models}-session pool."
    )
    lines.append("")
    summary_rows = [
        ["Models changing termination verdict (sn_verdict)", changes_verdict, pct(changes_verdict, n_models)],
        ["Models changing primary method class", changes_class, pct(changes_class, n_models)],
        ["Models with cross-test dominant-class drift", drift_cross, pct(drift_cross, n_models)],
        ["Models with > 2 distinct method classes", gt2_classes, pct(gt2_classes, n_models)],
    ]
    lines.append(md_table(["Signal", "Count", "Rate"], summary_rows))
    lines.append("")
    lines.append(
        f"Note: the pooled termination-verdict change above ({changes_verdict}/{n_models}) "
        "is not the same quantity as the manuscript's within-Test-01 verdict-flip count "
        f"({test01_verdict_flip}/{n_models}). The paper-facing rows below separate those "
        "definitions explicitly."
    )
    lines.append("")

    # paper-facing consistency checks
    lines.append("## Paper-facing consistency checks")
    lines.append("")
    lines.append(
        "These rows are the exact instability definitions used by the manuscript "
        "abstract and Appendix Table `tab:instability`. They deliberately separate "
        "pooled three-task changes from within-Test-01 rerun instability."
    )
    lines.append("")
    paper_rows = [
        [
            "Models switching primary method class within at least one open-ended task (Schema A, SANS, or Test 01)",
            any_within_task_class_change,
            pct(any_within_task_class_change, n_models),
        ],
        [
            "Models switching primary method class within Test 01 only",
            test01_class_change,
            pct(test01_class_change, n_models),
        ],
        [
            "Models using > 2 primary method classes within Test 01 only",
            test01_gt2_classes,
            pct(test01_gt2_classes, n_models),
        ],
        [
            "Models flipping termination verdict within Test 01 only",
            test01_verdict_flip,
            pct(test01_verdict_flip, n_models),
        ],
    ]
    lines.append(md_table(["Signal", "Count", "Rate"], paper_rows))
    lines.append("")

    # distribution table
    lines.append("## Distribution: distinct method-class count per model")
    lines.append("")
    lines.append(
        "How many distinct primary method classes does each model use across "
        "its combined Schema A + SANS + Test 01 sessions?"
    )
    lines.append("")
    class_dist_rows = [
        [k, class_dist[k], pct(class_dist[k], n_models)]
        for k in sorted(class_dist)
    ]
    lines.append(md_table(["Distinct method classes", "Models", "Share"], class_dist_rows))
    lines.append("")

    # per-model detail table
    lines.append("## Per-model breakdown")
    lines.append("")
    lines.append(
        "Per-model summary. Dom-class columns show the most frequent primary method "
        "class within that model's sessions for each task. Drift = Yes when the "
        "dominant class differs across at least two tasks."
    )
    lines.append("")
    detail_rows = []
    for model, s in sorted(stats.items()):
        detail_rows.append([
            model,
            s["sessions"],
            s["distinct_verdicts"],
            s["distinct_method_classes"],
            s["dom_class_schema_a"] or "(none)",
            s["dom_class_sans"] or "(none)",
            s["dom_class_test01"] or "(none)",
            "Yes" if s["cross_test_class_drift"] else "No",
        ])
    lines.append(md_table(
        ["Model", "Sessions",
         "Distinct termination verdicts",
         "Distinct method classes",
         "Dom class Schema A", "Dom class SANS",
         "Dom class Test 01", "Drift"],
        detail_rows,
    ))
    lines.append("")

    # cross-test dominant-class matrix
    lines.append("## Cross-test dominant class summary")
    lines.append("")
    lines.append(
        "Counts of models whose dominant primary method class shifts between "
        "tasks, by source-test pair. A shift is recorded when the dominant "
        "classes in the two tasks are both non-blank and differ."
    )
    lines.append("")

    pairs = [
        ("schema_a", "sans"),
        ("schema_a", "test01"),
        ("sans", "test01"),
    ]
    pair_drift_rows = []
    for src_a, src_b in pairs:
        drift_count = sum(
            1 for s in stats.values()
            if s[f"dom_class_{src_a}"] and s[f"dom_class_{src_b}"]
            and s[f"dom_class_{src_a}"] != s[f"dom_class_{src_b}"]
        )
        both_nonblank = sum(
            1 for s in stats.values()
            if s[f"dom_class_{src_a}"] and s[f"dom_class_{src_b}"]
        )
        pair_drift_rows.append([
            f"{src_a} vs {src_b}",
            both_nonblank,
            drift_count,
            pct(drift_count, both_nonblank),
        ])
    lines.append(md_table(
        ["Task pair", "Both non-blank", "Dominant class differs", "Rate"],
        pair_drift_rows,
    ))
    lines.append("")

    OUTPUT_PATH.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
