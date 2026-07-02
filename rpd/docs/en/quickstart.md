---
title: Quick start (5 minutes)
---

# Quick start (5 minutes)

In five minutes you go from opening the app to reading a complete verification. Open **[nx.geostru.ai/rpd](https://nx.geostru.ai/rpd/)** and follow the steps.

## 1. General data

In the **Parameters** tab, **General data** section, set:

- a project **description** (optional);
- the **road type** (defines the traffic spectrum);
- the **design life** in years;
- the **reliability R** (%) and the initial and final **service indices (PSI)** — required by the AASHTO method.

## 2. Geometry and 2D/3D preview

Open **Geometry and sections** and enter the number of lanes, widths, shoulders and slopes. On the right, the **cross-section preview** updates in **real time**.

With the **2D / 3D** toggle at the top of the panel you switch from the dimensioned drawing to the **three-dimensional model** of the embankment.

!!! tip "See while you design"
    The preview stays visible at all times: every value you change is reflected in the drawing immediately, without pressing any button.

## 3. Pavement layering

In **Layering** you define the thicknesses (cm) and the coefficients of the layers — **wearing course**, **binder**, **base**, **subbase** — and, if needed, add a **bituminous geogrid** reinforcement. Each layer can be enabled or disabled with the switch next to its name.

## 4. Subgrade and traffic

- In **Subgrade properties** choose the parameter (**CBR** or **Resilient modulus**) and its value.
- In **Design traffic** enter the **AADT** (annual average daily traffic), the growth rate and the percentages of commercial and lane vehicles.

## 5. Calculation method

In the **Calculation method** card choose between:

- **Empirical — AASHTO 1993**
- **Rational — Ivanov** (deflection)
- **Rational — Westergaard** (rigid pavements)

## 6. Results

Open the **Results** tab: the calculation runs automatically. You will see the **safety factor (FS)**, the **Structural Number**, the **allowable axles** and the full table of quantities, with the outcome **Verified** or **Not verified**.

!!! note "Understanding each value"
    Hover over a results row and click the **✨ Explain** icon: the AI assistant explains that parameter using the values of *your* project.

## 7. If it fails: recover with one click

When FS is below 1, the **How to pass the check** card appears with concrete proposals:

- increase the thickness of **one layer** (each chip is clickable: it applies and recomputes);
- or insert a **geogrid** with a given **TBR**.

After applying a solution, the **Undo and choose another solution** bar lets you go back and compare the alternatives.

!!! tip "Optimization"
    If instead the package is **over-designed**, RPD NX proposes to **reduce** a layer while keeping the check satisfied — less material, same safety.

## 8. Report and export

From the **Report** menu you generate the calculation document in **Word** or **PDF**; from the **Export** menu you save the project (`.rpdnx`) or the **cross-section** as SVG. See [File formats and export](formati.md).

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20RPD%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/rpd/docs/en/quickstart.md).*
