# Recognition vs Retrieval Funnel (PRT manuscript: tab:funnel)

- Generated: 2026-05-03
- Reproduces: appendix `tab:funnel`. The Schema B rows are marginal counts (one axis at a time); the joint count of yes on both axes appears in `headline_results.md`.

## Source fields

- Schema B Method D: `method_D_terminates == 'yes'` (recognition of method-level termination) and `method_D_in_boundary == 'yes'` (recognition of boundary admissibility), counted independently as marginals.
- Schema A retrieval: `turn1_norm_primary_method_method_class == 'transformed_calls'` on n=108.
- Test 01 retrieval: `norm_primary_method_method_class == 'transformed_calls'` on n=162 each for the KO7 (`prompt_variant == 'regular'`) and Fruit (`prompt_variant == 'control'`) conditions.

| Signal | Count | Rate |
| --- | --- | --- |
| Schema B: Method D terminates = yes (matches gold) | 105 | 97.2% |
| Schema B: Method D in_boundary = yes (matches gold) | 107 | 99.1% |
| Schema A: turn-1 method class = transformed_calls | 2 | 1.9% |
| Test 01 KO7: method class = transformed_calls | 3 | 1.9% |
| Test 01 Fruit: method class = transformed_calls | 0 | 0.0% |
