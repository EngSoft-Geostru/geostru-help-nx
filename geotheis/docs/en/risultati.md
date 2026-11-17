# Results

The **Results** tab interprets the test. The program checks which data are in the project (step-drawdown test, constant-rate test,
recovery, piezometers, stabilized drawdowns), calculates **all** the methods allowed by those data, compares them and proposes the
**design value** of transmissivity (T), hydraulic conductivity (K), storage coefficient (S) and radius of influence (R), plus the
**allowable discharge**. Each proposal is justified and remains a proposal until you confirm it.

Use this tab after entering the well and at least one test. If you do not have the step-drawdown test but know the critical discharge
of the well (from tests in nearby areas or from commissioning), you can enter it in the **Test** tab, *Known critical discharge* panel:
together with the well geometry, this is enough for the **single-well** methods, which give indicative T and K values. You do not need to start a calculation: the results update automatically whenever
the data or choices change, and viewing them does not use credits.

## How the tab is organized { #come-fatta-la-scheda }

From top to bottom:

1. **Test results**: the available data (in badges), the *Full calculation summary*, general warnings and two
   columns: **Methods calculated** (with reliability and the *proposed* label) and **Not applicable to the data** (with the reason). At the top
   right, choose the unit for T and K: m²/s or **per day** (m²/d, m/d).
2. **Design value** and **Allowable discharge**, side by side, each with the status *to be confirmed* or *confirmed*.
3. **Comparison of methods**: the table of T, K, S and R by method, with deviations above the threshold highlighted.
4. **Methods, parameters and charts**: one tab for each calculated method, with values, warnings, charts and choices.

Each method has a reliability assessment:

| Badge | Meaning |
|---|---|
| **reliable** | the method applies to the data and the result describes them well |
| **indicative** | the result relies on a weak assumption (steps not at steady state, only one piezometer, curve far from the data…): read it as an estimate |
| **not reliable** | the result must not be used (fit did not converge, S from the well, S > 1…) |
| **to be verified** | desktop-program formula not yet verified against the reference text |

A method name in the columns and in the comparison table is a link: it takes you to its tab.

## Design value { #valore-di-progetto }

The panel states which method supplies the values in use (*The program proposes:* or *Confirmed values in use:*), shows T, K,
S and R and, while they are proposed, the **justification**: why that method, whether it agrees with the second available method, and where S
and R come from.

- **Confirm the proposal** confirms T, K, S, R **and** the proposed allowable discharge together.
- **Use another method…** (menu) takes T, K and S from the method you choose; **Use for the design** in a method tab does the same.
- **Back to the proposal** removes the confirmations: the proposed values come back into use.

If you have confirmed and the data change in the meantime, the panel warns you: *With the current data the program would propose…*. The values
in use feed the report and the cone of depression.

Normally, the program prefers transient methods based on piezometers (Hantush in a leaky aquifer, otherwise Theis, then
Cooper-Jacob) to steady-state methods and step-drawdown-test methods, as indicated by Kruseman & de Ridder (1994): from the pumping well alone,
T can be derived, but not S.

## Allowable discharge { #portata-concedibile }

The panel prominently shows the proposed discharge (or the confirmed one) and below it: **Qc** (critical discharge, in red; *proposed Qc* if
you have not selected it yet), **Qopt** (optimum discharge, in green), **max Q tested** and **expected s**, the drawdown in the well at the
proposed discharge. The justification and any warnings about the dynamic level follow.

With the step-drawdown test, the rule is that of the desktop program: the allowable discharge is the **optimum discharge Q~ott~ = 0.9·Q~c~**,
never above the maximum tested discharge (beyond that, the characteristic curve is an extrapolation). The proposal also complies with the constraints on the
dynamic level: if 0.9·Q~c~ would take the level below the top of the confined aquifer or too close to the pump
intake, the program proposes the discharge that complies with them, derived from the characteristic curve. Without a step-drawdown test, the critical discharge
cannot be determined and the constant-rate test discharge is proposed, the only one for which the well behavior is known.
Without any test, with the **known critical discharge** entered in the Test tab, 0.9·Q~c~ of that discharge is proposed, and the
justification says that Q~c~ was entered by you and not derived from a test: it is a value to be confirmed with a test.

Commands (discharges in l/s):

