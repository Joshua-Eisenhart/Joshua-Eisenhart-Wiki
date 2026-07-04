---

title: Terrain Math
created: 2026-04-07
updated: 2026-04-08
type: concept
tags: [reference, research, geometry]
sources:
  - raw/articles/system-v5-reference-docs/terrain-math.md
framing: legacy
priming: false
status: superseded
superseded_by: "post-2026-05 current wiki canon"
reason: "dated before 2026-05"
---

# Terrain Math

## Overview

## State Variables

- | spinor | \(\psi_s(\phi,\chi;\eta)=\begin{pmatrix}e^{i(\phi+\chi)}\cos\eta\\ e^{i(\phi-\chi)}\sin\eta\end{pmatrix},\quad s\in\{L,R\}\) |
- | domain | \(\phi,\chi\in[0,2\pi),\quad \eta\in[0,\pi/2]\) |
- | carrier | \(S_s^3=\{\psi_s\in\mathbb C^2:\|\psi_s\|=1\}\) |
- | density | \(\rho_s=\psi_s\psi_s^\dagger\) |
- | density matrix | \(\rho_s(\phi,\chi;\eta)=\begin{pmatrix}\cos^2\eta & e^{2i\chi}\cos\eta\sin\eta\\ e^{-2i\chi}\cos\eta\sin\eta & \sin^2\eta\end{pmatrix}\) |
- | Bloch form | \(\rho_s=\frac12(I+r_x\sigma_x+r_y\sigma_y+r_z\sigma_z)\) |
- | Bloch vector | \(\vec r_s(\phi,\chi;\eta)=\bigl(\sin 2\eta\cos 2\chi,\ \sin 2\eta\sin 2\chi,\ \cos 2\eta\bigr)\) |

## Fixed Matrices

- | \(I\) | \(\begin{pmatrix}1&0\\0&1\end{pmatrix}\) |
- | \(\sigma_x\) | \(\begin{pmatrix}0&1\\1&0\end{pmatrix}\) |
- | \(\sigma_y\) | \(\begin{pmatrix}0&-i\\ i&0\end{pmatrix}\) |

## Related pages
- [[terrain-laws-and-loop-geometry]]
- [[formal-constraints-and-geometry]]
- [[engine-64-schedule-atlas]]
