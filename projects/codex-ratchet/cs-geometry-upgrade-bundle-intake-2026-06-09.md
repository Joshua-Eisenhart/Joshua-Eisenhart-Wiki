---
title: CS Geometry Upgrade Bundle Intake 2026-06-09
created: 2026-06-09
type: project-intake
status: active-router
claim_ceiling: source/design scaffold only; no Codex repo adoption, no sim admission, no canonical status, no physics/bridge promotion
framing: codex-ratchet
---

# CS Geometry Upgrade Bundle Intake 2026-06-09

## Source artifact

User-provided local zip:

```text
/Users/joshuaeisenhart/Desktop/codex_ratchet_cs_geometry_upgrade_bundle_v1_2026-06-09.zip
```

Hermes processed it because the chat attachment layer could not read binary zip files.

Observed archive facts:

```text
zip_sha256: 922deb11ebdb9b5a6fa01509d899660d6ebf9d6c3c906e7f8e64c209041ee97d
zip_bytes: 41928
zip_entries: 55
uncompressed_bytes: 71603
path_traversal_entries: 0
```

Extracted temp path:

```text
/tmp/codex_ratchet_cs_geometry_upgrade_bundle_v1_2026-06-09/build_codex_ratchet_cs_geometry_v1
```

Durable raw wiki copy:

```text
/Users/joshuaeisenhart/wiki/raw/articles/new-docs/codex-ratchet-cs-geometry-upgrade-bundle-v1-2026-06-09
```

Inventory:

```text
/Users/joshuaeisenhart/wiki/raw/articles/new-docs/codex-ratchet-cs-geometry-upgrade-bundle-v1-2026-06-09/_hermes_source_inventory.json
```

## What the bundle is

The bundle is a **Codex-Ratchet design/scaffold packet**, not a repo patch and not sim evidence.

Its main claim is that a missing discrete math / CS layer should sit between finite carriers and physics-facing language:

```text
finite carrier
-> graph / hypergraph / rewrite representation
-> multiway or causal event graph
-> topology / quotient / basin readouts
-> GNN / AI only after the graph object is explicit
```

That fits the current Codex Ratchet frame if treated as a routing/probe queue under the `M(C)` gate.

Safe import target:

```text
source/router + queue material for CS-layer tool-class mapping and micro-probes
```

Unsafe import target:

```text
direct authority replacement
repo-wide patch
admitted geometry
physics/Axis0/bridge promotion
canonical tool stack
```

## Contents read

Hermes inventoried and read the 55 extracted files:

- `README_SEND_FIRST.md`, `IMPLEMENTATION_STATUS.md`, `AUDIT_REPORT_CODEX_ONLY_V1.md`.
- 13 docs under `docs/`, including build order, CS layer curriculum, `M(C)` gap table, three-engine agent fabric, same-carrier micro-lego plan, no-promotion geometry tower, NumPy contamination policy, current-edge library backlog, and issue queue.
- 6 example agent skill cards.
- 6 issue stubs.
- 6 local test output files.
- 6 manifest/catalog files.
- 4 JSON schemas.
- 10 scripts, including local smokes, support probes, and NumPy contamination scanner.
- 1 source note: `source_notes/USER_CURRENT_GEOMETRY_STACK_AND_CS_LAYER.md`.

## Smoke / verification results

Checksum manifest:

```text
manifests/bundle_checksums.json checked 54 files
failures: 0
extra_not_in_manifest: 0
```

The manifest omits itself, so `54` checksum rows for `55` extracted files is expected.

Bundle local smokes with Codex sim-stack Python:

```text
/Users/joshuaeisenhart/.local/share/sim-stack/bin/python3 scripts/run_codex_local_smokes.py
passed: true
```

Smoke details:

- `codex_cs_curriculum_smoke.py`: ok, `12` classes, `10` queue rows.
- `current_edge_candidate_manifest_smoke.py`: ok, `20` libraries, required present.
- `codex_geometry_manifest_smoke.py`: passed, no failures.
- `library_sets_catalog_smoke.py`: passed, no failures.
- `mc_object_schema_smoke.py`: passed, no failures.
- `three_engine_agent_contract_smoke.py`: passed, no failures.

NumPy contamination scanner:

```text
whole bundle default scan: pass, findings=[]
examples/fixtures/bad_numpy_worker.py targeted scan: block, detects NumPy / NetworkX / np.asarray / np.array / .numpy() / pandas DataFrame
examples/fixtures/clean_worker.py targeted scan: pass
```

Important interpretation: the whole-bundle default scan does not mean no bad pattern exists anywhere; the bad fixture is intentionally present and is ignored as fixture/example material unless scanned directly.

Python support probe with canonical sim-stack Python:

- Present: `jax`, `diffrax`, `dynamiqs`, `netket`, `equinox`, `optax`, `optimistix`, `lineax`, `torch`, `torch_geometric`, `torchode`, `torchdiffeq`, `xitorch`, `cvxpylayers`, `z3`, `cvc5` Python module.
- Missing in that probe: `pytorch3d`, `graphology` Python module.
- `cvc5` executable was not found, even though the Python module is present.

