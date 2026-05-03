import Lake
open Lake DSL

package KO7Benchmark where
  moreLeanArgs := #["-Dpp.notation=true"]

@[default_target]
lean_lib KO7Benchmark where
  roots := #[`KO7Benchmark]

lean_lib KO7BenchmarkTheory where
  roots := #[`KO7BenchmarkTheory]

lean_exe ko7_answer_key_export where
  root := `KO7Benchmark.AnswerKeyExport

require mathlib from git "https://github.com/leanprover-community/mathlib4.git" @ "632465e4b02cb70a5dfa4cfe15468e8a62c2bd85"
