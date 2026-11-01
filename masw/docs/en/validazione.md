# Validation and limits

Point 10.2 of the Italian NTC 2018 asks the designer to assess the reliability of the code. This page summarises the material; it
is a **validation**, not a certification.

## Field of use

**Active** MASW surveys: source in line with a geophone spread at constant spacing. 1D model with horizontal layers, up to 5 modes.

## Limits to assess

- The model is **1D**: lateral changes, topography and dipping layers are not represented.
- The inversion is **stochastic and non-unique**: different profiles reproduce the same curve.
- **Investigation depth** is of the order of λ/2 of the longest wavelength reliably read. Below that the profile is extrapolated:
  the half-space and a 30 m V~s,eq~ need low-frequency energy.
- **Picking** is the operator's choice, and the result depends on it.
- ρ and ν are assumed; the curve is weakly sensitive to both.
- G, E~d~, K, E are **dynamic moduli**; NSPT and Q~c~ are indicative empirical correlations.
- Not covered: the desktop's ReMi and f-k view, passive sources, Love waves.

## Test cases

**Closed forms.** Among others: synthetic wave at 200 m/s, V~s,eq~ of 300 m/s with 10 m at 200 and 20 m at 400 m/s, bedrock at 20 m
(266.67 m/s, category E), resonance at V~s~/4H.

**Comparison with Easy-MASW desktop on ten projects.** The f-v map matches within 10⁻⁹, misfit and error % of the desktop model within
10⁻¹², theoretical curves within 10⁻⁹ relative, and a fixed-seed run is identical. This shows the port did not change the calculation,
not that the method is correct: for that, the closed forms and the literature apply.

## Differences from the desktop

| Desktop | MASW NX |
|---|---|
| Depths summed in single precision: in one example H = 29.999998 m and category E | double-precision sums: H = 30 m and category C |
| IBM SEG-Y samples read as IEEE | correct conversion |
| Depths of the six default layers inconsistent with thicknesses | cumulated depths |
| V~s,eq~ computed on the saved model | computed on the solution chosen on screen |

Unchanged from the desktop: the frequency column label, offset by less than one df, and the undivided v/f in the initial estimate, which
only affects the starting point.

The full document is available on request.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20MASW%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/masw/docs/en/validazione.md).*
