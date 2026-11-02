# HVSR NX — H/V spectral ratio

**HVSR NX** processes **single-station ambient noise measurements** in your browser: from the NS, EW and V traces to the H/V curve, from the
resonance frequency f~0~ with the SESAME checks to the layered model, then V~s,eq~, subsoil category and Word report. It is GeoStru's Easy HVSR
desktop program brought to the web.

[**Open the app**](https://nx.geostru.ai/hvsr/){ .md-button .md-button--primary }
[Quick start](quickstart.md){ .md-button }

## Who it is for

Geologists, geophysicists, geotechnical engineers and survey companies that take the measurement with a tromograph and must deliver its
processing: site resonance frequency, its reliability, estimated V~s~ profile and subsoil category under the Italian NTC 2018 code.

## How you work

The horizontal tabs follow the order of the job, left to right. The full description is in [Workflow](workflow.md).

1. **General data** — client, site, operator, position.
2. [**Traces**](tracce.md) — import the three-component recording.
3. [**Selection**](selezione.md) — split the recording into windows, exclude the disturbed ones.
4. [**Spectral analysis**](analisi-spettrale.md) — band, smoothing, sum of the horizontals, maps.
5. [**H/V spectrum**](spettro-hv.md) — f~0~, A~0~ and SESAME checks; then [model and search](modello.md) and
   [V~s,eq~ and category](categoria.md).
6. [**Report**](relazione.md) — Word, DXF and CSV.

Calculation runs on the server: the browser only draws and handles your gestures on the charts.

## Where to start

The [Quick start](quickstart.md) takes you to the H/V curve in a few minutes. The [Tutorial](tutorial.md) repeats a complete analysis on the project you open with **File → Open the example**, with the
numbers you should find. Before using results in a design, read [Validation and limits](validazione.md): the H/V curve alone does not determine
the V~s~ profile.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20HVSR%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/hvsr/docs/en/index.md).*
