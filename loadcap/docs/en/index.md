---
title: Loadcap NX — Manual
---

# Loadcap NX

**Loadcap NX** computes the **bearing capacity** (ultimate load) and the
**settlements** of shallow foundations, and produces the professional
**geotechnical report** according to NTC 2018 / Eurocodes. It is the web app of the
**GeoStru NX** suite, a port of the desktop Loadcap.

[**Open the app**](https://nx.geostru.ai/loadcap/){ .md-button .md-button--primary }

---

## What it computes

- **Bearing capacity** of strip, pad, raft and circular footings with the methods
  of **Terzaghi** (1955), **Meyerhof** (1963), **Hansen** (1970), **Vesic**
  (1975), **Brinch-Hansen** (EC7/EC8), **Meyerhof-Hanna** (1978, two-layer soils)
  and **Richards** (1993, seismic conditions).
- **Load combinations** with partial factors from NTC 2018 (A1/A2 · M1/M2 ·
  R1/R2/R3) and Eurocode 7 (DA1/DA2/DA3), plus SLS and seismic.
- **Additional checks**: sliding on the founding plane and punching.
- **Settlements**: elastic (Timoshenko-Goodier), oedometric (logarithmic and
  one-dimensional), **Schmertmann**, **Burland & Burbidge**, with the
  **time-settlement curve** from consolidation theory.
- **Stress state**: stress bulb, colour map, contact pressures and a 3D model.
- **NTC seismic action** with full hazard (spectrum, subsoil and topographic
  categories) and reduction of the bearing-capacity factors.

## The manual

| Chapter | Content |
|---|---|
| [Quick start](quickstart.md) | From opening the app to the first calculation in five minutes |
| [Foundation and geometry](geometria.md) | Types, B/L/H/D, embedment height, slope |
| [Stratigraphy and water table](stratigrafia.md) | Per-layer parameters, water table, paste/import |
| [Loads and combinations](carichi.md) | Design approaches, partial factors, sign convention |
| [Seismic action](sismica.md) | NTC hazard, effects on soil and structure |
| [Bearing capacity](carico-limite.md) | Methods, Nc/Nq/Nγ factors, sliding and punching checks |
| [Settlements](cedimenti.md) | Elastic, oedometric, Schmertmann, Burland, time curve |
| [Stress state and 3D](stato-tensionale.md) | Bulb, map, contact pressures, 3D model |
| [AI assistant](assistente-ai.md) | Fill from a document and geotechnical review |
| [Report and exports](relazione.md) | Geotechnical report, Word/PDF, GeoDropbox |
| [Example projects](esempi.md) | Ready-to-use validation files |
| [FAQ](faq.md) | Frequently asked questions |

---

## About Loadcap NX

Part of the **GeoStru NX** suite — professional web applications for geology,
geotechnics and hydrology.

[Open the Loadcap NX app](https://nx.geostru.ai/loadcap/) · [All NX products](https://help.nx.geostru.ai/) · [GeoStru website](https://www.geostru.ai/)

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Loadcap%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/loadcap/docs/en/index.md).*
