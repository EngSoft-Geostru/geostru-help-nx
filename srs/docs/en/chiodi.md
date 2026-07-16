---
title: Nails and anchors
---

# Nails and anchors

The **Anchors** section defines the nail (the cemented passive bar) and how
it is laid out on the slope. You can start from a **commercial catalog** or
enter the parameters **manually**.

## Nail catalog

The **Nail catalog** field lists the available catalogs; selecting one
reveals the **Nail type** field with the list of bars in that catalog, each
with its own diameter. The default catalog collects bar and anchor systems
for nailed mesh, in two families:

- **GEWI** — solid threaded bar, B500B steel.
- **TITAN** — hollow self-drilling bar, with outer and inner diameter,
  designed for loose soils or fractured rock where conventional drilling is
  difficult.

Choosing a nail from the catalog, SRS automatically fills the **bar
diameter φ_b**, the **yield strength f_yk** and the **bar type** (later
shown in the report). You can still correct the values manually after
selecting.

Selecting **-- Manual parameters --** in the Nail catalog field leaves all
fields freely editable: use it for bars not in the catalog, or to check a
solution already defined elsewhere.

## Bar and drilling parameters

| Symbol | Parameter | Unit |
|---|---|---|
| — | Bar type (free description, e.g. B500) | — |
| I.18 φ_b | Bar diameter | mm |
| I.19 f_yk | Bar yield strength | N/mm² |
| I.17 D_f | Drilling diameter | mm |
| I.16 L_a | Anchor length | m |
| I.15 β | Anchor inclination from horizontal | ° |

## Layout on the slope

| Symbol | Parameter | Unit |
|---|---|---|
| I.13 i_y | Vertical grid spacing | m |
| I.14 i_x | Horizontal grid spacing | m |

A tighter grid (smaller i_x, i_y) increases the number of anchors per
100 m² but reduces the tension required from each, because every nail
restrains a smaller overburden wedge (`V = i_x · i_y · S`). See
[Design checks](verifiche.md#anchors-per-100-m2).

## Grouting mortar

| Symbol | Parameter | Unit |
|---|---|---|
| I.20 R_ck (NTC) / f_ck (Eurocode) | Mortar compressive strength | N/mm² |
| I.21 η₁ | Bond coefficient | — |
| I.22 N_prof | Number of geotechnical investigation profiles | — |

With design code **NTC 2018** enter the cubic strength **R_ck**; with
**Eurocode** the field becomes **f_ck** (cylindrical strength, already
direct — no 0.83 conversion). The **η₁** coefficient is **1.00** for good
bar-mortar bond or **0.70** for poor bond (less favourable casting
conditions). **N_prof** (1 to "≥ 5") is the number of geotechnical
investigation verticals available in the area: the more there are, the
lower the reduction coefficient ξ_a4 applied to the bulb pull-out
resistance (see [Design checks](verifiche.md)).

## Design code and partial factors

The **Design code** field, at the top of the **Professional Data and
Project** section, selects the set of partial factors used in every check:

| Design code | γ_s (steel) | γ_Rap (anchors) | γ_Q1 static | γ_Q1 seismic | γ_c (mortar) | R_ck→f_ck |
|---|---|---|---|---|---|---|
| **Eurocode 7/8** (EN 1997 + EN 1998, DA1-C2) | 1.15 | 1.10 | 1.5 | 1.0 | 1.5 | 1.0 |
| **NTC 2018** | 1.15 | 1.20 | 1.5 | 1.0 | 1.5 | 0.83 |
| **User** | customisable | customisable | customisable | customisable | customisable | customisable |

Selecting **User** shows a panel with the six coefficients, all editable:
use it for codes other than NTC 2018 and Eurocode, or for sensitivity
studies.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20SRS%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/srs/docs/en/chiodi.md).*
