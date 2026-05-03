# Schema Test B — Master Data Schema

This schema documents the **current live public file**:

- `6.extracted-data/csv/schema-test-B-tests.csv`

The file currently has **108 rows** and **21 columns**. It is a public copy of
the reduced adjudicated Schema B answers. It mirrors the shared answer-bearing
and normalized columns from:

- `6.extracted-data/csv/schema-test-B-tests.csv`

and adds:

- `model`
- `provider`

downstream in the public copy.

Important: the live public file stores the **adjudicated extracted model
answers**, not a gold-overwritten answer-key table.

## Test role

Schema B asks 27 LLMs to assess five pre-specified proof methods (A-E) for the
duplicating primitive-recursion schema and to judge each method on two axes:

1. does the method prove termination as stated?
2. does the method stay within the benchmark boundary?

The dataset is single-response, single-round, with 54 `regular` rows and 54
`control` rows.

## Live columns

### Metadata

- `session_slug`: session identifier, `<model>__<timestamp>`, with `-control`
  suffixes on the clarified-control variant.
- `model`: canonical model display name added in the public copy.
- `provider`: canonical provider name added in the public copy.
- `prompt_variant`: prompt condition, `regular` or `control`.

### Answer-bearing method fields

- `method_A_terminates`: extracted verdict for method A. Live vocabulary:
  `yes`, `no`, `unclear`.
- `method_A_in_boundary`: extracted boundary verdict for method A. Live
  vocabulary: `yes`, `no`, `unclear`.
- `method_B_terminates`: extracted verdict for method B. Live vocabulary:
  `yes`, `no`, `unclear`.
- `method_B_in_boundary`: extracted boundary verdict for method B. Live
  vocabulary: `yes`, `no`, `moot`, `unclear`.
- `method_C_terminates`: extracted verdict for method C. Live vocabulary:
  `yes`, `no`, `unclear`.
- `method_C_in_boundary`: extracted boundary verdict for method C. Live
  vocabulary: `yes`, `no`, `moot`, `unclear`.
- `method_D_terminates`: extracted verdict for method D. Live vocabulary:
  `yes`, `no`.
- `method_D_in_boundary`: extracted boundary verdict for method D. Live
  vocabulary: `yes`, `no`.
- `method_E_terminates`: extracted verdict for method E. Live vocabulary:
  `yes`, `no`.
- `method_E_in_boundary`: extracted boundary verdict for method E. Live
  vocabulary: `yes`, `no`, `moot`, `unclear`.

### Normalized added columns

- `norm_method_D_terminates_rationale_family`: normalized family for the richer
  D-rationale text. Live vocabulary: `dp_subterm_criterion`, `dp_fails`.
- `norm_both_methods_count`: number of methods included in the model's final
  "satisfies both" answer, encoded as `0`-`5`.
- `norm_both_methods_has_A`: `1` when A is in the final both-methods answer,
  otherwise `0`.
- `norm_both_methods_has_B`: `1` when B is in the final both-methods answer,
  otherwise `0`.
- `norm_both_methods_has_C`: `1` when C is in the final both-methods answer,
  otherwise `0`.
- `norm_both_methods_has_D`: `1` when D is in the final both-methods answer,
  otherwise `0`.
- `norm_both_methods_has_E`: `1` when E is in the final both-methods answer,
  otherwise `0`.

## Gold grading reference

The benchmark gold answer is backed by:

- `3.lean/KO7Benchmark/BenchmarkContract.lean`
- `3.lean/KO7Benchmark/SchemaTests/AnswerKey.lean`
- `4.TTT2-Artifacts/ttt2/schema/`

Gold target values:

- A: `method_A_terminates = yes`, `method_A_in_boundary = no`
- B: `method_B_terminates = no`, `method_B_in_boundary = no`
- C: `method_C_terminates = no`, `method_C_in_boundary = no`
- D: `method_D_terminates = yes`, `method_D_in_boundary = yes`
- E: `method_E_terminates = no`, `method_E_in_boundary = no`
- Final both-methods answer: `D` alone, i.e. `norm_both_methods_count = 1`,
  `norm_both_methods_has_D = 1`, and all other `norm_both_methods_has_* = 0`

To grade Schema B, compare the live extracted fields in this file against the
gold target above. Do **not** assume the public file is already answer-key
corrected.

## Provenance note

After the 2026-04-20 repair pass:

- the public copy matches the reduced source normalized file on all shared
  columns
- the reduced source normalized file matches the richer
  `SCHEMA_B_data.normalized.csv` on all shared verdict and normalized
  fields
