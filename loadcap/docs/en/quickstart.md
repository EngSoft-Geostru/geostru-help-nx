---
title: Quick start (5 minutes)
---

# Quick start (5 minutes)

In five minutes you go from opening the app to reading a bearing-capacity check
with settlements. Open **[nx.geostru.ai/loadcap](https://nx.geostru.ai/loadcap/)**
and follow the steps.

!!! tip "Start from an example"
    The fastest way to get familiar is to load an **example project**: menu **?**
    (top) → **Resources** tab → choose, for instance, *Pad footing — NTC 2018*.
    The form fills itself and you can compute right away. See
    [Example projects](esempi.md).

## 1. General data

In the **Parameters** tab, **General data** section, set a project **description**
and the reference **standard** (NTC 2018, Eurocode, or *Free* for all-free fields).

## 2. Foundation geometry

In **Type and geometry** choose the type — **strip, pad, raft, circular** — and
enter the dimensions: base **B**, length **L**, height **H**, founding depth **D**.
On the right the **section preview** updates in real time. See
[Foundation and geometry](geometria.md).

## 3. Stratigraphy and water table

In **Stratigraphy** define the layers (thickness, unit weight **γ**, friction
angle **φ′**, cohesion **c′**, and the deformability parameters). You can **paste**
a table from Excel or **import** a stratigraphy from Dynamic Probing NX. In the
**Water table** card you set presence and depth from ground level. See
[Stratigraphy and water table](stratigrafia.md).

## 4. Loads and combinations

In **Design loads** enter the combinations. For each one choose the **approach**
(which prefills the partial factors) and the loads at the founding plane: pressure
**q**, or **N** with any moments **Mx/My** and shears **Hx/Hy**. ULS combinations
drive the bearing capacity, **SLS** ones drive the settlements. See
[Loads and combinations](carichi.md).

## 5. Calculation methods

In the **Calculation methods** card enable the methods to compare (Terzaghi,
Meyerhof, Hansen, Vesic, Brinch-Hansen, Meyerhof-Hanna). The governing method is
the one with the **lowest design resistance**.

## 6. Compute

Press **Compute** in the top bar. The calculation consumes NX credits.

!!! note "Previews with no charge"
    Previews (2D section, stress state, seismic spectrum, HTML report) update **for
    free**: credits are spent only with **Compute** and when exporting the report.

## 7. Results

Open **Bearing capacity**: for each combination you see, per method, the ultimate
load **q_lim**, the design resistance **R_d = q_lim / γ_R,v**, the service
pressure, the **safety factor** and the outcome **Verified / Not verified**. Where
a horizontal action is present the **sliding check** also appears. See
[Bearing capacity](carico-limite.md).

## 8. Settlements

The **Settlements** tab shows, for the selected service (SLS) combination, the
**elastic** and **oedometric** settlements per layer, the optional **Burland &
Burbidge** estimate and the **time curve**. See [Settlements](cedimenti.md).

## 9. Report and export

From the **Report** menu you generate the calculation document in **Word** or
**PDF**; from the **File** menu you save the project (`.lcnx`). See
[Report and exports](relazione.md).

!!! tip "The AI assistant"
    The **AI assistant** button at the top explains the results, fills the form
    from a report or a test file, and performs a **geotechnical review** of the
    project. See [AI assistant](assistente-ai.md).

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Loadcap%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/loadcap/docs/en/quickstart.md).*
