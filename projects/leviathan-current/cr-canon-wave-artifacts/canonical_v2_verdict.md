# Final verdict: cand_canonical_v2.py

Bottom line: the four mechanical properties hold, verified by code I ran myself, not by the builder's report. But the sim is NOT canonical-by-process and an LLM cannot make it so. The honest status is `passes local rerun` at the `tool_lego_fit_probe` ceiling. Canonical-by-process needs the owner gate regardless, and the file correctly refuses to claim it.

File: `/private/tmp/claude-501/-Users-joshuaeisenhart-Desktop-Codex-Ratchet/bd0a70f9-f5d4-400e-b9dd-65fc573b2e75/scratchpad/canon_wave/cand_canonical_v2.py`
Receipt: `/private/tmp/claude-501/-Users-joshuaeisenhart-Desktop-Codex-Ratchet/bd0a70f9-f5d4-400e-b9dd-65fc573b2e75/scratchpad/canon_wave/a2_state/sim_results/cand_canonical_v2_results.json`

## 1. Did automated authoring produce a genuinely canonical-grade sim?

No — but it produced a clean, blind, sharp `tool_lego_fit_probe`. The mechanical sub-properties of canonical grade hold; the process label does not.

What I checked this session, with the command result, not the builder's claim:

- LINT exit 0. `py_compile` ok. `pylint -E` clean (exit 0). pyflakes/ruff/flake8 are absent from the Makefile interpreter (`/Users/joshuaeisenhart/.local/share/codex-ratchet/envs/main/bin/python3`); pylint -E is the available error-class signal. The repo's own `scripts/lint_sim_contract.py` reports `violation_total: 0` on this file.
- RUN exit 0. Stdout: `all_pass=true blind_ok=true sharp_ok=true g2=14 su3=8 two_unit=3`. Receipt written.
- BLIND derivation: true, and load-bearing. The decision functions `blind_dimension_via_smt` and `_z3/_cvc5_exists_kernel_outside_span` take only `(name, rows, ncols, span)` — no integer target. `blind_dim` is set solely from `len(span)` at the first SMT UNSAT. The literals 8/14/3 appear only in the `all_pass` reproduction gate (lines 596-599), never in the decision path. I ran the blind ladder on five independent inputs and it returned the correct, independently-known kernel dimension every time: g2 no-fix = 14, su3 fix-e1 = 8, two-unit = 3, full-rank identity rows = 0, empty rows = 64. It computes; it does not echo.
- SHARP control: true, and value-coupled, confirmed by three probes I ran:
  - Canonical flip: both-unit-fix outside the blind-computed 3-dim span = UNSAT (z3 and cvc5); drop one fix = SAT (z3 and cvc5).
  - Coupling probe A: replacing the 3-dim span with the 8-dim su3 span KILLS the flip (both queries UNSAT). The flip is tied to the specific value d2=3, not a generic always-flip artifact.
  - Pinning probe B: both-fix outside a (d2-1)-dim span = SAT. Combined with UNSAT at exactly d2, this pins the dimension to exactly 3.
- LOAD-BEARING confirmed by corruption: forcing every z3 verdict to "sat" flips `all_pass`, `blind_ok`, `sharp_ok` to False. Forcing cvc5's verdict does the same. Both solvers actually drive the result.

So all four target properties (blind + sharp-flip + lint0 + run0) are real and code-verified. The remaining gap is process, not math.

## 2. Honest classification, and what the owner must do to promote

Classification (held honestly by the file): `classification = "tool_lego_fit_probe"`, `promotion_allowed = false`, `formal_admission_allowed = false`. Receipt confirms the same. Status on the ladder: `passes local rerun` — not `canonical by process`.

This ceiling is correct per project doctrine. A `tool_lego_fit_probe` is pre-admission evidence only. By the repo's definition, `canonical by process` requires `passes local rerun` + SIM_TEMPLATE provenance + tool manifest + non-empty reasons + classification field — and, by the kernel rules, an independent fresh-context audit before any "canonical" label. An LLM (this one, or the builder) cannot self-certify that last step; a builder's verdict on its own work is never the evidence.

To promote, the owner must:

1. Apply scratch to repo. Move/author the sim under `system_v4/probes/` (or the designated probe dir) starting from `system_v4/probes/SIM_TEMPLATE.py`, and run it through the Makefile sim target so it executes under the canonical interpreter and guards, not as a free-standing scratch script.
2. Open the ceiling deliberately. Change `classification` to `"canonical"`, set `promotion_allowed`/`formal_admission_allowed` as the queue requires, and add a reconciled queue/registry row. This is an owner act, not an automated one.
3. Independent fresh-context audit. Hand the promoted file to a fresh agent that did not build or verify it, with no answer supplied. The audit must independently re-derive blind (14/8/3 from the solver ladder, no target fed) and re-run the sharp flip + coupling probe, and must come back clean on both implementation and the receipt's claims. High-rigor closure applies because a canonical label is durable and citable.

Only after step 3 returns clean is `canonical by process` earned. The label stays owner-gated regardless of how clean the mechanical checks look.

## 3. What an LLM could not clear

Nothing in the math blocked the automated build — blindness, sharpness, the verdict-flip, lint, and run were all achieved by automated authoring and survive adversarial corruption probes. The one thing an LLM cannot supply is the process authority: the independent fresh-context certification and the owner's decision to open the ceiling and reconcile a queue row. That is by design (builder is not auditor; gates are code and process, not LLM judgment). So the honest statement is: the automated loop reached the mechanical bar, but it cannot grant itself canonical-by-process. The owner must run the blind fresh audit and open the gate. No math is missing; the gate is.

## 4. Diff / summary vs the original scout

Source scout: `system_v5/ops/formal_scouts/foundation_foundation_r5_g2_su3_reduction_jax.py` (math reused honestly: Cayley-Dickson octonion structure constants, the derivation constraint matrix, unit-fixing rows, Der(O)=g2 dim 14, stabiliser of one imaginary unit = su(3) dim 8).

Two changes, both load-bearing and both code-verified here:

- Fix 1 — blind derivation. The scout passed `expected_dim=8` into the SMT and compared the RREF free-coordinate count to the literal 8 (answer fed to the solver). v2 feeds no target. The dimension is decided by a z3+cvc5 SAT(k)→UNSAT(k+1) ladder; RREF only mints candidate kernel vectors as witnesses, and the reported dimension is `len(span)` at the first UNSAT. Verified: ladder returns 14/8/3/0/64 on five inputs without being told any of them.
- Fix 2 — sharp value-coupled negative control. The scout had no verdict-flipping control. v2 computes a second, independently-known subalgebra blind (two-unit fixing → dim 3), then runs a value-coupled SMT: both-fix outside the 3-dim span = UNSAT, drop one fix = SAT. Dropping the control constraint flips the verdict, the flip dies when the span is swapped to the 8-dim su3 span (so it is coupled to the specific value 3), and a (d2-1)-span probe pins the dimension to exactly 3.

Net: v2 turns a by-construction, answer-fed scout into a blind-derivation + sharp-flipping probe, with z3 and cvc5 both load-bearing (corrupting either flips the verdict). It is a clean `tool_lego_fit_probe` at `passes local rerun`. It is not, and does not claim to be, canonical — that gate is the owner's.
