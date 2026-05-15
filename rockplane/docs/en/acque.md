# Water

Water can be present at four locations and contribute as either a destabilising or a stabilising action.

## Parameters

| Parameter | Symbol | Units | Notes |
|---|---|---|---|
| Water unit weight | γ<sub>w</sub> | kN/m³ | default 9.81 |
| Ponded water at toe | H<sub>w</sub> | m | external water (lake, valley aquifer) leaning against the slope face |
| Water in the discontinuity | Z<sub>w</sub> | m | water depth in the joint, generates uplift U on the plane |
| Water in the tension crack | Z<sub>t</sub> | m | only with TC; generates force V perpendicular to the crack |
| Pressure distribution | – | – | none / triangular max-mid / triangular max-toe / triangular max-at-crack-base |
| Permeable slope | bool | – | connects ponded and joint water hydrostatically |

## Force decomposition

| Action | Formula | Direction |
|---|---|---|
| Uplift on the failure plane | U = ½·γ<sub>w</sub>·Z<sub>w</sub>·s<sub>wet</sub> | perpendicular to the plane, pushing the wedge outward |
| Water in the crack | V = ½·γ<sub>w</sub>·Z<sub>t</sub>² | perpendicular to the crack, pushing the wedge toward the valley |
| Ponded at toe | U<sub>p</sub> = ½·γ<sub>w</sub>·H<sub>w</sub>² | perpendicular to the slope face, pushing back into the wedge (stabilising) |

## Pressure distribution

The four options control how the pore water pressure varies along the failure plane:

- **None** — no uplift on the plane (default when Z<sub>w</sub> = 0)
- **Triangular max at mid-height** — pressure peaks at L/2, zero at toe and at crest
- **Triangular max at toe** — pressure peaks at the toe (typical of valley aquifer)
- **Triangular max at crack base** — pressure peaks at the bottom of the tension crack (typical of perched aquifer)

## Permeable slope toggle

When enabled, the external ponded water and the joint water are hydraulically connected. Z<sub>w</sub> is overridden to match H<sub>w</sub>, and U/U<sub>p</sub> are computed consistently to avoid double counting.

## On the section

- **U** vector: perpendicular to the failure plane, halfway along O→C
- **V** vector: perpendicular to the TC, halfway along C→D
- **U<sub>p</sub>** vector: perpendicular to the slope face, halfway along O→B

The blue dashed line shows the water level at the toe (Hw) and the water depth in the crack (Zt) is shown by a dashed level on the tension crack.
