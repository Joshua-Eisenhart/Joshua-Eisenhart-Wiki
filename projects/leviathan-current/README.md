---
title: Leviathan Current Wiki Project
created: 2026-06-17
updated: 2026-06-19
type: project-front-door
status: active current-source router
claim_ceiling: wiki routing and current-repo orientation; not fresh command proof; not maintainer acceptance; not release certification
sources:
  - https://github.com/lev-os/leviathan
  - https://raw.githubusercontent.com/lev-os/leviathan/main/README.md
  - https://raw.githubusercontent.com/lev-os/leviathan/main/docs/README.md
  - https://raw.githubusercontent.com/lev-os/leviathan/main/docs/NORTH_STAR.md
  - https://raw.githubusercontent.com/lev-os/leviathan/main/docs/ROADMAP.md
  - https://raw.githubusercontent.com/lev-os/leviathan/main/docs/ARCHITECTURE.md
  - /Users/joshuaeisenhart/wiki/wizard/harness-consolidated/14_leviathan_os_constraint_map.md
  - /Users/joshuaeisenhart/wiki/projects/levos/levos-dev-handoff-product-and-runtime-2026-06-15.md
  - /Users/joshuaeisenhart/wiki/projects/leviathan-current/source-inventory-2026-06-17.md
tags:
  - leviathan
  - lev-os
  - levos
  - runtime
  - wiki-project
---

# Leviathan Current Wiki Project

## Purpose

This folder is the current wiki project for understanding `lev-os/leviathan` as it is published on GitHub now.

For the actual content table of contents, start at [[projects/leviathan-current/index]].

It should answer four questions without forcing Josh to re-explain the project:

1. What is Lev / Leviathan?
2. What currently exists in the repo?
3. What is intended but not yet landed?
4. How do Josh's root constraints and JP Smith's Lev runtime architecture relate without collapsing into one another?

## Current bottom line

Observed from current repo docs: Lev is an open runtime for agent-human systems: agents act through real surfaces, under explicit policy, graph memory, auditable events, execution boundaries, and human approval surfaces.

The active repo docs describe the foundation as real but still being hardened. They explicitly say the universal context graph is not fully landed, the system is not enterprise-ready, and architecture is ahead of some implementation areas.

Current source/proof routers:

- [[specs/leviathan-current/README]]
- [[projects/leviathan-current/proof-backed-status-dashboard]]
- [[projects/leviathan-current/nuanced-assessment-and-josh-provenance-2026-06-19]]

Advisory intake and source-synthesis routers:

- [[projects/leviathan-current/packet-11-deeper-nuance-attribution-pack-intake-2026-06-19]]
- [[projects/leviathan-current/packet-12-pasted-deep-research-truth-provenance-intake-2026-06-19]]
- [[projects/leviathan-current/packet-13-pasted-fep-runtime-boundary-audit-intake-2026-06-19]]
- [[projects/leviathan-current/packet-14-pasted-fep-atlas-and-leviathan-boundary-intake-2026-06-19]]
- [[projects/leviathan-current/packet-15-wizard-multi-model-council-audit-2026-06-19]]
- [[projects/leviathan-current/codex-imports/v3-deep-repo-nuance-bundle-2026-06-19]]
- [[projects/leviathan-current/codex-imports/v4-cross-issues-deep-dive-2026-06-19]]

The latest fresh 2026-06-19 remote/clone check is `5dd98ac4ce7afeb9e4351787179c60208de6d23f`. The older clean-clone audit at [[projects/leviathan-current/deep-audit-current-snapshot-2026-06-18]] remains valid for its `c90ec...` snapshot and for demoting damaged-checkout conflict-marker claims.

## Best First Clicks

- [[projects/leviathan-current/read-first]]
- [[projects/leviathan-current/current-state-and-roadmap]]
- [[projects/leviathan-current/proof-backed-status-dashboard]]
- [[projects/leviathan-current/read-order-by-intent-2026-06-18]]
- [[projects/leviathan-current/packet-8-wizard-mass-swarm-receipt-2026-06-18]]
- [[projects/leviathan-current/packet-15-wizard-multi-model-council-audit-2026-06-19]]