Julia support probe:

```text
scripts/support_probe_julia.jl
```

This script is currently broken as a probe. It reports every package unavailable with:

```text
UndefVarError: `pkg` not defined in `Main`
```

Likely cause: dynamic import expression line:

```julia
@eval Main eval(Meta.parse("import $pkg"))
```

Do not use this Julia probe's package availability output as evidence until repaired. Use Codex Ratchet's existing strict runtime doctor / carrier-project checks instead.

## Useful material to ingest

1. **CS layer curriculum / tool-class map**
   - Graph theory, spectral graph theory, hypergraphs, graph rewriting, category theory for CS, automata/formal languages, e-graphs, combinatorial topology, DEC, causal sets/event structures, probabilistic graphical models/causal AI, GNNs.
   - Good as a missing middle layer between finite carrier and downstream physics-facing readouts.

2. **`M(C)` gap table scaffold**
   - Lists required fields: carrier state set, constraints, probes/readout family, quotient map, admissibility predicate, composition/bracketing, controls, update map, boundary/invariant/escape controls, receipt paths.
   - Good input for the already-selected next bounded packet: `M(C)` gap table hardening.

3. **Same-carrier geometry micro-lego queue**
   - First target remains Hopf fiber/base loop law or Weyl-on-Hopf chirality.
   - Requires one carrier, one geometry surface, one tool/function, one positive, one negative, one boundary, one result path, one demotion condition.

4. **Geometry tower visibility**
   - Preserves the same tower already reconciled in [[projects/codex-ratchet/octonion-g2-sedenion-carrier-geometry-audit-2026-06-08]]:
     `M(C)` gate -> `R/C/H/O/S` -> octonion carrier -> `Cl(6)` -> `G2` -> Fano -> `Spin(7)/G2/S7` -> `G2->SU3` fenced pressure -> sedenion/`PG(3,2)` graveyard.

5. **Current-edge library backlog**
   - Useful as a candidate menu only, not install order.
   - First-probe discipline is good: one library, one function/API, one tiny claim, one positive, one negative, one boundary, one demotion condition, one receipt.

6. **Contamination policy / scanner**
   - Useful scanner patterns for `.numpy()`, `np.asarray`, `np.array`, `pd.DataFrame`, NetworkX-as-canonical-state, and embedding-similarity-as-identity.
   - Needs Codex-native naming cleanup before live repo adoption because comments/docs still say `Lev` in several places.

## Issues / caveats before repo adoption

1. **Scope leakage:** the bundle says Codex-Ratchet-only, but several files still use Lev names:
   - schema `$id` values under `https://lev.dev/...` or `lev.*`;
   - schema titles like `Lev M(C) Finite Admissibility Object v0`;
   - agent examples mention `Lev-native stage labels`;
   - scripts mention `canonical Lev lanes` and `Lev sim-eval provider lane`;
   - provider IDs include `lev-sim-julia`, `lev-sim-jax`, `lev-sim-torch`, `lev-proof-solver`.

   Safe action: translate these to Codex Ratchet names or explicitly mark them as provenance before repo adoption.

2. **Broken Julia support probe:** `scripts/support_probe_julia.jl` should not be trusted until repaired.

3. **Support probe path:** running `python3 scripts/support_probe.py` used the default/system Python and gave many false missing-package results. Use `/Users/joshuaeisenhart/.local/share/sim-stack/bin/python3` for Codex Ratchet support probes.

4. **Candidate libraries are not install order:** `Catlab.jl`, `AlgebraicRewriting.jl`, `egglog`, `PGMax`, `Orbax`, etc. require support/recency audit + one-function probe before adoption.

5. **Schemas are design scaffolds:** the `M(C)` and geometry receipt schemas pass smoke tests, but they are not current repo authority and should not supersede existing validators without a migration packet.

## Routing decision

Do not apply this bundle directly to `/Users/joshuaeisenhart/Codex-Ratchet` yet.

Admit it into the wiki as:

```text
source/design scaffold + queue pressure for CS-layer/micro-probe work
```

Next safe repo-facing work should be one bounded packet:

```text
M(C) gap table hardening
```

Use this bundle's `docs/03_M_C_ADMISSIBILITY_OBJECT_GAP_TABLE.md` as a checklist, but fill it from current repo result receipts, especially:

- `M(C) v0` envelope;
- nonassoc root-vs-carrier discriminator;
- spinor holonomy variant;
- current octonion/G2/sedenion carrier-geometry audit;
- current Canon runtime contract fields.

## One-line handoff

The bundle is useful and internally smoke-clean as a design scaffold, but it must be translated and receipt-gated before repo adoption: keep the new CS/discrete-math layer, use the `M(C)` gap table and one-function tool-probe discipline, repair/ignore the Julia support probe, and do not let leftover Lev naming or candidate library menus become Codex authority.
