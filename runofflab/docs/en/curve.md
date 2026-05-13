# Rainfall curves

A **rainfall curve** (or IDF — Intensity-Duration-Frequency curve) links
the expected rainfall height \(h\) to a duration \(t\), for a fixed return
period \(T\):

$$
h(t, T) = a(T) \cdot t^{\, n(T)}
\qquad
i(t, T) = a(T) \cdot t^{\, n(T) - 1}
$$

with:

- \(h\) in mm, \(i\) in mm/h, \(t\) in hours;
- \(a(T)\) and \(n(T)\) derived from a log-log fit on the values
  \(h(t_i, T)\) provided by the probabilistic analyses.

## How Runoff Lab computes it

1. In the **Curves** panel → *Add* you select:
   - source **analysis** (e.g. Gumbel-moments);
   - **return period** (5, 10, 50, 100, 200 years or custom).
2. For each station duration, the height \(h(t_i, T)\) is taken from the
   fitted distribution.
3. Linear regression is applied in log-log space between \(\ln h\) and \(\ln t\):

$$
\ln h = \ln a + n \cdot \ln t
$$

   yielding \(a\) and \(n\).
4. The panel shows:
   - \(a\), \(n\), coefficient of determination \(R^2\);
   - table of observed vs curve values;
   - log-log plot with points and fitted line.

## Interpreting \(a\) and \(n\)

- \(\boldsymbol{a}\) = rainfall height for **\(t = 1\) hour** (for that \(T\)).
  Larger in wet climates or for high \(T\).
- \(\boldsymbol{n}\) = exponent of the law, always in \([0, 1]\). Typically:
  - \(n \approx 0.20\text{–}0.30\) for highly convective rainfall (short and intense);
  - \(n \approx 0.40\text{–}0.55\) for persistent frontal rainfall.

Low \(n\) → rainfall "concentrates" in short durations → small basins prone
to flash floods.

## Multiple return periods

Create a curve for each \(T\) of interest: typically 5, 50, 200 years for
hydraulic works. Overlay them on a single plot to show the "growth factor"
between return periods.

!!! tip
    Keeping at least T = 50 and T = 200 in the study is almost always
    required by a hydrological report for public works.

## When the log-log fit isn't enough

If \(R^2 < 0.95\) the 2-parameter law doesn't represent the station well.
Typical causes:

- **Sparse series** on some durations → unstable analysis.
- **Discontinuities** in the series (relocated rain gauge, historical vs
  recent period). Split the series and re-run analyses on sub-periods.
- **Scale effect**: for stations at high elevation or close to the sea,
  a single 2-parameter law may fail. Use 3-parameter models (TCEV level 3)
  that better constrain the tail.

## Export

Each curve enters the PDF report automatically with:

- parameters \(a\), \(n\), \(R^2\);
- observed vs predicted points table;
- h-t plot (log-log) and i-t plot (lin-lin) for the chosen \(T\);
- formula with numerical values substituted.
