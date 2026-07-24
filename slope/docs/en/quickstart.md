---
title: Quick start — Slope NX
---

# Quick start (5 minutes)

Let's verify a slope from scratch to reading the factor of safety. All you need is the browser and the slope profile.

## 1. Open the app

Go to **[nx.geostru.ai/slope](https://nx.geostru.ai/slope/)**. You can work right away as a guest; to save to the cloud, sign in with your GeoStru account.

On the left you'll find three tabs — **Input**, **Analysis**, **Output** — and on the right the **2D section**, **3D model**, **Stresses** and **Report** views.

## 2. Draw the topographic profile

In the **Input → Topographic profile** panel, enter the ground vertices (X, Z) in the table, or press **Draw** and click the points on the section. Alternatively, import a **DXF** or an image to trace over.

!!! tip "Start from an example"
    No profile at hand? Open the **?** dialog at the top and, in the **Resources** tab, load an **example scenario** (embankment, reservoir, wall): it is ready to calculate.

## 3. Assign the materials

In **Geotechnical materials** press **+ Add material** and set the parameters: unit weight γ, saturated γ<sub>sat</sub>, effective cohesion c′, friction angle φ′ and, for the undrained analysis, the undrained cohesion c<sub>u</sub>.

A slope with no contacts is a **single layer** (the bedrock). For several layers, draw the **stratigraphic contacts** and assign each region its material with a **double-click** on the polygon.

## 4. Water table, loads and seismic (if needed)

- **Water table**: draw the piezometric line in *Water table line*.
- **Loads**: add a distributed load and drag it into position on the section.
- **Seismic**: in the **Analysis** panel, enable the seismic analysis and compute k<sub>h</sub>/k<sub>v</sub> to NTC.

## 5. Choose method and design code

In the **Analysis** panel:

- **Analysis condition**: *Drained* (effective stress) or *Undrained* (total stress). New projects start in Drained.
- **Calculation method**: Bishop, Fellenius, Janbu, Spencer or Morgenstern-Price.
- **Design code**: NTC 2018, EC7-EC8 or User, with the partial factors of the combination.

## 6. Define the surface and calculate

Choose the surface shape:

- **Circular** → press **Automatic search**: the grid of centres places itself above the slope.
- **General** → assign the points or start the automatic search.

Press **Calculate**. In a few moments you see the **critical surface in red** and the **minimum FoS**; the **Output** tab lists the first surfaces by FoS.

!!! tip "Explore the grid"
    Hover over the grid nodes to see each centre's FoS. **Click** pins the surface, **double-click** or **Esc** stops the exploration.

## 7. Read and document

- Open **Output** for the verdict (FoS ≥ threshold = verified) and, with one click, ask the **AI** to explain the result or to **find the measure** (e.g. drainage) to reach the design FoS.
- Open **Report** for the document preview and download it in **Word**.

Done: you have verified your first slope. For the complete picture, continue with the **[Full workflow](workflow.md)**.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Slope%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/slope/docs/en/quickstart.md).*
