last_updated: 2026-04-16

# F01 and N01: The Nominalist Axioms

Every process rule in this system traces back to two root constraints. Not as convention, not as good practice — as derivation. If you cannot trace a rule to F01 or N01, it is either a convention (acceptable as policy) or noise (delete it).

---

## The Two Axioms

**F01 — Finitude:**
Any probe, batch, wave, or sim must be bounded. Infinite exploration of allowed space is excluded. Each layer admits a finite survivor set. Each check must terminate. Each batch has a bounded capacity.

**N01 — Non-commutation:**
Layer ordering is load-bearing. A∘B ≠ B∘A. Information flows in one direction: layer N sees layers 0 through N-1, not N+1. Kills are irreversible. Order is not a convenience — it is a constraint.

---

## All Process Rules Are Derivations

This table is not exhaustive. It shows the derivation structure:

| Process rule | Root constraint |
|---|---|
| Bounded wave sizes (no "run all 1125 at once") | F01 |
| Probe capacity limits per batch | F01 |
| Each sim must terminate (exit 0) | F01 |
| Survivor set is finite and listed | F01 |
| Shell-local before pairwise coupling | N01 |
| Coupling program steps 1-6 in order | N01 |
| No bridge claims before steps 1-5 | N01 |
| Re-ratcheting enters at layer 0 | N01 |
| No peeking at later shell constraints | N01 |
| Kills are permanent (no un-excluding) | N01 |

These are not independent design choices. They are what F01 and N01 look like when applied to the research process.

---

## Worked Example: Coupling Program Step Order

The coupling program runs steps 1-6 in strict order. Why?

Step 1 (shell-local sims) and Step 4 (topology-variant reruns) are not interchangeable. If you run Step 4 before Step 1, you have no shell-local baseline. The comparison has no ground. Step 4 on its own is not a step — it is noise.

This is N01: the ordering is the constraint. A∘B ≠ B∘A means running step 4 before step 1 is a different operation, not a shortcut to the same result. It is excluded.

---

## Self-Similarity

F01 and N01 constrain objects. They also constrain the process studying those objects. The ratchet is the constraints applied to themselves.

There is no privileged external viewpoint from which to study the system. The process is subject to the same constraints as the objects. Finitude applies to the researcher. Non-commutation applies to the research steps. Every batch rule, every step gate, every probe limit is a consequence — not a convention.

---

See [02_constraint_admissibility_primer.md](02_constraint_admissibility_primer.md) for how constraints eliminate.
See [06_coupling_program_order.md](06_coupling_program_order.md) for step-order protocol.
