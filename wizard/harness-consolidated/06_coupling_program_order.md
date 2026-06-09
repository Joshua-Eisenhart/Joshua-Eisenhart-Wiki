last_updated: 2026-04-16

# Coupling Program Order: Iterative Early Loops, Strict Late-Stage Blocks

The research program has an admission order for late-stage claims. Do not skip steps for emergence, bridge, axis, or engine work. Earlier steps may be revisited iteratively on bounded families.

Hard gate:
- tool sims first
- tool-integration sims next for any nonclassical lane
- then strengthen shell-local parents and bounded pairwise couplings in iterative loops
- widen coexistence/topology only where pairwise behavior is real
- emergence, bridge, axis, and engine claims come last

## Step 1: Shell-local Lego Sims
Which objects (states, operators, probes, entropies) are well-defined in isolation on each candidate shell?

Run independent lego sims on each shell class (spectral shells, geometric shells, etc.) before coupling anything. Do not leave Step 1 globally just because a few shell-local anchors are strong, but you may leave it locally when a bounded family has enough strong parents to make pairwise exploration informative.

## Step 2: Pairwise Coupling Sims
Which shell-local structures remain compatible when two shells run together? Which interact nontrivially?

Small 2-shell tests. Each pairing is a new micro-program.

## Step 3: Multi-shell Coexistence
Small stacking tests: 2-3 shells active at once. Do they survive each other? Does order matter?

This is where simultaneous-shell geometry is tested, not sequential ladders.

## Step 4: Topology-Variant Reruns
Same coupling test as steps 1-3, but with different topology class.

Is the coupling topology-stable or topology-sensitive? Run the same lego coupling on two different topologies and compare.

## Step 5: Emergence Tests
What entropy gradients, probes, or operators only appear when multiple shells run together?

What is genuinely novel in the coupling, not just inherited from shell-local behavior?

## Step 6: Bridge Claims Only
After steps 1-5 are complete: rho_AB (mutual density), Xi (shell overlap), Phi0 (bridge seam), Axis 0 (correlation persistence), and other bridge structures.

**Hard gate:** Do not make bridge, axis, or engine claims before evidence from steps 1-5 exists.

## Operational Gate Definition

Each step has a named admission criterion. The criterion is what admits work to that step; the narrative is not the criterion.

| Step | Admitted when | Excluded while |
|---|---|---|
| Step 1 open | always; tool sims active | — |
| Step 2 open | at least one shell-local lego sim for both shells exists and survives probe | Step 1 incomplete for either shell |
| Step 3 open | at least one pairwise result per proposed shell combination exists as `passes local rerun` | Step 2 incomplete for the proposed combination |
| Step 4 open | Steps 1-3 closed for the family under at least one topology class | — |
| Step 5 open | topology-variant results exist showing coupling is topology-stable or topology-sensitive | Step 4 incomplete |
| Step 6 open | Steps 1-5 closed; emergence results exist and name what is novel vs. inherited | Steps 1-5 not all closed |

**Failure mode to intercept:** a narrative that reframes Step 6 as available because the model extracted a plausible story from the constraint. Proof form: cite the specific step gate criterion and the result file that satisfies it. If the result file cannot be cited, the gate is not satisfied — the narrative is not the gate.

When this gate intercept fires, report: "Step N gate not satisfied; blocking." Do not smooth.

---

## Anti-Patterns

- Launching broad coupling/coexistence claims before the local parents are strong enough for bounded exploration
- Treating "passes test" as "the object is correct" (a survivor is still a candidate)
- Collapsing multiple surviving candidates into one "true" object prematurely
- Using entropy as the master organizing variable (constraints organize first)
- Skipping step 2-4 and jumping to bridge claims

## Cross-references

- See [05_four_sim_kinds.md](05_four_sim_kinds.md) for how to classify sims as you build
- See [07_z3_unsat_primacy.md](07_z3_unsat_primacy.md) for how to use UNSAT as proof of impossibility at each step
- LLM_CONTROLLER_CONTRACT.md (repo) documents the full rationale
