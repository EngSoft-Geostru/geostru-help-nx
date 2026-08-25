# Elevations and terrain model

A number on a screen looks the same whether it is worth a centimetre or ten
metres. It matters that you know which one you are holding.

## Where they come from

Elevations are read from a **digital terrain model** of global coverage,
typically on a grid of about **30 metres** (SRTM / Copernicus class). They are
**ground** elevations, not surface elevations: buildings and tree canopies are not
represented.

## What they are good for

- feasibility studies and preliminary design;
- longitudinal profiles of an alignment;
- an initial surface for a volume estimate;
- the terrain input of a geotechnical model, while the survey has not been
  commissioned yet.

## What they do not replace

!!! danger "They are not a topographic survey"
    Between two points a few metres apart the model has nothing new to say. A
    grid finer than the resolution of the model adds nodes, not information. For
    detailed design you need a survey.

## How to get them

**On demand** — the **Elevations** button at the top samples every point on the
map.

**Automatic** — the **Sample elevation on new points** checkbox in the sidebar
makes every new point arrive already sampled.

## When something does not arrive

The elevation service may not answer. In that case:

- **a message appears**, telling you how many points out of how many did not
  receive an elevation;
- the affected points are **left as they were** — they are not written to zero;
- the status bar reads *"Elevations updated: N of M points"*.

If everything went well, no pop-up appears at all: the result is already in the
*Elevation* column and in the elevation range in the sidebar.

!!! warning "Zero is ambiguous"
    A point that was never sampled shows `0.00`, exactly like a point genuinely
    at sea level. When in doubt, fetch the elevations again and read the status
    bar: it says how many points were actually updated.

## Spotting a value that does not add up

- **An isolated spike** of tens of metres between two nearby vertices on a short
  track is almost always an artefact of the model or a mis-clicked vertex, not
  terrain.
- **An elevation far from what you expect** in an urban area may simply reflect
  that the model describes the ground, not the buildings.
- **All elevations at zero** means the sampling was never run, or it failed.

The AI assistant checks exactly these things, if you ask it to.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Maps%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/maps/docs/en/quote.md).*
