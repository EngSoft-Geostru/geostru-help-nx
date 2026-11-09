# Earth pressure and seismic action

The formulas on this page describe the model of MDC NX; where the app departs from the desktop program, [Validation and
limits](validazione.md) says so.

## The calculation phases

For each combination the calculation proceeds in phases, as in the desktop program:

1. **Phase I — stem.** The pressures of soil and surcharges are computed on the inner face of the stem, divided into strips at changes of
   layer, water table and geometry. With Coulomb the thrust is inclined by the wall friction angle δ; with Rankine δ = 0. These pressures
   give the internal forces of the stem.
2. **Phase II — virtual back.** For the global checks the thrust surface is the **vertical through the end of the heel**: the soil above
   the heel is part of the wall system and weighs as a stabilising force. On the virtual back the thrust is inclined by the angle of
   shearing resistance of the soil. With weights, thrusts, loads and passive resistance the stabilising and overturning moments are
   computed about the downhill edge of the base, then sliding, overturning and bearing capacity.
3. **Phase III — foundation.** Toe, heel and shear key, loaded by the foundation pressures and by the weights above, give the internal
   forces of the foundation.
4. **Phase IV — piles.** Only for walls on piles: the actions of phase II go to the pile group (see
   [RC sections, piles and anchors](teoria-strutture.md)).

## Active pressure: Coulomb (Müller-Breslau)

With α the angle of the back face to the horizontal (90° for a vertical face), φ′ the angle of shearing resistance, δ the wall friction
angle and ε the slope of the backfill:

$$K_a=\frac{\sin^2(\alpha+\varphi')}{\sin^2\alpha\,\sin(\alpha-\delta)\left[1+\sqrt{\dfrac{\sin(\varphi'+\delta)\,\sin(\varphi'-\varepsilon)}{\sin(\alpha-\delta)\,\sin(\alpha+\varepsilon)}}\right]^2}$$

With a vertical face, horizontal backfill and δ = 0 this gives $K_a=\dfrac{1-\sin\varphi'}{1+\sin\varphi'}=\tan^2(45°-\varphi'/2)$.

**Rankine** in the program is the same formula with δ = 0: the thrust is normal to the face even with a sloping backfill. If ε exceeds φ′
the radicand is negative: the backfill is steeper than the friction angle and the formula has no solution, so check profile and parameters.

The backfill profile in segments is reduced to an **equivalent slope** ε, derived from the failure wedge on the real profile.

## At-rest pressure

$$K_0=1-\sin\varphi' \quad\text{(Jaky)}$$

with the correction for a sloping backfill of the desktop program, $K_0=(1-\sin\varphi')/(1-\sin\varepsilon)$.

## Pressures

Along the stem, at depth z:

| Term | Pressure |
|---|---|
| Soil | $\sigma(z)=\sum_k K_k\,\gamma'_k\,\Delta z_k$: each overlying layer contributes with its own K and its own weight, submerged below the water table |
| Surcharge q | $K\,q$, constant with depth |
| Cohesion c′ | $-2\,c'\sqrt{K}$; zones in tension do not push |
| Water | $\gamma_w\,(z-z_w)$ below the water level, normal to the face |

The horizontal and vertical components of the thrust follow from the inclination δ (phase I) or φ′ (phase II).

## Passive resistance

In front of the foundation, on the downhill face of the toe (and of the key, if any), the soil offers passive resistance:

$$K_p=\frac{\sin^2(\alpha-\varphi')}{\sin^2\alpha\,\sin(\alpha+\delta)\left[1-\sqrt{\dfrac{\sin(\varphi'+\delta)\,\sin(\varphi'+\varepsilon)}{\sin(\alpha+\delta)\,\sin(\alpha+\varepsilon)}}\right]^2}$$

which for a vertical face, horizontal ground and δ = 0 equals $(1+\sin\varphi')/(1-\sin\varphi')$. The percentage chosen in the
[Code and seismic action](sisma.md) step is used; the fill above the toe does not push.

## Seismic action: Mononobe-Okabe

With the seismic coefficients k~h~ and k~v~ (see [Seismic action](sisma.md)) the seismic angle is

$$\theta=\arctan\frac{k_h}{1-k_v}$$

and the seismic active pressure coefficient

$$K_{AE}=\frac{\sin^2(\alpha+\varphi'-\theta)}{\cos\theta\,\sin^2\alpha\,\sin(\alpha-\theta-\delta)\left[1+\sqrt{\dfrac{\sin(\varphi'+\delta)\,\sin(\varphi'-\varepsilon-\theta)}{\sin(\alpha-\theta-\delta)\,\sin(\alpha+\varepsilon)}}\right]^2}$$

The total thrust is $E_d=\tfrac12(1+k_v)\,K_{AE}\,\gamma\,H^2$; the **seismic increment** over the static value,
$\Delta K=(1+k_v)K_{AE}-K_a$, is distributed on the stem with its resultant at 2/3, 1/3 or 1/2 of the height according to the chosen
option. The same increment applies to surcharges. Below the water table the angle θ accounts for the submerged weight of the soil.

With at-rest pressure the increment is $\Delta K=k_h$.

Under seismic conditions the passive resistance is also reduced: K~PE~ of Mononobe-Okabe with δ = 0, multiplied by (1 − k~v~).

## Inertia forces

All masses that move with the wall receive a horizontal force k~h~·W and a vertical force k~v~·W acting upwards (the unfavourable direction), applied at their centroid: stem,
foundation, shear key, soil above the heel up to the virtual back, surcharges above the heel. The internal forces of the stem include the
inertia of the stem itself.

## References

- Coulomb C.A. (1776), *Essai sur une application des règles de maximis et minimis à quelques problèmes de statique*.
- Müller-Breslau H. (1906), *Erddruck auf Stützmauern*, Kröner, Stuttgart.
- Rankine W.J.M. (1857), *On the stability of loose earth*, Phil. Trans. Royal Society.
- Jaky J. (1944), *The coefficient of earth pressure at rest*, Journal of the Society of Hungarian Architects and Engineers.
- Okabe S. (1926), *General theory of earth pressure*, Journal of the Japan Society of Civil Engineers.
- Mononobe N., Matsuo H. (1929), *On the determination of earth pressures during earthquakes*, World Engineering Congress, Tokyo.
- D.M. 17/01/2018, *Aggiornamento delle Norme tecniche per le costruzioni* (Italian Building Code), §6.5 and §7.11.6.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20MDC%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mdc/docs/en/teoria-spinte.md).*
