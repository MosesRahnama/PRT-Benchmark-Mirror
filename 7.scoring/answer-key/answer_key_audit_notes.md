# Answer-Key Audit Notes

Running per-test audit log. One section per test, in the order `answer_keys.md` arranges them. Each entry records: Lean / TTT2 coverage status, verdict-column cross-check status, and any open follow-ups.

Date started: 2026-04-20.

---

## Schema A

Status: **CLOSED 2026-04-20**.

Lean coverage: **complete**.
- Kernel + context closure: `SchemaKernel.lean`.
- Truth witness (adequate at truth layer): `NonlinearWitness.wf_StepRev`.
- Candidate (A) LPO/RPO success: `CandidateA.candidateA_success_status`.
- Candidate (B) polynomial `[G(a,b)] = b` failure: `CandidateB.interpB_not_step_orienting`.
- Candidate (C) KBO variable-condition + uniform weight failure: `CandidateC.no_variable_condition_orientation`, `CandidateC.uniform_weight_ground_counterexample`.
- Candidate (D) DP + subterm criterion: `CandidateD.wf_DPPairRev`, `CandidateDBridge.candidateD_full_trs_wf`.
- Candidate (E) direct measure `μn+1` failure: `CandidateE.muE_not_root_orienting`, `CandidateE.muE_not_step_orienting`.
- Generalization of (B): `GCollapseBarrier.no_{g_left,g_right,f_arg2}_collapse_orients_step` plus function-form corollaries.
- Triaxial answer key: `BenchmarkContract.answerKey .schemaA` with 11 method families, backed by `test1_*_row_backed` and the Schema B row theorems (reused for the same kernel).

TTT2 coverage: **complete**.
- CERTIFIED YES: FAST, HYDRA, LPO, COMP.
- REJECTED MAYBE: KBO, POLY, MAT(2), MAT(3).
- Trail: `4.TTT2-Artifacts/ttt2/schema/Schema_CeTA_certification.txt`.

Verdict-column cross-check (`6.extracted-data/csv/schema-test-A-tests.csv`, 108 rows):

- `turn1_termination_correctness` rule: `Correct ↔ turn1_sn_verdict = yes`. Aligned with `NonlinearWitness.wf_StepRev`. Counts: 88 Correct / 20 Incorrect.
- `turn1_method_mathematical_validity` rule (current live form): `Correct ↔ method_class ∈ {path_order, transformed_calls}`. The `polynomial` class is uniformly `Incorrect` under the live rule because `answer_keys.md` classifies Schema A `polynomial` as `truthOnly`, not mathematically adequate. The manual review layer in `schema_a_method_review_overrides.csv` carries 11 override-driven downgrades (5 G-left-collapse polynomial rows + 6 polynomial-truthOnly explicit-witness rows) plus 5 kept-correct confirmations on path-order rows; on the live rule the validity values for the 11 downgraded rows would already evaluate to `Incorrect` mechanically, so the override layer at this point is provenance + reviewer-rationale rather than value-correction. After overrides: 34 Correct / 74 Incorrect. Override source: `schema_a_method_review_overrides.csv`.
- `turn1_method_correct_and_admissible` rule: `Correct ↔ method_class = transformed_calls`. 2 Correct / 106 Incorrect. This matches the `ok` row in the Lean table.
- `turn1_method_review_note`: 16 rows nonblank (11 downgrades + 5 kept-correct confirmations).

Sampled 10 rows: verdicts consistent with the rubric above. One session (`claude-opus-4.5__2026-04-10T14-17-01`) carries the override note with the `no_g_left_function_form_orients_step` citation, as expected.

Known rubric / script divergences:

- The Lean answer key splits `nonlinearPoly` (adequate at the method-class level) from `polynomial` (truthOnly when it collapses an argument). The live public scoring rule treats the entire `polynomial` method class as `Incorrect` so that the released CSV is consistent with the strict Schema A answer key. The manual review layer carries 11 reviewed downgrades (5 G-left-collapse + 6 polynomial-truthOnly) with theorem-citation rationales; the audit finds no uncaught collapse in the 108 rows beyond those.
- `rootOnly`, `affine`, `quadratic` exist in the Lean `MethodFamily` enum but have no distinct public `method_class`. In the 108 rows they fall under `direct_measure` or `polynomial`; scoring remains correct after the review layer.

