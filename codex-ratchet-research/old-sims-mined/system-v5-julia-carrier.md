# System v5 Julia Carrier Mine

## 1. Scope and Evidence Boundary

This file mines only the requested old-estate surfaces:

- `system_v5/julia_carrier/layers/`
- `system_v5/julia_carrier/artifacts/`

The `layers/` directory exists but contains no files. No layer implementation file was inspectable under the requested layer path, so this corpus does not claim direct layer-tower implementation evidence from that directory.

The old artifact surface contains one inspected file:

- `system_v5/julia_carrier/artifacts/algebra_structure_constants_v1.json`

V6 receipts were read only for convention, lineage, and boundary comparison:

- `system_v6/receipts/sedenion_witness_convention_20260610.md`
- `system_v6/receipts/canon_algebra_artifact_v1_results_20260610.json`
- `system_v6/receipts/estate_convention_ledger_20260610.md`
- `system_v6/receipts/estate_lineage_remediation_20260610.md`
- `system_v6/receipts/octonion_orientation_reconciliation_20260610.md`
- `system_v6/receipts/nonassoc_math_map_20260609.md`

Counts:

- Layer files inspected: 0.
- Artifact files inspected: 1.
- Convention divergences found: 2 actual cross-packet divergences, plus 3 guard rows.
- Unconsumed objects found: 8.

Boundary: this is a mine, not a roadmap. Nothing here promotes an old result to canonical status, formal admission, or a v6 packet claim. The admissible use is: tested labels, convention guards, exclusion tests, and candidate queues for future receipts.

## 2. Standard-Math Facts Mined

The artifact is a versioned structure-constant table for two algebras:

- Quaternion table: dimension 4, basis `1,i,j,k`, shape `4x4x4`, bracket convention `left`.
- Octonion table: dimension 8, basis `1,e1,e2,e3,e4,e5,e6,e7`, shape `8x8x8`, bracket convention `left`.

The artifact says the tables are derived from Julia packages:

- Quaternion table: `Quaternions.jl` basis products read from `Quaternion(s,v1,v2,v3)`.
- Octonion table: `Octonions.jl` basis products read from `Octonion(s,v1,v2,v3,v4,v5,v6,v7)`.

The finite Z3 proof rows support these bounded facts for the declared tables:

- Quaternion closure: 16 basis products, 64 bound structure constants, `sat`.
- Octonion closure: 64 basis products, 512 bound structure constants, `sat`.
- Quaternion noncommutativity has a basis witness: `i,j` with `ij - ji = 2k` in the declared coordinate convention.
- Octonion noncommutativity has a basis witness: `e1,e2` with `ij - ji` supported in the `e3` coordinate.
- Quaternion has no nonzero basis associator in the checked basis triples: 64 triples, `unsat` for existence of a nonzero basis associator.
- Octonion has a nonzero basis associator witness: basis labels `e1,e2,e4`, associator components `[0,0,0,0,0,-2,0,0]`.
- Octonion left-alternative, right-alternative, and flexible violation searches are `unsat` over the finite coefficient rows checked. This excludes those violation rows for this table; it does not admit downstream carrier claims by itself.

Useful standard-math extraction:

- `H` is a noncommutative but associative control. This blocks the lazy inference "noncommutative implies nonassociative."
- `O` is a disciplined nonassociative control: noncommutative, nonassociative, alternative, and flexible under the table/proof convention.
- The associator is a three-input observable. Two-input products can show noncommutativity, but the bracketing split needs triples.
- Structure constants are probe data, not a global identity. The basis order, orientation map, and bracket convention travel with every consumer.

## 3. Layer Tower Implementation Lessons

No `system_v5/julia_carrier/layers/` files were available, so direct layer-tower implementation lessons from that path are absent.

Supported lessons from the artifact and v6 convention receipts:

- Keep the algebra table as a data artifact with a proof tag. The table has `table_version=algebra_structure_constants_v1`, `proof_pass=true`, and `proof_tag=sha256:a9470fc299d39917a791bba0144d3e526866ad217b90fac1a6622b25d2c4652a`.
- Keep a consumer-facing receipt separate from the old artifact. The v6 receipt retargets the old artifact into `system_v6/receipts/canon_algebra_artifact_v1_results_20260610.json` with classification `scratch_diagnostic`, `promotion_allowed=false`, and `formal_admission_allowed=false`.
- Do not let the generator path become uninspected authority. The artifact names `system_v5/julia_carrier/canon_algebra_artifact_v1.jl` as source, but that source file is outside the requested old-estate read scope for this mine.
- Treat convention fields as load-bearing inputs. `bracket_convention=left` is present in both the artifact and v6 receipt; consumers still need to carry it explicitly.
- Store closure and identity checks as reusable finite proof rows. A downstream claim should point to the exact function of the table it consumes, such as closure, noncommutativity, no quaternion associator, or an octonion associator witness.
- Do not use a witness spelling without its convention. The sedenion receipt shows that the same displayed pair can be zero or nonzero when the parent table / basis order changes.

## 4. Canon Algebra Artifact Lineage

Old artifact:

- Path: `system_v5/julia_carrier/artifacts/algebra_structure_constants_v1.json`
- Schema/table version: `algebra_structure_constants_v1`
- Proof pass: `true`
- Proof tag: `sha256:a9470fc299d39917a791bba0144d3e526866ad217b90fac1a6622b25d2c4652a`
- Bracket convention: `left`
- Artifact source path recorded in JSON: `/Users/joshuaeisenhart/Codex-Ratchet/system_v5/julia_carrier/canon_algebra_artifact_v1.jl`
- Source hash recorded in JSON: `029907bc4729cac16a69579a5a1291674adb25f18582e65ad48d5bae48b10a09`

V6 receipt lineage:

- Commit-visible receipt: `system_v6/receipts/canon_algebra_artifact_v1_results_20260610.json`
- Object id: `canon_algebra_artifact_v1`
- Classification: `scratch_diagnostic`
- Claim ceiling: `scratch_diagnostic only; promotion_allowed=false; formal_admission_allowed=false`
- Artifact path: `/Users/joshuaeisenhart/Codex-Ratchet/system_v5/julia_carrier/artifacts/algebra_structure_constants_v1.json`
- Artifact hash: `824a0a2c794a949a83e4bd650c9620464b96eb0d1dcb3d0fe4901a4e86d05f2c`
- Generator hash: recorded by remediation as `029907bc4729cac16a69579a5a1291674adb25f18582e65ad48d5bae48b10a09`
- Remediation note: the ignored legacy result-estate path was retargeted to the commit-visible v6 receipt.

Tool integration lineage in the v6 receipt:

- Load-bearing: `Octonions`, `Quaternions`, `Z3`.
- Supportive: `JSON`, `JSON3`, `SHA`.
- `LinearAlgebra`: `None`.

Do not read `proof_pass=true` as canonical promotion. The v6 receipt explicitly says no three-engine envelope, no JAX/PyTorch consumer implementation, and no formal admission beyond this pinned data artifact receipt.

## 5. Conventions Divergence Table

| Old convention | V6 pin if found | Risk | Action |
| --- | --- | --- | --- |
| Artifact octonion parent table uses basis `1,e1,e2,e3,e4,e5,e6,e7` from `Octonions.jl`, bracket `left`. | Bloch packet convention doubles the canon artifact octonion table; S9 convention rebuilds the sedenion table from `R -> C -> H -> O -> S` in packet basis order. | Actual divergence: `(e1+e10)(e4+e13)` is zero in the Bloch convention but nonzero in the S9 convention; `(e1+e10)(e5+e14)` flips the other way. Universal zero-divisor spellings are killed. | Pin doubling rule and parent basis/order for every sedenion witness. Use invariant language: sedenion norm/fiber-law failure, not universal index spelling. |
| Old artifact orientation is a local octonion table convention. | Bloch old-to-new map is `[0,3,2,1,6,7,4,5]` with signs `[1,-1,1,1,-1,-1,1,-1]`; MCT weld basis lift is `perm=[0,1,2,3,4,7,6,5]`, signs `[1,1,1,1,1,-1,1,-1]`. | Actual divergence: packet-local maps are distinct. A consumer that compares products across packets without a map can manufacture or erase agreement. | Carry map name, signs, and lift rule before any cross-packet comparison. No cross-packet orientation reuse. |
| Artifact carries `bracket_convention=left`. | Canon receipt also pins `bracket_convention=left`; MCT weld receipt also reports `left`. | Guard row, not a mismatch. Risk is omission: downstream code can silently use the table under a different bracketing convention. | Carry `bracket_convention` as a required field in consumers and receipts. |
| Artifact contains quaternion and octonion tables only. | Sedenion witness rows are recomputed by Cayley-Dickson doubling, not read as native artifact rows. | Guard row. Treating the artifact as a sedenion table hides the derived parent-table dependency. | Label sedenion products as derived from a named parent table and doubling rule. |
| Artifact has `proof_pass=true`. | V6 receipt pins `classification=scratch_diagnostic`, `promotion_allowed=false`, `formal_admission_allowed=false`. | Guard row. Proof pass can be mistaken for canon admission. | Use as a pinned data/proof source only; require separate consumer receipts for downstream claims. |

