# Schema B Numbers (PRT manuscript: tab:schema-b-per-method, tab:schema-b-method-sets, tab:schema-b-variant)

- Generated: 2026-05-03
- Reproduces: the three Schema B appendix tables plus body 6.2 numbers.
- Denominators: n=108 total, regular=54, control=54.

## Source fields

- `method_X_terminates` for X in A..E: method-level termination-success axis (does the named method itself soundly prove SN of the schema?).
- `method_X_in_boundary` for X in A..E: method-level boundary-admissibility (is the method admissible under the rule-extracted contract?).
- `norm_both_methods_count` and `norm_both_methods_has_X`: the final accepted-set encoding.
- `prompt_variant` in {regular, control}: regular = primary prompt; control = boundary-clarified rewording.
- Gold: A=yes/no, B=no/no, C=no/no, D=yes/yes, E=no/no; final set = {D}.

## Per-method compact summary (`tab:schema-b-per-method`)

**Both axes correct**: session matches gold on both `terminates` and `in_boundary`. **Yes/yes accepted**: session said yes/yes regardless of gold; for D this is the gold joint-recognition count, for A/B/C/E it is a false-rival acceptance count.

| Method | Gold status | Both axes correct | Yes/yes accepted | Interpretation |
| --- | --- | --- | --- | --- |
| A | method succeeds, boundary no | 15 | 87 | path-order recognized but boundary overaccepted |
| B | method fails, boundary no | 7 | 62 | polynomial false rival accepted |
| C | method fails, boundary no | 11 | 6 | KBO mostly rejected |
| D | method succeeds, boundary yes | 104 | 104 | correct method recognized when supplied |
| E | method fails, boundary no | 6 | 62 | direct-measure false rival accepted |
| Full five-method answer table correct | all method rows correct | 0 | - | exclusion discipline fails globally |

## Accepted method-set distribution (`tab:schema-b-method-sets`)

Final selection counts. Only `{D}` matches gold. Sets with at most three sessions are aggregated into the `Other` row.

| Method set | Verdict | Count | Rate |
| --- | --- | --- | --- |
| {A, B, D, E} | off-gold | 35 | 32.4% |
| {A, B, D} | off-gold | 20 | 18.5% |
| {A, D} | off-gold | 19 | 17.6% |
| {D, E} | off-gold | 10 | 9.3% |
| {A, D, E} | off-gold | 7 | 6.5% |
| {A, B, C, D, E} | off-gold | 4 | 3.7% |
| {D} | correct | 4 | 3.7% |
| Other method sets (each count <= 3, n=6 sets) | off-gold | 9 | 8.3% |

## Regular vs. control prompt variant (`tab:schema-b-variant`)

Regular prompt presents the five-method menu under the benchmark contract; control prompt is a clarified-boundary rewording that does not change the gold answer.

| Signal | Regular | Rate | Control | Rate |
| --- | --- | --- | --- | --- |
| A both axes correct | 0 | 0.0% | 15 | 27.8% |
| B both axes correct | 3 | 5.6% | 4 | 7.4% |
| C both axes correct | 0 | 0.0% | 11 | 20.4% |
| D both axes correct | 53 | 98.1% | 51 | 94.4% |
| E both axes correct | 4 | 7.4% | 2 | 3.7% |
| Selection = {D} alone | 0 | 0.0% | 4 | 7.4% |
| All five methods correct | 0 | 0.0% | 0 | 0.0% |
