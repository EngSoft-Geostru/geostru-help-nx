# SPW NX

**SPW NX** is the GeoStru app for the design and verification of **embedded retaining walls**. It covers reinforced concrete piles, micropiles and diaphragms, with anchors, struts, loads and groundwater. The construction sequence is described by stages.

The central drawing shows the model as you build it. Results include diagrams, envelopes, governing conditions, checks and reinforcement.

[**Open SPW NX**](https://nx.geostru.ai/spw/){ .md-button .md-button--primary }

## Who it is for

It is for geotechnical and structural engineers designing an excavation supported by a retaining wall. You can start from a new project, an example or a `.spwx` file from the desktop program.

## What it does

- defines the site and seismic parameters according to NTC 2018;
- organises combinations before stages, with code factors and documented exceptions;
- uses one stratigraphy and one wall type throughout the project;
- follows excavations, backfilling, installation, prestressing, loads and groundwater changes as events;
- provides a limit equilibrium model (LEM) and a spring-based finite element model (FEM);
- shows displacements, bending moment, shear, axial force, pressures and ground reaction;
- checks sections, anchors, struts and geotechnical, hydraulic and serviceability conditions;
- produces the Word report and DXF drawings and passes data to Computo NX, PDM NX and CAD Tools;
- receives the site position from Atlante NX.

!!! note "Two calculation methods"
    In the **Calculation** step choose **FEM** (wall on springs, with displacements and stage history) or **LEM** (limit equilibrium, for embedment and internal forces of simple schemes). On-screen calculation is free with both methods.

## The ten steps

| Step | Contents |
|---|---|
| 1. Project | work data, studio, site, codes and seismic action |
| 2. Combinations | factor matrix, verification scope and exceptions |
| 3. Ground | ground surface, stratigraphy, subgrade reaction and initial water table |
| 4. Wall | type, geometry, materials, reinforcement and capping beam |
| 5. Elements | anchors, struts and loads, each with its own identifier |
| 6. Stages | construction events in chronological order |
| 7. Calculation | method, earth pressure theories, FEM options and run |
| 8. Results | details, diagrams, envelopes and governing conditions |
| 9. Checks and reinforcement | STR, GEO, HYD, UPL, SLE outcomes and final reinforcement |
| 10. Report and export | report preview and Word, DXF drawings, links to Computo NX, PDM NX and CAD Tools |

## Free and paid actions

Modelling, **on-screen calculation**, drawings, results and report preview use no credits. The Word report, DXF and opening in CAD Tools use **10 credits**. Each assistant message uses **3**. A failed operation is not charged.

See [Credits](crediti.md) for details.

## Session and saving

The project remains in the session for **30 minutes of inactivity**. Save your work with **File → Save** or **Save as…** to a `.spwnx` file. You can also use **GeoDropbox**.

!!! warning "Warning"
    “Saved” in a step means saved to the session. It does not mean that the project has been saved to a file on your computer.

## Manual map

| Chapter | Contents |
|---|---|
| [Quick start](quickstart.md) | an imported example, calculation and results |
| [Workflow](workflow.md) | the ten steps, one by one |
| [Combinations](combinazioni.md) | matrix, scopes, exceptions and factors to be confirmed |
| [Stages](fasi.md) | events, persistent state and thumbnails |
| [Methods](metodi.md) | LEM, FEM, earth pressure, seismic action, water, supports and checks |
| [Desktop import](importazione-desktop.md) | `.spwx` files, import report and model differences |
| [Formats](formati.md) | `.spwnx`, `.spwx`, Word, DXF and GeoDropbox |
| [Credits](crediti.md) | free actions, rates and failed operations |
| [Assistant](assistente.md) | reading the manual and project, changes and limits |
| [Validation](validazione.md) | references, comparisons and scope limits |
| [Glossary](glossario.md) | retaining wall terms |
| [Frequently asked questions](faq.md) | answers to common questions |

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/spw/docs/en/index.md).*
