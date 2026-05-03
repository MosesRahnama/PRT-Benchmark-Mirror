# Cross-test method-class and verdict consistency: Schema A + SANS + Test 01

- Generated: 2026-05-03
- Source CSVs: Schema A (n=108), SANS (n=108), Test 01 (n=324)
- Total pooled sessions: 540
- Model panel: 27 models (~20 sessions per model)

## What this analysis measures

For each model, all sessions across the three open-ended generation tasks are pooled (Schema A duplicating, SANS non-duplicating control, Test 01 KO7 + Fruit). Two fields are tracked: the termination verdict and the normalised primary method class. 'Changes' means the model produced at least two distinct non-blank values for that field across its pooled sessions. 'Dominant class per test' is the most frequent non-blank method class within each test's sessions for that model; 'cross-test class drift' is True when the dominant class differs across at least two of the three tests. Method-name granularity is intentionally not tracked: it is noisier than method class and obscures the load-bearing signal.

## Source fields

- `model`: canonical model identifier used for cross-CSV grouping; `canonical_model()` from `_common.py` normalises the o3 entry so all three CSVs join on the same key.
- `turn1_sn_verdict` (Schema A, SANS) / `sn_verdict` (Test 01): per-session termination verdict; tracked for distinct-value counts and for the within-Test-01 verdict-flip rate reported below.
- `turn1_norm_primary_method_method_class` (Schema A, SANS) / `norm_primary_method_method_class` (Test 01): canonical primary method-class label; tracked for distinct-value counts, dominant-class-per-test, and cross-test class drift.
- `source_test`: synthetic in-memory key (`schema_a` / `sans` / `test01`) added at load time to tag each pooled row with its origin CSV; never touched in the source CSVs.

Blank or whitespace-only values are excluded from every distinct-value set so missing data is never counted as a method choice.

## Aggregate: models that change across the three tests

Each row counts models whose value for that field varies across their 20-session pool.

| Signal | Count | Rate |
| --- | --- | --- |
| Models changing termination verdict (sn_verdict) | 15 | 55.6% |
| Models changing primary method class | 27 | 100.0% |
| Models with cross-test dominant-class drift | 21 | 77.8% |
| Models with > 2 distinct method classes | 25 | 92.6% |

Note: the pooled termination-verdict change above (15/27) is not the same quantity as the manuscript's within-Test-01 verdict-flip count (12/27). The paper-facing rows below separate those definitions explicitly.

## Paper-facing consistency checks

These rows are the exact instability definitions used by the manuscript abstract and Appendix Table `tab:instability`. They deliberately separate pooled three-task changes from within-Test-01 rerun instability.

| Signal | Count | Rate |
| --- | --- | --- |
| Models switching primary method class within at least one open-ended task (Schema A, SANS, or Test 01) | 27 | 100.0% |
| Models switching primary method class within Test 01 only | 26 | 96.3% |
| Models using > 2 primary method classes within Test 01 only | 15 | 55.6% |
| Models flipping termination verdict within Test 01 only | 12 | 44.4% |

## Distribution: distinct method-class count per model

How many distinct primary method classes does each model use across its combined Schema A + SANS + Test 01 sessions?

| Distinct method classes | Models | Share |
| --- | --- | --- |
| 2 | 2 | 7.4% |
| 3 | 7 | 25.9% |
| 4 | 13 | 48.1% |
| 5 | 4 | 14.8% |
| 6 | 1 | 3.7% |

## Per-model breakdown

Per-model summary. Dom-class columns show the most frequent primary method class within that model's sessions for each task. Drift = Yes when the dominant class differs across at least two tasks.

| Model | Sessions | Distinct termination verdicts | Distinct method classes | Dom class Schema A | Dom class SANS | Dom class Test 01 | Drift |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Claude Haiku 4.5 | 20 | 2 | 4 | direct_measure | direct_measure | direct_measure | No |
| Claude Opus 4.5 | 20 | 1 | 5 | path_order | polynomial | polynomial | Yes |
| Claude Opus 4.6 | 20 | 1 | 4 | structural_descent | structural_descent | polynomial | Yes |
| Claude Sonnet 4 | 20 | 3 | 3 | direct_measure | objection | direct_measure | Yes |
| Claude Sonnet 4.5 | 20 | 2 | 4 | direct_measure | direct_measure | objection | Yes |
| Claude Sonnet 4.6 | 20 | 2 | 5 | structural_descent | objection | polynomial | Yes |
| DeepSeek R1 | 20 | 2 | 5 | objection | structural_descent | objection | Yes |
| DeepSeek V3.2 | 20 | 2 | 4 | objection | objection | objection | No |
| GLM-5 | 20 | 1 | 4 | direct_measure | structural_descent | direct_measure | Yes |
| GPT-4o | 20 | 3 | 4 | objection | objection | objection | No |
| GPT-5.2 | 20 | 1 | 4 | path_order | direct_measure | path_order | Yes |
| GPT-5.2 Codex | 20 | 2 | 4 | objection | objection | path_order | Yes |
| GPT-5.3 Codex | 20 | 1 | 4 | structural_descent | direct_measure | path_order | Yes |
| GPT-5.4 | 20 | 1 | 4 | path_order | direct_measure | path_order | Yes |
| GPT-5.4 Pro | 20 | 1 | 4 | polynomial | polynomial | polynomial | No |
| GPT-OSS-120B | 20 | 1 | 2 | direct_measure | direct_measure | direct_measure | No |
| Gemini 2.5 Pro | 20 | 2 | 3 | path_order | structural_descent | objection | Yes |
| Gemini 3 Flash | 20 | 2 | 2 | path_order | objection | objection | Yes |
| Gemini 3.1 Pro | 20 | 1 | 3 | path_order | polynomial | polynomial | Yes |
| Grok 3 | 20 | 2 | 3 | path_order | objection | objection | Yes |
| Grok 4 | 20 | 2 | 5 | transformed_calls | direct_measure | structural_induction | Yes |
| Grok 4 Fast (reasoning) | 20 | 1 | 4 | structural_descent | structural_descent | direct_measure | Yes |
| Grok 4.1 Fast (reasoning) | 20 | 1 | 3 | direct_measure | direct_measure | structural_induction | Yes |
| Grok 4.20 Reasoning | 20 | 2 | 4 | structural_descent | direct_measure | structural_induction | Yes |
| Grok Code Fast 1 | 20 | 2 | 6 | path_order | direct_measure | direct_measure | Yes |
| Qwen3 Max Thinking | 20 | 2 | 3 | objection | direct_measure | objection | Yes |
| o3 | 20 | 1 | 3 | direct_measure | direct_measure | direct_measure | No |

## Cross-test dominant class summary

Counts of models whose dominant primary method class shifts between tasks, by source-test pair. A shift is recorded when the dominant classes in the two tasks are both non-blank and differ.

| Task pair | Both non-blank | Dominant class differs | Rate |
| --- | --- | --- | --- |
| schema_a vs sans | 27 | 16 | 59.3% |
| schema_a vs test01 | 27 | 15 | 55.6% |
| sans vs test01 | 27 | 16 | 59.3% |
