---
title: Stress state and 3D model
---

# Stress state and 3D model

The **Stress state** and **3D model** tabs show how the load spreads into the soil
and how the contact pressure distributes. The previews are generated **without
consuming credits**.

## Stress bulb

The **stress bulb** shows the isolines of the vertical stress increment Δσ produced
by the foundation, computed with the **Boussinesq** solution (Newmark/Fadum
factors). The bulb starts at the **founding plane** (depth D) and is drawn inside
the actual stratigraphic section, with coloured layers and the water table.

With the **combination selector** you choose the load to represent: the assigned
pressure q, or the one derived from N and the eccentricity.

## Colour map

The **colour map** is the same quantity as the bulb rendered as a continuous
gradient **heatmap** (blue to red as Δσ increases), with the vertical-stress
legend. It helps to read the load's influence zone at a glance.

## Contact pressures at the founding plane

The **contact pressures** diagram shows how the soil reacts beneath the foundation,
as a function of the load eccentricity:

- **e ≤ B/6** — **trapezoidal** diagram (the whole base reacts): σ_max and σ_min;
- **B/6 < e < B/2** — **triangular** diagram (partialised reaction);
- **e ≥ B/2** — **overturning**.

The diagram reports σ_max, σ_min, the eccentricity and the outcome.

## 3D model

The **3D model** tab shows the foundation embedded in the layered soil. Available
controls:

- **view mode** — Solid, Transparent (to see the embedded foundation) and
  Excavation (soil as a frame around the footprint);
- **3D bulb** — the Δσ field as translucent stacked shells below the foundation;
- **Moving section plane** — a slider moves a coloured slice along the length L, to
  see how the bulb changes section by section;
- **Rotate** — automatic rotation of the model.

!!! note "The bulb is a 3D field"
    The 2D views of the bulb are sections of the same three-dimensional solid: the
    3D model makes it explicit.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Loadcap%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/loadcap/docs/en/stato-tensionale.md).*
