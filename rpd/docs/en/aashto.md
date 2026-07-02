---
title: Empirical method AASHTO 1993
---

# Empirical method AASHTO 1993

The empirical method is the one proposed by the *AASHTO Guide for Design of Pavement Structures* (1993), based on the experimental results of the AASHO Road Test. It measures the adequacy of the pavement in terms of the **number of 82 kN (8.2 t) standard axles** the structure can carry, while maintaining the required serviceability, over the design life.

## Verification principle

The check compares two quantities:

- **N₈.₂,Calc** — the standard axles that actually *travel* on the design lane over the design life (see [Design traffic](traffico.md));
- **N₈.₂,Lim** — the standard axles the pavement is able to *carry*.

The **safety factor** is:

`FS = N₈.₂,Lim / N₈.₂,Calc`

The pavement is **verified** when `FS > 1`.

## Structural Number (SN)

The **Structural Number** represents the structural capacity of the package. It is the sum of the contributions of the layers:

`SN = Σ aᵢ · mᵢ · Dᵢ`

where, for each layer *i*:

- **Dᵢ** — thickness, in inches;
- **aᵢ** — structural coefficient (depends on the material);
- **mᵢ** — drainage coefficient (dimensionless; equal to 1 for bituminous mixes).

!!! note "Units"
    In RPD the Structural Number is shown in **inches** (with the cm equivalent next to it). Layer thicknesses, on the other hand, are entered in **cm**.

## The AASHTO equation

The number of allowable axles N₈.₂,Lim is obtained from:

`log₁₀(N₈.₂,Lim) = Z_R·S₀ + 9.36·log₁₀(SN+1) − 0.20 + [log₁₀(ΔPSI / 2.7)] / [0.40 + 1094/(SN+1)^5.19] + 2.32·log₁₀(M_R) − 8.07`

with:

- **Z_R** — standard normal deviate related to the reliability R (see table below);
- **S₀** — standard deviation (error on traffic and performance): 0.40–0.50;
- **ΔPSI = PSI,in − PSI,fin** — allowed serviceability loss;
- **M_R** — resilient modulus of the subgrade, in psi.

### Reliability R and the Z_R coefficient

The reliability R is the probability that the pavement reaches its intended design life. Each R corresponds to a value of Z_R (**negative for R > 50%**):

| R (%) | Z_R |
|---|---|
| 50 | 0.000 |
| 90 | −1.282 |
| 95 | −1.645 |
| 99 | −2.327 |

For intermediate values RPD interpolates linearly.

!!! note "Why is Z_R negative?"
    It is not an error: Z_R is the deviate of the lower tail of the normal distribution. The higher the reliability, the more negative it becomes, and in the term `Z_R·S₀` this makes the design more conservative (higher required SN). With R = 90% → Z_R = −1.282.

### Resilient modulus from CBR

You can enter **M_R** directly or derive it from the **CBR** of the subgrade. In RPD you choose the parameter in *Subgrade properties*; the CBR → M_R conversion is handled by the software.

## Data required in RPD

| Section | Data |
|---|---|
| General data | Design life, reliability R, initial and final PSI |
| Design traffic | AADT, growth rate, % commercial, % lane, standard deviation S₀ |
| Subgrade properties | CBR **or** Resilient modulus |
| Layering | For each layer: thickness, structural coefficient a, drainage coefficient m |

## Results

In the **Results** tab you find the safety factor, the Structural Number, the **allowable axles** (N₈.₂,Lim), the equivalence coefficient, Z_R, ΔPSI and M_R. If the check is not satisfied, the **How to pass the check** card proposes the thicknesses (or the geogrid TBR) required — see [Quick start](quickstart.md).

!!! tip "Theoretical background"
    The full method document can be downloaded from the app (**?** menu → *Resources* → "Empirical method"), or consult the [AASHTO Guide for Design of Pavement Structures](https://habib00ugm.files.wordpress.com/2010/05/aashto1993.pdf). In Italy the practical reference is the **Italian Catalogue of Road Pavements (CNR, BU 168/95)**.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20RPD%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/rpd/docs/en/aashto.md).*
