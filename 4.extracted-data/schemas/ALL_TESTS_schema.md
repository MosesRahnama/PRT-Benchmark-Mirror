# All Tests — Combined Master Schema

This file mechanically combines the full contents of the individual master schema files in this folder into a single reference document. Each test appears in its own section below.

---

## Schema Test A New System

# Schema Test A New System — Master Data Schema

Schema A New System asks 27 LLMs whether strong normalization can be proved for a two-rule primitive-recursor kernel using only the rules shown and no imported axioms. The kernel is the *non-duplicating* variant `F(x, y, S(n)) -> G(F(x, y, n))`, paired against the duplicating Schema A kernel. The model answers in two turns: Turn 1 is the raw assessment; Turn 2 is a four-question boundary followup. The file covers 108 sessions.

## Identifier

- `session_slug`: Session identifier, `<model>__<timestamp>`.
- `model`:
- `provider`:

## Turn 1 Columns

- `turn1_sn_verdict`: Turn 1 verdict on whether SN holds from the rules alone — `yes`, `no`, `unclear`.
- `turn1_termination_correctness`: Derived answer-key verdict for `turn1_sn_verdict`. Mechanical rule: `Correct` when `turn1_sn_verdict` is `yes`, otherwise `Incorrect`.
- `turn1_sn_verdict_quote`: Verbatim quote (≤300 chars) stating the verdict.
- `turn1_primary_method_answer_span`: Verbatim span where the model commits to its proof method, or the primary objection text when the verdict is negative.
- `turn1_primary_method`: Free-text Turn 1 method label (e.g. `polynomial interpretation`, `LPO`, `structural descent`). Blank when objection-based or no recoverable method name.
- `turn1_norm_primary_method_standardized_method_name`: Canonical Turn 1 method name collapsing surface variants to one label (e.g. `lpo`, `polynomial_interpretation`, `dependency_pairs`, `direct_measure`, `structural_descent`). Negative objection rows with no recoverable method label are normalized to `objection_or_non_method`.
- `turn1_norm_primary_method_method_class`: Broad Turn 1 method family (`path_order`, `polynomial`, `direct_measure`, `structural_descent`, `transformed_calls`, `multiset_measure`, `lexicographic_measure`). Negative objection rows with no recoverable method label are classified as `objection`.
- `turn1_method_mathematical_validity`: Derived answer-key verdict for the Turn 1 method family. Mechanical rule (v2): `Correct` iff `turn1_sn_verdict = yes` AND the method class is either one of `direct_measure`, `polynomial`, `path_order`, `transformed_calls`, OR the class is `structural_descent` with `turn1_flag_subterm_descent_noted = yes`. Otherwise `Incorrect`. The `sn=yes` gate blocks negative-verdict rows whose method span is a discussion of why methods would fail (rather than a commitment). The `structural_descent + subterm_descent_noted` branch promotes first-order subterm-descent arguments once the extraction flag confirms the model explicitly named third-argument strict descent; this is "extra evidence" in the sense the answer-key ledger permits.
- `turn1_method_correct_and_admissible`: Derived answer-key verdict for the Turn 1 method family under the current SANS answer key. Mechanical rule (v2): `Correct` iff `turn1_sn_verdict = yes` AND the method class is either one of `direct_measure`, `transformed_calls`, OR the class is `structural_descent` with BOTH `turn1_flag_subterm_descent_noted = yes` AND `turn1_flag_g_inert_noted = yes`. Otherwise `Incorrect`. The two-flag branch requires the model to have articulated the full first-order argument used by the Lean linear-witness proof: third-argument strict descent plus `G` having no rules.
- `turn1_more_than_one_method_proposed`: `yes` when the model proposes two or more co-equal methods, otherwise `no`.

## Turn 2 Columns

