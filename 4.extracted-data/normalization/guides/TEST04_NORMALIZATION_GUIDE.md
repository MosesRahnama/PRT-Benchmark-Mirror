# Test 04 Normalization Guide

Files reviewed:
- `test-04-measure-verification-tests/3.extraction/TEST04_extractor_01.csv`
- `test-04-measure-verification-tests/3.extraction/TEST04_extractor_01.normalized.csv`
- `test-04-measure-verification-tests/3.extraction/TEST04_extractor_02.csv`
- `test-04-measure-verification-tests/3.extraction/TEST04_extractor_02.normalized.csv`
- `test-04-measure-verification-tests/3.extraction/TEST04_data.csv`
- `test-04-measure-verification-tests/3.extraction/TEST04_data.normalized.csv`
- `test-04-measure-verification-tests/3.extraction/TEST04_SOURCE_NORMALIZATION_NOTES.md`

Current on-disk behavior:
- The normalized files are append-only. No raw columns were removed.
- Both extractor normalized files add the same nine columns.
- The data normalized file adds the parallel `final_` versions plus the source-audit pair.

Extractor normalization columns added:
- `norm_failure_rule_family_broad`
- `norm_failure_localization_quality`
- `norm_response_truncated_flag`
- `norm_tool_spill_flag`
- `norm_phase_component_error_flag`
- `norm_problematic_answer_flag`
- `norm_needs_adjudication`
- `source_normalization_flag`
- `source_normalization_notes`

Data normalization columns added:
- `norm_final_failure_rule_family_broad`
- `norm_final_failure_localization_quality`
- `norm_final_response_truncated_flag`
- `norm_final_tool_spill_flag`
- `norm_final_phase_component_error_flag`
- `norm_final_problematic_answer_flag`
- `norm_final_needs_adjudication`
- `source_normalization_flag`
- `source_normalization_notes`

What was normalized and why:
- `failure_rule_family` was normalized into a broader family so related localization labels can be analyzed together rather than as brittle raw strings.
- A second derived field, `failure_localization_quality`, was added to distinguish precise localization from partial, absent, or incorrect localization.
- `response_truncated_flag` and `tool_spill_flag` were normalized for consistent quality control.
- `phase_component_error_flag` was normalized because misunderstanding the phase component is one of the central evaluator-facing error modes in this test.
- `problematic_answer_flag` and `needs_adjudication` were normalized for reviewer workflow control.
- `source_normalization_flag` and `source_normalization_notes` were added as the audit trail.

Rationale for the design:
- Test 04 is the only one in this group where the normalization layer explicitly derives higher-level analytic fields from a semantic raw field (`failure_rule_family`).
- That derivation is justified because the raw failure labels vary in specificity, and the reviewers need both a broad bucket and a quality-of-localization judgment.
- The normalized layer does not currently add every field described in the older notes. It adds only the currently present broad-family and localization-quality derivations plus the mechanical review flags.

Accuracy note:
- The source notes discuss a broader normalization design including additional normalized flags. Those extra fields are not present in the current normalized headers. This guide reflects the current on-disk files only.
