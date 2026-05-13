# SCS-CN hydrographs

The **SCS-CN method** (Soil Conservation Service, now NRCS) transforms
a design hyetograph into the **flood hydrograph** at a basin section.
Two steps:

1. **Net rainfall** from total rainfall via the Curve Number;
2. **Convolution** with the SCS unit hydrograph, scaled to the lag time.

## Step 1 — net rainfall

The model assumes part of the rainfall is absorbed (initial abstraction
\(I_a\)) or accumulates as potential retention \(S\):

$$
S = \frac{25400}{\text{CN}} - 254
\qquad
I_a = 0.2 \cdot S
$$

With \(S\) in mm and CN in \([0, 100]\). For total cumulative rainfall \(P\):

$$
P_e =
\begin{cases}
0 & \text{if } P \le I_a \\[1mm]
\dfrac{(P - I_a)^2}{P - I_a + S} & \text{if } P > I_a
\end{cases}
$$

\(P_e\) is the **cumulative net rainfall**. Initial losses represent
vegetal interception + surface storage. Below \(I_a\) everything infiltrates.

### Curve Number

CN depends on the hydrologic soil type (A, B, C, D — from highly permeable
to impermeable) and **land cover**. Examples:

| Cover | A | B | C | D |
|-------|---|---|---|---|
| Moderately covered woods | 30 | 55 | 70 | 77 |
| Permanent meadows | 39 | 61 | 74 | 80 |
| Clean row crops | 67 | 78 | 85 | 89 |
| Impervious urban areas | 98 | 98 | 98 | 98 |

!!! tip "Integrated CN wizard"
    In the hydrograph panel an interactive wizard lets you:
    1. split the basin into multiple sub-areas;
    2. assign **hydrologic soil** and **land cover** to each;
    3. get the **area-weighted CN** for the basin.

    See the [SCS Tables](#full-cn-tables) section for the complete tables.

## Step 2 — SCS unit hydrograph

The dimensionless SCS unit hydrograph is a triangle with:

- **time to peak** \(t_p = 0.5\,D + T_{\text{lag}}\), where \(D\) is the
  net rainfall duration and \(T_{\text{lag}}\) the basin lag time;
- **unit peak discharge** \(q_p = 484 \cdot A / t_p\) (US units; in SI:
  \(q_p = 0.208 \cdot A / t_p\) with A in km² and \(t_p\) in hours);
- **base time** \(t_b = 2.67 \cdot t_p\).

The total hydrograph is the **convolution** of the \(\Delta P_e(t)\) sequence
with the unit hydrograph:

$$
Q(t) = \sum_{k} \Delta P_e(k) \cdot u(t - k)
$$

## Lag time — \(T_{\text{lag}}\)

\(T_{\text{lag}}\) is the time between the centroid of net rainfall and the
hydrograph peak. Typical estimates:

- **SCS formula**: \(T_{\text{lag}} = 0.6 \cdot T_c\) (Tc = time of
  concentration).
- **Time of concentration**: Kirpich, Giandotti, Pasini, Pezzoli depending
  on basin morphometry.

!!! tip "Tlag wizard"
    In the panel, the Tlag calculator accepts:
    - basin area A (km²);
    - main channel length L (km);
    - average slope i (%);

    It returns \(T_c\) with four classical formulas + the suggested
    \(T_{\text{lag}}\) as 0.6 \(T_c\). Choose the value you judge best
    suited to your basin type.

## Using it in Runoff Lab

1. Go to **Hydrographs** panel → *Add*.
2. Source: a **synthetic hyetograph** already built (or a direct curve).
3. Enter:
   - **basin area** A (km²);
   - **CN** (from wizard or manual);
   - **Tlag** (from wizard or manual).
4. Confirm → \(Q(t)\) chart, table with:
   - **\(Q_p\)** (peak discharge, m³/s);
   - **\(t_p\)** (time to peak, h);
   - **\(V_{\text{tot}}\)** (total runoff volume, m³);
   - **\(P_e\)** (total net rainfall, mm);
   - net rainfall / gross rainfall ratio (runoff ratio).

## SCS-CN method limitations

- Originally developed for small US agricultural basins (≤ 250 km²).
  For large basins, a distributed model is preferable.
- The assumption \(I_a = 0.2 S\) is a simplification: for highly impervious
  urban basins, \(I_a = 0.05 S\) may be more appropriate.
- Constant (linear) Tlag — doesn't capture loss non-linearities for
  extreme floods.

## Bibliography

- Soil Conservation Service (1972, 1986), *National Engineering Handbook,
  Section 4: Hydrology*. USDA.
- Mockus V. (1957), *Estimation of total (and peak rates of) surface runoff
  for individual storms*, USDA.
- Maidment D.R. (ed., 1993), *Handbook of Hydrology*, McGraw-Hill — ch. 9 (SCS).

## Full CN tables

(For brevity, an excerpt here; the in-app wizard has complete tables for:
woods, meadows, row crops, urban areas, residential, commercial,
infrastructure, natural bare ground.)
