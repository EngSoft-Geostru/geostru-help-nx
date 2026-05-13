# Input data — description of each field

Field-by-field reference for the RSL III app. For the operational flow
see [Workflow](workflow.md).

## Stratigraphy

**Stratigraphy** tab — define the 1D column from ground level downward,
down to the **bedrock** (seismic reference substratum, Vs ≥ 800 m/s).

### For each layer

| Field | Unit | Description |
|---|---|---|
| **Thickness (h)** | m | Layer thickness. Total sum ≥ depth to reference bedrock. |
| **Vs** | m/s | Shear-wave velocity at small strain (γ < 10⁻⁴%). From direct seismic tests: cross-hole, down-hole, MASW, ReMi, passive seismic (microtremor HVSR). |
| **ρ** (density) | kN/m³ | Unit weight. For soils above the water table ρ_d (dry), below ρ_sat (saturated). |
| **G_max** | MPa | Small-strain shear modulus. RSL III computes it automatically as `G_max = ρ · Vs²` if you don't enter it. |
| **ξ_min** | % | Minimum damping (small strain). Typical: 0.5-1% (dense sands), 1-3% (clays), 2-5% (anthropic fills). |
| **G/Gmax-γ curve** | — | Modulus degradation function. Chosen from the library (see below). |
| **ξ-γ curve** | — | Damping function. Same library as the G curve. |
| **Lithology** | — | Descriptive, does not enter the calculation. |

### Criteria for defining the bedrock

The last layer must be the seismic reference bedrock. Characteristics:

- **Vs ≥ 800 m/s** (NTC 2018 cat. A definition)
- **Expected linear elastic behaviour** at the site's seismicity level
  (γ < 10⁻³ %)
- Deep enough to capture the **first site natural frequency**:
  T₀ = 4H/Vs_mean → typically H = 30-100 m

!!! warning "Bedrock depth"
    If the bedrock is too shallow (e.g. 5-10 m above Vs > 800 m/s), the
    site **does not significantly amplify** and RSL III returns output
    similar to the standard NTC spectrum. In these cases detailed SRA
    is not worthwhile.

## Degradation curves

RSL III ships with a **standard library**. For each layer you can assign:

### Clays (Vucetic-Dobry 1991)

Family of curves as a function of the **plasticity index PI**:

- **PI = 0** (non-plastic clays / silty sands)
- **PI = 15-30** (medium-plastic clays)
- **PI = 30-50** (highly plastic clays)
- **PI > 50** (very high plasticity clays)

As PI increases, the G/Gmax curve "degrades more slowly" and ξ is
smaller. Highly plastic clays are the least dissipative case.

### Sands (Seed-Idriss 1970)

*Upper / mean / lower* family for sands. The **mean** is used by
default. Upper and lower cover the natural dispersion of sands.

### Darendeli (2001) — general formula

Synthetic literature curves, depending on PI, OCR and σ'_v (confining
pressure). More modern, recommended for advanced studies.

### EPRI (1993)

Family of curves by depth (typical of nuclear studies). Differentiates
by depth range (0-15 m, 15-50 m, 50-150 m, >150 m).

### Custom curves

Upload a `γ [%], G/Gmax [-], ξ [%]` table from your specific study (lab
tests: cyclic triaxial, resonant column, cyclic torsional shear). CSV
format with header.

## Input accelerogram

**Seismic input** tab. Load the horizontal acceleration accelerogram
at the **bedrock**.

### Supported formats

| Format | Typical origin |
|---|---|
| **PEER** | NGA-West / NGA-Subduction, worldwide accelerogram archive |
| **ITACA** | Italian Accelerometric Archive (INGV, Italian records) |
| **CSV / TXT** | header `time, accel` (or `t, a`) — generic |
| **GeoStru ACC** | export from [Spectra](https://www.geostru.ai/) or other GeoStru software |

### What to know about the accelerogram

- **Δt** (sampling step): typically 0.005-0.01 s
- **Total duration**: 20-40 s for real recordings, can reach 80 s for
  synthetic accelerograms with a long tail
- **a_max**: peak acceleration (PGA), in g or m/s²
- **Magnitude Mw and distance R**: useful in the technical report
  (spectral compatibility with NTC)

### Outcrop vs within

⚠️ Critical point:

- If the accelerogram is recorded on **outcropping bedrock** (e.g. rock
  exposed at the surface), choose *"Outcrop"* in the app. RSL III will
  apply spectral deconvolution, halving the amplitude inside the column.
- If the accelerogram is already defined **inside** the column (e.g.
  from a previous SHAKE model), choose *"Within"*. No deconvolution.

For archive recordings (PEER, ITACA): **outcrop** is the right choice
in 99% of cases.

### NTC-compatible spectrum

For NTC 2018-compliant analyses, the accelerograms must be
**spectrum-compatible** with the site (nominal life, usage class,
return period). Typically you use:

- **7 real accelerograms** (NTC 2018 recommendation, par. 7.3.5)
- Modified by scaling or spectral matching to be compatible with the
  target spectrum

In **multi-input** mode RSL III processes the 7 accelerograms and
produces the **mean** spectrum (plus envelope / std) — ready for
structural verification.

## Iteration parameters

**Advanced** tab:

- **Convergence tolerance**: default `0.5%` (max γ_eff variation between
  successive iterations)
- **Max iterations**: default `30` (usually converges in 4-8)
- **γ_eff/γ_max**: default `0.65` (Idriss formulation). Some literature
  uses 0.5 or 0.85 for special cases.
- **Maximum frequency f_max**: default `25 Hz` (caps discretisation and
  aliasing). Raise for studies with high-frequency accelerometers.

The default values are recommended. Change only if you know what
you're doing.

## Summary: minimum to get started

1. **Stratigraphy**: 3-10 layers with thickness, Vs, ρ
2. **Dynamic curves**: chosen from the library (even default Seed-Idriss)
3. **Accelerogram**: 1 PEER or ITACA file, duration > 20 s

Everything else is refinement.

---

## See also

- [Complete workflow](workflow.md) — practical use of the input data
- [Equivalent-linear method](metodo.md) — how RSL III uses these data
- [FAQ](faq.md) — questions on input parameters

---

*Page useful? [Contact us](mailto:info@geostru.ai?subject=Help%20RSL%20III%20-%20Input%20data).*
