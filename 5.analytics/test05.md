# Test 05 Numbers (PRT manuscript: tab:t05 and body 6.2 propose-vs-verify)

- Generated: 2026-05-03
- Reproduces: appendix `tab:t05` and the propose-vs-verify cross-test numbers.
- Denominator: n=108 for Test 05; 27-model panel for cross-test rows.

## Source fields

- `mu1_yes_no`, `mu2_yes_no`, `mu3_yes_no`: per-candidate verdicts in {yes, no, unclear}; gold = no for all three.
- `r_rec_succ_localization_correctness` == Correct iff the response names `R_rec_succ` as the decisive rule.
- `overall_test05_correctness` == Correct iff the response rejects all three candidates and localizes to `R_rec_succ`.
- Direct/lex proposer membership: at least one Schema A or Test 01 session with `sn_verdict == 'yes'` and `method_class == 'direct_measure'`. The paper restricts proposer membership to the canonical direct/lexicographic family rather than the broader structural-descent / structural-induction cluster.

## `tab:t05` rows

| Field and value | Count | Rate |
| --- | --- | --- |
| All three mu_i rejected simultaneously | 99 | 91.7% |
| r_rec_succ_localization_correctness = Correct | 105 | 97.2% |
| overall_test05_correctness = Correct | 98 | 90.7% |

## Body 6.2: propose-vs-verify cross-test contradiction

Per-model split. Step 1: identify models that ever propose a direct or lexicographic whole-term measure under a positive verdict in Schema A or Test 01 (the proposer set). Step 2: among those models, count those whose Test 05 sessions reject all three candidates in every Test 05 session, and those who do so in at least one.

| Signal | Comparison | Rate |
| --- | --- | --- |
| Direct/lex proposer models (Schema A or Test 01) | 22/27 | 81.5% |
|   Reject all three in every Test 05 session | 18/22 | 81.8% |
|   Reject all three in at least one Test 05 session | 21/22 | 95.5% |
