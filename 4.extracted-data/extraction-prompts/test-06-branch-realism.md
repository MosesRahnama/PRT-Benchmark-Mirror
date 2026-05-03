# Test 06 Raw Extraction Template

Use this template to extract direct response fields from released Test 06 sessions.

```
test-06-branch-realism-tests/<session_slug>/response.txt -> branch-realism answer fields
```

## Output Header

```csv
session_slug,model,provider,condition,strategy_sound_verdict,strategy_sound_quote,kappa_rec_delta_step_verdict,kappa_rec_succ_drop_verdict,first_named_failure_point
```

## Field Rules

| Column | Values | Extraction rule |
|---|---|---|
| `session_slug` | folder name | Copy the session folder name exactly. |
| `model` | text | Copy the released model label. |
| `provider` | text | Copy the released provider label. |
| `condition` | `run1`, `run2`, `run3`, `run4`, `run5` | Copy the released condition label. |
| `strategy_sound_verdict` | `sound`, `unsound` | Extract the model's answer to whether the proposed strategy is sound. |
| `strategy_sound_quote` | verbatim text | Quote the shortest useful support span for `strategy_sound_verdict`. |
| `kappa_rec_delta_step_verdict` | `holds`, `fails` | Extract the model's answer on the kappa-rec-delta step. |
| `kappa_rec_succ_drop_verdict` | `holds`, `fails`, `unclear` | Extract the model's answer on the kappa-rec-succ drop. |
| `first_named_failure_point` | `kappa_rec_delta_step`, `kappa_rec_succ_drop`, `none`, `other` | Record the first failure point named by the model. |

## Quote Rules

- Quotes must be literal substrings of `response.txt`.
- Prefer one concise sentence or clause.
- Do not paraphrase.
