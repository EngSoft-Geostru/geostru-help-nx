# Quickstart — from rainfall series to hydrograph in 5 minutes

This guide walks through the minimum path to get a flood hydrograph
starting from annual maxima of short-duration rainfall.

!!! tip "Want to try it without your own data?"
    Open the Info modal (top-right **?** icon) → **Resources** tab → click
    "**Cosenza — Metro_Cosenza**". This loads a complete station with a real
    ~30-year series. The rest of the guide works the same.

## 1. Open the study

1. Go to [`nx.geostru.ai/runofflab/`](https://nx.geostru.ai/runofflab/).
2. First time, the study is empty. You'll see **Station** metadata
   (name, code, basin, coordinates) and a list of **durations** below.
3. The header shows `*` next to the name when there are unsaved changes,
   and `Unsaved changes` in small text just below.

## 2. Enter the rainfall series

For each duration (60′, 180′, 360′, 720′, 1440′) paste the **annual maxima**
in millimetres.

- One value per line. Decimals with dot or comma.
- You need **at least 5 values** for a probabilistic analysis to make
  statistical sense; below 10-12 the results are quite uncertain.
- Durations with fewer than 2 values are skipped during analysis.

!!! example "Example"
    Duration 60′ (1 hour), years 1991-2020, Cosenza: 38.6, 41.2, 36.4, 52.1, …
    (one value per line).

Save as `.hgstudy` via `File → Save As` (or `Ctrl+Shift+S`). The file is a
portable JSON you can email or share.

## 3. Run a probabilistic analysis

In the **Analyses** panel → "**Add analysis**" → pick a family. For the
first study, start with:

- **Gumbel — Method of moments** (simple, robust, default in many Italian
  annuals).

The software computes:

- distribution parameters (\(\mu, \beta\) for Gumbel);
- rainfall heights \(h(T)\) for standard return periods (5, 10, 50, 100, 200 years);
- goodness-of-fit tests (KS and χ²).

To compare methods, also add a **GEV (L-moments)** or **TCEV Level 1**
(when in Italy and the VA.PI. dataset covers your region).

See [Probabilistic analyses](elaborazioni.md) for method details.

## 4. Build the rainfall curve

In the **Rainfall curves** panel → "**Add curve**" → pick the source analysis
and the return period (e.g. **T = 100 years**).

Log-log regression estimates the two parameters of

$$
h(t) = a \cdot t^{n}
$$

with \(t\) in hours and \(h\) in mm. Typical southern-Italy values:
\(n \approx 0.30\text{–}0.45\).

## 5. Synthetic hyetograph

From the curve, build a **design hyetograph** using Chicago or the
alternating-block method:

- **Synthetic hyetographs** panel → "Add hyetograph".
- Set **total duration** (e.g. 60 min) and **peak position** \(r\)
  (typically 0.4).
- The output is a time series of intensity \(i(t)\) — the rainfall
  "arriving" at the basin.

## 6. Flood hydrograph via SCS-CN

**Hydrographs** panel → "Add hydrograph". Enter:

- **Basin area** (km²);
- **Curve Number CN** (0-100, depends on soil + land cover);
- **Lag time Tlag** (hours).

!!! tip "CN and Tlag wizards"
    Don't know the right CN? Open the integrated **CN wizard** — pick
    hydrologic soil type and land use; CN gets area-weighted automatically.

The tool applies SCS-CN (net rainfall) and convolves with the dimensionless
SCS unit hydrograph, returning:

- volume and duration of net rainfall;
- **peak discharge \(Q_p\)** and time-to-peak;
- the full \(Q(t)\) curve.

## 7. Export the report

`File → Export PDF report` produces a single document with:

- station metadata and series;
- parameter tables for all analyses and h(T);
- rainfall curve plots;
- hyetographs and hydrographs;
- method and formulas for each section.

---

**Next steps:**
[Full workflow](workflow.md) · [Analyses in depth](elaborazioni.md) · [AI Import](ai-import.md)
