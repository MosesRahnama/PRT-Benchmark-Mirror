# Schema Test B Raw Extraction Template

Use this template to extract direct method-classification fields from released Schema Test B sessions.

```
schema-test-B-tests/<session_slug>/response.txt -> method A-E answer fields
```

## Output Header

```csv
session_slug,model,provider,prompt_variant,method_A_terminates,method_A_in_boundary,method_B_terminates,method_B_in_boundary,method_C_terminates,method_C_in_boundary,method_D_terminates,method_D_in_boundary,method_E_terminates,method_E_in_boundary
```

## Field Rules

| Column | Values | Extraction rule |
|---|---|---|
| `session_slug` | folder name | Copy the session folder name exactly. |
| `model` | text | Copy the released model label. |
| `provider` | text | Copy the released provider label. |
| `prompt_variant` | `regular`, `control` | Copy the released prompt variant. |
| `method_A_terminates` | `yes`, `no`, `unclear`, blank | Extract the model's termination classification for method A. |
| `method_A_in_boundary` | `yes`, `no`, `unclear`, blank | Extract the model's boundary classification for method A. |
| `method_B_terminates` | `yes`, `no`, `unclear`, blank | Extract the model's termination classification for method B. |
| `method_B_in_boundary` | `yes`, `no`, `unclear`, blank | Extract the model's boundary classification for method B. |
| `method_C_terminates` | `yes`, `no`, `unclear`, blank | Extract the model's termination classification for method C. |
| `method_C_in_boundary` | `yes`, `no`, `unclear`, blank | Extract the model's boundary classification for method C. |
| `method_D_terminates` | `yes`, `no`, `unclear`, blank | Extract the model's termination classification for method D. |
| `method_D_in_boundary` | `yes`, `no`, `unclear`, blank | Extract the model's boundary classification for method D. |
| `method_E_terminates` | `yes`, `no`, `unclear`, blank | Extract the model's termination classification for method E. |
| `method_E_in_boundary` | `yes`, `no`, `unclear`, blank | Extract the model's boundary classification for method E. |

Use blank only when the response does not address that method or dimension.
