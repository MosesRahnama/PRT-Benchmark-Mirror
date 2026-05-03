# Data Statement for PRT-Benchmark

Version: 1.0.0
Date published: 2026-04-25
License: Polyform Noncommercial 1.0.0 with Commercial License Available (<DATASET_FILE_URL_PLACEHOLDER>/LICENSE)
Contact: anonymized@neurips.invalid

This data statement summarizes the population, scope, and intended use
of the dataset. For exhaustive details see `DATASHEET.md`.

## Records

Each record is one frontier LLM benchmark session: a single prompt-and-
response interaction between a large language model and a fixed
first-order termination-reasoning task. The release covers 1,188
sessions across 27 frontier models and nine task families.

## Languages and domains

All prompts and model responses are in English. The domain is formal
methods: term rewriting, primitive recursion, dependency-pair
termination methods, Lean 4 mechanized proofs, and the orientation
boundary at the step-duplicating recursor. The dataset is **not** a
sample of general natural-language interaction.

## Populations represented

Models: 27 frontier LLMs from seven providers (OpenAI, Anthropic, xAI,
Google, DeepSeek, Zhipu AI, Alibaba). Provider counts are unbalanced
by design (8 OpenAI, 6 Anthropic, 6 xAI, 3 Google, 2 DeepSeek, 1 Zhipu
AI, 1 Alibaba) to maximize provider-comparison statistical power.

Models accessed via either GitHub Copilot Chat in VS Code (OpenAI and
Anthropic) or direct provider APIs (xAI, Google, DeepSeek, Zhipu AI,
Alibaba via OpenRouter under the author's BYOK keys). All session
parameters left at provider defaults.

## Populations NOT represented

- non-frontier LLMs (open-source small models, fine-tuned variants);
- LLMs not available through one of the seven listed providers;
- humans solving the benchmark tasks;
- models accessed under workspace-augmented conditions (the benchmark
  protocol deliberately disables workspace access, web, retrieval, and
  contextual memory).

## Risks and misuse

- Treating PRT outputs as a general reasoning benchmark rather than a
  narrow formal-methods evaluation will produce misleading
  generalizations.
- Reusing PRT method-class judgments without respecting the
  rule-extracted boundary discipline (i.e. accepting any "yes" verdict
  as evidence of termination competence) will overcount model
  competence by roughly an order of magnitude (97% recognition vs. 1%
  retrieval gap).
- Provider defaults can drift without a model-version bump; the
  per-session timestamps pin each rate to its date window.

## Intended use

- Auditing frontier LLM behavior at a single, externally-checkable
  proof interface.
- Reproducible cross-provider termination-reasoning evaluation under
  controlled session-isolation conditions.
- Studying false formal legitimacy: proof-shaped, confident model
  outputs that are mathematically false or boundary-external on this
  kernel.
- Driving training-data and prompting research aimed at narrowing the
  recognition / retrieval gap on formal-methods obligations.

## Sensitive information

No human-subject data, no personally-identifying information beyond
the public author/contact metadata in the citation and license, no
content from copyrighted books or paywalled sources.
