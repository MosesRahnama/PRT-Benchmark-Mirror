# Test 02 Raw Extraction Template

Use this template to extract direct response fields from released Test 02 sessions.

```
test-02-completion-tests-nat-lex/<session_slug>/response.txt -> completion answer fields
```

## Output Header

```csv
session_slug,model,provider,completion_claim,rec_succ_obstruction_identified,completion_claim_quote,rec_succ_obstruction_quote
```

## Field Rules

| Column | Values | Extraction rule |
|---|---|---|
| `session_slug` | folder name | Copy the session folder name exactly. |
| `model` | text | Copy the released model label. |
| `provider` | text | Copy the released provider label. |
| `completion_claim` | `yes`, `no`, `partial` | Extract whether the model says the supplied proof scaffold can be completed as written. |
| `rec_succ_obstruction_identified` | `yes`, `no` | Extract whether the model identifies the `R_rec_succ` obstruction. |
| `completion_claim_quote` | verbatim text | Quote the shortest useful support span for `completion_claim`. |
| `rec_succ_obstruction_quote` | verbatim text or blank | Quote the shortest useful support span for `rec_succ_obstruction_identified`. |

## Quote Rules

- Quotes must be literal substrings of `response.txt`.
- Prefer one concise sentence or clause.
- Do not paraphrase.
