# Modified RMR (Sen)

**Sen and Sadagah (2003)** modify the determination of the RMR proposed by Bieniawski **without modifying its classification**. Instead of reading the scores $A1$, $A2$, $A3$ from the stepped tables, they propose computing the RMR with a **simplified continuous equation** starting from the parameters of RQD, rock strength $S_u$ (MPa) and spacing $s$ (m) only, expressing the hydraulic conditions as a function of the flow rate $G$.

Bieniawski's coefficients for the **discontinuity condition** (A4) and for the **orientation** (A6) are kept unchanged. The result is a continuous RMR, less subjective than reading by ranges.

## Input parameters

The parameters enter the equation directly, without going through the stepped scores.

- **$S_u$** — uniaxial compressive strength (MPa), from the Point Load Test ($S_u = K\,I_s$), the Schmidt hammer ($S_u = 0{,}775\,R + 21{,}3$) or the ISRM estimate: see [compressive strength](classificazioni.md#resistenza-a-compressione-uniassiale-su).
- **RQD** — Rock Quality Designation, from borehole cores or, when these are unavailable, from the mean number of joints: see [RQD](classificazioni.md#rqd-rock-quality-designation).
- **$s$** — mean discontinuity spacing (m).
- **$G$** — flow rate expressing the hydraulic conditions.

The coefficients $A4$, $A5$ and $A6$ remain those of Bieniawski. The relevant tables are already reported on the Bieniawski page:

- [A4 — discontinuity conditions](rmr-romana.md#a4-condizioni-delle-discontinuita) (sub-parameters $v_1$–$v_5$);
- [A5 — hydraulic conditions](rmr-romana.md#a5-condizioni-idrauliche);
- [A6 — discontinuity orientation](rmr-romana.md#a6-orientamento-delle-discontinuita).

## Computing the corrected RMR

The corrected RMR is obtained directly from the continuous equation:

$$ RMR_c = 0{,}2\,RQD + 15\log(s) + 0{,}075\,S_u - 2{,}9\log(G) + 34 + (A_5 + A_6) $$

where $s$ is the spacing (m), $S_u$ the strength in MPa and $G$ the flow rate expressing the hydraulic conditions.

If a borehole from which to derive RQD is missing, the **mean number of joints** $n$ is introduced and the equation becomes:

$$ RMR_c = 20\,(1 + 0{,}1n)\,e^{-0{,}1n} - 15\log(n) + 0{,}075\,S_u - 2{,}9\log(G) + 34 + (A_5 + A_6) $$

## Rock mass classes

From the value of $RMR_c$, 5 classes are identified, the same as Bieniawski's:

| $RMR_c$ | 100–81 | 80–61 | 60–41 | 40–21 | ≤ 20 |
|---|---|---|---|---|---|
| Class | I | II | III | IV | V |
| Description | Very good | Good | Fair | Poor | Very poor |

## Characteristic parameters

From $RMR_c$ the cohesion and friction angle of the rock mass are derived (Sen et al.):

$$ c\ [\text{kPa}] = 3{,}625 \cdot RMR_c $$

$$ \varphi\ [°] = 25\,(1 + 0{,}01\,RMR_c)\ \text{ for } RMR_c > 20; \qquad \varphi = 1{,}5\,RMR_c\ \text{ for } RMR_c < 20 $$

For the relationships between the different classifications and the bibliographic references, see the [bibliography](bibliografia.md).

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Rock%20Mechanics%20NX).*
