# Workflow

A real project, from start to report. The steps are in the order you find them on the left; you can go back at any time. Every field is
saved when you leave it and the calculation restarts by itself: the checks on the right always match the data on screen.

## 1. General data and wall type

In the [General data and site](progetto.md) step type description, client, site and designer, pick the site on the map and press **Save**.
In the [Wall type](progetto.md#wall-type) step create the wall with the **guided setup** (type and height), then choose the foundation
(shallow, with shear key, on piles) and the optional parts. The type decides which fields you see: the shear key appears only with the
"With shear key" foundation, the piles only with a piled foundation.

If you start from a desktop project, open it with **File → Open…** (`.mdcx`): see [Files, desktop projects and GeoDropbox](file.md).

## 2. Describe the wall and the soil

- [Geometry](geometria.md): the dimensions of stem and foundation, slopes, shear key, shelves and blinding. Dimensions can also be
  changed with a click on their value in the section.
- [Soils and water table](terreno.md): layers from top to bottom, water table level, ground profile uphill and downhill, backfills.
- [Loads](carichi.md): distributed surcharges on the backfill and point loads.
- [Piles and anchors](pali-tiranti.md): piles (with a piled foundation) and ground anchors.
- [Materials](materiali.md): concrete and steel classes, partial factors, covers, environmental conditions.

## 3. Code and seismic action

In the [Code and seismic action](sisma.md) step choose the geotechnical and structural code and the analysis options (earth pressure
condition and method, passive thrust, bearing capacity). The seismic parameters come from the site coordinates with **Calculate from the
site**; **k_h and k_v from the site parameters (ULS-LS)** writes them into the wall, and from there into the generated seismic combinations.

## 4. Combinations and checks

The [Load combinations](verifiche.md#load-combinations) step shows the combinations generated from the code, read-only. **Customise** copies
them into the project and makes them editable; **Back to the code** regenerates them. The [Checks](verifiche.md) step lists, for every
combination, the safety factors, the partial factors and the **check × combination** summary. A click on a row shows that combination in
the section in the centre (thrusts, pressures, internal forces).

!!! tip "Tip"
    If a global check fails, the lever depends on the check: for **sliding** widen the base or switch to the foundation with shear key; for
    **overturning** lengthen the heel, which carries more stabilising soil; for **bearing capacity** widen the base or reduce the
    eccentricity.

## 5. Reinforcement

The [Reinforcement](armature.md) step shows the bars designed on the envelope of the structural combinations and the bar schedule; below
are the design data for the bars (diameters, minimum and maximum number of bars, distribution bars).

## 6. Report and drawings

In the [Report](relazione.md) step the preview is free. **Generate Word** and **Download the section (DXF)** use credits; a failed operation
is not charged and regenerating the same document with the same data is not charged again.

## 7. Save

The project lives on the server while you work: save it with **File → Save** (`.mdcnx`) or to **GeoDropbox**. An unsaved project is lost
when the session expires.

## What is free

| Action | Cost |
|---|---|
| Modelling, calculation with all checks, drawings and diagrams on screen, report preview | free |
| Word report | NX credits |
| Section in DXF | NX credits |
| Message to the assistant | NX credits |

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20MDC%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mdc/docs/en/workflow.md).*
