---
title: Stratigraphy and water table
---

# Stratigraphy and water table

The stratigraphy describes the soil below the founding plane, layer by layer. The
quality of the calculation depends directly on the quality of these parameters.

## Per-layer parameters

Each row of the **Stratigraphy** table has the main fields always visible and the
deformability parameters in the detail panel (arrow on the left).

| Symbol | Unit | Meaning |
|---|---|---|
| **s** | m | Layer thickness |
| **γ** | kN/m³ | Natural unit weight |
| **γ_sat** | kN/m³ | Saturated unit weight (below the water table) |
| **φ′** | ° | Effective shear resistance angle |
| **c′** | kPa | Effective cohesion |
| **c_u** | kPa | Undrained cohesion (total-stress analysis) |
| **E** | kPa | Elastic modulus (elastic and Schmertmann settlements) |
| **E_ed** | kPa | Oedometric modulus (oedometric settlements) |
| **ν** | – | Poisson's ratio |
| **C_s** | – | Secondary consolidation coefficient |
| **C_v** | – | Primary consolidation coefficient (time curve) |
| **N_SPT** | – | SPT blow count (Burland & Burbidge method) |

!!! warning "SI units, case-sensitive"
    Symbols are in SI units and follow scientific conventions: **kPa**, **MPa**,
    **kN/m³**. Be careful not to confuse γ (unit weight, kN/m³) with pressures
    (kPa).

### Which parameters are used for what

- **Bearing capacity**: γ, φ′, c′ (drained) or c_u (undrained).
- **Elastic settlements**: E, ν.
- **Oedometric settlements**: E_ed (and C_v for the time curve, C_s for the
  secondary part).
- **Burland & Burbidge settlements**: N_SPT.

If a layer has `E_ed > 0` it is treated with the oedometric method; without E_ed,
if `E > 0`, with the **Schmertmann** method. See [Settlements](cedimenti.md).

## Paste and import

Filling the stratigraphy by hand is not the only way:

- **Paste** — copy a table from an Excel sheet (or from the desktop grid) and paste
  it: a dialog lets you **map the columns** onto the fields. Layer colours are
  assigned with an **earthy gradient** from light (top) to dark (bottom).
- **Import** — load a stratigraphy in JSON format, typically **exported from
  Dynamic Probing NX** ("Export for Loadcap"), or a `.lcnx` file.

!!! tip "From test data to stratigraphy"
    For a stratigraphy derived from penetration tests, the rigorous interpretation
    belongs to **Dynamic Probing NX**: from there you export the already
    characterised layers (γ, φ′, c_u, E, N_SPT) ready for Loadcap.

## Water table

In the **Water table** card you set:

- **Water table presence** — absent or present;
- **Depth from ground level** — positive below ground level.

The water table governs the calculation of effective stresses (uplift) and,
therefore, both the bearing capacity and the settlements. Below the water table the
**γ_sat** unit weight is used.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Loadcap%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/loadcap/docs/en/stratigrafia.md).*
