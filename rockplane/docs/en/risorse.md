# Resources — sample files

Ready-to-use case studies to download and open with **File → Open from file…** in the app.

## How to use a sample

1. Click the `.rockplane` link below to download
2. Open RockPlane NX at [nx.geostru.ai/rockplane/](https://nx.geostru.ai/rockplane/)
3. Menu **File → Open from file…** and select the downloaded file
4. The project loads with all parameters set (geometry, material, water, seismic, reinforcement, catalogue)
5. Edit freely to explore

## Available samples

### Zone 1 — Block 2 (karst rock with TC and 5 rows of nails)

[**📥 Download `zona-1-blocco-2.rockplane`**](samples/zona-1-blocco-2.rockplane)

| Parameter | Value |
|---|---|
| Slope height H | 11.31 m |
| Slope face dip β | 70° |
| Failure plane dip α | 15° |
| Upper face dip ψ | 0° |
| Block depth B | 8 m |
| Tension crack | T = 3 m, θ = 70° |
| Unit weight γ | 22 kN/m³ |
| Cohesion c | 0 kPa |
| Friction angle φ | 38° |
| Seismic kh | 0.08 (Ω = 0°) |
| Water in TC (Zw) | 10 m (max at toe) |
| Reinforcement | 5 rows of φ32 nails, L=9m, Δ=15°, 2.66 m spacing |

Reference case from a legacy SRS GeoStru desktop print-out, rebuilt in RockPlane NX to validate the consistency between the desktop and the web version. Useful as a numerical reference.

**Expected output** (after opening and recomputing):
- FS ≈ 1.6 with the 5 rows of nails
- Without nails (disable them), FS drops to ~1.0–1.1 → nailing scheme correctly sized.

### Block 7 — desktop validation case (Barton-Bandis, 2 rows of nails)

[**📥 Download `blocco-7.rockplane`**](samples/blocco-7.rockplane)

| Parameter | Value |
|---|---|
| Slope height H | 4.5 m |
| Slope face dip β | 85° (near-vertical) |
| Failure plane dip α | 45° |
| Upper face dip ψ | 0° |
| Block depth B | 4 m |
| Tension crack | no |
| Strength criterion | **Barton-Bandis** |
| Unit weight γ | 22 kN/m³ |
| Cohesion c | 0 kPa |
| Friction angle | φ=38°, φb=32° |
| JRC | 8 |
| JCS | 160 MPa |
| Seismic kh | 0.08 |
| Water | none |
| Reinforcement | 2 rows of passive nails φ32 in φ90 hole, L=6 m, Δ=15°, 2.0 m spacing, Yt={2.5, 4.0} m |
| Single nail capacity | 325 kN |

Reference case from the GeoStru RockPlane **desktop validation manual**, rebuilt identically in RockPlane NX for numerical comparison.

!!! note "Desktop label vs nail in the tables"
    In the desktop manual the elements are drawn as "passive anchor" but the tables treat them as **nails** (analysis with nails). In RockPlane NX they are modelled consistently as `PassiveNail` with `NTC type = Nail`, soil-nail behaviour (Variant A NTC §6.7).

**Expected output** (after opening and recomputing):
- FS ≈ 3.0 — over-designed 2× compared to the target NTC of 1.3 (broad margin given the conservative near-vertical geometry).
- Single nail design resistances, if NTC calculation enabled, should match:
  - **Hole pull-out (Ta3)** ≈ 3360 kN (with σc = 30 MPa, π·90·6000·0.1σc / 2.16)
  - **Bar↔grout bond (Ta2)** ≈ 1622 kN (with τb = 2.69 N/mm², π·32·6000·τb)
  - **Steel resistance (Ta1)** = 325 kN (= η²·fy·A_gross, with η=0.7, fy=826, D=32)

---

## Want to share your own case?

If you have an interesting case to share as a sample (anonymised), write to [info@geostru.ai](mailto:info@geostru.ai?subject=RockPlane%20NX%20sample) attaching the `.rockplane` file saved from the software.

On the roadmap: a public sample library categorised by failure mode, applicable code and reinforcement type.
