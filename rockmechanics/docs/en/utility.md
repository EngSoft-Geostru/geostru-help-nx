# Utilities

Two support tools included in Rock Mechanics NX: estimating the **impact force of a rock block** on a structure and assessing **susceptibility to collapse triggered by a seismic event**.

## Impact force of a rock block { #forza-dimpatto-di-un-masso }

The impact force of a rock block on a masonry or concrete structure is evaluated based on the work of McCarty & Carden (1962), Kar (1978) and Knight (1980), as revisited by **Paronuzzi (1989)**.

### Quantities involved

| Symbol | Quantity |
|---|---|
| $F$ | impact force (t) |
| $P$ | weight of the block (kg) |
| $m = P/g$ | mass of the impacting block |
| $g$ | gravitational acceleration |
| $V$ | impact velocity of the block (m/s) |
| $T$ | impact duration (ms) |
| $z$ | penetration of the block into the structure (cm) |
| $\sigma$ | compressive strength of the structure (kPa) |
| $E_m$ | elastic modulus of the block (kPa) |
| $E_s$ | elastic modulus of the structure (kPa) |
| $d$ | maximum diameter of the block (cm) |
| $N$ | shape factor: 1 for a pointed block, 0.72 for a flat block |

### Procedure

The impacting mass is derived from the weight of the block:

$$ m = \frac{P}{g} $$

The **impact force** $F$ is a function of the block's momentum ($m\,V$) dissipated over the **impact duration** $T$. In turn, $T$ depends on the **penetration** $z$ of the block into the structure, and $z$ is obtained from a variable $Z$ that is a function of the structure's strength $\sigma$, the elastic moduli $E_m$ and $E_s$, the diameter $d$ and the shape factor $N$.

The following rule applies to the penetration/diameter ratio:

- if $z/d > 2$ then $z = z$ is assumed;
- if $z/d \leq 2$ then $z$ is corrected according to Paronuzzi's relation.

Finally, the **maximum stress** transmitted to the structure is obtained. The complete formulation follows Paronuzzi (1989) — see [Bibliography](bibliografia.md).

!!! tip "Sizing the defenses"
    For the actual design of rockfall protection works (rigid and flexible rockfall barriers) you can use the dedicated applications in [Geoapp](geoapp.md).

## Collapse prediction for a seismic event { #previsione-del-crollo-per-evento-sismico }

Seismic events, even of low magnitude, are recognized among the triggering causes of collapse phenomena. Susceptibility to seismic actions was studied by **Harp & Noble (1993)**, who propose classifying the rock mass with a methodology derived from **Barton's Q**.

Starting from the geostructural surveys, a value of **modified Q** is computed:

$$ Q = \frac{RQD}{J_n} \cdot \frac{J_r}{J_a} \cdot \frac{1}{A_F} $$

where RQD is obtained from the number of joints per cubic metre $J_v$ (see [RQD](classificazioni.md#rqd-rock-quality-designation)), $J_n$, $J_r$, $J_a$ are the joint parameters of Barton's classification ([$J_n$](classificazioni.md#jn) · [$J_r$](classificazioni.md#jr) · [$J_a$](classificazioni.md#ja)) and $A_F$ is the **aperture factor** of the discontinuities.

### Aperture factor A~F~

| Aperture of the discontinuities | $A_F$ |
|---|---|
| All joints are closed | 1.0 |
| Mostly closed, some open up to 2 cm | 2.5 |
| Mostly closed, some open up to 5 cm | 5.0 |
| More than 20% of the joints with apertures up to 20 cm | 7.5 |
| More than 60% of the joints with apertures up to 20 cm | 10.0 |
| Joints open more than 20 cm | 15.0 |

If the rock mass contains free blocks, $A_F$ must be increased by 1; likewise if a persistent joint is dip-slope oriented.

### Susceptibility classification

From the value of Q computed in this way, the authors propose the following classification of collapse susceptibility for a seismic event of magnitude > 5:

| Q | Collapse susceptibility |
|---|---|
| < 0.1 | Very high |
| 0.1 – 1 | High |
| 1 – 9.99 | Medium |
| > 10 | Low |

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Rock%20Mechanics%20NX).*
