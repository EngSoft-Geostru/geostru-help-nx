---
title: Full workflow — Slope NX
---

# Full workflow

This page follows a real project from start to export, including the advanced options. Work through the **Input → Analysis → Output** panels in order.

## 1. General data

In **Input → General data** you fill in client, subject, designer, date and coordinates (lat/lon). These fields feed the drawing **title block** and the report header. The **Format & scale** card sets sheet, horizontal scale and vertical exaggeration.

## 2. Geometry

- **Topographic profile**: the ground line, by points (X, Z), drawn, imported from DXF or traced from an image. Extend the profile at the sides with **Extend profile** when you need room downhill/uphill (useful for the global stability of walls).
- **Stratigraphic contacts**: the interfaces between layers. Each contact is the **bottom** of a layer; the region below the last contact is the **bedrock**.
- **Domain base level**: the horizontal floor of the model. It is derived automatically from the profile; you can fix it manually.

## 3. Materials

In **Geotechnical materials** you define the soils: γ, γ<sub>sat</sub>, c′, φ′, c<sub>u</sub>, φ<sub>u</sub> and, in the advanced parameters, permeability, elastic modulus, rock parameters and ISO pattern. Assign a material to each region with a **double-click** on the polygon: the region takes the **material colour**, so the assignment is visible at a glance.

## 4. Water table and loads

- **Water table**: the piezometric line. Below the table the slices use the saturated weight and the pore pressure is subtracted at the base (in drained conditions). In a reservoir, water above the ground surface is treated as a load/uplift according to the layer permeability.
- **Distributed loads**: bands of permanent (→ γ<sub>G</sub>) or variable (→ γ<sub>Q</sub>) load. They are dragged into position on the section and increase the weight of the slices within their range.

## 5. Design code and factors

In the **Analysis → Design code and verification** panel choose **NTC 2018**, **EC7-EC8** or **User** and the combination. The partial factors of groups **M** (materials) and **R** (resistance) reduce the parameters and/or the FoS. See **[Design code and partial factors](normativa.md)**.

## 6. Seismic action

Enable **Seismic analysis** for the pseudo-static approach. You can enter k<sub>h</sub>/k<sub>v</sub> manually or compute them to NTC from soil category, topography, nominal life and a<sub>g</sub>. See **[Seismic action](sismica.md)**.

## 7. Retaining structures

Add **RC walls** or **gabions** from the **Retaining structures** panel. The wall is dragged into position; its weight enters the slices and the critical surface does not cross it. With the **connect** option on, the **backfill** behind the wall is modeled as real soil in the calculation. See **[Retaining structures](muri.md)**.

## 8. Method and surface

- **Analysis condition**: drained or undrained.
- **Method**: Bishop, Fellenius, Janbu, Spencer, Morgenstern-Price. See **[Calculation methods](metodi.md)**.
- **Surface shape**: *Circular* (grid of centres, with **Auto-place grid**) or *General* (by points or automatic search).
- **Slices**, **radii per centre** and **design limit FoS** refine the search and the judgment.

## 9. Calculation and results

Press **Calculate**. The **2D section** shows the critical surface and the grid coloured by FoS; **Output** reports the verdict and the first N surfaces. If the calculation fails, an **actionable panel** explains the cause (e.g. grid off the slope, undrained analysis without c<sub>u</sub>) and offers buttons to fix it.

Ask the **AI** to **explain the result** or to **find the measure** (drainage) for the target FoS.

## 10. Views, report and export

Switch to **3D model** for the extrusion, to **Stresses** for the diagrams along the surface, to **Report** for the document. From there you download the **Word report** and export the section. See **[File formats and export](formati.md)**.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Slope%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/slope/docs/en/workflow.md).*
