#!/usr/bin/env python3
"""Rewrite <workspace> placeholders to the local checkout path.

This helper is intended for anonymous-review mirrors. It updates only the
literal `<workspace>` marker and leaves all other anonymization placeholders
unchanged.

Typical usage from the repository root:

    python prepare_review_workspace.py --apply

You can also point the placeholders at a different path:

    python prepare_review_workspace.py --workspace "D:\\review\\PRT-Benchmark-Anon" --apply
"""
from __future__ import annotations

import argparse
from pathlib import Path

PLACEHOLDER = "<workspace>"
TEXT_EXTS = {".md", ".txt", ".json", ".cff", ".html", ".lean", ".toml",
             ".yml", ".yaml", ".csv", ".tab", ".tsv", ".py"}
EXTENSIONLESS_TEXT_NAMES = {"LICENSE", "AUTHORS", "NOTICE", "COPYING", "INSTALL"}
SKIP_DIR_NAMES = {".git", ".lake", "__pycache__", "node_modules", ".venv"}


def is_text_file(path: Path) -> bool:
    return path.suffix.lower() in TEXT_EXTS or path.name in EXTENSIONLESS_TEXT_NAMES


def in_skip_dir(path: Path, root: Path) -> bool:
    return any(part in SKIP_DIR_NAMES for part in path.relative_to(root).parts)


def rewrite_workspace_markers(root: Path, workspace: str, *, apply: bool) -> tuple[int, int]:
    replacements = files_changed = 0
    for path in root.rglob("*"):
        if not path.is_file() or not is_text_file(path) or in_skip_dir(path, root):
            continue
        try:
            original = path.read_text(encoding="utf-8", errors="strict")
        except Exception:
            continue
        if PLACEHOLDER not in original:
            continue
        count = original.count(PLACEHOLDER)
        updated = original.replace(PLACEHOLDER, workspace)
        replacements += count
        files_changed += 1
        if apply:
            path.write_text(updated, encoding="utf-8")
    return replacements, files_changed


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    default_root = Path(__file__).resolve().parent
    parser.add_argument(
        "--root",
        type=Path,
        default=default_root,
        help="Anonymous mirror root. Defaults to the directory containing this script.",
    )
    parser.add_argument(
        "--workspace",
        default=None,
        help="Path string to substitute for <workspace>. Defaults to --root.",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Write the replacements in place. Without this flag, run in preview mode.",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    workspace = args.workspace or str(root)
    replacements, files_changed = rewrite_workspace_markers(root, workspace, apply=args.apply)

    mode = "applied" if args.apply else "preview"
    print(f"prepare_review_workspace.py ({mode})")
    print(f"root: {root}")
    print(f"workspace: {workspace}")
    print(f"files changed: {files_changed}")
    print(f"placeholder replacements: {replacements}")
    if not args.apply:
        print("Re-run with --apply to write the replacements in place.")


if __name__ == "__main__":
    main()
