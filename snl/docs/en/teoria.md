# Theory

This page summarises the theory behind SNL NX: the US guidelines **FHWA-NHI-14-007** for soil nail walls and, for internal stability, the wedge method of **Sheahan & Ho (2003)**. The assumptions and limits of the method are listed in [Validation and limits](validazione.md).

## Soil nailing

Soil nailing supports slopes and excavation faces by inserting reinforcing elements, the **nails**, into the ground: usually steel bars in grouted drillholes. Nails are **passive**: they are not prestressed and work in tension when the soil deforms, transferring the load to the ground by friction and bond along the interface.

In an excavation the wall is built **from the top down**:

1. a lift as high as the vertical nail spacing is excavated;
2. the ground is drilled, slightly downwards;
3. the bar is inserted and the hole grouted;
4. drainage and the first facing layer (shotcrete with mesh) are placed and connected to the nail heads;
5. the steps are repeated down to the final level, then the facing is completed.

So three elements have to be designed: the **soil**, the **nails** and the **facing**.

## Failure modes

| Mode | What happens | In SNL NX |
|---|---|---|
| Internal stability | a soil wedge slides on a surface that crosses the nails | planar wedge check, for each excavation stage |
| Global stability | the surface passes behind or below the nails | **not computed**: use a slope stability program, such as GeoStru Slope |
| Pull-out | the nail is pulled out of the ground beyond the failure surface | check for each nail and each stage |
| Tensile failure | the bar breaks | check for each nail and each stage |
| Facing | the shotcrete fails between the nails | pressure, shear and moment diagrams; the section check is separate |
| Sliding | the nailed block slides on its base | horizontal equilibrium of the block of width Bl |

## Excavation stages

Stages are not entered: SNL NX creates one per nail, in order of depth. In stage *i* the nails down to the *i*-th are installed and the excavation has reached halfway between nail *i* and the next one; the last stage reaches the toe of the wall, at depth H.

In each stage the failure surface starts at the bottom of the excavation reached, and internal stability, pull-out and nail failure are checked with the installed nails only.

## Active earth pressure

The effective horizontal active stress at depth *z* depends on the active earth pressure coefficient Ka, the effective vertical stress σ'v, the cohesion c' and the surcharges:

$$
\sigma'_a(z) = K_a\,\sigma'_v(z) - 2\,c'\sqrt{K_a} \;\ge 0
$$

Ka is computed layer by layer with the **Rankine** or the **Coulomb** theory; the latter accounts for the wall-soil friction δ, the facing inclination θ and the backslope inclination ε. For ε = 0 and a vertical facing, Rankine gives the classic value:

