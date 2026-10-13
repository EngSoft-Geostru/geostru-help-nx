# Validation and differences from the desktop version

Clause **10.2 of the Italian building code NTC 2018** asks the **designer** to assess the
reliability of the calculation code they use. That judgement is yours; our job is to give
you the material to form it: fields of use and limits, theoretical basis, test cases that
are fully worked and repeatable.

This page is the summary. It is a **validation**, carried out by those who develop the
program and verifiable by anyone: no third-party body is involved.

If you come from the desktop program and want to know why a number has changed, go to
[Differences from the desktop program](#differences-from-the-desktop-program).

## Fields of use and limits

Downhole NX processes the **down-hole seismic test**: a source at the surface, at a distance
d from the borehole axis, and a receiver lowered to successive depths. From the
first-arrival times of P and S waves it computes:

- the source–receiver distance and the **corrected times** for the obliquity of the path;
- with the **direct method**, for each seismic layer defined on the travel-time curve:
  V~p~, V~s~, unit weight, Poisson's ratio, G, E~d~, E, E~v~;
- with the **interval method**, the same parameters between two consecutive receivers and
  their averages per seismic layer;
- the **equivalent velocity** V~s,eq~ between an initial depth and a depth H (V~s,30~ with
  H = 30 m).

**Limits**

- **The result is only as good as the arrival times.** The app can propose them, but a
  proposal is not a reading: they must always be looked at again on the traces, starting
  with those the app itself marks as doubtful. The same holds for the proposed seismic
  layers: they are the subdivision that best follows the times, not a geological
  interpretation.
- It assumes **straight ray paths** between source and receiver. With strong velocity
  contrasts near the surface the real path is refracted and the corrected times of the first
  receivers are approximate; the effect grows with d and dies out with depth.
- With a single receiver the interval-method velocities are **pseudo-interval** velocities:
  the two times come from two different shots and the trigger error enters the difference in
  full.
- The automatic unit weight comes from an **empirical correlation**: it is an estimate. If
  you have measured values, assign them in the table.
- The moduli are **dynamic, small-strain** moduli: they are not the moduli for a settlement
  calculation.
- It **does not assign the subsoil category**.
- It applies no correction for borehole deviation or for the elevation of the source
  relative to ground level.
- It reads SEG-2 and text traces; it does not merge P and S files with different numbers of
  channels.

## Theoretical basis

The formulas, with the references, are on the [Theory](teoria.md) page: corrected times,
direct method, interval method, elastic parameters, unit-weight correlation, equivalent
velocity, automatic proposals, rounding.

## Test cases

Eight cases, repeated automatically at every version of the program. The first five have a
**closed-form** reference that anyone can redo by hand; the sixth is the comparison with the
desktop program; the seventh covers anomalous inputs; the eighth the automatic proposals.

| Case | Subject | Reference | Outcome |
|---|---|---|---|
| 1 | Homogeneous medium, V~p~ = 1 500 and V~s~ = 300 m/s, d = 3 m, 20 receivers | exact times of the straight path | interval V~s~ 299.98 ÷ 300.02 (≤ 0.01 %); V~p~ ≤ 0.03 %; V~s,eq~ = 300.0 |
| 2 | Two layers: 0–8 m at 600 / 200 m/s, 8–20 m at 1 800 / 450 m/s | closed form | V~s~ 200.0 and 450.0; V~p~ 600.0 and 1 800 ± 3; V~s,eq~ = 300.0 |
| 3 | Elastic parameters with γ = 19.6133 kN/m³, V~s~ = 200, V~p~ = 400 m/s | hand calculation | ν = 0.3333; G = 80.00; E~d~ = 320.00; E = E~v~ = 213.33 MPa |
| 4 | Unit weight from the correlation | hand calculation | 18.405 kN/m³ (V~s~ = 200 m/s, z = 5 m); 23.536 (V~s~ = 1 000 m/s) |
| 5 | V~s,eq~ of a known column: 0–10 m at 200, 10–30 m at 400 m/s | hand calculation | 300.00 between 0 and 30 m; 333.33 between 5 and 30 m; 200.00 between 0 and 10 m |
| 6 | Example of the desktop program | desktop program | see below |
| 7 | Anomalous inputs | expected behaviour | see below |
| 8 | Automatic proposals of times and seismic layers | operator's readings, known profiles | see below |

The deviations in cases 1 and 2 are the effect of rounding: corrected times to 4 decimals
of a millisecond, times at the bases to 2. On a 1 m interval at 1 500 m/s they amount to
± 0.2 m/s.

**Consistency check (case 5).** In the direct method the sum of the travel times through the
layers is the corrected S-wave time at H: V~s,eq~ cannot depend on where the layers are
placed. On the example it comes out at 242.86 m/s with one layer, with five layers and in
the interval method, with or without seismic layers.

### Case 6 — the desktop example

This is the project you open with **File → Open the example**: 30 receivers every metre
from 1 to 30 m, d = 2.6 m, automatic unit weight, five seismic layers with the bases saved
by the desktop program (5.04 – 10.30 – 17.78 – 25.32 – 30.11 m).

**Corrected times and interval method** match the desktop program to the last printed digit,
on all 30 rows. For instance, first interval (0–1 m): V~p~ = 348.21 and V~s~ = 163.09 m/s,
γ = 20.71 kN/m³, ν = 0.3595, G = 56.17, E~d~ = 256.06, E = 152.73, E~v~ = 181.17 MPa.

**Direct method.** With the conventions of the desktop program put back into the
calculation, Downhole NX returns exactly the desktop numbers: this shows that the deviations
below are the declared corrections, and nothing else.

| Layer | Base [m] | V~p~ [m/s] | V~s~ [m/s] | γ NX | γ desktop | G NX [MPa] | G desktop |
|---|---|---|---|---|---|---|---|
| 1 | 5.04 | 367.35 | 182.74 | 18.77 | 18.04 | 63.90 | 61.42 |
| 2 | 10.30 | 482.57 | 209.31 | 18.19 | 18.54 | 81.28 | 82.81 |
| 3 | 17.78 | 1 108.15 | 202.00 | 17.56 | 18.07 | 73.04 | 75.20 |
| 4 | 25.32 | 1 702.03 | 337.21 | 19.27 | 20.05 | 223.39 | 232.49 |
| 5 | **30.00** | **1 181.82** | **409.45** | 19.84 | 21.17 | 339.12 | 379.20 |

In the desktop program layer 5 has its base at 30.11 m, V~p~ = 1 209.60 and
V~s~ = 419.07 m/s. **V~s,30~ = 242.86 m/s** against 243.37 for the desktop program (−0.2 %).

There are two deviations, both intended:

1. **Last layer.** The desktop program puts the base of the last layer at the slant distance
   of the last receiver (30.11 m = √(30² + 2.6²)) instead of at its depth (30 m). With the
   same time the layer comes out thicker, and its velocity is overestimated by 2.3 %.
2. **Unit weight.** The desktop program feeds the correlation with the thickness of the
   layer instead of the depth. Downhole NX uses the mean depth. The unit weights change by
   −6 % to +4 %, and with them G, E~d~, E, E~v~, which depend on them linearly. Velocities
   and ν do not change.

### Case 7 — anomalous inputs

| Input | Behaviour |
|---|---|
| Duplicate, out-of-order or non-positive depth | No calculation; the error points to the row |
| S-only test (T~p~ = 0 everywhere) | P columns “--”; V~s~, G and V~s,eq~ computed |
| A missing time at one receiver | The two intervals touching it stay “--” for that wave; times at the bases are interpolated on the measured receivers |
| Decreasing corrected time | Interval “--”, warning with the receiver number |
| V~p~ ≤ V~s~, or V~p~/V~s~ ≤ √2 | ν and E “--” (and E~v~ if negative) |
| Decreasing time at the base between two bases (direct method) | The layer takes the parameters of the previous one and is marked “\*” |

### Case 8 — the automatic proposals

The proposals do not enter the calculation: what is measured here is how close they come to
what a person chooses.

**Arrival times, on a real survey.** 18 depths from 1 to 18 m, three-channel SEG-2 records
sampled at 64 µs. The comparison is with the times the operator picked by hand.

| Wave | Deviation from the manual pick | Times marked doubtful |
|---|---|---|
| P | median 0.3 ms, maximum 1.4 ms | 4 out of 18 |
| S | median 1.4 ms, maximum 5.3 ms | 10 out of 18, including all those above 4.5 ms |

On P waves the proposal matches the operator's reading within the uncertainty of the reading
itself; the doubtful times are those that do not increase with respect to the previous
depth, by half a millisecond or less.

On S waves the deviation is a few milliseconds, on times of 40–110 ms, and more than half of
the proposals are marked doubtful. At the first two depths the shear wave is buried under
the P-wave train; between 6 and 11 m the wavelet changes shape, and there the operator's
times are irregular too (74.5 – 75.8 – 77.5 – 84.9 ms). At 18 m the deviation is 4.2 ms and
the time is **not** marked: a time that is not doubtful is not right for that reason. This
is why the S proposals are checked one by one.

**Arrival times, on synthetic traces** (damped waves with a known arrival, on noise): P
within 0.6 ms; S within +3 / −6 ms. The early pick comes from the zero-phase filter, which
widens the wave train on both sides.

**Seismic layers, on profiles with known layers** (exact times of three and of five layers,
also with 0.5 ms of noise on the times): the bases are recovered exactly, within one metre
with the noise, with no extra layers.

**Seismic layers, on the example of case 6**: the proposal is 6 – 12 – 18 – 27 – 30 m, with a
misfit of 0.57 ms; the interpreter had chosen 5.04 – 10.30 – 17.78 – 25.32 – 30 m. The
proposed bases lie on the measurement depths, one every metre: the difference is within two
receivers. V~s,30~ is the same, 242.86 m/s, as it must be (case 5).

### Repeating the cases

Case 6 is repeated by opening the example and reading the tables of the Processing tab; on
the same example **Propose seismic layers** gives the subdivision of case 8. Cases 1–5 can be redone by hand with the formulas in [Theory](teoria.md): enter the
measurements in the Measurements tab and compare.

## Differences from the desktop program

Downhole NX **does not reproduce** some behaviours of the Downhole desktop program, because
they are calculation defects. Anyone comparing an old report with a new one finds here the
reason for each deviation.

| Desktop program | Downhole NX | Why | Effect |
|---|---|---|---|
| Base of the last seismic layer at the slant distance SR | At the depth of the last receiver | SR is a distance along the ray, not a depth | Velocity of the last layer and V~s,eq~ (example: −2.3 % and −0.2 %) |
| Direct-method γ from the correlation applied to the **thickness** of the layer | From the **mean depth** of the layer | The correlation is a function of depth; the desktop program itself uses depth in the interval method | γ and moduli of the direct method (example: γ from −6 % to +4 %) |
| Interval-method seismic layer whose base does not coincide with a receiver: every layer gets the mean of the whole profile | Base snapped to the nearest receiver | A layer must average its own intervals, not all of them | Averages per layer of the interval method |
| Interval-method V~s,eq~ from the **arithmetic mean** V~s~ of the seismic layers | On the **measurement intervals** | The arithmetic mean of velocities is not the velocity of the layer: it overestimates V~s,eq~ and makes it depend on where the boundaries are | Interval-method V~s,eq~ lower, on the safe side, and equal to that of the direct method (example: 265.81 → 242.86 m/s, −9 %) |
| ν of the previous row when V~p~ ≤ V~s~; E = 2·G without ν; negative E~v~ printed | “--” | A value that cannot be computed is not a test result | Anomalous rows |
| Layers that do not reach H: H divided by the time of the existing layers | Last layer extended to H, and declared | The formula needs stretches covering the whole thickness between z~0~ and H | V~s,eq~ of tests shorter than H |
| Numerator of V~s,eq~ truncated to the integer | H − z~0~ | 25.5 m is not 25 m | V~s,eq~ when H − z~0~ is not an integer |
| Missing time treated as zero | Interval “--” | A time that was not measured is not a zero time | Tests with incomplete receivers |

**What does not change.** Corrected times, values per measurement interval (except the
anomalous rows of the table) and V~p~, V~s~, ν of the direct-method seismic layers other
than the last one match the desktop program.

**Choices of the desktop program that are kept.** These are choices of method, not defects:

- the layer velocity of the direct method is the chord between the times at the two bases,
  not a least-squares line;
- the first interval runs from ground level, at time zero, to the first receiver: with a
  shallow first receiver and a large d it is the value most sensitive to the straight-path
  assumption;
- a layer with a decreasing time at its base copies the previous one;
- the unit-weight correlation and the intermediate rounding.

!!! tip "Comparing an old report"
    Open the `.dwhx` with **File → Open…** and compare the corrected times and the
    interval-method table first: they must match. Then look for the differences where the
    table above predicts them: last layer, γ and moduli of the direct method, V~s,eq~.

## Version

This page describes Downhole NX from version 2026.1.286 (October 2026), which introduced
the automatic proposals; cases 1–7 hold from 2026.1.285. The version of the
app is in the status bar at the bottom and in the **?** button, **Version** tab.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Downhole%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/downhole/docs/en/validazione.md).*
