# Within-test method-class and verdict consistency

- Generated: 2026-05-03
- Panel: 27 models
- Source CSVs: Schema A (n=108, 4/model), SANS (n=108, 4/model), Test 01 (n=324, 12/model = 6 KO7 + 6 Fruit).

Each surface is analysed independently on its own kernel. 'Changes' means the model produced at least two distinct non-blank values for the field across its repeated sessions on that surface. Blank or missing values are excluded from the distinct-value sets. Method-name granularity is not tracked: it is noisier than method class and obscures the load-bearing signal.

## Source fields

- `model`: canonical model identifier used to group each surface's sessions into 27 per-model pools; normalised through `canonical_model()` from `_common.py`.
- `turn1_sn_verdict` (Schema A, SANS) / `sn_verdict` (Test 01): session-level termination verdict. The per-model count of distinct non-blank values is the verdict-flip signal in the headline table.
- `turn1_norm_primary_method_method_class` (Schema A, SANS) / `norm_primary_method_method_class` (Test 01): canonical primary method-class label. The per-model count of distinct non-blank values is the method-class-change signal; counts above 2 feed the '>2 distinct method classes' column.
- `prompt_variant` (Test 01 only): `regular` for KO7-named sessions, `control` for fruit-renamed sessions. Used to split the Test 01 CSV into the KO7 (n=162) and Fruit (n=162) condition slices.

Blank or whitespace-only values are excluded from every distinct-value set so missing data is never counted as a verdict or method choice.

## Aggregate headline

| Surface | Change termination verdict | % | Change method class | % | >2 distinct method classes | % |
| --- | --- | --- | --- | --- | --- | --- |
| Schema A (n=108, 4/model) | 9 | 33.3% | 23 | 85.2% | 11 | 40.7% |
| SANS (n=108, 4/model) | 9 | 33.3% | 18 | 66.7% | 7 | 25.9% |
| Test 01 KO7 (n=162, 6/model) | 8 | 29.6% | 21 | 77.8% | 10 | 37.0% |
| Test 01 Fruit (n=162, 6/model) | 9 | 33.3% | 24 | 88.9% | 9 | 33.3% |
| Test 01 combined (n=324, 12/model) | 12 | 44.4% | 26 | 96.3% | 15 | 55.6% |

## Per-model: Schema A

Each row is one model's pool of 4 sessions on this surface. **Distinct termination verdicts** and **distinct method classes** count distinct non-blank values across the pool. Dominant class / verdict is the most frequent non-blank value.

| Model | Sessions | Distinct termination verdicts | Distinct method classes | Dominant method class | Dominant termination verdict |
| --- | --- | --- | --- | --- | --- |
| Claude Haiku 4.5 | 4 | 2 | 2 | direct_measure | yes |
| Claude Opus 4.5 | 4 | 1 | 2 | path_order | yes |
| Claude Opus 4.6 | 4 | 1 | 3 | structural_descent | yes |
| Claude Sonnet 4 | 4 | 1 | 1 | direct_measure | yes |
| Claude Sonnet 4.5 | 4 | 1 | 2 | direct_measure | yes |
| Claude Sonnet 4.6 | 4 | 1 | 3 | structural_descent | yes |
| DeepSeek R1 | 4 | 2 | 3 | objection | yes |
| DeepSeek V3.2 | 4 | 2 | 3 | objection | yes |
| GLM-5 | 4 | 1 | 3 | direct_measure | yes |
| GPT-4o | 4 | 2 | 2 | objection | no |
| GPT-5.2 | 4 | 1 | 2 | path_order | yes |
| GPT-5.2 Codex | 4 | 1 | 1 | objection | no |
| GPT-5.3 Codex | 4 | 1 | 3 | structural_descent | yes |
| GPT-5.4 | 4 | 1 | 1 | path_order | yes |
| GPT-5.4 Pro | 4 | 1 | 2 | polynomial | yes |
| GPT-OSS-120B | 4 | 1 | 2 | direct_measure | yes |
| Gemini 2.5 Pro | 4 | 2 | 3 | path_order | yes |
| Gemini 3 Flash | 4 | 1 | 1 | path_order | yes |
| Gemini 3.1 Pro | 4 | 1 | 2 | path_order | yes |
| Grok 3 | 4 | 2 | 2 | path_order | yes |
| Grok 4 | 4 | 2 | 2 | transformed_calls | yes |
| Grok 4 Fast (reasoning) | 4 | 1 | 3 | structural_descent | yes |
| Grok 4.1 Fast (reasoning) | 4 | 1 | 2 | direct_measure | yes |
| Grok 4.20 Reasoning | 4 | 2 | 3 | structural_descent | yes |
| Grok Code Fast 1 | 4 | 1 | 3 | path_order | yes |
| Qwen3 Max Thinking | 4 | 2 | 3 | objection | yes |
| o3 | 4 | 1 | 2 | direct_measure | yes |

## Per-model: SANS

Each row is one model's pool of 4 sessions on this surface. **Distinct termination verdicts** and **distinct method classes** count distinct non-blank values across the pool. Dominant class / verdict is the most frequent non-blank value.

