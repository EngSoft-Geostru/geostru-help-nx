# Validation and differences from the desktop version

Point **10.2 of the Italian NTC 2018** asks the **designer** to assess the reliability of the
calculation code they use. It is your judgement; our task is to give you the material to form
it: scope and limits, theoretical basis, solved and repeatable test cases.

This page is its summary, valid for the **calculation engine from version 1.1.0** (the
version is printed in the "Calculation code" block of every report). It is a **validation**,
carried out by the developer of the program and verifiable by anyone: no third-party body is
involved.

If you come from Easy-MASW desktop and want to know why a number has changed, go to
[Differences from the desktop program](#differences-from-the-desktop-program).

## Scope and limits

MASW NX processes **active MASW** surveys: a source in line with a geophone line at constant
spacing. From the traces it computes the f-v spectrum, derives the Rayleigh-wave dispersion
curve (picking, up to 5 modes) and inverts a V~s~ profile in plane-parallel layers; from the
profile it derives V~s,eq~, H, subsoil category (NTC 2018, NTC 2008) and estimated
geotechnical parameters.

**Limits**

- The model is **1D with horizontal, homogeneous layers**: lateral variations, topography and
  dipping layers are not represented.
- The inversion is **stochastic and non-unique**: different profiles reproduce the same curve.
  The misfit measures agreement with the picking, not the truth of the profile. Two runs give
  slightly different solutions.
- The **investigation depth** is of the order of λ/2 of the longest wavelength read reliably:
  below it, the profile is extrapolated. In particular the half-space and a V~s,eq~ over 30 m
  require energy at low frequencies.
- The **picking** is an operator's choice, and the result depends on it: higher modes taken
  for the fundamental overestimate V~s~. Automatic picking is a proposal: above 20 Hz the
  fundamental mode of the desktop example does not form a ridge in the map and must be
  completed by hand.
- ρ is the value assigned to the layers (in the desktop the "unit weight" is used as a
  density in kg/m³); ν is assumed. The curve is weakly sensitive to both.
- **G~0~, E~d~, M~0~, E are small-strain dynamic moduli.** NSPT (Ohta & Goto) and Qc
  (Jamiolkowski) are empirical correlations inverted from V~s~, indicative only.
- Not handled: the f-k view and ReMi/f-p of the desktop, passive sources, Love waves, joint
  inversion with HVSR, the Eurocode 8 category.

## Theoretical basis

The formulas, with references, are on the [Theory](teoria.md) page: f-v spectrum
(phase-shift, Park, Miller and Xia), forward problem (Thomson-Haskell-Dunkin, engine derived
from Geopsy and verified to machine precision), inversion (Nelder and Mead), V~s,eq~ (NTC 2018
§3.2.2), elastic parameters, Ohta and Goto, Jamiolkowski, SH transfer function with 1 %
damping.

## Test cases

Two groups: cases with a **closed-form** reference, which anyone can redo by hand or with a
spreadsheet, and the comparison with **Easy-MASW desktop** on ten projects. They are repeated
automatically at every version of the program.

### Closed forms

| Case | Data | Expected | MASW NX |
|---|---|---|---|
| Spectrum of a synthetic wave | 24 geophones at 1 m, f = 20 Hz, v = 200 m/s | ridge at 200 ± 10 m/s, column maximum 1 | ok |
| V~s,eq~ without bedrock | 10 m at 200 + 20 m at 400 m/s | 30 / (0.05 + 0.05) = 300 m/s, H = 30 m | 300 |
| Bedrock at 20 m | 10 m at 200, 10 m at 400, then V~s~ 900 m/s | 20 / 0.075 = 266.67 m/s, category E | 266.67, E |
| Bedrock within 3 m | 2 m at 200, then V~s~ 900 m/s | V~s,eq~ = 900 m/s, category A | 900, A |
| Foundation cutting a layer | 10 m at 200, then 400 m/s; foundation at 4 m | 30 / (0.03 + 0.06) = 333.33 m/s | 333.33 |
| Transfer, homogeneous layer | H = 10 m, V~s~ = 300 m/s, f = 3.75 Hz | 1 / \|cos(π/4)\| = 1.414 | 1.41 |
| Transfer on bedrock | H = 20 m, V~s~ = 200 m/s | first resonance V~s~/4H = 2.5 Hz | 2.5 Hz |
| Inversion of a known profile | 150 / 300 / 600 m/s, synthetic curve | misfit < 0.01, V~s1~ within 5 % | ok |
| Low-pass filter | cut-off 60 Hz, stop at 70 Hz, 20 dB, sampling 2,000 Hz | passes at 10 Hz, ≤ 0.11 at 70 Hz | ok |

### Comparison with Easy-MASW desktop

The reference values were generated on 29/10/2026 with the desktop calculation libraries on
its ten example projects. Comparing two implementations of ours **does not prove the
correctness of the method**, which rests on the closed forms: it proves that porting did not
change the calculation.

| Example | Traces | Samples | dt [s] | dx [m] | Map v×f | Picking | Desktop misfit | V~s,eq~ [m/s] | H [m] | Desktop cat. |
|---|---|---|---|---|---|---|---|---|---|---|
| DefaultExample | 24/24 | 5120 | 0.0005 | 1 | 799×180 | 30 | 0.07952 | 290.99 | 30 | C |
| NTC2018 3amasw | 24/24 | 2048 | 0.001 | 1 | 1999×123 | 27 | 0.17238 | 288.27 | 14.78 | E |
| geostru001 | 24/24 | 7651 | 0.000131 | 1 | 1550×74 | 38 | 0.12270 | 330.36 | 30 | C |
| geostru002 | 24/24 | 7651 | 0.000131 | 1 | 1599×74 | 39 | 0.16853 | 299.51 | 30 | E (see below) |
| geostru003 | 24/24 | 7651 | 0.000131 | 1 | 1550×74 | 40 | 0.12260 | 327.48 | 30 | C |
| geostru004 | 24/24 | 1000 | 0.001 | 2 | 1750×60 | 32 | – | – | – | – |
| geostru005 | 12/12 | 8000 | 0.00025 | 2.5 | 1799×202 | 20 | 0.07401 | 392.42 | 8.25 | B |
| geostru006 | 12/12 | 8000 | 0.00025 | 2.5 | 5999×120 | 15 | – | – | – | – |
| geostru007 | 11/12 | 2500 | 0.0002 | 5 | 4900×55 | 17 | 0.02713 | 1229.20 | 0 | A |
| geostru008 | 12/12 | 8000 | 0.00025 | 2.5 | 1199×120 | 15 | 0.00825 | 340.51 | 30 | C |

The dash marks projects saved without an inversion.

Outcome of the comparisons, on every example that has the data:

| Quantity | Tolerance | Outcome |
|---|---|---|
| f-v map against the saved one | 1·10⁻⁹ | within tolerance on 10 examples |
| Curve of maxima | exact on v, 1·10⁻¹² on f | identical to the one recomputed by the desktop |
| Regression coefficients | 1·10⁻⁶ relative | match |
| Misfit of the desktop model | 1·10⁻¹² | matches |
| Error % of the desktop model | 1·10⁻⁹ | matches |
| Theoretical curves of the desktop model | 1·10⁻⁹ relative | match |
| Run with fixed seed | misfit 1·10⁻¹², V~s~ 1·10⁻⁹ | identical |
| V~s,eq~, H, category (reproducing the desktop) | 1·10⁻⁹ / 1·10⁻⁵ / exact | match |

**Comments on the differences**

- In 4 examples the v curve saved in the file differs by 1 m/s from the one recomputed by the
  same desktop: it comes from an earlier version of the program. The comparison is made with
  the recomputed one.
- The category "left" in the desktop file is not a reference: it may be NTC 2008 or from an
  earlier model. The recomputed one is used.
- In geostru007 the desktop computes V~s,eq~ on the model saved in the layers (1,229.2 m/s),
  which is not the best solution (V~s1~ = 1,230.7 m/s): MASW NX uses the solution selected on
  screen.

## Differences from the desktop program

The principle is **parity first**: MASW NX reproduces the desktop calculation, and corrects
only the defects declared here. The kernel can still reproduce the desktop to the letter; the
tests use it to prove that the differences are the corrections and nothing else.

### Corrections

| Desktop defect | Effect | MASW NX |
|---|---|---|
| Depths summed in single precision when computing H | geostru002: H = 29.999998 m, category **E** instead of **C** | sums in double precision, 10⁻⁶ tolerance on the 30 m: **C** |
| SEG-Y samples in IBM format read as IEEE | wrong amplitudes | correct conversion |
| Trace deselected in the middle of the line | the following ones move one dx closer: distorted spectrum | the phase uses the real geophone position; identical on the examples |
| Depths of the six default layers inconsistent with their thicknesses | initial V~s~ estimated on wrong depths | cumulative depths |

### Reproduced for fidelity

To be reviewed, but left as in the desktop so that results remain comparable:

- the **frequency label** of the map columns is shifted by up to one frequency step df (less
  than 0.5 Hz on the examples, below the reading resolution);
- in the maxima filter k~min~ = k~max~ / n~f~;
- a V~s,eq~ of exactly 100, 360 or 800 m/s falls in no range: the app declares it instead of
  choosing.

## Engine versions

| Version | Date | What changes in the results |
|---|---|---|
| 1.0.0 | 30/10/2026 | First released version. |
| 1.1.0 | 31/10/2026 | Automatic picking on the **ridges** of the f-v map, on several modes too; initial model **proposed from the picking** instead of the six fixed layers 4-5-6-7-8 m (the same rule is in the desktop); initial V~s~ estimated with λ/2 on v~min~, v and v~max~ and default Poisson 0.2, aligned with the corrected desktop (before, only v~min~ was halved and the start was 0.3). |

The spectrum calculation and the inversion do not change: with the same picking and initial
layers the results of 1.0.0 are reproduced. On the desktop example (DefaultExample, 1,000
iterations), with the picking and layers of the file, MASW NX gives **misfit 0.0796** and
**error 0.204 %**, against 0.080 and 0.206 % of the desktop.

What changes is the starting point when the user does not enter the layers: with automatic
picking and the fixed desktop layers the error was **2.28 %**, with the proposed layers
**0.13–0.22 %** on three different seeds. Limit: above 20 Hz the fundamental mode of the
example does not form a ridge in the map, so automatic picking does not reach it and it must
be completed by hand.

## Reproducibility

The test cases are automated tests of the source code, repeated at every version; the
projects and expected results are archived with the code. The full validation document is
available on request from [info@geostru.ai](mailto:info@geostru.ai).

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20MASW%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/masw/docs/en/validazione.md).*
