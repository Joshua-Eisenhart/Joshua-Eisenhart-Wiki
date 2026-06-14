# Wizard Agent Contract

This wiki-local `AGENTS.md` points agents into the current Wizard wiki harness. It is subordinate to the current user request and to any repo-local `AGENTS.md` / `CLAUDE.md` in the working repository.

## Boot order

For agents reading this wiki:

1. Read `README.md`.
2. Read `00-read-first.md`.
3. Read this `AGENTS.md`.
4. Read `packet-v4-3-current/README.md`.
5. Read `packet-v4-3-current/00_READ_FIRST.md`.
6. Load the v4.3 MMM: `packet-v4-3-current/mmm/FULL_MMM_v4_3.md`, or `packet-v4-3-current/mmm/COMPACT_MMM_v4_3.md` plus `packet-v4-3-current/mmm/mini/MEMBER_MINI_MMM_REGISTRY_v4_3.md` when context is tight.
7. Read `packet-v4-3-current/WIZARD_v4_3.md`.
8. Load the active runtime adapter, e.g. `hermes-version-current/` or `claude-version-current/`.
9. Load the task.

## Current binding

Current Wizard binding is **v4.3**. The shared core lives in `packet-v4-3-current/`. Per-LLM adapters live as sibling folders under `~/wiki/wizard/` and must be retuned to each system's native tools.

Do not treat Hermes, Claude, Codex, or any other adapter as universal authority. Copying files across adapters is allowed; adoption requires retuning and receipt-backed verification.

## Legacy boundary

`packet-v4-2-current/` and earlier packet folders are legacy/provenance. Mine them only when the task calls for genealogy, migration source material, or comparison. Do not boot from them as current runtime law.

## Status labels

`exists < runs < passes local rerun < canonical by process`. Do not imply a higher label from a lower one.