| Model | Sessions | Distinct termination verdicts | Distinct method classes | Dominant method class | Dominant termination verdict |
| --- | --- | --- | --- | --- | --- |
| Claude Haiku 4.5 | 4 | 2 | 2 | direct_measure | yes |
| Claude Opus 4.5 | 4 | 1 | 2 | polynomial | yes |
| Claude Opus 4.6 | 4 | 1 | 1 | structural_descent | yes |
| Claude Sonnet 4 | 4 | 2 | 3 | objection | yes |
| Claude Sonnet 4.5 | 4 | 2 | 3 | direct_measure | no |
| Claude Sonnet 4.6 | 4 | 2 | 3 | objection | yes |
| DeepSeek R1 | 4 | 2 | 2 | structural_descent | yes |
| DeepSeek V3.2 | 4 | 1 | 1 | objection | no |
| GLM-5 | 4 | 1 | 1 | structural_descent | yes |
| GPT-4o | 4 | 1 | 1 | objection | no |
| GPT-5.2 | 4 | 1 | 2 | direct_measure | yes |
| GPT-5.2 Codex | 4 | 1 | 1 | objection | no |
| GPT-5.3 Codex | 4 | 1 | 2 | direct_measure | yes |
| GPT-5.4 | 4 | 1 | 3 | direct_measure | yes |
| GPT-5.4 Pro | 4 | 1 | 2 | polynomial | yes |
| GPT-OSS-120B | 4 | 1 | 1 | direct_measure | yes |
| Gemini 2.5 Pro | 4 | 1 | 2 | structural_descent | yes |
| Gemini 3 Flash | 4 | 1 | 1 | objection | no |
| Gemini 3.1 Pro | 4 | 1 | 2 | polynomial | yes |
| Grok 3 | 4 | 1 | 1 | objection | no |
| Grok 4 | 4 | 2 | 2 | direct_measure | yes |
| Grok 4 Fast (reasoning) | 4 | 1 | 2 | structural_descent | yes |
| Grok 4.1 Fast (reasoning) | 4 | 1 | 3 | direct_measure | yes |
| Grok 4.20 Reasoning | 4 | 2 | 3 | direct_measure | yes |
| Grok Code Fast 1 | 4 | 2 | 3 | direct_measure | yes |
| Qwen3 Max Thinking | 4 | 2 | 2 | direct_measure | yes |
| o3 | 4 | 1 | 1 | direct_measure | yes |

## Per-model: Test 01 KO7

Each row is one model's pool of 6 sessions on this surface. **Distinct termination verdicts** and **distinct method classes** count distinct non-blank values across the pool. Dominant class / verdict is the most frequent non-blank value.

| Model | Sessions | Distinct termination verdicts | Distinct method classes | Dominant method class | Dominant termination verdict |
| --- | --- | --- | --- | --- | --- |
| Claude Haiku 4.5 | 6 | 1 | 2 | direct_measure | yes |
| Claude Opus 4.5 | 6 | 1 | 4 | transformed_calls | yes |
| Claude Opus 4.6 | 6 | 1 | 2 | polynomial | yes |
| Claude Sonnet 4 | 6 | 2 | 2 | direct_measure | unclear |
| Claude Sonnet 4.5 | 6 | 2 | 2 | objection | no |
| Claude Sonnet 4.6 | 6 | 2 | 5 | objection | yes |
| DeepSeek R1 | 6 | 2 | 2 | objection | no |
| DeepSeek V3.2 | 6 | 1 | 1 | objection | no |
| GLM-5 | 6 | 1 | 2 | direct_measure | yes |
| GPT-4o | 6 | 2 | 3 | objection | no |
| GPT-5.2 | 6 | 1 | 3 | path_order | yes |
| GPT-5.2 Codex | 6 | 1 | 3 | direct_measure | yes |
| GPT-5.3 Codex | 6 | 1 | 3 | polynomial | yes |
| GPT-5.4 | 6 | 1 | 3 | path_order | yes |
| GPT-5.4 Pro | 6 | 1 | 2 | polynomial | yes |
| GPT-OSS-120B | 6 | 1 | 1 | direct_measure | yes |
| Gemini 2.5 Pro | 6 | 1 | 1 | objection | no |
| Gemini 3 Flash | 6 | 1 | 1 | objection | no |
| Gemini 3.1 Pro | 6 | 1 | 2 | polynomial | yes |
| Grok 3 | 6 | 2 | 2 | objection | no |
| Grok 4 | 6 | 2 | 4 | structural_induction | yes |
| Grok 4 Fast (reasoning) | 6 | 1 | 2 | direct_measure | yes |
| Grok 4.1 Fast (reasoning) | 6 | 1 | 1 | structural_induction | yes |
| Grok 4.20 Reasoning | 6 | 2 | 3 | direct_measure | yes |
| Grok Code Fast 1 | 6 | 1 | 3 | direct_measure | yes |
| Qwen3 Max Thinking | 6 | 1 | 1 | objection | no |
| o3 | 6 | 1 | 2 | direct_measure | yes |

## Per-model: Test 01 Fruit

