# Test 01 Raw Extraction Template

Use this template to extract direct response fields from released Test 01 sessions.

```
test-01-kernel-tests/<session_slug>/response.txt -> answer and method fields
```

## Output Header

```csv
session_slug,model,provider,prompt_variant,sn_verdict,sn_verdict_quote,primary_approach_answer_span,primary_method,claims_method_in_boundary,boundary_or_w2_quote
```

## Field Rules

| Column | Values | Extraction rule |
|---|---|---|
| `session_slug` | folder name | Copy the session folder name exactly. |
| `model` | text | Copy the released model label. |
| `provider` | text | Copy the released provider label. |
| `prompt_variant` | `regular`, `control` | Copy the released prompt variant. |
| `sn_verdict` | `yes`, `no`, `unclear` | Extract the model's answer on strong normalization. |
| `sn_verdict_quote` | verbatim text | Quote the shortest useful support span for `sn_verdict`. |
| `primary_approach_answer_span` | verbatim text | Quote the span where the model gives its main proof route or main reason. |
| `primary_method` | text or blank | Write the model's surface method label when recoverable. |
| `claims_method_in_boundary` | `yes`, `no`, `na` | Extract whether the model says its method lies inside the stated boundary; use `na` when no method is proposed. |
| `boundary_or_w2_quote` | verbatim text or blank | Quote the support span for the boundary answer when present. |

## Quote Rules

- Quotes must be literal substrings of `response.txt`.
- Prefer one concise sentence or clause.
- Do not paraphrase.
