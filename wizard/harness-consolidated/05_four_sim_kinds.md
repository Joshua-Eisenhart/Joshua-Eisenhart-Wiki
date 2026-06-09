last_updated: 2026-04-16

# Four Sim Kinds

Sims are not all the same. Different structures earn different labels. Confusing them is the core planning error.

## The Four Kinds

### 1. classical
- numpy substrate, coordinate-first
- baseline of what the math object is
- cheap, parallel, decorative by design
- status label: `exists` then `runs` then `passes local rerun` (never `canonical by process`)
- example: eigendecomposition of a density matrix, Hopf coordinates, Carnot cycle

### 2. nonclassical
- same math object, constraint-admissibility framing
- uses language of exclusion, UNSAT, probe-relative indistinguishability
- Nonclassical sims are required once the target is admissibility rather than computation. A nonclassical sim asks: what configurations are excluded by the constraint manifold? A classical sim asks: what is computed on a substrate? These are different questions. Nonclassical is not optional decoration — it is epistemically required for any claim about what can persist under the probe family Π.
- status: can be `exists` / `runs` / `passes`, but **not `canonical by process` alone**
- earns canonical status only if a tool is load-bearing for the admissibility claim (see kind 4)

### 3. tool-capability
- gate-level: does the tool work on this machine?
- z3 solves a SAT instance, clifford composes rotors, pyg propagates messages
- thin, thin, thin
- status: `exists` / `runs` (passes local rerun if the tool's own test suite runs)
- not the real work

### 4. tool-lego-integration
- specific tool applied to a specific lego such that removing the tool breaks the admissibility claim
- the tool is load-bearing for a structural impossibility or derivation or geometric claim on that lego
- this is where depth lives
- earns `canonical by process` because the tool manifest is satisfied, classification is set, and positive/negative/boundary tests all include the tool
- example: z3 UNSAT proof of a Pauli-fence on a nonclassical Hopf lego; clifford composition proving Weyl spinor transport is required

## The Hard Block

**Nonclassical is HARD BLOCKED until both conditions hold:**
1. Tool-capability sims exist and pass locally for each intended tool
2. At least one tool-lego-integration sim exists and passes for a relevant admissibility claim

Do not launch nonclassical coupling programs until integration sims exist for the layers involved.

## Classification Task

When planning a new sim batch, classify every sim into exactly one of these four kinds. A single file is classical OR nonclassical OR capability OR integration, never a mix.

The real backlog is the integration matrix: for each (tool, lego-family) pair, is there an integration sim? Empty cells are the actual work.

## Cross-references

- See [04_status_label_hierarchy.md](04_status_label_hierarchy.md) for what each label requires
- See [06_coupling_program_order.md](06_coupling_program_order.md) for when to start coupling
- See [07_z3_unsat_primacy.md](07_z3_unsat_primacy.md) for why UNSAT is the primacy tool for proof
