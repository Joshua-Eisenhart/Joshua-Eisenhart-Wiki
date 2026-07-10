# Claude Science Packet Tool-Truth Audit - 2026-07-10

Status: noncanonical wiki digest of a Ratchet tool-integration audit.

## Finding

Packet 112's isolated `143 pass / 0 fail / 0 skip` result is a real local
harness event, but it is not evidence that the QIT engines ran.

An AST and result-schema audit of all 144 Python files under
`sims_and_scripts` found:

| import root | files | share |
|---|---:|---:|
| NumPy | 136 | 94.4% |
| SciPy | 66 | 45.8% |
| JAX | 2 | 1.4% |
| Torch | 1 | 0.7% |
| Julia source files | 0 | 0% |

Counts overlap. The estate is more NumPy-heavy than the advisory WebUI's
rough count.

None of the 144 source files declares `TOOL_MANIFEST` or
`TOOL_INTEGRATION_DEPTH`. None of the 72 result JSON files has `tool_calls`,
`claim_path_tools`, either tool declaration, or top-level `all_pass`.

The harness predominantly gates on expected stdout substrings and approximate
regex matches. That can reproduce a script's intended console output. It does
not establish function-level engine use, nonredundant cross-runtime roles, or
demotion when an alleged engine is removed.

## Correct Interpretation

```text
NUMPY_DOMINATED_UNRECEIPTED_EXTERNAL_SCRIPT_ESTATE_NOT_A_REAL_MULTI_ENGINE_RUN
```

This does not make every NumPy calculation false. NumPy and SciPy are useful
for classical controls, fixtures, and narrow numerical diagnostics. The error
is calling a mostly NumPy script collection a running Julia/JAX/PyTorch engine
system.

The packet's ceiling is now:

```text
packet_112_143_0_0_is_a_local_console_harness_rerun_not_evidence_that_qit_or_dual_ratchet_engines_ran
```

## What Counts As An Engine Run

Each claimed tool must identify:

- qualified API/function;
- input and output object;
- positive, boundary, erased, and mutation controls;
- the exact gate affected;
- the demotion when the tool is bypassed;
- source and result hashes;
- a closed result schema and claim ceiling.

The roles should be nonredundant:

- **Julia:** semantic owner for QIT/algebra/dynamics/attractor work using native
  packages, not a translated NumPy mirror.
- **JAX:** x64 batched state, parameter, history, and adversarial sweeps using
  `jit`, `vmap`, linear algebra, and aligned packages.
- **PyTorch:** graph, autograd, or learned perception work only when removing
  it loses a measured capability.
- **SMT/formal:** derive a finite contradiction or countermodel from bound
  structure, never reassert a precomputed Boolean.
- **NumPy/SciPy:** baseline/control unless the claim is specifically classical
  numerical analysis.

Agreement among three translations is reproducibility. It is not three forms
of intelligence unless the roles perform different necessary work.

## Next Build

The next foundation-first card should be a finite probe/behavioral-object
kernel:

1. Julia computes the exact probe quotient, transition graph, behavioral
   partition, and attractor classes.
2. JAX exhaustively batches histories, probe subsets, order mutations, and
   semiconjugacy residuals.
3. PyTorch learns a graph/behavioral proxy and must transfer to held-out states
   and interventions; shuffled labels and erased probes must defeat it.
4. A validator rejects any claim above an instrument/capability anchor.

That would be a real perception/object instrument. It would still not prove
that the source 16-by-4 schedule or a cross-domain attractor is forced.

## Routes

- [[concepts/cross-view-attractor-nominalism-ledger-2026-07-10]]
- [[projects/codex-ratchet/packet-112-canonical-rerun-and-basin-audit-2026-07-10]]
- [[concepts/repo-tool-use-router]]
- [[specs/codex-ratchet/tool-function-receipt-status]]
- [[specs/codex-ratchet/sim-estate-integration-status]]
