last_updated: 2026-04-17T16:06:00-07:00

# Tier D — Boundary Admissibility UNSAT Certificates

Historical 2026-04-17 Tier D snapshot. Keep the downgrade/canonical-boundary note as provenance, but do not treat the live runner/gate wording below as current without a fresh repo/status preflight.

Historical status at 2026-04-17: in_progress
Historical gate at write time: GREEN by dated authority (`/Users/joshuaeisenhart/wiki/projects/codex-ratchet/tier_b.md`) for launch permission only; Tier D evidence itself was not a pass.
Historical runner at write time: live (`bash system_v5/ops/sim_runner.sh`).

## Historical state
- Tier B was green in the dated tier flow, so Tier D was considered authorized to run then. Current Tier D launch authority requires current repo/status preflight and current user authorization.
- Repo commit `1783afc9c4b5fa4dd11c5c844be3120d20ace665` downgraded D1 to `classical_baseline` because the probe used toy integer encodings rather than load-bearing boundary math.
- Repo commit `c135a4acc4ad0d3a263ceb5e06029c210378e949` downgraded D2-D4 to `classical_baseline` because they copied the D1 toy integer-encoding pattern and carried no actual math imports.
- Queue execution history still exists, but execution alone does not restore a higher label after the downgrade commits.

## Public label state
- `boundary_g_to_hopf_admissibility.py`: `classical_baseline` (repo downgrade `1783afc9c`)
- `boundary_hopf_to_weyl_admissibility.py`: `classical_baseline` (repo downgrade `c135a4acc`)
- `boundary_weyl_to_flux_admissibility.py`: `classical_baseline` (repo downgrade `c135a4acc`)
- `boundary_flux_to_pauli_admissibility.py`: `classical_baseline` (repo downgrade `c135a4acc`)

## Queue snapshot
- `ops/queue_tier_d.txt`: 0 pending / 4 DONE / 2 FAIL
- The current queue file is still useful as execution history, but the downgrade commits outrank any earlier canonical-style reading of those rows.

## Operational consequence
- No Tier D boundary artifact currently earns `canonical by process`.
- Tier D remains in progress until new boundary probes land with load-bearing math, runner evidence, and a later audit that re-earn public labels.

## Related commits
- `1783afc9c` — D1 downgrade after anti-toy / enforcement review
- `c135a4acc` — D2-D4 downgrade after same-pattern review
