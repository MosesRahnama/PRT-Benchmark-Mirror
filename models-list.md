# Model Roster - Coverage Status

Audit date: 2026-04-13

## Canonical role

This file is the **canonical model identity registry** for the benchmark.

Use it for:
- canonical display names;
- canonical providers;
- canonical slug prefixes;
- the authoritative 27-model roster.

Do not use `model-tests-overage.md` as the naming authority.
That file is a coverage audit derived from on-disk session folders.

This file lists every model in the project roster and shows, per test, how many sessions that model has completed vs how many the benchmark expects. Any cell below target is highlighted as **missing**.

Active roster: **27 models** (matches [model-tests-overage.md](model-tests-overage.md)).

- **Source of truth**: on-disk session folders under each test directory.
- **Target counts**: Schema A=4, Schema B regular=2, Schema B control=2, Schema A New System=4, Test 01 KO7=6, Test 01 Fruit=6, Test 02=4, Test 03=4, Test 04=4, Test 05=4, Test 06=4. Target total per model is **44** sessions.

## Coverage matrix

26 of 27 models at full coverage (44/44). Below target: Grok 4.1 Fast (reasoning).

| # | Model | Provider | Schema A<br>(4) | Schema B<br>(2) | Schema B Ctrl<br>(2) | Schema A New<br>(4) | T1 KO7<br>(6) | T1 Fruit<br>(6) | T2<br>(4) | T3<br>(4) | T4<br>(4) | T5<br>(4) | T6<br>(4) | Total | Target |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Claude Haiku 4.5 | Anthropic | 4 | 2 | 2 | 4 | 6 | 6 | 4 | 4 | 4 | 4 | 4 | 44 | 44 |
| 2 | Claude Opus 4.5 | Anthropic | 4 | 2 | 2 | 4 | 6 | 6 | 4 | 4 | 4 | 4 | 4 | 44 | 44 |
| 3 | Claude Opus 4.6 | Anthropic | 4 | 2 | 2 | 4 | 6 | 6 | 4 | 4 | 4 | 4 | 4 | 44 | 44 |
| 4 | Claude Sonnet 4 | Anthropic | 4 | 2 | 2 | 4 | 6 | 6 | 4 | 4 | 4 | 4 | 4 | 44 | 44 |
| 5 | Claude Sonnet 4.5 | Anthropic | 4 | 2 | 2 | 4 | 6 | 6 | 4 | 4 | 4 | 4 | 4 | 44 | 44 |
| 6 | Claude Sonnet 4.6 | Anthropic | 4 | 2 | 2 | 4 | 6 | 6 | 4 | 4 | 4 | 4 | 4 | 44 | 44 |
| 7 | DeepSeek R1 | DeepSeek | 4 | 2 | 2 | 4 | 6 | 6 | 4 | 4 | 4 | 4 | 4 | 44 | 44 |
| 8 | DeepSeek V3.2 | DeepSeek | 4 | 2 | 2 | 4 | 6 | 6 | 4 | 4 | 4 | 4 | 4 | 44 | 44 |
| 9 | Gemini 2.5 Pro | Google | 4 | 2 | 2 | 4 | 6 | 6 | 4 | 4 | 4 | 4 | 4 | 44 | 44 |
| 10 | Gemini 3 Flash | Google | 4 | 2 | 2 | 4 | 6 | 6 | 4 | 4 | 4 | 4 | 4 | 44 | 44 |
| 11 | Gemini 3.1 Pro | Google | 4 | 2 | 2 | 4 | 6 | 6 | 4 | 4 | 4 | 4 | 4 | 44 | 44 |
| 12 | GLM-5 | Zhipu AI | 4 | 2 | 2 | 4 | 6 | 6 | 4 | 4 | 4 | 4 | 4 | 44 | 44 |
| 13 | GPT-4o | OpenAI | 4 | 2 | 2 | 4 | 6 | 6 | 4 | 4 | 4 | 4 | 4 | 44 | 44 |
| 14 | GPT-5.2 | OpenAI | 4 | 2 | 2 | 4 | 6 | 6 | 4 | 4 | 4 | 4 | 4 | 44 | 44 |
| 15 | GPT-5.2 Codex | OpenAI | 4 | 2 | 2 | 4 | 6 | 6 | 4 | 4 | 4 | 4 | 4 | 44 | 44 |
| 16 | GPT-5.3 Codex | OpenAI | 4 | 2 | 2 | 4 | 6 | 6 | 4 | 4 | 4 | 4 | 4 | 44 | 44 |
| 17 | GPT-5.4 | OpenAI | 4 | 2 | 2 | 4 | 6 | 6 | 4 | 4 | 4 | 4 | 4 | 44 | 44 |
| 18 | GPT-5.4 Pro | OpenAI | 4 | 2 | 2 | 4 | 6 | 6 | 4 | 4 | 4 | 4 | 4 | 44 | 44 |
| 19 | GPT-OSS-120B | OpenAI | 4 | 2 | 2 | 4 | 6 | 6 | 4 | 4 | 4 | 4 | 4 | 44 | 44 |
| 20 | Grok 3 | xAI | 4 | 2 | 2 | 4 | 6 | 6 | 4 | 4 | 4 | 4 | 4 | 44 | 44 |
| 21 | Grok 4 | xAI | 4 | 2 | 2 | 4 | 6 | 6 | 4 | 5 | 4 | 4 | 4 | 45 | 44 |
| 22 | Grok 4 Fast (reasoning) | xAI | 4 | 2 | 2 | 4 | 6 | 6 | 4 | 4 | 4 | 4 | 4 | 44 | 44 |
| 23 | Grok 4.1 Fast (reasoning) | xAI | 4 | 2 | 2 | 4 | 6 | 6 | 4 | 3 | 4 | 4 | 4 | 43 | 44 |
| 24 | Grok 4.20 Reasoning | xAI | 4 | 2 | 2 | 4 | 6 | 6 | 4 | 4 | 4 | 4 | 4 | 44 | 44 |
| 25 | Grok Code Fast 1 | xAI | 4 | 2 | 2 | 4 | 6 | 6 | 4 | 4 | 4 | 4 | 4 | 44 | 44 |
| 26 | o3 | OpenAI | 4 | 2 | 2 | 4 | 6 | 6 | 4 | 4 | 4 | 4 | 4 | 44 | 44 |
| 27 | Qwen3 Max Thinking | Alibaba | 4 | 2 | 2 | 4 | 6 | 6 | 4 | 4 | 4 | 4 | 4 | 44 | 44 |
|  | **Totals** |  | **108** | **54** | **54** | **108** | **162** | **162** | **108** | **108** | **108** | **108** | **108** | **1188** | **1188** |

