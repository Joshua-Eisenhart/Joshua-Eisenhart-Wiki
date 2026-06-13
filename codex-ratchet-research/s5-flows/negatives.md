# S5 Flows - Negatives

Negatives are first-class controls for the S5 discriminator.

## Kill Tests

- A single finite step mapping the ball into itself does not prove a valid
  continuous semigroup. The generator must preserve the ball/CPTP condition for
  all `t >= 0` under the declared standard.
- Ball invariance is not complete positivity. A Nagumo/Brezis-style tangent
  condition can support an ordinary flow row while leaving the quantum
  semigroup/GKSL row open.
- Same fixed point is not same flow. Transient rotation, contraction rates, and
  N01 signature can differ while the equilibrium point matches.
- Quotient `56/56` survival is not alias. It is an observed quotient row, not
  the full eight-generator tuple.
- Mirror preservation on one pair does not identify the whole family. The
  Ni/Si rows can still separate even when Se/Ne mirror behavior survives.
- A Hamiltonian-only or rotation-heavy row can preserve purity/shell features
  while failing attractor, basin, or non-unital evidence.

## Designed-Fail Controls

The future battery should include a basin-preserving transient-change null, a
weak shift that passes easy validity but moves the fixed point, and a mirror
preserver that only protects a subset. These controls keep fixed-point,
quotient, mirror, and flow identity separate.
