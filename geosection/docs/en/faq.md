# FAQ — frequently asked questions

## General

### Is GeoSection NX free?

GeoSection NX is included in the **GeoStru NX** suite with a *freemium* plan.
For up-to-date details visit [`geostru.ai`](https://www.geostru.ai/) or
write to `info@geostru.ai`.

### Do I need to install anything?

No — it's a web app accessible from
[`nx.geostru.ai/geosection/`](https://nx.geostru.ai/geosection/) with any
modern browser.

## Boreholes

### Can I import boreholes from Stratigrapher?

Yes. **Stratigrapher NX** is the companion software for **stratigraphic
columns**. Export the boreholes as `.json` (GeoStru Stratigraphy format) →
in GeoSection open **File → Import boreholes** → select the file → boreholes
come in with stratigraphy + water table + core photos already structured.

### Can I create boreholes from CSV?

Yes. Accepted format:

```csv
nome,lat,lon,quota_pc,profondita_top,profondita_base,litologia,falda
S1,41.9028,12.4964,120.5,0,2.5,silty sand,1.8
S1,41.9028,12.4964,120.5,2.5,8.0,clay,
```

Required headers: `nome`, `lat`/`lon` or `E`/`N`, `quota_pc`,
`profondita_top`, `profondita_base`, `litologia`. The borehole is identified
by `nome` — multiple rows with the same name are layers of the same hole.

### How many boreholes do I need for a section?

Minimum **2 boreholes** to generate a section (one at each end). For good
sections you typically need at least **3-5 boreholes** distributed along
the trace.

## Section

### The auto interpolation of horizons is wrong

Possible causes:

- **Boreholes too far apart** (>200 m without intermediate ones) → linear
  interpolation becomes speculative. Add intermediate boreholes if possible.
- **Highly variable stratigraphy** (sand lens, paleochannel) → linear
  interpolation doesn't capture lateral variations. Edit manually by
  dragging horizons.
- **Wrong ground-level elevations** → check that borehole elevations are
  correct.

### Can I add annotations to the section?

Yes, after generating the section, you have annotation tools:

- **Text** — labels, notes, references.
- **Arrows** — flow directions, sliding directions.
- **Geological symbols** — faults, contacts, fold disks.
- **Lines/polylines** — extra horizons (e.g. supposed top of bedrock).

## Export

### Which format for the technical report?

- **Paginated PDF** is the most common (title + section + table + photos).
- **SVG** if you want to edit graphically in Inkscape/Illustrator.
- **DXF** if the section must enter existing CAD drawings.

### The core photos in the PDF are pixelated

Increase the **export resolution** in Options → PDF Export → 300 DPI for
professional printing (default 150 DPI for file weight).

## Missing your question

[Write to us](mailto:info@geostru.ai?subject=Help%20GeoSection%20NX%20-%20FAQ)
and we'll add it here.