Open follow-ups: none blocking. A downstream pass can add a `nonlinearPoly` sub-label if a public finer vocabulary is desired.

---

## Schema A New System (SANS)

Status: **CLOSED 2026-04-20**.

Lean coverage: **complete**.
- Kernel + context closure (unary `G`, no `g_left`/`g_right`): `SANSKernel.lean`.
- Truth witness: `LinearWitness.wf_StepRev` via `μ(F(x,y,n)) = μx + μy + μn + 1`, `μ(G(t)) = μt`, `μ(S(t)) = μt + 1`, `μ(Z)=μ(var)=0`. Every step strictly decreases `μ`.
- Answer-key record: `AnswerKey.canonicalAnswerKey` with `truth = yes`, `duplicationObstruction = lifted`, and four boolean adequacy fields (linear direct measure, KBO variable condition, polynomial, DP, path order).
- Re-exports: `AnswerKey.wf_StepRev_SANS`, `AnswerKey.linear_direct_measure_step_decreasing`, `AnswerKey.sans_answer_key_bundle`.

TTT2 coverage: **complete — and stronger than Schema A**.
- All 8 strategies certify: FAST, HYDRA, LPO, COMP, KBO, POLY, MAT(2), MAT(3).
- Trail: `4.TTT2-Artifacts/ttt2/schema-new-system/Schema_New_System_CeTA_certification.txt`.
- Summary: `4.TTT2-Artifacts/ttt2/schema-new-system/schema_new_system_certification_summary.json`.

Verdict-column cross-check (`6.extracted-data/csv/schema-test-A-new-system-tests.csv`, 108 rows):

- `turn1_termination_correctness` rule: `Correct ↔ turn1_sn_verdict = yes`. Aligned with `LinearWitness.wf_StepRev`. Counts: 74 Correct / 34 Incorrect.
- `turn1_method_mathematical_validity` rule (v2): `Correct ↔ sn=yes AND (class ∈ {direct_measure, polynomial, path_order, transformed_calls} OR (class = structural_descent AND subterm_descent_noted = yes))`. Counts: 73 Correct / 35 Incorrect.
- `turn1_method_correct_and_admissible` rule (v2): `Correct ↔ sn=yes AND (class ∈ {direct_measure, transformed_calls} OR (class = structural_descent AND subterm_descent_noted = yes AND g_inert_noted = yes))`. Counts: 55 Correct / 53 Incorrect. The two flag-gated branch encodes the first-order argument behind `LinearWitness`.

Method class distribution: direct_measure = 36, objection = 31, structural_descent = 27, polynomial = 9, path_order = 4, structural_induction = 1.

Sampled 5 rows: verdicts consistent with the rubric.

Known rubric / script divergences:

- `kbo_style` not in the live vocabulary for SANS. TTT2 certifies it but no row carries that class; no action required.
- `structural_induction` (1 row) is scored `Incorrect`. Flag for future extraction review: if the response is subterm descent mislabeled as induction, the normalization layer should reclassify.

Open follow-ups: none blocking.

---

## Schema B

Status: **CLOSED 2026-04-20**.

Lean coverage: **complete**. Same TRS as Schema A, so SchemaTests candidate proofs (A-E) apply verbatim. `BenchmarkContract.lean` provides row-by-row theorems for all five candidates plus `schemaBTable_fully_correct` and `schemaB_only_D_is_admissible` (closed by `decide`).

TTT2 coverage: **complete** via `4.TTT2-Artifacts/ttt2/schema/` (same kernel). FAST/HYDRA/LPO/COMP certified; KBO/POLY/MAT rejected.

Verdict-column cross-check (`6.extracted-data/csv/schema-test-B-tests.csv`, 108 rows):

- The live public file now stores the adjudicated extracted answers, not a
  gold-overwritten answer table.
- Public path:
  `6.extracted-data/csv/schema-test-B-tests.csv`
- Source reduced path:
  `6.extracted-data/csv/schema-test-B-tests.csv`
- Rich data path:
  `schema-test-B-tests/3.extraction/SCHEMA_B_data.normalized.csv`
