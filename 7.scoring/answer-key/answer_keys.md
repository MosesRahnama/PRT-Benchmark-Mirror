# Answer Keys

These notes align the formal answer sources with the current public master
schema files under
`6.extracted-data/schemas`.

For the schema controls and `test-01`, the core object is a method-family table:

- `truth`: the system actually terminates
- `adequate`: the named method is mathematically sound for this system
- `admissible`: the method stays within the benchmark boundary

Verdict labels used below:

- `ok`
- `adequateNotAdmissible`
- `truthOnly`
- `falseNegative`

For `test-02` through `test-06`, the key is task-specific and backed by
dedicated Lean answer-key modules rather than a fixed A-E table.

`schema-test-A-new-system-tests` is currently the exception: it is backed by
the TTT2/CeTA artifacts under `4.TTT2-Artifacts/ttt2/schema-new-system/`, but it is
not yet a separate `Task` in `3.lean/KO7Benchmark/BenchmarkContract.lean`.

---

## Schema A

Prompts:

- `1.test-prompts/Schema-Test-A-prompt.txt`
- `1.test-prompts/Schema-Test-A-Followup-Boundary-prompt.txt`

TRS (duplicating recursive step):

- `2.test-files/Schema-Test-A.trs`
- rules: `F(x, y, Z) -> x` and `F(x, y, S(n)) -> G(y, F(x, y, n))`

### Lean sources

- `3.lean/KO7Benchmark/SchemaTests/SchemaKernel.lean`
  (`KO7Benchmark.SchemaTests.Step`: context-closed step relation).
- `3.lean/KO7Benchmark/SchemaTests/NonlinearWitness.lean`
  (`NonlinearWitness.muW`, `NonlinearWitness.wf_StepRev`: full context-closed SN
  via `μ(F(x,y,n)) = (μy+1)(μn+1) + μx + 1`). This is the theorem-backed
  truth-level witness: Schema A terminates.
- `3.lean/KO7Benchmark/SchemaTests/CandidateA_PathOrderSupport.lean`
  (`CandidateA.candidateA_success_status`: LPO/RPO with precedence
  `F > G > S > Z` succeeds; adequate but out-of-boundary).
- `3.lean/KO7Benchmark/SchemaTests/CandidateB_PolynomialCounterexample.lean`
  (`CandidateB.interpB_not_step_orienting`: `[G(a,b)] = b` fails under
  context closure).
- `3.lean/KO7Benchmark/SchemaTests/CandidateC_KBOFailure.lean`
  (`CandidateC.no_variable_condition_orientation` and
  `CandidateC.uniform_weight_ground_counterexample`: KBO with the standard
  variable condition cannot orient the duplicating rule; the uniform-weight
  ground instance is heavier on the RHS).
- `3.lean/KO7Benchmark/SchemaTests/CandidateD_DependencyPairsWitness.lean` +
  `CandidateD_SoundnessBridge.lean`
  (`CandidateD.wf_DPPairRev`, `CandidateDBridge.candidateD_full_trs_wf`: DP
  with subterm projection to the third argument of `F` proves the DP problem
  well-founded and the full TRS SN).
- `3.lean/KO7Benchmark/SchemaTests/CandidateE_DirectMeasureCounterexample.lean`
  (`CandidateE.muE_not_root_orienting`,
  `CandidateE.muE_not_step_orienting`: the direct descent measure
  `μ(F(x,y,n)) = μn+1`, `μ(G(a,b)) = μb` fails on the base rule
  ground instance `F(S(Z),Z,Z) -> S(Z)` and propagates under context
  closure).
- `3.lean/KO7Benchmark/SchemaTests/GCollapseBarrier.lean`
  (`no_g_left_collapse_orients_step`, `no_g_right_collapse_orients_step`,
  `no_f_arg2_collapse_orients_step` plus function-form corollaries:
  generalizes the CandidateB collapse to every interpretation that drops a
  constructor argument).
- `3.lean/KO7Benchmark/SchemaTests/AnswerKey.lean`: consolidated re-export
  (`candidateA_succeeds`, `candidateB_fails`, `candidateC_fails`,
  `candidateD_pair_problem_succeeds`, `candidateD_full_system_succeeds`,
  `candidateE_fails`).
- `3.lean/KO7Benchmark/BenchmarkContract.lean`
  (`answerKey .schemaA`): triaxial verdict per method family.

### External evidence

- `4.TTT2-Artifacts/ttt2/schema/` reproduces this answer key through TTT2 1.20
  + CeTA certification on the same TRS.
  - CERTIFIED (YES): `Schema_FAST.cpf`, `Schema_HYDRA.cpf`, `Schema_LPO.cpf`,
    `Schema_COMP.cpf`.
  - REJECTED (MAYBE): `Schema_KBO.cpf`, `Schema_POLY.cpf`, `Schema_MAT2.cpf`,
    `Schema_MAT3.cpf`.
  - Full run log: `4.TTT2-Artifacts/ttt2/schema/Schema_CeTA_certification.txt`.

### Correct answer substance (triaxial, per method family)

| Method family | truth | adequate | admissible | Verdict | Lean backing |
|---|---|---|---|---|---|
| `dependencyPairs` | yes | yes | yes | `ok` | `CandidateDBridge.candidateD_full_trs_wf` |
| `nonlinearPoly` | yes | yes | no | `adequateNotAdmissible` | `NonlinearWitness.wf_StepRev` |
| `mpoSpecialized` | yes | yes | no | `adequateNotAdmissible` | PaperB module |
| `pathOrder` | yes | yes | no | `adequateNotAdmissible` | `CandidateA.candidateA_success_status` |
| `polynomial` (generic) | yes | no | no | `truthOnly` | `CandidateB.interpB_not_step_orienting` plus `GCollapseBarrier` |
| `kboStyle` | yes | no | no | `truthOnly` | `CandidateC.no_variable_condition_orientation` |
| `directMeasure` | yes | no | no | `truthOnly` | `CandidateE.muE_not_step_orienting` |
| `affine` | yes | no | no | `truthOnly` | subsumed by `GCollapseBarrier` / `CandidateB` |
| `quadratic` | yes | no | no | `truthOnly` | subsumed by `GCollapseBarrier` / `CandidateB` |
| `rootOnly` | yes | no | no | `truthOnly` | `CandidateE` (same shape) |
| `semanticObjection` | no | no | no | `falseNegative` | `NonlinearWitness.wf_StepRev` refutes |

Note on `polynomial`: the Lean answer key splits generic polynomial
(`truthOnly`) from `nonlinearPoly` (`adequateNotAdmissible`). The public
`method_class = polynomial` vocabulary does not distinguish them, which is why
the Schema A verdict script carries a row-level manual review layer (see
below).

### Mapping to consolidated CSV (`6.extracted-data/csv/schema-test-A-tests.csv`, 108 rows)

Verdict column rubric implemented by
`add_schema_a_answer_verdict_columns.py`:

