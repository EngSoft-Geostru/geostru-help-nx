---
title: File formats and export — Slope NX
---

# File formats and export

## Project file `.slope`

The project is saved as a **`.slope`** file (JSON): one file = one slope, with profile, contacts, materials, water table, loads, walls, grid, design code and results (results are recomputed on opening). You save in the **browser** (automatic draft) and as a file with **Save as**.

| Action | Shortcut |
|---|---|
| Save in browser | ++ctrl+s++ |
| Save as (`.slope`) | ++ctrl+shift+s++ |
| Open file | ++ctrl+o++ |
| New project | ++ctrl+n++ |

## Importing the geometry

- **DXF** — topographic profile and, in the multi-layer version, profile + interfaces + water table on separate layers.
- **Raster image** — a section to trace over (draw the profile on top of the image).
- **AI** — load the **PDF of a** Slope desktop **report** or describe the model in words: the assistant reconstructs geometry, materials, water table and structures.

## Export

- **Word report** (`.docx`) — a calculation document with introduction, geotechnical model, factors, method, results and conclusions, generated in the interface language.
- **Section** — the dimensioned 2D view, with an optional title block.
- **GeoSection** — export the stratigraphy to GeoSection NX for the borehole log.

!!! tip "GeoStru cloud"
    With a GeoStru account, projects are saved to **GeoDropbox** and are accessible from the other NX apps.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Slope%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/slope/docs/en/formati.md).*
