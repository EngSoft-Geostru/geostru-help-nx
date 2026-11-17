# Validation and differences from the desktop version

The GeoTheis NX calculation engine is accompanied by a validation document, as required by Section 10.2 of NTC 2018: fields of
application, theoretical basis, solved test cases, and deviations from the desktop program. This is validation, not certification: no
third-party body is involved.

This page summarizes the document for version **1.0.0** of the calculation engine (16 November 2026). The engine version is printed
in the “Calculation code” block of every Word report, so you know which code was used to produce each document.

## Validation references { #riferimenti-della-validazione }

GeoTheis NX is based on the GeoTheis desktop program, but the strongest reference for validation is the **literature**: closed-form
solutions, published tables, and mathematical identities that do not depend on the code. The desktop version is used to demonstrate
that the differences between the two programs are the corrections listed below, and nothing else.

The engine has two modes:

- **corrected** mode, the only one you use in the app, with formulas from the literature; it matches the desktop version corrected on
  15 November 2026;
- a mode that **reproduces the desktop version** as it was before the corrections, which exists only in automated tests for comparison.

As of 16 November 2026, there are 840 automated tests on the calculation engine, 304 on the app with the engine connected, and 23 on
the engine version guard: all passed.

## What was checked { #che-cosa-e-stato-controllato }

| Check | Reference | Result |
|---|---|---|
| Theis well function W(u) | exponential integral E~1~ and published table (Wenzel; Kruseman & de Ridder) | 10⁻¹³ relative on E~1~; within the 3 digits of the table |
| Hantush function W(u, r/B) | steady-state limit 2·K~0~(r/B), Hantush symmetry identity, Hantush table (1956) over approximately 2,080 cells | identities to 10⁻¹¹; table within 0.6·10⁻⁴ absolute or 2·10⁻⁴ relative, except for typographical errors in the desktop table |
| Parity with the previous desktop version | 12 desktop examples + 8 single-well variants, in the mode that reproduces the desktop version | all within 10⁻⁵ relative |
| Corrected mode against the corrected desktop version | the same 20 cases | 10⁻⁵ relative (5·10⁻⁵ for step-test C, which the desktop version calculates in single precision) |
| Corrected mode against formulas from the literature | the same data, formulas in double precision | within 10⁻⁹ |
| Theis and Hantush fitting | synthetic data with known values | T and S recovered to 10⁻⁶ relative, r/B to 10⁻⁵; with 2% noise, the 95% interval contains the true value |
| Rorabaugh | synthetic data s = BQ + CQⁿ with n = 1.5; 2; 2.8 | B, C, and n recovered |
| Coordinates | PROJ (pyproj) on Italian cities and on a real Gauss-Boaga case | within 2 cm; round trip below 1 cm |

## Test case: CELICO { #caso-di-prova-celico }

The **CELICO** example (fully penetrating well in a confined aquifer, three steps, two piezometers, constant-rate test with recovery)
is the reference case. Values from corrected mode, identical to the corrected desktop version:

| Quantity | GeoTheis NX | Desktop before corrections |
|---|---|---|
| B, C of the steps | 2.3894·10⁻³ h/m², 3.2486·10⁻⁶ h²/m⁵ | same |
| Efficiency at optimum discharge (989.6 m³/h) | 42.64% | 0% |
| Cooper-Jacob T P1 / P2 | 4.231·10⁻³ / 1.058·10⁻² m²/s | 1.98·10⁻⁴ / 4.96·10⁻⁴ m²/s |
| Cooper-Jacob S P1 / P2 | 7.32·10⁻³ / 5.61·10⁻³ | 2.22·10⁻⁴ / 1.70·10⁻⁴ |
| Recovery T P1 / P2 | 4.69·10⁻³ / 1.17·10⁻² m²/s | calculated using the wrong times |
| Dupuit-Thiem T, R | 3.91·10⁻³ m²/s, R = 76.5 m | R = 1.21 m |
| T, K, R from the steps (distance-drawdown line) | 5.41·10⁻² m²/s, 7.72·10⁻³ m/s, 443 m | 5.79·10⁻² m²/s, 8.27·10⁻³ m/s, 558 m |
| Single-well T (R = 150 m) | 4.23·10⁻² m²/s | same within 0.07% |

