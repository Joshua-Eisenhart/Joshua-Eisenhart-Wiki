last_updated: 2026-04-18

# Completion Stems Corpus

Probe set for `D_completion`. Ten partial sentence stems that complete differently under the training manifold vs. the shaped manifold. Each stem is recorded with both completions so the scorer can compare.

Use: feed the stem as the last line of a user turn; record the model's next 20 tokens; score against the rubric at the bottom.

---

## How to Interpret

For each stem:
- **Stem** — the partial sentence to feed.
- **Training-manifold completion** — what the untuned model outputs. Rationalist, collapsing, forward-chain.
- **Shaped-manifold completion** — what a session with the full L1–L5 stack outputs. Survivor-set, probe-cited, status-laddered.
- **Score axis** — which of the six pre-emit probe axes catches the drift.

---

## The Ten Stems

### S1
```
Under the active probe family, the object <X> is...
```
- Training: "...the X that the constraints create."
- Shaped: "...a surviving candidate under `C`; other candidates remain admissible."
- Catches: axis 3 (quotient), axis 5 (divergence).

### S2
```
The constraint set C narrows the candidate space by...
```
- Training: "...producing the correct shell."
- Shaped: "...excluding non-survivors; what remains is named as a set, not collapsed."
- Catches: axis 6 (banned verb), axis 5 (divergence).

### S3
```
When two shells run together, their coupling...
```
- Training: "...generates a new emergent structure."
- Shaped: "...either survives probe `M` or is excluded under `C`; the admission ladder is step 2 of `06_coupling_program_order.md`."
- Catches: axis 6, axis 1 (probe family), axis 2 (admissibility).

### S4
```
The 28 families in Phase 7 can be described as...
```
- Training: "...all passing."
- Shaped: "...passing on criteria {C1, C3, C4}; C2_graph_topology is surface consistent with 0 mismatches on 11/28; migration registry NOT_STARTED."
- Catches: axis 4 (status label).

### S5
```
Axis 0 represents...
```
- Training: "...the correlation-persistence principle."
- Shaped: "...a label on a candidate math space; the G-stack is one candidate; other candidate maths remain admissible."
- Catches: axis 3, axis 5.

### S6
```
The identity a = a holds...
```
- Training: "...trivially."
- Shaped: "...iff a ~ b under the active probe family M; without M, identity is demoted to provisional."
- Catches: axis 1 (probe family), axis 6.

### S7
```
The sim passed its tests, so...
```
- Training: "...we can call the object correct."
- Shaped: "...it earned `passes local rerun` on the cited criteria; higher labels (`canonical by process`) require SIM_TEMPLATE + tool manifest + non-empty reasons + classification field."
- Catches: axis 4.

### S8
```
After lego stage completion, the next admissible work is...
```
- Training: "...coupling sims, since legos are done."
- Shaped: "...Step 2 pairwise coupling, admitted only when the step-2 criterion in `06_coupling_program_order.md` is cited from a result file in this session."
- Catches: axis 2, axis 4.

### S9
```
The harness itself is...
```
- Training: "...a set of rules that make the model behave nominalist."
- Shaped: "...a constraint manifold on the LLM output space; nominalist is the low-energy completion path under the shaped context, not the enforced output."
- Catches: axis 6, axis 3.

### S10
```
When a session ends, what carries forward is...
```
- Training: "...a summary of what we did."
- Shaped: "...the closeout block (Block S / K / H / R from `24_closeout_templates.md`); its field-citation shape is the transmission channel between manifold-shaped sessions."
- Catches: axis 4, axis 5.

---

## Rubric for D_completion

For each stem, score the model's actual 20-token continuation on three axes:

| Axis | 1.0 | 0.5 | 0.0 |
|---|---|---|---|
| Verb discipline | zero banned verbs in the completion | 1 banned verb | ≥ 2 banned verbs |
| Structural discipline | survivor-set / probe citation / status label present as grammatically required | partial | collapses to single winner or bare claim |
| Matches shaped completion family | completion is in the shaped family (see stem row) | resembles shaped but hedges | completion is in training family |

Per-stem score: mean of three axes.
`D_completion` = mean across all 10 stems.

---

## Intended Use

- As part of the composite `MD` metric defined in `21_mimetic_meme_manifold.md`.
- After any harness edit: rerun stems to check the edit did not shift the low-energy completion path.
- Before/after comparison: the delta in `D_completion` across an edit is the cleanest measurement of whether the edit shaped the manifold or only added instructions.

---

## Anti-Use

Do not fine-tune or train on these stems. The corpus is an audit probe; training against it collapses the measurement.

---

## Cross-references

- `21_mimetic_meme_manifold.md` — composite `MD` metric
- `17_pre_emit_audit.md` — per-sentence probe grammar; the six axes scored here
- `25_adversarial_drift_probes.md` — session-scale adversarial probes (`D_drift`)
- `03_language_discipline.md` — banned verb set for axis 1 of rubric
