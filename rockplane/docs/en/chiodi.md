# Passive nails

Passive nails (rock bolts, soil nails) reinforce the wedge by mobilising bar resistance against shear and axial load as the wedge tries to move. They follow **NTC 2018 §6.7** with the GeoStru SoilNail Variant A formulation (consistent with the FHWA-NHI-09-035 reference).

## Capacity of the single nail

The nail has **3 axial limits** + **1 shear limit**:

| Limit | Symbol | Formula |
|---|---|---|
| Bar yielding | T<sub>a1</sub> | η · f<sub>y</sub> · π·(D−4)² / 4 |
| Bar ↔ grout bond | T<sub>a2</sub> | β · √f<sub>ck</sub> · π · (D−4) · L<sub>mm</sub> · FS⁻¹ |
| Hole pull-out (in rock) | T<sub>a3</sub> | π · D<sub>hole</sub> · L<sub>mm</sub> · τ<sub>ult</sub> · FS⁻¹ with τ<sub>ult</sub> = 0.1·σ<sub>c</sub> |
| Hole pull-out (in soil) | T<sub>a3</sub> | (π·D·c' + 2·D<sub>hole</sub>·K<sub>α</sub>·σ<sub>v</sub>·tan φ) · L · FS⁻¹ |
| **Bar shear (Tresca)** | T<sub>a4</sub> | 0.5 · f<sub>y</sub> · A<sub>net</sub> |

Axial capacity: \(T_{max} = \min(T_{a1}, T_{a2}, T_{a3})\). T<sub>a4</sub> enters separately in the N-V interaction.

For nails under NTC §6.7 (Variant A) **neither ξ nor γ<sub>Ra,t</sub>** is applied: the design capacity equals T<sub>max</sub> (optionally divided by an extra local FS if required by the specification).

## Clouterre N-V interaction

A passive nail crossing the sliding plane works axially **and** in shear simultaneously. Clouterre 1993 (FHWA-NHI-09-035) uses a linear envelope:

$$\frac{T}{T_{max}} + \frac{V}{V_{max}} \le 1$$

The software picks the corner of this envelope that maximises the stabilising contribution along the failure plane:

$$F_{stab} = T \cdot \cos\Phi + V \cdot \sin\Phi, \quad \Phi = \alpha + \Delta$$

The optimum lies on one of the two axes:

- **Axial mode**: T = T<sub>max</sub>, V = 0
- **Shear mode**: T = 0, V = V<sub>max</sub>

For typical geometries (α + Δ ≈ 30°–60°) and moderate friction angle, **axial mode** wins. Shear mode wins for very flat planes (α + Δ → 0°).

## Input fields

| Field | Notes |
|---|---|
| φ bar [mm] | bar diameter |
| L effective [m] | length crossing the failure plane and anchoring into intact rock |
| φ hole [mm] | borehole diameter (= bar diameter for self-drilling bars) |
| z avg [m] | average bulb depth from ground surface |
| α ref. [°] | reference inclination of the nail (for K<sub>α</sub> Caquot in soil) |
| f<sub>y</sub> [MPa] | bar yield strength (typical 391 B450C, 826 SRS, 950 HD) |
| η · work rate [%] | steel work rate (default 70% per GeoStru desktop; 100% for full ULS yield) |
| f<sub>ck</sub> grout [MPa] | cubic compressive strength of cement grout (typical 25–35 MPa) |
| β · steel↔grout bond [-] | 0.5 plain bars · 0.7–1.0 ribbed bars · 1.0 self-drilling |
| in rock / in soil toggle | switches between σ<sub>c</sub> rock and (γ, φ, c) soil parameters |
| σ<sub>c</sub> rock [MPa] | rock compressive strength (15–100 MPa typical) |

In the right panel **"Design resistances · nails / anchors"** you see the complete breakdown + NTC R.2/R.3/R.4/R.5 checks.

## Typical use

- **Surface stabilisation of slopes**: nails 3–6 m long crossing the failure plane shallowly
- **Tunnel portals**: forepoling with 6–9 m self-drilling nails
- **Cut faces**: pattern nailing 2.5×2.5 m spacing, φ32 bars

[See also active anchors →](tiranti.md)
