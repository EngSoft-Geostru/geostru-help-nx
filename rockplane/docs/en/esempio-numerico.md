# Numerical example worked by hand

Step-by-step reconstruction of a reference case to document the traceability of the calculation in RockPlane NX. Values are obtained analytically with a scientific calculator, independent of the software, and compared to the software output.

Serves as the **audit reference** for compliance reviews and for anyone who wants to manually check the consistency between the theoretical manual formulas (Hoek-Bray / RocPlane) and the implementation.

## 1. Base case input

| Parameter | Value |
|---|---|
| H · slope height | 30 m |
| β · slope face dip | 60° |
| α · failure plane dip | 30° |
| ψ · upper face dip | 0° |
| γ · unit weight | 26 kN/m³ |
| c · cohesion | 50 kPa |
| φ · friction angle | 30° |
| Approach | Characteristic (γ = 1.0) |
| Water / Seismic / Reinforcement | None |

## 2. Geometry

```
N = H / sin β = 30 / 0.86603 = 34.641 m
L = H / sin α = 30 / 0.50000 = 60.000 m
M = (L·cos α − H·cot β) / cos ψ = 34.641 m
A = ½·H²·(cot α − cot β) = ½·900·(1.732 − 0.577) = 519.62 m²
W = γ · A = 26 · 519.62 = 13 510.2 kN/m
```

## 3. Forces and equilibrium

```
F_x = 0                      (no E, no seismic, no reinforcement)
F_y = W_y = −γ_G · W = −13 510.2 kN/m
N   = −F_y·cos α + F_x·sin α − U
    = 13 510.2 · 0.866 + 0 − 0 = 11 700.6 kN/m
S   = −F_y·sin α − F_x·cos α
    = 13 510.2 · 0.500 − 0     = 6 755.1 kN/m
```

## 4. Mohr-Coulomb resistance and FS

```
τ_res = c·L/γ_c + N·tan φ/γ_φ
      = 50·60 + 11 700.6 · 0.57735
      = 3 000 + 6 754.8 = 9 754.8 kN/m

FS    = τ_res / |S| = 9 754.8 / 6 755.1 = 1.4441
```

## 5. Manual vs software comparison

| Quantity      | Hand            | Software        | Δ          |
|---------------|-----------------|-----------------|------------|
| N (normal)    | 11 700.6 kN/m   | 11 700.6 kN/m   | < 0.001 %  |
| S (shear)     | 6 755.1 kN/m    | 6 755.1 kN/m    | < 0.001 %  |
| τ_res         | 9 754.8 kN/m    | 9 754.8 kN/m    | < 0.001 %  |
| **FS**        | **1.4441**      | **1.4441**      | **0.0000** |

Exact match to 4 decimals. The software formulation faithfully reproduces the classical Hoek-Bray formula:

```
FS = (c·L + W·cos α·tan φ) / (W·sin α)
```

## 6. Extension with seismic kh = 0.15

```
S_mod = k_h · W = 0.15 · 13 510.2 = 2 026.5 kN/m
F_x   = −2 026.5 kN/m       F_y = −13 510.2 kN/m
N     = 13 510.2·0.866 − 2 026.5·0.500 = 10 687.3 kN/m
S     = 13 510.2·0.500 + 2 026.5·0.866 =  8 510.1 kN/m
τ_res = 3 000 + 10 687.3 · 0.57735     =  9 170.0 kN/m
FS    = 9 170.0 / 8 510.1 = 1.078
```

Software comparison: **FS = 1.0776**, match to 4 decimals.

## 7. Extension with water in the discontinuity (uplift U)

Base case + Z<sub>w</sub> = 10 m, triangular distribution max at toe.

```
u_max = γ_w · Z_w = 9.81 · 10 = 98.1 kPa
s_wet = Z_w / sin α = 10 / 0.5 = 20.0 m
U     = ½ · u_max · s_wet = ½ · 98.1 · 20 = 981.0 kN/m
N_eff = 11 700.6 − 981.0 = 10 719.6 kN/m
S     = 6 755.1 kN/m   (unchanged)
τ_res = 3 000 + 10 719.6 · 0.57735 = 9 188.4 kN/m
FS    = 9 188.4 / 6 755.1 = 1.360
```

Software comparison: **FS = 1.3603** and **U = 981.0 kN/m**. Exact match.

## 8. Extension with passive nail (Clouterre N-V)

Base case + passive nail F = 500 kN/m, Δ = 15° below horizontal.

```
K_x = F · cos Δ  =  500 · 0.96593 =  482.96 kN/m
K_y = −F · sin Δ = −500 · 0.25882 = −129.41 kN/m
N   = 13 639.6 · 0.866 + 482.96 · 0.500 = 12 054.2 kN/m
S   = 6 755.1 kN/m   (unchanged — passive K does not enter driving S)

contrib_K = K_x · cos α + K_y · sin α = 353.7 kN/m
τ_res     = 3 000 + 12 054.2 · 0.57735 + 353.7 = 10 314.5 kN/m
FS        = 10 314.5 / 6 755.1 = 1.527
```

**Clouterre check** — Φ = α + Δ = 45°:

| Mode | Contribution |
|---|---|
| Axial  | T_max·(cos Φ + sin Φ · tan φ) = **557.6** |
| Shear  | V_max·(sin Φ − cos Φ · tan φ) = **74.8**  |

Axial mode wins → applied force corresponds to K components computed above. Software comparison: **FS = 1.5267**.

## 9. Extension with active anchor

Base case + active anchor pre-load F = 500 kN/m, Δ = 20°.

The anchor enters as an **ACTION (J)** in the resultants F_x, F_y, not in the resistance.

```
J_x = F · cos Δ  =  500 · 0.93969 =  469.85 kN/m
J_y = −F · sin Δ = −500 · 0.34202 = −171.01 kN/m
F_x = 469.85 kN/m       F_y = −13 681.2 kN/m
N   = 13 681.2 · 0.866 + 469.85 · 0.500 = 12 082.8 kN/m
S   = 13 681.2 · 0.500 − 469.85 · 0.866 =  6 433.6 kN/m  (reduced)
τ_res = 3 000 + 12 082.8 · 0.57735 = 9 977.4 kN/m
FS    = 9 977.4 / 6 433.6 = 1.551
```

Software comparison: **FS = 1.5506**, match to 3 decimals.

!!! tip "Active anchor vs passive nail (same F = 500 kN/m, Δ ≈ 15-20°)"
    - **Active anchor** (F=1.551): reduces driving shear S directly (pre-applied force).
    - **Passive nail** (F=1.527): acts through resisting τ (mobilised during sliding).
    The anchor is slightly more effective for the same F.

## 10. Summary

| Case       | Addition to base                 | FS     | Internal test |
|------------|----------------------------------|--------|---------------|
| 1–5        | base case dry                    | 1.4441 | T03           |
| 6          | seismic k_h = 0.15               | 1.078  | T04           |
| 7          | water Z_w = 10 m, max at toe     | 1.360  | T05           |
| 8          | passive nail F = 500, Δ = 15°    | 1.527  | T07           |
| 9          | active anchor F = 500, Δ = 20°   | 1.551  | T06           |

All cases match **to 3-4 decimal places** with the software output, confirming the traceability of the calculation for each modelled mechanism (weight W, seismic S, water U, reinforcement J/K).

---

*For the complete suite of 97 automated regression tests, see the [repository README](https://github.com/EngSoft-Geostru) or contact the GeoStru team.*
