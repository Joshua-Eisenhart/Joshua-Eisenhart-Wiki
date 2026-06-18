---
title: Leviathan Current Read First
created: 2026-06-17
updated: 2026-06-18
type: read-first
status: active scaffold
claim_ceiling: routing note; not full conceptual synthesis
---

# Read First — Leviathan Current

## Why this project exists

Josh needs a wiki that can understand current Leviathan: what it is, what it can do, what it intends to do, what it could do, and how much of Josh's constraint doctrine is inside it.

This project exists because the repo is high-entropy: thousands of docs/code files, active submodules, source chats/transcripts, older LevOS/Leviathan material, and architecture that is partly ahead of implementation.

## First working definition

Observed from the current repo docs, Lev / Leviathan is a universal agent-human runtime. It turns intent into constrained, routed, auditable execution across surfaces.

Plain version:

```text
Lev is not just chat. It is a runtime where agents act through surfaces, under policy, with graph memory, receipts, leases, and event traces.
```

Current repo docs keep these planes separate:

- **FlowMind** — control and policy declarations.
- **Orchestration** — scheduling, worker coordination, execution strategy.
- **Graph** — state, knowledge, memory, traversal, lineage.
- **Event Bus** — canonical `LevEvent` spine, replay, audit.
- **Exec / Poly / Daemon** — execution SDK, bindings, process/runtime surfaces.
- **AgentPing** — human-loop surfaces.
- **AgentLease** — scoped authority and accountability, still partly product/roadmap depending on surface.

## The Josh / JP boundary

- Josh / Joshua Eisenhart: Codex Ratchet dev; supplied or shaped root constraints and the broader constraint-admissibility frame.
- JP Smith: Lev / LevOS developer; owns the Leviathan repo and runtime implementation lane.
- Leviathan contains many Josh ideas, but repo-current Lev is not the same object as Codex Ratchet.

Safe bridge statement:

```text
Codex Ratchet works on the mathematical/proof/admissibility kernel. Leviathan applies related constraint structure as a running agent-human runtime.
```

Do not collapse one into the other. Use the bridge as a map, not as proof.

## Constraint map

The wiki bridge currently maps Lev's five listed kernel constraints to two roots plus derived consequences:

- `C1 Finitude` ↔ `F01` root.
- `C2 Non-commutation` ↔ `N01` root.
- `C3 Nominalized reality` — derived from finitude / nominalist doctrine.
- `C4 Ratchet` — derived from finitude + non-commutation.
- `C5 Locality` — derived from finitude / probe-relative scope.

Use this map as doctrine alignment, not as implementation proof. For repo truth, read current Lev docs and code.

## Source mode for future agents

The persistent local checkout was deleted on 2026-06-18 at Josh's request after the Hermes lane mutated the repo while trying to build this wiki. Future Leviathan wiki work should read the live GitHub website/remote as the current source:

- Website front door: `https://github.com/lev-os/leviathan`
- Raw current files: `https://raw.githubusercontent.com/lev-os/leviathan/main/<path>`
- Stable snapshot files: `https://raw.githubusercontent.com/lev-os/leviathan/<commit>/<path>`
- Contents/tree API when a machine-readable listing is needed: `https://api.github.com/repos/lev-os/leviathan/contents/<path>?ref=main`

If the website/raw/API route is too limited for the wiki task, Josh has authorized downloading Leviathan again as a clean fresh clone. Prefer a disposable clone under `/tmp` for bounded scans. If a persistent checkout is needed, clone fresh from `https://github.com/lev-os/leviathan.git`; do not recover or reuse the damaged deleted checkout. Record the remote URL, commit SHA, and clean status before using the clone as evidence, and keep wiki work read-only unless Josh explicitly assigns a repo patch task.

Old pages in this folder may cite `/Users/joshuaeisenhart/GitHub/leviathan/...`; treat those as historical snapshot citations from the June 17-18 local inventory, not as instructions that the path still exists.

Remote `main` observed on 2026-06-18: `c90ec8499c83db3d17f6132ec734698a8de2dbce`.

## Read order for future agents

