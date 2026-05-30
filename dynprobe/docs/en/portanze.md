# Foundation bearing capacity

## Shallow foundations

Dynamic Probing NX computes the **allowable pressure** for shallow foundations on granular and cohesive soils according to reference methods from geotechnical literature. Results are expressed in kPa.

### Available methods

| Method | Soil type | Notes |
|---|---|---|
| **Terzaghi-Peck** | Sands, gravels | Classic from N_SPT, includes settlement correction |
| **Meyerhof** | Sands, gravels | Accounts for foundation shape and depth |
| **Bazaraa** | Sands, gravels | Conservative alternative to Meyerhof |
| **Peck-Hanson-Thornburn** | Sands, gravels | With allowable settlement limit |
| **Meigh-Hobbs** | Clays | From N_SPT for cohesive soils |
| **De Beer-Martens** | Sands | European method |

### Required input

In the **Bearing capacity** tab set:

- **Foundation width B** (m)
- **Embedment depth D** (m from ground level)
- **Allowable settlement** (mm) — typically 25 mm for strip footings, 25–50 mm for isolated footings
- **Calculation layer**: the method uses N_SPT of the layer in which the foundation is embedded

### Reading the result

The table shows the allowable pressure q_all for each method. The report lists all methods side by side — choose the one most appropriate to the stratigraphic context.

!!! warning "Foundations on clays"
    For foundations on clays, the calculation is based on Cu derived from the N_SPT → Cu correlation. Supplement with laboratory tests (triaxial, consolidation) for final designs.

## Deep foundations — driven pile (Meyerhof)

For driven piles, the app implements the **Meyerhof** method that estimates separately:

- **Q_p**: tip bearing capacity (contribution of the layer below the pile tip)
- **Q_l**: shaft bearing capacity (contribution of layers traversed by the pile)
- **Q_tot = Q_p + Q_l − W_p**: total bearing capacity net of pile self-weight

### Required input

- **Pile diameter** D (m)
- **Pile length** L (m)
- **Pile type**: the Meyerhof method distinguishes between piles driven in sand and in clay

The calculation uses N_SPT values of the layers according to the depth distribution defined in the stratigraphy. Total bearing capacity is reported in kN.

!!! info "Safety factor"
    The allowable bearing capacity is obtained by dividing the ultimate bearing capacity by the global safety factor. Dynamic Probing NX reports the ultimate bearing capacity — application of the safety factor is the designer's responsibility according to the applicable standard.
