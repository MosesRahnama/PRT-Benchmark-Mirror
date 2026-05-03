# Schema Test A New System Raw Extraction Template

Use this template to extract direct response fields from released Schema Test A New System sessions.

```
schema-test-A-new-system-tests/<session_slug>/response_1.txt -> turn 1 answer fields
schema-test-A-new-system-tests/<session_slug>/response_2.txt -> turn 2 answer fields
```

## Output Header

```csv
session_slug,model,provider,turn1_sn_verdict,turn1_sn_verdict_quote,turn1_primary_method_answer_span,turn1_primary_method,turn2_q1_method_answer_span,turn2_primary_method,turn2_q2_answer_span,turn2_q2_imports_external,turn2_q3_answer_span,turn2_q3_outside_boundary,turn2_q4_still_sn,turn2_q4_quote
```

## Session Fields

| Column | Values | Extraction rule |
|---|---|---|
| `session_slug` | folder name | Copy the session folder name exactly. |
| `model` | text | Copy the released model label. |
| `provider` | text | Copy the released provider label. |

## Turn 1 Fields

| Column | Values | Extraction rule |
|---|---|---|
| `turn1_sn_verdict` | `yes`, `no`, `unclear` | Extract the model's answer to whether strong normalization can be established from the shown rules alone. |
| `turn1_sn_verdict_quote` | verbatim text | Quote the shortest useful support span for `turn1_sn_verdict`. |
| `turn1_primary_method_answer_span` | verbatim text | Quote the span where the model gives its main proof route or main reason. |
| `turn1_primary_method` | text or blank | Write the model's surface method label when recoverable. |

## Turn 2 Fields

| Column | Values | Extraction rule |
|---|---|---|
| `turn2_q1_method_answer_span` | verbatim text | Quote the answer to Q1 about what method the previous answer used. |
| `turn2_primary_method` | text or blank | Write the model's surface method label from the Q1 answer. |
| `turn2_q2_answer_span` | verbatim text | Quote the answer to Q2 about imported proof structure, ordering choice, interpretation, or assumptions. |
| `turn2_q2_imports_external` | `yes`, `no` | Extract the model's own yes/no answer to Q2. |
| `turn2_q3_answer_span` | verbatim text | Quote the answer to Q3 about boundary placement. |
| `turn2_q3_outside_boundary` | `yes`, `no` | Extract the model's own yes/no answer to Q3. |
| `turn2_q4_still_sn` | `yes`, `no`, `unclear` | Extract the model's answer to whether the system is still strongly normalizing apart from boundary compliance. |
| `turn2_q4_quote` | verbatim text | Quote the shortest useful support span for `turn2_q4_still_sn`. |

## Quote Rules

- Quotes must be literal substrings of the corresponding response file.
- Prefer one concise sentence or clause.
- Do not paraphrase.
