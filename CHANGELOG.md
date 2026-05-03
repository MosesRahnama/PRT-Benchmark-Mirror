# Changelog

All notable changes to PRT-Benchmark are documented here. The release
follows semantic versioning. The Croissant metadata file
(`croissant.json`) is regenerated mechanically from live data sources on
every release; file hashes and counts in the metadata always match the
released artifacts.

## 1.0.0 -- 2026-04-25

### Added

- First public Croissant + RAI release for PRT-Benchmark.
- Root `croissant.json` describing all release artifacts:
  - 9 CSV-backed RecordSets (one per task family);
  - 2 JSON-backed RecordSets exposing the 1,188 session-transcript
    records via JSONPath extraction over `session.json` files;
  - FileSets for non-tabular folders (1.test-prompts, 2.test-files,
    3.lean, 4.TTT2-Artifacts, 5.test-sessions, 7.scoring, 8.analytics,
    6.extracted-data/normalization).
- Datasheet (`DATASHEET.md`).
- Data statement (`DATA_STATEMENT.md`).
- Citation file (`CITATION.cff`).
- Dual-license: PolyForm Noncommercial 1.0.0 + commercial-by-contact at
  `anonymized@neurips.invalid`. Full terms in `LICENSE`.
- GitHub Pages landing page (`docs/index.html`) with embedded JSON-LD
  for dataset discoverability.
