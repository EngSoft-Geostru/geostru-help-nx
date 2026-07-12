---
title: Bearing capacity
---

# Bearing capacity

The ultimate load **q_lim** is the pressure that brings the foundation soil to
failure. Loadcap NX computes it with several methods in parallel, for each ULS
combination, and compares the outcomes.

## The three-term equation

All methods start from the classic form of the ultimate load:

`q_lim = c·N_c·s_c·d_c·i_c + q·N_q·s_q·d_q·i_q + ½·γ·B·N_γ·s_γ·d_γ·i_γ`

where:

- **N_c, N_q, N_γ** — bearing-capacity factors, functions of φ′;
- **s** — **shape** factors (depend on B/L);
- **d** — **depth** factors (depend on D/B);
- **i** — load **inclination** factors;
- **q = γ·H_F** — surcharge at the founding plane (see
  [embedment height](geometria.md#embedment-height-h_f));
- **c** — cohesion (c′ drained, c_u undrained).

## The methods

| Method | Year | Notes |
|---|---|---|
| **Terzaghi** | 1955 | Historical formulation, not-too-deep foundations |
| **Meyerhof** | 1963 | General shape, depth and inclination factors |
| **Hansen** | 1970 | Extends Meyerhof (inclined base and ground) |
| **Vesic** | 1975 | Widely adopted N_γ factors; includes punching |
| **Brinch-Hansen** | — | EC7/EC8 formulation |
| **Meyerhof-Hanna** | 1978 | **Two-layer** soils (weak over strong or vice versa) |
| **Richards** | 1993 | Bearing capacity in **seismic conditions** |

Enable the methods to compare in the **Calculation methods** card. The **governing
result** is the one with the **lowest design resistance** across all methods and
combinations.

!!! tip "Why several methods"
    Different methods adopt different N_γ factors and corrections: comparing them
    gives a measure of the scatter of the result. Meyerhof-Hanna in particular is
    essential when a weak layer overlies a strong one.

## Eccentricity and effective area

With a moment, the load is eccentric. The eccentricity is `e = M / N`. Loadcap
adopts Meyerhof's **effective area** criterion, reducing the dimensions:
`B′ = B − 2·e_B`, `L′ = L − 2·e_L`.

!!! warning "Overturning"
    If the eccentricity exceeds `B/6` the reaction becomes partialised; beyond
    `B/2` the foundation **overturns** and Loadcap flags it. Large eccentricities
    strongly reduce the effective area and hence the bearing capacity.

## Check and safety factor

For each method and combination:

- **Design resistance**: `R_d = q_lim / γ_R,v`;
- **Service stress** at the founding plane `E_d`;
- **Safety factor**: `FS = q_lim / E_d`.

The combination is **verified** when the design resistance is greater than the
action (equivalent to `FS ≥ γ_R,v`).

## Sliding check

Additional check against sliding of the foundation under the horizontal action. It
is triggered when a shear exists (H_x or H_y). The design resistance is:

`R_d = (N·tan δ + a·A′ + E_pd) / γ_R,o`

with **δ** the soil-foundation friction angle, **a** the soil-foundation adhesion,
**A′** the effective area and **E_pd** the lateral passive thrust. The action is
`V_d = √(H_x² + H_y²)`; the check is satisfied when `FS = R_d·γ_R,o / V_d ≥
γ_R,o`.

In the **Sliding check** card (above the Water table) you set:

- **Soil-foundation adhesion a** [kN/m²];
- **Soil-foundation friction angle δ** [°];
- **Passive thrust fraction** [%].

!!! note "Zero values = automatic derivation"
    Leaving **adhesion and δ at 0**, Loadcap derives them from the layer below the
    founding plane (a = layer cohesion, δ = φ′). A **passive thrust fraction of 0**
    excludes the lateral passive thrust (active only for strip and pad footings).
    In undrained analysis δ is set to 0.

## Punching check

For foundations on low-stiffness soils, Loadcap performs the **punching** check
after Vesic, comparing the rigidity index I_r with its critical value I_crit. If
I_r < I_crit, punching failure occurs and is reported in the results.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Loadcap%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/loadcap/docs/en/carico-limite.md).*