## Source mode

The damaged local checkout at `/Users/joshuaeisenhart/GitHub/leviathan` was deleted on 2026-06-18 by direct user request. New wiki work reads the live GitHub website/remote, not a persistent local checkout.

Use:

- `https://github.com/lev-os/leviathan`
- `https://raw.githubusercontent.com/lev-os/leviathan/main/<path>` for current files
- `https://raw.githubusercontent.com/lev-os/leviathan/<commit>/<path>` for stable cited snapshots
- `https://api.github.com/repos/lev-os/leviathan/contents/<path>?ref=main` for machine-readable directory listings

Remote `main` observed on 2026-06-19 during Packet 10: `b7bca2cdbed5862743395f7c0330e7d640132764`.
Remote `main` observed on 2026-06-19 during the nuance/provenance pass: `5dd98ac4ce7afeb9e4351787179c60208de6d23f`.

Old local-path citations in this folder remain historical evidence from the June 17-18 local inventory and damaged-checkout containment pass. They are not current source instructions and do not prove the local path still exists.

If website/raw/API access is too limited for a packet, a clean fresh clone from `https://github.com/lev-os/leviathan.git` is allowed as a fallback. Prefer `/tmp` for disposable read-only scans. If a persistent checkout is needed, create it fresh, record the remote URL, commit SHA, and clean status, and do not edit it during wiki work unless Josh explicitly assigns a repo patch.

## Current repo authority order

For this project, read current repo sources before chat-derived or legacy material:

1. `https://github.com/lev-os/leviathan/tree/main/docs/specs/` or raw/API equivalents — normative contracts.
2. `https://raw.githubusercontent.com/lev-os/leviathan/main/docs/ARCHITECTURE.md` — canonical topology and ownership boundaries.
3. `https://raw.githubusercontent.com/lev-os/leviathan/main/docs/VISION.md` — stable strategic destinations.
4. `https://raw.githubusercontent.com/lev-os/leviathan/main/mvp.md` and `https://raw.githubusercontent.com/lev-os/leviathan/main/docs/ROADMAP.md` together — contested execution state until proof reruns settle the conflict.
5. `https://raw.githubusercontent.com/lev-os/leviathan/main/docs/NORTH_STAR.md` and `https://raw.githubusercontent.com/lev-os/leviathan/main/README.md` — vision and product frame.
6. `https://raw.githubusercontent.com/lev-os/leviathan/main/AGENTS.md` — agent/contributor operating contract, not product truth.
7. `https://github.com/lev-os/leviathan/tree/main/docs/design/` or raw/API equivalents — rationale and deeper design reference.
8. `docs/_inbox/`, `_archive/`, chats, transcripts, and older LevOS wiki notes — source material / provenance, not current implementation truth by default.

## Key current source artifacts

### Front door / control

