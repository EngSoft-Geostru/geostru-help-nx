# Soil category

This tab works on the solution chosen in [Inversion](inversione.md).

## Vs,eq and category

Choose **NTC 2018** or **NTC 2008** and enter the **foundation depth**, measured from ground level.

- **NTC 2018**: V~s,eq~ = H / Σ(h~i~/V~s,i~). H is the depth of the bedrock with V~s~ ≥ 800 m/s; if there is none within 30 m, H = 30.
- **NTC 2008**: V~s,30~ over the 30 m below the foundation. **Probabile suolo di tipo E** flags the condition that velocity
  alone cannot establish.

![Category and category table](img/06-categoria.png)

If the value falls exactly on a boundary (100, 360 or 800 m/s), or the foundation is in the bedrock beyond 30 m, the code
table assigns no category and the app says so in words instead of picking one.

## Layer parameters

For each layer: G~0~, E~d~, K, E and ν. These are **dynamic moduli at small strain**: do not use them directly in settlement
calculations.

**NSPT** (Ohta and Goto) and **Q~c~** (Jamiolkowski) are empirical correlations inverted from V~s~: choose composition, age
factor and soil type. Beyond 100 blows or 5000 kPa the app shows N/D. The half-space has no such estimates.

## Transfer function

The chart shows the 1D response of the profile, with 1 % damping, and the frequency of the maximum. With such low damping the
peaks are very high: it indicates resonance frequencies, not a design amplification.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20MASW%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/masw/docs/en/categoria.md).*
