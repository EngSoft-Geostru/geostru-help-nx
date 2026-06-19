# Geomechanical classifications — overview and common parameters

In geotechnical design in rock — both for the stability of a slope and for an underground work — detailed information on the strength and deformability characteristics of the rock mass is rarely available. The **geomechanical classifications** are empirical methods that, starting from the geostructural survey, return a rock-mass quality index and the characteristic parameters (cohesion, friction angle, deformation modulus) needed for the calculation.

Rock Mechanics NX implements six classifications, all fed by the **same discontinuity survey** (see [Workflow](workflow.md)):

| Classification | Index | Typical field of application | Page |
|---|---|---|---|
| Barton (1974, rev. 2002) | Q | Underground works, general characterisation | [Barton](barton.md) |
| Bieniawski (1976) + Romana (1985) | RMR · SMR | Tunnels, foundations, **slopes** (SMR) | [Bieniawski & Romana](rmr-romana.md) |
| Jašarević & Kovačević (1996) | n → RMR | Carbonate rock masses | [Jašarević](jasarevic.md) |
| Sen & Sadagah (2003) | continuous RMR | Simplified version of RMR | [Sen](sen.md) |
| Robertson (1988) | SRMR | **Slopes only** in weak rock (RMR < 40) | [Robertson](robertson.md) |
| Singh & Göel (1999) | N → RMR · Q | Tunnels | [Singh & Goel](singh-goel.md) |

Many methods share the same input parameters. To avoid repetition, the common definitions and tables are collected here: the pages of the individual methods refer back to them.

---

## Uniaxial compressive strength Su { #resistenza-a-compressione-uniassiale-su }

The `A1` parameter of all the methods derived from RMR is obtained from the **uniaxial compressive strength** $S_u$ of the intact rock. It can be determined in three ways.

### Point Load Test

Portable and field-based, it provides the **point load index** $I_s$, correlated to $S_u$ by:

$$ S_u = K \cdot I_s $$

The ISRM recommends $K = 24$, but in practice the value varies widely. Palmström suggests relating $K$ to $I_s$:

| $I_s$ (MPa) | K |
|---|---|
| < 3.5 | 14 |
| 3.5 – 6.0 | 16 |
| 6.0 – 10 | 20 |
| > 10 | 25 |

### Schmidt hammer test (sclerometer)

A non-destructive test that measures the *rebound hardness* of the rock. From the rebound index $R$, $S_u$ is obtained with the relationship of Irfan and Dearman (1978):

$$ S_u = 0{,}775 \cdot R + 21{,}3 $$

### ISRM standard (quick estimate)

In the preliminary phase, in the absence of tests, $S_u$ is estimated from the response of the rock to a blow from the geologist's hammer:

| Response of the rock | $S_u$ |
|---|---|
| Can be scratched with a fingernail or crumbled by hand | 0.25 – 1 MPa |
| Crumbles under blows of the pick; thin slabs break by hand | 1 – 5 MPa |
| The pick leaves shallow holes; thin slabs break under strong pressure | 5 – 25 MPa |
| The rock fractures with a single blow | 25 – 50 MPa |
| Fractures after two or three blows | 50 – 100 MPa |
| Only chips off | > 200 MPa |

!!! tip "Which method to use"
    If you have Point Load or Schmidt hammer tests, it is preferable to obtain `A1` from the equations of the Bieniawski charts (given on the page of each method) rather than from the step tables: the result is continuous and less subjective.

---

## RQD — Rock Quality Designation { #rqd-rock-quality-designation }

The **Rock Quality Designation** measures the degree of fracturing of the rock mass. From a borehole it is computed as the recovery percentage referred to the core pieces of length $\geq 100$ mm:

$$ RQD = 100 \cdot \frac{L_c}{L_t} $$

where $L_c$ is the sum of the lengths of the core pieces > 100 mm and $L_t$ is the total length of the measured run.

In the **absence of borehole cores**, RQD is obtained from the discontinuity survey with the relationship of Palmström (1982):

$$ RQD = 115 - 3{,}3 \cdot J_v $$

where $J_v$ is the number of joints per cubic metre of rock (volumetric joint count).

Alternatively, from the formula of Priest and Hudson (1981):

$$ RQD = 100 \cdot e^{-0{,}1\,\lambda} \cdot (0{,}1\,\lambda + 1) $$

with $\lambda$ the mean number of joints per linear metre.

!!! note "Minimum value"
    In the Barton and Singh & Goel classifications, if $RQD < 10$ a value of $RQD = 10$ is assumed anyway.

---

## Discontinuity spacing { #spaziatura-delle-discontinuita }

The **mean spacing** $s$ is the mean distance between two adjacent discontinuities of the same set. It determines the `A3` parameter of RMR (with method-specific equations) and enters the tables of Robertson and Jašarević.

---

## Parameters of the Barton classification (Q)

The four parameters that follow ($J_n$, $J_r$, $J_a$, $J_w$) and the SRF factor are common to **Barton**, **Singh & Goel** and, in derived form, to the [Seismic collapse](utility.md) utility. The relevant pages refer back to the tables below.

### Parameter J~n~ (Joint Set Number) { #jn }

It depends on the number of joint sets present in the rock mass.

