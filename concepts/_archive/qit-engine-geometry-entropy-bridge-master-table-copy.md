---

title: QIT Engine Geometry Entropy Bridge Master Table Copy
created: 2026-04-07
updated: 2026-04-08
type: concept
tags: [reference, research, validation, system]
sources:
  - raw/articles/system-v5-reference-docs/QIT_ENGINE_GEOMETRY_ENTROPY_BRIDGE_MASTER_TABLE copy.md
framing: legacy
---

# QIT Engine Geometry Entropy Bridge Master Table Copy

## Overview

# QIT Engine, Geometry, Entropy, and Bridge Master Table

- **Status:** Working support surface. This is not a doctrine rewrite. It is a compact controller/reference table that keeps the current ratchet order explicit and separates live runtime math from still-open bridge math.
- This packet answers four questions in one place:
- 1. what math is already live in the QIT engine
- 2. what geometry is already live in the constraint-manifold ladder
- 3. what entropy math is being processed now
- 4. where the still-open bridge into `Axis 0` begins
- Core separation rule:
- carrier / geometry is not the same thing as the engine
- engine runtime is not the same thing as the final `Axis 0` kernel
- runtime entropy/control math is not the same thing as the final cut-state entropy family

## Related pages
- [[constraint-on-distinguishability]]
- [[entropy-sweep-protocol]]
- [[axis-and-entropy-reference]]
