---
title: Slope and substrate
---

# Slope and substrate

SRS NX models the slope as an **overburden** (the potentially unstable
surface layer) resting on a **substrate** (soil or rock) into which the
nails are anchored. This page explains the parameters of the **Slope** and
**Substrate** sections and how SRS uses them to compute the
pre-intervention safety factor **FS₀**.

## Geometric scheme

The scheme below summarises the input geometry: slope inclined at **α**,
surface layer of thickness **S** (measured perpendicular to the slope),
water table within the layer (**S′ = m·S**), anchor dipping **β** below
the horizontal with total length **L_a = L_nc + L_b**, where
**L_nc = S / sin(α+β)** is the non-collaborating length in the surface
layer and **L_b** the bonded (bulb) length in the substrate.

<figure markdown="span">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 400" font-family="sans-serif" font-size="13" role="img" aria-label="Schema geometrico sezione"><polygon points="97.9,364.1 450.1,117.4 480.1,147.4 480.1,394.0 97.9,394.0" fill="#cbbfa5" stroke="#43403a" stroke-width="1" fill-opacity="0.75"/><polygon points="60.0,310.0 412.2,63.4 450.1,117.4 97.9,364.1" fill="#e8dcc3" stroke="#43403a" stroke-width="1.4" fill-opacity="0.95"/><line x1="78.9" y1="337.0" x2="431.2" y2="90.4" stroke="#3c8dd6" stroke-width="1.6" stroke-dasharray="7 5"/><text x="143.9" y="309.9" fill="#3c8dd6" font-size="12" font-style="italic" font-weight="600" transform="rotate(-35.0 143.9 309.9)">S′ = m·S</text><line x1="353.7" y1="144.7" x2="334.7" y2="117.6" stroke="#8a5a00" stroke-width="1.1"/><polygon points="334.7,117.6 340.7,121.2 336.1,124.5" fill="#8a5a00" stroke="#8a5a00" stroke-width="1"/><line x1="353.7" y1="144.7" x2="372.6" y2="171.7" stroke="#8a5a00" stroke-width="1.1"/><polygon points="372.6,171.7 366.6,168.1 371.3,164.8" fill="#8a5a00" stroke="#8a5a00" stroke-width="1"/><text x="353.7" y="138.7" fill="#8a5a00" text-anchor="middle" font-size="12" font-weight="600" transform="rotate(55.0 353.7 144.7)">S</text><line x1="346.5" y1="219.4" x2="431.1" y2="250.2" stroke="#1e5fa8" stroke-width="7"/><line x1="243.2" y1="181.7" x2="431.1" y2="250.2" stroke="#1e5fa8" stroke-width="2.2"/><line x1="238.0" y1="174.4" x2="248.3" y2="189.1" stroke="#43403a" stroke-width="3.5"/><line x1="243.2" y1="181.7" x2="353.2" y2="181.7" stroke="#43403a" stroke-width="1" stroke-dasharray="4 3"/><path d="M 287.2 181.7 A 44 44 0 0 1 284.5 196.8" fill="none" stroke="#43403a" stroke-width="1.1"/><text x="297.2" y="175.7" fill="#43403a" font-size="13" font-style="italic" font-weight="600">β</text><line x1="288.7" y1="217.5" x2="237.0" y2="198.7" stroke="#8a5a00" stroke-width="1.1"/><polygon points="237.0,198.7 244.0,198.2 242.0,203.5" fill="#8a5a00" stroke="#8a5a00" stroke-width="1"/><line x1="288.7" y1="217.5" x2="340.4" y2="236.3" stroke="#8a5a00" stroke-width="1.1"/><polygon points="340.4,236.3 333.4,236.8 335.3,231.4" fill="#8a5a00" stroke="#8a5a00" stroke-width="1"/><text x="288.7" y="211.5" fill="#8a5a00" text-anchor="middle" font-size="12" font-weight="600" transform="rotate(20.0 288.7 217.5)">L<tspan font-size="9" dy="2">nc</tspan></text><line x1="382.7" y1="251.7" x2="340.4" y2="236.3" stroke="#8a5a00" stroke-width="1.1"/><polygon points="340.4,236.3 347.4,235.8 345.4,241.2" fill="#8a5a00" stroke="#8a5a00" stroke-width="1"/><line x1="382.7" y1="251.7" x2="424.9" y2="267.1" stroke="#8a5a00" stroke-width="1.1"/><polygon points="424.9,267.1 418.0,267.6 419.9,262.2" fill="#8a5a00" stroke="#8a5a00" stroke-width="1"/><text x="382.7" y="245.7" fill="#8a5a00" text-anchor="middle" font-size="12" font-weight="600" transform="rotate(20.0 382.7 251.7)">L<tspan font-size="9" dy="2">b</tspan></text><line x1="323.5" y1="253.5" x2="229.5" y2="219.3" stroke="#8a5a00" stroke-width="1.1"/><polygon points="229.5,219.3 236.5,218.8 234.5,224.2" fill="#8a5a00" stroke="#8a5a00" stroke-width="1"/><line x1="323.5" y1="253.5" x2="417.4" y2="287.7" stroke="#8a5a00" stroke-width="1.1"/><polygon points="417.4,287.7 410.4,288.2 412.4,282.9" fill="#8a5a00" stroke="#8a5a00" stroke-width="1"/><text x="323.5" y="247.5" fill="#8a5a00" text-anchor="middle" font-size="12" font-weight="600" transform="rotate(20.0 323.5 253.5)">L<tspan font-size="9" dy="2">a</tspan></text><line x1="177.6" y1="264.0" x2="177.6" y2="312.0" stroke="#43403a" stroke-width="1.8"/><polygon points="177.6,312.0 174.7,305.6 180.4,305.6" fill="#43403a" stroke="#43403a" stroke-width="1"/><text x="184.6" y="308.0" fill="#43403a" font-size="13" font-style="italic" font-weight="600">W</text><line x1="177.6" y1="268.0" x2="129.6" y2="268.0" stroke="#43403a" stroke-width="1.8"/><polygon points="129.6,268.0 135.9,265.1 135.9,270.8" fill="#43403a" stroke="#43403a" stroke-width="1"/><text x="91.6" y="262.0" fill="#43403a" font-size="13" font-style="italic" font-weight="600">k<tspan font-size="9" dy="2">h</tspan><tspan dy="-2">·W</tspan></text><line x1="60.0" y1="310.0" x2="156.0" y2="310.0" stroke="#43403a" stroke-width="1" stroke-dasharray="4 3"/><path d="M 128.0 310.0 A 68 68 0 0 0 115.7 271.0" fill="none" stroke="#43403a" stroke-width="1.1"/><text x="138.0" y="296.0" fill="#43403a" font-size="13" font-style="italic" font-weight="600">α</text></svg>
<figcaption>Typical section: surface layer, substrate, water table and anchor.</figcaption>
</figure>

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
