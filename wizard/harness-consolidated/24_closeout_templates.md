last_updated: 2026-04-18

# Closeout Templates (L5)

Gap #4 of the MMM: the natural closeout shape ("I did X, now Y is done") is rationalist. It presumes forward-pipeline framing, collapses status labels, and admits no probe citation. This file is the manifold-level closeout layer.

Every agent closeout — worker, controller, Hermes, batch-runner — completes into one of the templates below. The templates are written so that completing them admits only nominalist closeout language.

---

## Why a closeout layer

A session ends with a summary. The summary enters the next session as context. If the summary is rationalist, the next session boots rationalist even under nominalist preamble — inter-file context (gap #5) is dominated by closeouts because closeouts are the last thing the model read.

Closeout shape is the highest-leverage hinge between sessions.

---

## The Four Closeout Blocks

Each role uses the block with the matching initial. Block contents are templated; fill in fields but do not rewrite the structure.

### Block S — Sim-worker closeout

```
Probe family M: <cite the probe family name + file path>
Active constraints C: <cite C or reference the constraint set by file>
Status label earned: <one of: exists | runs | passes local rerun | canonical by process>
Result file path: <path cited from this session's filesystem>
Criteria tested: <which of C1..Cn were checked, which were not>
Surviving candidates: <named set, not collapsed to a single winner>
Excluded candidates: <named set with cited exclusion evidence or UNSAT path>
Divergence preserved: <list of candidates still admissible under current C>
Not earned this session: <higher labels or criteria NOT checked>
```

### Block K — Controller closeout

```
Gates cited: <list of gates evaluated + step number from 06_coupling_program_order.md>
Admission decisions: <per gate: admitted | blocked | not evaluated>
Narrative substitutions intercepted: <if any adjacent-stage narratives were pressured and refused>
Worker claims verified: <per worker: which claims were checked against result files>
Worker claims not verified: <what was accepted on report only, if any>
Status label changes to registry: <none | list with cited evidence path>
Blocked actions: <named actions that were refused with gate criterion>
```

### Block H — Hermes closeout

```
Mode entered: <setup-only | launch-authorized>
Mode declared by: <user quote or file reference that authorized launch>
Files staged: <paths, not run>
Files run: <paths with exit code + result file path>
Stage gate read before stage-advancing action: <gate file + what was cited>
Actions refused for setup-only scope: <list>
Handoff state: <what the next session reads to pick up>
```

### Block R — Batch-runner closeout

```
Queue source: <sim_backlog_matrix.md or named queue file>
Queue position worked: <range, not "all" without citation>
Stage gate status per queued sim: <admitted to stage N | blocked at stage N>
Sims run from admitted stage only: <count + paths>
Sims skipped because queue≠permission: <count + reason per>
Queue-is-not-permission intercept fired: <count of times + actions not taken>
Result files produced this batch: <paths>
```

---

## Why These Shapes Are Manifold-Level

The natural closeout is "I did X, now Y is done" — a forward story with collapsed status. That shape is the low-energy path on the training manifold.

The blocks above are the lower-energy path on the shaped context: each field admits only a citation or a named exclusion. A closeout that skips a field reads as incomplete, not as smooth. Completing one of these blocks admits only nominalist closeout language because:

- `Status label earned:` admits one of four labels; "all pass" is excluded
- `Criteria tested:` admits a partition; collapsing to "verified" is excluded
- `Surviving candidates:` admits a set; collapsing to a single winner is excluded
- `Not earned this session:` admits what was NOT shown; omitting it reads as incomplete

A closeout without cited paths reads as incomplete rather than as finished.

---

## Anti-Patterns Excluded by This Layer

- "All sims pass" — excluded; `Criteria tested` partitions, `Status label earned` is singular
- "The next step is X" — excluded; closeout has no "next step" field; stage admission is the controller's gate, not the worker's story
- "Verified by Hermes" — excluded; Block K `Worker claims verified` requires per-claim citation
- "Queue shows X is next, so I ran it" — excluded; Block R `Queue-is-not-permission intercept` requires admission gate evidence
- Ending with a forward-plan paragraph — excluded; no forward-plan field exists

---

## Use at Session Boundary

Closeout is the last assistant message of a session. It becomes the first context fragment of the next session when the next session reads recent history. The closeout block is the transmission channel between manifold-shaped sessions; if the channel is rationalist, manifold depth decays between sessions.

When in doubt: a closeout that fits no block is out of admissible closeout space.

---

## Cross-references

- `21_mimetic_meme_manifold.md` — gap #4 in the "What's Missing" table now closed by this file
- `23_role_boot_templates.md` — L4 role blocks; closeout blocks here match the four roles
- `04_status_label_hierarchy.md` — status ladder cited in Block S
- `06_coupling_program_order.md` — gate criteria cited in Block K
- `17_pre_emit_audit.md` — probe grammar applied during session; this file applies it at exit
