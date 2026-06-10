---
title: Two Engine WIN/LOSE Carnot/Szilard Pattern 2026-06-09
created: 2026-06-09
updated: 2026-06-09
type: project
status: current routing / finite-pattern result intake
claim_ceiling: finite combinatorics and sim-result routing only; no QIT-engine admission, no final M(C), no physics, no I Ching proof
sources:
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v6/sims/winlose_pattern_derivation_discriminator/results/winlose_pattern_derivation_discriminator_envelope_results.json
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v6/sims/winlose_pattern_derivation_discriminator/audit_verdict.md
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v6/foundations/symbolic_layer_iching_taijitu_20260609.md
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v6/foundations/working_math_scaffold_20260609.md
  - projects/codex-ratchet/dual-carnot-szilard-qit-engine-witness-2026-06-09.md
  - projects/codex-ratchet/qit-axes-terrain-operator-fold-2026-06-09.md
  - projects/codex-ratchet/pre-ai-rosetta-ring-checkerboard-provenance-2026-06-09.md
tags:
  - codex-ratchet
  - winlose
  - two-engine
  - igt
  - carnot
  - szilard
  - iching
  - qit-engine
---

# Two Engine WIN/LOSE Carnot/Szilard Pattern 2026-06-09

## Purpose

This page keeps the corrected two-engine WIN/LOSE pattern in one place so future workers do not flatten it into:

```text
one table
an unordered square
an I Ching premise
a full physics/QIT admission
```

The current safe claim is narrower and stronger:

```text
The paired two-engine WIN/LOSE/win/lose casing structure is unique under sign scaffold + operator placement.
It is not sign-only, and it is not yet an admitted physics/QIT theorem.
```

## Current proof location

Main result:

```text
/Users/joshuaeisenhart/Codex-Ratchet/system_v6/sims/winlose_pattern_derivation_discriminator/results/winlose_pattern_derivation_discriminator_envelope_results.json
```

Audit:

```text
/Users/joshuaeisenhart/Codex-Ratchet/system_v6/sims/winlose_pattern_derivation_discriminator/audit_verdict.md
```

Commit with hardening result:

```text
d2a62a89e sims: terrain hardened (Axis-0 (+,+,-,-) confirmed under participation-ratio; in/out polarity dominant) + winlose re-posed (chart UNIQUE given signs+operator: 36 -> 1)
```

## What was proven

Observed result fields:

```text
full_constraints: 36   # balance + case-inversion duality
selected_outcome_coupling: 1  # signs + operator placement
drop_balance: 256
```

Precise theorem-shaped statement:

```text
Given:
  - paired Type1/Type2 table space,
  - per-engine balance,
  - case-inversion duality,
  - documented sign scaffold,
  - operator placement,

the documented paired WIN/LOSE table is the unique satisfying assignment.
```

What the audit killed:

```text
b6 = -b0*b3 alone does not force the table.
```

The b6 relation is scaffold metadata consistency under the current sign conventions. It is not, by itself, a predicate that filters the 36 assignment models.

## The pattern object

There are **two engine types**. The object is a paired structure:

```text
(Type 1 WIN/LOSE/win/lose table, Type 2 WIN/LOSE/win/lose table)
```

Base stage words:

```text
Se = LoseWin
Ne = WinLose
Ni = LoseLose
Si = WinWin
```

Paired table:

| Stage | Type 1 | Type 2 |
|---|---|---|
| Se | `LOSEwin` | `loseWIN` |
| Ne | `WINlose` | `winLOSE` |
| Ni | `loseLOSE` | `LOSElose` |
| Si | `winWIN` | `WINwin` |

## Stage word vs active loop readout

Owner correction, 2026-06-09: an engine loop does **not** read the whole stage word as the active loop value.

```text
stage word = paired two-loop structure
active loop readout = selected component/case of that word
```

Example:

```text
Ni stage word = loseLOSE
active loop may read = lose
```

Example:

```text
Type 1 outer loop at WINlose stage reads WIN
```

This applies across the 16 strategies:

```text
2 engine types x 2 loops x 4 stages = 16 loop-readout strategies
```

## Carnot loop orders

Owner correction: the order matters because these are Carnot-style engine orders, not a decorative traversal.

Two directed Carnot loop orders:

```text
Se -> Ne -> Ni -> Si
Se -> Si -> Ni -> Ne
```

These orders must be preserved separately from the unordered four-word alphabet. The square/algebra view can encode the base alphabet, but the engine lives in the directed cycles.

## Loop-readout map

The loop order determines the active readout rhythm:

