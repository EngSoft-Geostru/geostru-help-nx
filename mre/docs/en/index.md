# MRE NX — Reinforced soil

**MRE NX** checks and designs **reinforced soil** retaining structures built with
geosynthetics: external checks (overturning, sliding, bearing capacity), internal checks
on the reinforcements (pullout and rupture), global stability with Bishop and internal
checks on **tieback** and **compound** surfaces. The calculation engine comes from GSRD,
the GeoStru reference software for reinforced soil.

![MRE NX interface: parameters on the left, section preview on the right](img/01-parametri.png)

## What it does

- **Automatic NTC 2018 combinations**: static A1+M1+R3 and, when seismic action is on,
  the seismic combination with unit factors and the resistances of table 7.11.III.
- **Design or Check**: anchorage lengths derived level by level, or imposed and verified.
- **2D section and 3D model** always up to date while you enter the data, with the
  wrap-around facing detail and a grid texture for the geosynthetics.
- **Reinforcement archive** with a catalogue, your personal archive and import from a
  manufacturer data sheet in PDF (AI).
- **Global stability** A2+M2+R2 and internal tieback/compound surfaces with animation.
- **Calculation report** written as running text with figures and charts, exportable to
  DOCX/PDF.

## Where to start

1. [Quick start](quickstart.md) — from a new project to the first calculation in 5 minutes.
2. [Design code and combinations](combinazioni.md) — how the partial factors are applied.
3. [Checks](verifiche.md) — how to read the results combination by combination.

!!! tip "AI assistant"
    The **Assistant** button opens the built-in chat: it reads the current project,
    explains the results and can open a support ticket.

![The AI assistant panel next to the project](img/15-assistente.png)

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20MRE%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mre/docs/en/index.md).*
