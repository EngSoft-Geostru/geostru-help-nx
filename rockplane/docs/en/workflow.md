# Full workflow — realistic case

This page walks through a realistic project: rock slope with water, seismic, tension crack and a reinforcement scheme of passive nails plus drape mesh.

## Step 0 — Project details

Open the **Project details** card at the top of the screen:

- **Description**: short identifier of the case
- **Site**: location
- **Lat / Lon / Alt**: useful for the report header
- **Date**: today
- **Code**: choose between *Characteristic values (γ = 1.0)*, *NTC 2018 (A2+M2+R2)*, or one of the *EC7 design approaches DA1/DA2/DA3*

The **applied γ factors** chip strip immediately below shows the partial factors that are currently in use.

## Step 1 — Geometry of the wedge

Enter the geometry of the rock block under analysis:

| Parameter | Meaning |
|---|---|
| **H** | slope height [m] |
| **β** | slope face dip [°] |
| **α** | failure plane dip [°] |
| **ψ** | upper face dip [°] (0 = horizontal bench) |
| **B** | block depth (length ⟂ to the section) [m] |

If a **tension crack** is present, enable it and fill in:

| Parameter | Meaning |
|---|---|
| **T** | crack distance from the crest [m] |
| **θ** | crack dip [°] |

The 2D section on the right updates in real time. The `α crit` button next to α automatically searches for the most unfavourable α (sweep over the kinematically admissible range).

[Detail →](geometria.md)

## Step 2 — Material on the failure plane

Two strength criteria are available:

- **Mohr-Coulomb** (linear): τ = c + σ<sub>n</sub>·tan φ
- **Barton-Bandis** (non-linear): τ = σ<sub>n</sub>·tan(φ<sub>b</sub> + JRC·log₁₀(JCS/σ<sub>n</sub>))

Use Barton-Bandis for rough rock joints at low normal stress, where the roughness dilation i_eff is significant.

[Detail →](materiale.md)

## Step 3 — Actions

### Water

- **Hw**: water level ponded at the toe (lake, valley aquifer)
- **Zw**: water depth in the discontinuity (generates uplift U on the plane)
- **Pressure distribution**: triangular (max at mid-height / at toe / at crack base) or uniform
- **Permeable slope** toggle: connects external water to the discontinuity at the same level

### Seismic

- **αs = kh**: horizontal pseudo-static coefficient (NTC Tab. 7.11.I)
- **Ω**: seismic direction [°]

### External load

- **E**: magnitude per metre [kN/m]
- **δ**: inclination [°] (δ=0° horizontal toward the valley = unfavourable, δ=90° vertical = weight, δ=−90° upward = anchor pull)
- **Type**: permanent (γG) or variable (γQ)

[Detail water →](acque.md) · [Detail seismic →](sisma.md) · [Detail external →](forze-esterne.md)

## Step 4 — Reinforcement

### Catalogue

Build a catalogue of nail/anchor types and mesh types. Each type carries either:

- a **manually assigned capacity** F [kN], or
- a **computed design resistance** R<sub>d</sub> from the NTC formulas (§6.6 for anchors, §6.7 for nails)

### Install reinforcement

Use **+ add reinforcement** to add rows of nails/anchors at given Yt heights on the slope face, with horizontal spacing and inclination Δ. For meshes, simply pick the mesh type from the catalogue.

### Auto-design

The **auto-design** button computes the number of rows, positions and spacing needed to meet a target FS. Optional **with AI** review adds a technical comment, constructability concerns and refinement suggestions.

[Detail nails →](chiodi.md) · [Detail anchors →](tiranti.md) · [Detail meshes →](reti.md)

## Step 5 — Read the result

- The **factor of safety FS** is shown in the lower-left analysis panel
- The **overturning Fr** ratio is the structural overall check around the toe
- The **Computed geometry** card shows L, M, Q, A, W
- The **Forces on the plane** card shows N, S, τ, U, V
- The **Design resistances** card (visible when NTC calculation is enabled) shows the per-nail breakdown and NTC-style checks

## Step 6 — Verification under the chosen code

[Detail verification →](verifica.md)

## Step 7 — Export

Menu **Export**: Word report, SVG/PNG drawing, DXF technical drawing, or open the section directly in **Trispace NX** (web 2D CAD editor of the suite).

[Detail export →](export.md)
