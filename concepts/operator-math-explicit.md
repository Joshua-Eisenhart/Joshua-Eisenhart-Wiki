---

title: Operator Math Explicit
created: 2026-04-07
updated: 2026-04-14
type: concept
tags: [reference, research, geometry, operators, channels]
sources:
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/ENGINE_MATH_REFERENCE.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/CONSTRAINT_ON_DISTINGUISHABILITY_FULL_MATH.md
  - /Users/joshuaeisenhart/Desktop/Codex Ratchet/system_v5/docs/17_actual_lego_registry.md
framing: current
---

# Operator Math Explicit

## Definition
This page gives the cleaned local operator packet in math-first form.

Scope caution:
This is a current-docs synthesis of the local operator layer, mainly from the engine math reference and related registry rows. It is useful for cleanup and dependency control, but the repo still marks the broader `operator_family_admission` bundle as needing deeper lego work rather than as a fully closed packet.

The key correction is that the intrinsic local operator layer is not an arbitrary list of symbolic labels. It is a small set of concrete channel/generator families acting on the admitted qubit carrier `D(C^2)`. UP and DOWN are not extra primitive operators. They are later orientation/order distinctions that appear only after terrain placement or loop/order choices are made.

## State object
The local state object is the qubit density matrix:
- `H = C^2`
- `D(H) = { rho in B(H) : rho >= 0, Tr(rho) = 1 }`

Bloch/decomposition form:
- `rho = 1/2 (I + r_x sigma_x + r_y sigma_y + r_z sigma_z)`

Equivalent scalar parameterization used by the engine math docs:
- `rho = (a, d, u, v)` with
  - `a,d >= 0`
  - `a + d = 1`
  - `u^2 + v^2 <= ad`

So the operator layer already presupposes admitted density-state structure and cannot be treated as earlier than carrier admission.

## Fixed matrices and local basis
### Pauli basis
The basic local operator basis is:
- `sigma_x`
- `sigma_y`
- `sigma_z`

These generate the local qubit algebra and support both dissipative and unitary families.

### Raising and lowering operators
The standard ladder operators are:
- `sigma_+ = |1><0| = (sigma_x + i sigma_y)/2`
- `sigma_- = |0><1| = (sigma_x - i sigma_y)/2`

These matter because the open terrain families are built from them, not from vague “up/down” symbolic moves.

### Projectors
The standard basis projectors are:
- `P_0 = (1/2)(I + sigma_z)`
- `P_1 = (1/2)(I - sigma_z)`

The X-basis projectors are:
- `Q_+ = (1/2)(I + sigma_x)`
- `Q_- = (1/2)(I - sigma_x)`

These support the dephasing families and make the basis-dependence of dissipation explicit.

## Four base operator families
The current engine math reference names four recurring local families in the present local packet.

### 1. Z-dephasing family
This is the `sigma_z` dissipation family.

Kraus form:
- `K_0 = sqrt(1-q_1) I`
- `K_1 = sqrt(q_1) |0><0|`
- `K_2 = sqrt(q_1) |1><1|`

Effect:
- destroys off-diagonal coherence in the Z basis
- preserves populations

This is not a generic “destruction” operator. It is a basis-specific coherence-killing family.

### 2. X-dephasing family
This is the `sigma_x` dissipation family.

Kraus/projector form uses `Q_+` and `Q_-`.

Effect:
- destroys coherence in the X basis
- mixes populations in the computational basis

This matters because the dephasing basis changes what counts as preserved structure.

### 3. X-rotation family
This is the unitary `sigma_x` rotation family.

Representative unitary:
- `U_x(theta) = exp(-i theta sigma_x / 2)`

Effect:
- rotates the Bloch vector around the x-axis
- preserves purity

### 4. Z-rotation family
This is the unitary `sigma_z` rotation family.

Representative unitary:
- `U_z(phi) = exp(-i phi sigma_z / 2)`

Effect:
- rotates the Bloch vector around the z-axis
- preserves purity

## Why only four local families
The current local qubit setting has:
- two main dissipative basis families in this packet
- two main unitary rotation families in this packet

That is why the docs keep talking about four recurring local operator families before terrain placement and later engine-order elaboration.

This does not mean the whole system has only four interesting transforms forever. It means this is the current bounded local packet that should be understood before more compound layers are promoted.

## Relation to terrain and loop language
Operator math comes before full terrain placement but after carrier admission.

This means:
- the four base families are intrinsic local operator/channel families
- terrain placement puts those families onto left/right sheets and fiber/base loop contexts
- loop order, UP/DOWN, and signed variants are later organization layers, not extra primitive operators

So a dev or LLM should not read placement labels as if they were the base mathematics.

Also keep two order rows separate:
- `composition_order_sensitivity` is the local operator/channel order test
- `composition_order_noncommutation` is the later engine/placement composition object

They are related, but they should not be flattened into the same row.

## Relation to the geometry spine
This page belongs in the middle of the spine:
- after density-state admission
- after spinor/Hopf/Weyl setup is explicit enough to know what the operators act on
- before broad engine claims
- before flux promotion

In practical queue terms this is the operator packet that should sit near:
- `pauli_generator_basis`
- `clifford_generator_basis`
- `local_operator_action`
- `left_right_asymmetry`
- `composition_order_sensitivity`
- `channel_cptp_map`

## Relevance to this system
This page matters because your system is not trying to build engines out of arbitrary symbolic labels. It is trying to build them out of admissible local transforms on admitted information states.

That makes operator math foundational for:
- local legality
- channel composition
- left/right asymmetry
- terrain placement
- later engine cycles

## Open questions
- Which of the four local operator families remain distinct once they are placed on the Weyl/loop geometry packet?
- Which local operator distinctions survive same-carrier geometry cross-checks?
- How should the Pauli/local channel packet connect to the stronger Clifford/operator-admission packet without collapsing them together?
- Which order-sensitive distinctions become genuinely load-bearing at the local operator level rather than only at later engine assembly?

## Related pages
- [[engine-math-reference]]
- [[terrain-laws-and-loop-geometry]]
- [[operator-algebras-and-representation]]
- [[cptp-maps-and-channels]]
- [[constraint-on-distinguishability-full-math]]
- [[sim-build-spine-and-wiki-maintenance]]
- [[qit-engine-dev-framing]]
- [[clifford-algebra-qit]]
- [[density-matrix-mathematics]]
