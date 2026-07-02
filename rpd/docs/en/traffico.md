---
title: Design traffic (ESAL)
---

# Design traffic (equivalent standard axles)

All methods start from the **design traffic**: the number of **equivalent standard axles** of 8.2 t (ESAL) that will travel on the most loaded lane during the design life. RPD computes it automatically from the data you enter.

## Why "equivalent axles"

Commercial vehicles have different numbers of axles, loads and types. To compare them, the **standard axle** of 82 kN (8.2 t) is used: each real axle is converted into the number of standard axles that produce the **same damage**. Damage grows with the **fourth power** of the load:

`Ceq = (x / y)⁴`  — with *x* the real axle load and *y* = 82 kN.

The **mean equivalence coefficient (Ceq)** weights this conversion over the **traffic spectrum** of the chosen road type (the frequency of the various vehicle types).

## From AADT to cumulative axles

The starting figure is the **AADT** (annual average daily traffic) of the first year. RPD corrects it with:

- the **annual growth rate (r)** over the design life;
- the **percentage of commercial vehicles**;
- the **split by direction of travel** and the **percentage on the design lane**;
- the **wheel-path dispersion coefficient**;
- the **equivalence coefficient Ceq** (traffic spectrum + fourth-power rule).

The result is **N₈.₂,Calc**, the standard axles accumulated over the design life, then compared with the allowable axles in the [AASHTO method](aashto.md). For the rational methods, instead, **N** is used — the number of standard axles **per day** in the last year of the design life, which enters the allowable deflection.

## Data required in RPD

| Field | Meaning |
|---|---|
| AADT | Annual average daily traffic (vehicles/day), 1st year |
| Growth rate r (%) | Annual traffic increase |
| Commercial vehicles (%) | Share of heavy traffic |
| Traffic on the direction of travel (%) | Split between the two directions |
| Commercial vehicles on the design lane (%) | Share on the most loaded lane |
| Wheel-path dispersion coefficient | Reduction for wheel dispersion |
| Standard deviation S₀ | AASHTO only: error on traffic and performance (0.40–0.50) |

!!! note "Road type"
    The **road type** (in *General data*) selects the **traffic spectrum** used for the Ceq calculation. Choose the one matching your infrastructure.

!!! tip "Preliminary sizing"
    In the preliminary stage the pavement catalogues are useful: in Italy the **Italian Catalogue of Road Pavements (CNR, BU 168/95)**.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20RPD%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/rpd/docs/en/traffico.md).*
