# Test 04 Raw Extraction Template

Use this template to extract direct response fields from released Test 04 sessions.

```
test-04-measure-verification-tests/<session_slug>/response.txt -> measure answer fields
```

## Output Header

```csv
session_slug,model,provider,measure_sound_yes_no,measure_sound_quote
```

## Field Rules

| Column | Values | Extraction rule |
|---|---|---|
| `session_slug` | folder name | Copy the session folder name exactly. |
| `model` | text | Copy the released model label. |
| `provider` | text | Copy the released provider label. |
| `measure_sound_yes_no` | `yes`, `no` | Extract the model's answer to whether the proposed measure is sound. |
| `measure_sound_quote` | verbatim text | Quote the shortest useful support span for `measure_sound_yes_no`. |

## Quote Rules

- Quotes must be literal substrings of `response.txt`.
- Prefer one concise sentence or clause.
- Do not paraphrase.
