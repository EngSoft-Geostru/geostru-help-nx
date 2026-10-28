# Theory

This page sums up what the down-hole test measures and how Downhole NX goes from times to
velocities and moduli. The formulas are the same as in the
[validation document](validazione.md) and in the theoretical notes you can include in the
report.

## The down-hole test

The down-hole seismic test measures the **travel times** of compression (P) and shear (S)
waves between a **source at the surface**, at a distance d from the axis of a borehole, and
a **receiver** lowered into the hole to successive depths.

- The source is a plate struck vertically, to generate P waves, and sideways in both
  directions, to generate horizontally polarised shear waves (SH). It usually sits 1.5–2.5 m
  from the borehole mouth.
- The receiver is a three-component geophone clamped against the borehole wall; a
  multichannel seismograph records, and a trigger on the source sets time zero.
- The hole is cased with a pipe grouted to the wall, so that the waves reach the receiver
  without the disturbance of the annulus.
- Measurements are normally taken at 1 m spacing, keeping the orientation of the geophone
  constant.

At each depth one vertical shot and two horizontal shots in opposite directions are
recorded. Between the two S records the polarity of the shear wave **reverses**, that of the
P wave does not: this is how the first arrival of the S wave is recognised. From the records
you read the first-arrival times T~p~ and T~s~ at each depth z.

## Corrected times

The source–receiver path is inclined. For a receiver at depth z, with the source at a
horizontal distance d:

SR = √(z² + d²)

t~corr~ = t · z / SR

SR is the source–receiver distance, t the measured time, t~corr~ the time the wave would
take along the vertical. The assumption is a **straight ray path** in a horizontally layered
medium.

## Direct method

On the corrected time–depth plot (the **travel-time curve**) a homogeneous medium is a
straight line, and its slope is the velocity. The changes in slope identify the **seismic
layers**. For the layer between depths z~1~ and z~2~:

V = (z~2~ − z~1~) / [t~corr~(z~2~) − t~corr~(z~1~)]

t~corr~(z) is interpolated linearly between the two receivers next to the base, and from the
origin above the first receiver. The velocity of the layer is therefore the slope of the
**chord** between the two bases, not a least-squares line through the points of the layer.

If the corrected time does not increase between two bases, the layer has no velocity of its
own: it copies the parameters of the previous one and is marked with an asterisk.

## Interval method

For two consecutive receivers at depths z~1~ < z~2~:

V = (z~2~ − z~1~) / (t~corr,2~ − t~corr,1~)

The first interval runs from ground level, at time zero, to the first receiver.

With a single receiver the two times come from two different shots: these are
**pseudo-interval** velocities, and the trigger error enters the difference in full. Where
t~corr,2~ ≤ t~corr,1~ the method does not apply and the interval is left without a value
(“--”).

For each seismic layer of the interval method the **averages** of the values of the
intervals it contains are reported; the base of the layer always coincides with a
measurement depth.

## Dynamic elastic parameters

With the density ρ = γ / g and g = 9.80665 m/s²:

| Quantity | Formula |
|---|---|
| Poisson's ratio | ν = ½ · [(V~p~/V~s~)² − 2] / [(V~p~/V~s~)² − 1] |
| Shear modulus | G = ρ · V~s~² |
| Constrained modulus | E~d~ = ρ · V~p~² |
| Young's modulus | E = 2 · G · (1 + ν) |
| Bulk modulus | E~v~ = ρ · (V~p~² − 4/3 · V~s~²) |

Poisson's ratio is accepted only if 0 < ν < 0.5, that is with V~p~/V~s~ > √2: otherwise ν
and E show “--”. E~v~ also shows “--” if it comes out negative.

!!! warning "These are dynamic moduli"
    The moduli are small-strain moduli. They must not be used in a settlement calculation
    without a degradation law with strain level.

## Unit weight from the correlation

When the unit weight is not assigned to the measurements, it is estimated from an empirical
correlation with V~s~ [m/s] and with the mean depth z [m] of the layer or interval; γ is in
kN/m³.

For V~s~ < 800 m/s:

γ = [1 + 1 / (0.614 + 58.7 · (log~10~ z + 1.095) / V~s~)] · 9.80665

For V~s~ ≥ 800 m/s:

γ = 0.8 · log~10~ V~s~ · 9.80665