- **Operating discharge** + **Confirm**: confirms the entered value; **Confirm the proposal** confirms the program value.
- **Critical discharge Qc** + **Set**, or **On the chart** and a click on the characteristic curve at the critical discharge (Esc to
  cancel). **Remove** removes the choice and restores the proposal. They appear only if there is a step-drawdown test.

## Comparison of methods { #confronto-fra-i-metodi }

The table reports the **mean** of T, K, S and R and the reliability for each calculated method; the row of the proposed method is highlighted.
**Show the single series too** adds one row per piezometer (or well, or step). A colored cell indicates a *deviation above
the threshold relative to another method*; below the table, **Deviations to check** explains each deviation with the recommended check.

The deviation between two values is

$$
\text{scarto} = \frac{\max(a, b)}{\min(a, b)} - 1
$$

and the warning thresholds are **30%** for T and K, **100%** for S and R (S and R are estimated by order of magnitude).

!!! tip "Tip"
    A deviation above the threshold is not resolved by averaging: it says that at least one method is outside its assumptions. Open the tabs
    of the two methods, look at the charts and choose the one whose points follow the curve or straight line.

## Methods, parameters and charts { #metodi-parametri-e-grafici }

Each calculated method has a tab (the target indicates the one in use). Inside you find the bibliographic reference, reliability,
T, K, S, R, the method warnings, charts, choices by series and, collapsed under *Method parameters, series and notes*, the
complete list of parameters (with the 95% confidence interval when hovering over the value), the table by series and the notes.

| Chart | Method | Axes |
|---|---|---|
| Characteristic curve s–Q | characteristic curve | Q (l/s), s (m) downwards; Q~c~ in red, Q~ott~ in green, zone beyond the critical discharge |
| Specific drawdown s/Q–Q | characteristic curve | Q (l/s), s/Q (m per l/s), straight line s/Q = B + C·Q |
| Rorabaugh curve | Rorabaugh | s = BQ + CQⁿ compared with n = 2 |
| Cooper-Jacob · *series* | Cooper-Jacob | t (min) on a logarithmic scale, s (m); straight line, segment used |
| Recovery · *series* | recovery | t/t′ on a logarithmic scale, s′ (m) |
| Theis · *series*, Hantush · *series* | type curves | t (min) and s (m) on a log-log scale; fitted curve and, if present, dashed match-point curve |
| Distance-drawdown, Dupuit-Thiem, distance on steps | distance methods | r (m) on a logarithmic scale, s (m) downwards, R |

Each chart can be downloaded as a PNG with the button next to the title.

## How to use it, step by step { #come-si-usa-passo-passo }

1. Open **Results** after entering the well and the tests. Read the two columns: if a method you expect is among *Not
   applicable*, the reason tells you which data are missing.
2. Look at the **Comparison**. If there are *Deviations to check*, open the tabs of the methods involved.
3. In the charts, check that the points used (solid) follow the straight line or curve. Exclude anomalous readings with a click, or narrow
   the Cooper-Jacob interval.
4. If you are working with the step-drawdown test, select the **critical discharge** on the characteristic curve.
5. Read the justifications again and press **Confirm the proposal**, or choose another method or enter the operating discharge.
6. Go to the report: it reports the values in use and the choices made.

## Choices on the charts { #scelte-sui-grafici }

The choices do not change the project readings: they only change the interpretation and are saved in the file. Below the charts, for each series,
a *Points, intervals and adjustment* panel shows the points used out of the total, how many you excluded manually and the criterion by which the
program selected the points.

### Excluding a point { #escludere-un-punto }

A click on a point excludes it from the calculation (it becomes hollow); a click on a manually excluded point restores it. **Restore all** cancels the
exclusions for the series. This applies to Cooper-Jacob, recovery, Theis, Hantush and, on the characteristic curve, to the steps: an excluded step
leaves B, C and the critical pair, but remains numbered.

### Cooper-Jacob interval { #intervallo-di-cooper-jacob }

The Cooper-Jacob straight line is valid only for sufficiently long times (u < 0.05). The program proposes the final straight segment automatically;
you can replace it with your own interval:

- enter **From t** and **to t** in minutes and press **Apply the interval**; for recovery the fields are **From t′** and **to t′**;
- or **On the chart**: click the start and then the end of the interval (Esc to cancel);
- **Back to the proposed segment** removes your interval.

The same interval can be set on the Theis and Hantush series, to limit the fit to part of the test. A hollow point
that you did not exclude is outside the segment used: to include it again, change the interval.

