# Critical α — sweep

The failure plane dip α is the most influential single parameter for FS. The **α critical search** automatically sweeps α through the kinematically admissible range and finds the value that minimises FS.

## Why

In a real rock mass, the discontinuity that triggers planar failure can have a range of orientations. To bracket the worst case, the designer wants to know:

- the α that gives the lowest FS
- the corresponding FS<sub>min</sub>

If FS<sub>min</sub> ≥ FS<sub>required</sub>, the wedge is safe under all admissible α; if not, the design must be revised.

## How to use it

In the **Block geometry** card, next to the α input, click **`α crit`**. The software:

1. Determines the admissible range: α ∈ (ψ + 0.5°, β − 0.5°)
2. Runs a coarse sweep at 1° steps
3. Refines around the minimum at 0.05° steps
4. Sets the α field to the critical value
5. Recomputes the full model with α = α<sub>crit</sub>

A blue banner shows:

```
α crit ≈ XX.X°  ·  FS_min = X.XXX  (required ≥ X.XX)  ·  range [a°…b°]
```

with colour:

- 🟢 green if FS<sub>min</sub> ≥ FS<sub>required</sub>
- 🟡 yellow if 1.0 ≤ FS<sub>min</sub> < FS<sub>required</sub>
- 🔴 red if FS<sub>min</sub> < 1.0

## Physical meaning

The α<sub>crit</sub> typically lies between φ and (β − some margin). For pure friction (c = 0), the classical result is α<sub>crit</sub> = (β + φ) / 2.

When water, seismic or reinforcement are added, α<sub>crit</sub> can shift significantly. The sweep handles all of them automatically.

## Inadmissible cases

The sweep skips α values that:

- produce a degenerate wedge (area ≤ 0)
- produce a negative resisting τ (unphysical)
- produce a negative FS (unphysical)

If the project has reinforcement (especially R1 meshes), for α very close to β the wedge becomes a thin sliver, the mesh pressure dominates the small W, and the calculation can become unphysical. The sweep filters those points; a warning is shown if no admissible α exists.

[See also the verification page →](verifica.md)
