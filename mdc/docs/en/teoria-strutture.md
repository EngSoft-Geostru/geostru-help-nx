# RC sections, piles and anchors

## Reinforced-concrete sections

Sections are rectangular, one metre wide, with two layers of reinforcement at the cover distance from the faces. They are checked by the
GeoStru RC section solver, the same as in MP NX.

### ULS bending with axial force

Concrete with the parabola-rectangle law ($\varepsilon_{c2}=0.2\,\%$, $\varepsilon_{cu}=0.35\,\%$, $f_{cd}=\alpha_{cc}f_{ck}/\gamma_c$),
bilinear steel. The M-N domain is built over thin strips of the section; the check compares the point (N~Ed~, M~Ed~) with the domain and
returns the demand/capacity ratio.

With NTC 2018 the resisting moment is the **first-yield** moment: the smaller of the one that brings the steel to yield and the one that
brings the concrete to a compressive strain of 0.2 %. It is lower than the ultimate moment (about 10 % with small axial force) and
corresponds to the essentially elastic check that the code requires of foundations in the seismic combination; the desktop program applies
it to all sections and all combinations, and MDC NX does the same.

### Shear

Members without shear reinforcement, NTC 2018 eq. (4.1.23):

$$V_{Rd}=\max\left\{\left[\frac{0.18\,k\,(100\rho_l f_{ck})^{1/3}}{\gamma_c}+0.15\,\sigma_{cp}\right]b_w d\;;\;\left(v_{min}+0.15\,\sigma_{cp}\right)b_w d\right\}$$

with $k=1+\sqrt{200/d}\le 2$ (d in mm), $\rho_l=A_{sl}/(b_w d)\le 0.02$, $\sigma_{cp}=N_{Ed}/A_c\le 0.2f_{cd}$,
$v_{min}=0.035\,k^{3/2}f_{ck}^{1/2}$.

### Serviceability

Stresses on the cracked section (n = 15) and crack width (2019 Circular, C4.1.2.2.4):

$$w_k=s_{r,max}\,(\varepsilon_{sm}-\varepsilon_{cm})\qquad
\varepsilon_{sm}-\varepsilon_{cm}=\frac{\sigma_s-k_t\dfrac{f_{ctm}}{\rho_{eff}}(1+\alpha_e\rho_{eff})}{E_s}\ge 0.6\frac{\sigma_s}{E_s}$$

$$s_{r,max}=k_3c+k_1k_2k_4\frac{\phi}{\rho_{eff}}$$

with k~t~ = 0.6 for short-term loading and 0.4 for long-term loading, k~2~ = 0.5 for bending, ρ~eff~ referred to the effective area of
concrete in tension.

## Piles

### Actions at the head

The horizontal force H, vertical force V and moment M of phase II, for the share of load given to the piles, are transferred to the
**centroid of the pile heads**. With the resultant moment the equilibrium of all actions is used; with the overturning moment (prudent
choice) only the overturning contributions.

### Distribution: rigid cap

The cap is a rigid body with three displacements (u, w, θ). Each pile reacts with an **axial stiffness** k~a~ and a **transverse** one
k~t~; the equilibrium $\mathbf{K}\,\mathbf{d}=(H,V,M)$ gives the displacements and hence N, T (and M with a fixed head) of every row. With
vertical piles and negligible transverse stiffness the classic distribution is recovered:

$$N_i=\frac{V}{n}+\frac{M\,s_i}{\sum s_j^2}\qquad T_i=\frac{H}{n}$$

- **Axial stiffness** (Randolph and Wroth): elastic settlement of the pile in the soil with the mean modulus of the layers along the
  shaft, plus the shortening of the pile.
- **Transverse stiffness** (Hetényi, long pile): with the characteristic length $L_b=\sqrt[4]{4E_pI_p/(k\,D)}$, free head
  $k_t=2E_pI_p/L_b^3$.