## 6. Unconsumed Objects Queue

1. Full sedenion zero-divisor inventory / 84-pair graph.
   Why: v6 convention receipt supports witness instability across conventions; the nonassoc map says current receipts show witnesses and PG pressure, not full classification.
   Boundary: graveyard/control evidence only; no carrier promotion.

2. Octonion associator as 3-cell or cocycle fixture.
   Why: the artifact gives a concrete basis associator witness `e1,e2,e4 -> -2e5`.
   Boundary: may exclude bracketing-erasure controls; does not by itself assert topology or emergence.

3. Malcev / Akivis tangent probe from octonion commutator plus associator constants.
   Why: the artifact has finite commutator and associator data, and the nonassoc map marks Malcev/Akivis as ready but unimplemented.
   Boundary: tangent identity probe only; no global physics admission.

4. Split-octonion / split-`G2(2)` discriminator.
   Why: current compact octonion table is not enough to collapse compact/split alternatives.
   Boundary: needs separate split multiplication/signature convention and compact-vs-split controls.

5. Nucleus and associator-ideal harness.
   Why: binary pass/fail on associativity leaves the location of bracketing defects unmined.
   Boundary: finite table analysis only; keep algebra-local.

6. Associahedron/free-magma bracketing harness.
   Why: the artifact exposes a triple associator, but there is no reusable arity-4/5 bracketing-space generator in this mine.
   Boundary: grammar/harness object, not an independent math claim.

7. Same-carrier `M(C)` bracketing field.
   Why: current receipts keep bracketing and `M(C)` profile separated; integration would test whether associator changes the admissibility object or only a readout.
   Boundary: future packet must carry controls and receipts; no promotion from old artifact.

8. Quaternion-as-control consumer gate.
   Why: `H` is noncommutative but associative, a useful kill-control for root-only nonassoc overclaims.
   Boundary: control row only; does not choose the carrier.

## 7. Negative / Killed Candidates if Present

- Universal sedenion zero-divisor spelling: killed. The v6 convention receipt shows convention-dependent witness spellings. Future text must pin doubling rule and parent basis/order.
- Cross-packet octonion orientation reuse: killed. The Bloch and MCT maps are distinct and packet-local.
- `proof_pass=true` as canonical admission: killed. The v6 canon receipt pins the artifact as `scratch_diagnostic` with promotion and formal admission blocked.
- Quaternion nonassociativity: killed for the inspected table. The Z3 row reports no nonzero basis associator across 64 basis triples.
- "Layer tower implementation inspected from `layers/`": killed for this mine. The requested layer directory had zero files.

## 8. Source Index

Read-first and corpus authority:

- `AGENTS.md`
- `/Users/joshuaeisenhart/wiki/codex-ratchet-research/README.md`

Old estate scope:

- `system_v5/julia_carrier/layers/` - exists, zero files.
- `system_v5/julia_carrier/artifacts/algebra_structure_constants_v1.json`

V6 convention and lineage comparison:

- `system_v6/receipts/sedenion_witness_convention_20260610.md`
- `system_v6/receipts/canon_algebra_artifact_v1_results_20260610.json`
- `system_v6/receipts/estate_convention_ledger_20260610.md`
- `system_v6/receipts/estate_lineage_remediation_20260610.md`
- `system_v6/receipts/octonion_orientation_reconciliation_20260610.md`
- `system_v6/receipts/nonassoc_math_map_20260609.md`
