# Theory overview

This page summarises the pumping test theory used by GeoTheis NX: aquifer types, steady and transient flow, methods for the
constant-rate test and the step-drawdown test, head losses, radius of influence and single wells. The formulas are those of the
calculation engine. How the program chooses and compares the methods is explained in [Results](risultati.md); the glossary of
symbols is in [Glossary](glossario.md).

Notation: Q discharge, s drawdown, r distance from the well, t time since the start of pumping, t′ time since the pump stopped,
T transmissivity, S storativity (storage coefficient), K hydraulic conductivity (permeability), b thickness of the confined aquifer,
H~1~ saturated thickness of the unconfined aquifer, r~w~ well radius, R radius of influence. The engine works in SI units (m, s,
m³/s, m²/s, m/s); l/s, m³/h, minutes and per-day values are for display only.

## Aquifer types { #tipi-di-falda }

| Type (Well tab) | Description | Thickness used |
|---|---|---|
| **Unconfined** | water-table aquifer: the water surface is at atmospheric pressure and is lowered by pumping | H~1~ = static level − base |
| **Confined** | confined (artesian) aquifer: enclosed between two impermeable layers, the level rises above the aquifer top | b = top − base |
| **Leaky, unconfined** | below a semi-pervious layer that feeds it, with a free surface | b, as for the confined aquifer |
| **Leaky, confined** | below a semi-pervious layer that feeds it, under pressure | b, as for the confined aquifer |

**Transmissivity** is the discharge flowing through a 1 m wide strip of aquifer, over its full thickness, under a unit gradient:
T = K·b in a confined aquifer, T = K·H~1~ in an unconfined aquifer. **Storativity** S is the volume of water released by a column of
unit base area for a unit decline in head. In a confined aquifer S is small (typically 10⁻⁵–10⁻³) because the water comes from the
compressibility of the water and of the skeleton; in an unconfined aquifer it comes from the drainage of the pores and S approaches
the effective porosity (typically 10⁻²–0.3).

In a leaky aquifer the semi-pervious layer releases water to the aquifer when the head drops (**leakage**). Its hydraulic resistance
c = thickness/vertical permeability of the semi-pervious layer defines the **leakage factor** B = √(T·c).

## Steady and transient flow { #regime-stazionario-e-transitorio }

During constant-rate pumping the cone of depression widens over time: this is **transient flow**, described by Theis, Cooper-Jacob
and Hantush, which give T and S. If the cone stops widening (recharge, leakage, recharge boundaries) the drawdowns stabilise: this is
the **steady state** of Dupuit-Thiem, which gives T (or K) and the radius of influence R but not S.

