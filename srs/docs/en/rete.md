---
title: Facing mesh
---

# Facing mesh

The **facing mesh** distributes the anchors' reaction over the slope: it
restrains the overburden between one nail and the next, and is checked
against tension and punching at the anchor head. The **Mesh** section
defines its properties.

## Parameters

| Parameter | Description | Unit |
|---|---|---|
| Mesh | Mesh opening size (e.g. "6x8") | mm |
| Wire | Wire diameter (e.g. "2.70") | mm |
| I.25 γ_rete | Mesh resistance reduction coefficient | — |
| I.23 R_tr | Mesh unit tension resistance | kN/m |
| I.24 R_punz | Mesh punching resistance | kN |
| Mesh cost | Mesh cost, used for the cost estimate | €/m² |

**Mesh** and **Wire** are descriptive (they appear in the report) and don't
enter the check formulas directly: the values that matter for the
calculation are the two resistances **R_tr** and **R_punz**, taken from the
mesh manufacturer's technical data sheet.

## How they are used

SRS applies the **γ_rete** coefficient to the two characteristic
resistances to obtain the design resistances:

- **Design punching resistance** `R_punz,des = R_punz / γ_rete`
- **Design tension resistance** `R_tr,des = R_tr / γ_rete`

These design resistances are compared, respectively, against check **R.6
Mesh punching** and **R.7 Mesh tension** (see [Design checks](verifiche.md)).
With **γ_rete = 1.0** (default) the design resistances equal the
characteristic catalog values.

!!! note "A section independent of the other checks"
    Unlike the bar and mortar parameters, the mesh fields don't require the
    "verified fields" validation of the other sections: you can edit them
    and see the effect on checks R.6/R.7 without having to re-enter the
    whole project.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20SRS%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/srs/docs/en/rete.md).*