- Public file shape: 108 rows, 21 columns:
  `session_slug`, `model`, `provider`, `prompt_variant`, the 10 A-E answer
  fields, `norm_method_D_terminates_rationale_family`, and the 6
  `norm_both_methods_*` fields.
- Shared-column audit:
  - public copy matches the reduced source file on all shared columns
  - reduced source file matches the richer data on all shared verdict
    and normalized fields
- Two reduced-row verdict collapses were repaired on 2026-04-20 so the reduced
  and public files now agree with the richer data:
  - `gemini-3-flash-preview__2026-04-05T16-59-23`:
    `method_E_in_boundary` restored from `no` to `unclear`
  - `grok-4-0709__2026-04-05T11-59-23-control`:
    six A/B/C fields restored from `no` to `unclear`
- Gold for grading remains:
  A=(yes,no), B=(no,no), C=(no,no), D=(yes,yes), E=(no,no), with `D` alone as
  the exact both-methods answer.
- Gold-match counts on the repaired live public file:
  - `method_A_terminates = yes`: 102/108
  - `method_A_in_boundary = no`: 16/108
  - `method_B_terminates = no`: 13/108
  - `method_B_in_boundary = no`: 39/108
  - `method_C_terminates = no`: 100/108
  - `method_C_in_boundary = no`: 11/108
  - `method_D_terminates = yes`: 105/108
  - `method_D_in_boundary = yes`: 107/108
  - `method_E_terminates = no`: 28/108
  - `method_E_in_boundary = no`: 23/108
  - exact `D`-alone selection: 4/108
  - all 16 gold fields correct: 0/108

Known rubric / script divergences:

- Older historical ledger entries and archived helper-script reports still
  describe the superseded gold-overwritten Schema B public-file variant. They
  are provenance only and are no longer authoritative for the live public file
  semantics.
- `moot` and `unclear` are preserved in the live extracted answer fields.
  Grading still compares them against the benchmark gold target, so they count
  as mismatches relative to the formal answer key.

Open follow-ups: none blocking. Future work can split `Incorrect` into `Incorrect` vs. `Unresolved` on boundary axes for B/C/E if the analysis wants to preserve the moot-as-structural signal.

---

## Test 01 — Kernel

Status: **CLOSED 2026-04-20**.

Lean coverage: **complete for the public answer chain**.

- Benchmark-local: `KO7Kernel.lean` (TRS), `KO7DependencyPairs.lean` (DP problem WF), and `BenchmarkContract.lean` (`answerKey .test1` plus the direct answer-key rows used by scoring).
- No theory-only Lean modules are part of the public answer chain.

TTT2 coverage: **complete**. FAST / LPO / COMP certified; KBO / POLY / MAT(2) / MAT(3) rejected; FBI MAYBE (no CPF).

Verdict-column cross-check (`6.extracted-data/csv/test-01-kernel-tests.csv`, 324 rows):

- `termination_correctness = Correct ↔ sn_verdict = yes`. Counts: 222 Correct / 102 Incorrect.
- `method_mathematical_validity = Correct ↔ class ∈ {path_order, transformed_calls}`. Generic polynomial rows are truth-level only and stored as `Incorrect` on this kernel. Counts: 48 Correct / 276 Incorrect.
- `method_correct_and_admissible = Correct ↔ class = transformed_calls`. Counts: 3 Correct / 321 Incorrect. Matches the `ok` row in `answerKey .test1`.

Method class distribution across 324 rows (162 KO7 + 162 Fruit): direct_measure 98, objection 93, path_order 45, polynomial 42, structural_induction 29, structural_descent 14, transformed_calls 3.

Known rubric / script divergences:

1. `structural_descent` scores `Incorrect` on `method_mathematical_validity` regardless of whether the model named third-argument descent. Parallel to SANS's v2 upgrade: a `flag_w2_method_named` or `flag_subterm_descent_noted` gate would promote those rows.

Open follow-ups:

1. Optionally upgrade the Test 01 rubric with a `structural_descent + subterm-noted` promotion branch (parallel to SANS).

---

## Test 02 — Completion (Nat-Lex scaffold)

Status: **CLOSED 2026-04-20**.