### Type-curve adjustment (Theis and Hantush) { #ritocco-della-curva-tipo-theis-e-hantush }

Automatic fitting finds the T and S (and r/B for Hantush) that make the type curve follow all the piezometer readings. If you want
to impose a value, for example S from another test:

1. in the **Type-curve adjustment** row of the series, the **T (m²/s)** and **S** fields start from the fitted values;
2. enter the values to keep fixed and **leave empty** the one the program must fit to the data;
3. press **Adjust**: the adjusted curve appears dashed next to the fitted curve, and the method list shows
   *Theis (match point)* or *Hantush (match point)* with its deviation from the data.

**Back to the fit** removes the adjustment. The adjustment does not become the design value by itself: if you want to use it, press **Use for the
design** in its tab.

## Cone of depression { #cono-di-depressione }

Below the design value, a line summarizes the cone of depression that the drawing tab plots in the well section: with
which values (proposed or confirmed, and from which method), at which discharge and up to which radius. The cone discharge is the operating
discharge in use (confirmed, or the proposed allowable discharge); without one, the constant-rate test discharge.

- If T, S and the pumping duration are known: **Theis** curve (**Hantush** if the value comes from Hantush with B) at the end-of-pumping
  time, up to the transient radius of influence R(t).
- Otherwise: **Thiem** (confined aquifer) or **Dupuit** (unconfined aquifer) up to the design radius of influence R.

## Theoretical basis { #basi-teoriche }

Notation: Q discharge, s drawdown, r distance from the well, t time since the start of pumping, t′ time since shutdown, T
transmissivity, S storage coefficient, K hydraulic conductivity, b confined-aquifer thickness, H~1~ saturated thickness
of the unconfined aquifer, r~w~ well radius, R radius of influence. The calculation uses SI units (m, s, m³/s, m²/s, m/s); l/s, minutes and
daily values are for presentation only.

**Theis (1935).** Confined, homogeneous, isotropic aquifer of unlimited extent; fully penetrating well; constant discharge.

$$
s = \frac{Q}{4\pi T}\,W(u), \qquad u = \frac{r^2 S}{4 T t}, \qquad W(u) = \int_u^\infty \frac{e^{-y}}{y}\,dy
$$

**Cooper-Jacob (1946).** Logarithmic approximation of Theis, valid for u < 0.05. From the s – log~10~ t straight line, with Δs the drawdown
per logarithmic cycle and t~0~ the time at which the straight line gives s = 0:

$$
s = \frac{2{,}303\,Q}{4\pi T}\,\log_{10}\frac{2{,}25\,T\,t}{r^2 S}, \qquad T = \frac{\ln 10\; Q}{4\pi\,\Delta s}, \qquad S = \frac{2{,}25\,T\,t_0}{r^2}
$$

**Recovery (Theis 1935).** Residual drawdown s′ against log~10~(t/t′), with t = t~shutdown~ + t′:

