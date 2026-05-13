# Full workflow

The typical Runoff Lab NX analysis, from rainfall series to flood
hydrograph at a basin outlet section.

## Diagram

```
┌────────────────────┐
│ Station + series   │  annual h_max series for 60′, 3h, 6h, 12h, 24h
└─────────┬──────────┘
          ▼
┌────────────────────┐
│ Probabilistic      │  Gumbel / GEV / Pearson III / TCEV
│ analysis           │  → h(T) for T = 5, 10, 50, 100, 200 years
└─────────┬──────────┘
          ▼
┌────────────────────┐
│ Rainfall curve     │  log-log fit:  h = a · t^n  for fixed T
└─────────┬──────────┘
          ▼
┌────────────────────┐
│ Hyetograph         │  synthetic (Chicago design storm)
└─────────┬──────────┘
          ▼
┌────────────────────┐
│ SCS-CN hydrograph  │  CN, Tlag, area → Q(t), Q_peak
└────────────────────┘
```

Each box maps to a side panel in the UI. Data flows downward: change a
series, recompute upstream, and everything downstream regenerates.

---

## 1. Station and series

In the **Station** panel enter:

- **Metadata**: name, code, basin, municipality / province / region.
- **Coordinates**: latitude / longitude + altitude. Used for documentation
  in the final report.
- **Observation period**: start and end year of the historical series.
- **Instrument**: type (recording rain gauge, etc.).

Below, for each **duration** (60′, 3h, 6h, 12h, 24h, or custom) paste the
annual maxima in mm. Practical tips:

- copy from an Excel column and paste into the box — the parser splits
  on newlines;
- supports `.` and `,` as decimal separator;
- a duration with fewer than 2 values is excluded from analyses and gets
  a small "skipped" badge.

## 2. Probabilistic analyses

In the **Analyses** panel click *Add* → pick a family. The 4 supported
families:

| Family | Method | When to use |
|--------|--------|-------------|
| **Gumbel** | Moments, Maximum Likelihood | Default in many Italian annuals; simple and well-validated for extremes. |
| **GEV** | L-moments (Hosking) | More flexible than Gumbel; handles heavy tails (catastrophic events). |
| **Pearson III** | Moments (Foster/Kite) | Anglo-Saxon tradition; useful when the series shows marked skewness. |
| **TCEV** | Levels 0-3, regionalised VA.PI. | Italy-only; level 3 fully exploits the VA.PI. regionalisation. |

Each analysis computes:

- distribution parameters;
- heights \(h(T)\) for standard \(T\) values;
- KS and χ² goodness-of-fit tests;
- **Q-Q plot** observed vs theoretical.

[Mathematical detail →](elaborazioni.md)

!!! note "Comparing methods"
    Add multiple analyses for the same station. The output table puts the
    h(T) values from each method side-by-side: instant comparison, visual
    uncertainty discrimination.

## 3. Rainfall curves

In the **Curves** panel → *Add*. Select:

- the source **analysis** (e.g. *Gumbel-moments — 60′/3h/6h/12h/24h*);
- the **return period** (T = 5, 10, 50, 100, 200 years or custom).

Log-log fitting returns:

$$
h(t) = a \cdot t^n
\qquad
i(t) = a \cdot t^{n-1}
$$

with \(t\) in hours. The page shows the curve overlaid on the observed
points \((d_i, h(d_i, T))\) for visual inspection.

[Details →](curve.md)

## 4. Synthetic hyetographs

In the **Hyetographs** panel → *Add*. Select:

- source **curve**;
- event **total duration** (e.g. 60, 120, 360 min);
- **peak position** \(r \in [0, 1]\) (Chicago design storm).

The output is a stepped hyetograph with configurable resolution (default 1 min).

[Details →](pluviogrammi.md)

## 5. SCS-CN hydrograph

In the **Hydrographs** panel → *Add*. Enter:

- source **hyetograph** or curve;
- **basin area** (km²);
- **Curve Number CN** (0-100);
- **lag time Tlag** (hours).

The algorithm:

1. computes **initial abstraction** \(I_a = 0.2 S\) (with \(S = 25400/\text{CN} - 254\));
2. derives **net rainfall** \(P_e = (P - I_a)^2 / (P - I_a + S)\) per timestep;
3. convolves the sequence with the dimensionless **SCS unit hydrograph** (triangular shape, peak at 0.375 Tp);
4. sums → total hydrograph \(Q(t)\) with peak discharge \(Q_p\) and time-to-peak.

[Details + CN/Tlag wizards →](scs-cn.md)

## 6. Export

`File → Export PDF report`: a single document containing everything:

- metadata and series;
- per analysis: parameters, h(T), tests;
- per curve: \(a\), \(n\), \(R^2\);
- hyetographs and hydrographs with charts;
- methodology and standard bibliographic references;
- cover page with logo and project info.

## Save and recovery

- `Ctrl+S` → save in the browser (autosave is always on).
- `Ctrl+Shift+S` → download a `.hgstudy` file (portable JSON).
- `Ctrl+O` → open a previously saved `.hgstudy`.
- If you close the tab with unsaved changes, the browser shows the native
  "Are you sure you want to leave?" prompt; the session also stays in
  localStorage and is offered for recovery on next open.
