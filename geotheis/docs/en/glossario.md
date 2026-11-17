# Glossary

Terms and symbols used in GeoTheis NX, in alphabetical order. The formulas are explained in [Theoretical background](teoria.md).

!!! note "Note"
    The letter **B** has two meanings: in the step-drawdown test it is the coefficient of linear aquifer loss (s = BQ + CQ²);
    in a leaky aquifer it is Hantush's leakage factor. The context and units tell you which one applies.

**Drawdown (s)** — Difference between the static water level and the level measured during pumping, in m. In the step-drawdown test it is
cumulative from the start of the test.

**Critical drawdown (s~c~)** — Drawdown in the well at the critical discharge, on the characteristic curve s = BQ + CQ². Without a
step-drawdown test, you enter it as the known critical drawdown.

**Residual drawdown (s′)** — Drawdown remaining during recovery, measured from the static water level.

**Stabilised drawdowns** — Steady-state drawdowns in the well and piezometers, when the cone of depression no longer expands. They are used
by Dupuit-Thiem.

**Specific drawdown (s/Q)** — Drawdown divided by discharge. In the step-drawdown test, s/Q = B + C·Q is a straight line.

**Reliability** — The program's assessment of each method: *reliable*, *indicative*, *unreliable*, *to be verified*. See
[Results](risultati.md).

**Storage coefficient (S)** — Volume of water released from an aquifer column of unit base area for a unit decline in head. Dimensionless,
between 0 and 1. It is small in a confined aquifer (10⁻⁵–10⁻³) and approaches the effective porosity in an unconfined aquifer. It is derived
from piezometers, not from the pumping well.

**Well loss coefficient (C)** — Coefficient of the quadratic loss CQ² in the step-drawdown test; in SI units, s²/m⁵; in Walton's classes,
min²/m⁵. It increases as the well becomes clogged.

**Aquifer loss coefficient (B)** — Coefficient of the linear loss BQ in the step-drawdown test, in s/m².

**Completion** — How the well is constructed: drilling, casing (blank sections, screen, sump), annulus (gravel pack, cement seal, plugs),
wellhead chamber, pump.

**Cone of depression** — Surface of the lowered water level around the well during pumping; it vanishes at the radius of influence.

**Characteristic curve** — The well's s(Q) curve, s = BQ + CQ², obtained from the step-drawdown test. It is used to select the critical
discharge.

**Type curve** — The theoretical Theis W(u) or Hantush W(u, r/B) curve onto which the piezometer readings are superimposed.

**Distance-drawdown** — Method that uses the drawdowns in several piezometers at the same time, plotted against the logarithm of distance.

**Leakage** — Water yielded to the leaky aquifer by the semipermeable layer when the head falls.

**Well efficiency (E)** — Proportion of the drawdown due to the aquifer: E = BQ/(BQ + CQ²). It decreases as discharge increases; it equals
50 % at the discharge Q = B/C.

**Confined aquifer (under pressure, artesian)** — Aquifer enclosed between two impermeable layers; the static water level is above the top
of the aquifer.

**Unconfined aquifer (phreatic)** — Aquifer whose water surface is at atmospheric pressure and falls during pumping.

**Leaky aquifer** — Aquifer beneath a semipermeable layer that supplies it by leakage; in GeoTheis NX it can be *unconfined* or *confined*
(called “semi-unconfined” and “semi-artesian” in the desktop version).

**Leakage factor (B)** — B = √(T·c), in m, where c is the hydraulic resistance of the semipermeable layer. The larger B is, the less
significant the leakage.

**Fitting** — Automatic fitting of the type curve to the readings by least squares (Levenberg-Marquardt), which gives T, S (and r/B) with
95 % confidence intervals.

**Well function W(u)** — Exponential integral of the Theis solution.

**Dynamic water level** — Water level in the well during pumping.

**Static water level** — Water level at rest, before pumping; in the Well tab it is an elevation in m a.s.l.

**Head losses** — Drawdown in the well divided into aquifer losses (linear, BQ, laminar flow) and well losses (quadratic, CQ², turbulent
flow in the screen and gravel pack).

**Permeability or hydraulic conductivity (K)** — Seepage velocity under a unit gradient, in m/s; also displayed on screen in m/day.
K = T/b (or T/H~1~).

**Piezometer** — Observation well or tube at a known distance from the pumping well, in which drawdown is measured without pumping.
It is used to derive S and the radius of influence.

**Allowable discharge** — Discharge that the program proposes for operating the well: normally the optimum discharge, limited by the
maximum tested discharge and the constraints on the dynamic water level. See [Results](risultati.md#portata-concedibile).

**Critical discharge (Q~c~)** — Discharge above which well losses increase disproportionately. You select it on the characteristic
curve; if you do not, the program proposes Q = B/C.

**Known critical discharge** — Q~c~ and s~c~ that you enter in the Test tab without a step-drawdown test (from nearby tests or the
commissioning test), together with the assumed radius of influence, for single wells.

**Operating discharge** — Discharge that you confirm for the well; it feeds the report and the cone of depression.

**Optimum discharge (Q~ott~)** — 0.9·Q~c~.

**Specific capacity (Q/s)** — Discharge per metre of drawdown: the inverse of specific drawdown.

**Fully penetrating / partially penetrating well** — Fully penetrating if the screen extends through the full thickness of the aquifer,
partially penetrating if it extends through only part of it.

**Single wells** — Methods that estimate T and K from the critical pair (Q~c~, s~c~) alone and an assumed radius of influence, as if
steady-state conditions applied. They give indicative values.

**Step-drawdown test** — Pumping at increasing discharge rates in steps of equal duration; it gives the characteristic curve, head losses,
well efficiency and critical discharge.

**Constant-rate test** — Pumping at a fixed discharge with readings over time in the well and piezometers, usually followed by recovery;
it gives T, S and R.

**Match point** — Point (W, u, s, t/r²) read by superimposing the data and the type curve; T and S are derived from it. In GeoTheis NX it is
the result of a manual adjustment or a point imported from the desktop version.

**Radius of influence (R)** — Distance from the well at which the drawdown vanishes. Obtained from Thiem's straight line through the
piezometers, from the transient radius R(t) = √(2.25·T·t/S), or assumed for single wells.

**Well radius (r~w~)** — Radius of the pumping well, in m (not the diameter).

**Hydraulic resistance (c)** — Thickness of the semipermeable layer divided by its vertical hydraulic conductivity, in s.

**Recovery** — Rise in the water level after the pump is stopped; t′ is the time since shutdown.

**Aquifer thickness (b)** — Top minus base of the confined or leaky aquifer: b = TI − SI.

**Saturated thickness (H~1~)** — In an unconfined aquifer, static water level minus base: H~1~ = LS − SI.

**Impermeable base (SI)** — Base of the aquifer.

**Impermeable top (TI)** — Upper boundary of the confined aquifer.

**Transmissivity (T)** — Discharge passing through a 1 m-wide strip of aquifer, over its full thickness, under a unit gradient:
T = K·b (or K·H~1~), in m²/s; also displayed on screen in m²/day.

**u** — Dimensionless Theis variable, u = r²S/(4Tt). Cooper-Jacob is valid for u < 0.05.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20GeoTheis%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/geotheis/docs/en/glossario.md)*
