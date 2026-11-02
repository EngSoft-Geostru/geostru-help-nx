# Theory

## The H/V ratio

The ground vibrates all the time because of wind, sea and human activity. The ratio between the horizontal and the vertical spectrum of this noise has a peak at the site resonance frequency when
soft soil lies on stiffer ground (Nakamura 1989). For a single layer of thickness H and velocity V~s~ on rigid bedrock the resonance is about:

```text
f0 ≈ Vs / (4 H)
```

With 20 m at 200 m/s that is 2.5 Hz. It is an order of magnitude: the ellipticity maximum approaches this value only with a strong contrast. With contrast 10 the difference is nil, with contrast 4
it is 28 %.

## The calculation chain

1. **Windows** of samples from the recording.
2. Tukey **taper** and **Fourier transform**, with zero padding to the next power of 2.
3. **Smoothing** and resampling on the frequency grid.
4. **Mean spectra**: arithmetic mean of the amplitudes over the included windows.
5. **H/V**: combined horizontal divided by vertical, on the mean spectra.
6. **σ**: scatter of the window H/V around the mean curve, divided by the mean.

The curve is a **ratio of means**, not a mean of ratios: the desktop choice, kept. The σ is relative and is added to the curve to draw the band, as in the desktop program. The SESAME text instead
uses the geometric mean of the window curves and a factor σ~A~, which HVSR NX applies if you choose the text criteria: see [H/V spectrum](spettro-hv.md).

## Ellipticity

**Ellipticity** is the ratio between the horizontal and vertical displacement of a Rayleigh wave. It depends on frequency and stratigraphy, which is why the H/V curve can be read as the
ellipticity of the fundamental mode. This reading is an approximation: the measured curve also contains Love waves, higher modes and body waves (Fäh et al. 2001).

## SESAME

The European SESAME project published guidelines on the technique in 2004: durations, measurement conditions, reliability criteria. The criteria are in [H/V spectrum](spettro-hv.md). A peak that
passes the criteria is not thereby stratigraphic.

## V~s,eq~

See [V~s,eq~ and category](categoria.md).

## Bibliography

- SESAME (2004), *Guidelines for the implementation of the H/V spectral ratio technique on ambient vibrations*, Deliverable D23.12.
- Nakamura Y. (1989), Quarterly Report of RTRI 30(1), 25–33.
- Konno K., Ohmachi T. (1998), Bull. Seism. Soc. Am. 88(1), 228–241.
- Fäh D., Kind F., Giardini D. (2001), Geophys. J. Int. 145(2), 535–549.
- Wathelet M. (2005), PhD thesis, Université de Liège.
- Nelder J.A., Mead R. (1965), Computer Journal 7(4), 308–313.
- D.M. 17/01/2018, Italian building code (NTC 2018), §3.2.2.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20HVSR%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/hvsr/docs/en/teoria.md).*
