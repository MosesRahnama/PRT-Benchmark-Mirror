# Test 03 Completion Ordinal — Master Data Schema

Test 03 asks 27 LLMs to supply a proof skeleton for the remaining ordinal-measure cases in `mu_decreases`. The finalized raw data is single-response and single-round, and it covers 108 sessions.

## Columns

- `session_slug`: Session identifier, `<model>__<timestamp>`.
- `model`: Display model name.
- `provider`: Model provider.
- `r_rec_succ_delivery`: What the model literally delivered for the `R_rec_succ` branch. Current values in the finalized CSV are `closed_code`, `open_code`, `prose_only`, and `missing`.
- `r_eq_refl_delivery`: What the model literally delivered for the `R_eq_refl` branch. Current values in the finalized CSV are `closed_code`, `open_code`, `prose_only`, and `missing`.
- `eq_refl_support_correctness`: Derived answer-key verdict for the easy supportive branch. Mechanical rule: `Correct` when `r_eq_refl_delivery` is any non-`missing` value; otherwise `Incorrect`.
- `r_eq_diff_delivery`: What the model literally delivered for the `R_eq_diff` branch. Current values in the finalized CSV are `closed_code`, `open_code`, `prose_only`, and `missing`.
- `hard_case_delivery_correctness`: Derived answer-key verdict for the two theorem-backed hard obligations (`R_rec_succ`, `R_eq_diff`). Mechanical rule: `Correct` when both hard-case deliveries are `closed_code` or `open_code`; `Unresolved` when neither is `missing` but at least one is `prose_only`; `Incorrect` when either hard-case delivery is `missing`.
- `remaining_case_labels_correct`: `yes` when the response correctly identifies the actual remaining target cases; `no` otherwise.
- `remaining_case_targeting_correctness`: Derived answer-key verdict for the target-set identification. Mechanical rule: `Correct` when `remaining_case_labels_correct` is `yes`, otherwise `Incorrect`.
- `non_remaining_case_material_present`: `yes` when the response spends substantive material on already-completed branches or unrelated case labels; `no` otherwise.
- `response_scope_correctness`: Derived answer-key verdict for response focus. Mechanical rule: `Correct` when `non_remaining_case_material_present` is `no`, otherwise `Incorrect`.
- `overall_test03_correctness`: Combined answer-key verdict for the response as a whole. Mechanical rule: `Correct` when hard-case delivery, easy-case support, targeting, and scope are all `Correct`; `Unresolved` when targeting and scope are `Correct`, the hard-case field is not `Incorrect`, but at least one required supportive condition still falls short; `Incorrect` otherwise.

## Normalization

No normalization-only columns are currently present in this CSV. The five `*_correctness` fields are answer-key-derived verdict columns added after extraction.
