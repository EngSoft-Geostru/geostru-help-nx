# FAQ — frequently asked questions

## General

### Is LiquiTer NX free?

LiquiTer NX is part of the **GeoStru NX suite** with a *freemium* plan:

- **Free**: access, full calculation, CSV export
- **Subscription**: Word report, AI Import, multi-site batch, priority support

For details: [`geostru.ai`](https://www.geostru.ai/) or `info@geostru.ai`.

### Do I have to install anything?

**No**. LiquiTer NX is a **web app** that opens from
[`nx.geostru.ai/liquiter/`](https://nx.geostru.ai/liquiter/) in any
modern browser. Works on Windows / Mac / Linux PCs.

### Does my data go through GeoStru servers?

Calculations happen **server-side** (in GCP cloud, encrypted). Projects
are saved to your device as `.json` when you press *Save*. We do not
share data with third parties.

If you need **confidential data** handling (forensic reports, military
sites): contact us privately for on-premise hosting options.

---

## Input

### Where do I find a_g and Mw for my site?

- **a_g** (NTC 2018): from [parametri-sismici.geostru.ai](https://nx.geostru.ai/parametri-sismici/)
  with coordinates + return period (nominal life × Cu × P_VR)
- **Mw**: from the maximum expected magnitude of the **seismogenic zone**
  INGV (DISS database). For Italy: Calabria/Friuli ~ 7.0, Central
  Apennines ~ 6.5, Po Plain ~ 5.5–6.5, Sardinia < 5.5.

### Ground category without Vs,30

NTC 2018 allows estimation **from geotechnical tests**:

- Cat. **C**: dense sandy/gravelly soils, stiff clays
- Cat. **D**: loose granular soils, soft clays
- Cat. **E**: 5–20 m alluvial layer on a Cat. A substrate

When in doubt, assume **the worst case** or run MASW to measure Vs,30.

### How much does the result change between Seed and Boulanger?

In typical clean/silty sands, the difference is within **10–20%** on the
FSL. Boulanger-Idriss tends to be **more conservative** in silty sands.
Run both and compare — if both give LPI > 5 the site is critical
(agreement between methods strengthens the conclusion).

### Can I use LiquiTer on clays?

**No**, not directly. True liquefaction concerns saturated sands and
silty sands. For clays the phenomenon of **cyclic softening** (cyclic
degradation of undrained strength) may exist, but it requires different
methods (Boulanger-Idriss 2007 for clays, Bray-Sancio 2006). LiquiTer
does not currently implement cyclic softening.

Clays with **> 35% of particles < 5 µm** are **automatically excluded**
from the calculation (NTC 2018).

### Can I use LiquiTer on a slope?

LiquiTer NX assumes **horizontal ground**. On slopes the presence of a
static shear stress (K_α correction) modifies CRR. Slope analysis would
require a dedicated method — at the moment we only use K_α = 1
(horizontal), conservative for not-too-steep slopes.

---

## Calculation

### What does "Run calculation" do?

For each depth z along the stratigraphy:

1. Computes stresses σ_v, σ'_v
2. Computes CSR (Seed-Idriss)
3. Computes CRR with the selected method
4. Applies MSF and K_σ
5. Computes FSL = (CRR · MSF · K_σ) / CSR
6. Marks the layer as liquefiable if FSL < FSL_limit

Then integrates LPI and settlements.

### I see FSL = 99 in some layers. Why?

FSL = 99 (or "non-liquefiable") means the layer:

- Is **above the water table** (unsaturated soil)
- Has **% clay > 35%** (excluded by NTC)
- Is at **depth > 20 m** (excluded by NTC)
- Has **N-SPT too high** to be liquefiable (very dense soil)

All of these are cases where the calculation is **logically bypassed**.

### The default limit safety factor is 1.25, can I change it?

Yes. Default 1.25 (NTC 2018). You can set 1.0 (EC8) or 1.5 (conservative
analysis). Edit it in the *Limit safety factor* field. The calculation
itself is unchanged — only the **colour-coding threshold** (what is "red"
vs "green") and the **LPI counting** change.

---

## Exports

### The Word report won't open

- Check that you have Word 2016+, LibreOffice 6+, or Google Docs
- Open as a fallback in LibreOffice (it always handles `.docx`)
- If the issue persists, contact us at info@geostru.ai with the file attached

### I want to customise the Word template

For now the template is centralised. For a custom template (firm logo,
fonts), write to `info@geostru.ai`.

---

## My question isn't here

[Write to us](mailto:info@geostru.ai?subject=Help%20LiquiTer%20NX%20-%20FAQ)
and we'll add it.
