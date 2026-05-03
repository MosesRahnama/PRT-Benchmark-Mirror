# Headline Results (PRT Table 2)

- Generated: 2026-05-03
- Reproduces: `tab:headline-results` in the NeurIPS manuscript.

## What this table shows

The truth-to-admissibility cascade on the three open-ended surfaces, the closed-menu Schema B summary, and three diagnostic contrasts. Each cascade column counts sessions whose stored verdict column matches gold; rates use fixed denominators (n=324 for Test 01, n=108 for each Schema task). Recognition-vs-retrieval and hidden-vs-explicit contrasts are reported as percentage-point gaps.

## Source fields

- **Truth**: `sn_verdict` (Test 01) / `turn1_sn_verdict` (Schema A, SANS) == `yes`.
- **Adequate**: `method_mathematical_validity` / `turn1_method_mathematical_validity` == `Correct`.
- **Admissible**: `method_correct_and_admissible` / `turn1_method_correct_and_admissible` == `Correct`.
- **Schema B Method X yes/yes**: `method_X_terminates` == `yes` AND `method_X_in_boundary` == `yes`.
- **Full five-method correct**: all 10 per-method axes match gold AND the 6 selection-set fields match `{D}` alone.
- **SANS outside-boundary self-audit**: `turn2_q3_outside_boundary` == `yes`, restricted to the 55 admissible SANS rows.

## Open-ended cascade

| Surface | Truth | Adequate | Admissible | Truth -> adm. gap |
| --- | --- | --- | --- | --- |
| Test 01 (KO7 + Fruit, n=324) | 222 (68.5%) | 48 (14.8%) | 3 (0.9%) | -67.6 pts |
| Schema A (duplicating, n=108) | 88 (81.5%) | 34 (31.5%) | 2 (1.9%) | -79.6 pts |
| Schema A New System (control, n=108) | 74 (68.5%) | 73 (67.6%) | 55 (50.9%) | -17.6 pts |

## Closed-menu task (Schema B)

| Signal | Count | Rate |
| --- | --- | --- |
| Method D accepted yes/yes (terminates, in-boundary; gold) | 104 | 96.3% |
| Method A (path order) accepted yes/yes (gold yes/no) | 87 | 80.6% |
| Method B (polynomial) accepted yes/yes (gold no/no) | 62 | 57.4% |
| Full five-method answer table correct | 0 | 0.0% |

## Diagnostic gaps and contrasts

| Signal | Comparison | Rate / gap |
| --- | --- | --- |
| Recognition vs open-ended retrieval (Schema B Method D / Schema A admissible) | 104 vs 2 | +94.4 pts |
| Hidden vs explicit obstruction (Test 02 strict / Test 05 strict) | 14 vs 98 | +77.8 pts |
| Schema A New System admissible rows still self-audit outside-boundary | 51 of 55 | 92.7% |