- `turn1_termination_correctness = Correct` iff `turn1_sn_verdict = yes`.
  Aligned with `NonlinearWitness.wf_StepRev`.
- `turn1_method_mathematical_validity = Correct` iff
  `turn1_norm_primary_method_method_class ∈ {path_order, transformed_calls}`,
  with per-row overrides from `schema_a_method_review_overrides.csv`. The
  polynomial method-class is excluded from the Correct set on the duplicating
  Schema A kernel (Lean theorems `CandidateB.interpB_not_step_orienting` and
  `GCollapseBarrier.no_g_left_function_form_orients_step` refute it). The
  override layer is therefore confirmatory rather than functional for the
  polynomial rows; it remains functional for the path-order kept-correct rows.
- `turn1_method_correct_and_admissible = Correct` iff
  `turn1_norm_primary_method_method_class = transformed_calls`. This is the
  `.ok` row in `answerKey .schemaA`.
- `turn1_method_review_note`: nonblank when the reviewed row was inspected at
  clause level; carries both downgrades and kept-correct confirmations.

Raw evidence columns:

- `turn1_sn_verdict`, `turn2_q4_still_sn`: truth-level, target `yes`.
- `turn1_norm_primary_method_standardized_method_name`,
  `turn1_norm_primary_method_method_class`,
  `turn2_norm_primary_method_standardized_method_name`,
  `turn2_norm_primary_method_method_class`: method family.
- `turn2_q2_imports_external`, `turn2_q3_outside_boundary`: admissibility
  self-report.
- `turn1_flag_duplication_noted`, `turn1_flag_w2_method_named`,
  `turn1_flag_subterm_descent_noted`: rationale flags, not verdict.

Reviewed override rows (16 total in `schema_a_method_review_overrides.csv`):

- 5 G-left-collapse polynomial downgrades, each refuted by
  `KO7Benchmark.SchemaTests.GCollapseBarrier.no_g_left_function_form_orients_step`:
    - `claude-opus-4.5__2026-04-10T14-17-01` (`[G(y, t)] = [t] + 1`)
    - `claude-opus-4.6__2026-04-04T19-37-47` (`[G(a, b)] = b + 1`)
    - `deepseek-v3.2__2026-04-05T07-13-05` (`[G(a, b)] = [b]`)
    - `gpt-5.2__2026-04-04T19-37-12` (`G(y, u) := u`)
    - `gpt-5.3-codex__2026-04-05T10-15-18` (`[G](a, b) = b`)
- 6 explicit-nonlinear-polynomial downgrades, each rejected because Schema A
  `polynomial` is `truthOnly` in the Lean answer key (theorem
  `CandidateB.interpB_not_step_orienting`).
- 5 path-order kept-correct confirmations on rows with explicit LPO/RPO
  precedence (rule already grades them Correct; the override row carries the
  reviewer rationale).

After the rule tightening that drops `polynomial` from the Correct set, the
11 polynomial overrides are confirmatory only (the rule already produces
`Incorrect` on every polynomial row). The 5 path-order overrides remain
informationally meaningful as reviewer-rationale annotations. See
`schema_a_method_review_overrides.csv` for the per-row notes.

Current verdict counts (from
`add_schema_a_answer_verdict_columns_report.json`):

- termination: `Correct = 88`, `Incorrect = 20`.
- math validity: `Correct = 34`, `Incorrect = 74`.
- correct+admissible: `Correct = 2`, `Incorrect = 106`.
- manual overrides applied: 0 (rule and override agree on every reviewed row);
  review notes nonempty: 16.

### Known rubric / script divergences

1. `rootOnly`, `affine`, `quadratic` appear in the Lean `MethodFamily` enum
   but have no public `method_class` label. Rows that would land in these
   families are captured by `method_class ∈ {direct_measure, polynomial}` in
   practice, so the rubric treats them correctly under the tightened rule
   (all three are graded `Incorrect`).

---

## Schema A New System

Prompts:

- `1.test-prompts/Schema-Test-A-New-System-prompt.txt`
- `1.test-prompts/Schema-Test-A-New-System-Followup-Boundary-prompt.txt`

TRS (non-duplicating, unary `G`):

- `2.test-files/Schema-Test-A-New-System.trs`
- rules: `F(x, y, Z) -> x` and `F(x, y, S(n)) -> G(F(x, y, n))`
- the Schema A duplication obstruction is lifted: `y` is not carried into
  the RHS wrapper.

### Lean sources

- `3.lean/KO7Benchmark/SANSTests/SANSKernel.lean`
  (`KO7Benchmark.SANSTests.Step`: context-closed step; no `g_left`/`g_right`
  because `G` is unary).
- `3.lean/KO7Benchmark/SANSTests/LinearWitness.lean`
  (`LinearWitness.mu`, `LinearWitness.mu_step_decreases`,
  `LinearWitness.wf_StepRev`: linear first-order measure
  `μ(F(x,y,n)) = μx + μy + μn + 1`, `μ(G(t)) = μt`,
  `μ(S(t)) = μt + 1`, `μ(Z) = 0`, `μ(var) = 0`; every step strictly
  decreases it, so SN holds under context closure).
- `3.lean/KO7Benchmark/SANSTests/AnswerKey.lean`
  (`canonicalAnswerKey`, `wf_StepRev_SANS`,
  `linear_direct_measure_step_decreasing`, `kbo_variable_condition`,
  `sans_answer_key_bundle`).

### External evidence

- `4.TTT2-Artifacts/ttt2/schema-new-system/` reproduces the answer key on the same
  TRS. **All eight** archived strategies certify:
  - CERTIFIED YES: `FAST`, `HYDRA`, `LPO`, `COMP`, `KBO`, `POLY`, `MAT(2)`,
    `MAT(3)`.
  - Trail: `4.TTT2-Artifacts/ttt2/schema-new-system/Schema_New_System_CeTA_certification.txt`.
  - Summary: `4.TTT2-Artifacts/ttt2/schema-new-system/schema_new_system_certification_summary.json`.
  - Unlike Schema A, POLY / KBO / MAT strategies now all succeed; this
    confirms externally that the rule-extracted termination obstruction
    visible on Schema A is absent here.

### Correct answer substance

- truth-level answer: **yes**, theorem-backed by `LinearWitness.wf_StepRev`.
- `canonicalAnswerKey` fields (all `rfl`-backed):
  - `truth = yes`
  - `duplicationObstruction = lifted`
  - `linearDirectMeasureSuffices = true`
  - `kboVariableConditionHolds = true`
  - `polynomialInterpretationWorks = true`
  - `dependencyPairsWork = true`
  - `pathOrderAdequate = true`
