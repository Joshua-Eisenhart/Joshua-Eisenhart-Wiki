# S4 Operators - Negatives

Negatives are first-class controls for the S4 discriminator.

## Kill Tests

- Positive is not completely positive. A map can send the Bloch ball into
  itself and still fail as a channel if the Choi matrix is not positive
  semidefinite. Matrix transposition is the standard warning: it preserves the
  Bloch ball as a reflection but is not completely positive.
- Shifted diagonal affine maps need actual Choi or canonical inequality checks.
  A small-looking ellipsoid translation can still fail complete positivity.
- Unital is not non-unital. A weak translation cannot be hidden inside a Pauli
  channel label; `c_exact` and fixed point must be checked.
- Axis relabeling is not alias unless the parent z-probe and N01 roles are
  preserved. A channel can be CPTP under relabeling while still changing the
  tested role.
- Depolarizing similarity is not committed-role equality. Equal isotropic
  contraction or shell behavior does not give the ordered role tuple.
- Composition order matters for noncommuting rotation/dephasing hybrids. A
  dephase-then-rotate row should not be equated with rotate-then-dephase unless
  exact affine matrices agree.

## Designed-Fail Controls

Include a positive-but-not-CP affine candidate, a tiny non-unital shift near a
valid Pauli channel, and an axis-permuted committed row that preserves CPTP but
breaks the parent z-probe role. These controls prevent the S4 battery from
mistaking channel validity for stack identity.
