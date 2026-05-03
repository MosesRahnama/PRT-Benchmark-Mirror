# Schema B Normalization Guide

This guide documents the **live Schema B normalized outputs now on disk**.

Files reviewed:

- `schema-test-B-tests/3.extraction/SCHEMA_B_data.normalized.csv`
- `schema-test-B-tests/3.extraction/final_SCHEMA_B_data.csv`
- `6.extracted-data/csv/schema-test-B-tests.csv`
- `schema-test-B-tests/3.extraction/SCHEMA_B_SOURCE_NORMALIZATION_NOTES.md`
- `6.extracted-data/csv/schema-test-B-tests.csv`
- `internal field-enrichment step already applied before public export`

## Live file shapes

### Reduced source normalized file

`6.extracted-data/csv/schema-test-B-tests.csv`

- rows: `108`
- columns: `19`
- role: reduced adjudicated source package

Header:

- `session_slug`
- `prompt_variant`
- `method_A_terminates`
- `method_A_in_boundary`
- `method_B_terminates`
- `method_B_in_boundary`
- `method_C_terminates`
- `method_C_in_boundary`
- `method_D_terminates`
- `method_D_in_boundary`
- `method_E_terminates`
- `method_E_in_boundary`
- `norm_method_D_terminates_rationale_family`
- `norm_both_methods_count`
- `norm_both_methods_has_A`
- `norm_both_methods_has_B`
- `norm_both_methods_has_C`
- `norm_both_methods_has_D`
- `norm_both_methods_has_E`

### Live public copy

`6.extracted-data/csv/schema-test-B-tests.csv`

- rows: `108`
- columns: `21`
- role: public raw-data copy used downstream

It contains the same 19 shared columns as the reduced source file, plus:

- `model`
- `provider`

Those two columns are added downstream by
`add_schema_b_model_provider_columns.py`.

## What is actually normalized

### 1. Method D rationale family

Added column:

- `norm_method_D_terminates_rationale_family`

Source:

- richer data field `final_method_D_terminates_rationale` in
  `SCHEMA_B_data.normalized.csv`

Live vocabulary:

- `dp_subterm_criterion`
- `dp_fails`

Meaning:

- collapses the richer D-rationale text into a 2-value family for downstream
  grouping

### 2. Final both-methods expansion

Added columns:

- `norm_both_methods_count`
- `norm_both_methods_has_A`
- `norm_both_methods_has_B`
- `norm_both_methods_has_C`
- `norm_both_methods_has_D`
- `norm_both_methods_has_E`

Source:

- richer data field `final_both_methods` in
  `SCHEMA_B_data.normalized.csv`

Meaning:

- converts the comma-separated final method-set answer into one count column and
  five binary membership flags

### 3. Public-copy model/provider enrichment

Added columns in the public copy only:

- `model`
- `provider`

Source:

- `session_slug` prefix mapped through the canonical roster in
  `add_schema_b_model_provider_columns.py`

Meaning:

- makes the public copy directly usable for provider/model analysis without
  another join step

## Scope guardrail: Schema A method-review overrides

`6.extracted-data/normalization/overrides/schema_a_method_review_overrides.csv` is exported
into the public normalization folder
(`PRT-Benchmark/6.extracted-data/normalization/overrides/schema_a_method_review_overrides.csv`)
by `3.public-repo/build_6_extracted_data.py` so that public reviewers can
reproduce the manual override decisions reflected in the released CSVs. The
ledger physically lives in `6.extracted-data/` alongside the live CSVs
it patches, and is registered as a `cr:FileObject` in the released
`croissant.json`. It belongs to Schema A, not Schema B.

```
[schema_a_method_review_overrides.csv] -> [6.extracted-data/csv/schema-test-A-tests.csv]
[Schema B normalized source fields]    -> [6.extracted-data/csv/schema-test-B-tests.csv]
```

The Schema A override ledger carries 16 reviewed rows (11 downgrades to
`Incorrect` plus 5 kept-correct confirmations). It records manual review of
polynomial-class and related gray-zone Schema A rows and is reflected in
`turn1_method_mathematical_validity` plus `turn1_method_review_note` in the
Schema A public CSV.

The live Schema B public CSV does not consume that override ledger. Schema B's
polynomial-related answers are the extracted/adjudicated model answers for
fixed Method B in the five-method grid, while gold grading remains a separate
answer-key comparison step.

## What the live public file does **not** contain

The live public Schema B file does **not** currently contain:

- gold-overwritten A-E answer columns
- derived answer-key error-summary columns

Those belonged to an older public-file variant and should not be inferred from
the current filename.

## Fidelity checks

After the 2026-04-20 repair pass:

- the public file matches the reduced source normalized file on all shared
  columns
- the reduced source normalized file matches the richer
  `SCHEMA_B_data.normalized.csv` on all shared verdict and normalized
  fields

Two rows had been incorrectly hardened from `unclear` to `no` in the reduced
file and were repaired so the reduced/public copies now agree with the richer
data.

## Design note

Schema B normalization is intentionally narrow. The live normalized files keep
the extracted A-E verdicts as adjudicated model answers and only normalize:

1. the D-rationale family
2. the final both-method set
3. the public-copy model/provider labels

Gold grading against the Lean / TTT2 answer key is a separate comparison step,
not something baked into the current live public CSV.