- Method-family gold answers (triaxial):
  - `direct_measure` (linear): **adequate and admissible**.
    Witness: `LinearWitness.mu_step_decreases`.
  - `polynomial` (any linear): adequate. TTT2 POLY certifies.
  - `path_order` (LPO with `F > G > S > Z`): adequate; admissibility depends
    on whether the precedence is treated as imported.
  - `transformed_calls` (DP + subterm on third arg of `F`): adequate and
    admissible; redundant because the direct method already works.
  - `structural_descent` on the third argument of `F`: adequate at the
    argument level when the response explicitly names it; promoted to
    admissible only when paired with the "G has no rules" observation.
  - `kbo` (uniform weights, standard variable condition): adequate on SANS;
    certified by TTT2 KBO.

### Mapping to consolidated CSV (`6.extracted-data/csv/schema-test-A-new-system-tests.csv`, 108 rows)

Verdict column rubric implemented by
`add_schema_a_new_system_answer_verdict_columns.py` (v2, 2026-04-19):

- `turn1_termination_correctness = Correct` iff `turn1_sn_verdict = yes`.
  Aligned with `LinearWitness.wf_StepRev`.
- `turn1_method_mathematical_validity = Correct` iff
  `turn1_sn_verdict = yes` **and** (`method_class ∈ {direct_measure, polynomial, path_order, transformed_calls}` **or** (`method_class = structural_descent` **and** `turn1_flag_subterm_descent_noted = yes`)).
- `turn1_method_correct_and_admissible = Correct` iff
  `turn1_sn_verdict = yes` **and** (`method_class ∈ {direct_measure, transformed_calls}` **or** (`method_class = structural_descent` **and** `turn1_flag_subterm_descent_noted = yes` **and** `turn1_flag_g_inert_noted = yes`)).

The two flag-gated branches encode the first-order argument used by
`LinearWitness.mu_step_decreases`: third-argument strict descent plus `G`
having no rules.

Raw evidence columns:

- `turn1_sn_verdict`, `turn2_q4_still_sn`: truth-level target `yes`.
- `turn1_norm_primary_method_standardized_method_name`,
  `turn1_norm_primary_method_method_class`,
  `turn2_norm_primary_method_standardized_method_name`,
  `turn2_norm_primary_method_method_class`: method family.
- `turn1_flag_subterm_descent_noted`, `turn1_flag_g_inert_noted`,
  `turn1_flag_w2_method_named`: rationale flags used by the v2 rule.
- `turn2_q2_imports_external`, `turn2_q3_outside_boundary`: admissibility
  self-report; not authoritative against the Lean answer.

Current verdict counts (from
`add_schema_a_new_system_answer_verdict_columns_report.json`, 2026-04-20):

- termination: `Correct = 74`, `Incorrect = 34`.
- math validity: `Correct = 73`, `Incorrect = 35`.
- correct+admissible: `Correct = 55`, `Incorrect = 53`.
- method class distribution: `direct_measure = 36`, `objection = 31`,
  `structural_descent = 27`, `polynomial = 9`, `path_order = 4`,
  `structural_induction = 1`.

### Known rubric / script divergences

1. `BenchmarkContract.lean` now exposes a dedicated
  `.schemaANewSystem` task. Its rows cite the SANS answer-key bundle,
  `LinearWitness.wf_StepRev`, and the local SANS support modules for the
  DP / path-order / KBO-backed families.
2. `kbo` does not appear in the live method-class vocabulary for SANS; TTT2
   certifies it, but no row in the 108 is labeled `kbo_style`. No action
   needed unless the extractor vocabulary grows.
3. `structural_induction` appears once in the data and is scored
   `Incorrect` by the rubric. This matches the Lean answer key only under
   the narrow reading that structural induction on `Nat` imports external
   structure. If the response is actually giving third-argument subterm
   descent, the extractor should be labeling it `structural_descent`.
   This is an extraction / normalization concern, not a Lean gap.

---

## Schema B

Prompts:

- `1.test-prompts/Schema-Test-B-prompt.txt` (base: 27 models, single round,
  evaluate methods A-E against the same TRS).
- `1.test-prompts/Schema-Test-B-Control-Clarified-prompt.txt` (control: same
  as base, with a narrow rereading of the boundary constraint).

TRS (same duplicating kernel as Schema A):

- `2.test-files/Schema-Test-B.txt`
- rules: `F(x, y, Z) -> x` and `F(x, y, S(n)) -> G(y, F(x, y, n))`
- five pre-specified methods A-E, each explicitly defined in the test file.

### Lean sources

Schema B uses the same TRS and the same candidate proofs as Schema A. Every
row is theorem-backed.

- `3.lean/KO7Benchmark/SchemaTests/SchemaKernel.lean` (kernel + step).
- `3.lean/KO7Benchmark/SchemaTests/NonlinearWitness.wf_StepRev`
  (truth-level: TRS is SN).
- `3.lean/KO7Benchmark/SchemaTests/CandidateA_PathOrderSupport.candidateA_success_status`
  (method A adequate under LPO precedence `F > G > S > Z`).
- `3.lean/KO7Benchmark/SchemaTests/CandidateB_PolynomialCounterexample.interpB_not_step_orienting`
  (method B polynomial `[G(a,b)] = b` fails under context closure).
- `3.lean/KO7Benchmark/SchemaTests/CandidateC_KBOFailure.no_variable_condition_orientation`
  + `uniform_weight_ground_counterexample` (method C KBO fails by variable
  condition AND by uniform-weight ground instance).
- `3.lean/KO7Benchmark/SchemaTests/CandidateD_DependencyPairsWitness.wf_DPPairRev`
  + `CandidateD_SoundnessBridge.candidateD_full_trs_wf` (method D DP with
  subterm criterion succeeds).
- `3.lean/KO7Benchmark/SchemaTests/CandidateE_DirectMeasureCounterexample.muE_not_step_orienting`
  (method E direct descent fails on the base rule).
- `3.lean/KO7Benchmark/SchemaTests/AnswerKey.lean`: unified re-export.
- `3.lean/KO7Benchmark/BenchmarkContract.lean`:
  - `answerKey .schemaB` table.
  - Row theorems: `schemaB_A_pathOrder_key`, `schemaB_B_polynomial_key`,
    `schemaB_C_kbo_key`, `schemaB_D_dp_key`, `schemaB_E_directMeasure_key`.
  - Proof-backed rows: `schemaB_polynomial_adequacy_refuted`,
    `schemaB_kbo_adequacy_refuted`,
    `schemaB_directMeasure_adequacy_refuted`, `schemaB_dp_row_backed`,
    `schemaB_pathOrder_row_backed`.
  - Table closure: `schemaBTable`, `schemaBTable_fully_correct`,
    `schemaB_only_D_is_admissible`.

### External evidence

`4.TTT2-Artifacts/ttt2/schema/` applies verbatim (same TRS as Schema A).

- CERTIFIED YES (truth-level): FAST, HYDRA, LPO, COMP.
- REJECTED MAYBE: KBO, POLY, MAT(2), MAT(3). These rejections are the
  external mirror of the `CandidateB` / `CandidateC` Lean refutations on
  the same TRS.

