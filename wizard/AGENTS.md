# Codex Wizard Agent Contract

This wiki-local `AGENTS.md` is a Codex-facing pointer into the current Wizard wiki harness. It is subordinate to the current user request and to any repo-local `AGENTS.md` in the working repository.

## Boot order

For Codex against this wiki:

1. Read `README.md`.
2. Read `00-read-first.md`.
3. Read this `AGENTS.md`.
4. Read `packet-v4-2-current/README.md`.
5. Read `packet-v4-2-current/WIZARD_v4_2.md`.
6. Load `packet-v4-2-current/mmm/FULL_MMM_v4_2.md`.
7. Read `packet-v4-2-current/skills/SKILLS_MANIFEST_v4_2.md` and `packet-v4-2-current/mmm/` route-local mini-MMMs as needed.
8. Load the task and the runtime adapter needed for that task.

Wizard v4.2 is current. Do not silently downgrade current Wizard work to v4.1. Use v4.1 only when the user explicitly asks for legacy v4.1 comparison or provenance.

Wizard v4.3 is an additive object-preservation guard that runs *before* the v4.2 councils — not a new runtime and not a replacement for this boot order. Its authority is repo-held (Codex Ratchet: `system_v5/docs/WIZARD_V4_3_PRIMARY_OBJECT_PRESERVATION_SPEC_20260526.md`, `scripts/wizard_v4_3_object_preservation.py`, `.codex/skills/three-council-wizard-v4-3/`), not wiki-held. Run it as a preflight when the task has a novel object or shows salience/proxy drift, then run v4.2 here. Do not create a `packet-v4-3-current` directory. Wiki routing context: `hermes-current/wiki-wizard-v4-3-object-preservation-guard.md`.

## Codex-side notes

- Repo-root `AGENTS.md` remains Codex's binding authority for repo behavior. This wiki file does not override a repository contract.
- Claude / Opus / Gemini / other model routes are advisory until Codex checks them against local state and current Wizard/Codex project rules.
- Subagent, child, receipt, route, and status claims require current receipts. Parent-reported child summaries are not raw nested proof unless the artifacts are visible.

## Status labels

`exists < runs < passes local rerun < canonical by process`. Do not imply a higher label from a lower one.
