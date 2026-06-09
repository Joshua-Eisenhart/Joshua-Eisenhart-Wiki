---
type: summary
updated: 2026-05-17
tags: [harness, authority, v5, realignment]
---

# Wiki Harness v5 Alignment

## Purpose
This page is a dated bridge note for the 2026-04 v5-alignment repair. It should prevent salience drift between the `hermes-current/` front door, Codex Ratchet project status, repo/runtime specs, and lower-entropy concept routers.

## Current-use boundary
- Strongest use: transition note explaining how the older v5-alignment framing should be read after the newer `hermes-current/` spine exists.
- Weak use: live front door, runner-readiness claim, or replacement for `projects/codex-ratchet/read-first.md` / `projects/codex-ratchet/STATUS.md`.
- Authority boundary: this page routes readers; it does not certify repo health, promote sim status, or override project-specific status surfaces.

## Authority Ladder
1. **Hermes current spine (`hermes-current/`)**: mandatory read-first surface for Hermes-side behavior, stable working frame, active intentions, and current-vs-legacy rules.
2. **Project front doors and status surfaces**: for Codex Ratchet, read `projects/codex-ratchet/read-first.md` and `projects/codex-ratchet/STATUS.md` before treating any repo/spec page as operationally usable.
3. **System v5 specs and repo/runtime artifacts**: source of runtime/spec semantics when freshly located and relevant; they do not by themselves prove runner health or upgrade wiki/result status labels.
4. **Current bridging and concept pages**: translate and route doctrine after the front doors; they do not outrank the Hermes spine or project status.
5. **Legacy concept clusters and archives**: useful for genealogy/support; read with explicit current-vs-legacy and refinement-level boundaries.

## Reading Order for Autonomous Agents
1. `hermes-current/read-first.md`
2. `hermes-current/about-me-and-how-to-work-with-me.md`
3. `hermes-current/active-intentions.md`
4. `hermes-current/environment-and-rules.md`
5. `hermes-current/current-vs-legacy.md`
6. `hermes-current/skills-and-agent-rules.md`
7. `hermes-current/active-plans.md` when the task involves handoff, planning, automation, or next steps
8. `projects/codex-ratchet/read-first.md` and `projects/codex-ratchet/STATUS.md` when the task touches Codex Ratchet status, runner readiness, repo-backed claims, or queue/rerun work
9. `hermes-current/wiki-ingest-queue-and-priorities.md` and `hermes-current/wiki-wizard-v4-2-autoloop-control.md` for autonomous wiki-ingest/autoloop ticks
10. second-layer routers such as `concepts/current-canonical-spine.md`, `concepts/current-research-overlays.md`, `concepts/topic-map.md`, and root `index.md`

## Codex Ratchet safety fence
- Snapshot basis: `projects/codex-ratchet/STATUS.md` last updated `2026-05-17T05:32:27Z`, checkpoint `a14526226`.
- Current claim ceiling from that snapshot: cleanup checkpoint landed, but runner preflight is still red on `57` old claimed queue files and Git index instability remains live.
- Do not call Codex Ratchet runner-ready from a clean wiki probe, a v5 spec path, or a concept-page routing chain.
- Stop and surface the blocker if runner preflight is red, the claimed queue is unreconciled, Git index behavior is unproven, or the task would require repo/git/runner mutation from a wiki autoloop tick.

## Enforcement Rules
- **No Blob Pages**: every page must have a clear type and a defined role in the cluster.
- **Archive Over Delete**: move stale or redundant pages to `_archive/` only with same-tick link/navigation repair.
- **Structural Integrity**: every autonomous tick must leave the published wiki structurally clean under `wiki_probe.py`.
- **Scope Integrity**: `wiki_probe.py` is structural evidence only; it does not certify `hermes-current/`, project status truth, repo readiness, or runtime health.
- **Truth Labels**: repo-backed claims need `snapshot:` or `fresh-rerun:` support; artifact existence does not promote to `passes local rerun` or `canonical by process`.

## Audit Trace
- **2026-05-17**: Patched as a dated transitional authority/role note so it no longer routes agents around the `hermes-current/` front door or the Codex Ratchet red-status gate.
- **2026-04-16**: Page created to harden handoff and autonomous tick discipline.