- `read-first.md` — project boot note for future agents.
- `deep-audit-current-snapshot-2026-06-18.md` — current clean snapshot audit and replacement baseline for upstream source truth.
- `repo-current-vs-wiki-drift-audit-2026-06-18.md` — drift map explaining which older local-checkout pages are now historical.
- `concept-atlas-current-2026-06-18.md` — concept map with aliases, evidence levels, currentness, wiki targets, and claim ceilings.
- `evidence-frontier-and-blockers-dashboard-2026-06-18.md` — current contradictions/blockers that require reruns or source reconciliation.
- `proof-audit-roadmap-vs-mvp-2026-06-18.md` — clean-clone command proof audit for the `ROADMAP.md` vs `mvp.md` split.
- `proof-backed-status-dashboard.md` — current `b7bca2cd` source-doc split and proof-routing dashboard.
- `nuanced-assessment-and-josh-provenance-2026-06-19.md` — current `5dd98ac4` assessment of strengths, weaknesses, delusion/overclaim risk, and Joshua/JP provenance boundaries.
- `packet-11-deeper-nuance-attribution-pack-intake-2026-06-19.md` — pass-with-cautions intake for the deeper nuance/attribution pack.
- `packet-12-pasted-deep-research-truth-provenance-intake-2026-06-19.md` — pass-with-cautions intake for the pasted deep-research truth/provenance report; reinforces the current boundary and incompleteness posture without adding runtime proof.
- `packet-13-pasted-fep-runtime-boundary-audit-intake-2026-06-19.md` — pass-with-cautions intake for the pasted Leviathan/FEP runtime-boundary audit; routes active-inference and world-model support without adding implementation proof.
- `packet-14-pasted-fep-atlas-and-leviathan-boundary-intake-2026-06-19.md` — pass-with-cautions intake for the pasted FEP atlas correction and Leviathan boundary audit; routes FEP through the existing concept atlas and adds Leviathan-specific boundary split pages without adding runtime proof.
- `packet-15-wizard-multi-model-council-audit-2026-06-19.md` — multi-model council receipt and correction patch for Packet 14/FEP split pages; route/correction evidence only.
- `codex-imports/v3-deep-repo-nuance-bundle-2026-06-19.md` — branch-imported V3 deep-repo nuance bundle and page-split plan; source synthesis only, not runtime proof or maintainer acceptance.
- `codex-imports/v4-cross-issues-deep-dive-2026-06-19.md` — branch-imported V4 cross-issues bundle and page-split plan; source synthesis only, not runtime proof, product readiness, or maintainer acceptance.
- `josh-jp-attribution-boundary-v2-2026-06-19.md` — owner-corrected attribution boundary: Ratchet does not come from Leviathan; original Wizard idea credited to JP Smith per Josh.
- `no-ratchet-from-leviathan-policy.md` — short policy page preventing Ratchet-from-Lev inversion.
- `wizard-origin-provenance-note-2026-06-19.md` — project-local Wizard origin note.
- `packet-10-deep-research-upgrade-pack-intake-2026-06-19.md` — intake receipt for the 2026-06-19 deep-research report and ZIP upgrade pack.
- `specs/leviathan-current/README.md` — repo-facing mirror/source-authority router.
- `read-order-by-intent-2026-06-18.md` — read order by task/persona for a huge mixed repo.
- `source-inventory-2026-06-17.md` — first repo inventory; 12,699 files excluding common build/cache dirs; 4,848 Markdown/MDX files; 250 chat/transcript/Josh-JP routing candidates captured in the JSON sidecar.
- `source-inventory-2026-06-17.json` — full machine-readable inventory sidecar.
- `bounded-ingestion-plan.md` — finite packet plan for turning the repo into wiki pages.
- `worker-swarm-plan-2026-06-17.md` — first bounded worker-wave plan.
- `concept-map-start.md` — first current concept map with strict claim ceilings.
- `ratchet-working-receipt-2026-06-18.md` — scope-corrected ratchet assessment receipt: multi-model pressure found a contract-vs-implementation gap; repo code edits from the detour were reverted, so cite this as wiki/process guidance only.
- `model-pressure/fusion-glm-wiki-direction-2026-06-18.md` — OpenRouter Fusion + GLM 5.2 wiki-direction pressure memo; advisory only until source-verified.
- `wiki-swarm-launch-receipt-2026-06-18.md` — scope correction, model-pressure receipt, and background Packet 2/4/5 worker launch ledger.

### Packet 1 — current authority docs

- `what-is-leviathan.md` — plain-English current-authority synthesis.
- `current-state-and-roadmap.md` — status/roadmap synthesis with open gaps preserved.
- `architecture-planes-and-ownership.md` — four-plane/runtime ownership map.
- `contract-surface-map.md` — normative specs/contract map plus drift findings.
- `packet-1-processing-receipt-2026-06-17.md` — bounded processing receipt for this tranche.

### Packet 2 — runtime/module map

