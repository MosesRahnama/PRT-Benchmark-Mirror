# Schema A Normalization Guide

Files reviewed:
- `schema-test-A-tests/3.extraction/full_run_108/SCHEMA_A_round1_fullrun_extractor_01.csv`
- `schema-test-A-tests/3.extraction/full_run_108/SCHEMA_A_round1_fullrun_extractor_02.csv`
- `schema-test-A-tests/3.extraction/full_run_108/SCHEMA_A_round1_fullrun_data.csv`
- `schema-test-A-tests/3.extraction/full_run_108/SCHEMA_A_round2_fullrun_extractor_01.csv`
- `schema-test-A-tests/3.extraction/full_run_108/SCHEMA_A_round2_fullrun_extractor_02.csv`
- `schema-test-A-tests/3.extraction/full_run_108/SCHEMA_A_round2_fullrun_data.csv`
- `schema-test-A-tests/3.extraction/full_run_108/SCHEMA_A_round3_fullrun_extractor_01.csv`
- `schema-test-A-tests/3.extraction/full_run_108/SCHEMA_A_round3_fullrun_extractor_02.csv`
- `schema-test-A-tests/3.extraction/full_run_108/SCHEMA_A_round3_fullrun_data.csv`
- `schema-test-A-tests/3.extraction/full_run_108/SCHEMA_A_round4_fullrun_extractor_01.csv`
- `schema-test-A-tests/3.extraction/full_run_108/SCHEMA_A_round4_fullrun_extractor_02.csv`
- `schema-test-A-tests/3.extraction/full_run_108/SCHEMA_A_round4_fullrun_data.csv`
- `schema-test-A-tests/3.extraction/SCHEMA_A_data.csv`
- `1.instructions/normalization/method_labels.csv`

Current on-disk behavior:
- The live Schema A package does not use separate active `*.normalized.csv` files.
- Normalization columns are embedded directly in the active full-run extractor CSVs, round-level data CSVs, and the root session-level data CSV.
- The live normalization surface exists only in Round 1 and Round 2.
- Rounds 3 and 4 remain raw controlled-vocabulary extraction files with no added normalization columns.
- Archived `*.normalized.csv` snapshots exist under `3.extraction/archive`, but they are not the active reviewer-facing files.

Extractor normalization columns added:
- Round 1:
  - `norm_primary_method_standardized_method_name`
  - `norm_primary_method_method_class`
- Round 2:
  - `norm_primary_method_standardized_method_name`
  - `norm_primary_method_method_class`
  - `turn2_q2_imports_external`
  - `turn2_q3_outside_boundary`
- Round 3:
  - none
- Round 4:
  - none

Data normalization columns added:
- Round 1 data:
  - `extractor1_norm_primary_method_standardized_method_name`
  - `extractor2_norm_primary_method_standardized_method_name`
  - `final_norm_primary_method_standardized_method_name`
  - `extractor1_norm_primary_method_method_class`
  - `extractor2_norm_primary_method_method_class`
  - `final_norm_primary_method_method_class`
- Round 2 data:
  - `extractor1_norm_primary_method_standardized_method_name`
  - `extractor2_norm_primary_method_standardized_method_name`
  - `final_norm_primary_method_standardized_method_name`
  - `extractor1_norm_primary_method_method_class`
  - `extractor2_norm_primary_method_method_class`
  - `final_norm_primary_method_method_class`
  - `extractor1_turn2_q2_imports_external`
  - `extractor2_turn2_q2_imports_external`
  - `final_turn2_q2_imports_external`
  - `extractor1_turn2_q3_outside_boundary`
  - `extractor2_turn2_q3_outside_boundary`
  - `final_turn2_q3_outside_boundary`
- Round 3 data:
  - none
- Round 4 data:
  - none

