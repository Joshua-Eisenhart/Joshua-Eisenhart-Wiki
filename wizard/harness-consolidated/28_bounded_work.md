last_updated: 2026-04-18

# Bounded Work (L-bound)

The layer that shapes work units so the LLM does not skip ahead.

---

## The Failure Mode

Given a chain of steps with gates between them, the LLM's low-energy completion is to leap to the outcome. "Do step 2" completes into "...and here is also step 3's result, and step 4 looks like..." The model is not ignoring the gates. The model is completing a forward-chain the training manifold made low-energy.

Skip-ahead is the primary operational failure at every scale:

- worker completes the next sim and includes an unsolicited next-sim writeup
- controller declares a gate satisfied because adjacent gates are satisfied
- batch-runner runs a queue row because the previous row ran
- agent generalizes a local result to a broader claim in the same response

The instruction-level fix ("don't skip ahead") is constraint on a model still in a forward-chain-ambient topology. The L-bound fix shapes the work unit itself so that completing it admits only the bound, not the bound plus-one.

---

## The L-bound Principle

> A bounded work unit is a string-shaped artifact that admits completion only within its declared bound, and admits a named refusal at the bound's edge rather than a continuation past it.

A work unit without a declared bound is an open-ended invitation to complete forward. Declaring the bound is how the work unit refuses skip-ahead at the structural level.

---

## Work-Unit Block

Every task spawn (agent dispatch, user instruction with scope, controller hand-off, batch row) is wrapped in the following block:

```
Work unit
---------
Scope: <the single bounded claim or action this unit earns>
In-scope: <list of sub-claims/actions admitted under Scope>
Out-of-scope: <list of adjacent claims/actions explicitly excluded, even if they look natural next steps>
Bound exit condition: <the single result-file path or named refusal that ends this unit>
Skip-ahead refusal shape: if completing Scope suggests a natural next unit, name it and stop — the next unit is a separate work unit, not this one's continuation
```

The block is a shaped sentence. Completing it admits only the Scope; completing "past" it admits only the named refusal.

---

## Why This Shape Is Manifold-Level

The natural forward-chain completion after finishing a task is "...and the next thing to do is..." That completion is rationalist by default.

The block above admits two alternative completions as lower-energy than the forward-chain default:

1. **Scope exit with result-file citation:** "...bound exit condition satisfied: result file at `path`. Work unit closes here."
2. **Scope exit with named refusal:** "...Scope has natural continuation toward `adjacent work unit` which is Out-of-scope under this unit's bound. Skip-ahead refused; next unit requires separate admission."

Neither completion offers a forward chain. The model's low-energy path is to close the unit, not to leap.

---

## Bound Types

Different work units have different admissible bounds:

| Bound type | Scope example | Exit condition |
|---|---|---|
| Single-sim run | "Run `sim_X.py`; record result at `results/X.json`" | result file exists + exit code 0 |
| Single-gate check | "Evaluate coupling-program-order step 2 gate for family F" | per-gate admission decision + cited criterion |
| Single-claim verification | "Verify worker claim `Y` against result file `path`" | match / no-match decision + cited evidence |
| Single-registry edit | "Update `MIGRATION_REGISTRY.md` row `R` to label L if and only if gate `G` is cited from session" | edit applied OR gate-not-satisfied refusal |
| Setup-only | "Stage files for launch; do not execute" | staging manifest; no run |
| Batch row | "Run one row from queue whose stage gate is admitted" | one row run + closeout; queue not advanced |

The work-unit block declares which bound type is in effect.

---

## Role-Specific Anti-Skip-Ahead

Each role has a characteristic skip-ahead shape. The bounded-work block counters the specific shape:

### Worker (sim-runner)
- Skip-ahead shape: writing a "next sim" paragraph after reporting the current sim
- Counter: `Out-of-scope` explicitly lists "next-sim plans, next-sim writeups, next-sim hypotheses"

### Controller
- Skip-ahead shape: declaring an adjacent gate satisfied because a neighbor gate is satisfied
- Counter: `Out-of-scope` names each adjacent gate by ID and excludes inference from neighbors

### Hermes (launch authority)
- Skip-ahead shape: launching beyond the declared setup-only scope
- Counter: `Bound exit condition` = staging manifest; launch is separate work unit requiring separate admission

### Batch-runner
- Skip-ahead shape: running queue row N+1 because row N completed
- Counter: `Out-of-scope` names the next queue row by ID and excludes its execution; queue advancement requires separate admission with cited gate

---

## Construction Test for a Bounded Work Unit

A task prompt is L-bound iff:

1. Scope names a single bounded claim or action.
2. Out-of-scope explicitly lists the adjacent actions that the training manifold's forward-chain completion would reach for.
3. Bound exit condition is a result file path or a named refusal, not "when done."
4. The unit admits a refusal that reads as completion ("bound edge reached, next unit requires separate admission") rather than as failure.

A prompt failing any of these is not L-bound; it is instruction-on-manifold and will leak.

---

## Operational Admission Form

Queues, task lists, and batch plans are admission-pools, not ordered pipelines.

An admission pool is a set of candidate work units. A work unit runs iff its gate is admitted from session-visible evidence. Position in the pool has no admission force.

The admission-pool shape refuses the "ordered list is permission" completion by construction: there is no ordering, so there is no "next."

See `sim_backlog_matrix.md` header (rewritten 2026-04-18) for the operational form.

---

## Interaction with Other Layers

- L0 (`27_ambient_topology.md`) shapes the ambient so that bounded-work blocks read as natural; without L0, bounded-work blocks read as restrictive prose
- L5 (`24_closeout_templates.md`) closes the work unit; the closeout block is the bound exit condition's record
- L-meta (`29_harness_edit_protocol.md`) applies bounded-work to harness editing itself

---

## Failure Modes

- **Implicit bound:** a work unit with no declared bound silently completes forward. If Scope is not named, the unit is not bounded.
- **Bound-creep:** a unit whose Scope was small expands mid-execution to include "natural next steps." The fix is re-entering the bound at the first skip-ahead signal: stop, name the adjacent unit, refuse continuation.
- **Pool as ordered list:** an admission pool that has been mentally re-ordered (even without text reordering) collapses to a pipeline. The fix is to cite the admission gate explicitly every time, not just for the first launch.

---

## Cross-references

- `21_mimetic_meme_manifold.md` — bounded-work is one of the MMM's two primary failure modes
- `06_coupling_program_order.md` — stage gates the bounded-work admits or refuses
- `23_role_boot_templates.md` — role-specific bounded-work shapes embedded in role blocks
- `24_closeout_templates.md` — closeout blocks that close bounded work units
- `27_ambient_topology.md` — L0 layer this file operates on top of
- `LLM_CONTROLLER_CONTRACT.md` — controller intercept rule for narrative substitution (skip-ahead's cousin)