| Definition | $J_n$ |
|---|---|
| Massive rock, no or rare discontinuities | 0.5 – 1 |
| One set of discontinuities | 2 |
| One set of discontinuities + random ones | 3 |
| Two sets of discontinuities | 4 |
| Two sets of discontinuities + random ones | 6 |
| Three sets of discontinuities | 9 |
| Three sets of discontinuities + random ones | 12 |
| Four or more sets of discontinuities | 15 |
| Completely disintegrated rock | 20 |

!!! note "Tunnels"
    At a portal zone $J_n$ must be doubled; at an intersection zone of two tunnels it must be tripled.

### Parameter J~r~ (Joint Roughness Number) { #jr }

It depends on the roughness of the most unfavourable set.

| Definition | $J_r$ |
|---|---|
| Discontinuous joints | 4 |
| Rough or irregular, undulating joints | 3 |
| Smooth, undulating joints | 2 |
| Slickensided, undulating joints | 1.5 |
| Rough or irregular, planar joints | 1.5 |
| Smooth, planar joints | 1.0 |
| Slickensided, planar joints | 0.5 |
| Mineralised zones with clay minerals filling the discontinuity | 1.0 |
| Mineralised zones with sand, gravel, disintegrated zones | 1.0 |

The description refers to the small- and medium-scale characteristics. If the mean spacing of the main set exceeds 3 m, increase $J_r$ by 1. For planar, slickensided joints with striations oriented in the most unfavourable direction, use 0.5.

### Parameter J~a~ (Joint Alteration Number) { #ja }

It depends on the degree of alteration of the fractures, on the thickness and the nature of the infilling, determined on the most unfavourable set.

**Essentially closed joints** (aperture 1–3 mm) with walls in contact:

| Definition | $J_a$ |
|---|---|
| Sealed or mineralised joints | 0.75 |
| Unaltered joints or with slight oxidation | 1 |
| Slightly altered joints or with coatings of non-plastic material | 2 |
| Joints with silty coatings, limited non-plastic clay fraction | 3 |
| Coatings of low frictional-strength minerals (clays, mica, talc, graphite, chlorite, gypsum) | 4 |

**Moderately open joints** (< 5 mm), infilling that maintains contact between the walls in case of sliding:

| Definition | $J_a$ |
|---|---|
| Sandy infilling | 4 |
| Non-plastic clayey infilling, heavily overconsolidated | 6 |
| Plastic clayey infilling, moderately overconsolidated | 8 |
| Swelling clayey infilling | 8 – 12 * |

**Open joints** (> 5 mm), no contact between the walls in case of sliding:

| Definition | $J_a$ |
|---|---|
| Zones or bands of non-plastic silty or sandy clay | 5 |
| Zones or bands of disintegrated rock | 6 |
| Zones or bands of non-plastic clay | 6 |
| Zones or bands of swelling plastic clay | 8 |
| Zones or bands of swelling clay | 12 |
| Thick continuous zones of non-plastic clay | 10 |
| Thick continuous zones of non-swelling plastic clay | 13 |
| Thick continuous zones of swelling plastic clay | 13 – 20 * |

\* The value depends on the percentage of the swelling clay fraction and on the possibility of it coming into contact with water.

### Parameter J~w~ (Joint Water Number) { #jw }

It depends on the hydrogeological conditions.

| Definition | $J_w$ |
|---|---|
| Water absent or scarce, locally < 5 l/min | 1 |
| Medium inflow with occasional washout of the infilling | 0.66 |
| Strong or high-pressure inflow in compact rock with open discontinuities without infilling | 0.5 |
| Strong or high-pressure inflow with washout of the infilling | 0.33 |
| Exceptionally strong inflow immediately after excavation, decreasing over time | 0.2 – 0.1 |
| Exceptionally strong inflow immediately after excavation, constant over time | 0.1 – 0.05 |

In the last four cases, with effective drainage systems $J_w$ should be brought back to 1 or 0.66. For a characterisation far from the influence of the excavation, with $RQD/J_n$ sufficiently low (0.5 – 25), the values of $J_w$ (1.0 – 0.66 – 0.5 – 0.33) can be assumed as a function of the overburden heights (0–5; 5–25; 25–250; > 250 m).

### SRF factor (Stress Reduction Factor) { #srf }

A function of the stress state in massive rock or of the tectonic disturbance. See the full table on the [Barton](barton.md#srf) page, which distinguishes its four contexts (weakness zones, competent rock mass, squeezing rock mass, swelling rock mass).

---

## Comparison of the classifications

- **Barton (Q)** and **Singh & Goel (N)** start from the same joint indices; N is Q without the stress effect (SRF = 1).
- **Bieniawski (RMR)** is the reference from which **Romana (SMR)**, **Jašarević (n)** and **Sen** are derived, linked by empirical correlations of the type $RMR = f(\text{index})$.
- **Romana (SMR)** and **Robertson (SRMR)** are designed for **slopes**: the former adds to RMR the face/joint orientation factors, the latter is a scale dedicated to weak rock.

For the links between Q and RMR, the most widely used relationship of Bieniawski is:

$$ RMR = 9 \cdot \ln(Q) + 44 $$

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Rock%20Mechanics%20NX).*
