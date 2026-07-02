# engines/ — real-substrate engines and the cross-validation contract

Four independent numerical routes compute the same 16-stage contract; their
agreement is the validity mechanism (method-artifact exclusion), their
disagreement is a finding. Never widen a tolerance to make a substrate pass.

```
oracle_targets.py     numpy/scipy RK4 oracle  -> targets.json   (the contract)
jax_engine.py         JAX, exact superoperator expm, vmap+jit -> jax_results.json
torch_engine.py       PyTorch, batched matrix_exp (CPU/CUDA)  -> torch_results.json
julia_engine.jl       Julia, LinearAlgebra exp                -> julia_results.json
validate_engines.py   compares every *_results.json to targets; exit 0 = GREEN
```

Contract per stage (t0–t7 × 2 native operators): Bloch vectors of both N01
orders (terrain-first and operator-first), the order gap, plus per-terrain
non-unitality bit and fixed-point z. Derived invariants: 16 distinct stages,
16/16 positive order gaps, the 8/8 fusion split. Tolerances live in
`targets.json` and are part of the contract.

## Laptop setup (macOS)

```bash
cd <bundle>/engines
python3 -m venv .venv && source .venv/bin/activate
pip install numpy scipy "jax[cpu]" torch          # torch: CPU wheel is fine
python3 oracle_targets.py                          # writes targets.json
python3 jax_engine.py && python3 torch_engine.py
python3 validate_engines.py                        # expect GREEN
```

Julia (first run is the test — authored without a Julia runtime available):
```bash
julia -e 'using Pkg; Pkg.add("JSON")'
julia julia_engine.jl
python3 validate_engines.py                        # now validates 3 substrates
```

Verified in this sandbox: numpy oracle + JAX + PyTorch agree (GREEN) — RK4
integration vs two independent matrix-exponential implementations, matching to
1e-6 across all 16 stages. Julia is the remaining route; if it disagrees,
report the numbers rather than adjusting anything.

## Notes that will save you time

- **Float64 is mandatory.** `jax_engine.py` sets `jax_enable_x64` itself; if
  you refactor, keep it — JAX defaults to float32 and will fail the 1e-6
  contract by ~1e-4. Torch uses complex128 explicitly. On GPU, prefer CPU or
  float64-capable devices for the contract run; float32 GPU runs need the
  widened tolerance declared in `targets.json` (1e-3) and must say so.
- **The coherent axis is (1,1,1)/√3 and is load-bearing** (see
  `sims_and_scripts/axis_loadbearing_n01_sim.py`): on the z-axis convention the
  four Fe stages commute exactly with their terrains and 16/16 order
  sensitivity collapses to 12/16. Don't "simplify" H₀ to σz.
- **vec convention is column-stacking** (`vec(ρ) = ρ.T.reshape(4)` in
  numpy/torch, `reshape(transpose(ρ), 4)` in Julia). Mixing conventions
  produces transposed superoperators that still pass CPTP-looking sanity
  checks — the contract will catch it, but check this first if a substrate
  goes RED.
- **Regenerate `targets.json` only from `oracle_targets.py`**, never by hand;
  it is the single source of truth for model constants, and all engines read
  their constants from it (one place to change parameters).
- Scaling up (3-qubit / Cl(0,6) rung): the superoperator design generalizes —
  dims go 4→64, `expm` cost grows, JAX/torch batching becomes the point. The
  contract schema is dimension-agnostic except the Bloch readout, which should
  become a Pauli-basis expectation vector.