- **Fixed head**: Hetényi's matrix adds the fixing moment, which enters the check of the pile.

### Vertical bearing capacity

$$Q_{lim}=Q_p+Q_s\qquad Q_p=\frac{\pi D^2}{4}\left(\sigma'_{v,p}N_q+c\,N_c\right)\qquad Q_s=\pi D\sum_i\left(K\tan\delta\;\sigma'_{v,i}+\alpha\,c_i\right)\Delta l_i$$

N~q~ of Berezantzev as a function of φ′ at the toe and of the ratio L/D, $N_c=\max\{(N_q-1)\cot\varphi';9\}$. The coefficients K·tanδ and
the adhesion α depend on the pile type (bored or driven) and on the cohesion. For raked piles the true depth of the toe and the shaft length
in each layer are used. The design resistance is

$$R_d=\frac{Q_p}{\xi\,\gamma_b}+\frac{Q_s}{\xi\,\gamma_s}$$

with ξ = max(ξ~3~, ξ~4~) from the number of investigated verticals (NTC 2018 Table 6.4.IV) and γ~b~, γ~s~ from Table 6.4.II. A pile in
tension counts only the shaft resistance, reduced to 70 %. The group efficiency (Converse-Labarre), if chosen, multiplies the resistance:

$$E_g=1-\frac{\theta_L+\theta_F\,(m-1)/m}{90°}\qquad \theta=\arctan\frac{D}{i}$$

with i the spacings in the row and between rows, m the number of rows, E~g~ between 0.3 and 1.

### Lateral loading

Long pile on an elastic subgrade. With a constant subgrade modulus (Hetényi), head displacement, rotation and moments along the shaft come
from the closed-form solutions with L~b~; with a modulus increasing with depth (Matlock and Reese) from the relative stiffness length
$T=\sqrt[5]{E_pI_p/n_h}$ and the non-dimensional coefficients A~y~, B~y~, A~m~, B~m~. The soil pressure is compared with the limit lateral
pressure.

### Seismic action

The inertial actions of the wall reach the piles already in H, V and M of the seismic combination, without reducing their resistance. With
subsoil D or E, NTC 2018 also asks to consider the moments from kinematic interaction: the app reminds you of it.

## Anchors

The anchor acts on the stem with the design force per metre of wall $T/i$ (i spacing), inclined by the anchor angle α. The resistance of
the anchorage is the smallest of three:

| Resistance | Depends on |
|---|---|
| Grout body in the soil | diameter and length of the bond, effective stress at the depth of its centroid, φ′ and c′ of the layer, divided by γ~R~·ξ~a~ (NTC 2018 Tables 6.6.I and 6.6.III) |
| Grout-strand bond | $\pi\,n\,d_{tr}\,L_a\,\tau_{ad}$ |
| Steel | area of the strands times the design strength, net of prestress losses |

## References

- Hetényi M. (1946), *Beams on Elastic Foundation*, University of Michigan Press.
- Matlock H., Reese L.C. (1960), *Generalized solutions for laterally loaded piles*, J. Soil Mech. Found. Div., ASCE, 86(SM5).
- Randolph M.F., Wroth C.P. (1978), *Analysis of deformation of vertically loaded piles*, J. Geotech. Eng. Div., ASCE, 104(GT12).
- Poulos H.G., Davis E.H. (1980), *Pile Foundation Analysis and Design*, Wiley.
- Berezantzev V.G., Khristoforov V.S., Golubkov V.N. (1961), *Load bearing capacity and deformation of piled foundations*, Proc. 5th ICSMFE, Paris.
- Converse F.J., Labarre W.M., group efficiency formula, in Bowles J.E., *Foundation Analysis and Design*.
- D.M. 17/01/2018 §4.1, §6.4.3, §6.6; Circular 21/01/2019 no. 7, C4.1.2.2.4.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20MDC%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mdc/docs/en/teoria-strutture.md).*
