# Test 05 Candidate Class Reasoning — Master Data Schema

Test 05 asks 27 LLMs to assess three candidate additive termination measures `mu1`, `mu2`, and `mu3` for the KO7 calculus. The finalized raw data is single-response and single-round, and it covers 108 sessions.

## Columns

- `session_slug`: Session identifier, `<model>__<timestamp>`.
- `model`: Display model name.
- `provider`: Model provider.
- `response_truncated_flag`: `1` when the response is visibly truncated or materially incomplete; `0` otherwise.
- `tool_spill_flag`: `1` when the response includes tool/process chatter rather than staying on the task; `0` otherwise.
- `mu1_yes_no`: Final yes/no verdict for candidate `mu1`.
- `mu2_yes_no`: Final yes/no verdict for candidate `mu2`.
- `mu3_yes_no`: Final yes/no verdict for candidate `mu3`.
- `r_rec_succ_cited`: `yes` when the response explicitly cites `R_rec_succ` or directly analyzes that rule; `no` otherwise.
- `self_correction_flag`: `yes` when the response visibly revises or retracts an earlier claim; `no` otherwise.
- `self_contradiction_flag`: `yes` when incompatible claims remain in the delivered response without a clean resolved reading; `no` otherwise.
- `adjudicator_notes`: Free-text notes for ambiguity, follow-up, or short adjudication comments.
- `mu1_correctness`: Derived verdict column. `Correct` when `mu1_yes_no = no`; `Incorrect` when `mu1_yes_no = yes`.
- `mu2_correctness`: Derived verdict column. `Correct` when `mu2_yes_no = no`; `Incorrect` when `mu2_yes_no = yes`.
- `mu3_correctness`: Derived verdict column. `Correct` when `mu3_yes_no = no`; `Incorrect` when `mu3_yes_no = yes`.
- `r_rec_succ_localization_correctness`: Derived verdict column. `Correct` when `r_rec_succ_cited = yes`; `Incorrect` when `r_rec_succ_cited = no`.
- `overall_test05_correctness`: Derived verdict column. `Correct` when all three candidate verdicts are `no` and the shared `R_rec_succ` obstruction is cited, `Unresolved` when all three candidate verdicts are `no` but the shared obstruction is not cited, and `Incorrect` otherwise.

## Normalization

No normalization-only columns are currently present in this CSV.
