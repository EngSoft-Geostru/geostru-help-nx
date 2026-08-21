# Design code and load combinations

The calculation is organised in **combinations**: the engine runs a full set of checks for
each set of partial factors, and the results shown are, for every check, those of the
**governing combination** (lowest FS).

## NTC 2018

- **Static — A1+M1+R3 (STR+GEO)**: factors taken from the *Partial factors* card (γ~A~
  from table 2.6.I, γ~M~ = 1, γ~R3~ from table 6.5.I: bearing capacity 1.4 · sliding 1.1 ·
  overturning 1.15). The factor on loads depends on the surcharge type.
- **Seismic** (generated automatically when k~h~ > 0): **unit** actions and parameters
  (§7.11.1), resistances from **table 7.11.III** (bearing capacity 1.2 · sliding 1.0 ·
  overturning 1.0), surcharge reduced by **ψ₂** and, for overturning only, a seismic
  coefficient **increased by 50%** (§7.11.6.2.1).

The Partial factors card shows the two columns **Static** (editable) and **Seismic**
(imposed by the code, read-only, visible when k~h~ > 0).

## Eurocodes and User

- **EC 7/8**: static A1+M1+R2 plus a seismic combination with unit factors (EN 1998-5).
- **User**: a single combination with the factors from the card and the seismic action
  exactly as you entered it — no automatic behaviour.

## Where you see them

In the **Checks** tab every combination is declared with its name and the factors used,
and each card reports the FS of all combinations with the *governing* badge; in the
**Reinforcements** tab you can switch from the **design envelope** to the individual
combinations. Global stability uses its own A2+M2+R2 approach.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20MRE%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mre/docs/en/combinazioni.md).*
