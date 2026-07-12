---
title: Loads and combinations
---

# Loads and combinations

The **Design loads** card holds the combinations of actions on the foundation.
Each row is a combination, already combined (ULS or SLS), with its partial factors.

## The actions

For each combination you enter, at the **founding plane**:

| Symbol | Unit | Action |
|---|---|---|
| **q** | kN/m² | Design normal pressure (if set, replaces N) |
| **N** | kN | Vertical normal force |
| **M_x**, **M_y** | kN·m | Moments about the x and y axes |
| **H_x**, **H_y** | kN | Shears (horizontal actions) along x and y |

If you assign **q**, the foundation is loaded with a uniform pressure; if you
assign **N** (with any moments), the contact pressure is derived from N and the
eccentricity.

### Sign convention

The **compass** icon in the card header opens the **sign convention** diagram of
the actions: N vertical downward, H_x and H_y the shears along the axes, M_x and
M_y the moments about the x and y axes.

## Design approaches

The **Approach** menu prefills the partial factors according to the standard.
Changing approach updates the factors automatically; if you edit them by hand, the
combination becomes *Custom*.

| Approach | Typical use | γ_R,v (R) |
|---|---|---|
| **A1+M1+R1** | NTC — Approach 2 | 1.0 |
| **A2+M2+R2** | NTC — Approach 1, comb. 2 | 1.8 |
| **A1+M1+R3** | NTC — bearing capacity GEO (R3) | 2.3 |
| **A2+M2+R3** | NTC — R3 variant | 2.3 |
| **DA1-C1 / DA1-C2 / DA2 / DA3** | Eurocode 7 — Design Approach | per EC7 |
| **Seismic** | Seismic combination | 2.3 |
| **SLS** | Serviceability limit state → **settlements** | 1.0 |
| **Custom** | Free factors | — |

!!! note "ULS for bearing capacity, SLS for settlements"
    **ULS/GEO** combinations are used for bearing capacity; **SLS** (service)
    combinations for settlements. A complete project has at least one of each type.

## Partial factors

Each combination carries the partial factors applied to it:

- on the **parameters** (M): γ on tan φ′, on c′ and on c_u;
- on the **weights** (A): γ on the foundation weight and on the overburden weight;
- on the **resistances** (R): γ_R,v on the vertical bearing capacity and γ_R,o on
  the horizontal one (sliding).

The design resistance is `R_d = q_lim / γ_R,v`.

## CSV import

You can import the combinations from a **CSV** file:

- the **CSV template** button downloads an example file, with the sign convention
  reported in the header comments;
- the **CSV** button imports a file (delimiter `;` or `,`, decimals `.` or `,`),
  with columns `description ; approach ; q ; N ; Mx ; My ; Hx ; Hy`.

Approaches allowed in the CSV: `A1M1R1 A2M2R2 A1M1R3 A2M2R3 EC_DA1C1 EC_DA1C2
EC_DA2 EC_DA3 SISMA SLE`.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Loadcap%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/loadcap/docs/en/carichi.md).*
