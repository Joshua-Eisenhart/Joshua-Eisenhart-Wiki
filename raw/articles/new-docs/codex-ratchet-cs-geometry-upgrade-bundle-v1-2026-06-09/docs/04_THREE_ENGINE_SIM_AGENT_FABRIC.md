# Three-Engine Sim and Agent Fabric

Use Julia, JAX, and PyTorch as redundant sim engines under Codex-Ratchet receipts.

## Roles

- Julia: semantic/proof-side evaluator, finite carrier algebra, nonassociativity, Attractors/basin, interval/reachability/SOS, QIT reference kernels.
- JAX: batched differentiable dynamics, Diffrax/Dynamiqs/NetKet-style sweeps, counterexample search, sharded kernels.
- PyTorch: graph/geometric scorer, PyG/e3nn/message passing, torchode/torchdiffeq, ablation checks.
- Solver lane: cvc5/Z3/finite model checks, UNSAT cores, repair hints.

## Fan-in rule

No engine self-approves. Fan-in admission requires:

```text
code-owned scorer facts
+ proof/witness refs
+ result receipt
+ explicit claim ceiling
+ negatives and boundary tests
```