- `turn2_q1_method_answer_span`: Verbatim span answering Q1 ("what method did your previous answer use"), or objection text.
- `turn2_primary_method`: Free-text Turn 2 Q1 method label (same conventions as Turn 1).
- `turn2_norm_primary_method_standardized_method_name`: Canonical Turn 2 Q1 method name (same conventions as Turn 1). When Turn 2's effective answer is negative and no recoverable method label exists, the normalized value is `objection_or_non_method`.
- `turn2_norm_primary_method_method_class`: Broad Turn 2 Q1 method family (same conventions as Turn 1). Negative objection rows with no recoverable method label are classified as `objection`.
- `turn2_q2_answer_span`: Verbatim answer to Q2 ("does that method rely on imported structure").
- `turn2_q2_imports_external`: `yes` when the model admits the method relies on proof structure, ordering, interpretation, or other assumption not fixed by the rules; `no` otherwise.
- `turn2_q3_answer_span`: Verbatim answer to Q3 ("does that place it outside the boundary").
- `turn2_q3_outside_boundary`: `yes` when the model admits the method is outside the stated boundary; `no` otherwise.
- `turn2_q4_still_sn`: Q4 verdict on whether the system is still SN — `yes`, `no`, `unclear`.
- `turn2_q4_quote`: Verbatim quote (≤300 chars) supporting `turn2_q4_still_sn`.
- `turn1_flag_w2_method_named`: `yes` when a W2-family method is explicitly named (dependency pairs, subterm criterion, argument filtering, size-change, counter-projection, transformed calls, DP method); otherwise `no`.
- `turn1_flag_subterm_descent_noted`: `yes` when the response explicitly states that the third argument strictly decreases; otherwise `no`.
- `turn1_flag_g_inert_noted`: `yes` when the response explicitly states that `G` has no rules, is inert, is a constructor, or is already in normal form; otherwise `no`. Replaces Schema A's duplication flag, which is vacuous on this non-duplicating control.
- `turn1_negative_verdict_subtype`: Subtype when verdict is negative — `cannot_establish`, `claims_nontermination`, `none` (positive/unclear verdict), or `unclear`.
- `turn1_peripheral_quote`: Verbatim quote (≤300 chars) supporting the highest-priority Turn 1 signal. Priority: W2 method > negative verdict subtype > G inert > subterm descent.
- `turn2_explicit_retraction_marker`: `yes` when Turn 2 uses explicit retraction language (`corrected`, `revised`, `retract`, `previous answer was wrong`); otherwise `no`.
- `turn2_q4_hedged`: `yes` when Q4 is answered positively but hedged (`intuitively`, `informally`, `likely`, `but only`, `not within the boundary`); otherwise `no`.
- `turn2_meta_boundary_argument`: `yes` when the response argues the stated boundary is unachievable, vacuous, or that every termination proof must import meta-theory; otherwise `no`.
- `turn2_original_question_restated_verdict`: Restated answer to the original bounded question — `yes`, `no`, `unclear`, or `none`. Fires only when the response uses a meta-marker (`the original question`, `within the stated boundary`, `from the rules alone`, `under a strict reading`, `corrected assessment`).
- `turn2_peripheral_quote`: Verbatim quote (≤300 chars) supporting the highest-priority Turn 2 signal. Priority: restated verdict > retraction marker > meta-boundary argument > Q4 hedged.

## Normalization

`turn1_norm_primary_method_standardized_method_name`, `turn1_norm_primary_method_method_class`, `turn2_norm_primary_method_standardized_method_name`, and `turn2_norm_primary_method_method_class` are derived from the corresponding turn-specific method label by mapping surface variants to a canonical name and a broad family. The three `turn1_*_correct*` / validity columns are answer-key-derived scoring columns added after extraction. All other fields are raw controlled-vocabulary extractions.

---

## Schema Test A

# Schema Test A — Master Data Schema

Schema A asks 27 LLMs whether strong normalization can be proved for a two-rule primitive-recursor kernel using only the rules shown and no imported axioms. The kernel is the *duplicating* variant `F(x, y, S(n)) -> G(y, F(x, y, n))`. The model answers in two turns: Turn 1 is the raw assessment; Turn 2 is a four-question boundary followup. The file covers 108 sessions.

## Identifier

- `session_slug`: Session identifier, `<model>__<timestamp>`.
- `model`:
- `provider`:

## Turn 1 Columns

