# SINDy and Koopman Identification for QIT Engine Research

## Research Status

This is a hypothesis and experimental-method page. It is not Ratchet canon.

PySINDy and PyKoopman are useful because they ask two genuinely different
questions about one dynamical object:

- **PySINDy:** what sparse continuous generator could produce the observed
  local change?
- **PyKoopman/EDMD:** what finite-time linear action on selected observables
  predicts the next observation?

That makes them a promising pair for inspecting a proposed engine. It does not
make them the geometry and entropy ratchets, and agreement between them is not
independent proof when both are trained on the same authored simulation.

## Mathematical Relation

For a continuous system

```text
dx/dt = f(x),          x(t) = Phi^t(x0),
```

SINDy chooses a feature library `Theta(x)` and seeks a sparse coefficient
matrix `Xi`:

```text
X_dot approximately Theta(X) Xi.
```

Its output is a candidate state-space generator `f`.

The Koopman semigroup acts on observables rather than directly on states:

```text
(U^t g)(x) = g(Phi^t(x)).
```

EDMD selects an observable dictionary `psi` and fits a finite matrix `K`:

```text
psi(Y) approximately K psi(X).
```

Its output is a finite-time observable propagator. The infinitesimal Koopman
generator satisfies `L g = f dot grad(g)` under the required regularity. This
is the deep connection between the two views, but taking a matrix logarithm of
a learned finite-time `K` is not automatically a valid recovery of `L`:
spectrum, branch, closure, noise, and sampling assumptions matter.

For an affine Bloch map

```text
x_next = A x + b,
```

the constant observable closes the map exactly:

```text
z = [x, 1]
z_next = [[A, b], [0, 1]] z.
```

This is why the current PyKoopman receipt uses `Identity + EDMD` on an explicit
bias coordinate. It is finite affine system identification, not a theorem that
the physical quantum channel has a finite Koopman-invariant algebra.

## What Each Tool Can And Cannot Test

| Tool | Strong local use | Cannot establish by itself |
|---|---|---|
| PySINDy | sparse terrain vector field; coefficient equivalence; derivative and trajectory falsifiers | CPTP validity, entropy monotonicity, operator-order necessity, stage count |
| PyKoopman EDMD | finite signed beat map; held-out rollout; order/removal/duplication sensitivity | source authority, four-cell emergence, physical closure, useful task semantics |
| exact QIT carrier | Choi/superoperator identity, positivity, trace preservation, entropy and geometry measurements | learned perception or business usefulness |

The right design is triangular: exact carrier truth, generator identification,
and finite-time map identification should constrain each other while retaining
separate failure modes.

## July 9 Local Result

The new local packet is:

```text
/Users/joshuaeisenhart/Codex-Ratchet/system_v7/sims/stage16x4_system_id_instrument_v0/
```

It begins with the 16 source macro slots and the already-conditional four-cell
product cycle. For each slot it rotates both cycle orientations to the slot's
canonical operator and runs all four beats under the slot's one inherited
Axis-6 composition-order sign.

PySINDy receives exact derivatives of each house terrain generator and
reconstructs the time-one affine flow. Those reconstructed flows generate the
training pairs for 128 PyKoopman beat models: 64 maps in each of two candidate
orientations. Held-out targets are produced separately by the exact house
GKSL/channel implementation.

Measured result:

- minimum beat and rollout held-out R2: `1.0`;
- maximum rollout RMSE: `1.729546854431812e-15`;
- macro-map re-identification: `16/16` for both candidate orientations;
- beat removals changing endpoint: `128/128`;
- beat duplications changing endpoint: `128/128`;
- all 32 slot/orientation rows respond to reversal, wrong sign, terrain
  erasure, operator erasure, and all 23 alternate permutations;
- an identity/identity boundary is exactly order insensitive.

A targeted identity-confound audit then clusters the exact maps in both
orientations: full `16`, operator-erased `8`, terrain-erased `4`, and fully
erased `1`. This shows the 16-way result is jointly carried by terrain and the
canonical operator-cycle anchor rather than terrain/sign alone. It was added
after the first green run, so it is post-hoc evidence to preregister and repeat,
not part of the original gate set.

Leviathan FlowMind then regenerated both tool receipts and reran the instrument,
mechanical validator, contract lint, and packet tests as six deterministic gate
nodes. Local receipt: `rcpt-11e35733d5b600cf`, content hash
`315ab19729f84e91dfef8aad1112284c16254ef8f27f15829f631c2975601119`.

The separate active v7 constraint-core harness reruns green at `123/0/0`.
That same run regenerates formation loss `43.546185436758485` because the
trajectory-window PySINDy mean held-out R2 is `-42.54618543675848`. This is a
useful split verdict: execution infrastructure is green; observed-dynamics
handling/perception is not.

This is real local evidence that the concrete candidate architecture runs and
has teeth against its own transition target. It upgrades the 16 x 4 expansion
from independent one-step channels to an identifiable sequential candidate.

## Why This Is Not Yet Perception Or Emergence

The strongest PySINDy result uses analytic `x_dot`. That is an oracle-quality
measurement surface. It does not show that the engine can infer the generator
from noisy sensors, irregular sampling, partial observation, aliases, or
multimodal evidence.

The transition target is also generated by the same declared house maps whose
necessity is being tested. Destructive controls show nonredundancy inside that
model; they do not yet show better maintenance diagnosis, object binding,
prediction, or action selection than ordinary baselines.

Most importantly, four remains supplied:

```text
two source-selected operator axes
x two source-selected channel families
-> four product cells
-> one square cycle modulo reversal.
```

The local system-ID result does not run a geometry ratchet and an entropy
ratchet over a larger candidate set. It therefore cannot say the four
substages emerged.

## Proper Next Battery

1. Generate a declared candidate superset, including extra operator axes,
   families, sides, strengths, duplicates, and identity/commuting controls.
2. Freeze disjoint train, validation, and held-out state/trajectory families.
3. Run geometry-first and entropy-first ratchets independently and in both
   orders. Neither receives a desired survivor count.
4. Intersect stable survivor equivalence classes across seeds and candidate
   enumeration order.
5. Require the learned product of beat maps to match a direct whole-stage fit
   and exact superoperator/Choi composition.
6. Repeat with noisy, partial, irregularly sampled trajectories. Gate absolute
   error, not only improvement over a catastrophic shuffle.
7. Bind the emitted sequence to a frozen SME object task. Remove each survivor
   and require held-out object binding, prediction, or action quality to fall
   against bag-of-fields and ordinary entity-resolution baselines.
8. Only then compare Type-1 and Type-2 error profiles under equal information
   and compute budgets.

## Software Boundary

PySINDy `2.1.0` is compatible with the modern canonical Ratchet stack and has a
green bounded capability receipt. PyKoopman `1.2.1` is older and its package
metadata conflicts with that stack. Only `Identity + EDMD` is admitted.
`Polynomial` is broken against canonical scikit-learn, and NNDMD is untested.

The domain experiment belongs in Codex-Ratchet. Separate upstream source
checkouts are useful for API archaeology and release-locked tests; a new domain
repository would split authority without adding mathematical independence.

## Sources

- [[projects/codex-ratchet/source-intake/sindy-koopman-article-register-2026-07-09]]
- [[projects/codex-ratchet/engine-16x4-axis6-current-state-2026-07-09]]
- [[concepts/dual-ratchet-geometry-entropy-jordan-research-2026-07-09]]
- [[projects/codex-ratchet/qit-lev-operationalization-plan-2026-07-09]]
