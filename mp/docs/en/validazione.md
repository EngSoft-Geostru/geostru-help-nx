# Code validation

Clause **10.2 of the Italian NTC 2018** asks the **designer** to assess the reliability of
the calculation code they use. It is not a duty of the software producer: it is your
judgement. Our task is to give you the material to form it.

For MP NX that material is the **validation document**: fields of application and limits,
theoretical bases with references, fully solved and reproducible test cases. This page
summarises it. It is a **validation**, carried out by those who develop the program and
verifiable by anyone: no third-party body is involved.

## Fields of application and limits

MP NX computes a **single reinforced-concrete pile**, bored or driven, and a **single
micropile**. The functions are listed on the [home page](index.md).

It does not cover: pile groups and group efficiency; screw piles; jet grouting; steel or
timber piles; micropile networks, raked micropiles and critical buckling load; check of the
composite tubular section; non-circular sections in the structural check; pressuremeter
tests and dynamic formulae; Fleming's settlement; the full NTC seismic hazard and kinematic
moments.

The Winkler model captures neither the interaction between springs nor soil yielding beyond
the removal of springs: piles with large displacements need p-y or continuum analyses.

## Theoretical bases

Berezantsev et al. (1961), Terzaghi (1943), Janbu (1976), Hansen (1970) and Vesic (1977) for
N~q~ and N~c~; Broms (1964) in Viggiani's formulation (1999) for the lateral load; Poulos
and Davis (1980) for the settlement; Bowles (1996) and Chiarugi-Maia (1970) for the modulus
of subgrade reaction; NTC 2018 with Circular 7/2019, EN 1997-1 and EN 1992-1-1 for the
factors and the section check.

## Test cases

The document holds **18 cases**, all repeated as automated tests at every release.

| Cases | Subject | Reference | Difference |
|---|---|---|---|
| 1 | N~q~ and N~c~ at φ = 30° for all methods | literature formulae | < 1 % (< 2 % Berezantsev with D = 1 m) |
| 2–4 | pile in sand, in undrained clay, in rock | hand calculation | within ± 1 % |
| 5 | Broms, six cases (cohesive and cohesionless, free and fixed head) | closed forms | ± 1 % |
| 6 | Poulos and Davis | table of the method | 6.1 mm expected, 6.0–6.25 computed |
| 7 | NTC chain: ξ, γ~b~, γ~s~, tension, global factor | NTC 2018 tab. 6.4.II and 6.4.IV | exact |
| 8–10 | the three design examples | they load and calculate | — |
| 11–12 | FEM of Bowles example 16.10; Bowles K~s~ by hand | desktop and hand calculation | 0.0 % on the solver; 0.4 % through the archive |
| 13 | ultimate moment Ø 80 cm, 12 Ø 20 | non-dimensional design charts | 455 kNm expected and computed |
| 14–18 | five files of the MP desktop | desktop program | see below |

Wherever it exists, the reference is the **closed form from the literature** recomputed by
hand: anyone can verify it and it does not depend on us. The comparison with the desktop is
added to it, it does not replace it.

## Differences, explained

Differences are not hidden: each has a declared cause.

- **Pile weight, + 2 % (case 14).** The desktop, in its kg system, uses 2 500 kg/m³ for
  C20/25 (24.52 kN/m³); the SI archive has 25 kN/m³. Base and shaft match; once the weight
  difference is removed, Q and R~d~ are back within 0.1 %. The difference is conservative.
- **Elastic modulus, 0.4 % (case 11).** Same origin: the two desktop archives have different
  E for the same class. With the same modulus the solver matches to the fourth digit.
- **Shear resistances, − 2 % (case 16).** V~Rcd~ and V~Rsd~ are lower than the desktop at
  all nodes. It corresponds to an effective depth smaller by one stirrup diameter: the
  desktop uses a compiled version of the solver, MP NX the sources. The difference is
  conservative.
- **Cases 15, 17 and 18: 0.0 %** on ultimate load and design resistances; in case 15 also
  on the settlement, in case 18 also on Broms.

To reproduce a desktop file in the technical system, put the values of the technical archive
in the project archive (for C20/25: E~c~ = 29 380.7 MPa, γ = 24.52 kN/m³). The difference
that remains is then due to the calculation, not to the archives.

## Declared choices

Some behaviours of the desktop program have been **kept** and are listed in the document:
the taper factor F~w~ for φ ≥ 30°, the Vesic and Sano seismic correction starting from the
unreduced φ, the adhesion not removed when the founding plane falls within the first layer,
R~d~ with the pile weight of the first vertical. A desktop error in the description of
Broms' mechanism has instead been fixed; H~max~ does not change.

## Where to find it

The five validation cases can be downloaded from the app: see
[Example projects](esempi.md). The page on the validation of GeoStru codes opens from the
**?** button, **Resources** tab, item **Validation of the calculation code**.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20MP%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mp/docs/en/validazione.md).*