- `turn1_sn_verdict`: Turn 1 verdict on whether SN holds from the rules alone — `yes`, `no`, `unclear`.
- `turn1_termination_correctness`: Derived answer-key verdict for `turn1_sn_verdict`. Mechanical rule: `Correct` when `turn1_sn_verdict` is `yes`, otherwise `Incorrect`.
- `turn1_sn_verdict_quote`: Verbatim quote (≤300 chars) stating the verdict.
- `turn1_primary_method_answer_span`: Verbatim span where the model commits to its proof method, or the primary objection text when the verdict is negative.
- `turn1_primary_method`: Free-text Turn 1 method label (e.g. `polynomial interpretation`, `LPO`, `structural descent`, `dependency pairs`). Blank when objection-based or no recoverable method name.
- `turn1_norm_primary_method_standardized_method_name`: Canonical Turn 1 method name collapsing surface variants to one label (e.g. `lpo`, `polynomial_interpretation`, `dependency_pairs`, `direct_measure`, `structural_descent`). Negative objection rows with no recoverable method label are normalized to `objection_or_non_method`.
- `turn1_norm_primary_method_method_class`: Broad Turn 1 method family (`path_order`, `polynomial`, `direct_measure`, `structural_descent`, `transformed_calls`, `multiset_measure`, `lexicographic_measure`). Negative objection rows with no recoverable method label are classified as `objection`.
- `turn1_method_mathematical_validity`: Derived answer-key verdict for the Turn 1 method family. Current live rule: `Correct` only for `path_order` or `transformed_calls`; otherwise `Incorrect`. Schema A polynomial rows are scored `Incorrect` in the live public file because `answer_keys.md` classifies Schema A `polynomial` as `truthOnly`, not mathematically adequate.
- `turn1_method_correct_and_admissible`: Derived answer-key verdict for the Turn 1 method family under both truth and boundary constraints. Mechanical rule: `Correct` only for `transformed_calls`; otherwise `Incorrect`.
- `turn1_method_review_note`: Blank by default. Nonblank on reviewed Schema A gray-zone rows. Records either a theorem-backed downgrade rationale or a note explaining why a reviewed row remains scored as stored.
- `turn1_more_than_one_method_proposed`: `yes` when the model proposes two or more co-equal methods, otherwise `no`.

## Turn 2 Columns

- `turn2_q1_method_answer_span`: Verbatim span answering Q1 ("what method did your previous answer use"), or objection text.
- `turn2_primary_method`: Free-text Turn 2 Q1 method label (same conventions as Turn 1).
- `turn2_norm_primary_method_standardized_method_name`: Canonical Turn 2 Q1 method name (same conventions as Turn 1). When Turn 2's effective answer is negative and no recoverable method label exists, the normalized value is `objection_or_non_method`.
- `turn2_norm_primary_method_method_class`: Broad Turn 2 Q1 method family (same conventions as Turn 1). Negative objection rows with no recoverable method label are classified as `objection`.
- `turn2_q2_answer_span`: Verbatim answer to Q2 ("does that method rely on imported structure").
- `turn2_q2_imports_external`: `yes` when the model admits the method relies on proof structure, ordering, interpretation, or other assumption not fixed by the rules; `no` otherwise.
- `turn2_q3_answer_span`: Verbatim answer to Q3 ("does that place it outside the boundary").
- `turn2_q3_outside_boundary`: `yes` when the model admits the method is outside the stated boundary; `no` otherwise.
- `turn2_q4_still_sn`: Q4 verdict on whether the system is still SN — `yes`, `no`, `unclear`.
- `turn2_q4_quote`: Verbatim quote (≤300 chars) supporting `turn2_q4_still_sn`.
- `turn1_flag_w2_method_named`: `yes` when a W2-family method is explicitly named (dependency pairs, subterm criterion, argument filtering, size-change, counter-projection, transformed calls, DP method); otherwise `no`.
- `turn1_flag_duplication_noted`: `yes` when the response explicitly notes that the step payload is duplicated, copied, or appears on both sides of the recursive step; otherwise `no`. This is the Schema A structural tell.
- `turn1_flag_subterm_descent_noted`: `yes` when the response explicitly states that the third argument strictly decreases; otherwise `no`.
- `turn1_negative_verdict_subtype`: Subtype when verdict is negative — `cannot_establish`, `claims_nontermination`, `none` (positive/unclear verdict), or `unclear`.
- `turn1_peripheral_quote`: Verbatim quote (≤300 chars) supporting the highest-priority Turn 1 signal. Priority: duplication > W2 method > negative verdict subtype > subterm descent.
- `turn2_explicit_retraction_marker`: `yes` when Turn 2 uses explicit retraction language (`corrected`, `revised`, `retract`, `previous answer was wrong`); otherwise `no`.
- `turn2_q4_hedged`: `yes` when Q4 is answered positively but hedged (`intuitively`, `informally`, `likely`, `but only`, `not within the boundary`); otherwise `no`.
- `turn2_meta_boundary_argument`: `yes` when the response argues the stated boundary is unachievable, vacuous, or that every termination proof must import meta-theory; otherwise `no`.
- `turn2_original_question_restated_verdict`: Restated answer to the original bounded question — `yes`, `no`, `unclear`, or `none`. Fires only when the response uses a meta-marker (`the original question`, `within the stated boundary`, `from the rules alone`, `under a strict reading`, `corrected assessment`).
- `turn2_peripheral_quote`: Verbatim quote (≤300 chars) supporting the highest-priority Turn 2 signal. Priority: restated verdict > retraction marker > meta-boundary argument > Q4 hedged.

