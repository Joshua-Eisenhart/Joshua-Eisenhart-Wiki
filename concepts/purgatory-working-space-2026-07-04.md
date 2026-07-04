---
title: Purgatory is the working space
created: 2026-07-04
updated: 2026-07-04
type: concept
tags: [purgatory, graveyard, ratchet, doctrine]
status: provisional
---

Worked out in sessions 2026-07-01 to 2026-07-04 (threads running in the Desktop repo clone); salvaged from Claude memory 2026-07-04. Source memory file: feedback_purgatory_is_the_working_space.md.

## Overview

Purgatory is not a holding pen for rejected work. It is the working space itself — the lab where every sim, hypothesis, and object lives while it is built, run, mutated, compared, and graded. The owner's correction: "purgatory is the working space." Work does not happen at the edges of purgatory, trying to get things out of it. Work happens inside it, all the time.

This replaces the older name "graveyard," which wrongly connoted death and finality. Purgatory connotes provisional suspension — held, re-judgeable, not dead.

## The two thin edges, both provisional

Purgatory has two thin edges that rarely fire:

- **Hell** = z3 UNSAT, proven impossible under the current probe/constraint family C.
- **Heaven** = earned-by-process canon, itself still provisional ("a passing candidate is still a candidate").

Owner correction (2026-06-16): "hell is not exactly real either. all things can eventually be got out of purgatory. a=a can eventually be ratcheted." Finality is probe-relative. As the constraint family C grows, what was UNSAT can become admissible later. The rescue mechanism is killed-as-primitive re-derived-as-emergent: `a=a` was killed as a primitive identity, then ratcheted back as `a=a iff a~b`, derived from the probe relation.

UNSAT under the current C is still the primary proof form and the strongest available move — it ends a case within that C. It is not absolute finality across the growth of the model.

## Honest grounding (2026-06-17)

Checked against the corpus: as of 2026-06-17 the word "purgatory" appeared nowhere in `~/wiki` or `~/Codex-Ratchet`. The rename had not propagated; the system still said "graveyard." This is intent, not implementation.

The mechanism is real and on disk in the v4 layer:

- `system_v4/skills/graveyard_router.py` — `GraveyardRecord` and a resurrection interface
- the `graveyard-lawyer` skill (`system_v4/skill_specs/graveyard-lawyer/SKILL.md`, `skills/graveyard_lawyer.py`) — advocates for rejected concepts, `can_only_propose: true`
- `op_graveyard_rescue.py` — the resurrection loop

The rescue ordering in `get_rescue_candidates()` sorts by `(resurrection_attempts, timestamp)` — fewest-failed-attempts-then-oldest — not a likelihood score. "Priest" is not a system term; "lawyer" is. So the rename plus "priest" is intent, not implemented code, and "priest" being new (owner-coined 2026-06-17) is not a gap to flag.

Provenance: the graveyard/rescue/lawyer machinery traces to v3, confirmed from git history at commit `ecee5ea8a`. The active `~/Codex-Ratchet` clone has no `system_v3` because commit `4a1ba4753` untracked it and added it to `.gitignore`. Both repo clones share the same origin, so a clone only pulls tracked files. v3 is recoverable with `git checkout ecee5ea8a -- system_v3`.

## The three-tier extension (2026-07-03)

Owner extension: purgatory is where rejected things work on getting past gates after rejection. Three tiers, never conflated:

- **Hell** — UNSAT, structural impossibility. Permanent, monotone, z3-gated.
- **Purgatory** — gate-rejected but possible. Candidates mutate and re-attempt; this is the churning working population.
- **Heaven / admitted** — earned survivors, still provisional.

## Hallucination as variation, gates as selection

The key design point: wide, wild exploration is the fuel. LLM hallucination and wildness is a feature, not a bug — it is the variation source. Strict code gates are the selection operator. Owner: "this is how life evolves; constraints actually need things bouncing around in them."

Design implication for any ratchet sim: monotone exclusion applies only to hell. Purgatory-to-admitted flux over time is a primary observable — things do get past gates after rework. Generator variance should stay high; gates stay strict. Never narrow the generator to please the gate.

## Related pages

- `project_axis_program_near_complete.md` (Claude memory source; see [[projects/codex-ratchet/wrong-repo-memory-digest-2026-07-04|wrong-repo memory digest]])
- feedback_no_math_canon_mine_old_recent_manifold_is_direction (Claude memory)
- feedback_julia_canon_numpy_banned_v7sims_offcanon (Claude memory)