1. This file.
2. `README.md` in this folder.
3. `https://github.com/lev-os/leviathan` for the live repo front door and current README.
4. `https://raw.githubusercontent.com/lev-os/leviathan/main/docs/README.md`.
5. `https://raw.githubusercontent.com/lev-os/leviathan/main/docs/specs/README.md`.
6. `https://raw.githubusercontent.com/lev-os/leviathan/main/docs/ARCHITECTURE.md`.
7. `https://raw.githubusercontent.com/lev-os/leviathan/main/docs/VISION.md`.
8. `https://raw.githubusercontent.com/lev-os/leviathan/main/mvp.md`.
9. `https://raw.githubusercontent.com/lev-os/leviathan/main/docs/ROADMAP.md`.
10. `https://raw.githubusercontent.com/lev-os/leviathan/main/docs/NORTH_STAR.md`.
11. `https://raw.githubusercontent.com/lev-os/leviathan/main/AGENTS.md` for agent/contributor operating rules, not product truth.
12. [[projects/leviathan-current/deep-audit-current-snapshot-2026-06-18]].
13. [[projects/leviathan-current/repo-current-vs-wiki-drift-audit-2026-06-18]].
14. [[projects/leviathan-current/concept-atlas-current-2026-06-18]].
15. [[projects/leviathan-current/evidence-frontier-and-blockers-dashboard-2026-06-18]].
16. [[projects/leviathan-current/proof-audit-roadmap-vs-mvp-2026-06-18]].
17. [[projects/leviathan-current/read-order-by-intent-2026-06-18]].
18. `source-inventory-2026-06-17.md` here as a historical local snapshot.
19. `bounded-ingestion-plan.md` here.
20. Existing `projects/levos/*.md` pages for prior idea intake.
21. Chat/transcript candidates only after provenance classification.

## Current status

- Historical local repo checked at `/Users/joshuaeisenhart/GitHub/leviathan` during the first inventory, then deleted on 2026-06-18 by direct user request.
- Current source for new wiki work: `https://github.com/lev-os/leviathan` plus raw/API URLs.
- HEAD checked during initial local inventory: `a661ecbf410469becd7b89c3bfc5ee215721ae34`.
- Remote `main` checked on 2026-06-18 after local deletion: `c90ec8499c83db3d17f6132ec734698a8de2dbce`.
- Dirty local worktree observed before deletion: submodule changes and deleted `docs/vernacular.md`. Treat that as a historical damaged-checkout observation, not current upstream truth.
- First inventory written: `source-inventory-2026-06-17.md` plus JSON sidecar.
- Scope correction on 2026-06-18: this Hermes lane is wiki-only. Read the repo; do not edit it. Use `wiki-swarm-launch-receipt-2026-06-18.md` for the Packet 2/4/5 worker ledger.
- Packet 3/4/5 update on 2026-06-18: product-surface pages for AgentPing/AgentLease, constraint-boundary pages, and a chat-evidence promotion protocol now exist. They are candidate/controller-verified for structure and source-path grounding, not runtime proof.
- OpenRouter Fusion and GLM 5.2 have an advisory pressure memo at `model-pressure/fusion-glm-wiki-direction-2026-06-18.md`; verify source paths before promoting any claim.
- Current clean-snapshot reset page: [[projects/leviathan-current/deep-audit-current-snapshot-2026-06-18]].
- Current-vs-historical drift page: [[projects/leviathan-current/repo-current-vs-wiki-drift-audit-2026-06-18]].
- Current concept atlas: [[projects/leviathan-current/concept-atlas-current-2026-06-18]].
- Current evidence frontier: [[projects/leviathan-current/evidence-frontier-and-blockers-dashboard-2026-06-18]].
- Current clean-clone proof audit: [[projects/leviathan-current/proof-audit-roadmap-vs-mvp-2026-06-18]].
- Current proof-audit receipt: [[projects/leviathan-current/packet-7-clean-clone-proof-audit-receipt-2026-06-18]].
- Current Wizard mass-swarm receipt: [[projects/leviathan-current/packet-8-wizard-mass-swarm-receipt-2026-06-18]].
- Current stale external report intake: [[projects/leviathan-current/packet-9-external-upgrade-report-intake-2026-06-18]].
- Current read-order guide: [[projects/leviathan-current/read-order-by-intent-2026-06-18]].
- Important correction: old Packet 2 pages that say current Event Bus/build/TUI conflict markers block runtime health are now historical damaged-checkout findings. The clean snapshot at `c90ec8499c83db3d17f6132ec734698a8de2dbce` has no `<<<<<<<`/`>>>>>>>` scan hits. Runtime health is now mixed rather than untested: Packet 7 ran bounded install/build/test/gate commands in a disposable proof clone.
- Important correction: `docs/ROADMAP.md` and `mvp.md` disagree about S5/Pentagon/security/default-daemon gate status. Packet 7 reran the minimal clean-clone proof checks and found a split verdict: high audit and named SDK/Poly Pentagon pass, but default daemon Pentagon gate and `@lev-os/testing` are not green in that run.

## Do not

- Do not treat chat transcripts as implementation proof.
- Do not treat old LevOS product pages as current repo truth.
- Do not assume `/Users/joshuaeisenhart/GitHub/leviathan` exists.
- Do not recover the deleted damaged checkout or mutate a fresh clone while doing wiki work.
- Do not say `implemented`, `enterprise-ready`, or `canonical` unless current docs/code/tests earn that exact rung.
- Do not flatten Josh's root constraints into generic startup/product language.
- Do not flatten JP's runtime implementation work into Codex Ratchet math/proof work.
