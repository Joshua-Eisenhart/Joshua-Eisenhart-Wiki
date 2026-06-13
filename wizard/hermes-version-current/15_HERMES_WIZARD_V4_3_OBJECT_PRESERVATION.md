# 15 — Hermes Wizard v4.3 Object-Preservation Guard

## Status

- **Hermes-authored packet**: `packets/hermes_v4_3_retrocausal_object_card.json`
- **Validator**: repo `scripts/wizard_v4_3_object_preservation.py` (sole authority — not forked)
- **Spec**: repo `system_v5/docs/WIZARD_V4_3_PRIMARY_OBJECT_PRESERVATION_SPEC_20260526.md`
- **Proven**: selftest ✅ · example ✅ · validate ✅ · loop ✅ — all from a Hermes session
- **Current binding**: v4.3-gated v4.2. v4.3 validates the current-task object card before councils; v4.2 remains the execution/runtime/output machinery.

## What v4.3 does

Wizard v4.3 is an **object-preservation preflight**. Before any council, sim, or follow-up loop claims progress on the primary object:

1. The packet must pass the repo guard (`validate --input <packet.json>`)
2. The object card must carry all required fields, a correct SHA-256 hash, and (for `retrocausal_possibility_field`) the shell-specific invariants
3. Lateral mappings must declare preserves/loses/kill-control and obey promotion rules
4. The evidence spine must name wizard runtime, claim ceiling, blocked consumers, and at least one source lock or audit receipt
5. Claude material must be marked "reference only, not authority"

## Hermes-native differences

The Hermes packet differs from the Codex example packet in:

- **Evidence spine**: names the Hermes session as the wizard runtime; the repo guard is the authority, not Codex or Claude
- **Lateral mapping**: includes a "Hermes three-council proxy readout" (proxy lane) — a pass/fail preflight signal that councils consume but cannot promote to an object claim
- **Artifact surface**: points at `wiki/wizard/hermes-version-current/packets/` rather than repo receipt paths
- **No validator fork**: Hermes calls the repo script directly; there is no second copy

## How to run

```bash
cd /Users/joshuaeisenhart/Codex-Ratchet

# selftest (negative controls)
python3 scripts/wizard_v4_3_object_preservation.py selftest --out /tmp/v43_selftest.json

# validate Hermes packet
python3 scripts/wizard_v4_3_object_preservation.py validate \
  --input ~/wiki/wizard/hermes-version-current/packets/hermes_v4_3_retrocausal_object_card.json

# loop (build→premortem→repair→selftest, max 3 iterations)
python3 scripts/wizard_v4_3_object_preservation.py loop --max-loops 3 --out /tmp/v43_loop.json
```

## Claim ceiling

Object-preservation preflight only. This guard makes **no** sim, physics, Axis0, flux, or formal-admission claim. It ensures the object card is well-formed and the evidence spine is honest before anything downstream consumes it.

## Blocked consumers

- v4.2 council progress claim without a passing object card
- sim/proof promotion without source lock and audit-spine receipts

## Pitfalls (discovered during authoring)

1. **SHA mismatch**: `object_statement_sha256` must be the SHA-256 of the *exact byte string* of `object_statement`. A single trailing space or line break kills it.
2. **macOS has no `timeout` command**: use plain `python3` invocations, not `timeout N python3 …`
3. **Retrocausal hard path**: if `object_type` is `retrocausal_possibility_field`, the validator checks `RETROCAUSAL_REQUIRED_FIELDS` against `first_class_fields` (must include event_x, shells, branch_states, shell_radius_r, shell_orientation, future_continuations, compatibility_weights, compression_map, present_survivor, outward_record) and `RETROCAUSAL_REQUIRED_INVARIANT_TERMS` (future, inward, outward, survivor, compatibility) in `required_invariants`.
4. **Claude authority gate**: any `claude_pattern_cards` entry with `.claude` in `source_path` must say "reference" or "not authority" in `authority_reason`.
5. **Proxy/analogy cannot promote**: `promotion_allowed: true` is only valid for `adapter` and `probe` use types.
6. **`plain_language_definition` minimum 35 words**: shorter definitions are rejected.
7. **`jk fuzz` native term**: if present, must contain "future", "possibil", or "continuation" in its definition.
8. **Nested PEPS2D / Hopfield connection geometry**: PEPS3D (single fused 3D contraction) was replaced by nested PEPS2D / Hopfield connection geometry — L/R Weyl spinors on nested Hopf-torus sheets, Hopfield/PEPS2D bonds *are* the connection surface, geometry read from plaquette holonomy, Laplacian spectrum, heat trace, curvature, terrain/operator signatures. CTMRG works within each 2D layer; what's retired is CTMRG on structured 3D tensors. **Claim ceiling: diagnostic scratch carrier, not formal repo admission** (repo authority still has stale PEPS3D gates). Other current carriers: ITensors-MPS (scale ladder), exact dense (TensorKit), QuantumClifford (stabilizer levels), spinor trajectories (dissipative). All require contraction-error certificates.

## Provenance

- Authored: Hermes session, 2026-06-03
- Validator version: `wizard_v4_3_primary_object_card_v1`
- Prior art: Claude `.claude/skills/wizard-v43/SKILL.md` (reference only), Codex `.codex/skills/three-council-wizard-v4-3/SKILL.md` (reference only)