- `runtime-module-map-start.md` — package/workspace and core module starter map.
- `flowmind-control-plane-start.md` — FlowMind control-plane starter map.
- `event-graph-orchestration-start.md` — Event Bus / Graph / Orchestration starter map.
- `flowmind-control-plane.md` — FlowMind source/package control-plane map.
- `graph-state-knowledge-plane.md` — Graph state/knowledge ownership map.
- `event-bus-causality-plane.md` — Event Bus causality spine map from the damaged local checkout; use it for source mapping, then use the clean snapshot audit and Packet 7/8 proof audit pages for current runtime status.
- `orchestration-execution-plane.md` — Orchestration DAG/loop/queue execution-plane map.
- `exec-poly-daemon-boundary.md` — Exec / Poly / Daemon ownership split.
- `plugin-ownership-map.md` — plugin inventory, registration, and ownership map.
- `packet-2-runtime-map-receipt-2026-06-17.md` — bounded receipt and verification notes for the first Packet 2 tranche.
- `runtime-module-map-full-2026-06-18.md` — Packet 2 full runtime/module map across FlowMind, Orchestration, Graph, Event Bus, Exec, Poly, Daemon, plugins, and Rust crates; current snapshot with blockers.
- `runtime-build-test-surface-map-2026-06-18.md` — build/test/CI/tooling surface map; command/manifests/config/workflow map only, no package health claim.
- `packet-2-full-runtime-map-receipt-2026-06-18.md` — receipt for the full Packet 2 runtime map pass, including exact paths read and validation caveats.

Packet 2 note: these pages remain valuable as source maps, but their local-checkout conflict-marker blockers are superseded for current upstream truth by the clean snapshot audit. Current runtime status is mixed after Packet 7/8, with named SDK/Poly proof green while default daemon Pentagon, `@lev-os/testing`, and event-dispatch proof-spine remain red or blocked.

### Packet 3 — product surfaces and human-loop layer

- `agentping-human-loop-surfaces.md` — current-source map of AgentPing as Lev's default human-loop/reference host direction; runtime health remains open.
- `agentlease-scoped-authority.md` — scoped-authority map for AgentLease concept plus observed lease primitives; full product/runtime integration remains open.
- `packet-3-product-surfaces-receipt-2026-06-18.md` — controller-written receipt after the Packet 3 subagent failed before writeback.

### Packet 4 — Josh constraint contribution / boundary layer

- `josh-root-constraints-in-leviathan.md` — source-labeled map of Josh/root-constraint contribution inside current Lev surfaces.
- `lev-five-constraints-vs-f01-n01.md` — C1-C5 vs F01/N01 bridge, with C3-C5 held as derived/aligned unless source support is stronger.
- `codex-ratchet-vs-leviathan-boundary.md` — explicit boundary page: Leviathan contains many Josh ideas but is NOT Codex Ratchet.
- `nuanced-assessment-and-josh-provenance-2026-06-19.md` — sharper boundary: Codex Ratchet does not come from Leviathan; JP's original Wizard idea influenced Joshua's Wizard lineage; Joshua-origin constraint/QIT material appears inside Leviathan as design/provenance/plugin/runtime-validator surfaces.
- `packet-4-constraint-boundary-receipt-2026-06-18.md` — receipt for the boundary tranche.

### Packet 5 — chat/transcript provenance protocol

- `chat-evidence-promotion-protocol.md` — rulebook for promoting chat/transcript claims only after repo/code/doc/test match.
- `chat-tranche-1-processing-2026-06-18.md` — first bounded queue slice; rows 50-55 classified conservatively.
- `packet-5-chat-tranche-receipt-2026-06-18.md` — receipt for first chat/provenance tranche.

### Packet 6 — concept atlas and evidence frontier

