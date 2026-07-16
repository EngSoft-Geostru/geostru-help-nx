---
title: Slope and substrate
---

# Slope and substrate

SRS NX models the slope as an **overburden** (the potentially unstable
surface layer) resting on a **substrate** (soil or rock) into which the
nails are anchored. This page explains the parameters of the **Slope** and
**Substrate** sections and how SRS uses them to compute the
pre-intervention safety factor **FS₀**.

## Slope (overburden)

| Symbol | Parameter | Unit |
|---|---|---|
| I.1 α | Slope inclination | ° |
| I.2 S | Overburden thickness | m |
| I.3 γ_col | Unit weight | kN/m³ |
| I.4 φ_col | Friction angle | ° |
| I.5 c'_col | Drained cohesion | kPa |
| I.6 m | Dimensionless seepage-flow thickness | — |

**m** represents the position of the water table within the overburden:
**m = 0** means no water table, **m = 1** water table at ground level,
intermediate values an intermediate depth. It affects the uplift force and
reduces the available shear resistance.

## Substrate

Choose **Soil** or **Rock** with the two radio buttons: the card shows the
fields relevant to your choice.

### Soil

| Symbol | Parameter | Unit |
|---|---|---|
| I.8 ad_soil | Mortar-soil bond stress | MPa |
| I.9 α_iniez | Injection-mode coefficient | — |

The dropdown next to **ad_soil** suggests typical values by lithology
(basalt, limestone, sandstone, dolomite, schist, weathered schist, gypsum,
slate, or loose soils such as clays, sands and gravels), to be used as a
reference and adjusted based on site data. The **α_iniez** coefficient
distinguishes repeated injection (higher values) from simple injection, for
the same range of loose lithologies.

### Rock

| Symbol | Parameter | Unit |
|---|---|---|
| I.10 ad_rock | Mortar-rock bond stress | MPa |

Same lithology-preset principle as the soil bond stress.

!!! note "Indicative values, not a substitute for site investigation"
    The lithology presets are typical reference values from technical
    literature. The mortar-substrate bond stress used in design must always
    be confirmed by pull-out tests on site or by the mortar/anchor
    manufacturer's data.

## How SRS computes FS₀

Pressing **Calculate FS₀** (card **Design parameters**, step 1), SRS
determines the equilibrium of the overburden wedge tributary to a single
anchor, of plan area equal to the grid spacing **i_x × i_y**:

1. **Acting volume** `V = i_x · i_y · S`
2. **Weight** `W = V · γ_col`
3. **Uplift force** `U = 10 · m · V · cos(α)`
4. **Horizontal seismic force** `F_h = W · K_h` (0 if K_h = 0)
5. **Vertical seismic force** `F_v = F_h / 2`
6. **Resisting shear force** — from cohesion and friction on the sliding
   surface, net of the seismic components
7. **Acting shear force** — the component of weight and seismic forces
   along the slope
8. **FS₀ = resisting force / acting force**

If **FS₀** comes out negative, the slope is already unstable even before
any intervention: check the values you entered.

!!! warning "Update FS₀ after every slope change"
    FS₀ is computed once and stays stored until you recalculate it. If you
    change the overburden's inclination, thickness or geotechnical
    parameters after computing it, press **Calculate FS₀** again before
    running the full check.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20SRS%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/srs/docs/en/pendio.md).*
