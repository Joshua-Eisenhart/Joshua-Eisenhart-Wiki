---
title: Repo Layout Current Mirror
created: 2026-06-19
type: spec-mirror
status: draft_upgrade_pack
claim_ceiling: wiki routing / documentation upgrade only; no sim admission, no repo status promotion
tags: [codex-ratchet, repo-layout, spec]
sources:
  - Codex-Ratchet/REPO_LAYOUT.md
  - Codex-Ratchet/README.md
---


# Repo Layout Current Mirror — 2026-06-19

This is a wiki mirror card. The repo file is authoritative.

## Root surfaces

| Path | Role |
|---|---|
| `README.md` | entry point |
| `AGENTS.md` | Codex authority |
| `CLAUDE.md` | Claude/reference doctrine |
| `REPO_LAYOUT.md` | canonical layout map |
| `Makefile` | build/run entrypoints and Python authority |
| `scripts/` | runner, queue, lint, classification, witness checks |
| `system_v5/docs/` | human-readable current process/research docs |
| `system_v4/probes/` | active sim code and canonical sim results |

## Ignore/local-only reminder

Do not treat these as wiki/source authority unless a task explicitly asks for provenance or recovery:

- `work/`
- `archive/`
- `system_v3/`
- `obsidian_vault/`
- `overnight_logs/`
- `system_v4/runtime_state/`

## Key rules to mirror into wiki process

1. No random root docs.
2. Human-readable repo docs live under `system_v5/docs/`.
3. Sim results are written by probes, not hand-edited.
4. Every new sim starts from `system_v4/probes/SIM_TEMPLATE.py`.
5. `scripts/lint_sim_contract.py` is part of sim-contract checking.

## Claim ceiling

This mirror is for navigation. Exact repo paths remain authority.