```text
Deductive order Se -> Ne -> Ni -> Si gives alternating:
LOSE -> WIN -> LOSE -> WIN
or lowercase lose -> win -> lose -> win.

Inductive order Se -> Si -> Ni -> Ne gives paired blocks:
WIN -> WIN -> LOSE -> LOSE
or lowercase win -> win -> lose -> lose.
```

So the invariant is:

```text
deductive cycle = alternating readout
inductive cycle = paired/block readout
```

Engine type determines which rhythm is outer vs inner and which casing appears. Avoid the loose phrase "engine type only sets phase" unless `phase` is explicitly defined as loop/sheet placement.

Type 1 placement:

```text
outer loop = deductive / closure / Carnot order Se -> Ne -> Ni -> Si
inner loop = inductive / expansion / Carnot order Se -> Si -> Ni -> Ne
```

Type 1 readouts:

```text
outer: LOSE -> WIN -> LOSE -> WIN
inner: win  -> win -> lose -> lose
```

Type 2 placement:

```text
outer loop = inductive / expansion / Carnot order Se -> Si -> Ni -> Ne
inner loop = deductive / closure / Carnot order Se -> Ne -> Ni -> Si
```

Type 2 readouts:

```text
outer: WIN  -> WIN -> LOSE -> LOSE
inner: lose -> win -> lose -> win
```

Compact table:

| Engine | Loop | Carnot order | Active readout sequence |
|---|---|---|---|
| Type 1 | outer | Se -> Ne -> Ni -> Si | LOSE -> WIN -> LOSE -> WIN |
| Type 1 | inner | Se -> Si -> Ni -> Ne | win -> win -> lose -> lose |
| Type 2 | outer | Se -> Si -> Ni -> Ne | WIN -> WIN -> LOSE -> LOSE |
| Type 2 | inner | Se -> Ne -> Ni -> Si | lose -> win -> lose -> win |

## Why this expands degrees of freedom without becoming arbitrary

The pattern expands legal degrees of freedom in a highly constrained geometry:

```text
four stage words
+ two directed Carnot cycles
+ two engine placements
+ loop-selected readout components
+ sign scaffold
+ operator placement
```

This is better modeled as a constrained directed/fibered system than as a flat symbolic table.

A useful abstract object:

```text
Stages S = {Se, Ne, Ni, Si}
Directed cycles C_D = Se -> Ne -> Ni -> Si and C_I = Se -> Si -> Ni -> Ne
Engine sheets E = {Type1, Type2}
Loops L = {outer, inner}
Readout R(E, L, stage) -> WIN/LOSE/win/lose component
Operator placement O selects the unique valid paired table under constraints.
```

## Carnot/Szilard dual stack

Carnot supplies ordered thermodynamic legality:

```text
directed stroke cycle / open-closed / expansion-compression / no-free-work order
```

Szilard supplies measurement-memory-feedback legality at each stroke:

```text
probe -> measurement -> memory write -> feedback update -> reset / Landauer accounting
```

The dual-stack engine target is therefore:

```text
same finite QIT carrier
+ Carnot stroke order
+ Szilard readout/memory layer
+ IGT loop-selected WIN/LOSE readout
+ noncommuting D∘I vs I∘D order witness
```

## Relation to Axis 0-6

The pattern is a candidate source of the axis/readout schedule rather than a decoration placed after the fact.

Current safe mapping pressure:

```text
Axis0 = feedback polarity / shell-cut / response readout
Axis1 = open vs closed / expansion-compression legality
Axis2 = bath/chart/frame lens
Axis3 = inner/fiber vs outer/base loop readout
Axis4 = deductive vs inductive order
Axis5 = gradient vs spectral generator class
Axis6 = operator/terrain precedence
```

This does not admit final Axis0 or final QIT-engine status.

## Relation to I Ching

Owner correction: I Ching convergence was not meant to be forced.

Safe direction:

```text
two-engine pattern + axes + signed operators + QIT schedule
-> emergent 64-structure candidate
-> compare against I Ching / taijitu mapping
```

Unsafe direction:

```text
I Ching premise
-> force the engine into hexagram structure
```

The I Ching layer remains a downstream comparison/emergence test, not a premise.

## Claim ceiling

This page supports:

```text
finite pattern encoding
source/provenance routing
sim-result intake
future encoding targets
```

It does not support:

```text
final M(C)
canonical QIT engine
physics admission
I Ching proof
Axis0 closure
consciousness claim
```

## Next encoding targets

Encode the same pattern as:

1. finite CSP / model-count proof;
2. directed two-cycle automaton;
3. paired two-engine chart;
4. signed operator-placement table;
5. QIT channel/order schedule;
6. 64-state schedule candidate;
7. downstream I Ching comparison only after the 64-structure emerges.
