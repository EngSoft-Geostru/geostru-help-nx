# Glossary

Concise definitions of the terms, indices and symbols used in geostructural surveys, geomechanical classifications and the calculation report of Rock Mechanics NX. Where useful, each entry points to the chapter that covers it in depth.

## Survey and discontinuities

**Dip direction** — the direction, measured in degrees from North (0–360°), towards which a discontinuity plane dips, i.e. the direction of maximum slope projected onto the horizontal.

**Dip** — the angle (0–90°) between the discontinuity plane and the horizontal, measured along the line of maximum slope. Together with the dip direction it defines the *orientation* (attitude) of the plane.

**Discontinuity** — any surface of mechanical separation within the rock mass (joint, fracture, fault, bedding plane, schistosity) along which the tensile strength is practically nil. It is the element that governs the behaviour of the rock mass.

**Joint set** — a group of discontinuities with similar orientation, originated from the same tectonic event. The number of sets present determines the $J_n$ parameter in the [Barton](barton.md) classification.

**Persistence** — the areal extent of a discontinuity within its plane, measured as trace length. It expresses how continuous the fracture is: high persistence means potentially through-going sliding surfaces.

**Aperture** — the distance, measured orthogonally, between the two walls of a discontinuity along the stretch where they are not in contact. It affects permeability, infilling and shear strength.

**Roughness** — the small- and medium-scale surface irregularity of a discontinuity. It increases the peak friction angle; it is quantified by the **JRC** (*Joint Roughness Coefficient*, 0–20) for the Barton-Bandis criterion, or by the descriptors that set $J_r$.

**Weathering (alteration)** — the degree of degradation, by chemical and physical agents, of the discontinuity walls and of the rock matrix. It reduces strength and feeds into $J_a$ and the RMR scores.

**Infilling** — material (clay, silt, sand, calcite, etc.) interposed between the walls of a discontinuity. The nature and thickness of the infilling control the shear strength of the joint.

**Spacing** — the average distance $s$ between adjacent discontinuities of the same set, measured orthogonally to the planes. It determines block size and the `A3` parameter of RMR (see [Classifications](classificazioni.md#spaziatura-delle-discontinuita)).

**$J_v$ (volumetric joint count)** — the total number of joints per cubic metre of rock mass, summed over all sets. It is the basis for estimating RQD when borehole cores are unavailable.

## Classification indices

**RQD (Rock Quality Designation)** — the degree of fracturing of the rock mass, expressed as the percentage of core recovered in pieces $\geq 100$ mm. In the absence of boreholes it is estimated from $J_v$ (Palmström) or from $\lambda$ (Priest-Hudson). See [RQD](classificazioni.md#rqd-rock-quality-designation).

**Q-index (Barton)** — the index of the *Norwegian Geotechnical Institute classification* for underground works and general characterisation: $Q = \frac{RQD}{J_n} \cdot \frac{J_r}{J_a} \cdot \frac{J_w}{SRF}$. See [Barton](barton.md).

**RMR (Rock Mass Rating)** — Bieniawski's index (0–100) obtained by summing partial ratings (strength, RQD, spacing, joint conditions, water) and correcting for orientation. It is the reference from which many other classifications are derived. See [Bieniawski & Romana](rmr-romana.md).

**SMR (Slope Mass Rating)** — Romana's adaptation of RMR to slopes: factors that weight the relative orientation of the slope face and the joints and the excavation method are applied to RMR. See [Bieniawski & Romana](rmr-romana.md).

**SRMR (Slope Rock Mass Rating)** — Robertson's scale dedicated to soft-rock slopes (RMR < 40), where the classic RMR loses reliability. See [Robertson](robertson.md).

**n-index (Jašarević)** — the index of the Jašarević & Kovačević classification for carbonate rock masses, empirically correlated to RMR. See [Jašarević](jasarevic.md).

**N-index / Rock Mass Number** — Singh & Goel's *Rock Mass Number*: it coincides with the Q-index computed by setting $SRF = 1$, i.e. cleared of the effect of the stress state. See [Singh & Goel](singh-goel.md).

**RCR (Rock Condition Rating)** — RMR stripped of the rating for compressive strength and of the orientation correction; used as an intermediate quantity in the correlations between RMR and Q.

**GSI (Geological Strength Index)** — Hoek's index that describes the quality of the rock mass from its structure and the condition of the discontinuities; it is the input parameter of the Hoek-Brown failure criterion used to derive the strength parameters.

## Strength parameters

**$S_u$ — uniaxial compressive strength** — the uniaxial compressive strength of the *intact* rock (matrix). It is determined from the Point Load test, the Schmidt hammer or the ISRM estimate, and it feeds the `A1` parameter of all methods derived from RMR (see [Classifications](classificazioni.md#resistenza-a-compressione-uniassiale-su)).

**$I_s$ — point load index** — the index obtained from the Point Load Test, correlated to $S_u$ by $S_u = K \cdot I_s$, with $K$ a function of $I_s$.

**$\sigma_c$** — compressive stress; in the rock-mass context it denotes the reference compressive strength (intact rock or rock mass, depending on the criterion adopted).

**Cohesion $c$** — the component of shear strength independent of normal stress, in the Mohr-Coulomb criterion $\tau = c + \sigma_n \tan\varphi$. On real discontinuities it is often low or nil.

**Friction angle $\varphi$** — the frictional component of shear strength: $\tan\varphi$ multiplies the effective normal stress $\sigma_n$ in the Mohr-Coulomb criterion.

**Deformation modulus $E$** — the modulus relating stress and strain of the rock mass; it is estimated from the classifications (correlations with RMR, Q or GSI) and is a characteristic parameter of the output.

**SRF (Stress Reduction Factor)** — the stress-reduction factor of the Q-index, which accounts for the stress state in massive rock, tectonic disturbance and squeezing or swelling conditions (see [Barton](barton.md#srf)).

**$J_n$ (Joint Set Number)** — Barton's parameter linked to the number of joint sets: it increases as the number of sets, and therefore the break-up of the rock mass, increases (see [Classifications](classificazioni.md#jn)).

**$J_r$ (Joint Roughness Number)** — Barton's parameter that is a function of the roughness and waviness of the most unfavourable joint set (see [Classifications](classificazioni.md#jr)).

**$J_a$ (Joint Alteration Number)** — Barton's parameter that is a function of the alteration of the walls and of the nature/thickness of the discontinuity infilling (see [Classifications](classificazioni.md#ja)).

**$J_w$ (Joint Water Number)** — Barton's parameter that is a function of the hydraulic conditions (water inflow and pressure in the discontinuities) (see [Classifications](classificazioni.md#jw)).

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Rock%20Mechanics%20NX).*
