"""Shared helpers for the paper-number regeneration scripts.

Every script in this folder regenerates one paper-facing markdown table from
the released CSVs in `../6.extracted-data/csv/`.
"""
from __future__ import annotations

import csv
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
EXTRACTED_DATA = REPO_ROOT / "6.extracted-data" / "csv"


def load_csv(name: str) -> list[dict[str, str]]:
    """Return every row of `../6.extracted-data/csv/<name>` as a dict."""
    path = EXTRACTED_DATA / name
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def canonical_model(value: str) -> str:
    """Return the benchmark-canonical model name used for cross-file grouping."""
    stripped = (value or "").strip()
    if stripped.lower() == "o3":
        return "o3"
    return stripped


def pct(num: int, denom: int) -> str:
    """Format `num/denom` as a one-decimal percentage matching the paper."""
    if denom == 0:
        return "0.0%"
    return f"{100 * num / denom:.1f}%"


def md_table(headers: list[str], rows: list[list[object]]) -> str:
    """Render a GitHub-flavored markdown table with no external deps."""
    out = ["| " + " | ".join(str(h) for h in headers) + " |"]
    out.append("| " + " | ".join(["---"] * len(headers)) + " |")
    for row in rows:
        out.append("| " + " | ".join(str(cell) for cell in row) + " |")
    return "\n".join(out)


def assert_n(rows: list[dict[str, str]], expected: int, name: str) -> None:
    """Hard-fail if the CSV row count does not match the manuscript denominator."""
    actual = len(rows)
    if actual != expected:
        raise AssertionError(
            f"{name}: expected n={expected} sessions but CSV has {actual}. "
            f"The manuscript denominator and the data have drifted; "
            f"investigate before regenerating the table."
        )
