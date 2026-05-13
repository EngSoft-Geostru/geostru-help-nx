# RSL III — 1D Site Response Analysis

**RSL III** is the GeoStru web software for **site response analysis**
(SRA) on 1D soil columns. Given the site **stratigraphy** (layer
thickness, Vs, ρ, G/Gmax-γ and ξ-γ degradation curves) and a bedrock
**input accelerogram**, it computes the propagation of S waves to the
surface using the **equivalent-linear** scheme (iterative Idriss-Seed)
and returns the **response spectrum**, γ_max / a_max profiles and the
**ICMS amplification factors** for Level 3 seismic microzonation
(ICMS 2008/2018).

[**Open RSL III**](https://nx.geostru.ai/rsl/){ .md-button .md-button--primary }
[5-minute Quickstart](quickstart.md){ .md-button }

---

## What it does, in short

- **Input**: stratigraphy (thickness, Vs, ρ, dynamic curves), bedrock
  accelerogram (real or synthetic), analysis type
- **Calculation**: equivalent-linear scheme with successive iterations,
  until convergence of γ_eff (effective strain = 65% of γ_max)
- **Output**:
  - **Surface response spectrum** (PSA or SA)
  - **Input/output Fourier spectrum**
  - **Profiles** along the vertical: γ_max, a_max, σ_max
  - **ICMS amplification factors**: FA, FH, FT (for Level 3 seismic
    zonation)
- **Multi-site mode**: compare different columns (with one or more
  accelerograms), mean spectrum + statistics

## Who it's for

- **Geologists** producing **seismic microzonation** studies (ICMS
  Level 2 or 3) for municipalities
- **Earthquake engineers** designing buildings and structures with a
  site-specific accelerogram instead of the standard NTC spectrum
- **Consulting studios** integrating SRA analysis into a geotechnical
  report for construction in seismic zones

## How to get started

1. Open [`nx.geostru.ai/rsl/`](https://nx.geostru.ai/rsl/)
2. Load a sample or define the stratigraphy
3. Load an accelerogram (or use a sample one)
4. Press **Run calculation**
5. Inspect response spectrum + profiles + ICMS
6. Export the **Word report**

[See the complete workflow →](workflow.md)

## Manual chapters

### Getting started

- [**Quickstart**](quickstart.md) — 5 minutes from first access to first report
- [**Complete workflow**](workflow.md) — detailed input → calculation
  → export sequence

### Input

- [**Input data**](dati-input.md) — stratigraphy, degradation curves,
  input accelerogram, iteration parameters

### Calculation

- [**Equivalent-linear method**](metodo.md) — iterative Idriss-Seed
  scheme, transfer function, convergence, model limitations

### Output

- [**Amplification factors (ICMS)**](icms.md) — FA, FH, FT for Level 3
  seismic microzonation, ICMS 2008/2018 compliance

### Reference

- [**FAQ**](faq.md) — frequently asked questions

---

*Found an error or want to suggest content?
[Contact us](mailto:info@geostru.ai?subject=Help%20RSL%20III) — thanks!*
