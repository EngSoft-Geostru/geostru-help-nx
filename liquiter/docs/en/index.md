# LiquiTer NX — Liquefaction analysis

**LiquiTer NX** is the GeoStru web software for the **liquefaction analysis**
of saturated soils under seismic loading. Enter the stratigraphy, seismic
parameters and pick a method (Seed, Tokimatsu, Boulanger-Idriss, Andrus-Stokoe)
to obtain the **safety factor FSL** for each depth, the Liquefaction Potential
Index (LPI) and post-seismic settlements. Compliant with NTC 2018 and Eurocode 8.

[**Open LiquiTer NX**](https://nx.geostru.ai/liquiter/){ .md-button .md-button--primary }
[5-minute Quickstart](quickstart.md){ .md-button }

---

## What it does, in short

- **Input**: stratigraphy (γ, N-SPT, qc, clay fraction, Vs), seismic parameters
  (a_g, Mw), water table depth, code (NTC 2018 / EC8).
- **Calculation methods**: Seed (1971), Tokimatsu (1983), Boulanger-Idriss (2014),
  Andrus-Stokoe (Vs), Ishihara-Yoshimine (post-seismic settlements).
- **Output**: safety factor FSL vs depth, LPI index, settlements,
  Word `.docx` report, CSV export.

## Who it's for

- **Geologists and geotechnical engineers** assessing the liquefaction
  susceptibility of a site in compliance with NTC 2018 (chap. 7.11.3.4) or
  EC8 (EN 1998-5).
- **Consulting studios** producing technical opinions for foundation design,
  retaining structures, building in seismic zones.

## How to get started

1. Open [`nx.geostru.ai/liquiter/`](https://nx.geostru.ai/liquiter/)
2. Load a sample dataset or enter the stratigraphy
3. Set seismic parameters (a_g · Mw · code)
4. Pick the calculation method
5. Press **Run calculation** → FSL vs depth + LPI + settlements
6. Export to Word / CSV

[See the complete workflow →](workflow.md)

## Manual chapters

### Getting started

- [**Quickstart**](quickstart.md) — 5 minutes from first access to first report
- [**Complete workflow**](workflow.md) — detailed input → calculation → export sequence

### Input

- [**Input data**](dati-input.md) — description of every field (site,
  water table, seismic, stratigraphy)

### Calculation

- [**Calculation methods**](metodi.md) — Seed · Tokimatsu · Boulanger-Idriss ·
  Andrus-Stokoe · Ishihara-Yoshimine. When to use which, formulas, references.

### Output

- [**Exports**](esportazioni.md) — Word report, CSV, FSL/LPI interpretation

### Reference

- [**FAQ**](faq.md) — frequently asked questions

---

*Found an error or want to suggest content?
[Contact us](mailto:info@geostru.ai?subject=Help%20LiquiTer%20NX) — thanks!*