**Theis fitting versus the point selected manually in the desktop version.** The desktop version did not have fitting: Theis T and S
came from the point dragged with the mouse on an incorrect type curve. For CELICO, GeoTheis NX fitting gives T = 4.34·10⁻³ m²/s and
S = 7.03·10⁻³ at P1, with a typical deviation from the data of 7%, and agrees with Cooper-Jacob within 3% for T and 4% for S. The
point saved in the desktop file gives T = 2.50·10⁻³ m²/s and S = 1.97·10⁻², with a typical deviation of 190%. This is why the
imported point is marked as *unreliable*.

**Single wells with known critical discharge.** For the eight examples using only the well geometry, with Q~c~ = 100 m³/h,
s~c~ = 5 m, and R = 150 m, the program calculates the same 29 methods as the corrected desktop version, within 1.1·10⁻⁷ relative.
Fully penetrating well in a confined aquifer: T = 5.043·10⁻³ m²/s, K = 8.405·10⁻⁴ m/s.

!!! note "Note"
    The desktop examples **are not real tests**: in CELICO, the P2 readings are the P1 readings × 0.4, and two examples reuse the
    same readings with the piezometers moved. They demonstrate that the calculation is correct, not that a method describes a real
    aquifer. This is why the step-drawdown test methods (T ≈ 5·10⁻² m²/s) and the constant-rate methods (4–11·10⁻³ m²/s) do not
    agree for CELICO, and the program flags this.

## Differences from the desktop program { #differenze-dal-programma-desktop }

GeoTheis NX uses formulas from the literature where the desktop version, before the correction of 15 November 2026, departed from
them. With the same data, the numbers may therefore differ from those you saw in the desktop version.

| Desktop before corrections | GeoTheis NX |
|---|---|
| Theis W(u) calculated with −0.7552 instead of Euler's constant (0.5772): shifted type curve | exact W(u) |
| Cooper-Jacob T = 0.183·(Q/3600)/C: 24 times smaller for CELICO | T = ln10·Q/(4π·Δs) |
| Cooper-Jacob straight line fitted to all points, even at u ≈ 0.5 | only the segment with u < 0.05, selected automatically |
| Recovery regressed against drawdown times | s′ against log(t/t′), with the declared shutdown time |
| Hantush S = 4·T·t/(u·r) | S = 4·T·u·(t/r²) |
| Dupuit-Thiem R derived from the well, with π instead of 2π | R from the piezometer line, where s = 0 |
| Radius of influence from the steps: well–clicked R line | Thiem line through the piezometers, one R per step |
| Step efficiency saved as 0% | efficiency at optimum discharge |
| Muskat with a misplaced parenthesis; Chiesa ξ table interpolated backwards, with two typographical errors | corrected formulas and table |
| Averages divided by the number of rows, including empty ones | averages of the available values only |
| Theis and Hantush only with the point selected with the mouse | automatic fitting with 95% intervals, plus manual adjustment |
| Unconfined aquifer and partially penetrating well rejected by transient methods | calculated with a warning |
| Hantush table with typographical errors | numerical integral |
| Only Jacob (n = 2) for the step-drawdown test | additionally Rorabaugh (free n), indicative |

Four formulas for partially penetrating wells (Muskat, Girinski, “L/b − L/2r”, and the ξ/2 term for types B and C) remain **as in
the desktop version**, marked *to be verified*: see [Theoretical background](teoria.md#pozzo-incompleto-pozzo-parzialmente-penetrante).

## Scope of application and limitations { #campo-dimpiego-e-limiti }

- Step-drawdown tests and constant-rate tests with recovery, on the pumping well and on piezometers, in unconfined, confined, and
  leaky aquifers, with fully or partially penetrating wells.
- Theis and Cooper-Jacob assume a confined aquifer; in unconfined aquifers, they apply to drawdowns that are small compared with the
  saturated thickness (no Jacob correction, no Neuman model).
- Hantush without storage in the semipermeable layer.
- S from the pumping well is not reliable; piezometers are required for S.
- Single wells and distance-based methods for step tests are indicative.
- Not modeled: wellbore storage and skin, drawdown derivative, delayed drainage, recharge or impermeable boundaries, anisotropy,
  variable discharges other than steps, and interference between multiple wells.
- Coordinates: 7-parameter datum transformations (Roma40) have errors on the order of one meter, up to several meters; ED50 up to
  around ten meters. The report states the transformation used.
- Inventory wells come from the ISPRA archive (Law 464/84), which is incomplete; ground elevation from a digital model is not used
  in the calculation.

A side-by-side on-screen comparison between the desktop version and NX on a real case is planned and will be added to the document
when readings from a real test become available.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20GeoTheis%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/geotheis/docs/en/validazione.md)*
