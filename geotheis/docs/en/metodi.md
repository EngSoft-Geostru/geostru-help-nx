# Interpretation methods

This page is the catalogue of methods that GeoTheis NX applies to tests. For each one, you will find the required data, assumptions,
results and limitations. You do not choose which ones to calculate: the program calculates **all** the methods allowed by the data and
compares them in the [Results](risultati.md) tab. A method without the necessary data appears under *Not applicable*, with the reason.

Formulas are given in abbreviated form. The theoretical background, full assumptions and bibliography are in [Theory](teoria.md);
how to read graphs, reliability and proposals is covered in [Results](risultati.md).

Notation: Q discharge, s drawdown, r distance from the well, t time since pumping started, t′ time since shutdown, T
transmissivity (m²/s), K hydraulic conductivity (m/s), S storativity (dimensionless), R radius of influence (m), b thickness
of the confined aquifer (top − base), H~1~ saturated thickness of the unconfined aquifer (static level − base), r~w~ well
radius, L screen length.

## Which data for which methods { #quali-dati-per-quali-metodi }

| Data entered | Methods calculated |
|---|---|
| Step-drawdown test, 2 valid steps | [Well characteristic curve (Jacob)](#curva-caratteristica-jacob-n-2) |
| Step-drawdown test, 3 or more valid steps | plus [Rorabaugh](#curva-caratteristica-rorabaugh-n-libero) |
| Step-drawdown test with piezometers | plus [distance-drawdown on steps](#distanza-abbassamento-sui-gradini-thiem), [Dupuit-Thiem by step](#dupuit-thiem-per-gradino), [Cooper-Jacob on test stations](#cooper-jacob-sulle-stazioni-di-prova) |
| Step-drawdown test with selected critical discharge and assumed radius of influence | plus [single wells](#pozzi-singoli) |
| No valid steps, complete **known critical discharge** (Q~c~, s~c~, assumed R) | [single wells](#pozzi-singoli) |
| Constant-rate test with the well only | [Cooper-Jacob](#cooper-jacob-abbassamento) and [recovery](#risalita-theis-retta-di-cooper-jacob) on the well: T yes, S no |
| Constant-rate test with pumping readings in piezometers | plus [Theis (automatic fitting)](#theis-fitting-automatico); with at least two piezometers at different distances, also [distance-drawdown](#distanza-abbassamento-cooper-jacob) |
| Stabilised drawdowns | plus [Dupuit-Thiem (steady state)](#dupuit-thiem-regime-stazionario) |
| Leaky aquifer with readings in piezometers | plus [Hantush (automatic fitting)](#hantush-fitting-automatico) |
| Type curve fine-tuning, or a point saved by the desktop program | plus [Theis or Hantush (match point)](#theis-e-hantush-punto-di-coincidenza) |

A step is valid if it has positive discharge and drawdown in the well. The data entry rules are in [Test](prove.md); the
aquifer type and well penetration are selected in [Well](pozzo.md).

!!! note "Note"
    The aquifer type is decisive: Hantush is calculated only for a **leaky** aquifer; steady-state Dupuit-Thiem and single wells are not
    calculated for a leaky aquifer. If the aquifer type is not specified, the constant-rate methods assume a confined
    aquifer and state this in a warning.

## Step-drawdown test { #prova-a-gradini }

Step-drawdown test methods use **end-of-step** drawdowns. They describe the well (losses, critical discharge) better
than the aquifer: the resulting T and K values are indicative compared with the constant-rate test.

### Well characteristic curve (Jacob, n = 2) { #curva-caratteristica-jacob-n-2 }

*Jacob (1947); Walton (1962).*

- **Data**: at least 2 valid steps at different discharges.
- **Assumptions**: drawdown in the well is the sum of a linear aquifer loss and a quadratic well loss.

$$
s = B\,Q + C\,Q^2, \qquad \frac{s}{Q} = B + C\,Q
$$

B and C are obtained from the least-squares straight line of s/Q against Q for the valid steps.

- **Returns**: B (s/m²), C (s²/m⁵), R² of the straight line, well efficiency E = BQ/(BQ + CQ²), the proposed critical discharge Q = B/C
  (50% efficiency), well condition according to Walton (C in min²/m⁵) and, when you have selected the critical discharge Q~c~ on the graph:
  Q~opt~ = 0.9·Q~c~, s~c~ = B·Q~c~ + C·Q~c~², the critical specific capacity Q~c~/s~c~ and the efficiency at the optimum discharge.
- **Does not return** T, K, S, R.
- **Limitations**: with only 2 steps, the straight line passes through the points and there is no goodness-of-fit check; non-positive B or C indicates steps that are too
  short or not at steady state. This is the basis of the [allowable discharge](risultati.md#portata-concedibile).

| C (min²/m⁵) | Well condition (Walton) |
|---|---|
| ≤ 0.5 | Properly designed and developed |
| 0.5 – 1 | Moderate deterioration due to clogging |
| 1 – 4 | Severe deterioration or clogging |
| > 4 | Difficult to restore the well to its original condition |

### Well characteristic curve (Rorabaugh, variable n) { #curva-caratteristica-rorabaugh-n-libero }

*Rorabaugh (1953).*

- **Data**: at least 3 valid steps.
- **Assumptions**: as for Jacob, with a variable exponent for well losses: s = B·Q + C·Qⁿ (with n = 2, this reduces to Jacob).
- **Returns**: B, C, n with the 95% interval, and the root mean square error of the drawdowns.
- **Limitations**: with 3 steps, the curve passes exactly through the points; n outside 1.5–3.5 describes the points but does not have
  Rorabaugh's physical meaning. The result is then indicative.

### Distance-drawdown on steps (Thiem) { #distanza-abbassamento-sui-gradini-thiem }

*Thiem (1906).*

- **Data**: steps with drawdowns in piezometers; for each step, at least two piezometers with drawdown decreasing with
  distance.
- **Assumptions**: for each step, a straight line of s against log~10~ r (distance-based Thiem), as if conditions at the end of the step were steady.
- **Returns**: per step, Δs per logarithmic cycle, T = ln10·Q/(2π·Δs), K = T/b (T/H~1~ in an unconfined aquifer) and R where the straight line gives
  s = 0; averages over the calculated steps.
- **Limitations**: always indicative (the steps are not at steady state). In a leaky aquifer, T is calculated as for a confined aquifer, without
  leakage.

### Dupuit-Thiem by step { #dupuit-thiem-per-gradino }

*Dupuit (1863); Thiem (1906).*

- **Data**: steps, **fully penetrating** well, at least one piezometer, **unconfined** or **confined** aquifer.
- **Assumptions**: end-of-step drawdowns treated as steady state. With two or more piezometers, the pair consisting of
  piezometers 1 and 2 is used; with only one, the well–piezometer pair is used.
- **Returns**: T and K per step, and averages. In a confined aquifer, T = Q·ln(r~b~/r~a~)/(2π·(s~a~ − s~b~)), K = T/b; in an unconfined aquifer,
  the Dupuit formula is used, T = K·H~1~.
- **Limitations**: always indicative. With the well–piezometer pair, well drawdown includes head losses and T is
  underestimated.

### Cooper-Jacob on test stations { #cooper-jacob-sulle-stazioni-di-prova }

*Cooper & Jacob (1946).*

- **Data**: steps with the end-of-step **Time**, fully penetrating well, piezometers, **confined** aquifer.
- **Assumptions**: straight line of s/Q against log~10~ t for the steps, for each piezometer.
- **Returns**: T, S (from the piezometer distance) and K = T/b.
- **Limitations**: the steps have different discharges and the straight line does not account for the superposition of effects: the result is
  indicative and is **never used for the design**.

### Single wells { #pozzi-singoli }

*Dupuit (1863); Thiem (1906); Chiesa; Celico.*

- **Data**: a critical pair (Q~c~, s~c~) and an **Assumed radius of influence R**; well geometry (r~w~, screen) and
  aquifer elevations. The pair comes from the step-drawdown test (Q~c~ selected on the graph, s~c~ = B·Q~c~ + C·Q~c~²) or, without valid
  steps, from the **known critical discharge** entered in [Test](prove.md#portata-critica-nota-senza-prova-a-gradini). Assumed R is entered in
  that panel in both cases.
- **Assumptions**: the critical pair is treated as steady state. **Unconfined** or **confined** aquifer; you must specify whether the well is
  fully or partially penetrating.
- **Returns**: T and K for each applicable formula.
- **Limitations**: always indicative (assumed steady state, assumed R). It is not calculated for a leaky aquifer.

| Well and aquifer | Formulas calculated |
|---|---|
| Fully penetrating, unconfined aquifer | Dupuit: K = Q·ln(R/r~w~)/(π·(H~1~² − H~2~²)), T = K·H~1~, with H~2~ = H~1~ − s |
| Fully penetrating, confined aquifer | Thiem: T = Q·ln(R/r~w~)/(2π·s), K = T/b |
| Partially penetrating, unconfined aquifer | Chiesa (p. 187), with the distance between the bottom of the screen and the base |
| Partially penetrating, confined aquifer | Chiesa formula 5 (type A) or 11 (types B and C), plus Muskat, Kozeny, infinite thickness (Babushkin), Halek, Girinski, Zangar, “L/b − L/2r” |

The types of partially penetrating well in a confined aquifer (Chiesa): **A** screen separated from the top and not reaching the base; **B** screen adjoining
the top and shorter than the thickness; **C** screen separated from the top and reaching the base.

!!! warning "Warning"
    Halek, Muskat, Girinski, “L/b − L/2r” and the formula for types B and C are marked **to be verified**: these are desktop program formulas not
    yet verified against the reference text. Use them as a check, not as a design value.

## Constant-rate test { #prova-a-portata-costante }

All constant-rate methods require the **Test discharge**. Those based on piezometers require the piezometer distance r
([Well](pozzo.md) tab).

### Cooper-Jacob (drawdown) { #cooper-jacob-abbassamento }

*Cooper & Jacob (1946); Kruseman & de Ridder (1994).*

- **Data**: pumping readings in the well and/or piezometers.
- **Assumptions**: logarithmic approximation of Theis, valid for u = r²S/(4Tt) < 0.05: straight line of s against log~10~ t over the final segment.
  The program automatically selects the straight-line segment; you can change it (see
  [Cooper-Jacob interval](risultati.md#intervallo-di-cooper-jacob)).

$$
T = \frac{\ln 10\; Q}{4\pi\,\Delta s}, \qquad S = \frac{2{,}25\,T\,t_0}{r^2}
$$

- **Returns**: for each series, T (with 95% interval), K, S and the segment used; averages over the piezometers and R at the end of pumping,
  R = √(2.25·T·t/S).
- **Limitations**: from the well alone, T yes (it includes the effect of losses over the initial segment), S no: S from the well is not reliable and is not
  included in the average. With fewer than 3 points on the straight line, the series is indicative. In an unconfined aquifer, it applies to drawdowns small compared with
  H~1~; in a leaky aquifer, only before leakage becomes apparent.

### Recovery (Theis, Cooper-Jacob straight line) { #risalita-theis-retta-di-cooper-jacob }

*Theis (1935); Kruseman & de Ridder (1994).*

- **Data**: pumping and recovery readings, and the time of pump shutdown.
- **Assumptions**: residual drawdown s′ against log~10~(t/t′), with t = t~shutdown~ + t′; all valid points are used.
- **Returns**: T and K for each series, and average values. It gives neither S nor R.
- **Limitations**: with the well alone, the result is indicative. A recovery T differing by more than 30% from the pumping value requires checking
  the shutdown time and straight-line segment. The point where the straight line reaches s′ = 0 provides information about the aquifer: t/t′ ≈ 1
  complete recovery, well above 1 recharge, below 1 an impermeable boundary or finite volume.

### Theis (automatic fitting) { #theis-fitting-automatico }

*Theis (1935).*

- **Data**: pumping readings in at least one piezometer (well readings are not included).
- **Assumptions**: confined, homogeneous, isotropic, infinite aquifer; fully penetrating well; constant discharge.

$$
s = \frac{Q}{4\pi T}\,W(u), \qquad u = \frac{r^2 S}{4 T t}
$$

- **Returns**: for each piezometer, T and S with the 95% interval, and the standard error between curve and data; averages over the series that
  converged and R(t) at the end of pumping.
- **How it works**: least squares on the logarithms of drawdowns (Levenberg-Marquardt), starting from Cooper-Jacob. The match
  point is a result, not an input to be selected.
- **Limitations**: reliable with a standard error up to 25%, indicative above that, and unreliable if fitting does not converge.
  There must be more points than parameters. For an unconfined or leaky aquifer and a partially penetrating well, it is calculated with a warning.

### Hantush (automatic fitting) { #hantush-fitting-automatico }

*Hantush & Jacob (1955); Hantush (1956).*

- **Data**: **leaky** aquifer (unconfined or confined), pumping readings in at least one piezometer.
- **Assumptions**: as for Theis, plus leakage from a semipermeable layer without storage; third parameter r/B.
- **Returns**: T, S, r/B for each piezometer; the leakage factor B = r/(r/B) and the hydraulic resistance c = B²/T of the
  semipermeable layer; averages and R(t).
- **Limitations**: if r/B falls below 0.001, leakage is not visible in the data: the program repeats the fitting with Theis and B and c cannot be
  determined. Storage in the semipermeable layer is not considered.

### Theis and Hantush (match point) { #theis-e-hantush-punto-di-coincidenza }

- **Data**: one match point per piezometer, created by **Fine-tuning** the type curve (see
  [Type curve fine-tuning](risultati.md#ritocco-della-curva-tipo-theis-e-hantush)) or from a desktop program file.
- **Returns**: T = Q·W/(4π·s), S = 4·T·u·(t/r²); for Hantush, also B and c.
- **Limitations**: indicative at best; unreliable if the point curve is far from the data (standard error above 50%) or gives
  S > 1. It is never proposed on its own: you put it into use with **Use for the design**.

### Dupuit-Thiem (steady state) { #dupuit-thiem-regime-stazionario }

*Dupuit (1863); Thiem (1906).*

- **Data**: **Stabilised drawdowns** in piezometers ([Test](prove.md#portata-della-prova-e-abbassamenti-stabilizzati) tab),
  **fully penetrating** well, unconfined or confined aquifer; H~1~ for an unconfined aquifer.
- **Assumptions**: steady state. With two or more piezometers, a straight line of s against log~10~ r using only the piezometers; R where the straight line gives s = 0.
  In an unconfined aquifer, the straight line is based on Z = s·(2H~1~ − s).
- **Returns**: T, K, R; with two or more piezometers and the stabilised drawdown in the well, also the theoretical drawdown at the well wall and the well
  **head losses** (measured − theoretical).
- **Limitations**: with only one piezometer, the well–piezometer pair is used and the result is indicative. It does not apply to a leaky aquifer
  (use Hantush) or to a partially penetrating well.

### Distance-drawdown (Cooper-Jacob) { #distanza-abbassamento-cooper-jacob }

*Cooper & Jacob (1946); Kruseman & de Ridder (1994).*

- **Data**: at least two piezometers at different distances, read at the same pumping time.
- **Assumptions**: straight line of s against log~10~ r at time t; the program uses the last pumping reading in which at least two piezometers
  have a drawdown. The well is not included.
- **Returns**: T = ln10·Q/(2π·Δs), r~0~ where s = 0 (used as R), S = 2.25·T·t/r~0~².
- **Limitations**: reliable with 3 or more piezometers; with 2, the straight line passes through the points. At that time, u must be below 0.05 even at
  the farthest piezometer.

## Derived quantities { #grandezze-derivate }

- **K**: taken from the method; if the method gives only T, K = T/b for confined and leaky aquifers, and K = T/H~1~ for an unconfined aquifer. Without the
  thickness, K is not calculated.
- **Transient R**: R(t) = √(2.25·T·t/S) at the end of pumping, from methods that give T and S.
- **Design value**, **allowable discharge** and **cone of depression** are not methods: the program derives them from the calculated
  methods. See [Design value](risultati.md#valore-di-progetto), [Allowable discharge](risultati.md#portata-concedibile) and
  [Cone of depression](risultati.md#cono-di-depressione).

## Summary { #riepilogo }

| Method | T | K | S | R | Other | Reliability at best |
|---|---|---|---|---|---|---|
| Well characteristic curve (Jacob) | — | — | — | — | B, C, E, Q~c~, Q~opt~, s~c~, Walton | reliable |
| Rorabaugh | — | — | — | — | B, C, n | reliable |
| Distance-drawdown on steps | ✓ | ✓ | — | ✓ | per step | indicative |
| Dupuit-Thiem by step | ✓ | ✓ | — | — | per step | indicative |
| Cooper-Jacob on stations | ✓ | ✓ | ✓ | — | never for the design | indicative |
| Single wells | ✓ | ✓ | — | — | per formula | indicative |
| Cooper-Jacob | ✓ | ✓ | ✓ (piezometers) | ✓ | segment used | reliable |
| Recovery | ✓ | ✓ | — | — | t/t′ at s′ = 0 | reliable |
| Theis (fitting) | ✓ | ✓ | ✓ | ✓ | 95% intervals | reliable |
| Hantush (fitting) | ✓ | ✓ | ✓ | ✓ | r/B, B, c | reliable |
| Match point | ✓ | ✓ | ✓ | ✓ | B, c (Hantush) | indicative |
| Steady-state Dupuit-Thiem | ✓ | ✓ | — | ✓ | well losses | reliable |
| Distance-drawdown | ✓ | ✓ | ✓ | ✓ (r~0~) | time used | reliable |

The complete reliability criteria and the order in which the program selects the method to propose are in [Results](risultati.md).

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20GeoTheis%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/geotheis/docs/en/metodi.md).*
