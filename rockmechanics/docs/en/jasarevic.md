# Jašarević & Kovačević — n index

Developed by **Jašarević and Kovačević (1996)** on the carbonate formations of Croatia, this method has a clear derivation from the RMR system. The procedure is simple: at least three numerical coefficients are assigned relating to the **geomechanical** properties of the rock mass, and at least as many relating to **engineering-geological** properties. To each property you assign a value $n_i$ ranging from 1 to 5.

## Coefficient assignment table

On the left you find the geomechanical properties, on the right the engineering-geological ones; the last column reports the coefficient $n_i$.

| $S_u$ (MPa) | $I_{s\perp}$ (MPa) | $I_{s\parallel}$ (MPa) | $V_p$ (km/s) | $V_p/V_0$ | $\alpha$ | Water | RQD (%) | $J_v$ | $S$ (cm) | Joints (JRC) | $n_i$ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| > 130 | > 5.7 | > 0.8 | > 6.5 | > 0.8 | 70–90 | A | > 65 | 1–2 | > 50 | 16–20 | 1 |
| 100–130 | 5.3–5.7 | 0.7–0.8 | 4.7–6.5 | 0.6–0.8 | 0–20 | U | 45–65 | 2–5 | 20–50 | 12–16 | 2 |
| 70–100 | 4.7–5.3 | 0.6–0.7 | 3.0–4.7 | 0.4–0.6 | 20–35 | B | 35–45 | 5–10 | 10–20 | 8–12 | 3 |
| 40–70 | 4.3–4.7 | 0.5–0.6 | 1.2–3.0 | 0.2–0.4 | 35–50 | S | 25–35 | 10–15 | 6–10 | 4–8 | 4 |
| < 40 | < 4.3 | < 0.5 | < 1.2 | < 0.2 | 50–70 | F | < 25 | > 15 | < 6 | < 4 or infilled | 5 |

where:

- **$S_u$** = uniaxial compressive strength of the intact rock (see [Uniaxial compressive strength $S_u$](classificazioni.md#resistenza-a-compressione-uniassiale-su));
- **$I_{s\perp}$** = point load index measured perpendicular to the main discontinuity;
- **$I_{s\parallel}$** = point load index measured parallel to the main discontinuity;
- **$V_p$** = seismic velocity of the longitudinal waves;
- **$V_0$** = reference seismic velocity (intact rock);
- **$\alpha$** = dip of the most unfavourable discontinuity;
- **Water** = A: none — U: damp — B: wet — S: dripping — F: flowing;
- **RQD** = degree of fracturing of the rock mass (see [RQD](classificazioni.md#rqd-rock-quality-designation));
- **$J_v$** = number of joints per m³;
- **$S$** = discontinuity spacing.

!!! note "Non-unique values"
    If the values do not fall within a single row, take the intermediate numerical coefficient: for example, for $J_v$ between 5 and 15, $n_i = 3{,}5$ is assumed.

## Computing the n index

The n index is the average of the assigned coefficients:

$$ n = \frac{1}{N_T}\sum_{i=1}^{N_T} n_i $$

where $N_T$ is the number of properties considered (minimum 6) in the assignment of the coefficients.

## Correlation with RMR

The authors suggest the following correlation between the n index and the corrected RMR:

$$ RMR_c = 110 - 20\,n $$

From the value of $RMR_c$ you derive the class and quality of the rock mass, by analogy with Bieniawski's scale:

| $RMR_c$ | 100–81 | 80–61 | 60–41 | 40–21 | ≤ 20 |
|---|---|---|---|---|---|
| Class | I | II | III | IV | V |
| Description | Very good | Good | Fair | Poor | Very poor |

## Characteristic rock mass parameters

From $RMR_c$ you derive the strength and deformability parameters of the rock mass.

**Cohesion** (Sen):

$$ c\ [\text{kPa}] = 3{,}625 \cdot RMR_c $$

**Friction angle** (Sen):

$$ \varphi\ [°] = 25\,(1 + 0{,}01\,RMR_c)\quad \text{for } RMR_c > 20 $$

$$ \varphi\ [°] = 1{,}5\,RMR_c\quad \text{for } RMR_c < 20 $$

**Deformation modulus** (Jašarević & Kovačević):

$$ E\ [\text{MPa}] = \exp(4{,}407 + 0{,}081 \cdot RMR_c) $$

The authors consider this expression for $E$ to be more correct than that of **Serafim and Pereira (1983)**:

$$ E\ [\text{GPa}] = 10^{\frac{RMR_b - 10}{40}} $$

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Rock%20Mechanics%20NX).*