$$
s' = \frac{2{,}303\,Q}{4\pi T}\,\log_{10}\frac{t}{t'}, \qquad T = \frac{\ln 10\; Q}{4\pi\,\Delta s'}
$$

**Hantush-Jacob (1955).** Leaky aquifer with a semipermeable layer without storage; B leakage factor, c hydraulic resistance
of the semipermeable layer:

$$
s = \frac{Q}{4\pi T}\,W\!\left(u, \tfrac{r}{B}\right), \qquad W\!\left(u, \tfrac{r}{B}\right) = \int_u^\infty \frac{1}{y}\exp\!\left(-y - \frac{(r/B)^2}{4y}\right)dy, \qquad B = \sqrt{T c}
$$

**Type-curve fitting.** This is the log-log comparison between data and type curve, performed by least squares (Levenberg-Marquardt:
Marquardt 1963, Moré 1978) on the logarithms of the drawdowns. The typical deviation between data and curve is 10^RMSE − 1, with RMSE on the
base-10 logarithms. With the match point (W, u, s, t/r²): T = Q·W/(4π·s), S = 4·T·u·(t/r²); for Hantush, additionally B = r/(r/B), c = B²/T.

**Dupuit-Thiem, steady state (Dupuit 1863; Thiem 1906).** Straight line of stabilized piezometer drawdowns against log~10~ r;
R is the distance at which the straight line gives s = 0.

$$
\text{falda confinata: } s_1 - s_2 = \frac{Q}{2\pi T}\ln\frac{r_2}{r_1}, \quad T = \frac{\ln 10\; Q}{2\pi\,\Delta s}
\qquad
\text{falda libera: } H_1^2 - h^2 = \frac{Q}{\pi K}\ln\frac{R}{r}, \quad K = \frac{\ln 10\; Q}{\pi\,\Delta Z}
$$

with Z = s·(2H~1~ − s) and T = K·H~1~.

**Distance-drawdown.** Same s – log~10~ r straight line, using piezometer drawdowns at the same time t: T = ln10·Q/(2π·Δs), r~0~
where s = 0, S = 2.25·T·t/r~0~².

**Characteristic curve (Jacob 1947).** Linear aquifer losses (BQ) and quadratic well losses (CQ²), from the s/Q against Q straight line
on the steps; well efficiency E:

$$
s = B\,Q + C\,Q^2, \qquad \frac{s}{Q} = B + C\,Q, \qquad E = \frac{B\,Q}{B\,Q + C\,Q^2}
$$

The critical discharge Q~c~ is selected on the curve; if missing, the program proposes Q = B/C, where well losses equal
aquifer losses (E = 50%). Optimum discharge Q~ott~ = 0.9·Q~c~.

**Rorabaugh (1953).** Free exponent: s = B·Q + C·Qⁿ, estimated by least squares on the drawdowns; with n = 2, Jacob is recovered.

**Well condition (Walton 1962).** Classes based on coefficient C expressed in min²/m⁵: up to 0.5, properly designed and
developed; up to 1, moderate deterioration due to clogging; up to 4, severe deterioration or clogging; above that, difficulty
restoring the well to its original condition.

**Transient radius of influence.** From the Cooper-Jacob straight line with s = 0:

$$
R(t) = 1{,}5\sqrt{\frac{T\,t}{S}} = \sqrt{\frac{2{,}25\,T\,t}{S}}
$$

**Single wells.** They use the critical pair (Q~c~, s~c~) of the step-drawdown test as a steady-state condition and an assumed radius of influence
(Dupuit-Thiem and Celico formulas for the fully penetrating well; Chiesa, Celico, Muskat, Kozeny and others for the partially penetrating well): these are
indicative estimates.

Details of the algorithms, test cases and comparisons with the desktop program are in the [validation](validazione.md) document.

### References { #bibliografia }

- Theis C.V. (1935). *The relation between the lowering of the piezometric surface and the rate and duration of discharge of a well
  using ground-water storage*. Transactions of the American Geophysical Union, 16(2), 519–524.
- Cooper H.H., Jacob C.E. (1946). *A generalized graphical method for evaluating formation constants and summarizing well-field
  history*. Transactions of the American Geophysical Union, 27(4), 526–534.
- Jacob C.E. (1947). *Drawdown test to determine effective radius of artesian well*. Transactions ASCE, 112, 1047–1070.
- Hantush M.S., Jacob C.E. (1955). *Non-steady radial flow in an infinite leaky aquifer*. Transactions of the American Geophysical
  Union, 36(1), 95–100.
- Hantush M.S. (1956). *Analysis of data from pumping tests in leaky aquifers*. Transactions of the American Geophysical Union, 37(6),
  702–714.
- Rorabaugh M.I. (1953). *Graphical and theoretical analysis of step-drawdown test of artesian well*. Proceedings ASCE, 79, separate 362.
- Walton W.C. (1962). *Selected analytical methods for well and aquifer evaluation*. Illinois State Water Survey, Bulletin 49.
- Thiem G. (1906). *Hydrologische Methoden*. Leipzig, J.M. Gebhardt.
- Dupuit J. (1863). *Études théoriques et pratiques sur le mouvement des eaux dans les canaux découverts et à travers les terrains
  perméables*. 2nd ed., Paris, Dunod.
- Kruseman G.P., de Ridder N.A. (1994). *Analysis and Evaluation of Pumping Test Data*. 2nd ed., ILRI Publication 47, Wageningen.
- Chiesa G. *Idraulica delle acque di falda*. Palermo, Flaccovio.
- Celico P. *Prospezioni idrogeologiche*. Napoli, Liguori.
- Marquardt D.W. (1963). *An algorithm for least-squares estimation of nonlinear parameters*. Journal of the SIAM, 11(2), 431–441.
- Moré J.J. (1978). *The Levenberg-Marquardt algorithm: implementation and theory*. Lecture Notes in Mathematics 630, Springer.

## Example { #esempio }

!!! example "Example CELICO"
    Open the **CELICO** example from the examples list: fully penetrating well in a confined aquifer (r~w~ = 0.5 m, b = 7 m, H~1~ = 9 m), 3
    steps at 766.8 / 939.6 / 1,054.8 m³/h with s = 3.74 / 5.12 / 6.13 m, piezometers P1 at 23.5 m and P2 at 42.4 m, constant-rate test
    of 150 m³/h for 30,000 s with 18 pumping readings and 16 recovery readings, stabilized drawdowns, critical discharge selected in the file
    Q~c~ = 1,099.56 m³/h.

    - The program calculates 12 methods and proposes **Theis (automatic fitting)**, which agrees with Cooper-Jacob.
    - Theis fit: T = 4.34·10⁻³ m²/s and S = 7.03·10⁻³ on P1; T = 1.08·10⁻² m²/s and S = 5.40·10⁻³ on P2. Cooper-Jacob:
      4.231·10⁻³ m²/s and 7.32·10⁻³ on P1, 1.058·10⁻² m²/s and 5.61·10⁻³ on P2.
    - Design R = 76.5 m, from the Thiem straight line through the piezometers at steady state.
    - Characteristic curve: B = 2.3894·10⁻³ h/m², C = 3.2486·10⁻⁶ h²/m⁵, efficiency 42.64% at the optimum discharge.
    - Allowable discharge: 0.9·Q~c~ (about 275 l/s) would take the dynamic level below the top of the confined aquifer, so the
      program proposes the lower discharge that keeps the level at the top.
    - The comparison reports that the step-drawdown-test methods (T ≈ 5·10⁻² m²/s) are far from those of the constant-rate test
      (4–11·10⁻³ m²/s).

    The CELICO data are constructed (the P2 readings are those of P1 × 0.4): they are used to test the calculation and do not describe a
    real aquifer.

## Limitations { #limiti }

- **Theis and Cooper-Jacob** assume a confined, homogeneous, isotropic and unlimited aquifer, a fully penetrating well of negligible radius and
  constant discharge. In an unconfined aquifer and with a partially penetrating well, the program still calculates, with a warning, but **without**
  the Jacob correction s′ = s − s²/(2H) and without the Neuman model: the result applies to drawdowns that are small relative to the saturated thickness.
- **Hantush** is calculated only in a leaky aquifer and does not consider storage in the semipermeable layer.
- **S from the pumping well is not reliable** (head losses, uncertain effective radius): readings in a piezometer are required for S.
- The **step-drawdown-test** methods on piezometers and the **single-well methods** are indicative: they use end-of-step drawdowns, not
  steady-state drawdowns, or an assumed radius of influence. Four formulas for partially penetrating wells (Muskat, Girinsky, “L/b − L/2r”, Chiesa
  types B and C) are marked *to be verified*.
- Not modeled: wellbore storage and skin, drawdown derivative, delayed drainage in an unconfined aquifer, recharging
  or impermeable boundaries (image wells), anisotropy, variable discharges other than steps, interference among multiple wells.
- The proposals are decision support: the designer chooses and signs off the design value.

## Frequently asked questions { #domande-frequenti }

**Why is a method listed as “Not applicable”?**
The data it requires are missing: the reason is written next to the name (for example, piezometer readings, stabilized drawdowns, at least
two piezometers at different distances, leaky aquifer for Hantush).

**Theis and Cooper-Jacob give different values: which should I use?**
If the deviation is within 30%, the choice is immaterial and the program proposes Theis. Above that, check in the Cooper-Jacob chart that
the segment used is truly straight and at long times.

**I excluded a point by mistake.**
A second click on the point restores it; **Restore all** cancels all exclusions for the series.

**The adjustment does not change the design value.**
This is intentional: the adjustment appears as a separate method (*match point*). To use it, press **Use for the design** in its tab.

**Why is the allowable discharge lower than 0.9·Q~c~?**
Because 0.9·Q~c~ exceeds the maximum tested discharge, or would take the dynamic level below the top of the confined aquifer or
below the pump intake. The justification states which case applies.

**Can I view T in m²/day?**
Yes: at the top right of the tab, **T and K in** → **per day**. Only the presentation changes; the adjustment fields remain in m²/s.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20GeoTheis%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/geotheis/docs/en/risultati.md)*
