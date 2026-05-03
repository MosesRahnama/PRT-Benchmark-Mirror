# Datasheet for PRT-Benchmark

Version: 1.0.0
Date published: 2026-04-25
Citation: Anonymous Authors (2026). The Primitive Recursor and the Representation-Shift Bottleneck in Frontier LLM Termination Reasoning. PRT-Benchmark v1.0.0.
License: Polyform Noncommercial 1.0.0 with Commercial License Available (<DATASET_FILE_URL_PLACEHOLDER>/LICENSE)
Contact: anonymized@neurips.invalid

This datasheet follows the structure of Gebru et al., "Datasheets for
Datasets" (CACM 2021), adapted to the conventions of the NeurIPS 2026
Evaluations & Datasets Track.

---

## 1. Motivation

**For what purpose was the dataset created?**

PRT-Benchmark was created to evaluate frontier large language model
behavior at the smallest natural first-order proof obligation where the
termination verdict, witness adequacy, rule-extracted boundary
admissibility, and supervisory typing first become separable. The
benchmark fixes the orientation boundary of the step-duplicating
primitive recursor as the test interface and grades model responses on
three answer-key axes against externally-checkable artifacts (TTT2 / CeTA
certifications and a companion mechanized Lean 4 theorem stack).

**Who created the dataset?**

Anonymous Authors (Anonymous Authors).

**Who funded the creation of the dataset?**

Anonymous Authors.

---

## 2. Composition

**What do the records represent?**

Each record is one benchmark session: one prompt-and-response interaction
between a frontier large language model and a fixed first-order
termination-reasoning task. The release covers nine task families, 27
frontier models, and 1,188 sessions in total.

**How many records are there?**

```
schema-test-A-tests                       108 sessions
schema-test-A-new-system-tests            108 sessions
schema-test-B-tests                       108 sessions
test-01-kernel-tests                      324 sessions  (162 KO7 + 162 Fruit)
test-02-completion-tests-nat-lex          108 sessions
test-03-completion-tests-ordinal          108 sessions
test-04-measure-verification-tests        108 sessions
test-05-candidate-class-reasoning-tests   108 sessions
test-06-branch-realism-tests              108 sessions
                                         ----
                                         1188 total
```

**What does each record consist of?**

Each session-folder under `5.test-sessions/<test>/<session>/` contains:
- `prompt.txt` -- prompt delivered to the model;
- `response.txt` -- final model output;
- `thinking.txt` -- captured reasoning transcript where available;
- `session.json` -- structured session metadata + full transcript;
- `README.md` -- generated index for the session.

The corresponding row in the per-test CSV under `6.extracted-data/`
carries adjudicated structured fields (verdict, primary-method class,
correctness columns, presence flags) projected from the session content.

**Are there labels or targets?**

Yes. Every per-test CSV carries one or more answer-key-derived
correctness columns (e.g. `termination_correctness`,
`method_mathematical_validity`, `method_correct_and_admissible`,
`overall_test02_correctness`, etc.). Answer-key targets are fixed by
externally-checkable artifacts (TTT2/CeTA termination certifications and
the companion Lean 4 theorem stack), not by author judgment.

**Is any information missing from individual records?**

No. Where a model declined to answer or returned an unparseable
response, the relevant answer-bearing field is recorded as a
controlled-vocabulary value (e.g. `unclear`, `objection`, `na`) rather
than left blank.

**Are relationships between records made explicit?**

Yes. Every CSV row joins to its raw session folder via the
`session_slug` / `session_id` fields. The Croissant metadata file
(`croissant.json`) declares this join via `cr:references` between the
CSV-backed RecordSets and the JSON-backed transcript RecordSets.

**Recommended data splits?**

There are no train / dev / test splits. The dataset is an evaluation
benchmark, not a training corpus. Models are evaluated session-by-session
under the documented session-isolation protocol; cross-session
aggregates are computed against the full per-test denominator.

---

## 3. Collection process

**How was the data collected?**

Each session was run interactively against a frontier model under
deliberately minimal context conditions (no workspace access, no web,
no retrieval, no instruction files, contextual memory disabled).
Provider-default sampling parameters were used; no temperature or
reasoning-effort overrides were applied beyond Copilot's `medium`
selector on the OpenAI and Anthropic Copilot routes. The full session
conditions are documented in the per-test prompts and in the public
release's session-environment notes.

**Over what time period?**

Sessions were collected during the public benchmark window leading up to
the 2026-04-25 release. Per-session timestamps in
`session.json` pin each interaction to its exact date and time.

**Were the individuals notified about the collection?**

Sessions are model-system interactions, not human-subject data. No
human-subject collection occurred.

---

## 4. Preprocessing / cleaning / labeling

**Was any preprocessing of the data done?**

Yes. Raw exported chat logs were processed by an in-repository Python
extraction pipeline into per-session JSON files and per-test CSV
exports. Adjudicated structured fields were produced through a
documented extraction-and-adjudication workflow that maps free-text
method labels to canonical method-class taxonomies. Normalization rules
are documented under `6.extracted-data/normalization/`.

**Was the raw data saved in addition to the cleaned data?**

Yes. The full transcript JSONs under `5.test-sessions/` carry the raw
prompt, model response, and thinking transcript exactly as captured;
the extracted CSVs carry the adjudicated projected columns.

---

## 5. Uses

**Has the dataset been used for any tasks already?**

The PRT-Benchmark companion paper (Anonymous, "The Primitive Recursor and
the Representation-Shift Bottleneck in Frontier LLM Termination
Reasoning") reports the headline empirical findings on this dataset.

**What other tasks could the dataset be used for?**

- benchmarking new frontier LLMs at the same orientation-boundary
  interface;
- studying confession-method retrieval (W2-family witness selection)
  under controlled conditions;
- auditing model outputs for false formal legitimacy on formal-methods
  obligations;
- training and evaluating discriminative annotators for proof-shaped
  outputs.

**What tasks should the dataset NOT be used for?**

PRT-Benchmark is a narrow benchmark over one primitive-recursion
family. It should not be treated as a general reasoning benchmark, a
coding-benchmark, or a representative sample of LLM behavior on
arbitrary natural-language tasks. Reusing benchmark outputs without
respecting the documented boundary discipline (rule-extracted versus
boundary-external method status) will produce misleading results.

---

## 6. Distribution

**How will the dataset be distributed?**

Public GitHub mirror at `<DATASET_URL_PLACEHOLDER>`.
Canonical archival mirror is intended for Harvard Dataverse once a
dataset DOI is obtained. Croissant metadata (`croissant.json`) and a
GitHub Pages landing page accompany the release.

**When will it be distributed?**

2026-04-25 (initial public release).

**Will the dataset be distributed under a copyright or license?**

Yes. Dual-license: PolyForm Noncommercial 1.0.0 governs all
non-commercial use; commercial use requires a separate paid agreement
obtained by contacting anonymized@neurips.invalid. See `LICENSE` for full terms.

---

## 7. Maintenance

**Who is supporting / hosting / maintaining the dataset?**

Anonymous Authors. Contact: anonymized@neurips.invalid.

**How can the owner be contacted?**

By email: anonymized@neurips.invalid.

**Is there an erratum?**

Errata, corrections, and version-to-version changes are tracked in
`CHANGELOG.md`. The Croissant metadata file is regenerated mechanically
from live data sources on every release, so file hashes and counts in
the metadata always match the released artifacts.
