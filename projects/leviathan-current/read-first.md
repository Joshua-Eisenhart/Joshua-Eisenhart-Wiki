---
title: Leviathan Current Read First
created: 2026-06-17
updated: 2026-06-19
type: read-first
status: current-source-router
claim_ceiling: routing note and source authority map; not build proof; not release certification
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
- Owner-correction addendum, 2026-06-19: [[projects/leviathan-current/packet-11-deeper-nuance-attribution-pack-intake-2026-06-19]], [[projects/leviathan-current/josh-jp-attribution-boundary-v2-2026-06-19]], and [[projects/leviathan-current/no-ratchet-from-leviathan-policy]] make the boundary sharper: Codex Ratchet is not derived from Leviathan; convergent Ratchet-side material should be treated as Josh-origin unless direct contrary evidence exists; the original Wizard idea is credited to JP Smith per Josh.

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

Remote `main` observed on 2026-06-19 after the next processing pass: `5dd98ac4ce7afeb9e4351787179c60208de6d23f`.

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
12. [[specs/leviathan-current/README]].
13. [[projects/leviathan-current/proof-backed-status-dashboard]].
14. [[projects/leviathan-current/nuanced-assessment-and-josh-provenance-2026-06-19]].
15. [[projects/leviathan-current/packet-11-deeper-nuance-attribution-pack-intake-2026-06-19]].
16. [[projects/leviathan-current/josh-jp-attribution-boundary-v2-2026-06-19]].
17. [[projects/leviathan-current/no-ratchet-from-leviathan-policy]].
18. [[projects/leviathan-current/packet-12-pasted-deep-research-truth-provenance-intake-2026-06-19]].
19. [[projects/leviathan-current/packet-13-pasted-fep-runtime-boundary-audit-intake-2026-06-19]] as pasted FEP/runtime-boundary audit intake; advisory only, not FEP implementation proof.

Leviathan/FEP split pages from the Packet 14 intake: [[projects/leviathan-current/packet-14-pasted-fep-atlas-and-leviathan-boundary-intake-2026-06-19]], [[projects/leviathan-current/lev-runtime-boundary-2026-06-19]], [[projects/leviathan-current/leviathan-fep-runtime-boundary-2026-06-19]], [[projects/leviathan-current/sophisticated-inference-and-leviathan-2026-06-19]], [[projects/leviathan-current/world-model-reconciler-fep-support-2026-06-19]], [[projects/leviathan-current/leviathan-claim-ceilings-2026-06-19]], [[projects/leviathan-current/leviathan-validation-experiments-backlog-2026-06-19]], and [[projects/leviathan-current/provenance-status-guardrails-2026-06-19]]. These are source synthesis and external-theory support only, not runtime proof.

20. [[projects/leviathan-current/codex-imports/v3-deep-repo-nuance-bundle-2026-06-19]] as branch-imported V3 bundle intake; source synthesis only, not runtime proof.
21. [[projects/leviathan-current/codex-imports/v4-cross-issues-deep-dive-2026-06-19]] as branch-imported V4 cross-issues intake; source synthesis only, not runtime proof.

V4 split pages start at [[projects/leviathan-current/operating-contract-vs-product-proof-2026-06-19]], [[projects/leviathan-current/docs-authority-vs-status-drift-v4-2026-06-19]], [[projects/leviathan-current/security-gate-stack-v4-2026-06-19]], [[projects/leviathan-current/surface-family-matrix-v4-2026-06-19]], and [[projects/leviathan-current/release-readiness-ladder-v4-2026-06-19]]; all are source synthesis only, not runtime proof.

22. [[projects/leviathan-current/codex-ratchet-vs-leviathan-boundary]].
23. [[projects/leviathan-current/current-state-and-roadmap]].
24. [[projects/leviathan-current/architecture-planes-and-ownership]].
25. [[projects/leviathan-current/contract-surface-map]].
26. [[projects/leviathan-current/deep-audit-current-snapshot-2026-06-18]] as the older clean-clone audit at `c90ec...`.
27. [[projects/leviathan-current/repo-current-vs-wiki-drift-audit-2026-06-18]].
28. [[projects/leviathan-current/concept-atlas-current-2026-06-18]].
29. [[projects/leviathan-current/evidence-frontier-and-blockers-dashboard-2026-06-18]].
30. [[projects/leviathan-current/proof-audit-roadmap-vs-mvp-2026-06-18]].
31. [[projects/leviathan-current/read-order-by-intent-2026-06-18]].
32. `source-inventory-2026-06-17.md` here as a historical local snapshot.
33. Chat/transcript candidates only after provenance classification.

