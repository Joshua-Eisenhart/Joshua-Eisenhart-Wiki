---
title: Process Contract Mirror Index
created: 2026-05-21
updated: 2026-05-21
type: mirror-index
framing: current
tags: [specs, codex-ratchet, process, contracts, authority]
sources:
  - /Users/joshuaeisenhart/Codex-Ratchet/AGENTS.md
  - /Users/joshuaeisenhart/Codex-Ratchet/CODEX.md
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v5/docs/ENFORCEMENT_AND_PROCESS_RULES.md
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v5/docs/LLM_CONTROLLER_CONTRACT.md
  - /Users/joshuaeisenhart/Codex-Ratchet/system_v5/docs/LEGO_SIM_CONTRACT.md
---

# Process Contract Mirror Index

This index separates repo process contracts from concept doctrine.

The repo remains authoritative. Wiki mirrors help route language and salience; they do not override local instructions, validators, result receipts, or repo-held process docs.

## Authority Order For Codex Ratchet Work

1. Current user request.
2. Repo instruction files, especially `AGENTS.md` and `CODEX.md` when present.
3. Repo process docs under `system_v5/docs/`.
4. Live result, validator, readiness, and evidence artifacts under `system_v5/`.
5. Wiki concept/source pages as salience, genealogy, divergence, and translation reservoirs.

## Live Repo Sources

| repo source | wiki mirror state | note |
|---|---|---|
| `AGENTS.md` | specs index only | Codex authority surface for current repo behavior. |
| `CODEX.md` | specs index only | Codex-specific overlay/reference when present. |
| `system_v5/docs/ENFORCEMENT_AND_PROCESS_RULES.md` | [[specs/codex-ratchet/enforcement-process-rules-current|enforcement-process-rules-current]] | Current spec mirror; concept mirror remains historical. |
| `system_v5/docs/LLM_CONTROLLER_CONTRACT.md` | [[specs/codex-ratchet/llm-controller-contract-current|llm-controller-contract-current]] | Current spec mirror; concept mirror remains historical. |
| `system_v5/docs/LEGO_SIM_CONTRACT.md` | [[specs/codex-ratchet/lego-sim-contract-current|lego-sim-contract-current]] | Current spec mirror; concept mirror remains historical. |
| `system_v5/docs/FORMAL_SCOUT_READINESS_INDEX.md` | [[specs/codex-ratchet/formal-scout-readiness-status|formal-scout-readiness-status]] | Count-bearing only when its generated timestamp matches the repo source; otherwise a dated mirror. |
| `system_v5/docs/SIM_ESTATE_INTEGRATION_INDEX.md` | [[specs/codex-ratchet/sim-estate-integration-status|sim-estate-integration-status]] | Count-bearing only when its generated timestamp matches the repo source; otherwise a dated mirror. |
| `system_v5/docs/TOOL_FUNCTION_RECEIPT_MATRIX.md` | [[specs/codex-ratchet/tool-function-receipt-status|tool-function-receipt-status]] | Tool/function receipt snapshot, dated `2026-05-17`; not a current formal-scout readiness/count surface. |

## Mirror Discipline

- If a mirror contains generated counts, include the generated timestamp and source path.
- If a concept page contains old generated counts, mark them as historical or route to a spec mirror.
- Do not hand-maintain repo status prose across many concept pages.
- Do not treat `CLAUDE.md`, old handoffs, or old wiki mirrors as Codex behavior law.
- Do not treat Wizard orchestration, provider agreement, or external-model text as sim/proof evidence without local receipt boundaries.

## Next Contract Repairs

1. Keep [[enforcement-and-process-rules]], [[llm-controller-contract]], and [[lego-sim-contract]] as historical/source-language concept mirrors unless a later pass intentionally replaces them with short stubs.
2. Use [[specs/codex-ratchet/enforcement-process-rules-current|enforcement-process-rules-current]], [[specs/codex-ratchet/llm-controller-contract-current|llm-controller-contract-current]], and [[specs/codex-ratchet/lego-sim-contract-current|lego-sim-contract-current]] for current wiki-side routing.
3. Keep source/source-voice pages in `/concepts`; translate or caveat them rather than flattening them into repo specs.
