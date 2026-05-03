# Reviewer Guide: Raw Extraction Templates

```
released transcript -> direct response fields -> released CSV raw-column layer
```

This folder gives reviewers compact templates for reproducing the direct raw extraction layer of the benchmark.

For quality control, 15% of extracted sessions were randomly selected and audited by the author.

During dataset construction, extraction used independent passes by multiple agents, followed by consolidation and audit passes. These files are not a log of every historical instruction. They are clean reviewer templates distilled from the released transcripts, the retained raw CSV columns, and the audited field definitions.

Each template names only the direct response fields to extract for that test. Later derivation layers are handled elsewhere in the repository.

## Template Index

| Test | Template | Released CSV |
|---|---|---|
| Schema Test A - Primitive Duplicating Recursor | `schema-test-a.md` | `6.extracted-data/csv/schema-test-A-tests.csv` |
| Schema Test A New System - Non-Duplicating Control | `schema-test-a-new-system.md` | `6.extracted-data/csv/schema-test-A-new-system-tests.csv` |
| Schema Test B - Candidate Method Classification | `schema-test-b.md` | `6.extracted-data/csv/schema-test-B-tests.csv` |
| Test 01 - KO7 Kernel | `test-01-kernel.md` | `6.extracted-data/csv/test-01-kernel-tests.csv` |
| Test 02 - Completion Nat/Lex | `test-02-completion-nat-lex.md` | `6.extracted-data/csv/test-02-completion-tests-nat-lex.csv` |
| Test 03 - Completion Ordinal | `test-03-completion-ordinal.md` | `6.extracted-data/csv/test-03-completion-tests-ordinal.csv` |
| Test 04 - Measure Verification | `test-04-measure-verification.md` | `6.extracted-data/csv/test-04-measure-verification-tests.csv` |
| Test 05 - Candidate Class Reasoning | `test-05-candidate-class-reasoning.md` | `6.extracted-data/csv/test-05-candidate-class-reasoning-tests.csv` |
| Test 06 - Branch Realism | `test-06-branch-realism.md` | `6.extracted-data/csv/test-06-branch-realism-tests.csv` |
