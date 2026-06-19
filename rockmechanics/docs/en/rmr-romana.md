# Bieniawski & Romana — RMR and SMR

The classifications of **Bieniawski (1976)** and **Romana (1985)** constitute the most widely used empirical reference for characterising a rock mass when direct information on strength and deformability is scarce. The latter derives from the former, which for slopes was too conservative.

Bieniawski's classification is based on six parameters measured in the field or in the laboratory:

| | Parameter | Meaning |
|---|---|---|
| **A1** | uniaxial compressive strength $S_u$ | strength of the intact rock |
| **A2** | Rock Quality Designation (RQD) | degree of fracturing |
| **A3** | discontinuity spacing | block size |
| **A4** | discontinuity conditions | persistence, aperture, roughness, alteration, infilling |
| **A5** | hydraulic conditions | water inflows |
| **A6** | discontinuity orientation | face/joint correction |

From these the **Rock Mass Rating (RMR)** is obtained and, with Romana's corrections, the **Slope Mass Rating (SMR)**. In practice RMR is differentiated into:

$$ RMR_b = A1 + A2 + A3 + A4 + A5 \qquad RMR_c = RMR_b + A6 $$

that is, **basic RMR** (without orientation) and **corrected RMR**.

## A1 — compressive strength

$S_u$ is obtained from the Point Load Test, the Schmidt hammer or the ISRM estimate: see [common parameters](classificazioni.md#resistenza-a-compressione-uniassiale-su).

From the ISRM Standard, Bieniawski (1989) assigns to A1:

| $S_u$ (MPa) | > 200 | 100–200 | 50–100 | 25–50 | 5–25 | 1–5 | < 1 |
|---|---|---|---|---|---|---|---|
| **A1** | 15 | 12 | 7 | 4 | 2 | 1 | 0 |

If $S_u$ is available from the Point Load test or the Schmidt hammer, the app derives A1 from the **continuous equations** that interpolate Bieniawski's original charts, for ranges of $S_u$: ≤ 44.5 · 44.5–93.75 · 93.75–140 · 140–180 · 180–240 · > 240 MPa (above 240 MPa, $A1 = 15$). The result is continuous and less subjective than reading off the steps.

## A2 — RQD

RQD is obtained from borehole cores or, when these are unavailable, from the number of discontinuities (Palmström, Priest-Hudson): see [RQD](classificazioni.md#rqd-rock-quality-designation). A2 is then obtained from the equations that interpolate Bieniawski's charts, for ranges of RQD (≤ 26.5 · 26.5–39 · … · > 90 %).

## A3 — spacing

Once the mean spacing $s$ (mean distance between adjacent discontinuities) has been computed, A3 is obtained from Bieniawski's equations for ranges of $s$: ≤ 0.2 · 0.2–0.4 · 0.4–0.66 · 0.66–0.94 · 0.94–1.6 · 1.6–2.0 · > 2.0 m.

## A4 — discontinuity conditions { #a4-condizioni-delle-discontinuita }

Reading A4 from Bieniawski's tables is subjective. It is better to sum five sub-parameters:

$$ A4 = v_1 + v_2 + v_3 + v_4 + v_5 $$

**$v_1$ — Joint persistence**

| Persistence (m) | ≤ 1 | 1–3 | 3–10 | 10–20 | > 20 |
|---|---|---|---|---|---|
| $v_1$ | 6 | 4 | 2 | 1 | 0 |

**$v_2$ — Joint aperture**

| Aperture (mm) | Completely closed | < 0.1 | 0.1–1 | 1–5 | > 5 |
|---|---|---|---|---|---|
| $v_2$ | 6 | 5 | 4 | 1 | 0 |

**$v_3$ — Joint roughness**

| Roughness | Very rough | Rough | Slightly rough | Smooth | Slickensided |
|---|---|---|---|---|---|
| $v_3$ | 6 | 5 | 3 | 1 | 0 |

**$v_4$ — Wall alteration**

| Alteration | Unweathered | Slightly | Moderately | Highly weathered | Decomposed |
|---|---|---|---|---|---|
| $v_4$ | 6 | 5 | 3 | 1 | 0 |

**$v_5$ — Discontinuity infilling**

| Infilling | None | Hard < 5 mm | Hard > 5 mm | Soft < 5 mm | Soft > 5 mm |
|---|---|---|---|---|---|
| $v_5$ | 6 | 4 | 2 | 2 | 0 |

## A5 — hydraulic conditions { #a5-condizioni-idrauliche }

Referred to a 10 m face:

| Inflows per 10 m | None | < 10 l/min | 10–25 l/min | 25–125 l/min | > 125 l/min |
|---|---|---|---|---|---|
| Condition | Dry | Damp | Wet | Dripping | Flowing |
| **A5** | 15 | 10 | 7 | 4 | 0 |

## A6 — discontinuity orientation { #a6-orientamento-delle-discontinuita }

Correction coefficient according to the work:

| Application | Very favourable | Favourable | Fair | Unfavourable | Very unfavourable |
|---|---|---|---|---|---|
| Tunnels | 0 | −2 | −5 | −10 | −12 |
| Foundations | 0 | −2 | −7 | −15 | −25 |

!!! warning "Slopes"
    For slopes, A6 according to Bieniawski is too conservative: in the calculation Romana's methodology (SMR, below) is used.

## RMR classes and characteristic parameters

From the value of $RMR_c$, 5 classes are identified:

| $RMR_c$ | 100–81 | 80–61 | 60–41 | 40–21 | ≤ 20 |
|---|---|---|---|---|---|
| Class | I | II | III | IV | V |
| Description | Very good | Good | Fair | Poor | Very poor |

From $RMR_b$ the characteristic parameters are derived (Bieniawski):

$$ c_p\ [\text{kPa}] = 5 \cdot RMR_b \qquad \varphi_p\ [°] = 0{,}5 \cdot RMR_b + 5 \qquad E\ [\text{GPa}] = 2 \cdot RMR_b - 100 $$

The **residual** values of cohesion and friction are obtained with an $RMR_b$ reduced according to Priest (1983):

$$ RMR_b^{res} = RMR_b - 0{,}2 \cdot RMR_b $$

The formula for $E$ holds for $RMR > 50$; for lower values **Serafim and Pereira (1983)** is used:

$$ E = 10^{\frac{RMR - 10}{40}} \quad [\text{GPa}] $$

The **GSI** (Geological Strength Index) is obtained from:

$$ GSI = RMR - 5 $$

with RMR computed on the first four parameters and dry hydraulic conditions ($A5 = 15$); valid for $RMR > 23$.

## Slope Mass Rating (SMR, Romana 1985)

Romana adds to $RMR_b$ adjustment factors for the relative orientation between discontinuities and face, plus a factor for the excavation method:

$$ SMR = RMR_b + (F_1 \cdot F_2 \cdot F_3) + F_4 $$

- **$F_1$** depends on the parallelism between the dip directions of the face and of the joints;
- **$F_2$** refers to the joint dip (planar failure);
- **$F_3$** retains Bieniawski's relationships for the face/joint dip;
- **$F_4$** corrects for the excavation method (empirical).

The conditions checked are **planar failures** and **toppling failures**; the method has also been extended to **wedge** failures (Anbalagan et al.).

### Factor F~1~

| case (Planar $\alpha_j-\alpha_f$ · Toppling $\alpha_j-\alpha_f-180°$ · Wedge $\alpha_i-\alpha_f$) | $F_1$ |
|---|---|
| > 30° | 0.15 |
| 30°–20° | 0.40 |
| 20°–10° | 0.70 |
| 10°–5° | 0.85 |
| < 5° | 1.00 |

### Factor F~2~

| Planar $\beta_j$ · Wedge $\beta_i$ | $F_2$ (planar/wedge) | $F_2$ (toppling) |
|---|---|---|
| < 20° | 0.15 | 1.00 |
| 20°–30° | 0.40 | 1.00 |
| 30°–35° | 0.70 | 1.00 |
| 35°–45° | 0.85 | 1.00 |
| > 45° | 1.00 | 1.00 |

### Factor F~3~

| Planar/Wedge $\beta_j-\beta_f$ | Toppling $\beta_j+\beta_f$ | $F_3$ |
|---|---|---|
| > 10° | < 110° | 0 |
| 10°–0° | 110°–120° | −6 |
| 0° | > 120° | −25 |
| 0°–(−10°) | — | −50 |
| < −10° | — | −60 |

### Factor F~4~ (excavation method)

| Method | $F_4$ |
|---|---|
| Natural slope | +15 |
| Presplitting | +10 |
| Smooth blasting | +8 |
| Normal blasting | 0 |
| Poor blasting | −8 |

where $\alpha_j$ = joint dip direction, $\alpha_i$ = dip direction of the intersection line (wedge), $\alpha_f$ = face dip direction, $\beta_j$ = joint dip, $\beta_i$ = dip of the intersection line, $\beta_f$ = face dip.

### SMR classes

| SMR | 100–81 | 80–61 | 60–41 | 40–21 | 21–0 |
|---|---|---|---|---|---|
| Class | I | II | III | IV | V |
| Description | Very good | Good | Fair | Poor | Very poor |
| Stability | Completely stable | Stable | Partially stable | Unstable | Completely unstable |
| Failure mode | None | Possible blocks | Along planes or wedges | Along planes or large wedges | On large planes or roto-translational |
| Stabilisation | None | Occasional | Systematic | Extensive | Reprofile the slope |

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Rock%20Mechanics%20NX).*
