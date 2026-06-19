# Singh & Goel — N index

Singh and Göel (1999), for application in the field of **tunnels**, propose computing the **Rock Mass Number** $N$ starting from Barton's Q classification, excluding the stress effect (i.e. by setting $SRF = 1$):

$$ N = \frac{RQD}{J_n} \cdot \frac{J_r}{J_a} \cdot J_w $$

In other words, $N$ is the Q index without the $SRF$ factor: see the [Barton](barton.md) page for the full calculation of Q.

## Input parameters

The indices $J_n$, $J_r$, $J_a$, $J_w$ are defined in the common tables:

- [Parameter $J_n$](classificazioni.md#jn)
- [Parameter $J_r$](classificazioni.md#jr)
- [Parameter $J_a$](classificazioni.md#ja)
- [Parameter $J_w$](classificazioni.md#jw)

For **RQD**, its nominal value is taken; if $RQD < 10$, a value of 10 is assumed anyway (see [RQD](classificazioni.md#rqd-rock-quality-designation)).

## Coefficient A1

The parameter $A_1$ is derived from the **uniaxial compressive strength** $S_u$ of the intact rock, determined by a Point Load test, Schmidt hammer, or the standard ISRM procedure: see [Uniaxial compressive strength Su](classificazioni.md#resistenza-a-compressione-uniassiale-su).

The app derives $A_1$ from the continuous equations that interpolate Bieniawski's charts, subdivided by intervals of $S_u$:

| Interval of $S_u$ (MPa) |
|---|
| $\leq 44{,}5$ |
| $44{,}5 - 93{,}75$ |
| $93{,}75 - 140$ |
| $140 - 180$ |
| $180 - 240$ |
| $> 240$ |

Above 240 MPa, $A_1 = 15$ is assumed.

!!! tip "Continuous equations"
    If you have Point Load or Schmidt hammer test results, it is preferable to derive $A_1$ from the equations of Bieniawski's charts rather than from the stepped tables: the result is continuous and less subjective.

## Coefficient A6 (orientation of the discontinuities)

For the orientation of the discontinuities, the correction coefficient $A_6$ is applied:

| Very favourable | Favourable | Fair | Unfavourable | Very unfavourable |
|---|---|---|---|---|
| 0 | −2 | −5 | −10 | −12 |

## Results derived from the calculation of N

From the value of $N$, the **Rock Condition Rating** (Singh-Goel) is obtained:

$$ RCR = 8\,\ln(N) + 30 $$

and from this the corrected and base values of RMR:

$$ RMR_{corretto} = RCR + (A_1 + A_6) \qquad RMR_{base} = RCR + A_1 $$

From Bieniawski's relation $RMR = 9\,\ln(Q) + 44$, Barton's Q index is obtained:

$$ Q = e^{\frac{RMR - 44}{9}} $$

and therefore the Stress Reduction Factor and the normalised Q index:

$$ SRF = \frac{N}{Q} \qquad Q_c = Q \cdot \frac{\sigma_c}{100} $$

where $\sigma_c$ is the uniaxial compressive strength of the rock.

## Rock mass classes

As a function of $RMR_c$, the rock mass is divided into five classes:

| $RMR_c$ | 100–81 | 80–61 | 60–41 | 40–21 | ≤ 20 |
|---|---|---|---|---|---|
| Class | I | II | III | IV | V |
| Description | Very good | Good | Fair | Poor | Very poor |

The resulting Q index ranges from 0.001 to 1000 and is subdivided into 9 classes:

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

## Characteristic parameters

From the value of $RMR_b$ (Bieniawski), the peak characteristic parameters of the rock mass are derived:

$$ c_p\ [\text{kPa}] = 5\,RMR_b \qquad \varphi_p\ [°] = 0{,}5\,RMR_b + 5 \qquad E\ [\text{GPa}] = 1{,}5\,RMR_b - 100 $$

The residual values of cohesion and friction angle are obtained by introducing into the formulas a modified $RMR_b$ according to $RMR_b^{res} = RMR_b - 0{,}2\,RMR_b$ (Priest, 1983).

The formula for $E$ is valid for $RMR > 50$; for lower values, the expression of Serafim and Pereira (1983) is used:

$$ E\ [\text{GPa}] = 10^{\frac{RMR_b - 10}{40}} $$

Alternatively, as for [Barton](barton.md), the frictional and cohesive components of the rock mass can be extracted from N/Q:

$$ \varphi' = \arctan\!\left(\frac{J_r \cdot J_w}{J_a}\right) \qquad c' = \frac{RQD}{J_n} \cdot \frac{1}{SRF} \cdot \frac{\sigma_c}{100} $$

The bibliographic references are collected on the [Bibliography](bibliografia.md) page.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Rock%20Mechanics%20NX).*
