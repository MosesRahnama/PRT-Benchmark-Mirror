# Test 05 Raw Extraction Template

Use this template to extract direct candidate-answer fields from released Test 05 sessions.

```
test-05-candidate-class-reasoning-tests/<session_slug>/response.txt -> candidate answer fields
```

## Output Header

```csv
session_slug,model,provider,mu1_yes_no,mu2_yes_no,mu3_yes_no
```

## Field Rules

| Column | Values | Extraction rule |
|---|---|---|
| `session_slug` | folder name | Copy the session folder name exactly. |
| `model` | text | Copy the released model label. |
| `provider` | text | Copy the released provider label. |
| `mu1_yes_no` | `yes`, `no` | Extract the model's answer for candidate `mu1`. |
| `mu2_yes_no` | `yes`, `no` | Extract the model's answer for candidate `mu2`. |
| `mu3_yes_no` | `yes`, `no` | Extract the model's answer for candidate `mu3`. |
