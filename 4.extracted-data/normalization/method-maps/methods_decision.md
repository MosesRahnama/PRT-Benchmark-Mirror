# Method Rename Decisions

Keep these canonical method names as-is:
- `direct_measure`
- `lexicographic_measure`
- `multiset_measure`
- `polynomial_interpretation`
- `ordinal_interpretation`
- `lpo`
- `rpo`
- `path_order_generic`
- `dependency_pairs`
- `structural_descent`
- `structural_induction`
- `well_founded_induction`
- `tait_computability`
- `objection_or_non_method`

Redundant `standardized_method_name` values to rename:
- `s_count_measure` -> `direct_measure`
- `s_depth_measure` -> `direct_measure`
- `s_nesting_depth_measure` -> `direct_measure`
- `s_chain_depth_measure` -> `direct_measure`
- `delta_count_measure` -> `direct_measure`
- `third_argument_height_measure` -> `direct_measure`
- `weight_measure` -> `direct_measure`
- `natural_number_interpretation` -> `polynomial_interpretation`
- `interpretation_argument` -> `polynomial_interpretation`
- `subterm_criterion` -> `dependency_pairs`
- `accessibility_induction` -> `well_founded_induction`
- `noetherian_induction` -> `well_founded_induction`
- `structural_recursion` -> `structural_descent`
- `primitive_recursion` -> `structural_descent`
- `induction_argument` -> `structural_induction`

One exception:
- If a row currently under `interpretation_argument` explicitly names an ordinal-valued interpretation, rename it to `ordinal_interpretation`, not `polynomial_interpretation`.
