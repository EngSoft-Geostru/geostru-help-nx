---
title: Rational method — Ivanov (deflection)
---

# Rational method — Ivanov (deflection)

The **maximum deflection** method (Ivanov) is a rational method that sets up the elastic problem in soils according to Boussinesq. The verification criterion limits the **maximum deflection** produced at the surface at the end of the pavement design life.

## Verification principle

Two deflections are compared:

- **f_adm** — allowable deflection, a function of traffic;
- **f_d** — deflection computed under the tyre load.

The **safety factor** is:

`FS = f_adm / f_d`

The pavement is **verified** when `FS ≥ 1`.

## How RPD computes it

1. **Equivalent elastic modulus (E_eq)** — the multilayer mass is reduced to a single equivalent modulus, iterating **from bottom to top** (subbase → base → binder → wearing course). The subgrade starting modulus is estimated from the CBR: `E₀ = 65 · CBR^0.65`. Each active layer modifies E_eq as a function of its own elastic modulus **E**, its thickness and the radius of the tyre footprint.
2. **Allowable deflection** — `f_adm = 0.17 − 0.026 · log₁₀(N)`, where **N** is the number of standard axles per day in the last year of the design life.
3. **Computed deflection** — `f_d = p · Dp / E_eq`, with **p** the tyre inflation pressure and **Dp** the footprint diameter.

!!! note "Wearing course"
    In the rational calculation you can **exclude the wearing course** (option in *Layering*): in many approaches the wearing course is not considered load-bearing.

## Data required in RPD

| Section | Data |
|---|---|
| Mechanical loads | Tyre footprint diameter (Dp), inflation pressure (p) |
| Subgrade properties | CBR (for E₀) |
| Layering | For each layer: thickness and **elastic modulus E** (kg/cm²) |
| Design traffic | Needed for f_adm (axles/day at end of design life) |

!!! tip "Mechanical loads"
    The *Mechanical loads* fields are used only by the rational methods (Ivanov and Westergaard). With the AASHTO method they remain visible but inactive.

## Results

In the **Results** tab you see the allowable deflection, the computed one, the equivalent modulus E_eq, the number of axles/day and the safety factor, together with the verification condition.

!!! tip "Theoretical background"
    The rational method document can be downloaded from the app (**?** menu → *Resources* → "Rational method — Ivanov").

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20RPD%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/rpd/docs/en/ivanov.md).*
