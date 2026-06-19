# Barton — Q index

Developed in 1974 at the **Norwegian Geotechnical Institute** essentially for underground works, Barton's classification was later extended to different fields; in 2002 Barton himself proposed a comprehensive revision.

## Computing the Q index

$$ Q = \frac{RQD}{J_n} \cdot \frac{J_r}{J_a} \cdot \frac{J_w}{SRF} $$

where the six indices are:

- **RQD** — Rock Quality Designation, accounts for the subdivision of the rock mass;
- **$J_n$** — Joint Set Number, depends on the number of joint sets;
- **$J_r$** — Joint Roughness Number, depends on the roughness of the most unfavourable set;
- **$J_a$** — Joint Alteration Number, depends on the degree of alteration and on the infilling, for the most unfavourable set;
- **$J_w$** — Joint Water Number, depends on the hydrogeological conditions;
- **SRF** — Stress Reduction Factor, a function of the stress state or of tectonic disturbance.

The three ratios have a physical meaning: $RQD/J_n$ is related to **block size**, $J_r/J_a$ to the **shear strength** between blocks, $J_w/SRF$ to the **active stress state**.

More recently Q has been **normalised** with respect to the uniaxial compressive strength of the rock $\sigma_c$:

$$ Q_c = Q \cdot \frac{\sigma_c}{100} $$

## Input parameters

The parameters $J_n$, $J_r$, $J_a$, $J_w$ are defined in the common tables:

- [Parameter $J_n$](classificazioni.md#jn)
- [Parameter $J_r$](classificazioni.md#jr)
- [Parameter $J_a$](classificazioni.md#ja)
- [Parameter $J_w$](classificazioni.md#jw)

For **RQD** its nominal value is used; if $RQD < 10$ a value of 10 is assumed anyway (see [RQD](classificazioni.md#rqd-rock-quality-designation)).

## SRF factor (Stress Reduction Factor) { #srf }

### Weakness zones intersecting the excavation

| Definition | SRF |
|---|---|
| Multiple weakness zones with clay or chemically disintegrated rock, very loose surrounding rock | 10 |
| Single weakness zones with clay or disintegrated rock (overburden ≤ 50 m) | 5 |
| Single weakness zones with clay or disintegrated rock (overburden > 50 m) | 2.5 |
| Multiple shear zones in competent rock, loosening of the surrounding rock | 7.5 |
| Single shear zone in competent rock (overburden ≤ 50 m) | 5 |
| Single shear zone in competent rock (overburden > 50 m) | 2.5 |
| Heavily fractured zones intersected by open and continuous discontinuities | 5 |

If the weakness zones influence but do not directly intersect the excavation, SRF should be reduced by 25–50%.

### Competent rock mass with geostatic stress problems

| Definition | $\sigma_c/\sigma_1$ | $\sigma_\theta/\sigma_c$ | SRF |
|---|---|---|---|
| Low stress field, near surface | > 200 | < 0.01 | 2.5 |
| Favourable stress conditions | 200 – 10 | 0.01 – 0.3 | 1 |
| High stress field (favourable in the crown, unfavourable at the sidewalls) | 10 – 5 | 0.3 – 0.5 | 0.5 – 2 |
| Moderate rock bursts after more than one hour, massive rock | 5 – 3 | 0.5 – 0.65 | 5 – 50 |
| Almost immediate rock bursts, massive rock | 3 – 2 | 0.65 – 1 | 50 – 400 |

where $\sigma_c$ is the compressive strength of the rock, $\sigma_\theta$ the maximum tangential stress at the excavation boundary, $\sigma_1$ and $\sigma_3$ the major and minor principal stresses.

If $\sigma_1/\sigma_3$ is between 5 and 10, reduce $\sigma_c$ to $0{,}75\,\sigma_c$; if > 10, reduce to $0{,}5\,\sigma_c$. If the depth of the crown below ground level is less than the width of the excavation, Barton suggests SRF = 5. The last three rows apply to very hard, massive rocks, with $RQD/J_n$ between 50 and 200.

### Squeezing rock mass

| Definition | SRF |
|---|---|
| Moderately squeezing rock mass | 5 – 10 |
| Strongly squeezing rock mass | 10 – 20 |

### Swelling rock mass

| Definition | SRF |
|---|---|
| Moderately swelling rock mass | 5 – 10 |
| Strongly swelling rock mass | 10 – 15 |

!!! note "Characterisation away from the excavation"
    To characterise the rock mass away from the influence of the excavation, the SRF values (5 – 2.5 – 1.0 – 0.5) can be assumed as a function of the overburden heights (0–5; 5–25; 25–250; > 250 m).

## Rock mass classes

The Q index ranges from 0.001 to 1000 and is divided into 9 classes:

| Q | Class | Description |
|---|---|---|
| 0.001 – 0.01 | IX | Exceptionally poor |
| 0.01 – 0.1 | VIII | Extremely poor |
| 0.1 – 1 | VII | Very poor |
| 1 – 4 | VI | Poor |
| 4 – 10 | V | Fair |
| 10 – 40 | IV | Good |
| 40 – 100 | III | Very good |
| 100 – 400 | II | Extremely good |
| 400 – 1000 | I | Exceptionally good |

## Characteristic rock mass parameters

Two strength components are extrapolated from Q:

**Frictional component** (approximation of the friction angle of the rock mass):

$$ \varphi' = \arctan\!\left(\frac{J_r \cdot J_w}{J_a}\right) $$

**Cohesive component** (approximation of the cohesion of the rock mass):

$$ c' = \frac{RQD}{J_n} \cdot \frac{1}{SRF} \cdot \frac{\sigma_c}{100} $$

The **static deformation modulus** of the rock mass is determined according to the expression of **Serafim and Pereira (1983)** derived from RMR, obtaining the equivalent RMR with $RMR = 9\ln(Q) + 44$:

$$ E_m = 10^{\frac{RMR - 10}{40}} \quad [\text{GPa}] $$

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Rock%20Mechanics%20NX).*
