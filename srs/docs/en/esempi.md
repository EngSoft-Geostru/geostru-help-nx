---
title: Example projects
---

# Example projects

SRS NX ships with two ready-to-use example projects, one for a **soil**
substrate and one for **rock**. In both, the slope is unstable as-is
(FS₀ = 0.5) and the intervention brings it to a design safety factor
FS_des = 1.3: they represent a realistic case where nailing is actually
needed, not just an edge case.

| Example | Substrate | Content |
|---|---|---|
| **Soil example** | Soil (ad_soil = 0.3 MPa) | 35° slope, 1.6 m overburden, GEWI Ø25 nail, R_ck 30 mortar |
| **Rock example** | Rock (ad_rock = 1.0 MPa) | Same slope geometry and same nail, rock substrate |

## How to use them

1. Go to **File → Open** in the toolbar.
2. Download (or select, if already on disk) the `.srs` file of the example
   you want.
3. The form fills itself automatically.
4. Press **Calculate** to re-run the calculation and compare the results.

!!! tip "Compare soil and rock"
    The two examples share the same slope geometry, the same nail and the
    same grid spacing: only the substrate changes. They're a good starting
    point for understanding how much the substrate-mortar bond stress (I.8
    or I.10) affects the R.5 bulb-slip check.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20SRS%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/srs/docs/en/esempi.md).*
