# SRMR (Robertson)

The **Slope Rock Mass Rating** (SRMR, Robertson 1988) is applicable **only to the stability of rock slopes**. It is derived from RMR and was developed by the consulting firm **Steffen Robertson & Kirsten**, starting from the observation that the RMR system, when applied to quarry excavations in weak rock masses with $RMR < 40$, leads to an incorrect estimate of the strength parameters.

$$ SRMR = A_1 + A_2 + A_3 + A_4 $$

where $A_1$ derives from the strength of the intact rock, $A_2$ from RQD, $A_3$ from the spacing of the discontinuities, and $A_4$ from the condition of the discontinuities.

### Value of A1 (intact rock strength)

It is obtained from the point load index $I_s$ or from the uniaxial compressive strength $S_u$ (see [Uniaxial compressive strength $S_u$](classificazioni.md#resistenza-a-compressione-uniassiale-su)).

| $I_s$ (MPa) | $S_u$ (MPa) | $A_1$ |
|---|---|---|
| > 10 | > 250 | 30 |
| 4–10 | 100–250 | 27 |
| 2–4 | 50–100 | 22 |
| 1–2 | 25–50 | 19 |
| (not applicable, use $S_u$) | 5–25 | 17 |
| — | 1–5 | 15 |
| — | 0.6–1 | 10 |
| — | 0.15–0.6 | 6 |
| — | 0.08–0.15 | 2 |
| — | 0.04–0.08 | 1 |
| — | < 0.04 | 0 |

### Value of A2 (RQD)

RQD is obtained from core recovery or, in the absence of borehole cores, it is estimated from the discontinuity survey (see [RQD — Rock Quality Designation](classificazioni.md#rqd-rock-quality-designation)).

| RQD (%) | 90–100 | 75–90 | 50–75 | 25–50 | < 25 |
|---|---|---|---|---|---|
| $A_2$ | 20 | 17 | 13 | 8 | 3 |

### Value of A3 (spacing)

| $s$ (m) | > 2 | 0.6–2 | 0.2–0.6 | 0.06–0.2 | < 0.06 |
|---|---|---|---|---|---|
| $A_3$ | 20 | 15 | 10 | 8 | 5 |

### Value of A4 (condition of the discontinuities)

| Condition | $A_4$ |
|---|---|
| Very rough, discontinuous, closed, unweathered walls | 30 |
| Slightly rough, continuous, aperture < 1 mm, slightly weathered walls | 25 |
| Slightly rough, continuous, aperture < 1 mm, weathered walls | 20 |
| Smooth, planar, continuous, aperture 1–5 mm, infilling < 5 mm | 10 |
| Continuous, aperture > 5 mm, infilling > 5 mm (always apply when $S_u < 1$ MPa) | 0 |

!!! note "The hydraulic factor"
    The factor related to hydraulic conditions is not considered in the calculation, because the amount of water present in the rock mass does not directly affect its strength. However, since it is a destabilising force, water must be introduced as such in the stability analysis.

### Characteristic parameters (SRMR < 40)

For $SRMR < 40$, failure is governed solely by the mechanical characteristics of the rock mass; Robertson assigns the following values, with a further subdivision into classes:

| SRMR | Class | Cohesion (kPa) | Friction angle (°) |
|---|---|---|---|
| 40–35 | IVa | 138 | 40 |
| 35–30 | IVa | 86 | 36 |
| 30–25 | IVb | 50–72 | 30–34 |
| 25–20 | IVb | 50–70 | 26–30 |
| 20–15 | Va | 50–60 | 24–27.5 |
| 15–5 | Vb | 14–50 | 21–24 |

For the bibliographic references, please see the [bibliography](bibliografia.md).

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Rock%20Mechanics%20NX).*
