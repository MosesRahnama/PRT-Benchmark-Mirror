# Schema A Numbers (PRT manuscript: tab:schema-a-detail and body 6.1)

- Generated: 2026-05-03
- Reproduces: appendix `tab:schema-a-detail` plus all Schema A body-prose numbers in section 6.1.
- Denominator: n=108 (27 models, 4 paired sessions per model).

## Source fields

- `turn1_sn_verdict` in {yes, no}: first-turn termination verdict; gold=yes.
- `turn1_method_mathematical_validity` == Correct iff method class is `path_order` or `transformed_calls`.
- `turn1_method_correct_and_admissible` == Correct iff method class is `transformed_calls`.
- `turn2_q3_outside_boundary` == yes: model's own self-audit on whether its Turn-1 route is outside the rule-extracted boundary.
- `turn2_q4_still_sn` == yes: post-audit SN verdict after the boundary follow-up.
- `turn1_norm_primary_method_method_class`: canonical method-class label.

## Verdict and method-validity rows

| Field and value | Count | Rate |
| --- | --- | --- |
| Turn-1 sn_verdict = 'yes' | 88 | 81.5% |
| Turn-1 sn_verdict = 'no' | 20 | 18.5% |
| Turn-1 method_mathematical_validity = Correct | 34 | 31.5% |
| Turn-1 method_correct_and_admissible = Correct | 2 | 1.9% |
| Turn-2 q3_outside_boundary = yes (self-reports off-boundary) | 104 | 96.3% |
| Turn-2 q4_still_sn = yes (post-audit SN verdict) | 100 | 92.6% |
| Turn-2 q4_still_sn = no or unclear (post-audit SN verdict) | 8 | 7.4% |

## Selected Turn-1 proof-method classes

Five classes referenced in the body or relevant to the gold split. On Schema A only `path_order` (adequate by class, boundary-external) and `transformed_calls` (correct and admissible) clear math validity; `direct_measure`, `structural_descent`, and `polynomial` are mathematically false on this duplicating kernel.

| Method class | Count | Rate |
| --- | --- | --- |
| path_order (adequate by class, boundary-external) | 32 | 29.6% |
| direct_measure (mathematically false on this kernel) | 24 | 22.2% |
| structural_descent (mathematically false on this kernel) | 19 | 17.6% |
| polynomial (mathematically false on this kernel) | 11 | 10.2% |
| transformed_calls (correct and admissible) | 2 | 1.9% |