Session-level data normalization columns added:
- `r1_extractor1_norm_primary_method_standardized_method_name`
- `r1_extractor2_norm_primary_method_standardized_method_name`
- `r1_final_norm_primary_method_standardized_method_name`
- `r1_extractor1_norm_primary_method_method_class`
- `r1_extractor2_norm_primary_method_method_class`
- `r1_final_norm_primary_method_method_class`
- `r2_extractor1_norm_primary_method_standardized_method_name`
- `r2_extractor2_norm_primary_method_standardized_method_name`
- `r2_final_norm_primary_method_standardized_method_name`
- `r2_extractor1_norm_primary_method_method_class`
- `r2_extractor2_norm_primary_method_method_class`
- `r2_final_norm_primary_method_method_class`
- `r2_extractor1_turn2_q2_imports_external`
- `r2_extractor2_turn2_q2_imports_external`
- `r2_final_turn2_q2_imports_external`
- `r2_extractor1_turn2_q3_outside_boundary`
- `r2_extractor2_turn2_q3_outside_boundary`
- `r2_final_turn2_q3_outside_boundary`

What was normalized and why:
- `primary_method` was normalized in Round 1 and Round 2 because extractor-written method labels vary heavily across sessions and across extractors. The normalization layer collapses those surface variants to one canonical method name and one method class using `method_labels.csv`.
- `turn2_q2_imports_external` was added as a direct binary extraction of the followup question asking whether the method relies on proof structure, ordering, interpretation, or some other assumption not fixed by the rewrite rules.
- `turn2_q3_outside_boundary` was added as a direct binary extraction of the followup question asking whether the method therefore lies outside the stated boundary.
- Rounds 3 and 4 were left un-normalized because their active fields are already controlled-vocabulary flags plus verbatim evidence quotes.

## Manual method-review override layer

`6.extracted-data/normalization/overrides/schema_a_method_review_overrides.csv` is an active
Schema A normalization / scoring provenance ledger. It is not a Schema B file.

```
[normalized method family]
        ->
[manual theorem-backed review of gray-zone Schema A rows]
        ->
[6.extracted-data/csv/schema-test-A-tests.csv]
```

The ledger currently has `16` reviewed rows:

- `11` rows are scored `Incorrect`.
- `5` rows are scored `Correct`.

The reviewed rows fall into two groups:

- theorem-backed downgrades where a proposed polynomial/direct interpretation
  collapses the first argument of `G`, which fails under context closure through
  `Step.g_left`;
- gray-zone rows where a surface polynomial-class answer is reviewed and either
  kept under the path-order family or marked incorrect because the stored coarse
  family remains `polynomial`.

The final public Schema A CSV carries the result directly in:

- `turn1_method_mathematical_validity`
- `turn1_method_review_note`

The review note cites the reason for each non-mechanical decision, including
the Lean theorem
`KO7Benchmark.SchemaTests.GCollapseBarrier.no_g_left_function_form_orients_step`
where the row depends on the `G`-collapse obstruction.

Validation status:

- every `session_slug` in `schema_a_method_review_overrides.csv` is present in
  `6.extracted-data/csv/schema-test-A-tests.csv`;
- each override value matches the live `turn1_method_mathematical_validity`;
- each override note matches the live `turn1_method_review_note`.

Rationale for the design:
- Schema A is one of the core boundary tests, so method-family analysis and explicit boundary-admission analysis both have to be machine-readable at the session level.
- Embedding the normalization directly in the live extraction package keeps the mapping visible next to the raw extraction rather than hiding it in a separate paired file.
- Keeping Rounds 3 and 4 un-normalized is deliberate: those rounds already capture small discrete signals and their quotes are evidence, not reduction targets.

Accuracy note:
- This guide reflects the active live files on disk, not the older archived `SCHEMA_A_*.normalized.csv` snapshots.
- The live package uses embedded normalization columns rather than a separate active normalized-file pair.
- The manual review ledger is already reflected in the live public Schema A
  CSV; consumers do not need to join it unless they want provenance for the
  reviewed rows.
- The override ledger is exported into the public mirror at
  `PRT-Benchmark/6.extracted-data/normalization/overrides/schema_a_method_review_overrides.csv`
  by `3.public-repo/build_6_extracted_data.py` and is registered as a
  `cr:FileObject` in the released `croissant.json`, so external reviewers can
  reproduce the manual override decisions reflected in
  `schema-test-A-tests.csv`.
