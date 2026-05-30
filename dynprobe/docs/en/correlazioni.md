# Geotechnical correlations

## What they are

Geotechnical correlations transform N_SPT into soil strength and deformability parameters. They are empirical formulas derived from international literature — their use is well established in geotechnical practice, but they remain estimates: always supplement with laboratory data when available.

## How to read them

In the **Correlations** tab of the Editor, for each layer in the stratigraphy a table appears with the computed values. The left column indicates the parameter; the subsequent columns show the values according to the different reference authors. You can activate or deactivate individual authors using the toggles at the top of each column.

The **preferred value** (⭐) feeds the **Parameter summary** tab and the Word report.

## Parameters for cohesive soils (COES)

| Parameter | Meaning |
|---|---|
| **Cu** | Undrained shear strength (kPa) |
| **Mo** | Oedometric modulus (MPa) |
| **Ey** | Young's modulus (MPa) |
| **Vs** | Shear wave velocity (m/s) |
| **γ** | Unit weight (kN/m³) |
| **Classification** | Consistency (very soft → very stiff) |

Reference authors cited in Italian and international geotechnical literature: Terzaghi-Peck, Schmertmann, Ohta-Goto, and others.

## Parameters for non-cohesive soils (INCO)

| Parameter | Meaning |
|---|---|
| **Dr** | Relative density (%) |
| **φ** | Internal friction angle (°) |
| **φ_160** | Friction angle from normalised N_1,60 (°) |
| **Mo** | Oedometric modulus (MPa) |
| **Ey** | Young's modulus (MPa) |
| **Vs** | Shear wave velocity (m/s) |
| **ν** | Poisson's ratio |
| **G** | Shear modulus (MPa) |

Reference authors: Meyerhof, Peck, Hanson, Thornburn, Ohta-Goto, Seed-Idriss, and others.

!!! warning "Validity limits"
    Each correlation was developed for a specific range of N_SPT and specific soil types. When N_SPT is very low (< 3) or very high (> 50), results should be interpreted with caution. The app highlights out-of-range values.

## Parameter envelope

When you have multiple tests on the same site, the **Envelope** tab shows for each layer the min-max range of parameters across all tests, with the **design criterion** selectable (minimum / mean / maximum / preferred value ⭐). The design value automatically feeds the Summary.

## Parameter summary

The **Summary** tab collects in a single table the characteristic geotechnical values for each layer — useful as a overview table to include in the geotechnical report. The Word report includes it automatically.
