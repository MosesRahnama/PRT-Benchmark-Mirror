# Test 01 Numbers (PRT manuscript: tab:t01-consolidated, tab:t01-overall, body 6.1.1)

- Generated: 2026-05-03
- Reproduces: body Table 3 (`tab:t01-consolidated`), Appendix Table (`tab:t01-overall`), and the body-prose numbers in section 6.1.1.
- Denominators: total n=324 (KO7 regular = 162, Fruit control = 162).

## Body Table 3: consolidated distribution

Headline rows reported in the body. The 'yes with mathematically false method' composite is the conjunction `sn_verdict == 'yes'` AND `method_mathematical_validity == 'Incorrect'`. The transformed-call admissible row splits by condition because the manuscript reports a directional gap (3 retrievals on KO7, 0 on Fruit).

| Signal | Count | Rate |
| --- | --- | --- |
| SN verdict 'yes' (truth correct) | 222 | 68.5% |
| 'Yes' verdict with a mathematically false method | 175 | 54.0% |
| Primary method: dependency pairs / subterm criterion (W2) | 3 | 0.9% |
|   of which KO7 condition | 3 | 1.9% |
|   of which Fruit condition | 0 | 0.0% |

## Appendix `tab:t01-overall`: full distribution

The complete verdict and method-class breakdown, n=324. `method_class` of `path_order` and `transformed_calls` count as mathematically adequate; only `transformed_calls` is also boundary-admissible. Polynomial is excluded from the adequate set on this kernel by the Lean theorem `test1_polynomial_not_adequate` and the archived TTT2 certificate `KO7_POLY.cpf`.

| Field and value | Count | Rate |
| --- | --- | --- |
| sn_verdict = yes | 222 | 68.5% |
| sn_verdict = no | 94 | 29.0% |
| sn_verdict = unclear | 8 | 2.5% |
| method_mathematical_validity = Correct | 48 | 14.8% |
| method_correct_and_admissible = Correct | 3 | 0.9% |
| direct_measure (W0, mathematically false on this kernel) | 98 | 30.2% |
| path_order (W1, adequate by class, boundary-external) | 45 | 13.9% |
| polynomial (W1, mathematically false, boundary-external) | 42 | 13.0% |
| structural_induction (W0, mathematically false) | 29 | 9.0% |
| structural_descent (W0, mathematically false) | 14 | 4.3% |
| transformed_calls (W2, correct and admissible) | 3 | 0.9% |

## Body 6.1.1: boundary self-report layer

The body claim 'only 3/231 are actually admissible' restricts to sessions whose Turn-1 `claims_method_in_boundary` equals 'yes', then counts how many of those carry `method_correct_and_admissible == 'Correct'`.

| Signal | Count | Rate |
| --- | --- | --- |
| Sessions self-certifying as in-boundary | 231 | 71.3% |
|   of which actually admissible | 3 | 1.3% |
