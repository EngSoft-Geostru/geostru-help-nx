# Active anchors

Active anchors (pre-stressed tie-rods) apply a pre-load on the wedge as soon as they are installed, regardless of any movement. They follow **NTC 2018 §6.6** with the classical 3-limit + ξ + γ<sub>Ra,t</sub> chain.

## Capacity of the single anchor

Three limits, R<sub>min</sub> = min of the three:

| Limit | Symbol | Formula |
|---|---|---|
| Steel resistance | R<sub>steel</sub> | A<sub>s</sub> · f<sub>yd</sub> · η |
| Bar ↔ grout bond (bond zone only) | R<sub>bond</sub> | π · D<sub>bar</sub> · L<sub>bond</sub> · τ<sub>b</sub> |
| Bulb pull-out | R<sub>pullout</sub> | π · D<sub>bulb</sub> · L<sub>bond</sub> · τ<sub>ult</sub> |

In rock: τ<sub>ult</sub> ≈ 0.1 · σ<sub>c</sub> (Bustamante-Doix 1985).

## Reduction chain

$$R_k = \frac{R_{min}}{\xi}, \quad R_d = \frac{R_k}{\gamma_{Ra,t}}, \quad \text{Capacity} = \frac{R_d}{FS_{local}}$$

| Coefficient | Source | Notes |
|---|---|---|
| ξ | NTC Tab. 6.6.III | conservative fallback ξ=1.4 with 0 pull-out tests; decreases with the number of preliminary pull-out tests (1.4 → 1.3 → 1.2 → 1.1 with ≥4 tests) |
| γ<sub>Ra,t</sub> | NTC §6.6 | **1.10** for temporary anchors, **1.20** for permanent anchors |
| FS<sub>local</sub> | designer | extra local safety factor, default 1.0 |

## ξ table

| no. preliminary pull-out tests | ξ |
|---|---|
| 0 (no test — conservative fallback) | 1.40 |
| 1 | 1.40 |
| 2 | 1.30 |
| 3 | 1.20 |
| ≥4 | 1.10 |

!!! note "Pull-out tests, not boreholes"
    The number of "preliminary pull-out tests" refers to dedicated anchor pull-out tests prior to construction (NTC Tab. 6.6.III). It is **not** the count of geotechnical boreholes (that one applies to piles, Tab. 6.4.IV).

## Input fields

| Field | Notes |
|---|---|
| φ bar [mm] | strand or bar diameter |
| L total [m] | total length (free + bond) |
| L free [m] | free length (no bond), in the wedge |
| L bond [m] | bond length in the intact rock mass |
| φ hole [mm] | borehole diameter |
| z avg [m] | average bulb depth |
| f<sub>yd</sub> [MPa] | design steel resistance |
| η work [%] | steel work rate (typical 60–90% for anchors) |
| τ<sub>b</sub> [N/mm²] | bar↔grout bond stress (typical 1.5–3 N/mm²) |
| no. pull-out tests | for ξ from Tab. 6.6.III |
| γ<sub>Ra,t</sub> | automatically updated when temporary/permanent is changed |

In the right panel **"Design resistances · nails / anchors"** the full ξ / γ<sub>Ra,t</sub> / FS chain is shown step by step.

## Active vs passive

- **Active anchor**: pre-load F applied immediately as an **action** on the wedge. Reduces both the driving shear S and the normal N (via the angle Δ).
- **Passive nail**: no pre-load. Mobilises force only when the wedge tries to move. Adds resistance via the τ resisting term ([see passive nails →](chiodi.md)).

For the same single capacity F, active anchors are slightly more effective (they reduce S directly), but passive nails are simpler to install and don't require tensioning equipment.
