# Dynamic Probing NX

> Processing of **dynamic penetration tests** (DPL · DPM · DPH · DPSH) and **borehole SPT** — automatic stratigraphy, geotechnical correlations, NTC 2018 subsoil category, shallow and deep foundation bearing capacity, EC7 / NTC §6.2.2 characteristic values.

[**Open the app**](https://nx.geostru.ai/dynprobe/){ .md-button .md-button--primary }
[Quick start (5 minutes)](quickstart.md){ .md-button }

---

## Overview

- **What it does**: reads field readings from a continuous dynamic test or a series of borehole SPT tests, returns the interpreted stratigraphy with characteristic geotechnical parameters and bearing capacity checks, all compliant with current standards (NTC 2018, NTC 2008, EC8, Eurocode 7).
- **Who it is for**: geologists and geotechnical engineers who need to process dynamic borings, classify the stratigraphic profile and produce the calculation report.
- **How long it takes**: 5 minutes (example .dypx file) → 30 minutes (full real case with stratigraphy, correlations and bearing capacity).

## Typical workflow

1. Open the app: `nx.geostru.ai/dynprobe/`
2. Create a new file or import a `.dypx` from the GeoStru desktop or a CSV from a datalogger.
3. Go to **General data** and fill in the site information (name, coordinates, instrument, client).
4. Enter (or check) the **blow count readings** in the Readings tab: the app immediately displays them in the N/depth chart.
5. Move to **Interpreted stratigraphy**: define the number of layers, boundaries and soil type (cohesive / non-cohesive). The app computes the mean N_SPT per layer using the selected method.
6. Consult the **Geotechnical correlations** — for each layer, a table with derived parameters (Cu, φ, Mo, Ey, Vs, γ …).
7. Check the **Subsoil category** according to NTC 2018 / NTC 2008 / EC8.
8. If needed, compute the **Bearing capacity** of a shallow or deep foundation (Meyerhof driven pile).
9. Read the **Characteristic values** EC7 / NTC §6.2.2 in the dedicated tab.
10. Export the **Word report** or the project file `.dprobe`.

## Manual chapters

| Chapter | Content |
|---|---|
| [Quick start](quickstart.md) | From file loading to first result in 5 minutes |
| [Instruments](strumenti.md) | DPL, DPM, DPH, DPSH, borehole SPT — how to enter them and relevant parameters |
| [Interpreted stratigraphy](stratigrafia.md) | How to define layers, the 7 N_SPT aggregation methods |
| [Geotechnical correlations](correlazioni.md) | Derived parameters for cohesive and non-cohesive soils, reference authors |
| [Subsoil category](categoria.md) | NTC 2018, NTC 2008, EC8 — input, calculation logic, reading the result |
| [Foundation bearing capacity](portanze.md) | Shallow foundations (6 methods) and deep foundations (Meyerhof driven pile) |
| [Characteristic values](caratter.md) | EC7 §2.4.5.2 / NTC §6.2.2 — normal, lognormal, Student-t |
| [Export and report](export.md) | Word report, AGS4, GeoSection, site plan, KMZ |
| [File formats](formati.md) | `.dprobe` (NX JSON) · `.dypx` (desktop) · CSV datalogger |
| [Resources and examples](risorse.md) | Downloadable sample files |
| [FAQ](faq.md) | Frequently asked questions |
