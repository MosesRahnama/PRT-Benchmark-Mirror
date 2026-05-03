# Test 04 Numbers (PRT manuscript: tab:t04 and body 6.2)

- Generated: 2026-05-03
- Reproduces: appendix `tab:t04` and the Test 04 body-prose numbers in section 6.2.
- Denominator: n=108.

## Source fields

- `measure_sound_correctness` == Correct iff the response correctly judges the supplied measure unsound.
- `phase_exposure_localization_correctness` == Correct iff the response localizes to the wrapper-exposure (phase-exposure) branch.
- `overall_test04_correctness` == Correct iff both axes match gold.
- Decoy-only conjunction: `r_rec_succ_cited == 'yes'` AND `phase_exposure_localization_correctness != 'Correct'`. This is the 33/108 (30.6%) figure in the body.

| Field and value | Count | Rate |
| --- | --- | --- |
| measure_sound_correctness = Correct (measure is unsound) | 84 | 77.8% |
| phase_exposure_localization_correctness = Correct | 75 | 69.4% |
| overall_test04_correctness = Correct | 74 | 68.5% |
| Decoy-only (R_rec_succ cited without phase exposure) | 33 | 30.6% |