- `concept-atlas-current-2026-06-18.md` — source-backed concept atlas across runtime, state/memory, product surfaces, and docs/provenance boundaries.
- `evidence-frontier-and-blockers-dashboard-2026-06-18.md` — unresolved contradiction and blocker dashboard, including `mvp.md` vs `docs/ROADMAP.md`.
- `read-order-by-intent-2026-06-18.md` — safer read-order guide for humans, agents, runtime auditors, wiki workers, and provenance work.
- `packet-6-concept-atlas-receipt-2026-06-18.md` — worker/source/wiki receipt for this packet.

### Packet 7 — clean-clone proof audit

- `proof-audit-roadmap-vs-mvp-2026-06-18.md` — command-backed split verdict for the `docs/ROADMAP.md` vs `mvp.md` contradiction.
- `packet-7-clean-clone-proof-audit-receipt-2026-06-18.md` — route, worker, command, and wiki receipt for the proof audit.

Packet 7 note: the named `pentagon-sdk-poly-binding` run/gate passes after package builds, but default `lev pentagon run/gate --project .` fails with 42 daemon mini-app missing-artifact diagnostics, and `@lev-os/testing test` fails before assertions. High audit exits 0 while low/moderate vulnerabilities remain.

### Packet 8 — Wizard mass swarm cleanup

- `packet-8-wizard-mass-swarm-receipt-2026-06-18.md` — Wizard v4.3 object card, Codex-native multi-model worker receipts, external-route blockers, and wiki cleanup receipt.

Packet 8 note: the daemon Pentagon blocker is narrower than "artifacts absent"; a representative report stores absolute artifact paths from another checkout while clone-local mini-app artifacts exist. The `@lev-os/testing` blocker is narrowed to Vitest/Bun-condition source-entry resolution around `@lev-os/utils`. Event-dispatch proof is blocked on `@lev-os/daemon` and `@lev-os/config/xdg-paths` package/build resolution, not on CLI help surface absence.

### Packet 9 — stale external upgrade report intake

- `packet-9-external-upgrade-report-intake-2026-06-18.md` — intake and quarantine page for an external "Leviathan OS Wiki Upgrade Research and Packaging Report" attachment.

Packet 9 note: the report is useful as advisory packaging pressure but stale for current wiki truth. Its three-plane architecture framing, failed-public-wiki-retrieval premise, non-portable `turn...` citations, and lack of Packet 7/8 proof state block direct merge.

### Packet 10 — deep-research upgrade pack intake

- `packet-10-deep-research-upgrade-pack-intake-2026-06-19.md` — intake page for `/Users/joshuaeisenhart/Desktop/deep-research-report.md` and `/Users/joshuaeisenhart/Desktop/leviathan_wiki_upgrade_pack_2026-06-19.zip`.
- `proof-backed-status-dashboard.md` — current proof/source split dashboard created from the pack plus fresh source check.
- `specs/leviathan-current/README.md` — new repo-facing mirror policy page.

Packet 10 note: the ZIP is useful as an upgrade plan, but it carried `c90ec...` while current remote `main` was `b7bca2cd`. Accepted changes were routed through current source checks, not blindly imported.

### Packet 11 — deeper nuance and attribution addendum

- `packet-11-deeper-nuance-attribution-pack-intake-2026-06-19.md` — intake page for `/Users/joshuaeisenhart/Desktop/deep-research-report (1).md` and `/Users/joshuaeisenhart/Desktop/leviathan_os_deeper_nuance_attribution_pack_2026-06-19.zip`.
- `owner-correction-receipt-2026-06-19.md` — owner correction for Josh/Joshua/Codex Ratchet identity and no-Ratchet-from-Lev boundary.
- `josh-jp-attribution-boundary-v2-2026-06-19.md` — attribution boundary table.
- `leviathan-strengths-weaknesses-delusion-audit-2026-06-19.md` — source-backed pre-release runtime-project assessment with overclaim risks.
- `unmergeable-claims-register-2026-06-19.md` and `source-audit-queue-v2-2026-06-19.md` — claims that must stay split or be source-audited before stronger use.

Packet 11 note: this addendum is owner-correction and wiki attribution routing. It is not runtime proof and not implementation-authorship proof.

