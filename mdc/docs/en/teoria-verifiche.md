# Global checks

The global checks concern the wall as a rigid body and use the actions of phase II (thrust on the virtual back, weights of wall and soil
above the heel, loads, passive resistance), for every combination, with the soil parameters reduced by the M factors and the resistances
divided by the R factors. For walls on piles the checks of the pile rows replace them.

## Sliding

The sliding plane is the base of the foundation or, with a shear key, the line from the downhill edge to the bottom of the key. With the
forces projected on that plane (inclined by α~b~):

$$T=F_x\cos\alpha_b+F_y\sin\alpha_b \qquad N=-F_x\sin\alpha_b+F_y\cos\alpha_b$$

$$F_{s,T}=\frac{\dfrac{N\tan\delta_b+c_a\,B}{\gamma_{R,sl}}+\dfrac{S_p}{\gamma_{R,t}}}{T}$$

with δ~b~ the base friction angle and c~a~ the adhesion (those of the founding layer, or the values written in the
[Code and seismic action](sisma.md) step, reduced with γ~φ~ and γ~c~), B the width of the base, S~p~ the mobilised passive resistance at
the toe (with the chosen participation percentage), γ~R,sl~ and γ~R,t~ the factors for sliding and for the resistance of the soil at the toe
(NTC 2018 Table 6.5.I: 1.1 and 1.4 in combination A1+M1+R3, 1.0 and 1.2 in the seismic one). This is the form the engine uses and the
report prints; the desktop program did not divide the passive resistance by γ~R,t~.

## Overturning

About the downhill edge of the base:

$$F_{s,R}=\frac{M_{stab}}{\gamma_{R,ov}\;M_{ov}}$$

M~stab~ collects the moments of the weights (wall, soil above the heel, stabilising surcharges), of the vertical component of the thrust and
of the passive resistance; M~ov~ those of the horizontal component of the thrust, of water, of seismic forces and of overturning loads. With
NTC 2018 the seismic overturning check uses β~m~ increased by 50 % (see [Seismic action](sisma.md)).

## Eccentricity and foundation pressures

With N the vertical resultant and M the moment about the centre of the base, the eccentricity is e = M/N. With B the width of the base:

| Case | Pressures |
|---|---|
| $\lvert e\rvert\le B/6$ (resultant within the kern) | trapezoidal: $\sigma_{max,min}=\dfrac{N}{B}\left(1\pm\dfrac{6e}{B}\right)$ |
| $\lvert e\rvert>B/6$ | partialised triangle: $\sigma_{max}=\dfrac{2N}{3u}$, with u the distance of the resultant from the compressed edge, over a length 3u |

A resultant outside the base (u ≤ 0) makes the wall fail. With lean concrete the pressures are also reported at the base of the lean
concrete.

## Bearing capacity

### Vesic

On the effective width $B'=B-2e$ (Meyerhof), with D the embedment of the founding plane, γ~1~ the unit weight of the soil above the
founding plane and γ that below:

$$q_{lim}=c'N_c\,s_c d_c i_c g_c+\gamma_1 D\,N_q\,s_q d_q i_q g_q+\tfrac12\gamma B' N_\gamma\,s_\gamma d_\gamma i_\gamma g_\gamma \qquad Q_{lim}=q_{lim}\,B'$$

$$N_q=e^{\pi\tan\varphi'}\tan^2\!\left(45°+\frac{\varphi'}{2}\right)\qquad N_c=(N_q-1)\cot\varphi'\qquad N_\gamma=2(N_q+1)\tan\varphi'$$

| Factors | Expression |
|---|---|
| Shape (wall of length L) | $s_q=1+\frac{B'}{L}\tan\varphi'$, $s_\gamma=1-0.4\frac{B'}{L}$, $s_c=1+\frac{B'}{L}\frac{N_q}{N_c}$; long wall: 1 |
| Depth | $K=D/B'$ (or $\arctan(D/B')$ if D > B′); $d_c=1+0.4K$, $d_q=1+2\tan\varphi'(1-\sin\varphi')^2K$, $d_\gamma=1$ |
| Load inclination | $i_q=\left(1-\dfrac{H}{N+B'c'\cot\varphi'}\right)^m$, $i_\gamma=\left(1-\dfrac{H}{N+B'c'\cot\varphi'}\right)^{m+1}$, $i_c=i_q-\dfrac{1-i_q}{N_c\tan\varphi'}$, m = 2 for the wall |
| Ground slope at the toe (β) | $g_c=1-\beta/147°$, $g_q=g_\gamma=(1-\tan\beta)^2$ |

With φ′ = 0 (undrained conditions, c′ = c~u~): N~c~ = 2 + π, N~q~ = 1, N~γ~ = 0. The shape, depth and inclination factors can be excluded
in the [Code and seismic action](sisma.md) step. With the water table at the founding plane the third term uses the submerged unit weight.

### Brinch Hansen

Same structure, with $N_\gamma=1.5(N_q-1)\tan\varphi'$, $s_q=1+\frac{B'}{L}\sin\varphi'$, inclination factors
$i_q=\left(1-\dfrac{0.5H}{N+B'c'\cot\varphi'}\right)^5$, $i_\gamma=\left(1-\dfrac{0.7H}{N+B'c'\cot\varphi'}\right)^5$ and ground-slope factors
$g_q=g_\gamma=(1-0.5\tan\beta)^5$.

### Safety factor

$$F_{s,Q}=\frac{Q_{lim}}{\gamma_{R,q}\,N}$$

with γ~R,q~ = 1.4 in the A1+M1+R3 combination and 1.2 in the NTC 2018 seismic one.

## References

- Vesic A.S. (1975), *Bearing capacity of shallow foundations*, in Winterkorn & Fang, *Foundation Engineering Handbook*, Van Nostrand Reinhold.
- Brinch Hansen J. (1970), *A revised and extended formula for bearing capacity*, Danish Geotechnical Institute, Bulletin 28.
- Meyerhof G.G. (1953), *The bearing capacity of foundations under eccentric and inclined loads*, Proc. 3rd ICSMFE, Zurich.
- Bowles J.E. (1996), *Foundation Analysis and Design*, 5th ed., McGraw-Hill.
- D.M. 17/01/2018, §6.4.2, §6.5.3.1.1, Tables 6.2.I, 6.2.II, 6.5.I; §7.11.6.2.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20MDC%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mdc/docs/en/teoria-verifiche.md).*
