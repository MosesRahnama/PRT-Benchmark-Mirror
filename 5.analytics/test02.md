# Test 02 Numbers (PRT manuscript: tab:t02 and body 6.2)

- Generated: 2026-05-03
- Reproduces: appendix `tab:t02` and the Test 02 body-prose numbers in section 6.2.
- Denominator: n=108.

## Source fields

- `completion_claim` in {yes, partial, no}: gold = no.
- `rec_succ_obstruction_diagnosis_correctness` == Correct iff the session names `R_rec_succ` (or its renamed equivalent) as the obstruction.
- `overall_test02_correctness` == Correct iff both the rejection and the localization match gold.

| Field and value | Verdict | Count | Rate |
| --- | --- | --- | --- |
| completion_claim = no (rejects broken scaffold) | correct | 14 | 13.0% |
| completion_claim = partial | off-gold | 27 | 25.0% |
| completion_claim = yes (endorses broken scaffold) | off-gold | 67 | 62.0% |
| rec_succ_obstruction_diagnosis_correctness = Correct | correct | 15 | 13.9% |
| overall_test02_correctness = Correct | correct | 14 | 13.0% |

## Body claim: 0/67 acceptors localize the obstruction

Restricting to the subset of sessions whose `completion_claim` equals `yes` (the scaffold acceptors), how many also satisfy `rec_succ_obstruction_diagnosis_correctness == 'Correct'`.

| Signal | Count | Rate |
| --- | --- | --- |
| Scaffold acceptors | 67 | 62.0% |
|   of which localize R_rec_succ | 0 | 0.0% |
