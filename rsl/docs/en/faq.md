# FAQ — frequently asked questions

## General

### Is RSL III free?

RSL III is part of the **GeoStru NX suite** with a *freemium* plan.
For up-to-date details visit [`geostru.ai`](https://www.geostru.ai/)
or write to `info@geostru.ai`.

### Do I have to install anything?

**No**. RSL III is a **web app** that opens from
[`nx.geostru.ai/rsl/`](https://nx.geostru.ai/rsl/) in any modern
browser.

### What does "equivalent linear" mean?

It is a site response analysis method that approximates the non-linear
soil behaviour with successive iterations of **linear** analyses. See
[metodo.md](metodo.md) for details.

---

## Stratigraphy

### Where do I get Vs values?

Direct measurement with seismic tests:

- **MASW** (Multichannel Analysis of Surface Waves) — the most common,
  from the surface with aligned geophones
- **ReMi** (Refraction Microtremor) — from ambient seismic noise
- **Cross-hole** / **Down-hole** — paired or single boreholes with
  seismograph (more accurate)
- **HVSR** (passive microtremor seismic, Nakamura 1989) — only to
  estimate the site fundamental frequency, not point-wise Vs(z)
- **Seismic Cone Penetration Test** (SCPT) — continuous Vs along a CPTU

If you don't have direct measurements, **do not** estimate Vs from
literature or N-SPT — it is too imprecise for RSL.

### How deep must the stratigraphy be?

Down to the **seismic reference bedrock** (Vs ≥ 800 m/s).

In Italy typically:

- Po Plain / coastal sedimentary: 50-300 m
- Intermontane basins (Umbria, Marche, Abruzzo): 30-100 m
- Mountain / cliff areas: 5-30 m

If you don't reach Vs > 800 m/s with the boreholes, extrapolate with
constant or linearly increasing Vs to an assumed depth (document this
in the technical report).

### Can I use SPT instead of Vs?

**No, not directly**. SPT measures penetration resistance, not shear-wave
velocity. There are empirical correlations (Ohta-Goto 1978, Ohsaki-
Iwasaki 1973, Pitilakis 1999) but they are **very uncertain** (typical
error 30-50%).

For liquefaction SPT is fine (see
[LiquiTer](https://nx.geostru.ai/liquiter/)). For RSL you need direct
seismics.

### How do I choose the degradation curve?

Depends on the soil:

- **Sands** → Seed-Idriss (1970), Darendeli (2001)
- **Clays** → Vucetic-Dobry (1991), as a function of PI
- **Gravels** → specific curves (limited library, rarely available)
- **Anthropic fills** → sand curves with increased ξ_min
- **Soft marine soils** → Vucetic-Dobry for medium PI + smaller γ_min

When in doubt, try 2 different curves (e.g. Seed-Idriss + Darendeli)
and compare the results. If FA/FH factors change little (< 10%), the
choice is not critical.

---

## Input accelerogram

### How many accelerograms do I need?

For NTC 2018 / ICMS 2008-2018 compliant studies: **at least 7
spectrum-compatible accelerograms** (NTC par. 7.3.5). RSL III in
multi-input mode processes them all and produces the **mean** spectrum.

For sensitivity or educational studies: 1-3 accelerograms are enough.

### Where do I find real accelerograms?

- **PEER NGA-West** (USA, but also European events): [ngawest2.berkeley.edu](https://ngawest2.berkeley.edu/)
- **ITACA** (Italian, INGV): [itaca.mi.ingv.it](http://itaca.mi.ingv.it/)
- **ESM** (European Strong-Motion Database): [esm.mi.ingv.it](https://esm-db.eu/)
- **GeoStru Spectra** ([geostru.ai](https://www.geostru.ai/)): GeoStru suite for spectrum-compatible accelerogram selection

### How do I do "spectral matching" / scaling?

RSL III **does not** do automatic scaling. You must pre-process the
accelerograms with dedicated software — we recommend **GeoStru Spectra**
([geostru.ai](https://www.geostru.ai/)), which produces NTC-spectrum-
compatible accelerogram series ready to import into RSL III.

### Outcrop or within?

See [dati-input.md#outcrop-vs-within](dati-input.md#outcrop-vs-within).
For archive recordings (PEER, ITACA): **outcrop** is the right choice
in 99% of cases.

---

## Calculation

### How many iterations are needed?

Typically **4-8** for standard accelerograms. If the calculation
requires >15 iterations and does not converge, it usually means:

- Soil with γ_max > 1% (strongly non-linear regime → EQL method not
  reliable, use non-linear SRA)
- Anomalous degradation curve
- Too-fine discretisation (reduce f_max)

### What to do if the calculation does not converge?

1. Raise the tolerance to 1% (default 0.5%)
2. Raise max iterations to 50
3. Check that the computed γ_max is < 1% in all layers
4. If γ_max > 1% in any layer → the site is in a significantly
   non-linear regime, RSL III is not the right tool

### γ_eff = 0.65 · γ_max — why 65%?

It is an empirical value calibrated by Idriss (1968) on experimental
tests. It represents the "average equivalent strain" during the cyclic
history. For seismic histories with a single dominant pulsation it can
be 0.5-0.55, for long-tail histories 0.7-0.85. RSL III uses 0.65 by
default; you can change it under **Advanced**.

---

## Output

### FA, FH, FT — which one for my project?

See [icms.md](icms.md) for the full table.

In short:

- **Low-rise buildings** (1-3 storeys): FA
- **Medium-rise buildings** (4-7 storeys): FH
- **Tall buildings** (10+ storeys): the RSL spectrum directly (FT is
  only a summary)

### The RSL spectrum is below the NTC one, is that OK?

Yes, it can happen. It means your site amplifies **less** than the
standard NTC spectrum predicts for the assumed ground category.
Consequence: **you can design less conservatively** but only if your
RSL analysis is well supported by:

- Measured Vs (not estimated)
- 7+ spectrum-compatible accelerograms
- ICMS 2008/2018 compliance

Otherwise use the standard NTC spectrum.

### Post-seismic settlements?

RSL III **does not** compute post-seismic settlements from liquefaction.
If your site has liquefiable layers, after the RSL analysis use
[**LiquiTer NX**](https://nx.geostru.ai/liquiter/) for liquefaction +
settlements.

---

## My question isn't here

[Contact us](mailto:info@geostru.ai?subject=Help%20RSL%20III%20-%20FAQ)
and we'll add it.