### Correct answer substance

| Method | terminates | adequate | admissible | Verdict | Backing theorem |
|---|---|---|---|---|---|
| A (LPO, `F > G > S > Z`) | yes | yes | no | `adequateNotAdmissible` | `CandidateA.candidateA_success_status` + `schemaB_pathOrder_row_backed` |
| B (polynomial, `[G(a,b)] = b`) | yes | no | no | `truthOnly` | `CandidateB.interpB_not_step_orienting` |
| C (KBO, uniform weights) | yes | no | no | `truthOnly` | `CandidateC.no_variable_condition_orientation`, `uniform_weight_ground_counterexample` |
| D (DP + subterm, `π(F) = 3`) | yes | yes | yes | `ok` | `CandidateD.wf_DPPairRev`, `CandidateDBridge.candidateD_full_trs_wf`, `schemaB_dp_row_backed` |
| E (direct descent, `μn+1`) | yes | no | no | `truthOnly` | `CandidateE.muE_not_step_orienting` |

Final answer to the prompt: **only method D satisfies both conditions**,
certified by `schemaB_only_D_is_admissible` (`by decide`).

### Mapping to live consolidated CSV (`6.extracted-data/csv/schema-test-B-tests.csv`, 108 rows)

The current live public file is:

- `6.extracted-data/csv/schema-test-B-tests.csv`

It currently stores the **adjudicated extracted answers**, not a gold-overwritten
answer-key table. Its live columns are:

- `session_slug`, `model`, `provider`, `prompt_variant`
- the 10 A-E answer fields
- `norm_method_D_terminates_rationale_family`
- `norm_both_methods_count`
- `norm_both_methods_has_A` through `norm_both_methods_has_E`

The shared answer-bearing and normalized columns match:

- `6.extracted-data/csv/schema-test-B-tests.csv`

and the reduced source file in turn matches the richer
`SCHEMA_B_data.normalized.csv` on those shared fields.

Gold target values for grading:

- A: `method_A_terminates = yes`, `method_A_in_boundary = no`
- B: `method_B_terminates = no`, `method_B_in_boundary = no`
- C: `method_C_terminates = no`, `method_C_in_boundary = no`
- D: `method_D_terminates = yes`, `method_D_in_boundary = yes`
- E: `method_E_terminates = no`, `method_E_in_boundary = no`
- final both-methods answer: `D` alone, i.e.
  `norm_both_methods_count = 1`, `norm_both_methods_has_D = 1`, and all other
  `norm_both_methods_has_* = 0`

So Schema B grading should now be read as:

1. keep the live public file as the extracted/adjudicated answer surface
2. compare its 10 A-E fields and 6 both-method fields against the gold targets
   above

Current gold-match counts on the live public file (2026-04-20 audit):

- `method_A_terminates = yes`: 102 / 108
- `method_A_in_boundary = no`: 16 / 108
- `method_B_terminates = no`: 13 / 108
- `method_B_in_boundary = no`: 39 / 108
- `method_C_terminates = no`: 100 / 108
- `method_C_in_boundary = no`: 11 / 108
- `method_D_terminates = yes`: 105 / 108
- `method_D_in_boundary = yes`: 107 / 108
- `method_E_terminates = no`: 28 / 108
- `method_E_in_boundary = no`: 23 / 108
- exact `D`-alone selection: 4 / 108
- all 16 gold fields correct: 0 / 108

### Known rubric / script divergences

1. Older helper scripts in `6.extracted-data/` describe a different
   Schema B public-file variant in which the A-E fields were overwritten to the
   gold answer and error-summary columns were appended. That is **not** the
   current live public file.
2. The live public file preserves extracted `moot` and `unclear` values on
   boundary axes instead of collapsing them in the data layer. Grading still
   compares those values against the benchmark gold target (`no` on B, C, E).
3. `prompt_variant = control` does not change the gold answer. Under the formal
   contract, A remains boundary-external and only D satisfies both conditions.

---

## Test 01 — Kernel

Prompts:

- `1.test-prompts/Test-01-Kernel-prompt.txt` (KO7 constructors).
- `1.test-prompts/Test-01-Kernel-Fruit-prompt.txt` (Fruit renaming control).

Files:

- `2.test-files/Test-01-Kernel.lean`: 7-constructor `Trace` with 8 step rules
  (`R_int_delta`, `R_merge_void_left`, `R_merge_void_right`,
  `R_merge_cancel`, `R_rec_zero`, `R_rec_succ`, `R_eq_refl`, `R_eq_diff`).
- `2.test-files/Test-01-Kernel-Fruit.lean`: isomorphic calculus with renamed
  constructors (`plum`/`grape`/`mango`/`peach`/`pear`/`banana`/`cherry`) and
  one added side condition `a ≠ b` on `R_cherry_diff`. The side condition
  restricts the step relation, which only tightens SN.

### Lean sources

- `3.lean/KO7Benchmark/KO7Kernel.lean` (`Trace` + 8-rule `Step`).
- `3.lean/KO7Benchmark/BenchmarkContract.lean`: `answerKey .test1` plus
  row-backed theorems
  - `test1_dp_key`, `test1_directMeasure_not_adequate`,
    `test1_polynomial_not_adequate`, `test1_kbo_not_adequate`,
    `test1_pathOrder_adequate_but_not_admissible`,
    `test1_nonlinearPoly_truth_but_not_admissible`.
  - Authoritative KO7-side backing:
    `test1_dp_row_backed` and `KO7DependencyPairs.wf_DPPairRev`.

### External evidence

- `4.TTT2-Artifacts/ttt2/ko7/` reproduces the answer on the 8-rule KO7 TRS.
  - CERTIFIED YES: `KO7_FAST.cpf`, `KO7_LPO.cpf`, `KO7_COMP.cpf`.
  - REJECTED MAYBE: `KO7_KBO.cpf`, `KO7_POLY.cpf`, `KO7_MAT2.cpf`,
    `KO7_MAT3.cpf`.
  - FBI: MAYBE, no CPF produced.
  - Trail: `4.TTT2-Artifacts/ttt2/ko7/KO7_CeTA_certification.txt`.

### Correct answer substance

Triaxial verdict per method family is exactly the Schema A table (same
answer key object, same Lean-backing pattern; `answerKey .test1` and
`answerKey .schemaA` agree on the 11 families). Summary:

