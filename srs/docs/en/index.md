---
title: SRS NX — Manual
---

# SRS NX

**SRS NX** designs and verifies **soil nailing with facing mesh** for slope
stabilisation, according to **NTC 2018 / Eurocodes**. It stabilises slopes in
soil or rock with cemented passive nails/bars and a facing mesh, sizing the
anchors until the design safety factor is reached. It is the web app of the
**GeoStru NX** suite.

[**Open the app**](https://nx.geostru.ai/srs/){ .md-button .md-button--primary }

![SRS NX interface](img/srs-interfaccia.png)

## Who it's for

Engineers and geologists designing surface stabilisation of soil or rock
slopes — road and railway cuts, excavation fronts, slopes prone to shallow
landslides — with nailing and a metal facing mesh.

## What it calculates

- The **pre-intervention safety factor FS₀**, from the slope geometry and
  the geotechnical parameters of the overburden.
- The **tension force** each nail must provide to bring the safety factor
  from the pre-intervention value FS₀ to the **design value FS_des** you set.
- The **six resistance checks** (R.2–R.7) for bar, mortar, bulb and mesh,
  each with its own safety factor.
- The **number of anchors and drilling metres** needed per 100 m² of mesh,
  and a cost estimate for the intervention.
- The **calculation report** in Word and PDF.

## How it works, in short

Describe the slope (inclination, overburden thickness, geotechnical
parameters) and the substrate (soil or rock). Pick a nail from the catalog or
enter the parameters manually, set the anchor grid spacing and the facing
mesh. SRS computes FS₀, asks for the design safety factor FS_des, and sizes
the required anchor tension accordingly. Press **Calculate** and read the
outcome of the six checks.

## The manual

| Chapter | Content |
|---|---|
| [Quick start](quickstart.md) | From opening the app to the first calculation in five minutes |
| [Interface and workflow](workflow.md) | Toolbar, sidebar, tabs and the input → calculation → checks sequence |
| [Slope and substrate](pendio.md) | Overburden, soil/rock, geotechnical parameters |
| [Seismic action](sismica.md) | Horizontal seismic coefficient K_h |
| [Nails and anchors](chiodi.md) | GEWI/TITAN catalog, manual parameters, geometry |
| [Facing mesh](rete.md) | Mesh, wire, tension and punching resistance |
| [Design checks](verifiche.md) | R.2–R.7, FS₀/FS_des/ΔFS, anchors per 100 m² |
| [AI assistant](assistente-ai.md) | Set up the project from a description, seismic coefficient from a location |
| [Report and exports](relazione.md) | Word/DOC/PDF, saving the project, GeoDropbox |
| [Example projects](esempi.md) | Ready-to-use .srs files (soil, rock) |
| [FAQ](faq.md) | Frequently asked questions |

---

## About SRS NX

Part of the **GeoStru NX** suite — professional web applications for
geology, geotechnics and hydrology.

[Open the SRS NX app](https://nx.geostru.ai/srs/) · [All NX products](https://help.nx.geostru.ai/) · [GeoStru website](https://www.geostru.ai/)

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20SRS%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/srs/docs/en/index.md).*
