---

title: Rosetta Terrain Mapping
created: 2026-04-07
updated: 2026-04-08
type: concept
tags: [reference, research, geometry]
sources:
  - raw/articles/system-v5-reference-docs/rosetta-terrain-mapping.md
framing: legacy
priming: false
---

# Rosetta Terrain Mapping

## Overview
- Yes. The clean parse rule is:
- \text{outer token}=\text{UPPERCASE word in the IGT label}
- \text{inner token}=\text{lowercase word in the IGT label}
- So your example is exactly:
- \text{LOSEwin} \Rightarrow \text{outer}= \text{LOSE},\ \text{inner}= \text{win}
- \text{outer LOSE} = TiSe \quad (\text{UP }Ti)
- \text{inner win} = SeFi \quad (\text{DOWN }Fi)

## Math Key

- | Terrain | Math law |
- | `Funnel` | \(X_F^L\) |
- | `Vortex` | \(X_V^L\) |

## Related pages
- [[terrain-laws-and-loop-geometry]]
- [[engine-64-schedule-atlas]]
- [[axis-and-entropy-reference]]
