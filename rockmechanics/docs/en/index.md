# Rock Mechanics NX

> Processing of the **geostructural survey** of rock masses carried out on site with compass and clinometer according to **ISRM** recommendations — geomechanical classifications, characteristic rock-mass parameters and stability checks for planar and wedge sliding.

[**Open the app**](https://nx.geostru.ai/rockmechanics/){ .md-button .md-button--primary }
[5-minute quickstart](quickstart.md){ .md-button }

---

## At a glance

- **What it does**: it represents and processes the discontinuity survey of a rock mass, runs the main **geomechanical classifications** (Barton, Bieniawski/Romana, Jašarević, Sen, Robertson, Singh & Goel), derives the characteristic parameters (cohesion, friction angle, deformation modulus) and checks stability for the kinematic mechanisms of **planar sliding** and **wedge sliding (Sliding 3D)**.
- **For whom**: geologists and geotechnical engineers who characterise a rock mass, classify the quality of the rock and produce the geomechanical report.
- **How many minutes**: 5 (first classification on a survey that is already prepared) → 45 (real case with several joint sets, multiple classifications and a stability check).

The survey follows the procedure described in the ISRM recommendations *"Suggested Methods for the Quantitative Description of Discontinuities in Rock Masses"*.

## Typical workflow

1. Open the app: `nx.geostru.ai/rockmechanics/`
2. Enter the **geostructural survey data**: discontinuity sets, attitude (dip direction/dip), spacing, persistence, aperture, roughness, weathering, infilling, hydraulic conditions.
3. Determine the **intact rock strength** $S_u$ (Point Load, Schmidt hammer or ISRM estimate) and the **RQD**.
4. Choose one or more **geomechanical classifications**: the app computes the quality index and the rock-mass class.
5. Read the derived **characteristic parameters** (cohesion $c$, friction angle $\varphi$, modulus $E$, GSI).
6. If needed, run the **stability check** for planar or wedge sliding, including water, seismic action and external forces.
7. Use the **utilities** for the impact force of a boulder or for the seismic susceptibility to collapse.
8. Export the **calculation report** and the graphical outputs.

[See the full workflow →](workflow.md)

## Manual chapters

### Getting started
- [Quickstart](quickstart.md) — from joint attitude to your first classification in 5 minutes
- [Full workflow](workflow.md) — the ISRM survey and the input → calculation → export sequence

### Geomechanical classifications
- [Overview and common parameters](classificazioni.md) — $S_u$, RQD, spacing, $J_n/J_r/J_a/J_w$/SRF
- [Barton (Q index)](barton.md) — underground works and general characterisation
- [Bieniawski & Romana (RMR · SMR)](rmr-romana.md) — tunnels, foundations and slopes
- [Jašarević & Kovačević (n index)](jasarevic.md) — carbonate rock masses
- [Modified RMR (Sen)](sen.md) — simplified continuous formulation
- [SRMR (Robertson)](robertson.md) — slopes in weak rock
- [Singh & Goel (N index)](singh-goel.md) — tunnels, derivation from Q

### Stability checks
- [Planar sliding](scivolamento-planare.md) — limit equilibrium on a single plane
- [Sliding 3D](sliding-3d.md) — sliding of a tetrahedral wedge

### Utilities
- [Impact force · seismic collapse](utility.md) — Paronuzzi and Harp & Noble

### Output and reference
- [Export and report](export.md) — calculation report and outputs
- [File formats](formati.md) — project and survey data
- [Resources](risorse.md) — downloadable figures and sample files
- [Glossary](glossario.md) — geomechanical symbols and terminology
- [Bibliography](bibliografia.md) — scientific references
- [Geoapp](geoapp.md) — complementary online calculations
- [FAQ](faq.md) — frequently asked questions

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Rock%20Mechanics%20NX).*
