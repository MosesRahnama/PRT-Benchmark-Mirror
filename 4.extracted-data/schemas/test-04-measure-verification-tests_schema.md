# Test 04 Measure Verification — Master Data Schema

Test 04 asks 27 LLMs to assess whether a proposed lexicographic measure `(phase, cost)` is sound for the KO7 rewrite calculus. The finalized raw data is single-response and single-round, and it covers 108 sessions.

## Columns

- `session_slug`: Session identifier, `<model>__<timestamp>`.
- `model`: Display model name.
- `provider`: Model provider.
- `measure_sound_yes_no`: Final yes/no verdict on whether the proposed measure is sound.
- `measure_sound_quote`: Verbatim quote supporting `measure_sound_yes_no`.
- `r_rec_succ_cited`: `yes` when the response explicitly cites or analyzes `R_rec_succ`; `no` otherwise.
- `phase_exposure_cited`: `yes` when the response explicitly identifies the wrapper-removal / exposure problem that can raise phase at the root; `no` otherwise.
- `self_correction_flag`: `yes` when the response visibly revises or retracts an earlier claim; `no` otherwise.
- `self_contradiction_flag`: `yes` when incompatible claims remain in the delivered response without a clean resolved reading; `no` otherwise.
- `review_notes`: Free-text notes for follow-up, ambiguity, or short adjudication comments.
- `measure_sound_correctness`: Derived verdict column. `Correct` when `measure_sound_yes_no = no`; `Incorrect` when `measure_sound_yes_no = yes`.
- `phase_exposure_localization_correctness`: Derived verdict column. `Correct` when `phase_exposure_cited = yes`; `Incorrect` when `phase_exposure_cited = no`.
- `overall_test04_correctness`: Derived verdict column. `Correct` when the response both rejects the measure and cites the wrapper-exposure failure, `Unresolved` when it rejects the measure without the decisive localization, and `Incorrect` when it says the measure is sound.
- `quote_spawn_versus_answer_mismatch`: Helper QC column. Current live values are `yes` or `no`. It records whether a post-extraction quote/span review found the stored support text mismatched against the finalized answer field. It is not itself an answer-key verdict column.

## Normalization

No normalization-only columns are currently present in this CSV.
