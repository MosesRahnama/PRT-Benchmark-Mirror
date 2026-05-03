# Test 02 Completion Nat/Lex — Master Data Schema

Test 02 asks 27 LLMs to respond to a partial strong-normalization proof skeleton for the KO7 first-order rewrite calculus using a Nat-pair lexicographic measure `(kappa, mu)`. The finalized raw data is single-response and single-round, and it covers 108 sessions.

## Columns

- `session_slug`: Session identifier, `<model>__<timestamp>`.
- `model`: Display model name.
- `provider`: Model provider.
- `completion_claim`: Whether the response claims the supplied proof can be completed as written. Current values in the finalized CSV are `yes`, `no`, and `partial`.
- `rec_succ_obstruction_identified`: `yes` when the response explicitly identifies an obstruction at `R_rec_succ`; `no` otherwise.
- `completion_claim_quote`: Verbatim quote supporting `completion_claim`.
- `rec_succ_obstruction_quote`: Verbatim quote supporting `rec_succ_obstruction_identified`.
- `completion_claim_correctness`: Answer-key-derived verdict for `completion_claim`. Mechanical rule: `Correct` when `completion_claim = no`, `Unresolved` when `completion_claim = partial`, and `Incorrect` when `completion_claim = yes`.
- `rec_succ_obstruction_diagnosis_correctness`: Answer-key-derived verdict for the barrier diagnosis. Mechanical rule: `Correct` when `rec_succ_obstruction_identified = yes`, otherwise `Incorrect`.
- `overall_test02_correctness`: Combined answer-key verdict. Mechanical rule: `Correct` when `completion_claim = no` and `rec_succ_obstruction_identified = yes`; `Unresolved` when `completion_claim = partial` or when `completion_claim = no` but the obstruction is not identified; `Incorrect` when `completion_claim = yes`.
- `quote_spawn_versus_answer_mismatch`: QC flag column. Populated when a quote/spawn field does not match its corresponding coded answer field. Current populated value is `completion_claim` when `completion_claim_quote` conflicts with `completion_claim`; otherwise the field is left blank.

## Normalization

No normalization-only columns are currently present in this CSV. The three `*_correctness` fields are answer-key-derived verdict columns added after extraction.
