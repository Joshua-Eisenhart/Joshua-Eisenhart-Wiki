last_updated: 2026-04-17

# Leviathan OS Constraint Map

Leviathan OS is a parallel project (`~/GitHub/leviathan/`, primary doc: `lev_mega_book_curated.pdf`). It runs the same nominalist/constraint/ratchet doctrine at the OS and computer science level. The two projects are not copies of each other — they are the same constraint structure applied at different scales.

When an LLM reads this wiki, it serves both projects.

---

## The Listed Kernel Constraints Compress to Two Roots

Lev docs still list five kernel constraints, but the current doctrine compresses them to two roots plus three derived consequences:

| Lev term | Status here | Codex-ratchet equivalent | What it constrains |
|---|---|---|---|
| **C1 — Finitude** | root | F01 | Bounded probe/batch/wave capacity; no unbounded exploration |
| **C2 — Non-commutation** | root | N01 | Ratchet ordering; A∘B ≠ B∘A; layer order is load-bearing |
| **C3 — Nominalized reality** | derived from C1 | Owner nominalist doctrine | Only named, validated artifacts survive; no implicit ambient objects |
| **C4 — Ratchet** | derived from C1+C2 | Codex-ratchet ratchet | Constraints only tighten; no un-excluding survivors |
| **C5 — Locality** | derived from C1 | Probe-relative scope | No ambient authority; every claim is probe-relative and scoped |

Across both projects, cite C1+C2 / F01+N01 as the primitive roots. Treat C3-C5 as earned consequences, not extra axioms.

---

## The Four Planes

Lev's runtime architecture has four operational planes:

- **FlowMind** — intent and goal representation
- **Orchestration** — scheduling, batch management, wave control
- **Graph** — relational structure of active objects and their edges
- **Event Bus** — communication between planes, ordered and scoped

This maps to the codex-ratchet layered constraint manifold at runtime scale. FlowMind is the admissibility condition surface — what is even in scope. Orchestration is the coupling program step manager — F01 applied to scheduling. Graph is the PyTorch computational graph / constraint manifold topology. Event Bus is the constraint propagation channel — N01 applied to information flow direction.

---

## Two Lev Primitives as Codex-Ratchet Analogs

**Lev Receipt = z3 UNSAT analog.**
A Receipt is a terminal proof that a transaction completed under constraint. It cannot be forged. It cannot be reversed. It is the Lev equivalent of z3 returning UNSAT on a constraint encoding — structural impossibility, not probabilistic confidence.

**Graph patch = admitted constraint update.**
When new evidence is incorporated into Lev's graph, it is a patch: a bounded, scoped, ordered update to the relational structure. Not a rewrite. Not ambient state mutation. This is what admitting a new constraint update looks like at OS scale — it follows C1 (bounded), C2 (ordered), C5 (scoped).

---

## Convergence

Codex-ratchet proves the math structures (sims, coupling programs, z3 proofs). Leviathan implements them as a running runtime (kernel constraints, planes, receipts). Rules here for sim behavior are not research conventions — they are the target architecture.

A coupling program step violated in codex-ratchet = C2 violated in Lev. Unbounded sim waves = C1 violated. The constraint map is shared across both projects.

---

See [12_f01_n01_nominalist_axioms.md](12_f01_n01_nominalist_axioms.md) for F01/N01 derivation.
See [07_z3_unsat_primacy.md](07_z3_unsat_primacy.md) for UNSAT as primary proof form.
