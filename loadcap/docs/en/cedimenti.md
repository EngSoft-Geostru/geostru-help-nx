---
title: Settlements
---

# Settlements

Settlements are computed with the **service (SLS)** combinations. The
**Settlements** tab reports, for the selected combination, the elastic and
oedometric contributions per layer, the optional Burland & Burbidge estimate and
the time curve.

!!! note "With which loads"
    Unlike the bearing capacity (ULS), settlements are evaluated with the
    **service** pressures. The **combination selector** at the top of the tab lets
    you switch between SLS combinations.

## Elastic settlements (Timoshenko-Goodier)

Immediate settlement of an elastic half-space, computed **at the centre** and **at
the edge** of the foundation:

`w = q·B·(1−ν²)·I / E`

where I is an influence factor depending on the shape (B/L) and on the optional
**rigid substratum depth** (bedrock). It needs the **elastic modulus E** and the
**Poisson's ratio ν**. The result is in **mm**.

## Oedometric settlements

For layers with an oedometric modulus **E_ed**, the primary consolidation
settlement is computed by sublayers. Loadcap offers two formulations:

- **One-dimensional**: `w_c = Δσ·H / E_ed`;
- **Logarithmic** (Terzaghi): `w_c = H·RR·log₁₀[(σ′_v0 + Δσ)/σ′_v0]`, with
  `RR = (σ′_v0 + Δσ)/(0.435·E_ed)`.

Choose the formulation with the **Oedometric method** selector. The **secondary
settlement** (creep) is added if the C_s coefficient is defined.

!!! tip "Which method"
    The logarithmic method is consistent with classic consolidation theory; the
    one-dimensional one is more direct and conservative for small stress
    increments. For comparisons with desktop calculations, use the same
    formulation.

## Schmertmann method

For layers with an elastic modulus **E** but without E_ed, Loadcap applies the
**Schmertmann** method (1970-1978), based on the strain factor **I_z**:

- net pressure `q = q_applied − σ′_v0(D)`;
- depth factor `C₁ = 1 − 0.5·σ′_v0/q` (minimum 0.5);
- peak `I_z,max = 0.5 + 0.1·√(q/Δp)`;
- triangular I_z distribution (axisymmetric or plane depending on L/B);
- creep factor `C₂ = 1 + 0.2·log₁₀(t/0.1)`.

The per-layer settlement is `w = C₁·q·I_z·H_s/E`, in cm.

## Burland & Burbidge

Empirical estimate based on the **N_SPT** blow count, suited to granular soils:

`w = f_s·f_h·f_t·(q − ⅔·σ′_v0)·I_c·B^0.7`

with I_c the compressibility index (function of N_SPT), and the correction factors
f_s (shape), f_h (thickness of the compressible layer) and f_t (time). Enable it
with the dedicated checkbox; it requires N_SPT on the layers.

## Time-settlement curve

For layers with a consolidation coefficient **C_v**, Loadcap traces the **time
curve** of the consolidation settlement, from Terzaghi's theory:

- settlement reached at the degree of consolidation U: `w(U) = w_t·U/100`;
- corresponding time: `t(U) = T_v(U)·H²/C_v`.

The table reports the pair (consolidation percentage, time in days) up to 100%.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Loadcap%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/loadcap/docs/en/cedimenti.md).*
