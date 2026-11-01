# Theory

## The idea

Rayleigh waves travel at different speeds depending on frequency: low frequencies "feel" deeper ground. The
velocity-frequency curve (**dispersion curve**) depends on the V~s~ profile, and inverting it recovers the profile.

## f-v spectrum

For each frequency and trial velocity the traces are brought back into phase and summed (Park, Miller and Xia, 1999):

```text
S(f, v) = Σ_k U_k(f) · exp(−i · 2π · f · x_k / v)
```

The modulus, normalised to the maximum of each column, is the map. If v is right the traces add in phase and |S| is large.

## Forward model

The theoretical curve of a layered profile is computed with the Thomson-Haskell and Dunkin propagator. The engine derives
from Geopsy/gpdc (M. Wathelet) and was validated to machine precision against the desktop's native library.

## Inversion

The optimiser is the Nelder-Mead simplex (1965), with bounds and re-initialisation. The objective function is

```text
misfit = (1 + nD − nR) · √( Σ ((v_obs − v_calc) / v_obs)² / nR )
```

with n~D~ picks and n~R~ those for which the mode exists. The percentage error is the ratio between the mean of
(v~obs~ − v~calc~)² and the mean of v~obs~², times 100.

## Parameters

G = ρV~s~², E~d~ = ρV~p~², K = ρ(V~p~² − 4/3 V~s~²), E = 2ρV~s~²(1+ν).

## References

Park C.B., Miller R.D., Xia J. (1999), *Multichannel analysis of surface waves*, Geophysics 64(3). Thomson W.T. (1950), J. Appl. Phys. 21.
Haskell N.A. (1953), BSSA 43. Dunkin J.W. (1965), BSSA 55. Wathelet M. (2005), PhD thesis, Univ. de Liège. Nelder J.A., Mead R. (1965),
Computer Journal 7. Ohta Y., Goto N. (1978), Earthq. Eng. Struct. Dyn. 6. Jamiolkowski M. et al. (1985), Proc. XI ICSMFE.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20MASW%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/masw/docs/en/teoria.md).*
