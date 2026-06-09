# Packet Manifest v4.2

authority_status: canonical-runtime-pointer
packet_version: v4.2
current_runtime: `WIZARD_v4_2.md`

## Canonical Boot Path

Load in this order:

1. `mmm/FULL_MMM_v4_2.md`, or `mmm/COMPACT_MMM_v4_2.md` plus `mmm/mini/MEMBER_MINI_MMM_REGISTRY_v4_2.md` when context is tight.
2. `WIZARD_v4_2.md`.
3. `skills/SKILLS_MANIFEST_v4_2.md`.
4. One adapter, only when needed.

`WIZARD_v4_2.md` is self-contained. Topology, schemas, task cards, output rules, management-parent rules, external audit protocol, and Codex adapter rules are embedded there.

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

- `WIZARD_v4_2.md`: canonical-runtime.
- `mmm/FULL_MMM_v4_2.md`: canonical-runtime salience.
- `mmm/COMPACT_MMM_v4_2.md`: canonical-runtime salience.
- `mmm/mini/MEMBER_MINI_MMM_REGISTRY_v4_2.md`: canonical-runtime salience registry.
- `skills/SKILLS_MANIFEST_v4_2.md`: canonical-skill manifest.
- `skills/**/*.md`: packet-local canonical skills when listed in `skills/SKILLS_MANIFEST_v4_2.md`.

## Drift Rule

If any operational text disagrees with `WIZARD_v4_2.md`, `WIZARD_v4_2.md` controls runtime and conformance must fail until the contradiction is fixed.

## Reference-Only MMM Candidates

- `mmm/SALIENCY_TRANCHE_01_CANDIDATE.md`: reference-only source-language candidate from whole-wiki/MMM processing. It is not active boot salience until explicitly admitted and conformance-checked. Initial behavior test is recorded at `../../../concepts/mmm-saliency-test-harness.md`.
- `mmm/SALIENCY_TRANCHE_02_V4_3_OBJECT_PRESERVATION_MAINTENANCE_CANDIDATE.md`: reference-only v4.3 object-preservation / maintenance salience overlay. It exists so v4.3 maintenance workers can preload object-card, proxy-drift, route-truth, and MMM-admission language before task rules. It is not canonical runtime salience unless dedup, behavior checks, and conformance explicitly admit it.

## Excluded From Runtime

No `.DS_Store`, `__pycache__`, generated receipt estate, transcript, HTML report, old packet copy, or source archive is part of the active boot path.