The first has the form of the correlation proposed for saturated soils by Burns and Mayne
(1996) from seismic cone measurements. It is an **estimate**: if you have measured values,
assign them in the table of the
[Measurements](misure.md#unit-weight-automatic-or-assigned) tab.

Example: V~s~ = 200 m/s, z = 5 m → γ = 18.41 kN/m³. For V~s~ = 1 000 m/s, γ = 23.54 kN/m³
at any depth.

## Equivalent velocity

V~s,eq~ = (H − z~0~) / Σ (h~i~ / V~s,i~)

over the stretches between the initial depth z~0~ and depth H, with h~i~ the thickness and
V~s,i~ the velocity of each stretch. In the Italian code NTC 2018 (§3.2.2) z~0~ is the
foundation level and H the depth of the bedrock, 30 m if it is deeper: in that case it is
V~s,30~.

- In the **direct method** the stretches are the seismic layers.
- In the **interval method** the stretches are the **measurement intervals**, with or
  without seismic layers. The arithmetic mean of the interval velocities of a layer is not
  the velocity of the layer (which is thickness divided by time), and cannot go into the
  formula. If even a single interval between z~0~ and H has no V~s~, the sum is not defined
  and the interval-method V~s,eq~ stays not computable (“--”): the stretch is not skipped.
- If the test is shorter than H, the last stretch is extended to H and the app says so.

A consequence that works as a check: in the direct method, **when H is the base of a
layer**, Σ h~i~/V~s,i~ is the corrected S-wave time at depth H. V~s,eq~ then does not
depend on where the layers above are placed, and the two methods give the same value, apart
from rounding. If H falls inside a layer, the stretch down to H takes the average velocity
of the whole layer, and the direct-method V~s,eq~ changes with the base of that layer.

## Automatic proposals

The proposals of arrival times and of seismic layers **are not part of the calculation**:
they produce input data, times and layer bases, that you accept, correct or discard. Once
accepted, the calculation is that of the sections above.

### P-wave arrival times

On the vertical channel, between the start of the record and the maximum of the trace, the
app looks for the instant k that minimises the **Akaike criterion**:

AIC(k) = k · ln σ²(x~1~…x~k~) + (n − k) · ln σ²(x~k+1~…x~n~)

where σ² is the variance of the samples before and after k. The minimum is the point where
the trace goes from noise to signal.

### S-wave arrival times

On the horizontal channels the shear wave comes after the tail of the P waves. So:

1. the horizontal component of maximum energy is built; with two shots in opposite
   directions the app works on their difference, in which the P waves cancel out;
2. a zero-phase low-pass filter at 150 Hz is applied;
3. the peak of the shear wave is located and the same criterion is applied in the window of
   1.25 periods before it.

Then the whole profile is examined. A time that deviates by more than 3 ms from the robust
(Theil–Sen) line through the times at the neighbouring depths is searched again around the
expected value and marked **doubtful**. A time that does not increase with depth, or is read
on a trace with a low signal-to-noise ratio, is doubtful too.

The zero-phase filter widens the wave train on both sides: on S waves the proposal can be a
few milliseconds early.

### Seismic layers

All subdivisions with bases on measurement depths and at least two intervals per layer are
considered. An exhaustive search (dynamic programming) picks the one whose broken line,
which in the direct method joins the corrected times at the bases, has the minimum squared
misfit from the corrected P and S times.

The number of layers m is the one that minimises

N · ln(RSS / N) + 1.5 · (2m − 1) · ln N

with N the number of times and RSS the sum of squared misfits, never lower than the reading
uncertainty (0.3 ms per time). The second term charges for each extra layer: without it, the
best subdivision would have one layer for every pair of intervals.

How good the proposals are on real data is in
[Validation](validazione.md#case-8-the-automatic-proposals).

## Rounding

The calculation proceeds on rounded values, like the desktop program it derives from:
corrected times to 4 decimals of a millisecond, velocities and unit weights to 2 decimals,
interval ν to 4, times at the layer bases to 2 decimals of a millisecond.

The effect is small but visible on thin, fast layers: 0.01 ms on a 2 m layer at 2 000 m/s
(1 ms travel time) is 1 % of the velocity.

## Limits of the method

- **The result is only as good as the arrival times.** The app can propose them, but a
  proposal is not a reading: they must always be looked at again on the traces, starting
  with those marked as doubtful. The same holds for the proposed seismic layers: they are
  the subdivision that best follows the times, not a geological interpretation. The
  interval velocity is sensitive even to small errors when the interval is
  short; the direct method averages over several receivers and is more stable, but depends
  on the choice of the seismic layers.
- **Straight ray paths.** With strong velocity contrasts near the surface the real path is
  refracted and the corrected times of the first receivers are approximate. The effect grows
  with d and dies out with depth (Kim et al., 2004). The first interval, from ground level
  to the first receiver, is the most sensitive value.
- **No correction** for borehole deviation or for the elevation of the source relative to
  ground level.
- **The classification of the subsoil is left to the designer**: V~s,eq~ is a number, and
  assigning the category takes the depth of the bedrock, which the test alone does not
  always reach.

## References

- Akaike H. (1974), *A new look at the statistical model identification*, IEEE Transactions
  on Automatic Control, 19(6). For its use on first arrivals: Maeda N. (1985), *A method for
  reading and checking phase times in auto-processing system of seismic wave data*, Zisin,
  38.
- ASTM D7400, *Standard Test Methods for Downhole Seismic Testing*.
- Auld B. (1977), *Cross-hole and down-hole Vs by mechanical impulse*, Journal of the
  Geotechnical Engineering Division, ASCE, 103(GT12).
- Burns S.E., Mayne P.W. (1996), *Small- and high-strain measurements of in-situ soil
  properties using the seismic cone penetrometer*, Transportation Research Record 1548.
- Carrara E., Rapolla A., Roberti N., *Le indagini geofisiche per lo studio del sottosuolo:
  metodi geoelettrici e sismici*, Liguori.
- Kim D.S., Bang E.S., Kim W.C. (2004), *Evaluation of various downhole data reduction
  methods for obtaining reliable Vs profiles*, Geotechnical Testing Journal, 27(6).
- Kramer S.L. (1996), *Geotechnical Earthquake Engineering*, Prentice Hall.
- D.M. 17/01/2018, *Norme tecniche per le costruzioni* (Italian building code), §3.2.2.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Downhole%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/downhole/docs/en/teoria.md).*