Each row is one model's pool of 6 sessions on this surface. **Distinct termination verdicts** and **distinct method classes** count distinct non-blank values across the pool. Dominant class / verdict is the most frequent non-blank value.

| Model | Sessions | Distinct termination verdicts | Distinct method classes | Dominant method class | Dominant termination verdict |
| --- | --- | --- | --- | --- | --- |
| Claude Haiku 4.5 | 6 | 2 | 4 | direct_measure | yes |
| Claude Opus 4.5 | 6 | 1 | 1 | polynomial | yes |
| Claude Opus 4.6 | 6 | 1 | 4 | polynomial | yes |
| Claude Sonnet 4 | 6 | 2 | 2 | direct_measure | unclear |
| Claude Sonnet 4.5 | 6 | 2 | 2 | objection | no |
| Claude Sonnet 4.6 | 6 | 1 | 3 | polynomial | yes |
| DeepSeek R1 | 6 | 2 | 2 | objection | no |
| DeepSeek V3.2 | 6 | 1 | 2 | objection | no |
| GLM-5 | 6 | 1 | 2 | direct_measure | yes |
| GPT-4o | 6 | 2 | 2 | objection | no |
| GPT-5.2 | 6 | 1 | 3 | polynomial | yes |
| GPT-5.2 Codex | 6 | 1 | 2 | path_order | yes |
| GPT-5.3 Codex | 6 | 1 | 3 | path_order | yes |
| GPT-5.4 | 6 | 1 | 4 | polynomial | yes |
| GPT-5.4 Pro | 6 | 1 | 3 | path_order | yes |
| GPT-OSS-120B | 6 | 1 | 1 | direct_measure | yes |
| Gemini 2.5 Pro | 6 | 2 | 2 | objection | no |
| Gemini 3 Flash | 6 | 2 | 2 | objection | no |
| Gemini 3.1 Pro | 6 | 1 | 3 | structural_descent | yes |
| Grok 3 | 6 | 1 | 1 | objection | no |
| Grok 4 | 6 | 1 | 2 | direct_measure | yes |
| Grok 4 Fast (reasoning) | 6 | 1 | 2 | direct_measure | yes |
| Grok 4.1 Fast (reasoning) | 6 | 1 | 2 | structural_induction | yes |
| Grok 4.20 Reasoning | 6 | 2 | 2 | structural_induction | yes |
| Grok Code Fast 1 | 6 | 1 | 4 | structural_induction | yes |
| Qwen3 Max Thinking | 6 | 2 | 2 | objection | no |
| o3 | 6 | 1 | 2 | direct_measure | yes |

## Per-model: Test 01 combined

Each row is one model's pool of 12 sessions on this surface. **Distinct termination verdicts** and **distinct method classes** count distinct non-blank values across the pool. Dominant class / verdict is the most frequent non-blank value.

| Model | Sessions | Distinct termination verdicts | Distinct method classes | Dominant method class | Dominant termination verdict |
| --- | --- | --- | --- | --- | --- |
| Claude Haiku 4.5 | 12 | 2 | 4 | direct_measure | yes |
| Claude Opus 4.5 | 12 | 1 | 4 | polynomial | yes |
| Claude Opus 4.6 | 12 | 1 | 4 | polynomial | yes |
| Claude Sonnet 4 | 12 | 2 | 2 | direct_measure | unclear |
| Claude Sonnet 4.5 | 12 | 2 | 2 | objection | no |
| Claude Sonnet 4.6 | 12 | 2 | 5 | polynomial | yes |
| DeepSeek R1 | 12 | 2 | 2 | objection | no |
| DeepSeek V3.2 | 12 | 1 | 2 | objection | no |
| GLM-5 | 12 | 1 | 2 | direct_measure | yes |
| GPT-4o | 12 | 3 | 4 | objection | no |
| GPT-5.2 | 12 | 1 | 4 | path_order | yes |
| GPT-5.2 Codex | 12 | 1 | 3 | path_order | yes |
| GPT-5.3 Codex | 12 | 1 | 3 | path_order | yes |
| GPT-5.4 | 12 | 1 | 4 | path_order | yes |
| GPT-5.4 Pro | 12 | 1 | 3 | polynomial | yes |
| GPT-OSS-120B | 12 | 1 | 1 | direct_measure | yes |
| Gemini 2.5 Pro | 12 | 2 | 2 | objection | no |
| Gemini 3 Flash | 12 | 2 | 2 | objection | no |
| Gemini 3.1 Pro | 12 | 1 | 3 | polynomial | yes |
| Grok 3 | 12 | 2 | 2 | objection | no |
| Grok 4 | 12 | 2 | 5 | structural_induction | yes |
| Grok 4 Fast (reasoning) | 12 | 1 | 2 | direct_measure | yes |
| Grok 4.1 Fast (reasoning) | 12 | 1 | 2 | structural_induction | yes |
| Grok 4.20 Reasoning | 12 | 2 | 3 | structural_induction | yes |
| Grok Code Fast 1 | 12 | 1 | 4 | direct_measure | yes |
| Qwen3 Max Thinking | 12 | 2 | 2 | objection | no |
| o3 | 12 | 1 | 3 | direct_measure | yes |