| Method family | Verdict | Backing |
|---|---|---|
| `dependencyPairs` (DP + subterm criterion) | `ok` | `test1_dp_row_backed` |
| `nonlinearPoly` | `adequateNotAdmissible` | `answerKey .test1` row, public answer-key object only |
| `mpoSpecialized` | `adequateNotAdmissible` | `answerKey .test1` row, public answer-key object only |
| `pathOrder` (LPO) | `adequateNotAdmissible` | `test1_pathOrder_adequate_but_not_admissible` + TTT2 `KO7_LPO.cpf` |
| `polynomial` (generic) | `truthOnly` | `test1_polynomial_not_adequate` + TTT2 `KO7_POLY.cpf` REJECTED |
| `kboStyle` | `truthOnly` | `test1_kbo_not_adequate` + TTT2 `KO7_KBO.cpf` REJECTED |
| `directMeasure` | `truthOnly` | `test1_directMeasure_not_adequate` |
| `affine`, `quadratic`, `rootOnly` | `truthOnly` | subsumed by direct / polynomial refutations |
| `semanticObjection` | `falseNegative` | not an accepted proof family in the public answer key |

The KO7 kernel **is** strongly normalizing under context closure.

### Fruit control

The Fruit prompt uses isomorphic constructors plus a side condition
`a ≠ b` on the equality-diff rule. The side condition only restricts the
set of valid Step instances. The public answer chain does not export or
cite a separate rename-invariance theory module; the same answer-key rule
is applied to the KO7 and Fruit rows.

### Mapping to consolidated CSV (`6.extracted-data/csv/test-01-kernel-tests.csv`, 324 rows = 162 KO7 + 162 Fruit)

Verdict column rubric implemented by
`add_test01_answer_verdict_columns.py`:

- `termination_correctness = Correct` iff `sn_verdict = yes`.
- `method_mathematical_validity = Correct` iff
  `norm_primary_method_method_class ∈ {path_order, transformed_calls}`. The
  polynomial method-class is excluded from the Correct set on the KO7 / Fruit
  duplicating kernel; the archived TTT2 certificate `KO7_POLY.cpf` is
  REJECTED for this method family.
- `method_correct_and_admissible = Correct` iff
  `norm_primary_method_method_class = transformed_calls`. This is the
  `ok` row in `answerKey .test1`.

Raw evidence columns:

- `prompt_variant` (`regular` / `control`): derived from `-fruit` suffix in
  `session_slug`; does not change the answer key.
- `sn_verdict`, `sn_verdict_quote`: truth-level.
- `norm_primary_method_*`: method family.
- `primary_answer_mode` (`method` / `objection` / `shortcut_or_local` /
  `unclear`): shape of the response.
- `claims_method_in_boundary`: model's own admissibility claim.
- `transformed_call_signal`, `flag_w2_method_named`,
  `flag_mentions_external_framework`, `flag_mentions_root_only`,
  `flag_size_growing_rule_noted`: rationale flags; not gold-verdict.

Current verdict counts (from
`add_test01_answer_verdict_columns_report.json`):

- termination: `Correct = 222`, `Incorrect = 102`.
- math validity: `Correct = 48`, `Incorrect = 276`.
- correct+admissible: `Correct = 3`, `Incorrect = 321`.
- method class distribution: direct_measure 98, objection 93, path_order
  45, polynomial 42, structural_induction 29, structural_descent 14,
  transformed_calls 3.
- `flag_w2_method_named = yes`: 7 sessions.
- `transformed_call_signal = explicit_w2_method`: 3 sessions;
  `subterm_containment_only`: 60.

### Known rubric / script divergences

1. `structural_induction` (29 rows) and `structural_descent` (14 rows) both
   score `Incorrect` by the rubric. Structural induction on `Nat` or on
   `Trace` imports external induction principles and is correctly marked
   `Incorrect` on admissibility; structural descent is adequate only when the
   model explicitly names third-argument descent (a flag not modeled in the
   current Test 01 rubric). This is a candidate for the same v2 upgrade as
   SANS.

---

## Test 02 — Completion (Nat-Lex scaffold)

Prompt:

- `1.test-prompts/Test-02-Completion-Nat-Lex-prompt.txt`

File:

- `2.test-files/Test-02-Completion-Nat-Lex.lean` (KO7 kernel with 8 rules,
  3 proved local cases, 5 `sorry` cases, lex measure `(kappa, mu)`).

### Lean sources

- `3.lean/KO7Benchmark/KO7Kernel.lean` (the TRS).
- `3.lean/KO7Benchmark/Test02_NatLex_AnswerKey.lean`:
  - `kappa`, `mu`, `measure`, `LexOrder`, `wf_LexOrder`, `drop_left`,
    `drop_right`: reuses the fixture scaffold verbatim.
  - Local-closure theorems: `int_delta_measure_decreases`,
    `rec_zero_measure_decreases`, `eq_refl_measure_decreases`,
    `eq_diff_measure_decreases`.
  - Barrier: `recSuccBarrierLhs`, `recSuccBarrierRhs`,
    `rec_succ_barrier_step`, `rec_succ_barrier_kappa_ties`,
    `rec_succ_barrier_mu_increases`,
    `rec_succ_barrier_not_lex_decreasing`.
  - Global conclusion: `scaffold_not_step_decreasing`.
  - Record: `AnswerKey`, `canonicalAnswerKey`, with
    `primaryTaskOutcome = correct`, `scaffoldStance = scaffoldBroken`,
    `primaryCategory = barrierDiagnosis`,
    `recSuccRequiresBarrierDiagnosis = true`,
    `recSuccKappaTiesOnNestedDelta = true`, plus the four local-closure
    flags.
  - Bundle: `canonical_answer_key_sound` (one global failure + four
    local closures).
- `3.lean/KO7Benchmark/BenchmarkContract.lean::test2_row_backed` re-exports
  the scaffold stance and the step-not-lex-decreasing refutation.

### Correct answer substance

- the supplied `(kappa, mu)` scaffold is **broken**
  (`scaffold_not_step_decreasing`).
- the decisive obstruction is `R_rec_succ` on the nested
  `delta (delta void)` witness (`rec_succ_barrier_step` +
  `rec_succ_barrier_kappa_ties` + `rec_succ_barrier_mu_increases`).
- `R_int_delta`, `R_rec_zero`, `R_eq_refl`, `R_eq_diff` already close
  under the supplied measure.

### Mapping to consolidated CSV (`6.extracted-data/csv/test-02-completion-tests-nat-lex.csv`, 108 rows)

Verdict column rubric implemented by
`7.scoring/add_test02_answer_verdict_columns.py`:

- `completion_claim_correctness = Correct` iff `completion_claim = no`;
  `Unresolved` iff `completion_claim = partial`; else `Incorrect`.
- `rec_succ_obstruction_diagnosis_correctness = Correct` iff
  `rec_succ_obstruction_identified = yes`, else `Incorrect`.
- `overall_test02_correctness`: `Correct` iff
  `completion_claim = no` AND `rec_succ_obstruction_identified = yes`;
  `Unresolved` when `completion_claim = partial` or when
  `completion_claim = no` but the obstruction is not identified; else
  `Incorrect`.

Raw evidence columns:

- `completion_claim` (`yes`, `no`, `partial`): gold target `no`.
- `rec_succ_obstruction_identified` (`yes`, `no`): gold target `yes`.
- `completion_claim_quote`, `rec_succ_obstruction_quote`: verbatim
  evidence.

