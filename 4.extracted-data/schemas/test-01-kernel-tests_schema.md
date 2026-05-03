# Test 01 Kernel — Master Data Schema

Test 01 asks 27 LLMs whether strong normalization can be proved for a first-order rewrite calculus with 8 step rules, using only the rules shown and no imported object-level axioms. Single-turn: one response per session. Two conditions run in parallel: **KO7** (canonical constructor names `void`, `delta`, `integrate`, `merge`, `app`, `recΔ`, `eqW`) and **Fruit** (isomorphic calculus with renamed constructors `plum`, `grape`, `mango`, `peach`, `pear`, `banana`, `cherry`, plus one added side condition `a ≠ b` on `R_cherry_diff`). A trailing `-fruit` on the session slug means Fruit, otherwise KO7. The file covers 324 sessions (162 KO7 + 162 Fruit).

## Columns

- `session_slug`: Session identifier, `<model>__<timestamp>` (KO7) or `<model>__<timestamp>-fruit` (Fruit).
- `model`: Display model name.
- `provider`: Model provider.
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
