---
title: IGT Pattern Structure (independent of QIT engines)
created: 2026-04-15
updated: 2026-06-06
type: concept
tags: [igt, iching, pattern, topology, degrees-of-freedom, candidate]
framing: current
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# IGT Pattern Structure (independent of QIT engines)

## What this page is

A record of the structural properties of the IGT win/lose/WIN/LOSE pattern system — and the I-Ching / hexagram patterns connected to it — as an independent object to be simmed on its own terms.

**Critical framing rule**: IGT and I-Ching patterns are their own simulation target. The QIT engines are a separate system. If these two independently-simmed systems later converge on the same invariants, that convergence is Rosetta evidence. Do not assert the connection in advance. Do not write "win/lose = fiber loops" as current doctrine. Sim both independently and let the pattern speak.

**Anti-collapse rule**: The degrees of freedom are not defined by the 4 outcome labels. They are defined by how win/lose and WIN/LOSE scales create and constrain behavior *differently*. Do not merge the two scales. Do not treat CW/CCW as a labeling choice. The engine nuances (if any) come from the pattern itself — they are not imposed from outside.

---

## The IGT carrier structure

The IGT carrier set is exactly: {win, lose} × {WIN, LOSE} = {−1,+1}²

Four carriers, two independent binary axes:
- **Small axis** (lowercase): win/lose — short-horizon, microscale outcome
- **Large axis** (uppercase): WIN/LOSE — long-horizon, macroscale attractor

These are **not** the same quantity at two scales. They are structurally independent. `win` nested inside `LOSE` is a valid and important configuration — the long-horizon attractor is not the sum of short-horizon signs.

The 4 carriers sit on a cyclic 4-ring (yin/yang square) where adjacency = single-axis flip:

```
(win, WIN) ─── (win, LOSE)
    │                │
(lose, WIN) ─── (lose, LOSE)
```

Edges = Hamming distance 1 (one axis flips). Diagonals = Hamming distance 2 (both axes flip simultaneously). Confirmed: `sim_igt_atom_2_structure.py` (4-cycle, 4 edges, 2 diagonals).

---

## The key observation: only 2 symmetrical patterns

From the 4-ring, **only 2 distinct symmetrical traversal patterns exist** (up to rotation equivalence):

1. **Pattern A (Clockwise / Inductive)**: (win,WIN) → (win,LOSE) → (lose,LOSE) → (lose,WIN) → back
   - Axis-0 flip first, then Axis-2 flip, alternating: Ax0 → Ax2 → Ax0 → Ax2
   - In terrain language: Se → Si → Ni → Ne

2. **Pattern B (Counter-clockwise / Deductive)**: (win,WIN) → (lose,WIN) → (lose,LOSE) → (win,LOSE) → back
   - Axis-2 flip first, then Axis-0 flip, alternating: Ax2 → Ax0 → Ax2 → Ax0
   - In terrain language: Se → Ne → Ni → Si

These are the ONLY 2 options. Not 4, not 8 — 2. The symmetry group of the 4-ring is the dihedral group D₄, but the two distinct directed cycles (CW vs CCW) are not equivalent under any reflection that preserves the carrier semantics (win/WIN independence).

This 2-ness forced the engine structure. Two independent engines. One CW, one CCW. Not more.

---

## Candidate connections to QIT (NOT asserted — to be tested)

These are observations from the discovery path. They are recorded here as candidates for future sim testing, not as current doctrine.

- The 2-pattern uniqueness (CW/CCW) *might* correspond to the two independent engine chiralities. Not confirmed. Sim both independently first.
- The two-scale nesting (short-horizon inside long-horizon) *might* correspond to inner/outer loop topology in the engine. Not confirmed.
- The 4-ring structure *might* map onto terrain families (Se/Si/Ne/Ni). Not confirmed. This is a correlation layer, not primary math.

**The right question**: when IGT sims and QIT engine sims are run fully independently, do any invariants agree? If yes — what invariant, under what conditions, with what tolerance? That is the Rosetta question.

2026-06-06 route update: when the owner says all models are different perspectives on the same thing, preserve the broader convergence route in [[model-convergence-qit-engine-full-stack]]. That page does not erase this independence rule. It says the recurring skeleton may be one proposed constraint/carrier/geometry stack, while each IGT-to-QIT correspondence still needs a finite map and a distinct-control receipt before it becomes more than Rosetta pressure.

---

## What the DOFs actually are (anti-collapse)

The DOFs are NOT:
- 4 outcome labels (win, lose, WIN, LOSE)
- 2 binary axes acting independently and interchangeably
- The specific terrain names if they appear

The DOFs ARE defined by:
1. **Independence of the two scales** — win/lose and WIN/LOSE cannot be conflated. Short-horizon and long-horizon are structurally separate. win nested inside LOSE ≠ win nested inside WIN.
2. **Direction of traversal** — CW and CCW are not equivalent. Collapsing them loses whatever chirality the pattern contains.
3. **Attractor is not the sum of rounds** — The long-horizon WIN/LOSE label is not recoverable from summing short-horizon win/lose signs in general. The nesting structure is the information.

These DOFs must be preserved in any sim. If a sim flattens them, it is not testing the IGT system.

---

## What needs to be simmed (IGT/I-Ching lane, independent)

| Target | What to test | Tools |
|---|---|---|
| 2-pattern uniqueness | z3 UNSAT: no 3rd symmetrical traversal exists on 4-ring under scale-independence constraint | z3 |
| Attractor irreducibility | `sim_igt_deep_nested_win_lose_irreducibility.py` — already exists; check results | existing |
| I-Ching trigram/hexagram structure | 8 trigrams (3-bit), 64 hexagrams (6-bit) — what symmetry group? what adjacency? | sympy, rustworkx |
| Hexagram transition rules | Which hexagrams are adjacent under single-line change? What cycles exist? | rustworkx, z3 |
| Yin/yang nesting | Does the 2-level nesting (solid/broken line) produce a structure analogous to win/WIN? | classical_baseline first |
| IGT × I-Ching overlap | Do the 4 IGT carriers embed naturally into the 8 trigrams or 64 hexagrams? | open question |

None of these are confirmed connections to QIT. They are the IGT/I-Ching lane, to be run and let the results speak.

---

## Related pages

- [[axis-and-entropy-reference]] — Axis 4 (loop order family): inductive/deductive sequences are candidate IGT pattern analogs — not confirmed
- [[igt-four-strategy-perception-decomposition]] — current candidate perception-policy decomposition that keeps the locked IGT terrain spine separate from interpretive 4F/emotion/evolution/FEP/Hoffman readouts
- [[igt-atom-result-audit]] — artifact-facing audit of the atom chain and nearest follow-on result surfaces; keeps `exists` separate from rerun-backed status
- [[taijitu-probe-reconciliation-card]] — symbolic reconciliation card for what the taijitu layer can still say safely versus what remains fenced as witness language
- [[jungian-functions-and-igt-explicit-math-geometry-map]] — compact digest separating carrier geometry, operator math, ordered tokens, and IGT stage grammar
- jungian-functions-and-igt-explicit-math-geometry-map-copy (archived) — legacy source map
- [[constraint-on-distinguishability]] — two-scale distinguishability is relevant to win/WIN independence