Current counts (sampled 2026-04-22):

- `completion_claim`: `yes = 67`, `no = 14`, `partial = 27`.
- `rec_succ_obstruction_identified`: `yes = 15`, `no = 93`.
- `completion_claim_correctness`: `Correct = 14`, `Unresolved = 27`,
  `Incorrect = 67`.
- `rec_succ_obstruction_diagnosis_correctness`: `Correct = 15`,
  `Incorrect = 93`.
- `overall_test02_correctness`: `Correct = 14`, `Unresolved = 27`,
  `Incorrect = 67`.

### Known rubric / script divergences

1. A reproducible verdict script now exists at:
   - `7.scoring/add_test02_answer_verdict_columns.py`
   - `test-02-completion-tests-nat-lex/3.extraction/add_test02_answer_verdict_columns.py`
   It rebuilds the three correctness columns from
   `test-02-completion-tests-nat-lex/3.extraction/TEST02_data.csv`
   and writes both the extraction-local and public `6.extracted-data/csv/test-02-completion-tests-nat-lex.csv`
   files. The only remaining non-reproducible helper field is
   `quote_spawn_versus_answer_mismatch`, which is preserved from an existing
   public final file.
2. `overall_test02_correctness` currently tracks `completion_claim_correctness` exactly
   (14 / 27 / 67). The schema defines a second-tier `Unresolved` when
   `completion_claim = no` but the obstruction is not identified, but
   in the current 108 rows every `completion_claim = no` row also has
   `rec_succ_obstruction_identified = yes`, so the "missed-barrier"
   refinement has no live signal. If it must be auditable, a future pass
   should spot-check the 14 `completion_claim = no` rows.

---

## Test 03 — Completion (Ordinal scaffold)

Prompt:

- `1.test-prompts/Test-03-Completion-Ordinal-prompt.txt`

File:

- `2.test-files/Test-03-Completion-Ordinal.lean` (KO7 kernel, 8 rules, 5
  proved local cases, 3 `sorry` remaining: `R_rec_succ`, `R_eq_refl`,
  `R_eq_diff`; ordinal measure in `omega0^*`).

### Lean sources

- `3.lean/KO7Benchmark/KO7Kernel.lean` (the TRS).
- `3.lean/KO7Benchmark/Test03_Ordinal_AnswerKey.lean`:
  - `mu` (ordinal measure, reused from fixture).
  - Easy-case theorems (all closed):
    `int_delta_measure_decreases`, `merge_void_left_measure_decreases`,
    `merge_void_right_measure_decreases`, `merge_cancel_measure_decreases`,
    `rec_zero_measure_decreases`, `eq_refl_measure_decreases`.
  - Hard-case obligations (left as `Prop` parameters):
    `RecSuccObligation`, `EqDiffObligation`.
  - Conditional closure:
    `mu_decreases_of_hard_obligations`,
    `strong_normalization_of_hard_obligations`.
  - Independent root-step closure:
    `acc_root_step`, `strong_normalization_closed`.
  - Record + bundle: `AnswerKey`, `canonicalAnswerKey`,
    `canonical_answer_key_sound` (viable-but-incomplete stance + 6 easy
    closures + an unconditional root-step SN theorem + 2 hard obligations
    imply the scaffold-specific ordinal-measure proof).
- `3.lean/KO7Benchmark/BenchmarkContract.lean::test3_row_backed`.

### Correct answer substance

- the ordinal scaffold is **viable but incomplete**.
- six rule branches close mechanically under the supplied `mu`
  (every rule except `R_rec_succ` and `R_eq_diff`).
- the full strong-normalization proof reduces to **two** substantive
  hard obligations: `R_rec_succ` (`RecSuccObligation`) and `R_eq_diff`
  (`EqDiffObligation`).
- independent of the published ordinal-measure scaffold, the root-step
  relation is now closed by `strong_normalization_closed`. This proves the
  Test 03 SN truth clause without assuming the two scaffold-specific ordinal
  inequalities.
- in the **fixture as published**, 5 of 8 rule cases carry a proof
  and 3 are `sorry`: `R_rec_succ`, `R_eq_refl`, `R_eq_diff`.
  `R_eq_refl` is left as `sorry` in the fixture but closes by
  `eq_refl_measure_decreases` in the Lean answer key (it is a routine
  positivity argument). So the aligned gold answer identifies three
  remaining target labels but treats `R_eq_refl` as easy support rather
  than a theorem-backed hard obligation.

### Mapping to consolidated CSV (`6.extracted-data/csv/test-03-completion-tests-ordinal.csv`, 108 rows)

Verdict column rubric implemented by
`add_test03_answer_verdict_columns.py`:

- `hard_case_delivery_correctness`: `Correct` when both `r_rec_succ_delivery`
  and `r_eq_diff_delivery` are `closed_code` or `open_code`;
  `Unresolved` when both are non-`missing` but at least one is only
  `prose_only`; `Incorrect` when either is `missing`.
- `eq_refl_support_correctness`: `Correct` when `r_eq_refl_delivery`
  is any non-`missing` value; else `Incorrect`.
- `remaining_case_targeting_correctness`: `Correct` iff
  `remaining_case_labels_correct = yes`.
- `response_scope_correctness`: `Correct` iff
  `non_remaining_case_material_present = no`.
- `overall_test03_correctness`: combined verdict across hard-case delivery,
  easy-case support, targeting, and scope (see schema for the exact
  lattice).

Raw evidence columns:

- `r_rec_succ_delivery`, `r_eq_refl_delivery`, `r_eq_diff_delivery`:
  delivery shape (`closed_code` / `open_code` / `prose_only` / `missing`).
- `remaining_case_labels_correct`, `non_remaining_case_material_present`:
  scope / targeting.

Current counts (from
`add_test03_answer_verdict_columns_report.json`, refreshed 2026-04-22 after the
targeted raw-session repair):

- `r_rec_succ_delivery`: open_code 83, closed_code 10, prose_only 13,
  missing 2.
- `r_eq_refl_delivery`: closed_code 88, open_code 6, prose_only 11,
  missing 3.
- `r_eq_diff_delivery`: open_code 82, closed_code 10, prose_only 13,
  missing 3.
- `hard_case_delivery_correctness`: 93 / 12 / 3.
- `eq_refl_support_correctness`: 105 / 3.
- `remaining_case_targeting_correctness`: 103 / 5.
- `response_scope_correctness`: 102 / 6.
- `overall_test03_correctness`: 88 Correct, 12 Unresolved, 8 Incorrect.

### Known rubric / script divergences

1. The rubric gives `closed_code` and `open_code` equal credit at the
   hard-case delivery axis; only `prose_only` triggers `Unresolved`.
   That is a stylistic rather than mathematical decision: a rigorous
   `sorry` with a well-named target is rated as addressed. If the
   downstream analysis wants to single out fully closed proofs, a
   separate strict column (`closed_code` only) would need to be added.
