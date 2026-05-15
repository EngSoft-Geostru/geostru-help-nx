# Export

Menu **Export ▾** offers four export targets.

## Calculation report (Word)

Generates a `.docx` calculation report ready for stamp and signature. Sections:

| § | Content |
|---|---|
| 1 | Introduction and code framework (NTC 2018 §6.6 / §6.7 / §6.8, EC7 Design Approaches, pseudo-static seismic) |
| 2 | Theoretical model (Hoek-Bray equations) |
| 3 | Input data (project, geometry, material, water, seismic, external, reinforcement) |
| 4 | Computed geometry |
| 5 | Design resistances of nails and anchors (per type, with breakdown and component checks) |
| 6 | Forces on the failure plane (+ Barton-Bandis diagnostics if active) |
| 7 | Verification result (sliding FS + overturning F<sub>r</sub>) |
| 8 | Warnings |
| Annex A | Code validation suite (97 automated tests) |

The report uses InvariantCulture for numerical formatting (dot decimal separator, ISO date format).

## Drawing (SVG / PNG)

Exports the currently active viewport:

- **2D tab**: serialises the SVG section as a vector image. Open in browser, Inkscape, AutoCAD, Trispace.
- **3D tab**: PNG snapshot of the WebGL canvas at the current camera angle.

## Technical drawing (DXF)

Generates a DXF R12 file with:

- Wedge polygon (slope face, upper bench, failure plane, tension crack)
- Water level at the toe
- Vertex labels O, B, C, D
- Nails/anchors at their real positions (head on the slope face, bulb distinguished from free length)
- Drape mesh skin + fixing nails grid
- Horizontal and vertical dimensions (H, slope face length, failure plane projection)
- β and α angle annotations
- Information block at the bottom (geometry, material, FS)

Compatible with AutoCAD, BricsCAD, DraftSight, Trispace NX.

## Open in Trispace NX

Opens the section directly in **Trispace NX**, the web 2D CAD editor of the GeoStru NX suite. Pattern:

1. Browser POSTs the project to `/api/rockplane/trispace-handoff`
2. Server generates the DXF + a temporary token (5 min TTL) in cache
3. Browser opens Trispace with `?importUrl=<token-url>` query parameter
4. Trispace fetches the DXF from the token URL and loads it

In development (localhost) the handoff URL is not reachable from outside; the software automatically falls back to "download DXF locally + open Trispace empty". The user then opens the file in Trispace via **File → Open**.

## File format `.rockplane`

The native project file is **JSON** with `.rockplane` extension. [See file formats →](formati.md)
