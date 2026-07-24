---
title: FAQ — Slope NX
---

# Frequently asked questions

## The calculation says "no valid surface". Why?

The typical causes, explained by the actionable panel that appears:

- **Grid of centres off position** relative to the slope → use **Auto-place grid**.
- **Undrained analysis without c<sub>u</sub>**: if the materials have no undrained cohesion, the strength is zero → switch to **Drained** or set c<sub>u</sub>.
- **Profile too short**: surfaces emerge beyond the end → **Extend profile**.

## What's the difference between Drained and Undrained?

**Drained** (effective stress) uses c′ and φ′ and subtracts the pore pressure at the base: it is the **long-term** condition. **Undrained** (total stress) uses c<sub>u</sub> with φ = 0 and does not subtract u: it is the **short-term** condition in fine soils. New projects start in Drained.

## Which method should I choose?

For **circular** surfaces start with **Bishop simplified**. For **general** (non-circular) surfaces use **Janbu**, **Spencer** or **Morgenstern-Price**. **Fellenius** is the most conservative, useful as a reference.

## Why must the FoS be ≥ 1 and not ≥ 1.3?

It depends on the verification method. With **partial factors** (NTC/EC at limit states) the margin is already in γ<sub>R</sub>, so the verification is satisfied for **FoS ≥ 1.0**. With **characteristic parameters** (traditional method) the reference values are FoS ≈ 1.3–1.5 (static) and 1.1–1.3 (seismic). See **[Design code](normativa.md)**.

## How does the calculation treat the backfill behind the wall?

With **connect** on, the backfill is modeled as **real soil**: its weight and strength enter the calculation, with the material you assign by double-clicking the wedge. If instead you drew the profile already at the finished grade, leave connect OFF. See **[Retaining structures](muri.md)**.

## Can I reconstruct a model from an old report?

Yes. Load the report **PDF** (or a description in words) into the **AI** assistant: it reconstructs profile, layers, water table and structures in a preview to review before applying.

## Is my project safe if I close the browser?

Slope NX saves an **automatic draft** in the browser. To avoid losing work, save the **`.slope`** file (or to the cloud with your account). When you open an example or a new file, the app **warns** if there is a project in progress.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Slope%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/slope/docs/en/faq.md).*
