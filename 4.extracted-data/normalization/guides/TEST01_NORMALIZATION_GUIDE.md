# Test 01 Normalization Guide

Files reviewed:
- `test-01-kernel-tests/3.extraction/full_run_324/TEST01_round1_fullrun_extractor_01.csv`
- `test-01-kernel-tests/3.extraction/full_run_324/TEST01_round1_fullrun_extractor_02.csv`
- `test-01-kernel-tests/3.extraction/full_run_324/TEST01_round1_fullrun_data.csv`
- `test-01-kernel-tests/3.extraction/full_run_324/TEST01_round2_fullrun_extractor_01.csv`
- `test-01-kernel-tests/3.extraction/full_run_324/TEST01_round2_fullrun_extractor_02.csv`
- `test-01-kernel-tests/3.extraction/full_run_324/TEST01_round2_fullrun_data.csv`
- `test-01-kernel-tests/3.extraction/full_run_324/TEST01_round3_fullrun_extractor_01.csv`
- `test-01-kernel-tests/3.extraction/full_run_324/TEST01_round3_fullrun_extractor_02.csv`
- `test-01-kernel-tests/3.extraction/full_run_324/TEST01_round3_fullrun_data.csv`
- `test-01-kernel-tests/3.extraction/full_run_324/TEST01_round4_fullrun_extractor_01.csv`
- `test-01-kernel-tests/3.extraction/full_run_324/TEST01_round4_fullrun_extractor_02.csv`
- `test-01-kernel-tests/3.extraction/full_run_324/TEST01_round4_fullrun_data.csv`
- `test-01-kernel-tests/3.extraction/TEST01_data.csv`
- `1.instructions/normalization/method_labels.csv`
- `1.instructions/normalization/fruit_primary_method.csv`

Current on-disk behavior:
- The live Test 01 package does not use separate active `*.normalized.csv` files.
- Normalization columns are embedded directly in the active Round 1 full-run extractor CSVs, Round 1 data CSV, and the root session-level data CSV.
- The live normalization surface exists only in Round 1.
- Rounds 2, 3, and 4 remain raw controlled-vocabulary extraction files with no added normalization columns.
- Archived `*.normalized.csv` snapshots exist under `3.extraction/archive`, but they are not the active reviewer-facing files.

Extractor normalization columns added:
- Round 1:
  - `norm_primary_method_standardized_method_name`
  - `norm_primary_method_method_class`
- Round 2:
  - none
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
  - none
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

What was normalized and why:
- `primary_method` was normalized in Round 1 because extractor-written method labels vary heavily across sessions and across extractors. The normalization layer collapses those surface variants to one canonical method name and one method class using `method_labels.csv`.
- Rounds 2, 3, and 4 were left un-normalized because their active fields are already controlled-vocabulary signals plus verbatim audit quotes.
- `fruit_primary_method.csv` exists as a separate cross-condition rename resource for Fruit-condition method wording, but that rename has not been applied as a live normalization layer in the active Test 01 extraction package.

Rationale for the design:
- Test 01’s main free-text normalization problem is the Round 1 method label. The later rounds already operate on small discrete vocabularies such as verdict subtype, W2 signal, and framework flags.
- Embedding the normalization directly in the live extraction package keeps the mapping visible next to the raw extraction rather than hiding it in a separate paired file.
- Leaving the Fruit rename unapplied in the live package preserves raw condition-specific wording while keeping the mapping resource available for later pooled analysis.

Accuracy note:
- This guide reflects the active live files on disk, not the older archived `TEST01_*.normalized.csv` snapshots.
- The live package uses embedded normalization columns rather than a separate active normalized-file pair.