### Packet 12 — pasted deep-research truth/provenance intake

- `packet-12-pasted-deep-research-truth-provenance-intake-2026-06-19.md` — intake page for `/Users/joshuaeisenhart/.codex/attachments/cbd2ee6d-9a7c-48a3-b94d-68e49c4ab56c/pasted-text.txt`.

Packet 12 note: the report is useful as advisory pressure and mostly reinforces Packet 10/11. It does not carry portable citations or fresh repo proof.

### Packet 13 — pasted FEP/runtime-boundary audit intake

- `packet-13-pasted-fep-runtime-boundary-audit-intake-2026-06-19.md` — intake page for `/Users/joshuaeisenhart/.codex/attachments/0b62aa68-2c2c-46e1-b573-b1a9c1554537/pasted-text.txt`.

Packet 13 note: the audit is useful for FEP/active-inference and world-model boundary discipline. It does not make Leviathan an implemented FEP runtime, and its non-portable citations require source re-checks before stronger use.

### Packet 14 — FEP atlas correction and Leviathan boundary split

- `packet-14-pasted-fep-atlas-and-leviathan-boundary-intake-2026-06-19.md` — intake page for `/Users/joshuaeisenhart/.codex/attachments/9d7bccf2-41e3-4c04-9659-2e2acb2d01da/pasted-text.txt` and `/Users/joshuaeisenhart/.codex/attachments/bd9c4688-e356-4945-bf43-775915982d72/pasted-text.txt`.
- `lev-runtime-boundary-2026-06-19.md` — runtime boundary map for policy/control, orchestration/execution, graph/context, event/audit, package/surface, and human-loop surfaces.
- `leviathan-fep-runtime-boundary-2026-06-19.md` — FEP/active-inference support map; blocks "Leviathan implements FEP" wording.
- `sophisticated-inference-and-leviathan-2026-06-19.md` — belief-state planning crosswalk for world-model/reconciler questions.
- `world-model-reconciler-fep-support-2026-06-19.md` — world-model/reconciler support and proof backlog boundary.
- `leviathan-claim-ceilings-2026-06-19.md` — wording ladder for narrative, provenance, contract, package, source, test, proof, product, and release claims.
- `leviathan-validation-experiments-backlog-2026-06-19.md` — future validation experiment cards; none run yet.
- `provenance-status-guardrails-2026-06-19.md` — provenance status labels for verified, user-provided, source-signal, unspecified, disputed, and rejected claims.

Packet 14 note: the FEP concept atlas already existed. This packet only adds the Leviathan-facing split and keeps all pages below runtime proof.

### Packet 15 — multi-model council audit and correction

- `packet-15-wizard-multi-model-council-audit-2026-06-19.md` — receipt for a bounded Wizard-style council over Packet 14, the FEP split pages, root/project discoverability, and Codex Ratchet provenance boundaries.

Packet 15 note: four Codex-native model lanes completed. Claude Sonnet, Gemini, and Ollama lanes were attempted but blocked by authentication/runtime availability. The packet records corrections to wording and navigation only; it is not a full Wizard Max Assembly proof, Leviathan runtime proof, FEP implementation proof, release certification, or Codex Ratchet proof.

### V3 branch import bundle

- `codex-imports/v3-deep-repo-nuance-bundle-2026-06-19.md` — branch-imported Markdown bundle from `origin/leviathan-v3-info-import-2026-06-19`. It should be split into subsystem pages only after current source reads and evidence labeling; it is not runtime proof, release certification, or maintainer acceptance.

### V4 branch import bundle

- `codex-imports/v4-cross-issues-deep-dive-2026-06-19.md` — branch-imported Markdown bundle from `origin/leviathan-v4-cross-issues-import-2026-06-19`. It should be split into cross-issue pages only after current source reads and evidence labeling; it is not runtime proof, product readiness, release certification, or maintainer acceptance.

Split pages now derived from this bundle:

