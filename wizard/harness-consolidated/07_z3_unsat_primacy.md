last_updated: 2026-04-16

# Z3 UNSAT Primacy: Why Impossibility Precedes Existence

Quantum mechanics speaks in negation. UNSAT — structural impossibility — is the primary proof form, not SAT (something works).

## The Asymmetry

**SAT (existence)**: We found values that satisfy the constraint. This lego survives the check. Good. Limited evidence.

**UNSAT (impossibility)**: No values can satisfy this constraint. This configuration is forbidden by structure. Stronger claim.

In quantum math, UNSAT is foundational:
- No-cloning: UNSAT for any map copying arbitrary qubit states
- No-broadcasting: UNSAT for shared optimal measurement on separated systems
- Uncertainty relations: UNSAT for simultaneous eigenstates of incompatible observables
- Monogamy of entanglement: UNSAT for state satisfying all mutual-information inequalities

These are the load-bearing theorems. They constrain what can persist, not what must exist.

## Why This Matters for Sims

In [06_coupling_program_order.md](06_coupling_program_order.md), each step uses z3 to ask: what configurations are forbidden?

- **Step 1 (shell-local)**: UNSAT on Pauli commutation in a nonclassical shell = shell rejects that operator family
- **Step 2 (pairwise)**: UNSAT on simultaneous eigenstate across two shells = shells are incompatible under naive composition
- **Step 4 (topology variant)**: UNSAT on a coupling under one topology but SAT under another = topology is not decorative

The surviving structures (SAT results) are what couple after UNSAT eliminates the impossible.

## The Pauli / Bare Hilbert / Flux-Carrier Example

Compare two claims:

1. **Existence claim (weaker)**: "Pauli ops with a flux carrier produced I_c > 0." That is SAT evidence. It shows one admissible witness.
2. **Structural claim (stronger)**: "Pauli ops cannot run admissibly on bare Hilbert without a flux carrier." That is an UNSAT target. If z3 excludes every bare-Hilbert encoding, the result is structural rather than contingent.

The second claim teaches more. It excludes an entire class of attempted worlds. The first only shows one world that survived.

## Integration Requirement

For [05_four_sim_kinds.md](05_four_sim_kinds.md), a tool-lego-integration sim on z3 means:
- The lego carries a structural claim (e.g., "operator families X and Y cannot coexist")
- z3 encodes the constraint set
- UNSAT confirms the claim is forced by structure, not contingency

Result: the claim earns [04_status_label_hierarchy.md](04_status_label_hierarchy.md) canonical-by-process status because the proof is load-bearing.

## Cross-references

- See ENFORCEMENT_AND_PROCESS_RULES.md Rule 7 and Rule 2 (repo) for tool role contract
