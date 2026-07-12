---
title: Foundation and geometry
---

# Foundation and geometry

The **Type and geometry** card defines the shape and placement of the foundation.
The **section preview**, on the right, updates in real time on every change,
without consuming credits.

## Foundation types

| Type | Description | Calculation dimensions |
|---|---|---|
| **Strip** | Continuous strip footing | B (width), L (length) |
| **Pad** | Isolated rectangular footing | B × L |
| **Raft** | Extended slab foundation | B × L |
| **Circular** | Circular footing | radius R (in calc B = L = 2R) |

The chosen type adapts the shape and depth factors and the section drawing (for
strip and pad the column is drawn too; raft and circular are drawn with the
excavation).

## Geometric parameters

| Symbol | Field | Meaning |
|---|---|---|
| **B** | Base | Foundation width [m] |
| **L** | Length | Dimension orthogonal to the section [m] |
| **H** | Height | Thickness/height of the foundation body [m] |
| **D** | Founding depth | Depth of the bearing plane from ground level [m] |
| **R** | Radius | Circular footing only [m] |

### Embedment height H_F

The **embedment height H_F** defines the effective overburden at the founding
plane. When the foundation is not fully confined by the soil (for example a pad
footing with a working excavation that has not been backfilled), the lateral
surcharge that stabilises the failure mechanism is not `γ·D` but only `γ·H_F`.

- Tick **« = founding depth »** for **full embedment**: the surcharge is `γ·D`
  (standard behaviour).
- Untick it and enter **H_F < D** for **partial embedment**: the surcharge reduces
  to `γ·H_F`, on the safe side.

!!! note "Effect on bearing capacity"
    The embedment height acts only on the **surcharge term** (factor N_q). The
    **depth factors** keep using the real depth D.

## Analysis condition: drained or undrained

- **Drained** (effective stress): φ′ and c′ are used. This is the typical
  condition for granular soils and for long-term checks.
- **Undrained** (total stress): φ = 0 and c = c_u. This is the short-term condition
  for saturated cohesive soils.

## Geotechnical parameters in the failure wedge

The **Calculation parameters** option sets how the values of φ′, c′ and γ used in
the formula are obtained:

- **Weighted average of the layers** — average of the parameters of the layers
  involved in the failure wedge, weighted on the thicknesses;
- **Classic method (bearing layer)** — the parameters of the layer the foundation
  rests on are used.

!!! tip "Comparison with the desktop"
    When comparing with desktop calculations, make sure this option is set the same
    way: weighted average and bearing layer can give appreciably different bearing
    capacities in non-uniform stratigraphies.

## Foundation on a slope

If the foundation is close to a slope, set the **slope inclination β** [°] and the
**foundation–slope distance**. The bearing capacity reduces accordingly (reduction
factors on the capacity). The section shows the slope on the relevant side.

!!! note "Convention"
    In Loadcap NX the slope is drawn on the **right** of the foundation, with β
    positive going downhill.

## Colour and rendering

The foundation **colour** is customisable and appears both in the 2D preview and in
the [3D model](stato-tensionale.md).

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Loadcap%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/loadcap/docs/en/geometria.md).*
