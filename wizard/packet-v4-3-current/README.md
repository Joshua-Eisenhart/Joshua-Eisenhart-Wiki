# Wizard v4.3 Current Packet

authority_status: canonical-runtime-pointer

Wizard v4.3 is a lean, self-contained operational packet for the three-council Wizard runtime, with v4.3-owned MMMs, skills, conformance, and per-LLM adapter boundaries.

The main correction from v4.1 is topology:

- Councils are sequential stages.
- Parent routes are council-member work functions.
- Voices, skills, lanes, guards, and compile fields are child agent roles.
- Management parents supervise liveness and output quality, but do not vote as council members.

## Runtime Boot

When this packet is used as the current Wizard runtime from Hermes, Codex, or Claude, it begins after any required v4.3 object-preservation / maintenance preflight. v4.3 is not a replacement runtime; it records object-preservation and maintenance gate truth before v4.3 councils consume the task.

Main thread:

1. Load `PACKET_MANIFEST_v4_3.md`.
2. Load `mmm/FULL_MMM_v4_3.md` when context allows.
3. If context is tight, load `mmm/COMPACT_MMM_v4_3.md` plus `mmm/mini/MEMBER_MINI_MMM_REGISTRY_v4_3.md`.
4. Load `WIZARD_v4_3.md`.
5. Load `skills/SKILLS_MANIFEST_v4_3.md`.
6. Load the task/source context.

Parent agents:

1. Load compact MMM.
2. Load the parent route mini-MMM.
3. Load the assigned task card.
4. Launch real children for the route.

Child agents:

1. Load compact MMM as universal salience.
2. Load required function-fit mini-MMM slices for the child job type.
3. Load source-language overlay when the job touches Codex Ratchet doctrine, source docs, wiki claims, or MMM compression.
4. Add optional/random voice or lane slices only after required slices are loaded.
5. Run one bounded child role.
6. Return a receipt with required/optional slices and the slice that changed output.

## File Set

- `WIZARD_v4_3.md`: complete operational runtime contract with topology, schemas, task cards, output rules, adapter rules, and audit loop embedded.
- `mmm/FULL_MMM_v4_3.md`: full positive salience surface.
- `mmm/COMPACT_MMM_v4_3.md`: universal compact MMM for parents and children.
- `mmm/mini/MEMBER_MINI_MMM_REGISTRY_v4_3.md`: parent and child mini-MMM registry.
- `skills/`: packet-local operational skills.
- `conformance/validate_v4_3_packet.py`: packet conformance check.
- `agents/`: packet-local agent specifications for parent routes, managers, Wizard loop agents, voices, and auditors.
- `taskcards/`: parent/child/subagent boot rules, schemas, and task-card templates.

The core runtime rules live in `WIZARD_v4_3.md`. Supporting `agents/`, `taskcards/`, `schemas/`, `templates/`, `adapters/`, `skills/`, and `conformance/` files are packet-local support surfaces; they do not replace the core runtime file.

## Non-Goals

This packet is not a log format, not a transcript archive, and not a document farm. Receipts stay internal unless diagnostics are requested.

## Folder/adaptation boundary

`packet-v4-3-current/` is the shared runnable v4.3 packet. Runtime-specific folders such as `../hermes-version-current/` and `../claude-version-current/` adapt this packet to one LLM/system. The shared packet is not itself Hermes, Claude, or Codex.