2. The Lean answer key closes `R_eq_refl` (easy), but the fixture
   leaves it as `sorry`. The rubric reflects this: `r_eq_refl_delivery`
   feeds the "easy support" column, not the hard-case column.

---

## Test 04 — Measure Verification

Prompt:

- `1.test-prompts/Test-04-Measure-Verification-prompt.txt`

File:

- `2.test-files/Test-04-Measure-Verification.lean` (KO7 kernel, 8 rules,
  proposed measure `(phase, cost)` where `phase = 1` only when the `recDelta`
  third argument is `delta`-wrapped; else `phase = 0`).

### Lean sources

- `3.lean/KO7Benchmark/KO7Kernel.lean` (the TRS).
- `3.lean/KO7Benchmark/Test04_MeasureVerificationCounterexample.lean`:
  - `phase`, `cost`, `measure`, `LexLt`: match the fixture.
  - `rec_succ_measure_decreases`: the decoy branch `R_rec_succ` actually
    lex-decreases (phase drops from 1 to 0). This is the distracting
    "good" case in the proposed measure.
  - `exposedCounterexample := recDelta void void (delta void)`.
  - `merge_void_left_exposes_high_phase`: `Step (merge void e) e` holds;
    on the left side `phase = 0`, on the right side `phase = 1`.
    The `measure` as a tuple rises from `(0, …)` to `(1, …)`.
  - `measure_not_step_decreasing`: global conclusion.
- `3.lean/KO7Benchmark/BenchmarkContract.lean::test4_row_backed` re-exports
  the refutation.

### Correct answer substance

- the proposed lexicographic measure is **unsound**
  (`measure_not_step_decreasing`).
- `R_rec_succ` is a decoy — it actually decreases the lex pair because
  `phase` drops from 1 to 0 (`rec_succ_measure_decreases`). Citing
  `R_rec_succ` is a common wrong localization.
- the true failure is any wrapper-removal rule that exposes a
  `recDelta _ _ (delta _)` subterm at the root, because `phase` is a
  root-only predicate. The concrete Lean witness uses `R_merge_void_left`
  on `merge void (recDelta void void (delta void))`.

### Mapping to consolidated CSV (`6.extracted-data/csv/test-04-measure-verification-tests.csv`, 108 rows)

Verdict column rubric implemented by
`7.scoring/add_test04_answer_verdict_columns.py`:

- `measure_sound_correctness = Correct` iff `measure_sound_yes_no = no`.
  Matches `measure_not_step_decreasing`.
- `phase_exposure_localization_correctness = Correct` iff
  `phase_exposure_cited = yes`.
- `overall_test04_correctness`: `Correct` iff both above are `Correct`;
  `Unresolved` iff the measure is rejected but the wrapper-exposure
  localization is missing; `Incorrect` iff the response says the
  measure is sound.

Raw evidence columns:

- `measure_sound_yes_no` (`yes`, `no`): gold target `no`.
- `r_rec_succ_cited` (`yes`, `no`): diagnostic only; a `yes` on
  `R_rec_succ` alone is a wrong localization.
- `phase_exposure_cited` (`yes`, `no`): gold target `yes` for a correct
  localization.
- `measure_sound_quote`: verbatim evidence.
- `self_correction_flag`, `self_contradiction_flag`, `review_notes`: not
  answer-bearing.

Current counts (sampled 2026-04-20):

- `measure_sound_yes_no`: `no = 84`, `yes = 24`.
- `r_rec_succ_cited`: `yes = 87`, `no = 21`.
- `phase_exposure_cited`: `yes = 75`, `no = 33`.
- `measure_sound_correctness`: `Correct = 84`, `Incorrect = 24`.
- `phase_exposure_localization_correctness`: `Correct = 75`,
  `Incorrect = 33`.
- `overall_test04_correctness`: `Correct = 74`, `Unresolved = 10`,
  `Incorrect = 24`.

### Known rubric / script divergences

1. `r_rec_succ_cited = yes` with `phase_exposure_cited = no` is a
   common failure mode (the response names a plausible but wrong
   branch). The rubric captures this via `Unresolved`, not `Incorrect`.
   That is a generous reading; a stricter rubric could require the
   correct localization for full credit.

---

## Test 05 — Candidate Class Reasoning

Prompt:

- `1.test-prompts/Test-05-Candidate-Class-Reasoning-prompt.txt`

File:

- `2.test-files/Test-05-Candidate-Class-Reasoning.lean` (KO7 kernel, 8 rules,
  three candidate additive measures `mu1`, `mu2`, `mu3`).

### Lean sources

- `3.lean/KO7Benchmark/KO7Kernel.lean` (the TRS).
- `3.lean/KO7Benchmark/Test05_CandidateClassCounterexamples.lean`:
  - `mu1`, `mu2`, `mu3` (fixture definitions reused verbatim).
  - `lhs := recDelta void void (delta void)`,
    `rhs := app void (recDelta void void void)`.
  - `rec_succ_ground_step : Step lhs rhs`: the single step that breaks
    all three candidates.
  - `mu1_ground_counterexample`: `mu1 lhs = mu1 rhs` (tie).
  - `mu2_ground_counterexample`: `mu2 lhs = mu2 rhs` (tie).
  - `mu3_ground_counterexample`: `mu3 lhs < mu3 rhs` (increases).
  - `mu1_not_root_orienting`, `mu2_not_root_orienting`,
    `mu3_not_root_orienting`: all three fail to orient the step.
- `3.lean/KO7Benchmark/BenchmarkContract.lean::test5_row_backed` re-exports
  the `mu1` refutation.

### Correct answer substance

- all three candidates fail
  (`mu1_not_root_orienting`, `mu2_not_root_orienting`,
  `mu3_not_root_orienting`).
- the decisive shared obstruction is `R_rec_succ` on the ground step
  `recDelta void void (delta void) → app void (recDelta void void void)`.
- `mu1` and `mu2` tie on that step (same total weight on LHS and RHS).
- `mu3` strictly increases on that step.

### Mapping to consolidated CSV (`6.extracted-data/csv/test-05-candidate-class-reasoning-tests.csv`, 108 rows)

Verdict column rubric implemented by
`7.scoring/add_test05_answer_verdict_columns.py`:

- `mu1_correctness = Correct` iff `mu1_yes_no = no`. Aligned with
  `mu1_not_root_orienting`.
- `mu2_correctness = Correct` iff `mu2_yes_no = no`.
- `mu3_correctness = Correct` iff `mu3_yes_no = no`.
- `r_rec_succ_localization_correctness = Correct` iff
  `r_rec_succ_cited = yes`.
- `overall_test05_correctness`: `Correct` iff all three candidate
  verdicts are `no` AND the shared `R_rec_succ` obstruction is cited;
  `Unresolved` iff all three are `no` but the shared obstruction is
  missing; else `Incorrect`.

