# Quickstart — your first calculation in 5 minutes

In 5 minutes you see RSL III working on a sample stratigraphic column.

## 1. Open the app

Go to [`nx.geostru.ai/rsl/`](https://nx.geostru.ai/rsl/).

## 2. Load a sample

Top toolbar → **Samples** → pick a ready-made case (e.g. *"Saturated sand
on bedrock — Central Italy M=6.0"*).

The sample populates:

- **Stratigraphy**: 4-6 layers with realistic Vs, γ, G/Gmax and ξ curves
- **Input accelerogram**: real seismic record (e.g. from ITACA)
- **Reference bedrock** (Vs > 800 m/s) as the base of the column

## 3. Run the calculation

Press **Run calculation** at the top. RSL III:

1. Discretises the column into sub-layers (step chosen automatically
   from Vs and f_max)
2. Initialises G = G_max and ξ = ξ_min for each layer
3. Computes the **transfer function** from bedrock to surface
   (reflection/transmission coefficients method, frequency domain)
4. Estimates γ_max for each layer; updates G and ξ by reading the
   degradation curves
5. **Iterates** until γ_eff changes by less than the tolerance (~0.5%)
   — typically 4-8 iterations

Time: 1-3 seconds for a 20-50 m column.

## 4. Inspect the results

The main outputs you see:

### Surface response spectrum

The **PSA** (Pseudo Spectral Acceleration) compared with the reference
NTC spectrum for the site. Where the RSL PSA **exceeds** the NTC one
are zones of **local amplification** that the site imposes on the
structure.

### γ_max, a_max, σ_max profiles

For each depth along the column, shows:

- **γ_max** (maximum shear strain, in %) — layers with γ > 0.1% are
  in a significantly non-linear regime
- **a_max** (peak acceleration) — amplification from bedrock to surface
- **σ_max** (maximum shear) — useful for liquefaction and stability
  checks

### ICMS amplification factors

**FA** (amplification factor, short periods 0.1-0.5 s), **FH** (long
periods 0.4-0.8 s) and **FT** (all periods) — the three indicators
required by Italian Level 3 seismic microzonation (ICMS 2008/2018).

[More on ICMS factors →](icms.md)

## 5. Export the Word report

Toolbar → **Report**. Download the `.docx` with:

- Cover page + input data
- Tabulated stratigraphy + degradation curves
- Input accelerogram + Fourier
- Surface response spectrum + NTC comparison
- γ_max, a_max, σ_max profiles
- ICMS amplification factors
- Conclusions

---

## Next steps

- [**Complete workflow**](workflow.md) — a real project from start to finish
- [**Equivalent-linear method**](metodo.md) — how the calculation works
- [**ICMS**](icms.md) — amplification factors for microzonation
- [**Input data**](dati-input.md) — complete description of every field

---

*Page useful? Questions? [Contact us](mailto:info@geostru.ai?subject=Help%20RSL%20III%20-%20Quickstart).*
