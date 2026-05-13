# ICMS amplification factors

The **amplification factors** quantify in a synthetic way how much the
site amplifies seismic shaking with respect to the reference bedrock.
They are the main output of a **Level 3 seismic microzonation** per the
**Italian Indirizzi e Criteri per la Microzonazione Sismica**
(ICMS 2008/2018, Department of Civil Protection).

## The 3 factors

ICMS requires **three factors** computed over specific period intervals:

| Factor | Interval | Meaning |
|---|---|---|
| **FA** | 0.1 – 0.5 s | Short periods — stiff structures (buildings up to 5 storeys) |
| **FH** | 0.4 – 0.8 s | Medium-long periods — 5-10 storey buildings |
| **FT** | all | Full spectrum (a summary scalar) |

Each factor is the ratio of the integral of the site response spectrum
(RSL output) and the integral of the NTC bedrock spectrum (cat. A) over
the specific period interval:

$$
F = \frac{\int_{T_1}^{T_2} \text{PSA}_{\text{site}}(T) \, dT}{\int_{T_1}^{T_2} \text{PSA}_{\text{bedrock}}(T) \, dT}
$$

(simplified formulation — the ICMS version uses integration over
discrete PSA values at the step specified by the standard).

## Interpretation

- **F = 1.0** → the site behaves like a standard bedrock (no
  amplification)
- **F = 1.0–1.5** → modest amplification, common
- **F = 1.5–2.0** → significant amplification, sensitive site
- **F > 2.0** → very high amplification, problematic soil (sedimentary
  basins, thick soft soils)

The F values are the **main input** for **municipal seismic
microzonation maps** and for urban planning decisions (unstable zones,
stable amplified zones, stable non-amplified zones).

## Which factor to use for what

### For building design

It depends on the **fundamental period** of the building T₁:

- **Low-rise buildings** (1-3 storeys, T₁ ≈ 0.1-0.3 s): use **FA**
- **Medium-rise buildings** (4-7 storeys, T₁ ≈ 0.4-0.7 s): use **FH**
- **Tall buildings** (10+ storeys, T₁ > 1 s): use the RSL spectrum
  directly, because standard ICMS does not cover long periods

### For municipal microzonation

You produce **FA maps** and **FH maps** overlaid on the municipality's
geological cartography. Areas with the same F range are **homogeneous
seismic micro-zones**.

### For vulnerability studies

FT (single scalar) is the fastest way to compare different
stratigraphy-input combinations.

## ICMS Level 3 procedure in practice

1. **Identify the representative geological sections** of the
   municipality (typically 3-10 sections)
2. **Define the stratigraphy** along each section (Vs from MASW +
   geognostic boreholes)
3. **Choose 7 accelerograms** spectrum-compatible with the area's NTC
4. For each significant stratigraphic column, run RSL III in
   **multi-input** mode with the 7 accelerograms
5. Compute FA, FH, FT as the **mean** over the 7 accelerograms
6. Create the **thematic maps** by overlaying the F values on the
   micro-areas
7. Publish the **microzonation report** following the ICMS structure

RSL III includes automatic computation of FA, FH, FT — see the
**Results** tab → **Amplification factors** pane.

## RSL III output for ICMS

The **Word report** automatically includes:

- Table of the 3 factors for each input accelerogram
- **Statistics** (mean, standard deviation) in multi-input mode
- Mean PSA plot + max/min envelope
- Comparison with the standard NTC spectrum (cat. A) → reference line

For a complete **microzonation project**, also export:

- PSA spectrum CSV point-by-point (for GIS cartography)
- γ, a, σ vs depth profiles (for the technical report)

## Reference standards

- **ICMS 2008/2018** — *Indirizzi e Criteri per la Microzonazione
  Sismica*, Italian Department of Civil Protection (DPC)
- **NTC 2018** — D.M. 17/01/2018, chapter 7.11.3 (seismic action)
- **EC8 — EN 1998-5** — Eurocode 8, Annex F (local effects)
- **OPCM 3274/2003** and **3519/2006** — establishment of mandatory
  seismic microzonation in Italian municipalities

---

## See also

- [Equivalent-linear method](metodo.md) — how the factors are computed
- [Complete workflow](workflow.md) — microzonation end-to-end
- [FAQ](faq.md) — questions on ICMS

---

*Page useful? [Contact us](mailto:info@geostru.ai?subject=Help%20RSL%20III%20-%20ICMS).*