## Normalization

`turn1_norm_primary_method_standardized_method_name`, `turn1_norm_primary_method_method_class`, `turn2_norm_primary_method_standardized_method_name`, and `turn2_norm_primary_method_method_class` are derived from the corresponding turn-specific method label by mapping surface variants to a canonical name and a broad family. The three `turn1_*_correct*` / validity columns are answer-key-derived scoring columns added after extraction. `turn1_method_review_note` is the only row-level manual review column in the public Schema A file, and is currently used for theorem-backed polynomial corrections plus note-only annotations on a small reviewed gray-zone subset. All other fields are raw controlled-vocabulary extractions.

---

## Schema Test B

# Schema Test B — Master Data Schema

This schema documents the **current live public file**:

- `6.extracted-data/csv/schema-test-B-tests.csv`

The file currently has **108 rows** and **21 columns**. It is a public copy of
the reduced adjudicated Schema B answers. It mirrors the shared answer-bearing
and normalized columns from:

- `6.extracted-data/csv/schema-test-B-tests.csv`

and adds:

- `model`
- `provider`

downstream in the public copy.

Important: the live public file stores the **adjudicated extracted model
answers**, not a gold-overwritten answer-key table.

## Test role

Schema B asks 27 LLMs to assess five pre-specified proof methods (A-E) for the
duplicating primitive-recursion schema and to judge each method on two axes:

1. does the method prove termination as stated?
2. does the method stay within the benchmark boundary?

The dataset is single-response, single-round, with 54 `regular` rows and 54
`control` rows.

## Live columns

### Metadata

- `session_slug`: session identifier, `<model>__<timestamp>`, with `-control`
  suffixes on the clarified-control variant.
- `model`: canonical model display name added in the public copy.
- `provider`: canonical provider name added in the public copy.
- `prompt_variant`: prompt condition, `regular` or `control`.

### Answer-bearing method fields

- `method_A_terminates`: extracted verdict for method A. Live vocabulary:
  `yes`, `no`, `unclear`.
- `method_A_in_boundary`: extracted boundary verdict for method A. Live
  vocabulary: `yes`, `no`, `unclear`.
- `method_B_terminates`: extracted verdict for method B. Live vocabulary:
  `yes`, `no`, `unclear`.
- `method_B_in_boundary`: extracted boundary verdict for method B. Live
  vocabulary: `yes`, `no`, `moot`, `unclear`.
- `method_C_terminates`: extracted verdict for method C. Live vocabulary:
  `yes`, `no`, `unclear`.
- `method_C_in_boundary`: extracted boundary verdict for method C. Live
  vocabulary: `yes`, `no`, `moot`, `unclear`.
- `method_D_terminates`: extracted verdict for method D. Live vocabulary:
  `yes`, `no`.
- `method_D_in_boundary`: extracted boundary verdict for method D. Live
  vocabulary: `yes`, `no`.
- `method_E_terminates`: extracted verdict for method E. Live vocabulary:
  `yes`, `no`.
- `method_E_in_boundary`: extracted boundary verdict for method E. Live
  vocabulary: `yes`, `no`, `moot`, `unclear`.

### Normalized added columns

- `norm_method_D_terminates_rationale_family`: normalized family for the richer
  D-rationale text. Live vocabulary: `dp_subterm_criterion`, `dp_fails`.