$$
K_a = \tan^2\!\left(45^\circ - \frac{\varphi'}{2}\right)
$$

Surcharges add a horizontal stress: the uniform load in proportion to Ka, the strip and the line load with the elastic half-space solutions for a rigid wall.

## Nail force

Each nail carries the thrust of its **zone of influence**: the band of wall from halfway between the nail and the one above (or the top) to halfway between the nail and the one below (or the toe). The height of the band is the vertical spacing Sv of the nail, its width the horizontal spacing Sh. The nail force is the resultant of the total pressure on the zone, taken along the nail:

$$
F_i = \frac{k_n\,S_h}{\cos\alpha_i}\int_{z_a}^{z_b} \sigma_h(z)\,dz
$$

where σh is the sum of the effective active stress, the water pressure and, under seismic action, the seismic increment; kn (typically 0.85) accounts for the nail not carrying the whole thrust. In layered soil the pressure jumps and changes slope at the interfaces: that is why it is integrated over the zone instead of taking the value at mid-height.

## Internal stability check

For each stage the soil wedge bounded by the facing, the backslope and a plane starting at the bottom of the excavation with inclination β on the horizontal is considered. β is assigned or equals 45° + φ̄'/2. Force equilibrium of the wedge (Sheahan & Ho, 2003) gives the safety factor:

$$
FS = \frac{\bar c'\,L_s + \left[(W(1+k_v)+Q)\cos\beta - k_h W\sin\beta - U\right]\tan\bar\varphi' + S}{\left[(W(1+k_v)+Q)\sin\beta + k_h W\cos\beta\right]\gamma_R}
$$

with

$$
S = \frac{1}{S_h}\sum_i R_i\left[\cos(\beta+\alpha_i) + \sin(\beta+\alpha_i)\tan\bar\varphi'\right], \qquad R_i = \min(R_{T,i},\,R_{PO,i})
$$

- W wedge weight, Q resultant of the loads on the wedge, U water thrust on the surface;
- Ls length of the failure surface;
- c̄' and φ̄' thickness-weighted means over the layers excavated in the stage;
- Ri resistance of nail *i* crossed by the surface: the minimum of tensile failure and pull-out (FHWA);
- γR the R factor of the internal checks.

The check is satisfied if FS ≥ 1.

## Pull-out

A nail pulls out when the force exceeds the resistance of the part beyond the failure surface, of length **Le** (effective length):

$$
R_{PO} = \frac{\pi\,D\,L_e\,\tau_{lim}}{\xi}, \qquad FS_{PO} = \frac{R_{PO}}{F\,\gamma_{R,PO}}
$$

D is the drillhole diameter, ξ the correlation factor, τlim the limit shear resistance at the interface. τlim grows with the vertical stress at the middle of the effective length, with the interaction coefficient K and with the friction of the layer where the bond length lies, and includes an adhesion related to cohesion. The effective length changes from one stage to the next, because the failure surface moves down with the excavation.

## Tensile failure

$$
R_T = \frac{\pi\,d_c^2}{4}\,f_y, \qquad FS_T = \frac{R_T}{F\,\gamma_{R,T}}
$$

dc is the bar diameter, fy the steel strength.

## Sliding

Sliding is a special case of global stability: the nailed block, of width **Bl**, slides on the foundation soil. Horizontal equilibrium is imposed, not rotational equilibrium:

$$
FS = \frac{R_s}{\gamma_R\left[P_{a,h} + Q_h + \Delta P_{aE} + \Delta Q_{hE} + U_1\right]}
$$

$$
R_s = c'_f\,B_l + \left(W + P_{a,v} + Q - U_2\right)\tan\varphi'_f
$$

- Pa soil thrust on the inner side of the block, of height H1, with horizontal and vertical components;
- Qh horizontal thrust of the surcharges;
- ΔPaE and ΔQhE seismic increments;
- U1 water thrust on the inner side, U2 uplift at the base;
- c'f and φ'f parameters of the foundation soil.

Bl is chosen in the Analysis step: equal to H, assigned, or automatic from the projection of the first nail. The check is satisfied if FS > 1.

## Facing

The facing is modelled as a beam along the wall loaded by the total earth pressure and supported by the nails, whose reactions are the nail forces. SNL NX plots pressure, shear and moment per metre of wall. The diagrams are indicative: the structural check of the reinforced concrete section and of the nail head is done separately.

## Seismic action

The seismic action is **pseudo-static**, with the project coefficients kh and kv. Under seismic action the thrust is computed with the **Mononobe-Okabe KaE** coefficient, and the increment over the static thrust enters the nail forces and sliding with its own factor A. In the internal check the wedge weight is multiplied by (1 + kv) and the horizontal force kh·W is added.

From the site parameters the app proposes

$$
k_h = \beta_m\,\frac{a_{max}}{g}, \qquad k_v = \pm 0.5\,k_h
$$

with amax = SS·ST·ag at the SLV and βm = 0.38 unless you change it. The proposal is a help: the choice of kh and kv remains the designer's.

## Partial factors

The codes associate a different approach with each check. For NTC 2018 the reference is:

| Check | NTC 2018 | Reference |
|---|---|---|
| Sliding | A1 + M1 + R3 | §6.5.3.1.1 |
| Pull-out (the nail as an anchor) | A1 + M1 + R3 | §6.6.2 |
| Internal stability (as an excavation face) | A2 + M2 + R2 | §6.8.2 |
| Nail failure | A1 + M1 + R1 or A2 + M2 + R1 | §6.5.3.1.2 |

Under seismic conditions the reference is §7.11. For Eurocode 7 the design approaches DA1 (combinations 1 and 2), DA2 and DA3 of EN 1997-1 apply.

SNL NX uses **one combination** per project: the same A and M factors for all checks and one R factor for each (failure, pull-out, sliding, internal checks). Choosing the code loads:

| Code | A, M | R failure | R internal | R sliding | R pull-out | ξ |
|---|---|---|---|---|---|---|
| NTC 2018, permanent structure | 1 | 1 | 1.1 | 1.1 | 1.2 | 1 |
| NTC 2018, temporary structure | 1 | 1 | 1.1 | 1.1 | 1.1 | 1 |
| Eurocode 7 | 1 | 1 | 1 | 1 | 1 | 1 |
| User | free | | | | | |

The factors can be changed by hand in the Analysis step, and the factor A of each load is typed in the Loads step. To apply different approaches to different checks literally, calculate the project more than once, one per combination.

## Bibliography

- Lazarte C.A., Robinson H., Gómez J.E., Baxter A., Cadden A., Berg R. (2015). *Geotechnical Engineering Circular No. 7 — Soil Nail Walls Reference Manual*, FHWA-NHI-14-007. Federal Highway Administration.
- Sheahan T.C., Ho C.L. (2003). *Simplified trial wedge method for soil nailed wall analysis*. Journal of Geotechnical and Geoenvironmental Engineering, 129(2), 117-124.
- Rankine W.J.M. (1857). *On the stability of loose earth*. Philosophical Transactions of the Royal Society of London, 147.
- Coulomb C.A. (1776). *Essai sur une application des règles de maximis et minimis à quelques problèmes de statique relatifs à l'architecture*.
- Okabe S. (1926). *General theory of earth pressure*. Journal of the Japanese Society of Civil Engineers, 12(1).
- Mononobe N., Matsuo H. (1929). *On the determination of earth pressures during earthquakes*. Proc. World Engineering Congress, Tokyo.
- Terzaghi K. (1943). *Theoretical Soil Mechanics*. Wiley.
- Poulos H.G., Davis E.H. (1974). *Elastic Solutions for Soil and Rock Mechanics*. Wiley.
- D.M. 17/01/2018, *Aggiornamento delle Norme tecniche per le costruzioni* (Italian building code); Circolare n. 7 of 21/01/2019.
- EN 1997-1:2004, *Eurocode 7 — Geotechnical design — Part 1: General rules*.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/snl/docs/en/teoria.md).*
