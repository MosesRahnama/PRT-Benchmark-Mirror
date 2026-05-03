# Method-class frequency and termination-verdict-flip stats per surface

- Generated: 2026-05-03
- Panel: 27 models
- Source CSVs: Schema A (n=108), SANS (n=108), Test 01 (n=324, 162 KO7 + 162 Fruit).

Each surface is independently aggregated. Method-name granularity is not tracked. Blank or missing values are excluded from every share. The `Test 01 combined` column is the union of `Test 01 KO7` and `Test 01 Fruit` (n=324).

## Primary method class frequency

Counts the canonical primary method class chosen on each session, side-by-side across the five surfaces. Rates are over the surface's total session count. Classes are ordered by their pooled count over Schema A + SANS + Test 01 combined, so the load-bearing rows appear first. Classes that never appear on a surface show as 0.

| Method class | Schema A (n=108) | SANS (n=108) | Test 01 KO7 (n=162) | Test 01 Fruit (n=162) | Test 01 combined (n=324) |
| --- | --- | --- | --- | --- | --- |
| direct_measure | 24 (22.2%) | 36 (33.3%) | 52 (32.1%) | 46 (28.4%) | 98 (30.2%) |
| objection | 20 (18.5%) | 31 (28.7%) | 48 (29.6%) | 45 (27.8%) | 93 (28.7%) |
| path_order | 32 (29.6%) | 4 (3.7%) | 22 (13.6%) | 23 (14.2%) | 45 (13.9%) |
| polynomial | 11 (10.2%) | 9 (8.3%) | 18 (11.1%) | 24 (14.8%) | 42 (13.0%) |
| structural_descent | 19 (17.6%) | 27 (25.0%) | 6 (3.7%) | 8 (4.9%) | 14 (4.3%) |
| structural_induction | 0 (0.0%) | 1 (0.9%) | 13 (8.0%) | 16 (9.9%) | 29 (9.0%) |
| transformed_calls | 2 (1.9%) | 0 (0.0%) | 3 (1.9%) | 0 (0.0%) | 3 (0.9%) |
| **any non-blank** | **108 (100.0%)** | **108 (100.0%)** | **162 (100.0%)** | **162 (100.0%)** | **324 (100.0%)** |
| (blank) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |

## Termination-verdict frequency

The session-level termination verdict on each surface (gold = yes on Schema A, SANS, and Test 01). Side-by-side counts and rates.

| Verdict | Schema A (n=108) | SANS (n=108) | Test 01 KO7 (n=162) | Test 01 Fruit (n=162) | Test 01 combined (n=324) |
| --- | --- | --- | --- | --- | --- |
| yes | 88 (81.5%) | 74 (68.5%) | 111 (68.5%) | 111 (68.5%) | 222 (68.5%) |
| no | 20 (18.5%) | 34 (31.5%) | 48 (29.6%) | 46 (28.4%) | 94 (29.0%) |
| unclear | 0 (0.0%) | 0 (0.0%) | 3 (1.9%) | 5 (3.1%) | 8 (2.5%) |
| (blank) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) | 0 (0.0%) |

## Within-surface verdict-flip and method-class-change incidence

Per surface, the number of models (out of 27) whose repeated sessions on the SAME kernel produce at least two distinct non-blank termination verdicts (verdict flip) or at least two distinct non-blank primary method classes (class change). Same definition as `within_test_method_consistency.py`. Denominator is the 27-model panel.

| Surface | Models flipping termination verdict | % | Models changing method class | % |
| --- | --- | --- | --- | --- |
| Schema A (n=108, 4/model) | 9 | 33.3% | 23 | 85.2% |
| SANS (n=108, 4/model) | 9 | 33.3% | 18 | 66.7% |
| Test 01 KO7 (n=162, 6/model) | 8 | 29.6% | 21 | 77.8% |
| Test 01 Fruit (n=162, 6/model) | 9 | 33.3% | 24 | 88.9% |
| Test 01 combined (n=324, 12/model) | 12 | 44.4% | 26 | 96.3% |
