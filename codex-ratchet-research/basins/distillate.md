# Basins - Distillate

Use only this bounded extraction for future MMM cards, blind sheets, or sim
prompts.

## MMM Register

`basin` means the initial-condition set that reaches a stated attractor under a
stated evolution rule, phase-space region, and destination criterion.

`attractor` means an invariant destination supported by an attracting
neighborhood, trapping region, attracting block, or positive-measure Milnor
realm. It is not a name the system "wants."

`Conley` means recurrent pieces plus gradient-like complement. It supplies
chain recurrence, attractor-repeller pairs, Morse decompositions, Conley index,
and complete Lyapunov witnesses.

`attractor lattice` means bounded distributive lattice structure over
attractors/attracting neighborhoods. Boolean language is blocked unless the
Booleanization or regular-block assumptions are explicit.

`Milnor basin` means positive-measure attraction. It does not imply open basin,
Lyapunov stability, noise robustness, or clean boundary.

`riddled` means clean local decomposition is blocked: arbitrarily small
neighborhoods contain positive-measure points from a rival basin.

## Basin Criterion In Exclusion Language

A set survives as an attractor iff at least one declared attractor criterion is
met:

- trapping/attracting neighborhood criterion;
- attracting-block criterion;
- isolated invariant set plus the needed Conley/Morse relation;
- positive-measure Milnor realm when the claim is measure-theoretic;
- numerical destination only when explicitly labeled numerical.

Exclude attractor status when the set is merely invariant, merely frequently
visited, merely named by a clustering algorithm, or merely stable under a single
sampled initial condition.

Exclude multiple-basin claims when the control is a generic stable affine or
linear flow. One attracting equilibrium is the expected result; extra basins
mean the sim or labeler introduced something else.

Exclude clean-decomposition claims when riddled, intermingled, Wada, or
unresolved fractal-boundary evidence survives. Keep the obstruction explicit.

Exclude canonical identity when only basin fraction, fixed point, attractor ID,
or destination label matches. Names are labels; equivalence needs the stated
canonicalizer.

Exclude "the system wants" language. The allowed language is: trajectories from
this region converge to, are trapped by, have omega-limit in, have time-average
statistics for, or are assigned by a numerical mapper to a destination.

## Sim Prompt Hooks

- "Run the stable affine fail control; expected output is one basin or a
  degeneracy warning, not multistability."
- "Run the nonlinear multistable contrast; expected output is multiple basins
  with the sampling domain and measure named."
- "Run the gradient control; expected output allows multiple wells but forbids
  cyclic recurrence outside declared recurrent sets."
- "Run the riddled/intermingled control; expected output must lower the claim
  from clean partition to resolution-sensitive or blocked."
- "Run the Conley/interval box route only for certified recurrence/order claims;
  do not use it to assert basin volume unless the volume observable is tested."
- "Run Attractors.jl as numerical basin mapping; record grid, solver, transient
  horizon, sampler, lost trajectories, and boundary diagnostics."

## Promotion Boundary

This distillate is admissible as research-corpus input. It is not a canonical
basin theorem for Codex Ratchet, not a sim result, and not a bridge or axis-level
claim.
