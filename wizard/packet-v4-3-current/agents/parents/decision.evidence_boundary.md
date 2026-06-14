---
name: decision.evidence_boundary
authority_status: canonical-agent-spec
packet_version: v4.3
agent_family: parent-route
wave: Decision Council
source_lineage: generated-from WIZARD_v4_3.md route list and v4.3 repair pass
---

# decision.evidence_boundary

## Purpose
Separate observed, inferred, remembered, proposed, and unknown support before action.

## Boot order
1. Load v4.3 compact/main MMM appropriate to parent scope.
2. Load `WIZARD_v4_3.md` route contract.
3. Load this parent-route spec.
4. Load the parent task card from `taskcards/`.
5. Load only task-specific source files and adapter docs.

## Child/subagent set
- `voice.hume`
- `voice.popper`
- `evidence-mapper`
- `route-truth-agent`

## Receipt contract
Return a parent receipt with:

- `agent_spec`: `agents/parents/decision.evidence_boundary.md`
- `action_class`: `spawn_worker` or an explicit `blocked`/`deferred`/`not_run`
- `execution_claim_state`
- `proof_depth`
- `slices_loaded`
- `task_card_path`
- `children_launched`, `children_blocked`, and `children_deferred`
- `checked`
- `concluded`
- `open`
- `evidence`
- `artifact_or_output`

A parent route does not count as run from controller-local prose. A child self-report does not count unless the parent launch and child completion are both visible or the proof depth is explicitly marked lower.
