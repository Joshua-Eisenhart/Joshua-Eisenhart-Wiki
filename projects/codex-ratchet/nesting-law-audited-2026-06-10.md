# Nesting law — audited receipt router

Status: project routing note / receipt index.  
Written: 2026-06-10, after S1 foundation closeout.  
Repo anchor: `/Users/joshuaeisenhart/Codex-Ratchet/system_v6/receipts/nesting_law_audited_20260610.md`, commit `6499eb470`.  
Claim ceiling: routing and math-correction receipt only; no `M(C)`, carrier admission, physics, QIT-engine, or geometry-complete claim.

## What this routes to

The committed repo receipt is the current companion to [[projects/codex-ratchet/geometry-sim-program-canonical-2026-06-10]]. It records the audited nesting-law corrections that future S1/S2/S3 workers must not lose.

Core corrections:

```text
noncommutation is the weak root binary order condition:
  AB != BA

anticommutation is a sharpened signed binary condition only when nonzero:
  AB + BA = 0 AND AB != 0

nonassociativity is the root ternary order condition:
  [a,b,c] = (ab)c - a(bc) != 0

the octonion sharpened ternary path is the alternating associator / alternativity,
not global anti-associativity.
```

Global anti-associativity:

```text
(ab)c = -a(bc)
```

is kept only as a designed-to-fail negative-control branch for unital/octonion paths.

## Thirteen nesting types

The receipt distinguishes heterogeneous arrow types. Do not collapse them into one generic `nested` relation.

```text
1. subset / submanifold
2. quotient
3. covering-space / group quotient
4. principal bundle / fibration
5. convex extension / boundary inclusion
6. foliation
7. dynamical / flow
8. tensor
9. algebra extension
10. group action / orbit
11. refinement / limit
12. preservation group
13. filtration
```

Example chain:

```text
C^2 ⊃ S^3 -> S^2 ⊂ B^3
```

uses multiple arrow types:

```text
submanifold / normalization
Hopf quotient / bundle
boundary inclusion into convex channel body
```

## Four sim modes and one cross-cutting test family

The four modes remain:

```text
FREE
RESTRICTED / STACKED
QUOTIENTED
RATCHETED
```

Order/bracket pressure is not a fifth mode. It is a cross-cutting test family that can run inside any mode:

```text
[A,B]x
AB + BA with AB != 0
[a,b,c]
alternating-associator rows
anti-associativity negative-control rows
```

## Ratchet measure caveat

The naive conditioned-measure update:

```math
\mu_{t+1}(E)=\frac{\mu_t(E\cap G_{t+1})}{\mu_t(G_{t+1})}
```

is valid only when:

```math
\mu_t(G_{t+1})>0.
```

If the survivor set is lower-dimensional or measure-zero in the ambient geometry — for example a shell `T_eta` inside `S^3` — the receipt must use induced / disintegrated / coarea surface measure instead of dividing by zero. Every ratchet receipt must state which case it uses.

## Use rule

Load this note when working on:

- geometry sim modes;
- S2 connection/curvature/flux/foliation cards;
- ratcheted-mode cards;
- noncommutation / anticommutation / nonassociativity ladder claims;
- Bloch/density quotient erasure claims;
- finite quotient / lens tower work.

This page is a router. For exact evidence, read the repo receipt and current committed sim folders.
