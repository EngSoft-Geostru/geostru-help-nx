---
title: Seismic action — Slope NX
---

# Seismic action

Slope NX includes seismic action with the **pseudo-static approach**: to each slice weight it adds a horizontal force k<sub>h</sub>·W and a vertical one k<sub>v</sub>·W, where k<sub>h</sub> and k<sub>v</sub> are the **seismic coefficients**.

Enable **Seismic analysis** in the **Analysis → Method and parameters** panel.

## Manual coefficients or from NTC

You can enter k<sub>h</sub> and k<sub>v</sub> **manually** (useful for EC/LRFD/User), or compute them to **NTC** from the seismic panel:

- **Subsoil category** (A–E) and **topographic category** (T1–T4).
- **Use class** and **nominal life** (V<sub>N</sub>) → reference period.
- Hazard parameters: a<sub>g</sub>/g (SLV), F<sub>0</sub>, T<sub>C</sub>*.

The computation returns a<sub>max</sub>, the reduction coefficient β and the coefficients k<sub>h</sub> = β·a<sub>max</sub>/g and k<sub>v</sub> = ±0.5·k<sub>h</sub> (per the code coefficients for soils and structures).

## Import from GeoStru PS

If you have already computed the hazard with **GeoStru Spectra** (or an equivalent tool), you can **import** the seismic-parameters file (`.txt`) and Slope NX fills in k<sub>h</sub>/k<sub>v</sub> automatically.

!!! note "Threshold in seismic conditions"
    With characteristic parameters (traditional method) the reference FoS values drop to **1.1–1.3** in the presence of an earthquake. With partial factors at limit states the verification remains satisfied for FoS ≥ 1.0.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Slope%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/slope/docs/en/sismica.md).*
