---
title: PyTorch Distributed Training Reference
created: 2026-04-10
updated: 2026-04-16
type: concept
tags: [reference, research, tooling, implementation, runtime, system]
sources:
  - /Users/joshuaeisenhart/wiki/concepts/pytorch-ratchet-build-plan.md
  - /Users/joshuaeisenhart/wiki/concepts/docs-vs-sims-gap-audit.md
  - /Users/joshuaeisenhart/wiki/concepts/quantum-shannon-theory-reference.md
  - /Users/joshuaeisenhart/wiki/concepts/probe-doc-result-map.md
  - /Users/joshuaeisenhart/wiki/raw/articles/new-docs/TODO.md
framing: current
---

# PyTorch Distributed Training Reference

This page is a support/reference note for the distributed-training layer that could sit beneath the repo's PyTorch sims. The current sim surface is mostly local, autograd-heavy, and single-process; this page records how scaling could work if the execution layer moved to multi-process training, sharding, or device-mesh layouts.

## 1. Definition

PyTorch distributed training is the family of execution modes where one logical training job is split across multiple processes, devices, or nodes while preserving a shared model semantics. The main coordination primitives are process groups, collectives, and explicit rank/world-size discipline.

Distributed training is not one thing:
- DDP replicates the model and synchronizes gradients.
- FSDP shards parameters, gradients, and optimizer state.
- Device meshes organize multiple process groups across dimensions.
- Join/uneven-input utilities keep collectives from hanging when ranks exit early.

The relevant question for this wiki is not whether distributed training is "better" in general, but which sim families become admissible under memory, communication, and ordering constraints.

## 2. Key structures

### Process group
A process group is the communication shell that defines which ranks participate in a collective. Everything else depends on this shell being coherent: rank assignment, world size, and backend choice must agree.

### Collectives
Core collectives include all-reduce, reduce-scatter, all-gather, broadcast, barrier, and monitored barrier. These are the execution skeleton for gradient sync and parameter redistribution.

### DDP
DistributedDataParallel is the replication route: every rank holds a full model replica, each rank computes local gradients, and all-reduce makes the gradients agree. DDP is simple and often the first scaling step.

### FSDP
Fully Sharded Data Parallel is the sharding route: parameter shards are materialized only when needed, gradients are reduced in sharded form, and optimizer state is also partitioned. FSDP reduces per-rank memory pressure at the cost of more complex communication.

### Mixed precision and offload
FSDP commonly pairs with mixed precision and optional CPU offload. These are execution controls, not changes to the underlying mathematical object.

### State dict forms
Full, sharded, and local state dicts are different views of the same checkpoint surface. The page that matters is not the size of the checkpoint alone but whether the chosen form preserves loadability, restartability, and rank-local constraints.

## 3. Relevance to this system

The current repo snapshot's PyTorch sims mostly use local tensors, local autograd, and explicit module definitions. That means the cited evidence is about operator structure, channel composition, and gradient behavior, not yet about multi-rank sharding.

Distributed training becomes relevant only if one of these constraints becomes load-bearing:
- model state no longer fits on one device
- a sim family becomes communication-bound rather than compute-bound
- the probe needs rank-local structure with synchronized global updates
- a future torch-native ratchet wants to separate execution locality from model semantics

In the present wiki snapshot, distributed training is a scaling layer, not a proof layer.

## 4. DDP versus FSDP

DDP and FSDP solve different bottlenecks.

DDP:
- easiest to reason about
- keeps a full copy of the model on every rank
- synchronizes gradients after backward
- good when memory is sufficient and the bottleneck is compute or data throughput

FSDP:
- shards model state across ranks
- can wrap submodules or the whole model
- typically needs more care around wrapping policy, auto-wrap boundaries, and checkpoint semantics
- good when per-rank memory is the bottleneck

The cited repo scan does not show evidence that FSDP is already required. It does show that torch modules, autograd, and channel math are load-bearing in a subset of probes. That is a different claim.

## 5. Execution discipline

Distributed training must satisfy ordering discipline:
- all ranks must enter collectives in the same order
- uneven inputs need join-style handling
- async work must be waited on before crossing process-group boundaries
- NCCL requires especially careful device and rank discipline

For this wiki, that means distributed training should be documented as a constrained execution shell, not as a generic performance trick.

## 6. What is already earned

| Claim | Evidence surface | Status |
|---|---|---|
| PyTorch sims exist across many local probe files | `system_v4/probes/*.py` | `exists` |
| No FSDP-specific sim file was found in the repo scan | repo search for `fsdp` / `FSDP` | `exists` |
| The repo has load-bearing torch sims and torch-heavy modules | `sim_torch_channel_composition.py`, `sim_e3nn_ic_invariance.py`, `sim_bridge_to_rhoab_construction.py`, `sim_torch_cz.py` | `exists` |
| The build plan already treats PyTorch as the Axis 0 / ratchet execution surface | `pytorch-ratchet-build-plan` | `exists` |
| Quantum capacity and coherent information are already the information-theory layer beneath the execution surface | `quantum-shannon-theory-reference` | `exists` |
| The docs-vs-sims audit still reports structural gaps between docs and execution | `docs-vs-sims-gap-audit` | `exists` |

## 7. What is still open

1. Which probe families, if any, become memory-limited enough to justify FSDP rather than DDP.
2. Whether sharded execution changes only runtime layout or also changes which sim claims are practical to test.
3. Whether a future multi-rank ratchet should use DDP for simplicity first, then graduate to FSDP only for specific heavy families.
4. Whether device-mesh layouts are needed before FSDP is worth adopting in this repo.
5. Which checkpoint form would best preserve the existing baseline / negative-battery workflow.

## 8. One proposed next lane

If this layer is needed next, the bounded target is: write one minimal distributed proof-of-layout sim that uses DDP only, not FSDP.

Why this lane:
- DDP is the simplest admissible distributed shell
- it tests rank setup, gradient sync, and checkpoint discipline without adding sharding complexity
- it gives a concrete baseline before any FSDP wrapping policy is considered

Proposed target classification: `passes local rerun`

## 9. Optional dependencies

Optional means optional; none of these are required for the current local sim layer.

- NCCL: for CUDA collectives when multi-GPU scaling is actually needed
- Gloo: for CPU collectives or debugging paths
- FSDP2: if the repo ever needs modern sharded wrapping semantics
- DeviceMesh: if a future model wants multi-dimensional parallelism
- torchrun: if process launch needs a standard entrypoint
- checkpoint wrappers: if sharded state needs structured save/load

## Related Pages

- [[pytorch-ratchet-build-plan]] — current torch-native ratchet plan
- [[probe-doc-result-map]] — map from sim families to result artifacts
- [[docs-vs-sims-gap-audit]] — where docs and execution still diverge
- [[migration-registry]] — where PyTorch migration state is tracked
- [[quantum-shannon-theory-reference]] — information-theory layer beneath channel semantics
- [[quantum-computing-applications]] — local operator-level PyTorch use cases
- [[tool-manifest-audit]] — current tool adoption and gaps
- [[cptp-maps-and-channels]] — channel math that distributed execution may carry
