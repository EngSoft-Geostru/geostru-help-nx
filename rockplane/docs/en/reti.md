# Meshes — R1 drape and R2 cable panel

Two mesh families are supported.

## R1 — Drape rock-fall mesh (adhering)

Wire mesh held against the slope face by a regular grid of short nails. The mesh exerts an equivalent **uniform normal pressure q** on the wedge.

### Capacity

$$q = \frac{T_{nail}}{\text{spacing}_O \cdot \text{spacing}_V}$$

where T<sub>nail</sub> is the single nail capacity and spacing_O × spacing_V is the nail grid (typical 3×3 m).

### Input fields

| Field | Notes |
|---|---|
| Wire φ [mm] | wire mesh diameter (typical 3 mm) |
| Mesh H/V [mm] | wire mesh opening (typical 80×80 mm) |
| Spacing H/V [m] | nail grid (typical 3×3 m) |
| T nail [kN] | single nail capacity (declared by the supplier) |

The card shows the computed q in kN/m². Toggle off **"Compute q from parameters"** to enter q manually.

### Where it enters the analysis

R1 contributes a normal force on the slope face. The components R1<sub>x</sub>, R1<sub>y</sub> are added to the global F<sub>x</sub>, F<sub>y</sub> together with the other actions.

### Short fixing nails vs structural nails

A common question: should the nails fixing the R1 mesh also be modelled as separate **passive nails** in the Reinforcement section?

- **Case A — short fixing nails** (do not cross the failure plane): they only hold the mesh. Already represented by `T_nail / mesh_area = q`. **Do NOT** add them as separate reinforcement.
- **Case B — long structural nails** (cross the failure plane, anchor in intact rock): they contribute directly to wedge stability (force K + Clouterre shear). Model **both** the R1 mesh **and** the long nails.

Rule of thumb: if the nail length is ≥ 1.5× the depth of the failure plane, it is structural (Case B).

## R2 — Cable panel (high-resistance caging)

A grid of high-strength steel cables, mobilising a **shear capacity τ** per metre of section that adds directly to the resisting shear on the failure plane.

### Capacity

$$\tau = T_{cable} \cdot n \cdot \frac{1000}{\text{spacing}_{mm}}$$

where T<sub>cable</sub> is the single cable capacity, n is the number of parallel cables and spacing is the cable spacing in millimetres.

### Input fields

| Field | Notes |
|---|---|
| Spacing [mm] | cable spacing (typical 600 mm) |
| n cables | number of cables (typical 1) |
| T cable [kN] | single cable capacity (typical 60 kN for φ8) |

### Where it enters the analysis

R2 adds directly to the resisting τ on the failure plane:

$$\tau_{total} = c \cdot L + N \cdot \tan\varphi + K_{passive} + \tau_{R2}$$

## What RockPlane does NOT verify

- Punching of the single mesh-nail node (R<sub>punz</sub>) — typically certified by the supplier
- Global tension of the mesh panel (R<sub>tr,mesh</sub>) — same

These are internal structural checks of the mesh product, not stability checks of the wedge. RockPlane uses the declared capacity and inserts it as an action / resistance in the planar stability analysis.
