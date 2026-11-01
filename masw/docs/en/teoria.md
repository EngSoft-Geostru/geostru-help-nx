# Theory

This page summarises what the MASW survey measures and how MASW NX goes from the traces to the
V~s~ profile and the subsoil category. The formulas are the same as in the
[validation document](validazione.md).

## The MASW survey

**MASW** (Multichannel Analysis of Surface Waves) derives the shear-wave velocity profile from
the **dispersion of Rayleigh surface waves**. In layered ground, waves of different frequency
have different wavelengths and therefore "feel" different thicknesses: low frequencies (long
wavelengths) sample the ground at depth, high frequencies only the shallow layers. The phase
velocity thus depends on frequency, and this dependence, the **dispersion curve**, carries the
information on the V~s~ profile.

In the **active** survey a source (usually a sledgehammer on a plate) generates the waves at
the end of a linear **line** of vertical geophones at constant spacing dx (typically 12 or 24
4.5 Hz geophones, 1–3 m apart). A seismograph records the traces. The geometry affects the
result:

- the **length of the line** limits the longest wavelength resolved, and therefore the
  investigation depth;
- the **spacing** dx limits the shortest wavelength, and therefore the near-surface
  resolution;
- the **source offset** from the first geophone lets a fully formed surface wave arrive,
  without letting it attenuate too much.

## The f-v spectrum

The phase velocity – frequency spectrum is computed with the **phase-shift** method (Park,
Miller and Xia, 1998–1999), a weighted sum (slant stack) in the frequency domain:

1. the Fourier transform U~j~(f) of each trace u~j~(t), at the geophone at position x~j~, is
   computed;
2. for each frequency f and each trial velocity v the traces are brought into phase for that
   velocity and summed:

    E(f, v) = | Σ~j~ U~j~(f) / |U~j~(f)| · exp(i·2π·f·x~j~/v) |

3. each column (frequency) is normalised to its maximum.

Where v is the true phase velocity of a mode at that frequency, the traces add up in phase
and the map shows a maximum. The ridges of the map are the dispersion curves of the Rayleigh
**modes**: the **fundamental** (mode 0) and the **higher modes**.

### Apparent curve and regression

The maximum of each column gives the **apparent curve**. MASW NX excludes the maxima equal to
the minimum or maximum of the whole curve (edges of the map) and fits a **polynomial
regression** of degree 2–10 through it. It is a reading aid, as in the desktop: where several
modes have similar energy, the apparent curve jumps from one mode to another.

### Wavelength and depth

Each point (f, v) of the curve has wavelength λ = v / f. As a rule of thumb, a Rayleigh wave
of wavelength λ is mostly sensitive to the ground down to a depth of the order of λ/2 – λ/3.
The initial V~s~ estimate and the layer proposal (below) are based on this.

## Automatic picking on the ridges

**Automatic** picking looks for the ridges of the map:

1. for each column, the local maxima of the smoothed column with enough amplitude and
   prominence; nearly flat columns and peaks with wavelengths beyond the reach of the line are
   discarded;
2. peaks of neighbouring columns with a small velocity jump form ridges; only long (at least
   4 Hz) and strong ridges are kept;
3. each ridge goes to the nearest mode of the synthetic model, if there is one, otherwise to
   the modes in order of velocity;
4. the ridges are sampled at a regular frequency step and, where the map allows, extended to
   low frequencies.

It is a proposal: where the fundamental does not form a ridge the picking does not reach it.

## The forward problem

Given a model of plane-parallel layers, each with thickness h, V~s~, V~p~ and density ρ,
over a half-space, the dispersion curves of the Rayleigh modes are computed with the
**propagator matrix** method of Thomson (1950) and Haskell (1953), in the stable formulation
of Dunkin (1965). The code is the port of the Geopsy calculation (Wathelet, 2005, open source
under the LGPL licence), the same engine as Easy-MASW desktop, and matches the desktop library
to machine precision.

V~p~ is obtained from V~s~ and the layer's Poisson's ratio ν:

V~p~ = V~s~ · √[ 2(1 − ν) / (1 − 2ν) ]

## Inversion

The inversion looks for the model whose theoretical curves best reproduce the picking. The
unknowns are the thicknesses and V~s~ of the unlocked layers, each within its Min and Max
bounds; ν and ρ stay as assigned. The search uses the **Nelder–Mead simplex** (1965) with
constraints and restarts, starting from the initial model and from random points: two runs
give slightly different solutions.