- `norm_both_methods_count`: number of methods included in the model's final
  "satisfies both" answer, encoded as `0`-`5`.
- `norm_both_methods_has_A`: `1` when A is in the final both-methods answer,
  otherwise `0`.
- `norm_both_methods_has_B`: `1` when B is in the final both-methods answer,
  otherwise `0`.
- `norm_both_methods_has_C`: `1` when C is in the final both-methods answer,
  otherwise `0`.
- `norm_both_methods_has_D`: `1` when D is in the final both-methods answer,
  otherwise `0`.
- `norm_both_methods_has_E`: `1` when E is in the final both-methods answer,
  otherwise `0`.

## Gold grading reference

The benchmark gold answer is backed by:

- `3.lean/KO7Benchmark/BenchmarkContract.lean`
- `3.lean/KO7Benchmark/SchemaTests/AnswerKey.lean`
- `4.TTT2-Artifacts/ttt2/schema/`

Gold target values:

- A: `method_A_terminates = yes`, `method_A_in_boundary = no`
- B: `method_B_terminates = no`, `method_B_in_boundary = no`
- C: `method_C_terminates = no`, `method_C_in_boundary = no`
- D: `method_D_terminates = yes`, `method_D_in_boundary = yes`
- E: `method_E_terminates = no`, `method_E_in_boundary = no`
- Final both-methods answer: `D` alone, i.e. `norm_both_methods_count = 1`,
  `norm_both_methods_has_D = 1`, and all other `norm_both_methods_has_* = 0`

To grade Schema B, compare the live extracted fields in this file against the
gold target above. Do **not** assume the public file is already answer-key
corrected.

## Provenance note

After the 2026-04-20 repair pass:

- the public copy matches the reduced source normalized file on all shared
  columns
- the reduced source normalized file matches the richer
  `SCHEMA_B_data.normalized.csv` on all shared verdict and normalized
  fields

---

## Test 01 Kernel

# Test 01 Kernel — Master Data Schema

Test 01 asks 27 LLMs whether strong normalization can be proved for a first-order rewrite calculus with 8 step rules, using only the rules shown and no imported object-level axioms. Single-turn: one response per session. Two conditions run in parallel: **KO7** (canonical constructor names `void`, `delta`, `integrate`, `merge`, `app`, `recΔ`, `eqW`) and **Fruit** (isomorphic calculus with renamed constructors `plum`, `grape`, `mango`, `peach`, `pear`, `banana`, `cherry`, plus one added side condition `a ≠ b` on `R_cherry_diff`). A trailing `-fruit` on the session slug means Fruit, otherwise KO7. The file covers 324 sessions (162 KO7 + 162 Fruit).

## Columns

