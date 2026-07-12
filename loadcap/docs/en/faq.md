---
title: FAQ
---

# Frequently asked questions

## The bearing capacity does not match a desktop calculation. Why?

The two most frequent causes, both configurable:

1. **Wedge parameters** — "weighted average of the layers" versus "classic method
   (bearing layer)" give different results in non-uniform stratigraphies. See
   [Foundation and geometry](geometria.md#geotechnical-parameters-in-the-failure-wedge).
2. **Embedment height** — if the surcharge is `γ·H_F` (partial embedment) instead
   of `γ·D`, the N_q term changes. See
   [embedment height](geometria.md#embedment-height-h_f).

Also make sure you enabled the **same methods** and the same condition
(drained/undrained).

## Which calculation method should I use?

Enable several methods and compare them: the governing result is the **lowest
design resistance**. Meyerhof-Hanna is specific to **two-layer soils**; Richards to
**seismic conditions**. See [Bearing capacity](carico-limite.md).

## Are settlements computed with ULS loads?

No: settlements are evaluated with the **service (SLS)** combinations. Make sure you
have at least one SLS combination. See [Settlements](cedimenti.md).

## When does the sliding check appear?

Only when the combination has a **horizontal action** (H_x or H_y ≠ 0). Without a
shear the check is not needed. The parameters (adhesion, δ, passive thrust) are set
in the **Sliding check** card, above the Water table.

## Does the calculation consume credits? And the previews?

**Compute** and the **report export** consume NX credits. Previews (2D section,
stress state, seismic spectrum, HTML report) are **free** and update in real time.

## Can I import the stratigraphy from a penetration test?

Yes. From **Dynamic Probing NX** use "Export for Loadcap" and in Loadcap press
**Import** in the Stratigraphy card. Alternatively, attach the test file to the
**AI assistant**, which derives a draft from it. See
[Stratigraphy and water table](stratigrafia.md#paste-and-import).

## How do I save and reopen a project?

From the **File** menu: **Save** generates a **.lcnx** file, **Open** reloads it.
See [Report and exports](relazione.md#saving-and-geodropbox).

## In which languages is Loadcap NX available?

The app interface is available in **Italian** and **English**.

---

Didn't find the answer? [Write to us](mailto:info@geostru.ai?subject=Help%20Loadcap%20NX) — we reply the same day.

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Loadcap%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/loadcap/docs/en/faq.md).*
