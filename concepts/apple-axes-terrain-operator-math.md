---

title: Apple Axes Terrain Operator Math
created: 2026-04-07
updated: 2026-04-08
type: concept
framing: legacy
priming: false
tags: [reference, research, validation, system]
sources:
  - raw/articles/system-v5-reference-docs/apple axes terrain operator math.md
---

# Apple Axes Terrain Operator Math

## Overview

## Inward / Type 1 Terrains

- | Type | Terrain | Code | Equation |
- | Type 1 | Funnel | `Se-IN` | \(\dot\rho=\sum_k D_{L^{Se,\mathrm{in}}_k}(\rho)-i\,\varepsilon_{Se,\mathrm{in}}[H_0,\rho]\) |
- | Type 1 | Vortex | `Ne-IN` | \(\dot\rho=-i[H_0,\rho]+\varepsilon_{Ne,\mathrm{in}}\sum_k D_{L^{Ne,\mathrm{in}}_k}(\rho)\) |
- | Type 1 | Pit | `Ni-IN` | \(\dot\rho=D_{L^{Ni,\mathrm{in}}}(\rho)-i\,\varepsilon_{Ni,\mathrm{in}}[H_0,\rho]\) |
- | Type 1 | Hill | `Si-IN` | \(\dot\rho=-i[H_C^{\mathrm{in}},\rho]+\sum_j \kappa_j^{\mathrm{in}}\left(P_j^{\mathrm{in}}\rho P_j^{\mathrm{in}}-\frac12(P_j^{\mathrm{in}}\rho+\rho P_j^{\mathrm{in}})\right)\), with \([H_C^{\mathrm{in}},P_j^{\mathrm{in}}]=0\) |

## Outward / Type 2 Terrains

- | Type | Terrain | Code | Equation |
- | Type 2 | Cannon | `Se-OUT` | \(\dot\rho=\sum_k D_{L^{Se,\mathrm{out}}_k}(\rho)+i\,\varepsilon_{Se,\mathrm{out}}[H_0,\rho]\) |
- | Type 2 | Spiral | `Ne-OUT` | \(\dot\rho=+i[H_0,\rho]+\varepsilon_{Ne,\mathrm{out}}\sum_k D_{L^{Ne,\mathrm{out}}_k}(\rho)\) |
- | Type 2 | Source | `Ni-OUT` | \(\dot\rho=D_{L^{Ni,\mathrm{out}}}(\rho)+i\,\varepsilon_{Ni,\mathrm{out}}[H_0,\rho]\) |
- | Type 2 | Citadel | `Si-OUT` | \(\dot\rho=+i[H_C^{\mathrm{out}},\rho]+\sum_j \kappa_j^{\mathrm{out}}\left(P_j^{\mathrm{out}}\rho P_j^{\mathrm{out}}-\frac12(P_j^{\mathrm{out}}\rho+\rho P_j^{\mathrm{out}})\right)\), with \([H_C^{\mathrm{out}},P_j^{\mathrm{out}}]=0\) |

## Related pages
- [[terrain-laws-and-loop-geometry]]
- [[engine-64-schedule-atlas]]
- [[axis-and-entropy-reference]]
