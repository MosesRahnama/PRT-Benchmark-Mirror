# Test 06 Numbers (PRT manuscript: tab:t06 and body 6.2)

- Generated: 2026-05-03
- Reproduces: appendix `tab:t06` and the Test 06 body-prose numbers in section 6.2.
- Denominator: n=108.

## Source fields

- `strategy_sound_correctness` == Correct iff the response judges the helper strategy unsound (gold = unsound).
- `kappa_rec_delta_step_correctness` == Correct iff the response correctly identifies that the helper's claimed metric drop on `kappa_rec_delta_step` is false.
- `nested_delta_branch_diagnosis_correctness` == Correct iff the nested-delta branch is correctly named as the failure point.
- `overall_test06_correctness` == Correct iff both the unsound verdict and the nested-delta diagnosis match gold.

| Field and value | Count | Rate |
| --- | --- | --- |
| strategy_sound_correctness = Correct (strategy unsound) | 77 | 71.3% |
| kappa_rec_delta_step_correctness = Correct | 74 | 68.5% |
| nested_delta_branch_diagnosis_correctness = Correct | 74 | 68.5% |
| overall_test06_correctness = Correct | 58 | 53.7% |