Lean coverage: **complete**. `Test02_NatLex_AnswerKey.lean` proves all four local-closure cases, formalizes the `R_rec_succ` barrier on the nested-`delta` witness, and concludes `scaffold_not_step_decreasing`. Bundled in `canonical_answer_key_sound`. Re-exported in `BenchmarkContract.test2_row_backed`.

TTT2 coverage: **not applicable**. Test 02 is a proof-skeleton completion task on a supplied lex measure, not a TRS termination probe. No dedicated TTT2 folder required.

Verdict-column cross-check (`6.extracted-data/csv/test-02-completion-tests-nat-lex.csv`, 108 rows):

- `completion_claim_correctness`: 15 Correct (claim = no), 27 Unresolved (claim = partial), 66 Incorrect (claim = yes). Rule aligned with schema.
- `rec_succ_obstruction_diagnosis_correctness`: 16 Correct, 92 Incorrect.
- `overall_test02_correctness`: 15 / 27 / 66. Matches `completion_claim_correctness` exactly because every `completion_claim = no` row also has `rec_succ_obstruction_identified = yes` in the data.

Known rubric / script divergences:

- A reproducible verdict script exists at `7.scoring/add_test02_answer_verdict_columns.py` and emits `add_test02_answer_verdict_columns_report.json`.
- The schema defines an `Unresolved` when claim = no but obstruction missing; no live rows exercise this branch. Audit does not need action unless a future run produces such a row.

Open follow-ups: none blocking.

---

## Test 03 — Completion (Ordinal scaffold)

Status: **CLOSED 2026-04-20**.

Lean coverage: **complete**. `Test03_Ordinal_AnswerKey.lean` proves all six easy-case ordinal decreases under `mu` (including `R_eq_refl`, which the fixture leaves as `sorry`) and isolates the two hard obligations `R_rec_succ` and `R_eq_diff` as `RecSuccObligation`/`EqDiffObligation`. `mu_decreases_of_hard_obligations` closes `mu_decreases` given those two. `strong_normalization_of_hard_obligations` then gives WF. Bundled in `canonical_answer_key_sound`. Re-exported in `BenchmarkContract.test3_row_backed`.

TTT2 coverage: **not applicable** (ordinal completion task, not a TRS termination probe).

Verdict-column cross-check (`6.extracted-data/csv/test-03-completion-tests-ordinal.csv`, 108 rows): script `add_test03_answer_verdict_columns.py` present.

- `hard_case_delivery_correctness`: 93 Correct / 12 Unresolved / 3 Incorrect.
- `eq_refl_support_correctness`: 105 Correct / 3 Incorrect.
- `remaining_case_targeting_correctness`: 103 Correct / 5 Incorrect.
- `response_scope_correctness`: 102 Correct / 6 Incorrect.
- `overall_test03_correctness`: 88 Correct / 12 Unresolved / 8 Incorrect.

Known rubric / script divergences:

- The rubric credits `closed_code` and `open_code` equally at the hard-case axis; only `prose_only` triggers `Unresolved`. Documented, not a gap.
- The Lean answer key closes `R_eq_refl` internally; the rubric routes it through "easy support", not "hard case". Aligned.

Open follow-ups: none blocking.

---

## Test 04 — Measure Verification

Status: **CLOSED 2026-04-20**.

Lean coverage: **complete**. `Test04_MeasureVerificationCounterexample.lean` proves `rec_succ_measure_decreases` (the decoy), exhibits `exposedCounterexample = recDelta void void (delta void)`, and closes `measure_not_step_decreasing` via `merge_void_left_exposes_high_phase`. Re-exported in `BenchmarkContract.test4_row_backed`.

TTT2 coverage: **not applicable** (measure-soundness task).

Verdict-column cross-check (`6.extracted-data/csv/test-04-measure-verification-tests.csv`, 108 rows):

- `measure_sound_correctness`: 84 Correct / 24 Incorrect. Aligned with `measure_not_step_decreasing`.
- `phase_exposure_localization_correctness`: 75 Correct / 33 Incorrect.
- `overall_test04_correctness`: 74 Correct / 10 Unresolved / 24 Incorrect.
- Common failure pattern: `r_rec_succ_cited = yes` + `phase_exposure_cited = no` (wrong localization), landing in Unresolved.

Known rubric / script divergences:

