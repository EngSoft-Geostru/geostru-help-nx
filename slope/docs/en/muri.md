---
title: Retaining structures — Slope NX
---

# Retaining structures (walls and gabions)

Slope NX models retaining structures as part of the slope, both in the drawing and in the calculation. You add them from the **Input → Retaining structures** panel.

## RC wall and gabions

- **RC wall**: cantilever with footing, defined by parametric dimensions (height, head/base thicknesses, downhill/uphill toes, footing thickness) and the concrete unit weight.
- **Gabions**: stepped stacked blocks (base × number of rows), with the fill unit weight.

The wall is created from the dialog and **dragged into position** on the section: arm the move with the ✥ icon, then drag; the command disarms itself after the move. The facing direction (downhill on the left or right) sets the orientation.

## Effect in the calculation

- The wall **weight** enters the slices that intersect its footprint.
- The critical surface **does not cross** the wall: it is a rigid body, surfaces go around it.
- For **global stability** it helps to extend the profile downhill/uphill and use **Auto-place grid**, which positions the centres so the circles pass beneath the footing and daylight at the toe.

## Backfill behind the wall

With the **connect the head** option on, the **backfill** soil behind the wall is not just graphics: it is modeled as **real soil** in the calculation. The calculation profile rises in the backfill zone (without double-counting the concrete) and the added volume enters as a layer.

Assign the **backfill material** with a **double-click** on the hatched wedge behind the wall: that material's weight and strength (c′, φ′) enter the calculation where the surface crosses the backfill.

!!! tip "Backfill already at grade"
    If you drew the topographic profile **already at the finished grade** (backfill included in the ground line), leave connect **OFF**: the backfill is already soil and the wedge is not needed.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Slope%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/slope/docs/en/muri.md).*