- [[projects/leviathan-current/operating-contract-vs-product-proof-2026-06-19]]
- [[projects/leviathan-current/docs-authority-vs-status-drift-v4-2026-06-19]]
- [[projects/leviathan-current/agents-md-operating-contract-risk-2026-06-19]]
- [[projects/leviathan-current/exec-poly-daemon-package-posture-v4-2026-06-19]]
- [[projects/leviathan-current/app-layer-readiness-map-2026-06-19]]
- [[projects/leviathan-current/onboarding-dx-proof-ladder-v4-2026-06-19]]
- [[projects/leviathan-current/security-gate-stack-v4-2026-06-19]]
- [[projects/leviathan-current/plugin-manifest-inflation-risk-v4-2026-06-19]]
- [[projects/leviathan-current/vision-strategic-truth-vs-magnus-opus-overhang-2026-06-19]]
- [[projects/leviathan-current/north-star-narrative-vs-proof-map-2026-06-19]]
- [[projects/leviathan-current/memory-backend-readiness-ladder-2026-06-19]]
- [[projects/leviathan-current/config-xdg-fractal-root-gap-2026-06-19]]
- [[projects/leviathan-current/surface-family-matrix-v4-2026-06-19]]
- [[projects/leviathan-current/lev-agentping-agentguard-three-system-map-2026-06-19]]
- [[projects/leviathan-current/enterprise-readiness-gap-v4-2026-06-19]]
- [[projects/leviathan-current/moat-vs-adoption-proof-v4-2026-06-19]]
- [[projects/leviathan-current/release-readiness-ladder-v4-2026-06-19]]

### Contribution / provenance / research / assessment starters

- `josh-contribution-signal-radar.md` — grounded starter radar for Josh's constraint contributions in docs/code.
- `josh-contribution-signal-index-2026-06-17.md` — broader controller-generated signal index after contribution-worker route failure.
- `chat-provenance-queue-2026-06-17.md` — classified queue for 250 chat/transcript/handoff candidates.
- `provenance-ledger-josh-jp-pass-1-2026-06-18.md` — first provenance ledger matching Josh/JP signals to current repo surfaces.
- `packet-4-provenance-receipt-2026-06-18.md` — receipt for the first provenance-ledger pass.
- `research-connection-map-start.md` — starter map of research-connected repo surfaces.
- `doing-well-failing-promising-start.md` — first assessment of strengths, failures, promise, and falsifiers.

## Existing related wiki surfaces

- `projects/levos/levos-gpt-webui-idea-ledger-2026-06-15.md` — processed GPT WebUI ideas; useful, not repo-current proof.
- `projects/levos/levos-dev-handoff-product-and-runtime-2026-06-15.md` — product/runtime framing; useful as a handoff draft, not repo contract.
- `projects/levos/levos-gpt-webui-representation-audit-2026-06-15.md` — coverage ledger for earlier idea intake.
- `wizard/harness-consolidated/14_leviathan_os_constraint_map.md` — constraint bridge between Lev terms and Josh/Codex Ratchet terms.

## Claim discipline

Do not say the wiki fully understands Leviathan yet. Current status is: scaffold exists, current-authority synthesis pages exist, the old local-checkout runtime maps are demoted, the 2026-06-18 clean snapshot audit supersedes damaged-checkout conflict-marker blockers for its snapshot, and Packet 10 adds a 2026-06-19 source check at `b7bca2cd`. Runtime verification is still not settled by prose: `docs/ROADMAP.md` and `mvp.md` currently disagree about Pentagon/default daemon, `@lev-os/testing`, and scoped security status, so the wiki must call that a source-doc split until a fresh proof packet reruns the commands.

The live synthesis must keep three layers separate:

- **repo-current implementation and contracts** — what files and tests say now;
- **JP/Lev-dev intent** — what the Lev docs and chat/source material say the system is trying to become;
- **Josh/root-constraint contribution** — finitude, non-commutation, nominalist reality, ratchet, locality, and the broader constraint/admissibility doctrine.
