# Test 03 Raw Extraction Template

Use this template to extract direct delivery-form fields from released Test 03 sessions.

```
test-03-completion-tests-ordinal/<session_slug>/response.txt -> proof-obligation delivery fields
```

## Output Header

```csv
session_slug,model,provider,r_rec_succ_delivery,r_eq_refl_delivery,r_eq_diff_delivery
```

## Field Rules

| Column | Values | Extraction rule |
|---|---|---|
| `session_slug` | folder name | Copy the session folder name exactly. |
| `model` | text | Copy the released model label. |
| `provider` | text | Copy the released provider label. |
| `r_rec_succ_delivery` | `closed_code`, `open_code`, `prose_only`, `missing` | Extract the delivery form for the `R_rec_succ` obligation. |
| `r_eq_refl_delivery` | `closed_code`, `open_code`, `prose_only`, `missing` | Extract the delivery form for the `R_eq_refl` obligation. |
| `r_eq_diff_delivery` | `closed_code`, `open_code`, `prose_only`, `missing` | Extract the delivery form for the `R_eq_diff` obligation. |

Use `closed_code` when the response provides a syntactically closed proof term or tactic block for the named obligation.

Use `open_code` when the response gives code with holes, admits, unresolved placeholders, or missing dependencies.

Use `prose_only` when the response explains the proof without giving usable code for the named obligation.

Use `missing` when the named obligation is not addressed.