## Current status

- Historical local repo checked at `/Users/joshuaeisenhart/GitHub/leviathan` during the first inventory, then deleted on 2026-06-18 by direct user request.
- Current source for new wiki work: `https://github.com/lev-os/leviathan` plus raw/API URLs.
- HEAD checked during initial local inventory: `a661ecbf410469becd7b89c3bfc5ee215721ae34`.
- Remote `main` checked on 2026-06-18 after local deletion: `c90ec8499c83db3d17f6132ec734698a8de2dbce`.
- Remote `main` checked on 2026-06-19 during Packet 10 intake: `b7bca2cdbed5862743395f7c0330e7d640132764`.
- Remote `main` checked on 2026-06-19 during the nuance/provenance pass: `5dd98ac4ce7afeb9e4351787179c60208de6d23f`.
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
- Current deep-research/ZIP upgrade-pack intake: [[projects/leviathan-current/packet-10-deep-research-upgrade-pack-intake-2026-06-19]].
- Current deeper nuance/attribution addendum intake: [[projects/leviathan-current/packet-11-deeper-nuance-attribution-pack-intake-2026-06-19]].
- Current pasted deep-research truth/provenance intake: [[projects/leviathan-current/packet-12-pasted-deep-research-truth-provenance-intake-2026-06-19]]. Advisory/pass-with-cautions only; reinforces runtime-first wording, incompleteness, and Josh/JP boundaries, while non-portable citations and public-only assumptions block direct promotion.
- Current pasted FEP/runtime-boundary audit intake: [[projects/leviathan-current/packet-13-pasted-fep-runtime-boundary-audit-intake-2026-06-19]]. Advisory/pass-with-cautions only; reinforces FEP as formal neighbor, not implementation proof.
- Current FEP atlas / Leviathan boundary split intake: [[projects/leviathan-current/packet-14-pasted-fep-atlas-and-leviathan-boundary-intake-2026-06-19]]. Advisory/pass-with-cautions only; routes FEP through the concept atlas and creates Leviathan-specific boundary pages without adding runtime proof.
- Current branch-imported V3 deep repo nuance bundle: [[projects/leviathan-current/codex-imports/v3-deep-repo-nuance-bundle-2026-06-19]]. It is source synthesis and split-planning material only; it does not add runtime proof or maintainer acceptance.
- Current branch-imported V4 cross-issues bundle: [[projects/leviathan-current/codex-imports/v4-cross-issues-deep-dive-2026-06-19]]. It is source synthesis and split-planning material only; it does not add runtime proof, product readiness, or maintainer acceptance.
- Current proof status dashboard: [[projects/leviathan-current/proof-backed-status-dashboard]].
- Current nuanced assessment / Josh provenance boundary: [[projects/leviathan-current/nuanced-assessment-and-josh-provenance-2026-06-19]].
- Current owner correction / attribution boundary: [[projects/leviathan-current/josh-jp-attribution-boundary-v2-2026-06-19]], [[projects/leviathan-current/no-ratchet-from-leviathan-policy]], and [[projects/leviathan-current/wizard-origin-provenance-note-2026-06-19]].
- Current specs mirror/router: [[specs/leviathan-current/README]].
- Current read-order guide: [[projects/leviathan-current/read-order-by-intent-2026-06-18]].
- Important correction: old Packet 2 pages that say current Event Bus/build/TUI conflict markers block runtime health are now historical damaged-checkout findings. The clean snapshot at `c90ec8499c83db3d17f6132ec734698a8de2dbce` has no `<<<<<<<`/`>>>>>>>` scan hits. Runtime health is now mixed rather than untested: Packet 7 ran bounded install/build/test/gate commands in a disposable proof clone.
- Important correction: `docs/ROADMAP.md` and `mvp.md` still disagree across the Packet 10 and nuance/provenance source reads. `ROADMAP.md` says Pentagon/default daemon, `@lev-os/testing`, and security remain red/open; `mvp.md` says those scoped gates are green while launch readiness remains blocked. Treat this as a source-doc split until fresh commands settle it.

## Do not

- Do not treat chat transcripts as implementation proof.
- Do not treat old LevOS product pages as current repo truth.
- Do not assume `/Users/joshuaeisenhart/GitHub/leviathan` exists.
- Do not recover the deleted damaged checkout or mutate a fresh clone while doing wiki work.
- Do not say `implemented`, `enterprise-ready`, or `canonical` unless current docs/code/tests earn that exact rung.
- Do not flatten Josh's root constraints into generic startup/product language.
- Do not flatten JP's runtime implementation work into Codex Ratchet math/proof work.
