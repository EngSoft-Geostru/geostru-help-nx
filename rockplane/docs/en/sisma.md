# Pseudo-static seismic

Earthquake action on the wedge follows the NTC §3.2 / §7.11.3 pseudo-static formulation.

## Parameters

| Parameter | Symbol | Units | Notes |
|---|---|---|---|
| Horizontal seismic coefficient | α<sub>s</sub> = k<sub>h</sub> | – | NTC Tab. 7.11.I: kh = βs · amax / g (with βs reduction for natural slopes) |
| Seismic direction | Ω | ° | rotation of the seismic vector with respect to horizontal; 0° = toward the valley |

The vertical seismic coefficient k<sub>v</sub> is **not** modelled as an independent parameter. The user can encode a vertical component by playing with Ω (≠ 0° pushes the force slightly upward or downward).

## Equivalent force

The pseudo-static force applied at the wedge centroid is:

$$S = k_h \cdot W$$

with components:

$$S_x = -S \cdot \cos\Omega, \quad S_y = -S \cdot \sin\Omega$$

The minus signs follow the convention "seismic force away from the slope". The partial factor on seismic actions is γ<sub>E</sub> = 1.0 (NTC §3.2.4).

## Typical values

| Site class / zone | NTC region | k<sub>h</sub> typical |
|---|---|---|
| Class A (rock) | low seismicity | 0.02–0.04 |
| Class B/C | medium seismicity | 0.05–0.10 |
| Class A | high seismicity | 0.08–0.12 |
| Class C/D | high seismicity | 0.12–0.20 |

## On the section

The seismic force S is drawn as an arrow from the centroid G of the wedge, scaled to be visible (minimum 50 px). The label `S = X kN/m` is placed perpendicular to the arrow.

## Common use

Set kh to the value required by the site classification, leave Ω = 0 (horizontal toward the valley). FS drops by roughly 1−0.5·k<sub>h</sub>·tan α / tan(α − k<sub>h</sub>) — typically 10–30% for moderate seismicity.

[See also the verification page →](verifica.md)
