# Full workflow

The sequence of a real project, from the on-site survey to the report. The detailed options are in the pages of the individual chapters.

## 1. The geostructural survey (ISRM)

Rock Mechanics NX represents and processes the **geostructural discontinuity survey** carried out on site with the **compass and clinometer** method, according to the ISRM recommendations *"Suggested Methods for the Quantitative Description of Discontinuities in Rock Masses"* (1978).

For each discontinuity set, the ISRM parameters are described:

| Parameter | Description | Where it counts |
|---|---|---|
| **Attitude** | dip direction and dip | orientation `A6`, SMR, stability |
| **Spacing** $s$ | mean distance between adjacent discontinuities | `A3`, RQD from $J_v$ |
| **Persistence** | continuity of the joint over the face | `A4` (v1) |
| **Aperture** | distance between the walls | `A4` (v2), $J_a$ |
| **Roughness** | at small and medium scale | `A4` (v3), $J_r$, JRC |
| Wall **weathering** | degree of degradation | `A4` (v4), $J_a$ |
| **Infilling** | nature and thickness of the material | `A4` (v5), $J_a$ |
| **Hydraulic conditions** | from dry to heavy inflow | `A5`, $J_w$ |

!!! tip "Digital acquisition of the survey"
    The survey can be acquired in the field with **eGeo Compass** or processed with **GMS (GeoMechanical Survey)**, which interfaces with the app. The joint sets and attitudes are thus imported without manual re-entry.

## 2. Intact rock strength and RQD

- **$S_u$** (uniaxial compressive strength): from a Point Load Test, Schmidt hammer or ISRM estimate.
- **RQD**: from borehole cores or estimated from the volumetric joint count $J_v$ / from the number of joints per metre.

Full definitions and equations in [Overview and common parameters](classificazioni.md).

## 3. Geomechanical classification

The method (or more than one) is chosen according to the structure and the lithology. All methods draw on the same survey:

- **Underground / general** → [Barton (Q)](barton.md), [Singh & Goel (N)](singh-goel.md)
- **Tunnels and foundations** → [Bieniawski (RMR)](rmr-romana.md)
- **Slopes** → [Romana (SMR)](rmr-romana.md), [Robertson (SRMR)](robertson.md)
- **Carbonate rock masses** → [Jašarević (n)](jasarevic.md)
- **Simplified continuous RMR** → [Sen](sen.md)

The output of each classification is: numerical index → **class** (I–V or I–IX) → rock-mass **quality** → **characteristic parameters** ($c$, $\varphi$, $E$, GSI).

!!! note "Several classifications compared"
    It is good practice to evaluate the rock mass with several methods and compare their characteristic parameters: the empirical correlations are calibrated on different contexts, and the scatter of the results is itself an indication of reliability.

## 4. Stability check

When the survey identifies a kinematically possible mechanism:

- **[Planar sliding](scivolamento-planare.md)** — a discontinuity with a dip direction close (± 20°) to that of the face and a smaller dip. Tension crack, water in the joints, seismic action and external forces are considered.
- **[Sliding 3D](sliding-3d.md)** — two sets intersecting to form a tetrahedral wedge; sliding along the line of intersection or on a single plane.

For sliding along **two joints** in the design phase of the intervention (bolts, anchors, mesh), refer to the technical sheet of [RockPlane NX](https://help.nx.geostru.ai/rockplane/en/).

## 5. Utilities

- **[Impact force of a boulder](utility.md#forza-dimpatto-di-un-masso)** on a masonry or concrete structure (Paronuzzi, 1989).
- **[Prediction of collapse due to a seismic event](utility.md#previsione-del-crollo-per-evento-sismico)** (Harp & Noble, 1993), with a susceptibility classification derived from Q.

## 6. Export

The **calculation report** is generated with the survey data, the classifications and the checks, plus the graphical outputs. See [Export and report](export.md) and [File formats](formati.md).

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Rock%20Mechanics%20NX).*
