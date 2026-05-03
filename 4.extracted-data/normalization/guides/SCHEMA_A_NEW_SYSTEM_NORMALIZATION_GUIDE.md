# Schema A New System Normalization Guide

Files reviewed:
- `schema-test-A-new-system-tests/3.extraction/full_run_108/SCHEMA_A_NEW_SYSTEM_round1_fullrun_extractor_01.csv`
- `schema-test-A-new-system-tests/3.extraction/full_run_108/SCHEMA_A_NEW_SYSTEM_round1_fullrun_extractor_02.csv`
- `schema-test-A-new-system-tests/3.extraction/full_run_108/SCHEMA_A_NEW_SYSTEM_round1_fullrun_data.csv`
- `schema-test-A-new-system-tests/3.extraction/full_run_108/SCHEMA_A_NEW_SYSTEM_round2_fullrun_extractor_01.csv`
- `schema-test-A-new-system-tests/3.extraction/full_run_108/SCHEMA_A_NEW_SYSTEM_round2_fullrun_extractor_02.csv`
- `schema-test-A-new-system-tests/3.extraction/full_run_108/SCHEMA_A_NEW_SYSTEM_round2_fullrun_data.csv`
- `schema-test-A-new-system-tests/3.extraction/full_run_108/SCHEMA_A_NEW_SYSTEM_round3_fullrun_extractor_01.csv`
- `schema-test-A-new-system-tests/3.extraction/full_run_108/SCHEMA_A_NEW_SYSTEM_round3_fullrun_extractor_02.csv`
- `schema-test-A-new-system-tests/3.extraction/full_run_108/SCHEMA_A_NEW_SYSTEM_round3_fullrun_data.csv`
- `schema-test-A-new-system-tests/3.extraction/full_run_108/SCHEMA_A_NEW_SYSTEM_round4_fullrun_extractor_01.csv`
- `schema-test-A-new-system-tests/3.extraction/full_run_108/SCHEMA_A_NEW_SYSTEM_round4_fullrun_extractor_02.csv`
- `schema-test-A-new-system-tests/3.extraction/full_run_108/SCHEMA_A_NEW_SYSTEM_round4_fullrun_data.csv`
- `schema-test-A-new-system-tests/3.extraction/SCHEMA_A_NEW_SYSTEM_data.csv`
- `1.instructions/normalization/method_labels.csv`

Current on-disk behavior:
- The live Schema A New System package does not use separate active `*.normalized.csv` files.
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

Post-data repair layer now present in the live final files:
- The live public final file and the live source final file both include an additional normalization repair for objection-style rows:
  - `6.extracted-data/csv/schema-test-A-new-system-tests.csv`
  - `6.extracted-data/csv/schema-test-A-new-system-tests.csv`
- Turn 1 repair rule:
  - if `turn1_sn_verdict = no` and the normalized method fields were blank, they were filled to:
    - `standardized_method_name = objection_or_non_method`
    - `method_class = objection`
  - This removed the blank negative-verdict pocket without inventing a raw `turn1_primary_method`.
- Turn 2 repair rule for negative rows:
  - if `turn2_q4_still_sn = no` and the normalized method fields were blank, they were filled to:
    - `standardized_method_name = objection_or_non_method`
    - `method_class = objection`
- Turn 2 repair rule for positive but non-method rows:
  - if `turn2_q4_still_sn = yes`, the normalized method fields were blank, and the existing `turn2_q1_method_answer_span` clearly described informal reasoning, undefined-symbol reasoning, underspecification, or explicitly said there was no formal termination proof method, the normalized fields were also filled to:
    - `standardized_method_name = objection_or_non_method`
    - `method_class = objection`
  - This was a normalization repair only. The raw `turn2_primary_method` field was left blank where the model did not actually name a method.
- Practical effect:
  - Turn 1 blank negative rows were normalized into the objection bucket.
  - Turn 2 no longer has blank normalized-method fields in the live final files.

Rationale for the design:
- Schema A New System is the paired non-duplicating control, so method-family analysis and explicit boundary-admission analysis have to be comparable to Schema A at the same session granularity.
- Embedding the normalization directly in the live extraction package keeps the mapping visible next to the raw extraction rather than hiding it in a separate paired file.
- Keeping Rounds 3 and 4 un-normalized is deliberate: those rounds already capture small discrete signals and their quotes are evidence, not reduction targets.

Accuracy note:
- This guide reflects the active live files on disk, not the older archived `SCHEMA_A_NEW_SYSTEM_*.normalized.csv` snapshots.
- The live package uses embedded normalization columns rather than a separate active normalized-file pair.
- The current live state includes both the original extraction-time normalization columns and the later objection-style repair fills described above.
