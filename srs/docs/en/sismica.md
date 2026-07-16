---
title: Seismic action
---

# Seismic action

SRS NX accounts for seismic action with a **pseudostatic** approach: a
single horizontal seismic coefficient representing the increase in
destabilising forces caused by an earthquake.

## The K_h coefficient

In the **Seismic parameters** section set:

| Symbol | Parameter | Unit |
|---|---|---|
| I.11 K_h | Horizontal seismic coefficient | — |

With **K_h = 0** (default) the check is purely static. With **K_h > 0** SRS
introduces two additional forces into the overburden wedge equilibrium:

- **Horizontal seismic force** `F_h = W · K_h`
- **Vertical seismic force** `F_v = F_h / 2`

Both enter the computation of the resisting and acting shear forces (see
[Slope and substrate](pendio.md#how-srs-computes-fs0)), reducing **FS₀**
and increasing the tension force required from the anchor.

## Effect on the γ_Q1 coefficient

When K_h is non-zero, SRS applies the seismic-condition partial factor of
actions **γ_Q1** (γ_Q1 = 1.0 for both NTC 2018 and Eurocode) instead of the
static one (γ_Q1 = 1.5). This coefficient multiplies the design tension and
shear force on the anchor (E.10, E.11). See [Design checks](verifiche.md).

## How to determine K_h

You can compute K_h with any code-based method of your choice, starting
from the site's seismic hazard (ground acceleration a_g, subsoil and
topographic category). Alternatively, SRS's **AI assistant** fetches the NTC
seismic hazard parameters for a location and proposes a ready-to-review K_h
value. See
[AI assistant](assistente-ai.md#3-seismic-coefficient-from-a-location).

!!! warning "Always check local amplification"
    The coefficient proposed by the assistant assumes unit stratigraphic and
    topographic amplification (S = S_S · S_T = 1). If the site's subsoil
    category or morphology implies significant amplification, increase K_h
    accordingly before using it in the design: the choice remains the
    designer's responsibility.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20SRS%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/srs/docs/en/sismica.md).*
