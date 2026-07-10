# ClaimGate And Wizard Patch Genealogy - 2026-07-10

## Boundary

`/Users/joshuaeisenhart/Desktop/claimgate archive` is source provenance and
staging. It is not the active Lev repository. Current comparison is against the
clean upstream worktree at commit `6bcb9974e41c3d59bfef5ffc6341fecc99cf7eee`.

## What Survived

Three early evaluator patches were absorbed and later moved into current
`plugins/sim-witness`. Ordered-channel parity, seam receipts, QIT bridging, and
replay repair were adapted upstream rather than copied byte-for-byte. The
constraint battery was independently superseded by a stronger upstream
implementation.

This is real lineage: part of the user's evaluator work reached current Lev.

## What Did Not Survive

- the full ClaimGate package/runtime;
- the old `proof-spec-generator` integration target;
- the stale local `lev-wizard-ratchet` branch;
- the general Wizard v4.3 council runtime;
- the object-card validator as a current Lev runtime;
- signed wave-read and v58 seat-reroute implementations;
- the sequential-shift evaluator and several live receipt patches.

The stale branch is 40 commits ahead and 1,563 behind current upstream. It is
provenance, not a merge base for current work.

## Valuable Design Material

These ideas remain worth a fresh port:

- primary-object cards with forbidden substitutions and repair loops;
- canonical Decision, Failure, and Follow-Up councils;
- explicit role/model binding and MMM slices;
- typed rejection and return edges;
- signed/read-bound provenance checks;
- seat-level timeout, failure, and reroute receipts;
- sequential-statistics admission for stream evidence.

The correct destination is a bounded plugin or application over current
FlowMind, Exec, Eval, and provider contracts. It should not revive the old
ClaimGate subtree.

## Current Runtime Gap

Current Lev has non-authoritative witness evidence, content-address
recomputation, deterministic sensors, `EvalDecision`, world-model discharge,
and `ProofBundle`. The proof-bundle assembly still lacks an observed non-test
production caller. Current Samurai repairs improve executor receipts but do not
make a QIT engine or Wizard runtime.

Related:

- [[projects/leviathan-current/wizard-model-lane-runtime-audit-2026-07-09]]
- [[concepts/leviathan-framework]]