- A reproducible verdict script exists at `7.scoring/add_test04_answer_verdict_columns.py` and emits `add_test04_answer_verdict_columns_report.json`.
- Unresolved is a lenient bucket for "rejected the measure but named the wrong branch." Downstream analysis can tighten this if desired.

Open follow-ups: none blocking.

---

## Test 05 — Candidate Class Reasoning

Status: **CLOSED 2026-04-20**.

Lean coverage: **complete**. `Test05_CandidateClassCounterexamples.lean` proves the three candidates all fail on a single ground `R_rec_succ` step. `mu1_ground_counterexample` (tie), `mu2_ground_counterexample` (tie), `mu3_ground_counterexample` (strict increase), closed by `mu1/mu2/mu3_not_root_orienting`. Re-exported in `BenchmarkContract.test5_row_backed`.

TTT2 coverage: **not applicable** (candidate-class audit, not a TRS probe).

Verdict-column cross-check (`6.extracted-data/csv/test-05-candidate-class-reasoning-tests.csv`, 108 rows):

- `mu1_correctness`: 102 Correct / 6 Incorrect.
- `mu2_correctness`: 101 Correct / 7 Incorrect.
- `mu3_correctness`: 102 Correct / 6 Incorrect.
- `r_rec_succ_localization_correctness`: 105 Correct / 3 Incorrect.
- `overall_test05_correctness`: 98 Correct / 1 Unresolved / 9 Incorrect.

Known rubric / script divergences:

- A reproducible verdict script exists at `7.scoring/add_test05_answer_verdict_columns.py` and emits `add_test05_answer_verdict_columns_report.json`.
- Current rubric credits any mention of `R_rec_succ` at the localization axis, even without confirming the specific ground instance. Stricter rubric would require the ground step or at least the generalized argument (both mu_i tie for i=1,2 or mu3 increases).

Open follow-ups: none blocking.

---

## Test 06 — Branch Realism

Status: **CLOSED 2026-04-20**.

Lean coverage: **complete**. `Test06_BranchRealismCounterexample.lean` proves both helpers false via the nested-`delta` witness: `kappa_rec_delta_step_is_false`, `kappa_rec_succ_drop_is_false`. `rec_succ_ground_counterexample` gives the concrete step `lhs = recDelta void void (delta (delta void)) → rhs = app void (recDelta void void (delta void))` with `kappa rhs = kappa lhs`. Re-exported in `BenchmarkContract.test6_row_backed`.

TTT2 coverage: **not applicable** (helper-strategy audit).

Verdict-column cross-check (`6.extracted-data/csv/test-06-branch-realism-tests.csv`, 108 rows):

- `strategy_sound_correctness`: 75 Correct / 33 Incorrect.
- `kappa_rec_delta_step_correctness`: 74 Correct / 34 Incorrect.
- `kappa_rec_succ_drop_correctness`: 60 Correct / 48 Incorrect.
- `nested_delta_branch_diagnosis_correctness`: 74 Correct / 34 Incorrect.
- `failure_localization_quality`: 74 Correct / 2 Unresolved / 32 Incorrect.
- `counterexample_support_correctness`: 58 Correct / 50 Incorrect.
- `overall_test06_correctness`: 58 Correct / 50 Incorrect.

Known rubric / script divergences:

- `overall_test06_correctness` has no live `Unresolved` rows; the schema permits that bucket but no session lands there.
- Observed overall count (58) happens to equal `counterexample_support_correctness` Correct (58). Documented rule is over the four core axes only; the match appears to be a data artifact. Worth flagging in case a future rerun produces a divergence.

Open follow-ups:

1. Spot-check whether the overall=58 rule actually implements the documented four-axis rule or silently includes counterexample support. If the latter, update the schema to match; if the former, update the audit note with the session-level chain demonstration.

---

## Summary (2026-04-20)

All 9 tests closed. `answer_keys.md` now cites per-question Lean theorems (and, for Schema A / SANS / Test 01, TTT2 artifacts). `answer_key_audit_notes.md` records the verdict-column cross-check per test. The remaining non-blocking follow-ups are rubric refinements only (for example, an optional Test 01 structural-descent promotion branch and the Test 06 overall-rule spot check). No gold answer was changed during the audit.
