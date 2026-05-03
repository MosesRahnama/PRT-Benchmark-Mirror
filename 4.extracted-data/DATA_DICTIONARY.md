# Public Data Dictionary

This file describes the public extracted-data layer for the PRT benchmark release.

## Released CSVs

The authoritative observational tables are the nine CSVs in `csv/`:

| CSV | Rows | Surface |
|---|---:|---|
| `schema-test-A-tests.csv` | 108 | Schema A duplicating boundary test |
| `schema-test-A-new-system-tests.csv` | 108 | Schema A matched non-duplicating control |
| `schema-test-B-tests.csv` | 108 | Schema B five-method closed-menu test |
| `test-01-kernel-tests.csv` | 324 | KO7/Fruit kernel termination test |
| `test-02-completion-tests-nat-lex.csv` | 108 | Nat-lex scaffold completion test |
| `test-03-completion-tests-ordinal.csv` | 108 | Ordinal scaffold completion test |
| `test-04-measure-verification-tests.csv` | 108 | Measure verification test |
| `test-05-candidate-class-reasoning-tests.csv` | 108 | Candidate-class reasoning test |
| `test-06-branch-realism-tests.csv` | 108 | Branch-realism strategy audit |

Each CSV contains one row per model session. Shared columns include session identity, model/provider identity, extracted model-response fields, normalized fields where applicable, and answer-key verdict columns where the scoring layer has derived them.

## Schema Documentation

Column-level documentation lives in `schemas/`:

- `ALL_TESTS_schema.md` summarizes shared conventions across all surfaces.
- Each `*_schema.md` file documents the corresponding CSV in `csv/`.

If a CSV field is unclear, use the matching schema document as the authoritative definition.

## Normalization Provenance

Normalization documentation lives in `normalization/`:

- `normalization/guides/` contains per-surface normalization guides.
- `normalization/method-maps/` contains method-label and method-renaming tables.
- `normalization/overrides/` contains active manual-review ledgers. The Schema A override ledger records reviewed rows whose decisions are already reflected in `csv/schema-test-A-tests.csv`.

## Answer-Key and Derived Verdicts

Answer-key artifacts are not stored in this data folder. They live in `../7.scoring/answer-key/`:

- `answer_key.json` is the machine-readable gold layer consumed by scoring scripts.
- `answer_keys.md` and `answer_keys_simplified.md` are human-readable mirrors.

The scoring scripts in `../7.scoring/` use those artifacts to regenerate or verify answer-key verdict columns in the released CSVs.

## Analytics

The scripts and markdown outputs in `../8.analytics/` read the CSVs in `csv/` and regenerate the empirical paper numbers. They do not require private extraction files or LLM access.
