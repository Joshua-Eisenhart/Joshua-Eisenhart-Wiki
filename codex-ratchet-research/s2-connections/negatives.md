# S2 Connections - Negatives

Negatives are first-class test material. They say what standard results and the
round-3 registry forbid before any future card tries to use the layer.

## Kill Tests

- Equal `c1` does not imply equal connection. A Chern class classifies the
  underlying U(1) bundle, not the full connection-with-holonomy object used by
  the registry.
- Same curvature density does not automatically imply same lifted holonomy
  tuple under a pinned chart and convention. Large-gauge and constant-shift
  variants must pass the lifted holonomy vector before aliasing.
- Endpoint-preserving bumps are not killed by topology alone. They are designed
  to survive the Chern row and fail, if they fail, at curvature density or
  annular Stokes rows.
- Matching one or two leaves is not global equality. A finite selected-leaf
  match is killed by expanded leaf holonomy or annular flux if off-anchor leaves
  separate.
- Boundary-conditioned leaf unions are invalid as flux evidence until the cover
  and disintegration rule are well-defined. Invalid conditioning is a failed
  comparison, not a negative result about the connection.

## Designed-Fail Controls

The future discriminator should include controls that deliberately share `c1`
while changing density, deliberately share two leaves while changing off-anchor
holonomy, and deliberately shift lifted holonomy while keeping `F` unchanged.
Those controls prevent the battery from collapsing topology, curvature, and
transport into one word.
