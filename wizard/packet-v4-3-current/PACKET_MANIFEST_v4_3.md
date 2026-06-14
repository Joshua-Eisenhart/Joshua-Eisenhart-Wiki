# Packet Manifest v4.3

authority_status: canonical-runtime-pointer
packet_version: v4.3
current_runtime: `WIZARD_v4_3.md`

## Canonical Boot Path

Load in this order:

1. `mmm/FULL_MMM_v4_3.md`, or `mmm/COMPACT_MMM_v4_3.md` plus `mmm/mini/MEMBER_MINI_MMM_REGISTRY_v4_3.md` when context is tight.
2. `WIZARD_v4_3.md`.
3. `skills/SKILLS_MANIFEST_v4_3.md`.
4. `agents/AGENTS_MANIFEST_v4_3.md`.
5. `taskcards/TASKCARDS_MANIFEST_v4_3.md`.
6. One adapter, only when needed.

This manifest describes the current v4.3 runtime boot. Object-preservation, maintenance, route truth, and MMM loading are part of v4.3 current routing; per-LLM adapters bind the shared packet to each runtime.

`WIZARD_v4_3.md` owns the core runtime contract. Packet-local `agents/` and `taskcards/` files now provide instantiation surfaces for the parent/child/manager roles described there.

## Authority Tags

Every active runtime-bearing file must declare one authority status:

- `canonical-runtime-pointer`
- `canonical-runtime`
- `canonical-topology`
- `canonical-schema`
- `canonical-skill`
- `adapter`
- `conformance`
- `reference-only`
- `archive`

No untagged runtime-bearing file is authoritative.

## Active Runtime Files

- `WIZARD_v4_3.md`: canonical-runtime.
- `mmm/FULL_MMM_v4_3.md`: canonical-runtime salience.
- `mmm/COMPACT_MMM_v4_3.md`: canonical-runtime salience.
- `mmm/mini/MEMBER_MINI_MMM_REGISTRY_v4_3.md`: canonical-runtime salience registry.
- `skills/SKILLS_MANIFEST_v4_3.md`: canonical-skill manifest.
- `skills/**/*.md`: packet-local canonical skills when listed in `skills/SKILLS_MANIFEST_v4_3.md`.
- `conformance/validate_v4_3_packet.py`: packet conformance check.
- `conformance/validate_v4_3_cross_adapter_drift.py`: local cross-adapter drift check for Hermes/Claude/Codex v4.3 route surfaces.
- `skills/claude-bridge/scripts/*.py`: packet-local helper scripts for the Claude bridge route when that adapter/route is invoked.
- `agents/AGENTS_MANIFEST_v4_3.md`: canonical-agent-spec manifest.
- `agents/**/*.md`: packet-local agent specs when listed in `agents/AGENTS_MANIFEST_v4_3.md`.
- `taskcards/TASKCARDS_MANIFEST_v4_3.md`: canonical-schema manifest for parent/child task cards.
- `taskcards/**/*.md`: packet-local boot rules, schemas, and templates when listed in `taskcards/TASKCARDS_MANIFEST_v4_3.md`.

## Drift Rule

If any operational text disagrees with `WIZARD_v4_3.md`, `WIZARD_v4_3.md` controls runtime and conformance must fail until the contradiction is fixed.

## Reference-Only MMM Candidates

- `mmm/SALIENCY_TRANCHE_01_CANDIDATE.md`: reference-only source-language candidate from whole-wiki/MMM processing. It is not active boot salience until explicitly admitted and conformance-checked. Initial behavior test is recorded at `../../../concepts/mmm-saliency-test-harness.md`.
- `mmm/SALIENCY_TRANCHE_02_V4_3_OBJECT_PRESERVATION_MAINTENANCE_CANDIDATE.md`: reference-only v4.3 object-preservation / maintenance salience overlay. It exists so v4.3 maintenance workers can preload object-card, proxy-drift, route-truth, and MMM-admission language before task rules. It is not canonical runtime salience unless dedup, behavior checks, and conformance explicitly admit it.

## Excluded From Runtime

No `.DS_Store`, `__pycache__`, generated receipt estate, transcript, HTML report, old packet copy, or source archive is part of the active boot path.