Raw evidence columns:

- `mu1_yes_no`, `mu2_yes_no`, `mu3_yes_no` (`yes`, `no`): gold target
  `no` on all three.
- `r_rec_succ_cited` (`yes`, `no`): gold target `yes`.
- `response_truncated_flag`, `tool_spill_flag`,
  `self_correction_flag`, `self_contradiction_flag`, `adjudicator_notes`:
  not answer-bearing.

Current counts (sampled 2026-04-20):

- `mu1_yes_no`: `no = 102`, `yes = 6`.
- `mu2_yes_no`: `no = 101`, `yes = 7`.
- `mu3_yes_no`: `no = 102`, `yes = 6`.
- `r_rec_succ_cited`: `yes = 105`, `no = 3`.
- `overall_test05_correctness`: `Correct = 98`, `Unresolved = 1`,
  `Incorrect = 9`.

### Known rubric / script divergences

1. The "single shared obstruction" framing (`R_rec_succ`) in the schema
   is strictly correct for the fixture's three candidates. The Lean
   layer uses one concrete ground step; a response that names
   `R_rec_succ` in general but does not verify it on that step still
   scores `Correct` on `r_rec_succ_localization_correctness` under the
   current rubric.

---

## Test 06 — Branch Realism

Prompt:

- `1.test-prompts/Test-06-Branch-Realism-prompt.txt`

File:

- `2.test-files/Test-06-Branch-Realism.lean` (KO7 kernel, 8 rules,
  structural measure `kappa`, two sorry-bearing helper theorems:
  `kappa_rec_delta_step` and `kappa_rec_succ_drop`).

### Lean sources

- `3.lean/KO7Benchmark/KO7Kernel.lean` (the TRS).
- `3.lean/KO7Benchmark/Test06_BranchRealismCounterexample.lean`:
  - `kappa` (matches the fixture).
  - Concrete witness: `lhs := recDelta void void (delta (delta void))`,
    `mid := recDelta void void (delta void)`,
    `rhs := app void mid`.
  - `nested_delta_values`: `kappa lhs = 1`, `kappa mid = 1`,
    `kappa rhs = 1` — all three agree, which is the whole point.
  - `rec_succ_nested_delta_step : Step lhs rhs`.
  - `rec_succ_ground_counterexample`: `kappa rhs = kappa lhs` (tie, so
    `kappa` does not strictly decrease on this `R_rec_succ`).
  - `kappa_rec_delta_step_is_false`: the first helper is false on
    `n = delta void`. Concretely `kappa (recDelta b s (delta (delta n))) =
    kappa (recDelta b s (delta n))` when the inner `delta` already
    contributes the `+1`, so the claimed equality `... = kappa (recDelta b
    s n) + 1` does not hold for all `n`.
  - `kappa_rec_succ_drop_is_false`: the second helper is false because
    it rewrites using the false first helper.
- `3.lean/KO7Benchmark/BenchmarkContract.lean::test6_row_backed` re-exports
  `kappa_rec_delta_step_is_false`.

### Correct answer substance

- the helper strategy is **unsound**
  (`kappa_rec_delta_step_is_false`, `kappa_rec_succ_drop_is_false`).
- `kappa_rec_delta_step` is the fundamental bug: it asserts
  `kappa (recDelta b s (delta n)) = kappa (recDelta b s n) + 1` for all
  `n`, but `kappa` already gave the `+1` when the old `n` was itself a
  `delta _`.
- `kappa_rec_succ_drop` is a downstream bug: its proof rewrites using
  the broken first helper, so it fails on the same nested-`delta`
  witness.
- the critical case is `n = delta m` (equivalently, the LHS `delta`
  wraps another `delta`).
- the cleanest aligned answer names `kappa_rec_delta_step` as the root
  cause and gives the nested-`delta` counterexample.

### Mapping to consolidated CSV (`6.extracted-data/csv/test-06-branch-realism-tests.csv`, 108 rows)

Verdict column rubric implemented by
`add_test06_answer_verdict_columns.py`:

- `strategy_sound_correctness = Correct` iff
  `strategy_sound_verdict = unsound`.
- `kappa_rec_delta_step_correctness = Correct` iff
  `kappa_rec_delta_step_verdict = fails`.
- `kappa_rec_succ_drop_correctness = Correct` iff
  `kappa_rec_succ_drop_verdict = fails`.
- `nested_delta_branch_diagnosis_correctness = Correct` iff
  `n_equals_delta_m_cited = yes`.
- `failure_localization_quality`: `Correct` when
  `first_named_failure_point = kappa_rec_delta_step`,
  `Unresolved` when `first_named_failure_point = kappa_rec_succ_drop`,
  else `Incorrect`.
- `counterexample_support_correctness = Correct` iff
  `concrete_counterexample_provided = yes`.
- `overall_test06_correctness`: `Correct` when strategy=unsound AND
  both helper verdicts=fails AND nested-delta cited; schema permits
  `Unresolved` when those are correct but nested-delta is missing;
  else `Incorrect`.

Raw evidence columns:

- `condition` (`run1`-`run5`): multi-run condition label.
- `strategy_sound_verdict`, `kappa_rec_delta_step_verdict`,
  `kappa_rec_succ_drop_verdict`, `n_equals_delta_m_cited`,
  `first_named_failure_point`, `concrete_counterexample_provided`:
  raw extractions.
- `strategy_sound_quote`: verbatim evidence.

Current counts (from
`add_test06_answer_verdict_columns_report.json`, 2026-04-20):

- `condition`: run1/run2/run3/run4/run5 = 27/27/26/27/1.
- `strategy_sound_verdict`: unsound 75, sound 31, mixed 2.
- `kappa_rec_delta_step_verdict`: fails 74, holds 34.
- `kappa_rec_succ_drop_verdict`: fails 60, holds 38, unclear 10.
- `n_equals_delta_m_cited`: yes 74, no 34.
- `first_named_failure_point`: kappa_rec_delta_step 74, none 31,
  kappa_rec_succ_drop 2, other 1.
- `concrete_counterexample_provided`: yes 58, no 50.
- `overall_test06_correctness`: Correct 58, Incorrect 50.

### Known rubric / script divergences

1. The schema permits an `Unresolved` bucket for
   `overall_test06_correctness` (strategy + both helpers correct but
   nested-delta missing). In the current 108 rows this bucket does not
   fire: every row with both helpers judged `fails` also cites the
   nested-delta branch.
2. The observed overall count (58) equals the `counterexample_support_correctness`
   Correct count exactly. The documented `overall_test06_correctness`
   rule is over the four core axes (strategy + 2 helpers + nested-delta);
   counterexample support is separate. The overlap here appears to be
   an artifact of the data, not a rule change — every session with the
   four core axes all Correct also provided a concrete counterexample.
   Worth checking if a future rerun produces a divergence.
