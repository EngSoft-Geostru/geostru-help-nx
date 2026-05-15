# RockPlane NX

> Stability verification of rock slopes subject to **planar failure mechanism** — single persistent discontinuity with daylighting (Hoek-Bray / RocPlane).

[**Open the app**](https://nx.geostru.ai/rockplane/){ .md-button .md-button--primary }
[5-minute quickstart](quickstart.md){ .md-button }

---

## In a nutshell

- **What it does**: Limit Equilibrium (LEM) verification of a planar rock wedge, with automatic computation of the NTC §6.6 design resistance for anchors, §6.7 for passive nails (SoilNail Variant A), Clouterre criterion for N-V interaction on passive nails, R1 drape meshes and R2 cable panels.
- **For whom**: geologists and design engineers who need to validate the safety of a rock face against planar failure, size a reinforcement scheme (nailing + mesh) and produce the calculation report compliant with NTC 2018 / Eurocode 7.
- **Time to first result**: 5 minutes (sample case) → 30 minutes (real case with reinforcement).

## Typical workflow

1. Open the app: `nx.geostru.ai/rockplane/`
2. Fill in **Project details** (Description, Lat/Lon, Date, Site).
3. Enter the **wedge geometry**: H, β, α, ψ, B; optional tension crack T/θ.
4. Enter the **material**: γ, c, φ (Mohr-Coulomb on the plane) or Barton-Bandis (φb, JRC, JCS).
5. Enter optional **actions**: water (Hw/Zw/Zt), seismic kh/Ω, external force E/δ.
6. Add **reinforcement** from the catalogue: nails/anchors with NTC design, R1/R2 meshes.
7. Choose the **code approach**: Characteristic (γ=1) · NTC 2018 (A2+M2+R2) · EC7 (DA1/DA2/DA3).
8. Read **FS** at the top and the **checks** (R<sub>i</sub> ≥ E<sub>d</sub>) for each element.
9. Export the **Word report** and/or the **DXF** of the section.

[See the full workflow →](workflow.md)

## Manual chapters

### Model input
- [Wedge geometry](geometria.md) — H, β, α, ψ, B, tension crack
- [Material](materiale.md) — unit weight γ, cohesion c, friction angle φ
- [Water](acque.md) — Hw external ponded, Zw in the discontinuity, Zt in the crack
- [Pseudo-static seismic](sisma.md) — kh, kv, Ω direction
- [External force E](forze-esterne.md) — magnitude, δ inclination, G/Q load type

### Reinforcement
- [Passive nails](chiodi.md) — NTC §6.7, SoilNail Variant A, Clouterre N-V
- [Active anchors](tiranti.md) — NTC §6.6, ξ Tab. 6.6.III, γ<sub>Ra,t</sub>
- [Meshes](reti.md) — R1 drape (normal pressure), R2 caging (resisting τ)

### Computation
- [Theoretical model](modello-teorico.md) — Hoek-Bray equations (1)–(30)
- [Code approach](verifica.md) — TA · NTC · EC7 partial factors
- [Critical α](alfa-critico.md) — sweep of the failure plane dip

### Output
- [Word/DXF export](export.md) — full calculation report
- [File formats](formati.md) — `.rockplane` (JSON)

### Reference
- [Resources](risorse.md) — downloadable sample files
- [Numerical example](esempio-numerico.md) — hand-worked tracking case
- [Glossary](glossario.md) — symbols, terminology
- [FAQ](faq.md) — frequently asked questions

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20RockPlane%20NX).*