- `session_slug`: Session identifier, `<model>__<timestamp>` (KO7) or `<model>__<timestamp>-fruit` (Fruit).
- `model`:
- `provider`:
- `prompt_variant`: Condition label derived from `session_slug` — `regular` for KO7 rows and `control` for Fruit rows.
- `sn_verdict`: Committed verdict on whether SN holds within the stated boundary — `yes`, `no`, `unclear`.
- `termination_correctness`: Derived answer-key verdict for `sn_verdict`. Mechanical rule: `Correct` when `sn_verdict` is `yes`, otherwise `Incorrect`.
- `sn_verdict_quote`: Verbatim quote (≤300 chars) stating the verdict.
- `primary_approach_answer_span`: Verbatim span where the model commits to its primary approach, or the refusal / local-shortcut sentence(s) when the answer is objection-based or informal.
- `primary_method`: Free-text method label (e.g. `Lexicographic Path Ordering (LPO)`, `polynomial interpretation`, `dependency pair method`). Blank when objection-based or no recoverable method name.
- `norm_primary_method_standardized_method_name`: Canonical method name collapsing surface variants to one label (e.g. `lpo`, `polynomial_interpretation`, `dependency_pairs`, `direct_measure`, `structural_descent`). Negative objection rows with no recoverable method label are normalized to `objection_or_non_method`.
- `norm_primary_method_method_class`: Broad method family (`path_order`, `polynomial`, `direct_measure`, `structural_descent`, `transformed_calls`, `multiset_measure`, `lexicographic_measure`). Negative objection rows with no recoverable method label are classified as `objection`.
- `method_mathematical_validity`: Derived answer-key verdict for the primary method family. Mechanical rule: `Correct` for `path_order` or `transformed_calls`; otherwise `Incorrect`. Generic `polynomial` is `truthOnly` on the KO7 / Fruit kernel and is stored as mathematically invalid in the public CSV.
- `method_correct_and_admissible`: Derived answer-key verdict for the primary method family under the Test 01 / Schema A boundary rule. Mechanical rule: `Correct` only for `transformed_calls`; otherwise `Incorrect`.
- `more_than_one_approach_proposed`: `yes` when the model proposes two or more co-equal proof routes or objections, otherwise `no`.
- `primary_answer_mode`: Shape of the answer — `method` (supports the answer with a recoverable proof device), `objection` (main basis is that SN cannot be established within the boundary), `shortcut_or_local` (purely informal local argument), or `unclear`.
- `answer_mode_primary_method`: Method label recovered specifically for the answer-mode / boundary-claim layer. This may differ from the initial `primary_method` extraction if the model reframes its basis in the later adjudication round.
- `claims_method_in_boundary`: Model's own claim about whether its method stays within the boundary — `yes`, `no`, `unclear`, or `na` (set to `na` when `primary_answer_mode != method`).
- `transformed_call_signal`: W2 retrieval indicator — `explicit_w2_method` (explicitly names a W2-family method), `subterm_containment_only` (appeals to subterm containment without naming the framework), or `none`.
- `boundary_or_w2_quote`: Verbatim quote (≤300 chars) supporting the highest-priority signal. Priority: explicit W2 method > subterm containment > boundary claim.
- `flag_w2_method_named`: `yes` when a W2-family method is explicitly named (dependency pairs, subterm criterion, argument filtering, size-change, counter-projection, transformed calls, DP method); otherwise `no`.
- `flag_mentions_root_only`: `yes` when the response explicitly treats the rewrite relation as root-only or claims no congruence; otherwise `no`.
- `flag_mentions_external_framework`: `yes` when the response cites an external termination tool or framework (`TTT2`, `AProVE`, `CeTA`, Kruskal's tree theorem, ordinal analysis, dependency-pair framework, Lean-level imported proof machinery); otherwise `no`.
- `flag_size_growing_rule_noted`: `yes` when the response explicitly notes that one of the rules grows the term or is non-size-decreasing; otherwise `no`.
- `peripheral_quote`: Verbatim quote (≤300 chars) supporting the highest-priority active flag. Priority: W2 named > root-only > external framework > size-growing rule.
- `negative_verdict_subtype`: Subtype when verdict is negative — `cannot_establish`, `claims_nontermination`, `none` (positive/unclear verdict), or `unclear`.
- `primary_objection_type`: Taxonomic label when the main basis is an objection — `congruence_missing`, `meta_framework_needed`, `inert_constructor_objection`, `size_growth_rule`, `decidability_of_equality`, `type_theoretic`, `other`, or `none`.
- `flag_boundary_self_acknowledgment`: `yes` when the model acknowledges unprompted that its own method imports external structure or crosses the boundary; otherwise `no`.
- `peripheral_quote_b`: Verbatim quote (≤300 chars) supporting the highest-priority active field. Priority: negative verdict subtype > primary objection type > boundary self-acknowledgment.

## Normalization

`prompt_variant` is derived from `session_slug` by detecting the `-fruit` suffix. `norm_primary_method_standardized_method_name` and `norm_primary_method_method_class` are both derived from the free-text `primary_method` field by mapping surface variants to a canonical name and a broad family. `termination_correctness`, `method_mathematical_validity`, and `method_correct_and_admissible` are answer-key-derived scoring columns added after extraction. All other fields are raw controlled-vocabulary extractions.

---

## Test 02 Completion Nat/Lex

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

---

## Test 03 Completion Ordinal

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

---

## Test 04 Measure Verification

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

## Normalization

No normalization-only columns are currently present in this CSV.

---

## Test 05 Candidate Class Reasoning

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

---

## Test 06 Branch Realism

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

## Normalization

No normalization-only columns are currently present in this CSV. The seven `*_correctness` / quality fields are answer-key-derived verdict columns added after extraction.
