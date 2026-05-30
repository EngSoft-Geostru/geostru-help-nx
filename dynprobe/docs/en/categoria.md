# Subsoil category

## Purpose

The subsoil category determines the expected seismic amplification for the site and governs the value of the parameter **S** (stratigraphic amplification coefficient) in the NTC 2018 response spectra.

Dynamic Probing NX automatically computes the category from the V_s values of the layers, derived from N_SPT → Vs correlations.

## Supported standards

| Standard | Reference parameter | Notes |
|---|---|---|
| **NTC 2018** (D.M. 17/01/2018) | V_s,30 | Main method for buildings and structures |
| **NTC 2008** (D.M. 14/01/2008) | V_s,30 | Compatibility with existing projects |
| **Eurocode 8** (EN 1998-1) | V_s,30 | European reference |

## How V_s,30 is computed

V_s,30 is the average shear wave velocity over the first 30 m of depth, weighted by layer thicknesses. For boring depths less than 30 m, the app uses a default seismic bedrock (rock) for the missing metres — this value is configurable in the **Subsoil cat.** tab.

## How to read the result

In the **Subsoil cat.** tab of the Editor you find:

- **V_s,eq**: computed equivalent velocity (m/s)
- **Category**: letter A / B / C / D / E (NTC 2018) with text description
- **Layer table**: contribution of each layer to the V_s,30 computation

The calculation updates automatically every time you modify the stratigraphy or the V_s values of the layers.

!!! info "Vs from laboratory tests"
    If you have direct V_s measurements (MASW, down-hole, cross-hole), you can override the V_s value of each layer in the dedicated column of the table — the V_s,30 calculation uses the manually entered values instead of those estimated from correlations.

## NTC 2018 categories

| Category | Description |
|---|---|
| **A** | Outcroping rock masses or very stiff soils (V_s,30 > 800 m/s) |
| **B** | Deposits of sands, compact gravels or stiff clays (360 < V_s,30 ≤ 800 m/s) |
| **C** | Deposits of medium-dense sands, gravels or medium-consistency clays (180 < V_s,30 ≤ 360 m/s) |
| **D** | Deposits of loose granular soils or soft cohesive soils (V_s,30 ≤ 180 m/s) |
| **E** | Profiles with surficial alluvial layers with V_s < 360 m/s and thickness within certain limits on a category A or B substratum |
