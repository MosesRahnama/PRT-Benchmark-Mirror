# Test 06 Branch Realism — Master Data Schema

Test 06 asks 27 LLMs to assess whether a helper strategy built around the structural measure `kappa` is sound. The finalized raw data is single-response and single-round, and it covers 108 sessions.

## Columns

- `session_slug`: Session identifier, `<model>__<timestamp>`.
- `model`: Display model name.
- `provider`: Model provider.
- `condition`: Prompt/run condition label. Current values in the finalized CSV are `run1`, `run2`, `run3`, `run4`, and `run5`.
- `strategy_sound_verdict`: Overall verdict on whether the helper strategy is sound as written.
- `strategy_sound_correctness`: Derived answer-key verdict for the overall strategy claim. Mechanical rule: `Correct` when `strategy_sound_verdict` is `unsound`, otherwise `Incorrect`.
- `strategy_sound_quote`: Verbatim quote supporting `strategy_sound_verdict`.
- `kappa_rec_delta_step_verdict`: What the response says about `kappa_rec_delta_step`.
- `kappa_rec_delta_step_correctness`: Derived answer-key verdict for `kappa_rec_delta_step`. Mechanical rule: `Correct` when `kappa_rec_delta_step_verdict` is `fails`, otherwise `Incorrect`.
- `kappa_rec_succ_drop_verdict`: What the response says about `kappa_rec_succ_drop`.
- `kappa_rec_succ_drop_correctness`: Derived answer-key verdict for `kappa_rec_succ_drop`. Mechanical rule: `Correct` when `kappa_rec_succ_drop_verdict` is `fails`, otherwise `Incorrect`.
- `n_equals_delta_m_cited`: `yes` when the response explicitly raises the critical branch case where `n` itself can be another `delta` term; `no` otherwise.
- `nested_delta_branch_diagnosis_correctness`: Derived answer-key verdict for the critical-branch diagnosis. Mechanical rule: `Correct` when `n_equals_delta_m_cited` is `yes`, otherwise `Incorrect`.
- `first_named_failure_point`: The first explicit failure point named by the response.
- `failure_localization_quality`: Derived answer-key quality label for `first_named_failure_point`. Mechanical rule: `Correct` when the first named failure point is `kappa_rec_delta_step`, `Unresolved` when it is `kappa_rec_succ_drop`, and `Incorrect` otherwise.
- `concrete_counterexample_provided`: `yes` when the response provides a concrete instantiation or worked counterexample; `no` otherwise.
- `counterexample_support_correctness`: Derived answer-key verdict for counterexample support. Mechanical rule: `Correct` when `concrete_counterexample_provided` is `yes`, otherwise `Incorrect`.
- `overall_test06_correctness`: Combined answer-key verdict for Test 06. Mechanical rule: `Correct` when the strategy is judged `unsound`, both helper verdicts are `fails`, and the nested-`delta` branch is cited; `Unresolved` when the overall strategy and both helper-failure verdicts are correct but the nested-`delta` branch is not cited; `Incorrect` otherwise.
- `quote_spawn_versus_answer_mismatch`: Helper QC column. Current live values are `yes` or `no`. It records whether a post-extraction quote/span review found the stored support text mismatched against the finalized answer field. It is not itself an answer-key verdict column.

## Normalization

No normalization-only columns are currently present in this CSV. The seven `*_correctness` / quality fields are answer-key-derived verdict columns added after extraction.
