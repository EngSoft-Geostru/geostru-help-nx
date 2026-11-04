# Validation and limits

The full validation document (NTC 2018 §10.2) comes with the code: field of use, theoretical basis, solved test cases and differences from the
desktop program. It is a validation: no third-party body is involved.

## Field of use and limits

- Areas and works to which Ordinance 55/2018 applies; zones for which the MS3 study provides a spectrum.
- Comparison always with the horizontal spectrum, η = 1, T~R~ = 475 years.
- The topographic category uses the crest S~T~, without the reduction with the elevation of the site.
- T~min~ and T~max~ are an input of the designer.

## Test cases

- **Hand-worked cases** at the edges of the thresholds: ratio exactly 1.30 (does not exceed) and 1.31 (exceeds); areas +20 % (does not exceed) and
  +21 % (exceeds); 2·T~max~ = 1.10 s (comparison made) and 1.12 s (not applicable).
- **Parity with the desktop** on 42 cases produced with the desktop program: same counts, same outcomes, regularisation within 1e-5, in the mode
  that reproduces the desktop (used only in the tests).
- **San Severino example** (microzone 13, cat. C, T1, T~min~ 0.1 s, T~max~ 0.5 s): maximum ratio 1.498, areas −17.2 %, outcome further
  investigations.

## Differences from the desktop program

The app follows the text of the Ordinance where the desktop (before the correction of 03/11/2026) departed from it:

| Desktop | NX |
|---|---|
| condition 1 as share of points above the code spectrum, 30 % threshold | pointwise exceedance: maximum ratio > 1.30 |
| three outcomes, with automatic «RSL»; screen and report could differ | two outcomes from the text, the same everywhere |
| area with an extra triangle from the origin, and −1 with T~min~ and 2·T~max~ in the same branch | exact integrals |
| 2·T~max~ > 1.1 s not handled | comparison not applicable |
| limit state, η and vertical spectrum free | T~R~ 475, η = 1, horizontal |
| a~max~ from the Sa of the second point | from Se(0.01 s) |
| SV read from the file | SV derived from SA |

For this reason, on the same spectrum, the NX outcome can differ from the desktop one: in the San Severino example the desktop wrote
«simplified approach», NX «further investigations required».

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20RSL%20III%20A%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/rsl3a/docs/en/validazione.md).*
