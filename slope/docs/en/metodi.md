---
title: Calculation methods (LEM) — Slope NX
---

# Calculation methods (LEM)

Slope NX uses the **limit equilibrium method** (LEM): the potentially unstable mass is divided into vertical **slices** and the **factor of safety** (FoS) is sought as the ratio between the available shear strength and the mobilized one along the slip surface.

$$ FoS = \frac{\tau_{f}}{\tau} = \frac{c' + (\sigma - u)\tan\varphi'}{\tau_{mob}} $$

## The five methods

| Method | Equilibrium | Inter-slice forces | Surfaces |
|---|---|---|---|
| **Fellenius** (ordinary) | Moments | Neglected | Circular |
| **Bishop simplified** | Moments | Horizontal only | Circular |
| **Janbu** | Forces | Horizontal only | Any |
| **Spencer** | Forces + moments | Constant inclination | Any |
| **Morgenstern-Price** (GLE) | Forces + moments | Function f(x) | Any |

- **Fellenius** is the most conservative (it neglects inter-slice forces): useful as a quick estimate and a code reference.
- **Bishop simplified** is the standard for **circular** surfaces: accurate and stable, valid when the base does not assume the lever arm = R.
- **Janbu, Spencer, Morgenstern-Price** satisfy more equilibrium equations and are valid for **general** (non-circular) surfaces too. Bishop and Fellenius are allowed for circles only.

!!! note "Analysis condition"
    In **drained** (effective stress) the strength uses c′ and φ′ and the pore pressure u is subtracted at the base. In **undrained** (total stress) the strength is c<sub>u</sub> with φ = 0 and u is **not** subtracted (c<sub>u</sub> already incorporates it). If you choose undrained, make sure the materials have c<sub>u</sub> > 0.

## Surface shape

- **Circular** — the search examines circles centred on the nodes of the **grid of centres**; several radii are tried per centre. **Auto-place grid** puts the grid above the slope's critical zone.
- **General** — a surface of any shape defined by **points**, or found by a **global search** (evolutionary algorithm) that explores the whole domain.

## Admissible surfaces

A surface is discarded if it is not kinematically valid: if it **emerges above the profile** (it would split the mass in two), if it **crosses a retaining structure**, or if it drops **below the bedrock**. If the search finds nothing, the actionable panel explains why.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Slope%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/slope/docs/en/metodi.md).*
