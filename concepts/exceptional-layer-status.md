---
title: Exceptional layer status
created: 2026-07-19
updated: 2026-07-19
type: concept
tags: [algebra, mathematics, cartan, e6, quantum]
sources:
  - pack186/github_authority/system_v7/constraint_core/MODEL_LAYER_LEDGER.md
  - owner-pack-RATCHET_188 (AXES_7_12_AND_EXCEPTIONAL_FIELD_STATUS_188.md, EVERY_LAYER_EXPLICIT_MATH_AND_RUNTIME_188.md)
  - owner-pack-178-cumulative-thread-essence-v2 (70_PRIOR_CUMULATIVE_THREAD/model/08_ENTROPIC_GEOMETRY_FLUX_AND_EXCEPTIONAL_MATH.md)
  - manifold_layer_ledger_20260614.md (v7 G1-G6 companion ledger)
framing: current
status: research-note
---

# Exceptional layer status

Research-note tier. Every claim cites its source file. Status labels follow
`exists < runs < passes local rerun < canonical by process` — nothing below
reaches `canonical by process`. See [[concepts/entropic-geometry-one-object]]
for the entropy/geometry half of the same 178/08 source document.

## Cayley-Dickson ladder

Source: MODEL_LAYER_LEDGER.md (pack186 v7 ledger), Layer 0.5, lines 768-772,
marked "hypothetical lane." Object: `R(1) -> C(2) -> H(4) -> O(8) -> S(16)`,
each doubling "the shortest leap," each losing one property. Commutativity
dies at H ("order-level N01"); associativity dies at O ("grouping-level N01
= nonassociativity ratcheted"). Hurwitz `|xy|=|x||y|` holds R through O
(error ~1e-13), fails at S (error ~200).

A related source (08_ENTROPIC_GEOMETRY_FLUX_AND_EXCEPTIONAL_MATH.md, sec. 5)
gives `[L_a,R_b]x = -[a,x,b]` for octonions — commutator of left/right
multiplication equals the negative associator — framed as a "holonomy seed."
It states explicitly this order (nonassociativity-before-noncommutation) "is
a meaningful candidate," not settled: "it remains possible that ordinary
associative noncommuting structures suffice."

## Sedenion zero-divisor witness

MODEL_LAYER_LEDGER.md line 771: `(e1+e10)(e5+e14) = 0` — two nonzero
sedenion elements annihilate, so "the ratchet STOPS at O." Referenced again
at line 2368 (UP-112): "sedenions excluded by zero-divisors either way,"
independent of whether associativity is treated as forced or optional.

## Der(O)/G2 = 14, F4 = 52, E6 = 78

Two treatments, not fully reconciled. **Layer 0.5** (lines 771-772) reports
G2 = Aut(O), dimension 14, and is explicit this row carries the dimension
only — "the concrete G2 ACTION ... lives in Layer 0.8." **UP-108** (lines
2273-2289, 2026-07-08) answers the owner's question "so g2 ratchets to f4?
... not sure order" with "ANSWER (derived, not asserted)": order is
G2 -> F4 -> E6 -> E7 -> E8, each the symmetry of one more layer on the same
octonions.

| Group | Definition given | Dim | Status given |
|---|---|---|---|
| G2 | Aut(O) = Der(octonions) — carrier symmetry | 14 | DERIVED in-sim |
| F4 | Aut(H3(O)) = Der(Albert algebra) — observable-algebra symmetry | 52 | DERIVED in-sim |
| E6 | str(H3(O)) = Der + traceless L (26 found) — cubic-form symmetry | 78 | DERIVED in-sim |
| E7 | conformal / Freudenthal triple | 133 | CITED, magic square |
| E8 | full magic-square corner | 248 | CITED, magic square |

Derivation boundary stated directly: "g2/f4/e6 derived from the
octonion/Albert structure; e7/e8 cited from Freudenthal-Tits." A G2
derivation of O applied entrywise to a Hermitian 3x3 octonionic matrix is
itself an F4 derivation (Jordan-derivation defect 9.1e-15) — "the O -> H3(O)
ratchet and the G2 -> F4 ratchet are the SAME step." Pack 188
(AXES_7_12_AND_EXCEPTIONAL_FIELD_STATUS_188.md, line 30) states these three
numbers "were previously derived in-sim," consistent with but not a new
derivation of UP-108.

## H3(O) vs H4(O)

**UP-107** (lines 2261-2271): Hermitian octonionic n×n matrices satisfy the
Jordan identity only for n≤3 — defect ~1e-13 at n=2,3, ~6e2 at n=4. Framed as
independently forcing a 3-qubit floor "from a completely different direction
than tomography counting."

**Pack 188** (AXES_7_12_AND_EXCEPTIONAL_FIELD_STATUS_188.md lines 24-46;
EVERY_LAYER_EXPLICIT_MATH_AND_RUNTIME_188.md row 21): on the four Pack-188
engine channels, "all four three-engine H3(O) charts pass the Jordan identity
at 5.4e-16 to 7.4e-16," with exact agreement across chart overlaps — H3(O)
"charts glue" (a "surviving refinement"). By contrast "one direct four-engine
H4(O) chart fails at 1.20e-7" (listed under "excluded"). Both sources agree
the mechanism is nonassociativity breaking the Jordan identity past rank 3.
Pack 188 leaves open "a transition law that makes F4 load-bearing across
chart overlaps."

## G2 as "stacking symmetry" — hypothesis, not a result

The exact phrase is not verbatim in the source set. Closest: entropic-geometry
doc sec. 6 — "G2 is the automorphism group of the octonions and the
stabilizer of a generic positive three-form in seven dimensions... It is a
candidate for nested entropic geometry and bracket-sensitive flux." Sec. 7
explicitly refuses promotion: "dimension matching is insufficient... That
clustering is not derivation."

Layer 0.8 (lines 788-792, "hypothetical lane") exhibits a concrete G2 action
`phi=exp(0.3 D)` satisfying `phi(xy)=phi(x)phi(y)` to ~1e-16 on a finite
spinor network, leaving the network's bracketing gap invariant — read as "G2
is the symmetry group of the network coupling schedule." That is one network,
not a field-of-engines claim. UP-111 (lines 2340-2355) directly tests field-
level exceptional value and reports a negative: the 8-terrain field's
automorphism group is finite (order 4); single-engine Choi symmetry is
`so(4)`, dim 6 — "classical/quaternionic," not exceptional. Conclusion: "the
exceptional tower does not emerge for free at the field/upper-manifold
level." Both readings — candidate value (sec. 6, Layer 0.8) and explicit
field-level rebuttal (UP-111) — survive; the sources do not resolve them
against each other.

## G1-G6 license objects

Not present in MODEL_LAYER_LEDGER.md itself. That file (line 919) cross-
references a separate "L1-L15 + G1-G6 inventory," calling it "an INVENTORY
(a campaign tracking table, 'NOT a result')." The G1-G6 rows actually live in
a companion file found in the same pack sweep, `manifold_layer_ledger_
20260614.md` (DRAFT status), not in the file the task named:

| Row | Name | Definition given | Status |
|---|---|---|---|
| G1 | The G2 layer | (name only) | DEFERRED — needs 7D `W_A` + pinned 3-form `phi` + four tests |
| G2 | SU(3) as G2 substructure | `SU(3)=Stab_G2(u)`, `G2/SU(3)=S^6` | DEFERRED — G1 must license first |
| G3 | Spin(7) via Cayley form | needs the 8D extension | DEFERRED |
| G4 | Spin(8) triality | needs maps `8v->8s->8c->8v` | NAMED, NOT SCHEDULED |
| G5 | F4 = Aut(J3(O)) | needs the 27D Jordan target `J` | NAMED, NOT SCHEDULED |
| G6 | split G2(2) + sedenion zero-divisor boundary | controls for G1-G5 | NAMED, NOT SCHEDULED, not promoted |

All six carry ladder label `DEFERRED` or `NAMED, NOT SCHEDULED` — none
reaches `runs`. Stated directly: "No packet is permitted until each one's
explicit LICENSING OBJECT exists." These are permission gates for future
work, not exceptional-group results.

## Divergences to preserve

- G2's dimension (14) has three independent evidence pieces at different
  ceilings: a bare count (Layer 0.5), a re-derivation plus G2⊂F4 containment
  (UP-108), and a concrete group action (Layer 0.8). None is canonical.
- UP-112 (lines 2357-2377) states the H->O carrier lift is "an UNFORCED
  observable-side FORK," and "non-associativity is INSTALLED not forced" —
  alongside UP-107/UP-108's real computed numbers (14, 52, 78). The numbers
  are genuine; reaching the carrier that makes them relevant is not forced.
- G2 field-level value: candidate (sec. 6, Layer 0.8) vs. explicit negative
  (UP-111). Both stand.

## Open / unresolved

- No source here shows a concrete G2/F4/E6 action on the axes-7-12
  field-of-engines object; UP-111 found that level's symmetry is classical.
- Pack 188 names "a transition law that makes F4 load-bearing across chart
  overlaps" as open, not merely unstarted.
- G1-G6 each need a named prerequisite object (7D `W_A`+`phi` for G1; 8D
  extension for G3; triality maps for G4; 27D Jordan target for G5) that no
  read source reports as built.
- E7 (133) and E8 (248) are cited from the magic square, not derived — lower
  ceiling than G2/F4/E6.
- UP-113 (lines 2379-2399) reports every engine operation available (channel
  composition, Jordan product, Lie bracket) is associative or Jacobi-obeying,
  so none can generate genuinely octonionic (non-Jacobi, Moufang) structure —
  named as the precise missing mechanism, independent of the G1-G6 gates.
