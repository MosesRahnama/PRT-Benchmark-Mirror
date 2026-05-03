# Per-Model Instability and Cross-Test Incoherence (PRT manuscript: tab:instability)

- Generated: 2026-05-03
- Reproduces: appendix `tab:instability` and the cross-test incoherence numbers in section 7.
- Denominator: 27-model panel.

## Source fields and definitions

- **Verdict flip**: per model, the set of distinct nonblank `sn_verdict` values across the model's 12 Test 01 sessions has more than one element.
- **>=k recoverable method classes**: per model, count of distinct `norm_primary_method_method_class` values from the canonical six rewriting families {direct_measure, path_order, polynomial, structural_induction, structural_descent, transformed_calls} >= k. The non-method label `objection` is excluded; that is what the paper means by 'recoverable proof-method class'.
- **KO7-vs-Fruit axis tuple change**: 4-tuple of session counts (sn_verdict yes, math Correct, admissible Correct, `flag_w2_method_named` yes) differs between the model's 6 KO7 sessions and 6 Fruit sessions.
- **Cross-test incoherent**: exists Test 01 session with `sn_verdict == 'yes'` AND `method_correct_and_admissible != 'Correct'` (yes through a boundary-external or mathematically false method), AND exists Test 04 session with `measure_sound_yes_no == 'yes'` OR Test 06 session with `strategy_sound_verdict == 'sound'` (raw endorsement of a mechanically broken artifact).
- **D-alone Schema B model**: at least one Schema B session whose final selection set is exactly `{D}` (norm_both_methods_count == 1, has_D == 1, has_A/B/C/E == 0).

## Instability rows

| Statistic | Count | Rate |
| --- | --- | --- |
| Models whose Test 01 sn_verdict flips across 12 sessions | 12 | 44.4% |
| Models using at least 2 distinct recoverable method classes | 18 | 66.7% |
| Models using at least 3 distinct recoverable method classes | 14 | 51.9% |
| Models whose KO7-vs-Fruit axis-count tuple changes | 18 | 66.7% |
| Cross-test incoherent (T01 yes via bad method AND T04 or T06 endorses unsound) | 18 | 66.7% |
| Models ever isolating {D} alone in Schema B | 3 | 11.1% |
| Of the 3 D-alone models, retrieve transformed_calls in Schema A | 0 | 0.0% |
