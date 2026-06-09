# Geometry Stack and Constraint Ratchet Doctrine

Purpose: establish the formal doctrine for stacking geometries as non-commutative constraint layers.

Status: active current doctrine page.

Source: `/Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/new docs/plans/geometry_stack_ratchet_doctrine.md` (2026-04-14).

## Core Claim

Stacked geometries form a **real ratcheting constraint layer** IFF the stack is **non-commutative** ($A \circ B \neq B \circ A$ on some probe state). If you can freely swap order, it is not a ratchet — just independent filters.

## Why This Matters

The geometric constraint manifold is described as nested simultaneous shells where inner shells are MORE constrained than outer. For this nesting to be a ratchet (rather than a decorative hierarchy), the composition of shells must be order-sensitive. Non-commutativity IS the constraint ratchet.

## Verification Markers

- **Pairwise geometry couplings**: $A \circ B$ on probe $P$ vs $B \circ A$ on $P$ $\to$ assert inequality.
- **BCH commutator**: non-zero $[A,B]$ = non-trivial stacking.
- **z3 UNSAT**: probe admissible under $A \circ B$ $\to$ excluded under $B \circ A$.
- **Triple/N-stack**: of $N!$ orderings, only a subset admits a witness.
- **Commuting pair controls**: use as negative controls (not targets).

## Candidate Math

The **G-tower reduction chain** ($GL \to O \to SO \to U \to SU \to Sp$) is the leading candidate for the ratchet carrier:
- Each reduction tightens structure group.
- Chain order is rigid in 5/6 tested adjacent pairs.
- z3 UNSAT proofs exist for invalid-order reductions (sim_gtower_order_z3_unsat_invalid_reduction_order).

## Tool Discipline

- **clifford** (Cl(3), Cl(6), Pin/Spin): natural carrier of non-commutative rotor composition.
- **sympy** (Pauli algebra, BCH): closed-form commutators.
- **e3nn**: equivariant irrep composition.
- **z3 / cvc5**: UNSAT proof of excluded-reversed-order.
- **NO numpy** for decisive non-commutativity computations; numpy matrix products lose the rotor/bivector structure.

## Evidence (2026-04-14)

- **10/10 non-commutative pairs** confirmed $A \circ B \neq B \circ A$.
- **5 rigid G-tower adjacent reductions**.
- **Commuting controls** correctly classified as non-ratcheting.

## Related notes
- [[read-first]]
- [[active-intentions]]
- [[g-tower-hopf-weyl-integration]]
- [[ratcheting-as-obstruction-and-refinement]]
- [[geometry-stack-ratchet-doctrine]]