The objective function (**misfit**) compares, point by point and mode by mode, the observed
velocity v~obs~ with the computed one v~calc~:

misfit = (1 + n~D~ − n~R~) · √[ Σ ((v~obs~ − v~calc~) / v~obs~)² / n~R~ ]

with n~D~ observed points and n~R~ points for which the model has the corresponding mode: a
model that "loses" a mode is penalised. The **percentage error** is:

error % = mean[(v~obs~ − v~calc~)²] / mean[v~obs~²] · 100

### Initial estimate and layer proposal

- **Initial estimate from picking**: each point gives three depths, v~min~/(2f), v/(2f) and
  v~max~/(2f), where v~min~ and v~max~ are the ends of its uncertainty bar. The initial V~s~
  of a layer is the mean of the velocities whose depths fall in the layer; Min and Max are
  half and double.
- **Propose layers**: first layer h~1~ ≈ λ~min~/2 (at least 0.5 m), depth of the half-space
  z ≈ λ~max~/3 limited between 5 and 40 m, thicknesses in geometric progression
  h~1~·r<sup>k</sup> up to z, rounded to half a metre, with a ±50 % margin; then the initial
  estimate.

## V~s,eq~ and subsoil category

According to the Italian NTC 2018 (§3.2.2):

V~s,eq~ = H / Σ~i~ (h~i~ / V~s,i~)

with h~i~ and V~s,i~ thickness and velocity of the layers between the foundation and the
depth H of the **bedrock**, the first layer with V~s~ ≥ 800 m/s. If the bedrock is deeper
than 30 m, H = 30 m. NTC 2008 uses V~s,30~, the harmonic mean over the 30 m below the
foundation.

## Elastic parameters and correlations

From the density ρ and the velocities:

| Quantity | Formula |
|---|---|
| Poisson's ratio | ν = (q/2 − 1) / (q − 1), with q = (V~p~/V~s~)² |
| Shear modulus | G~0~ = ρ·V~s~² |
| Oedometric modulus | E~d~ = ρ·V~p~² |
| Bulk modulus | M~0~ = E~d~ − 4/3·G~0~ = ρ·(V~p~² − 4/3·V~s~²) |
| Young's modulus | E = 2·ρ·V~s~²·(1 + ν) |

The empirical correlations, inverted to obtain the parameter from V~s~:

- **Ohta and Goto** (1978): V~s~ = 54.33 · N<sup>0.173</sup> · α · β · (z / 0.303)<sup>0.193</sup>,
  with z the mid-depth of the layer, α the age factor (1 for Holocene deposits, 1.303 for
  Pleistocene) and β the composition factor (1 silts and clays, 1.09 sands, 1.19 sands and
  gravels);
- **Jamiolkowski** (1985): V~s~ = α · q~c~<sup>β</sup>, with α and β depending on the soil
  type.

## Transfer function

The amplification of vertically incident SH waves through the layers of the solution, with
the half-space as bedrock and 1 % damping, is computed with 1D propagation in a layered
medium. For a homogeneous layer of thickness H on rigid bedrock the first resonance is at
f~0~ = V~s~ / 4H.

## References

- Park C.B., Miller R.D., Xia J. (1999). *Multichannel analysis of surface waves*.
  Geophysics, 64(3), 800–808.
- Thomson W.T. (1950). *Transmission of elastic waves through a stratified solid medium*.
  Journal of Applied Physics, 21, 89–93.
- Haskell N.A. (1953). *The dispersion of surface waves on multilayered media*. Bulletin of
  the Seismological Society of America, 43, 17–34.
- Dunkin J.W. (1965). *Computation of modal solutions in layered, elastic media at high
  frequencies*. Bulletin of the Seismological Society of America, 55, 335–358.
- Wathelet M. (2005). *Array recordings of ambient vibrations: surface-wave inversion*. PhD
  thesis, Université de Liège.
- Nelder J.A., Mead R. (1965). *A simplex method for function minimization*. The Computer
  Journal, 7, 308–313.
- Ohta Y., Goto N. (1978). *Empirical shear wave velocity equations in terms of
  characteristic soil indexes*. Earthquake Engineering and Structural Dynamics, 6, 167–187.
- Jamiolkowski M. et al. (1985). *New developments in field and laboratory testing of
  soils*. Proc. XI ICSMFE, San Francisco.
- Ministero delle Infrastrutture e dei Trasporti (2018). *Aggiornamento delle Norme tecniche
  per le costruzioni* (NTC 2018), §3.2.2.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20MASW%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/masw/docs/en/teoria.md).*
