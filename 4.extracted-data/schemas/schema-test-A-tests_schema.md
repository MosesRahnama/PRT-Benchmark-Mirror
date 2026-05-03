# Schema Test A — Master Data Schema

Schema A asks 27 LLMs whether strong normalization can be proved for a two-rule primitive-recursor kernel using only the rules shown and no imported axioms. The kernel is the *duplicating* variant `F(x, y, S(n)) -> G(y, F(x, y, n))`. The model answers in two turns: Turn 1 is the raw assessment; Turn 2 is a four-question boundary followup. The file covers 108 sessions.

## Identifier

- `session_slug`: Session identifier, `<model>__<timestamp>`.
- `model`: Canonical model display name added in the public copy.
- `provider`: Canonical provider name added in the public copy.

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
- `quote_spawn_versus_answer_mismatch`: Public QC helper column at the end of the CSV. Live vocabulary is `yes` / `no`. `yes` marks rows where the stored quote/span layer does not align with the coded answer field it is meant to support.

## Normalization

`turn1_norm_primary_method_standardized_method_name`, `turn1_norm_primary_method_method_class`, `turn2_norm_primary_method_standardized_method_name`, and `turn2_norm_primary_method_method_class` are derived from the corresponding turn-specific method label by mapping surface variants to a canonical name and a broad family. The three `turn1_*_correct*` / validity columns are answer-key-derived scoring columns added after extraction. `turn1_method_review_note` is the only row-level manual review column in the public Schema A file, and is currently used for theorem-backed polynomial corrections plus note-only annotations on a small reviewed gray-zone subset. All other fields are raw controlled-vocabulary extractions.
