# Validation and limits

The full validation document (NTC 2018 §10.2) accompanies the code: field of application, theoretical basis, solved test cases and
differences from the desktop program. It is called validation, not certification: no third party is involved. §10.2 asks the **designer**
to assess the reliability of the code they use; this page and that document are the material to do so. The current revision applies to
**calculation engine 1.0.0**, the version every report prints in the "Calculation code" block.

## Field of application

- RC cantilever walls (with shear key, back shelf and front shelf), gravity walls, walls on one, two or three rows of piles or on free rows,
  anchored walls, basement wall (restrained at the top).
- NTC 2018, NTC 2008 and the Eurocodes, with the combinations generated from the code or given by the designer.
- Pseudo-static NTC 2018 seismic action with Mononobe-Okabe and β~m~ for walls from the site parameters.
- Layered soil (up to ten layers), water table, ground profile in segments, backfills, distributed surcharges and point loads.
- Rectangular RC sections at ULS (bending with axial force, shear without shear reinforcement) and SLS (stresses, cracking), or allowable
  stresses; envelope reinforcement, distribution bars, bar schedule.

## Limits

- The calculation is per metre of wall, in plane strain: no three-dimensional effects, corners or height changes along the wall.
- The distributed surcharge on the backfill is reduced to an **equivalent uniform surcharge**: with distant loads or narrow strips the earth
  pressure is approximate.
- There is **one** water table; downhill the uplift takes the water table at most at ground level.
- With a backfill design slope greater than φ~d~ the earth pressure coefficient is conventional: the program flags it, the choice of model
  is the designer's.
- The vertical seismic action has a single direction (upwards on the masses).
- **Global stability** of the wall-soil system is not computed: it must be checked separately with a slope stability program.
- Permanent seismic displacements and seismic capacity are not in the results.
- Counterfort, gabion and stone masonry walls open but are not computed.
- Shear in the wall sections is checked without shear reinforcement; the reinforcement is always designed (bars assigned by hand are not
  used).
- In the first release the engine notes are in Italian even with the English interface, and the internal force diagrams of the foundation
  join the values of the design sections with straight lines.

## Test cases

| Case | Reference | Result |
|---|---|---|
| Guide 1, 3 m cantilever wall on sand | hand calculation of the whole chain: K~a~ 0.234891, B′ 1.630 m, Q~lim~ 1087.3 kN/m | NX and desktop agree to the fourth digit: F~s~ sliding 3.7946, bearing capacity 8.6067 |
| Closed-form coefficients | Rankine, Müller-Breslau, Mononobe-Okabe active and passive (Kramer 1996) | 6 decimals |
| Parity with MDC desktop | 22 distributed examples and 8 variants (seismic, counterfort, basement wall, piles in 1 and 3 rows): 30 cases, 87 combinations | earth pressures, forces, global checks, stem internal forces 87/87; reinforcement 16/16; ULS check 12/12; gravity walls 5/5; piles 23/23 |
| Corrections in normal use | one hand-checked test for every corrected defect | e.g. Guide 1: overturning 6.6597 → 6.5319 with the passive thrust among the stabilising actions |
| The app uses the engine as it is | Guides 1, 2 and 3 opened from the page and compared with the engine called directly | agreement to 10⁻⁹ |

The parity tolerances are 10⁻⁴ relative on forces and coefficients, 10⁻³ on RC sections, exact integers for the reinforcement. A single
difference is commented (0.03 % on a toe section in Guide 3, due to rounding at the half thousandth).

## Differences from the desktop program

MDC NX gives the same results as the desktop where the desktop is right. Where it is not, it corrects and declares it. The main corrections:

| Desktop | MDC NX |
|---|---|
| no uplift on the base | trapezoidal uplift (water table uphill, at most at ground level downhill) |
| the moment of the passive thrust reduced the overturning moment | the passive thrust is among the stabilising actions |
| γ~R~ for the soil resistance at the toe never applied to the passive thrust | applied (E~p~/γ~R,t~) |
| seismic passive thrust equal to the static one | Mononobe-Okabe passive × (1 − k~v~) |
| weight of the surcharge on the heel with the unfavourable factor; "linear" load with a wrong extent | weight with γ ≤ 1 for permanent loads, zero for variable ones; linear load as a trapezoid |
| base friction and adhesion typed by hand not reduced by γ~φ~ and γ~c~ | reduced; bearing capacity with the layer parameters |
| NTC 2018 seismic combinations created with k~h~ = 0 | k~h~ and k~v~ from the site |
| no vertical inertia force | −k~v~·W on the masses |
| semi-gravity wall: bar strength ten times too high | corrected |
| axial force taken as absolute value in the ULS check (tension became compression) | with its sign |
| front shelf: the last action added several times | sum of the actions |
| piles with increasing modulus: Hetényi characteristic length instead of Matlock-Reese | $T=(EI/n_h)^{1/5}$ |
| tubular micropiles in tension always "not verified" | correct N-M interaction |
| anchors: inclination rounded to whole radians; no check of the load; anchors ignored without the TIR action | exact inclination, check E~d~ ≤ R~d~, γ~TIR~ = 1 |

They stay as in the desktop, because they are modelling choices and not errors: the first-yield resisting moment with NTC 2018 (see
[RC sections, piles and anchors](teoria-strutture.md)), the discretisation of the sections, the backfill design slope, the pile bearing
capacity correlations.

For this reason, on the same project, the safety factors of MDC NX may differ from those of the desktop, almost always on the safe side.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20MDC%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mdc/docs/en/validazione.md).*
