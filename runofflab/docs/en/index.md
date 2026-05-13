# Runoff Lab NX — User manual

**Runoff Lab NX** is the GeoStru web tool for **extreme rainfall analysis**
and **rainfall-runoff transformation**. Starting from an annual maxima
series of short-duration rainfall (60′, 3h, 6h, 12h, 24h) you get:

- **Probabilistic analyses** (Gumbel, GEV, Pearson III, regional TCEV);
- **IDF rainfall curves** \(h = a \cdot t^n\) for a given return period;
- **Synthetic hyetographs** (Chicago design storm);
- **Flood hydrographs** using the SCS-CN method.

[**Open Runoff Lab NX**](https://nx.geostru.ai/runofflab/){ .md-button .md-button--primary }
[5-minute quickstart](quickstart.md){ .md-button }

---

## Who it's for

- **Hydraulic engineers** sizing storm sewers, detention basins, spillways, road crossings.
- **Geologists** producing hydraulic compatibility studies.
- **Designers** preparing flow / return-period assessments for local authorities.

## What you can do

| Feature | What it does |
|---------|--------------|
| **Station + series** | Station metadata + annual maxima by duration. |
| **Analyses** | Parameter estimation for Gumbel, GEV, Pearson III, TCEV (4 levels). |
| **Goodness-of-fit** | Automatic Kolmogorov-Smirnov and χ² tests. |
| **Rainfall curves** | \(h = a \cdot t^n\) per \(T\), with log-log regression. |
| **Hyetographs** | Chicago design storm from an IDF curve. |
| **SCS-CN hydrograph** | Net rainfall + unit hydrograph + convolution. |
| **AI Import** | Auto-extract a rainfall series from annual report PDFs or Excel tables. |
| **Ready samples** | Three Calabria stations (Cosenza, Rende, Montalto) for exploration. |
| **Save** | `.hgstudy` file (JSON), browser autosave. |
| **Export** | Full PDF report with charts and tables. |
| **Multilingual** | IT, EN, DE, ES, RO (TCEV analyses use the VA.PI. dataset and are available only in Italian). |

## Getting started

1. Open [`nx.geostru.ai/runofflab/`](https://nx.geostru.ai/runofflab/).
2. **Station**: enter metadata and, for each duration, the annual maximum values (h<sub>max</sub> in mm).
3. **Analyses**: pick a family (Gumbel / GEV / Pearson III / TCEV) → get h(T) for T = 5, 10, 50, 100, 200 years.
4. **Curves**: from an analysis + T, compute \(a\) and \(n\) of the law \(h = a t^n\).
5. **Hyetographs** / **Hydrographs**: use the curve to build synthetic hyetographs and a flood hydrograph via SCS-CN.
6. *File → Export PDF report* for documentation.

[See the full workflow →](workflow.md)

## Manual chapters

### Getting started

- [**5-minute quickstart**](quickstart.md)
- [**Full workflow**](workflow.md)

### Method reference

- [**Probabilistic analyses**](elaborazioni.md) — Gumbel, GEV, Pearson III, TCEV
- [**Rainfall curves**](curve.md) — \(h = a t^n\) and return period
- [**Synthetic hyetographs**](pluviogrammi.md) — Chicago design storm
- [**SCS-CN hydrograph**](scs-cn.md) — Curve Number, Tlag, convolution

### Tools

- [**AI Import**](ai-import.md) — series extraction from PDF/Excel
- [**FAQ**](faq.md) — common gotchas

---

*Found an error or want to suggest content?
[Drop us a line](mailto:info@geostru.ai?subject=Help%20Runoff%20Lab%20NX) — thanks!*
