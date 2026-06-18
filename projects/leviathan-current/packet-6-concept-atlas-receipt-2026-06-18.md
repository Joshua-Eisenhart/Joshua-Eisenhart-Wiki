---
title: Packet 6 Concept Atlas Receipt
created: 2026-06-18
updated: 2026-06-18
type: packet-receipt
status: active
source_snapshot: c90ec8499c83db3d17f6132ec734698a8de2dbce
claim_ceiling: worker/source/wiki receipt; not FULL Wizard proof, not test proof
---

# Packet 6 Concept Atlas Receipt

## Scope

Josh asked to keep going because Leviathan is a massive repo with many concepts to process.

This packet built a higher-level concept atlas and evidence frontier from the current clean source snapshot. It does not claim the wiki is complete.

Outputs:

- [[projects/leviathan-current/concept-atlas-current-2026-06-18]]
- [[projects/leviathan-current/evidence-frontier-and-blockers-dashboard-2026-06-18]]
- [[projects/leviathan-current/read-order-by-intent-2026-06-18]]
- this receipt

## Source Snapshot

- Repo: `https://github.com/lev-os/leviathan.git`
- Disposable clone: `/tmp/leviathan-wiki-src-20260618`
- Remote `main`: `c90ec8499c83db3d17f6132ec734698a8de2dbce`
- Clone `HEAD`: `c90ec8499c83db3d17f6132ec734698a8de2dbce`
- Latest commit subject observed: `Route eval harnesses through durable owners`
- Clone status: clean

No dependency install, build, typecheck, or test suite was run.

## v4.3 Object Guard

Object card:

- `/tmp/leviathan_concept_atlas_v43_object_card.json`
- Object statement hash: `6771b62931a3352ad8b22fc3b23d86ec61d695cd2685d7b86c7b36ca339d6d1f`

Validation:

```bash
python3 scripts/wizard_v4_3_object_preservation.py validate --input /tmp/leviathan_concept_atlas_v43_object_card.json --out /tmp/leviathan_concept_atlas_v43_validation.json
```
Result:

- `ok: true`
- `errors: []`
- warning: forbidden substitutions should explicitly block proxy or label replacement

The warning was preserved as a caution: this packet is a concept atlas/evidence frontier, not a proof that concept labels are safe to promote.

## Worker Lanes

Native Codex workers completed:

| Lane | Agent | Model | Result |
|---|---|---|---|
| FlowMind/control/policy | `019edc5b-4d01-7bb0-a258-53223ef0e7b1` | `gpt-5.5` | completed |
| Exec/runtime/event/daemon | `019edc5b-6340-70b1-9e41-2108c905f648` | `gpt-5.4` | completed |
| Graph/memory/world-model | `019edc5b-7ae6-7482-96d0-8c6dfd3e5b32` | `gpt-5.4-mini` | completed |
| Product/plugin reroute | `019edc5d-7dd3-77c3-ba0d-01c45902ac88` | `gpt-5.3-codex-spark` | completed |
| Information architecture/provenance | `019edc5b-af40-75d3-900b-b16d125643da` | `gpt-5.5` | completed |

Blocked/rerouted:

| Lane | Agent | Status |
|---|---|---|
| First product/plugin worker | `019edc5b-91af-77c1-a3e9-78af2f08fd67` | errored on context-window compaction; not counted as completed |

Claude Bridge:

- Not rerun in this packet because the previous packet hit authentication failure.
- No Claude result is counted here.

## Main Findings Accepted

Accepted into the wiki after controller source checks:

1. Four-plane technical boundary is safer than the README's three-plane public shorthand.
2. `docs/ROADMAP.md` and `mvp.md` conflict on S5/Pentagon/security/default-daemon gate status.
3. Current JS graph-ish package is `core/context-graph`; docs mentioning `core/graph/**` are stale unless fresh source changes prove otherwise.
4. `core/world-model` is source-backed but experimental/unwired for production claims in this packet.
5. `@lev-os/daemon-pentagon` exists in source, so "missing package" is stale as source-presence wording.
6. Product/plugin surfaces need posture labels: active, downstream, proposal, inconsistent, experimental, or contested.
7. `docs/specs/README.md` is still the normative spec router, but its count is stale.
8. `docs/_inbox/**` and `_archive/**` should be explicitly demoted by default.

## Local Inventories

Deterministic inventory sidecar:

- `/tmp/leviathan_concept_inventory_20260618.json`

Observed counts:

- `core` dirs: 42
- `plugins` dirs: 54
- `apps` dirs: 19
- `crates` dirs: 43
- `docs` Markdown files: 429
- `docs/_inbox` Markdown files: 115
- `_archive` Markdown files: 1037
- root `package.json` workspaces: 122
- `docs/specs/spec-*.md`: 84
- all Markdown under `docs/specs`: 217

Counts are inventory evidence only. They do not prove package health.

## Blockers Carried Forward

- Fresh proof rerun needed for `mvp.md` vs `docs/ROADMAP.md`.
- Build/typecheck/test health remains unproven.
- Submodules were not initialized.
- Plugin posture needs a full manifest/package/config reconciliation pass.
- No maintainer acceptance or source patch was requested or performed.

## Verification To Run After Edits

Run the wiki probe:

```bash
python3 /Users/joshuaeisenhart/wiki/tools/wiki_probe.py --wiki-root /Users/joshuaeisenhart/wiki --output /tmp/leviathan-current-wiki-probe-packet6-20260618.json
```