Assumptions common to the analytical methods: homogeneous, isotropic aquifer of constant thickness and infinite extent; horizontal
flow towards a fully penetrating well; constant discharge; well of negligible radius. Where your data depart from them, the program
still calculates and says so with a warning (see [Limits](risultati.md#limiti)).

## Constant-rate test { #prova-a-portata-costante }

### Theis (1935) { #theis-1935 }

Transient-flow solution in a confined aquifer:

$$
s = \frac{Q}{4\pi T}\,W(u), \qquad u = \frac{r^2 S}{4 T t}, \qquad W(u) = \int_u^\infty \frac{e^{-y}}{y}\,dy
$$

W(u) is the **well function** (the exponential integral E~1~). The engine calculates it with the Abramowitz & Stegun series (5.1.11
for u ≤ 1, continued fraction 5.1.22 for u > 1), with a relative error of the order of 10⁻¹⁵.

The classic method overlays, on a log-log scale, the s – t/r² readings on the W(u) – 1/u type curve and reads a **match point**
(W, u, s, t/r²):

$$
T = \frac{Q\,W}{4\pi s}, \qquad S = 4\,T\,u\,\frac{t}{r^2}
$$

GeoTheis NX performs the same overlay with an **automatic least-squares fit** (Levenberg-Marquardt) on the logarithms of the drawdowns
of each piezometer, and gives T and S with the 95 % confidence interval. The match point remains available as an adjustment (see
[Results](risultati.md#ritocco-della-curva-tipo-theis-e-hantush)).

### Cooper-Jacob (1946) { #cooper-jacob-1946 }

For small u the series of W(u) reduces to its first two terms, W(u) ≈ −0.5772 − ln u, and the drawdown grows linearly with the
logarithm of time:

$$
s = \frac{2.303\,Q}{4\pi T}\,\log_{10}\frac{2.25\,T\,t}{r^2 S}
$$

From the s – log~10~ t straight line, with Δs the drawdown per log cycle and t~0~ the time at which the line gives s = 0:

$$
T = \frac{\ln 10\;Q}{4\pi\,\Delta s}, \qquad S = \frac{2.25\,T\,t_0}{r^2}
$$

The approximation holds for **u < 0.05**. The program automatically uses the final segment with t > 11.25·t~0~ (i.e. u < 0.05) and
recalculates t~0~ until the selection no longer changes. On the pumping well T can be derived, S cannot: the well losses and the
uncertain effective radius distort the intercept.

### Recovery (Theis 1935) { #risalita-theis-1935 }

After the pump stops the water level recovers. By superposition (pumping that continues plus an equal injection from the stop), the
residual drawdown s′ is:

$$
s' = \frac{2.303\,Q}{4\pi T}\,\log_{10}\frac{t}{t'}, \qquad t = t_{stop} + t', \qquad T = \frac{\ln 10\;Q}{4\pi\,\Delta s'}
$$

with Δs′ the residual drawdown per log cycle of t/t′. Recovery gives T but not S. If the line reaches s′ = 0 at a t/t′ very different
from 1, the aquifer has recharge (t/t′ > 1) or an impermeable boundary or a finite volume (t/t′ < 1).

### Hantush-Jacob (1955) { #hantush-jacob-1955 }

In a leaky aquifer, with the semi-pervious layer without storage:

$$
s = \frac{Q}{4\pi T}\,W\!\left(u, \tfrac{r}{B}\right), \qquad W\!\left(u, \tfrac{r}{B}\right) = \int_u^\infty \frac{1}{y}\exp\!\left(-y - \frac{(r/B)^2}{4y}\right)dy, \qquad B = \sqrt{T c}
$$

At early times the curve follows Theis; at late times leakage flattens it towards the steady value W(0, r/B) = 2·K~0~(r/B). The
engine calculates W(u, r/B) by numerical integration (Gauss-Kronrod), not with Hantush's table. With a match point:
T = Q·W/(4π·s), S = 4·T·u·(t/r²), B = r/(r/B), c = B²/T. The program applies Hantush only if the aquifer is leaky; if the fit brings
r/B below 10⁻³, leakage is not visible in the data and the result coincides with Theis.

### Dupuit-Thiem, steady state (Dupuit 1863; Thiem 1906) { #dupuit-thiem-regime-stazionario-dupuit-1863-thiem-1906 }

With the stabilised drawdowns of the piezometers:

$$
\text{confined aquifer: } s_1 - s_2 = \frac{Q}{2\pi T}\ln\frac{r_2}{r_1}, \qquad T = \frac{\ln 10\;Q}{2\pi\,\Delta s}
$$

$$
\text{unconfined aquifer: } H_1^2 - h^2 = \frac{Q}{\pi K}\ln\frac{R}{r}, \qquad K = \frac{\ln 10\;Q}{\pi\,\Delta Z}, \qquad Z = s\,(2H_1 - s), \qquad T = K\,H_1
$$

where Δs (or ΔZ) is the change per log cycle of distance on the s – log~10~ r (or Z – log~10~ r) line of the piezometers, and R is the
distance at which the line gives s = 0. With a single piezometer the line passes through the well, and the result is indicative.

### Distance-drawdown { #distanza-abbassamento }

On the same s – log~10~ r line, but with the piezometer drawdowns **at the same time t** of pumping (Cooper-Jacob in distance):
T = ln10·Q/(2π·Δs), r~0~ where s = 0, S = 2.25·T·t/r~0~². At least two piezometers at different distances are needed, and u must be
small even at the farthest piezometer.

## Step-drawdown test { #prova-a-gradini-di-portata }

The well is pumped at increasing discharges Q~1~, Q~2~, … in steps of equal duration; for each step the drawdown at the end of the
step is read (cumulative from the start of the test).

### Head losses and Jacob's equation (1947) { #perdite-di-carico-ed-equazione-di-jacob-1947 }

The drawdown in the well is the sum of a **linear aquifer loss** (laminar flow, BQ) and a **quadratic well loss** (turbulent flow in
the screens, in the gravel pack and near the well, CQ²):

$$
s = B\,Q + C\,Q^2, \qquad \frac{s}{Q} = B + C\,Q
$$

B and C are the intercept and the slope of the **specific drawdown** s/Q versus Q line, by least squares on the valid steps. s/Q (or
its inverse Q/s, the **specific capacity**) tells how much the well «yields».

The **efficiency** of the well is the share of drawdown due to the aquifer:

$$
E = \frac{B\,Q}{B\,Q + C\,Q^2}
$$

and it decreases as the discharge increases. The program calculates it at the reference discharge given in the project, otherwise at
the optimal discharge.

### Critical discharge and optimal discharge { #portata-critica-e-portata-ottimale }

The **critical discharge** Q~c~ is the discharge beyond which the well losses grow disproportionately with respect to the benefit: you
choose it on the characteristic curve s(Q). If you do not choose it, the program proposes Q = B/C, the discharge at which the well
losses equal the aquifer losses (E = 50 %). The **optimal discharge** is Q~ott~ = 0.9·Q~c~, and the **critical drawdown** s~c~ is that
of the curve at Q~c~.

### Well condition (Walton 1962) { #condizioni-del-pozzo-walton-1962 }

Classes based on the coefficient C expressed in min²/m⁵:

| C (min²/m⁵) | Well condition |
|---|---|
| ≤ 0.5 | properly designed and developed |
| 0.5–1 | mild deterioration due to clogging |
| 1–4 | severe deterioration or clogging |
| > 4 | difficult to restore the well to its original condition |

### Rorabaugh (1953) { #rorabaugh-1953 }

Generalises Jacob with a free exponent:

$$
s = B\,Q + C\,Q^n
$$

estimated by least squares on the drawdowns (with n = 2 Jacob is recovered). At least three steps are needed; with three the curve
passes through the points. Values of n outside 1.5–3.5 do not have Rorabaugh's physical meaning and the program flags this.

### Distance methods on the steps { #metodi-in-distanza-sui-gradini }

With piezometers, the end-of-step drawdowns also give:

- **Thiem distance line** for each step: s versus log~10~ r on the piezometers, T = ln10·Q/(2π·Δs), K = T/b (or T/H~1~ in an
  unconfined aquifer), R where s = 0;
- **Dupuit-Thiem per step**: the pair of readings well–P1 or P1–P2 as in steady state;
- **Cooper-Jacob on the test stations**: s/Q versus log~10~ t on the steps, T = 2.30/(4π·Δ(s/Q)), S = 2.25·T·t~0~/r².

The end-of-step drawdowns are not at steady state: these results are **indicative**, and the last one never enters the proposal.

## Radius of influence { #raggio-dazione }

The radius of influence R is the distance at which the drawdown becomes zero. GeoTheis NX derives it, in order of preference:

1. from the **Thiem line** on the stabilised drawdowns of the piezometers (s = 0);
2. from the Cooper-Jacob **transient radius** at the end of pumping, if S is known:

$$
R(t) = 1.5\sqrt{\frac{T\,t}{S}} = \sqrt{\frac{2.25\,T\,t}{S}}
$$

3. from the Thiem distance line on the steps (indicative).

R(t) grows with the pumping duration: it is not a property of the aquifer but of the state of the test. In the **single wells** R is
not calculated: it is an **assumed** value that you enter.

## Single wells { #pozzi-singoli }

When there is only the well, the **single wells** methods use the critical pair (Q~c~, s~c~) as if it were a steady state, with an
assumed radius of influence R. The pair comes from the step-drawdown test or, without steps, from the **known critical discharge**
entered in the [Test](prove.md) tab. The results are **indicative estimates**: they do not replace a test with piezometers. Leaky
aquifers are not handled.

### Fully penetrating well (Celico) { #pozzo-completo-celico }

$$
\text{confined aquifer (Thiem): } T = \frac{Q\,\ln(R/r_w)}{2\pi\,s}, \quad K = \frac{T}{b}
\qquad
\text{unconfined aquifer (Dupuit): } K = \frac{Q\,\ln(R/r_w)}{\pi\,(H_1^2 - H_2^2)}, \quad T = K\,H_1
$$

with H~2~ = H~1~ − s.

### Partially penetrating well { #pozzo-incompleto-pozzo-parzialmente-penetrante }

If the screen crosses only part of the aquifer, the flow lines also converge vertically towards the screen and the drawdown in the
well is larger than that of a fully penetrating well. The formulas correct for the geometry; L is the screen length.

**Unconfined aquifer** (Chiesa), with a the distance between the bottom of the screen and the base:

$$
K = \frac{Q\,\ln(R/r_w)}{\pi\left[(H_1 - a)^2 - (H_2 - a)^2\right]}\cdot\frac{1}{1 + (0.3 + 10\,r_w/H_1)\,\sin(1.8\,a/H_1)}, \qquad T = K\,H_1
$$

**Confined aquifer** (Chiesa), according to the screen position (D distance from the top to the start of the screen):

- type A, screen detached from the top and not reaching the base: T = Q/(2π·s)·[ln(R/(2b)) + (b/L)·ln(2L/r~w~)];
- type B, screen attached to the top, shorter than the thickness, and type C, screen detached from the top and reaching the base:
  T = Q/(2π·s)·[ln(R/r~w~) + ξ/2], with ξ from Chiesa's table as a function of b/r~w~ and L/b;
- K = T/b.

In a confined aquifer the program also calculates the specific formulas (K from which T = K·b, or T from which K = T/b):

| Method | Formula |
|---|---|
| Kozeny (1933) | K = Q/(2π·s·L)·ln(R/r~w~) / [1 + 7·√(r~w~/(2L))·cos(π·L/(2b))] |
| Infinite thickness (Babushkin) | K = Q/(2π·s·L)·ln(2L/r~w~) |
| Halek | K = Q/(2π·s·L)·[ln(4(L/r~w~)/(L/R + √(1 + L²/R²))) + 1 − (R/L)(1 − √(1 + L²/R²))] |
| Zangar | K = Q/(2π·s·L)·ln(L/r~w~) |
| Muskat | T = Q/(2π·s)·[(b/2L)·(2·ln(4b/r~w~) − ln Γ) − ln(4b/R)] |
| Girinski | K = Q/(2π·s·L)·ln(1.6·L/r~w~), only with L/r~w~ ≤ 5 |
| «L/b − L/2r» | T = Q/(2π·s)·ln((2/L)·(L/2r~w~) + 0.2/b) |

!!! warning "Warning"
    Five formulas are marked **to be checked** against the reference text and remain as in the desktop program: Halek (reconstructed,
    not compared with the text), Muskat (value of ln Γ), Girinski (the L/r~w~ ≤ 5 limit excludes it for any real screen),
    «L/b − L/2r» (the argument of the logarithm is not dimensionless, so T depends on the unit of measurement) and the ξ/2 term
    of types B and C. Use them only for comparison.

## Cone of depression { #cono-di-depressione }

The cone drawn in the well section uses the design values in use:

- with T, S and the pumping duration, the **Theis** curve (**Hantush** if the value comes from Hantush) at the end of pumping, from
  r~w~ to R(t);
- otherwise **Thiem** (confined aquifer) or **Dupuit** (unconfined aquifer) up to the design radius of influence R.

## Validity of the results { #validita-dei-risultati }

- Theis and Cooper-Jacob assume a confined aquifer. In an unconfined aquifer they hold as long as the drawdown is small compared with
  the saturated thickness: the program does not apply Jacob's correction s′ = s − s²/(2H) nor Neuman's model for delayed yield.
- Hantush does not account for the storage of the semi-pervious layer.
- Not modelled: wellbore storage and skin, recharge or impermeable boundaries, anisotropy, variable discharges other than steps,
  interference of multiple wells.

The summary of the limits is in [Results → Limits](risultati.md#limiti); the checks on the calculation code are in
[Validation](validazione.md).

## References { #bibliografia }

- Theis C.V. (1935). *The relation between the lowering of the piezometric surface and the rate and duration of discharge of a well
  using ground-water storage*. Transactions of the American Geophysical Union, 16(2), 519–524.
- Cooper H.H., Jacob C.E. (1946). *A generalized graphical method for evaluating formation constants and summarizing well-field
  history*. Transactions of the American Geophysical Union, 27(4), 526–534.
- Jacob C.E. (1947). *Drawdown test to determine effective radius of artesian well*. Transactions ASCE, 112, 1047–1070.
- Hantush M.S., Jacob C.E. (1955). *Non-steady radial flow in an infinite leaky aquifer*. Transactions of the American Geophysical
  Union, 36(1), 95–100.
- Hantush M.S. (1956). *Analysis of data from pumping tests in leaky aquifers*. Transactions of the American Geophysical Union, 37(6),
  702–714.
- Hantush M.S. (1964). *Hydraulics of wells*. In: Advances in Hydroscience, vol. 1, Academic Press.
- Rorabaugh M.I. (1953). *Graphical and theoretical analysis of step-drawdown test of artesian well*. Proceedings ASCE, 79, separate 362.
- Walton W.C. (1962). *Selected analytical methods for well and aquifer evaluation*. Illinois State Water Survey, Bulletin 49.
- Thiem G. (1906). *Hydrologische Methoden*. Leipzig, J.M. Gebhardt.
- Dupuit J. (1863). *Études théoriques et pratiques sur le mouvement des eaux dans les canaux découverts et à travers les terrains
  perméables*. 2nd ed., Paris, Dunod.
- Kozeny J. (1933). *Theorie und Berechnung der Brunnen*. Wasserkraft und Wasserwirtschaft, 28.
- Kruseman G.P., de Ridder N.A. (1994). *Analysis and Evaluation of Pumping Test Data*. 2nd ed., ILRI Publication 47, Wageningen.
- Chiesa G. *Idraulica delle acque di falda*. Palermo, Flaccovio.
- Celico P. *Prospezioni idrogeologiche*. Napoli, Liguori.
- Abramowitz M., Stegun I.A. (1964). *Handbook of Mathematical Functions*. National Bureau of Standards, Applied Mathematics Series 55.
- Marquardt D.W. (1963). *An algorithm for least-squares estimation of nonlinear parameters*. Journal of the SIAM, 11(2), 431–441.
- Moré J.J. (1978). *The Levenberg-Marquardt algorithm: implementation and theory*. Lecture Notes in Mathematics 630, Springer.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20GeoTheis%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/geotheis/docs/en/teoria.md).*
