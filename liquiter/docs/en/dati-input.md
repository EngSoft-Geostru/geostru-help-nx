# Input data — description of each field

Field-by-field reference for the **Liquefaction** page of LiquiTer NX.
For the operational flow see [Workflow](workflow.md).

## "General data" section

### Description

Free text, max 200 characters. Appears on the cover of the Word report.
Example: *"4-storey residential building — Versilia, lot B"*.

### Address

Optional. If filled in, appears in the report.

### Coordinates (lat / lon)

WGS84 in decimal degrees (e.g. `41.9028`, `12.4964`). Used to:

- Geolocate the site on the report map
- Pre-fill a_g and Mw from [Parametri Sismici](https://nx.geostru.ai/parametri-sismici/)
  (if this option is enabled)

### Water table depth (Zw)

Water table depth in **metres** from ground level.

- If Zw > Zmax (maximum depth of the stratigraphy) → no saturated layer →
  **no liquefaction**
- If the water table varies seasonally → use the **worst case** (highest)
  to be conservative

## "Seismic parameters" section

### Code

| Option | Reference |
|---|---|
| **NTC 2018** | Italian D.M. 17/01/2018, Chap. 7.11.3.4 (liquefaction susceptibility) |
| **EC8 — EN 1998-5** | Eurocode 8, Annex F |

The choice determines:
- Limit safety factors (NTC default 1.25, EC8 default 1.0)
- Formulas for CSR and correction factors
- Exclusion criteria (NTC: depth < 20 m, soils with > 5% particles
  < 5 µm, etc.)

### Ground category (A · B · C · D · E)

From Vs,30. Determines the site parameters (S_S, S_T) for computing a_max.

See [workflow.md#categoria-suolo](workflow.md#ground-category-a-b-c-d-e) for the full table.

### Topographic category (T1 · T2 · T3 · T4)

Affects the topographic amplification factor S_T (1.0 – 1.4).

### a_max (peak ground acceleration)

Peak ground acceleration in **g** (e.g. `0.15`).

**Where to get it from**:

- From [`parametri-sismici.geostru.ai`](https://nx.geostru.ai/parametri-sismici/)
  (free) — enter coordinates + return period and it returns a_g
- From the INGV grid (`esse1-gis.mi.ingv.it`)
- From municipal geological reports (for level-3 seismic microzonation)

### Magnitude Mw

**Moment magnitude** of the design earthquake. Typical range for Italy:
**5.5 – 7.0** depending on the INGV zonation.

For Italian territory, the **maximum expected magnitude** of the
seismogenic zone (INGV DISS database) can be used:

| INGV zone | Typical Mw |
|---|---|
| Calabria/Sicily/Friuli | 6.5 – 7.0 |
| Central Apennines | 6.0 – 6.7 |
| Po Plain | 5.5 – 6.5 |
| Sardinia | < 5.5 (low seismicity) |

## "Analysis method" section

See [Calculation methods](metodi.md) for details on each.

### Clean vs silty sands

- **Clean sands**: fines content (< 0.075 mm) **< 5%**
- **Silty sands**: fines content **5–35%**
- > 35% fines: the soil is clayey, not liquefiable (still check with the
  Boulanger 2014 plasticity criterion)

Affects the N1,60 → N1,60,cs correction formula (clean-sand equivalent).

### Loose vs medium-dense sands

Affects the K_σ scaling factor for stresses. Loose sands have a larger
CRR reduction as σ'_v increases.

### Step mode

- **MetaStrato** (default): one calculation point per layer change
- **PassoFisso**: one point every `Δz` (e.g. every 0.5 m)

PassoFisso returns a "cleaner" FSL(z) plot but can overestimate the
contributions of thin layers. MetaStrato is more representative.

### Limit safety factor

Default `1.25` (NTC 2018). Threshold below which a point is considered
"liquefiable". The calculation uses this value to:

- Colour-code the verdict (green/red) in the table
- Include/exclude the layer from LPI and settlement totals

For more conservative analyses use `1.5`. For limit analyses (real risk
computation, not code-driven) use `1.0`.

## "Stratigraphy" section

Dedicated tab, managed by **layer**. For each layer:

| Field | Unit | Meaning |
|---|---|---|
| **Top depth** | m | top elevation |
| **Bottom depth** | m | bottom elevation (the bottom of one layer is the top of the next) |
| **Lithology** | — | descriptive, does not enter the calculation |
| **γ** | kN/m³ | unit weight; **total** above the water table, **saturated** below |
| **N-SPT** | blows/30cm | from the Standard Penetration Test (UNI EN ISO 22476-3) |
| **qc** | MPa | CPT tip resistance (UNI EN ISO 22476-1). Optional. |
| **Vs** | m/s | S-wave velocity. Optional. |
| **% clay** | % | fraction < 5 µm; > 35% rules out liquefaction (NTC) |

### Stratigraphy import

The **Stratigraphy** tab has functions for:

- **Import CSV** (stratigraphy exported from other GeoStru software or from Excel)
- **AI Import** (photo of the borehole log, AI extracts the parameters)
- **Stratigraphy adapter** (compatibility with other GeoStru formats)

---

## See also

- [Complete workflow](workflow.md) — the flow of the whole process
- [Calculation methods](metodi.md) — formulas for each method
- [FAQ](faq.md) — questions on input parameters

---

*Page useful? [Contact us](mailto:info@geostru.ai?subject=Help%20LiquiTer%20NX%20-%20Input%20data).*
