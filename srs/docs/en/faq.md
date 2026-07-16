---
title: Frequently asked questions
---

# Frequently asked questions

## What's the difference between a nail and a tie-back anchor?

A **nail** (or passive bar) is an unstressed anchor: it develops tension
only as the ground around it deforms, after the mortar is grouted. A
**tie-back anchor** is instead pre-stressed with a jack right after
installation, applying a known force from the start. SRS NX designs passive
nails (soil nailing): the tension force required from the anchor is the one
needed to bring the slope from FS₀ to FS_des, not a pre-load set by the
designer.

## The calculation gives a negative FS₀. What does it mean?

It means the slope is **already unstable as-is**, before any intervention:
the acting shear force exceeds the resisting one. Check the overburden's
geotechnical parameters (especially φ_col and c'_col) and the inclination
α: realistic values for your site almost always give a positive FS₀, even
if low.

## Do I have to recalculate FS₀ every time?

Yes, if you change a **slope** or **substrate** parameter after already
computing it: FS₀ stays at its previous value until you press **Calculate
FS₀** again. The full calculation (**Start**/**Calculate**) first checks
that FS₀ is consistent with the current data.

## R_ck or f_ck: which one do I enter?

It depends on the **design code** you chose. With **NTC 2018** enter the
cubic compressive strength **R_ck**, which SRS converts to cylindrical
strength f_ck with the 0.83 factor. With **Eurocode** the field becomes
**f_ck** directly (no conversion: EC2 already works in cylindrical
strength). See [Nails and anchors](chiodi.md#grouting-mortar).

## A check is not satisfied: what do I change?

Every failed check shows a specific hint in the results card. In general:
**R.2/R.3** (bar) are solved by increasing the bar diameter φ_b or the
steel grade; **R.4/R.5** (mortar and bulb) by increasing the length L_a,
the drilling diameter D_f or the mortar strength; **R.6/R.7** (mesh) by
choosing a mesh with higher resistances or reducing the i_x spacing. See
the details in [Design checks](verifiche.md).

## Does the calculation consume credits? And the AI assistant?

Yes. **Calculate** and the **report export** consume NX credits, as does
every message sent to the **AI assistant**. There are no unlimited free
operations: plan your verification calculations around your credit
balance.

## Can the AI assistant replace the designer?

No. The assistant fills in the form from a description, fetches the
seismic coefficient for a location, and explains results, but it does not
verify the geotechnical consistency of the project nor take
responsibility for the calculation. Always review the values it sets
before calculating, and the results before putting them in the report. See
[AI assistant](assistente-ai.md).

## How do I save and reopen a project?

From the **File** menu: **Save** generates an **.srs** file, **Open**
reloads it. Projects can also be kept on **GeoDropbox**. See
[Report and exports](relazione.md#saving-the-project).

## In which languages is SRS NX available?

The app interface is available in **Italian, English, Spanish, Polish,
French and Romanian**. The manual is published in Italian (source) and
English.

---

Didn't find the answer? [Write to us](mailto:info@geostru.ai?subject=Help%20SRS%20NX) — we reply the same day.

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20SRS%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/srs/docs/en/faq.md).*
