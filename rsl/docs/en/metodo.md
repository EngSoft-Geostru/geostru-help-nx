# Equivalent-linear method

RSL III implements the **equivalent-linear** method of Idriss-Seed
(1968, 1970), the industry standard for 1D site response analysis in
the frequency domain.

## Basic idea

Real soil is **non-linear**: G and ξ depend on γ_max reached during
the earthquake. A truly non-linear analysis solves the equation of
motion step-by-step in the time domain, with complex hysteretic
constitutive laws.

The **equivalent-linear** approach is a practical compromise:

1. Solve a **linear** analysis in the frequency domain (simple and fast)
2. Estimate γ_max in each layer
3. Update G and ξ to the "secant" corresponding to γ_eff = 0.65 · γ_max
4. Re-solve the linear analysis with the new G and ξ
5. Iterate until convergence

The γ_eff = 65% of γ_max is an empirical approximation to "represent"
the average effect of non-linearity over the entire cyclic history.

## Calculation scheme

### Step 1 — Discretisation

The stratigraphic column is discretised into N **sub-layers** of
thickness Δh. Criterion to avoid aliasing at high frequencies:

$$
\Delta h \leq \frac{V_s^{\min}}{4 \cdot f_{\max}}
$$

with f_max = 25 Hz (default). For Vs minimum = 100 m/s → Δh ≤ 1 m.

RSL III computes Δh automatically; typically discretises into 20-50
sub-layers.

### Step 2 — Transfer function

For vertical plane S waves in horizontally stratified columns, the
transfer function H(ω) between surface and bedrock is computed with
the **reflection/transmission coefficients method** (Haskell-Thomson,
i.e. the *propagator matrix* method of Aki-Richards):

$$
H(\omega) = \frac{u_{\text{surface}}(\omega)}{u_{\text{bedrock}}(\omega)}
$$

where each layer interface generates coefficients `r` (reflection) and
`t` (transmission) as a function of acoustic impedances `Z = ρ · Vs`.

For N layers the transformation becomes a product of 2×2 matrices (one
per layer). RSL III computes it at ~2000-4000 frequencies of the
accelerogram Fourier transform.

### Step 3 — Output Fourier spectrum

$$
F_{\text{out}}(\omega) = H(\omega) \cdot F_{\text{in}}(\omega)
$$

The inverse Fourier transform gives the **surface accelerogram** in
the time domain.

### Step 4 — γ_max estimate

In each sub-layer, given the computed maximum shear τ_max:

$$
\gamma_{\max} = \frac{\tau_{\max}}{G_{\text{secant}}}
$$

And hence:

$$
\gamma_{\text{eff}} = 0{,}65 \cdot \gamma_{\max}
$$

### Step 5 — Update G and ξ

For each sub-layer, read the degradation curves at γ_eff:

- **G_new = G_max · (G/G_max)(γ_eff)**
- **ξ_new = ξ(γ_eff)**

### Step 6 — Convergence

Compare γ_eff(iter) with γ_eff(iter-1). If the maximum variation across
all sub-layers is < tolerance (default 0.5%), **convergence reached**.
Otherwise go back to step 2 with the new G and ξ.

Typically converges in **4-8 iterations** for standard accelerograms.

## Method limitations

### 1. Average equivalence

γ_eff = 65% of γ_max is a proxy for the average effect. For
accelerograms with **a single, very isolated peak** + low tail (e.g.
near-impulsive events) it overestimates non-linearity. For accelerograms
with **many similar-amplitude cycles** (long tail) the estimate is good.

### 2. Strong-motion non-linearity

For **strains γ > 1%** the equivalent-linear method becomes inaccurate:
heavily strained clays have asymmetric hysteretic behaviour that the
secant model does not capture. For extreme shaking (unstable slopes in
the Friuli / L'Aquila zone) use non-linear SRA in the time domain.

### 3. 1D vertical

Assumes **vertical propagation** of S waves. Does not capture:

- **2D / 3D** topography effects (ridges, valleys)
- **Sedimentary basin** effects (lateral reflections)
- **Surface waves** (Rayleigh, Love)

For sites with significant topography or marked basin geometry, pair
with 2D analysis using **Geostru RSL 2D**, our dedicated software for
two-dimensional site response.

### 4. Horizontal bedrock

The bedrock-soil interface is assumed horizontal. For strongly inclined
bedrock (e.g. slope accumulations) the 1D representation is inadequate.

## When to use RSL III (and when not)

✅ **Suitable**:

- **Seismic microzonation** Level 3 studies (ICMS)
- NTC spectrum vs site spectrum verification for standard design
- Horizontally stratified granular/cohesive masses with known Vs
- **Moderate intensity** seismic events (a_max ≤ 0.4 g, γ_max < 1%)

❌ **Not suitable** (or requires integration with other tools):

- Studies on **slopes** or ridges (need 2D topographic FA)
- Real-time **liquefaction** analysis (RSL estimates γ_max but not
  pore-pressure build-up — use LiquiTer for liquefaction)
- **Highly non-linear** events (a_max > 0.6 g, γ > 2%)
- Deep sedimentary basins with 2D/3D effects

## References

- **Idriss I.M., Seed H.B. (1968)** — *Seismic response of horizontal soil
  layers*. JSMFD, ASCE
- **Schnabel P.B., Lysmer J., Seed H.B. (1972)** — *SHAKE: A computer
  program for earthquake response analysis of horizontally layered sites*.
  EERC Report, UC Berkeley
- **Bardet J.P., Tobita T. (2001)** — *NERA / EERA: Equivalent-linear
  earthquake site response analyses*
- **Kramer S.L. (1996)** — *Geotechnical Earthquake Engineering*. Prentice Hall
- **ICMS 2008/2018** — *Indirizzi e Criteri per la Microzonazione Sismica*,
  Italian Department of Civil Protection

---

## See also

- [Complete workflow](workflow.md) — the method in the process
- [Input data](dati-input.md) — which curves to choose
- [ICMS factors](icms.md) — method output for microzonation

---

*Page useful? [Contact us](mailto:info@geostru.ai?subject=Help%20RSL%20III%20-%20Method).*