## Models with complete coverage (44/44)

- Claude Haiku 4.5 (Anthropic)
- Claude Opus 4.5 (Anthropic)
- Claude Opus 4.6 (Anthropic)
- Claude Sonnet 4 (Anthropic)
- Claude Sonnet 4.5 (Anthropic)
- Claude Sonnet 4.6 (Anthropic)
- DeepSeek R1 (DeepSeek)
- DeepSeek V3.2 (DeepSeek)
- Gemini 2.5 Pro (Google)
- Gemini 3 Flash (Google)
- Gemini 3.1 Pro (Google)
- GLM-5 (Zhipu AI)
- GPT-4o (OpenAI)
- GPT-5.2 (OpenAI)
- GPT-5.2 Codex (OpenAI)
- GPT-5.3 Codex (OpenAI)
- GPT-5.4 (OpenAI)
- GPT-5.4 Pro (OpenAI)
- GPT-OSS-120B (OpenAI)
- Grok 3 (xAI)
- Grok 4 (xAI)
- Grok 4 Fast (reasoning) (xAI)
- Grok 4.20 Reasoning (xAI)
- Grok Code Fast 1 (xAI)
- o3 (OpenAI)
- Qwen3 Max Thinking (Alibaba)

## Plain roster

| # | Model | Provider | Slug prefix |
|---|---|---|---|
| 1 | Claude Haiku 4.5 | Anthropic | `claude-haiku-4.5` |
| 2 | Claude Opus 4.5 | Anthropic | `claude-opus-4.5` |
| 3 | Claude Opus 4.6 | Anthropic | `claude-opus-4.6` |
| 4 | Claude Sonnet 4 | Anthropic | `claude-sonnet-4` |
| 5 | Claude Sonnet 4.5 | Anthropic | `claude-sonnet-4.5` |
| 6 | Claude Sonnet 4.6 | Anthropic | `claude-sonnet-4.6` |
| 7 | DeepSeek R1 | DeepSeek | `deepseek-r1-0528` |
| 8 | DeepSeek V3.2 | DeepSeek | `deepseek-v3.2` |
| 9 | Gemini 2.5 Pro | Google | `gemini-2.5-pro` |
| 10 | Gemini 3 Flash | Google | `gemini-3-flash-preview` |
| 11 | Gemini 3.1 Pro | Google | `gemini-3.1-pro-preview` |
| 12 | GLM-5 | Zhipu AI | `glm-5` |
| 13 | GPT-4o | OpenAI | `gpt-4o` |
| 14 | GPT-5.2 | OpenAI | `gpt-5.2` |
| 15 | GPT-5.2 Codex | OpenAI | `gpt-5.2-codex` |
| 16 | GPT-5.3 Codex | OpenAI | `gpt-5.3-codex` |
| 17 | GPT-5.4 | OpenAI | `gpt-5.4` |
| 18 | GPT-5.4 Pro | OpenAI | `gpt-5.4-pro` |
| 19 | GPT-OSS-120B | OpenAI | `gpt-oss-120b` |
| 20 | Grok 3 | xAI | `grok-3` |
| 21 | Grok 4 | xAI | `grok-4-0709` |
| 22 | Grok 4 Fast (reasoning) | xAI | `grok-4-fast-reasoning` |
| 23 | Grok 4.1 Fast (reasoning) | xAI | `grok-4-1-fast-reasoning` |
| 24 | Grok 4.20 Reasoning | xAI | `grok-4.20-0309-reasoning` |
| 25 | Grok Code Fast 1 | xAI | `grok-code-fast-1` |
| 26 | o3 | OpenAI | `o3` |
| 27 | Qwen3 Max Thinking | Alibaba | `qwen3-max-thinking` |
