# Synthetic hyetographs (Chicago design storm)

A **synthetic hyetograph** is the time distribution of rainfall height
within a design event. While the IDF curve only tells you *how much* it
rained over a given interval, the hyetograph tells you *how* it was
distributed in time: this is the information needed to apply rainfall-runoff
transformation.

Runoff Lab NX uses the **Chicago Design Storm** (Keifer & Chu, 1957), the
standard method for building synthetic hyetographs from an IDF curve.

## Method idea

Instant intensity on either side of the peak is obtained directly from
the IDF inversion:

$$
i(t_b) = a \cdot \left(\frac{t_b}{r}\right)^{\!n-1}
\qquad
i(t_a) = a \cdot \left(\frac{t_a}{1-r}\right)^{\!n-1}
$$

with:

- \(r\) peak position (\(r = 0.4\) typical);
- \(t_b\) time before the peak;
- \(t_a\) time after the peak;
- \(a\), \(n\) parameters of the source curve.

Result: a sequence of intensities centred on the peak, asymmetrically
decreasing toward head and tail.

## Building it in Runoff Lab

1. Go to the **Synthetic hyetographs** panel → *Add*.
2. Set:
   - source **curve** (e.g. Gumbel — T=100 years);
   - event **total duration** \(D\) in minutes (60, 120, 360, …);
   - **peak position** \(r\) in \([0, 1]\);
   - **time step** \(\Delta t\) (1, 5, 10 min — default 1 min).
3. Confirm → the chart shows the bar-chart hyetograph, the table shows
   values \(\big(t_i, i(t_i)\big)\).

## Choosing \(r\)

| \(r\) | Interpretation |
|-------|----------------|
| **0.0** | Peak at start — decreasing rainfall. Saturated urban basins. |
| **0.3** | Early peak. |
| **0.4** (default) | Compromise adopted by Italian guidelines (PAI, basin authorities). |
| **0.5** | Symmetric — overestimates peak discharge on ordinary basins. |
| **1.0** | Peak at end — increasing rainfall. |

## When to use it

The synthetic hyetograph is used to:

- feed the **rainfall-runoff model** (see [SCS-CN Hydrographs](scs-cn.md));
- document the design hyetograph in hydraulic reports;
- test work sensitivity to different scenarios (\(D\), \(r\)).

!!! note "Alternative hyetographs"
    Chicago is one standard but alternatives exist (Huff, Sifalda,
    alternating blocks). Runoff Lab NX currently implements only the
    Chicago method; for almost all practical uses it's sufficient.

## Bibliography

- Keifer C.J., Chu H.H. (1957), *Synthetic Storm Pattern for Drainage Design*,
  ASCE Hydraulic Division 83.
- Watt W.E., Chow K.C.A. (1985), *A general expression for basin lag time*,
  Canadian Journal of Civil Engineering 12(2).
