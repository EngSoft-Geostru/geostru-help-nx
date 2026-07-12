---
title: Seismic action
---

# Seismic action

Loadcap NX reduces the bearing capacity in seismic conditions accounting for both
the **kinematic** effect (on the soil) and the **inertial** effect (on the
structure). The **Seismic action** card adapts to the chosen standard.

## With NTC 2018: full hazard

With **NTC 2018**, the card shows the site seismic hazard:

- **Location** (lat/lon WGS84), **nominal life V_N** and **use class**;
- the table of the **four limit states** (SLO, SLD, SLV, SLC) with `a_g`, `F_0`,
  `T_C*`;
- the **subsoil category** (A…E) and the **topographic category** (T1…T4), which
  determine the amplification coefficients S_S, C_C, S_T;
- the elastic **response spectrum**, drawn in real time.

From these data Loadcap derives the **seismic coefficients**:

- **k_h** (soil) and **k_v** = ±0.5·k_h;
- **k_hi** (structure) = `S_e(T₁) / q`, with period `T₁ = c₁·H^¾`.

!!! tip "Import from GeoStru PS"
    The **Import from GeoStru PS** button reads the text file exported by the
    GeoStru seismic-hazard service and automatically fills location, categories and
    the four limit states.

### Soil and structure: two distinct effects

Under seismic conditions two reductions of the bearing capacity come into play:

- **Kinematic effect (soil)** — due to the acceleration passing through the
  foundation soil; it depends on **k_h**.
- **Inertial effect (structure)** — due to the inertia forces transmitted by the
  superstructure; it depends on **k_hi**, related to the fundamental period T₁ and
  the behaviour factor q.

The **Cascone-Maugeri** method combines the two contributions into a correction
factor on the N_γ term. The dedicated panel in the card explains the difference
between the two coefficients and how they are computed.

!!! note "Fundamental period T₁"
    T₁ is computed as `c₁·H^¾` (c₁ = 0.085 steel · 0.075 r.c. · 0.050 other
    structures) or it can be **assigned** directly.

## With Eurocode / other standards: direct coefficients

With Eurocode 8 or standards other than the NTC, the card shows the **direct
seismic coefficients**: enter k_h, k_v, a_g and k_hi taken from the reference
standard (no spectrum and no GeoStru PS import). Loadcap applies them to the
bearing-capacity factors.

## Effect on the calculation

When the seismic action is active, the bearing-capacity factors (particularly
N_γ) reduce and, consequently, the ultimate load reduces. The
[geotechnical report](relazione.md) includes the "Seismic hazard and actions"
section with the limit-state table and the applied coefficients.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Loadcap%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/loadcap/docs/en/sismica.md).*
