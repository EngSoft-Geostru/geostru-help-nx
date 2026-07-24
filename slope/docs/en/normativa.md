---
title: Design code and partial factors — Slope NX
---

# Design code and partial factors

Slope NX verifies stability against three references, selectable in the **Analysis → Design code and verification** panel.

| Code | Approach |
|---|---|
| **NTC 2018** (D.M. 17/01/2018) | Partial factors at limit states (ULS). |
| **EC7-EC8** (EN 1997) | Design Approach with partial factors. |
| **User** | Free coefficients defined by the designer. |

## Partial factors

The factors are grouped into three groups.

**Group M — materials.** Reduce the design strength parameters:

$$
\tan\varphi'_d = \frac{\tan\varphi'_k}{\gamma_{\varphi'}}, \quad
c'_d = \frac{c'_k}{\gamma_{c'}}, \quad
c_{u,d} = \frac{c_{u,k}}{\gamma_{cu}}
$$

**Group R — global resistance.** Divides the final FoS: FoS<sub>d</sub> = FoS / γ<sub>R</sub>.

**Group A — actions.** γ<sub>G</sub> on permanent, γ<sub>Q</sub> on variable.

## Single-source principle

In slope stability the permanent actions derive from the **soil self-weight**: they are, at the same time, the destabilizing action and the origin of the resistance (friction). By the **single-source principle** the group A factors **do not change** the factor of safety. The verification therefore depends on the **M** and **R** factors.

!!! note "How to read the FoS"
    Applying the partial factors (Limit States), the margin is already incorporated in γ<sub>R</sub>: the verification is satisfied for **FoS ≥ 1.0**. With **characteristic parameters** (traditional method, no reduction) the reference values are **FoS ≈ 1.3–1.5** in static and **1.1–1.3** in seismic conditions.

The **design limit FoS** set in the Analysis panel does not enter the calculation: it governs only the **judgment** (below threshold the FoS is flagged in red).

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Slope%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/slope/docs/en/normativa.md).*
