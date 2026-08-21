# External and internal checks

## External checks

In order: **overturning**, **sliding**, **bearing capacity** (Hansen with load inclination
factors). Each card shows the FS of the governing combination in large type and, below it,
the FS of every combination with the *governing* badge; the strip at the top declares the
name and the factors of each combination.

- **Overturning**: moments about the downhill toe; FS = M~s~/M~r~. In the seismic
  combination the seismic coefficient is increased by 50% (NTC §7.11.6.2.1).
- **Sliding**: resistance W·tanφ~f~ on the foundation plane against the thrust.
- **Bearing capacity**: Hansen q~lim~ against the vertical load.

![External check cards with the FS of the governing combination](img/09-verifiche.png)

## Internal checks

For every reinforcement level: **pullout** (the effective length is the portion beyond the
failure wedge) and **rupture** (R~d~ against the action). In the Design approach the
required length is derived level by level; in Check the imposed length is verified. If a
level falls entirely inside the wedge the program reports it.

The overall verdict ("All checks are satisfied") requires FS ≥ 1 on external and internal
checks, plus global stability and the tieback/compound checks when they are computed.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20MRE%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mre/docs/en/verifiche.md).*
