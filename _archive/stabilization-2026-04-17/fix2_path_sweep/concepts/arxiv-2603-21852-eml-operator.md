# arXiv:2603.21852 — EML: All Elementary Functions from a Single Binary Operator

Updated against the repo-side external-math mirror on 2026-04-14.

## Citation

- **Authors:** Andrzej Odrzywołek
- **Title:** All elementary functions from a single binary operator
- **arXiv ID:** 2603.21852 (v2)
- **Year:** 2026 (v1: 2026-03-23; v2: 2026-04-04)
- **URL:** https://arxiv.org/abs/2603.21852

## Core claims

- There exists a single binary operator — call it `eml` — such that, together with the constant `1`, the closure under composition contains the standard scientific-calculator repertoire (sin, cos, exp, ln, sqrt, +, -, *, /, and the constants e, pi, i).
- The operator is `eml(x, y) = exp(x) - ln(y)`.
- This is the continuous-math analogue of NAND/NOR functional completeness in Boolean logic: one gate generates the entire algebra.
- The construction was found by systematic exhaustive search over small binary-operator families, not derived from first principles.
- Applications demonstrated in the paper: symbolic regression via trainable binary trees optimized with Adam (i.e., `eml` as the sole hidden-layer primitive).

## Key mathematical objects

- **The operator**
  $$\mathrm{eml}(x, y) = e^{x} - \ln(y)$$
- **Generating set:** `{ eml, 1 }`.
- **Closure:** the set of expressions built by finite composition trees with leaves in `{1}` and internal nodes labeled `eml` — claimed to be dense in / equal to the elementary functions of one real (or complex) variable on appropriate domains.
- **Example reconstructions** (schematic, from the paper's constructions):
  - `exp(x) = eml(x, 1)` since `ln(1) = 0`.
  - Subtraction, then division, then ln and exp individually, then the trig/hyperbolic family via Euler-style identities, each as finite `eml`-trees over `{1}`.
- **Symbolic-regression layer:** parameterize a depth-`d` binary tree of `eml` nodes; train leaves / structural weights by gradient descent.

## How this relates to the five self-similar frameworks

Honest mapping — most connections are weak:

- **QIT Engine (physics shell):** No direct connection. `eml` is a statement about the free algebra over one elementary-function primitive, not about admissible geometric shells, distinguishability, or constraint manifolds. It does not touch F01/N01.
- **Scientific Method (epistemology):** Weak connection. The result is an *expressivity compression* claim: one primitive spans what we thought required many. This is structurally adjacent to the project's compression-to-density-matrix line, but the compression here is syntactic/operator-theoretic, not informational.
- **Holodeck (perception):** No connection.
- **IGT (behavior):** No connection.
- **Leviathan (civilization):** No connection.

The honest summary: this paper is a **tool-level result**, not a framework-level one. Its relevance to Codex Ratchet is as a *primitive-set candidate* for any sim that uses trainable symbolic-function trees.

## Relation to G-structure tower and constraint-admissibility

- `eml` does not live on any G-structure the project currently tracks. It is coordinate-dependent (exp and ln are chart-local on R_>0 and C\{0}) and has no obvious invariance group.
- The interesting admissibility question is inverted: *which* elementary functions remain representable by finite-depth `eml` trees under precision/domain constraints? That is a constraint-admissibility question the project's methodology can ask of any operator basis.
- `eml` could plausibly serve as a minimal-primitive baseline against which the project's favored primitives (Clifford rotor ops, TopoNetX gating, PyG message passing) are compared for expressivity-per-node. This is a **classical_baseline** role, not canonical.

## Open questions the paper does NOT answer

- No quantitative bound on tree depth needed to approximate a given target to tolerance epsilon — expressivity is shown, efficiency is not.
- No treatment of numerical conditioning (exp/ln amplify / compress wildly; finite-precision breakdown regions are unmapped).
- No invariance / symmetry structure — the basis is not adapted to any Lie group.
- No proof that `{eml, 1}` is minimal; no uniqueness claim for the operator.
- No extension to operator-valued / multi-variable geometry (vector fields, forms, connections).
- No connection to information-theoretic compression, entropy, or distinguishability — purely an algebraic/functional result.

## Related wiki pages

- [[sympy-symbolic-math-reference]] — sympy is the natural tool for verifying `eml`-tree identities symbolically.
- [[operator-math-explicit]] — broader operator catalog; `eml` would be a minimal-primitive entry.
- [[operator-algebras-and-representation]] — contrast: `eml` generates a *free composition algebra*, not a representation-theoretic one.
- [[compression-to-density-matrix-map]] — syntactic vs informational compression — `eml` is the former.
- [[research-index-compression-terms]] — index entry.
- [[lego-build-catalog]] — where a bounded `eml` primitive-basis baseline would register in the local lego program.

## Status for Codex Ratchet

- **Verdict:** Narrow but real result. Not a framework-level input. Useful as a *primitive-basis baseline* for symbolic-regression sims and as a counterpoint to structure-adapted bases (Clifford, e3nn, PyG).
- **Priority:** Low. Process as classical_baseline sim legos only if the symbolic-regression lane is activated. Does not unblock any current coupling / shell sim.

## Repo-side processing note

The repo manifest now routes this paper through `system_v5/new docs/EXTERNAL_MATH_EML_OPERATOR.md`.

That repo-side mirror adds one bounded planning detail not previously surfaced clearly in this wiki page:
- there is an 8-lego atomization plan for EML
- all eight proposed legos are explicitly `classical_baseline`
- the plan is still pending owner review / launch authorization

So the current honest state is:
- the paper is processed into the wiki and repo summary surfaces
- the atomization plan exists as a repo-side proposal
- the atomized EML legos do not yet count as landed sim work in the wiki
