---
title: Rational method — Westergaard (rigid)
---

# Rational method — Westergaard (rigid pavements)

The **Westergaard** method is based on the solution of Lagrange's equation for **thin plates**. The pavement is modelled as a **multilayer plate on elastic soil**: the method computes the maximum deflection of the slab under load. It is particularly suited to **rigid pavements**.

## Verification principle

As with Ivanov, the allowable deflection is compared with the computed one:

`FS = f_adm / f_d`

The pavement is **verified** when `FS ≥ 1`. The allowable deflection has the same form as in the Ivanov method: `f_adm = 0.17 − 0.026 · log₁₀(N)`.

## How RPD computes it

RPD solves the multilayer plate with a **double Fourier series**, layer by layer, summing the contributions:

- each layer is characterised by an elastic modulus **E**, a thickness, a Poisson's ratio **ν** (assigned by position: 0.2 for the 1st layer, 0.3 for the 2nd, 0.4 for the following ones) and a coefficient **αK** that links the modulus to the modulus of subgrade reaction (`K = E / αK`);
- the tyre load is distributed over a square area equivalent to the footprint;
- the modulus of subgrade reaction **K** closes the model at the base.

The verification deflection is the one computed **at the surface** (first layer).

## Data required in RPD

| Section | Data |
|---|---|
| Mechanical loads | Tyre footprint diameter, inflation pressure |
| Subgrade properties | **Modulus of subgrade reaction K** (kg/cm³) |
| Layering | For each layer: thickness, **elastic modulus E**, coefficient **αK** |
| Design traffic | Needed for f_adm |

!!! note "Modulus of subgrade reaction K"
    The Westergaard method requires the **modulus of subgrade reaction K** (in *Subgrade properties*) and the **αK** coefficients of the individual layers (in *Layering*).

## Results

In the **Results** tab you find the allowable deflection, the computed one, the safety factor and the verification condition.

!!! tip "When to use it"
    Use Westergaard for **rigid pavements** (concrete slabs); for flexible ones AASHTO 1993 (empirical) or Ivanov (deflection) are more appropriate.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20RPD%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/rpd/docs/en/westergaard.md).*
