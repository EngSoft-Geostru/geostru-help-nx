# Quickstart — your first calculation in 5 minutes

In 5 minutes you see LiquiTer NX working on a sample dataset.

## 1. Open the app

Go to [`nx.geostru.ai/liquiter/`](https://nx.geostru.ai/liquiter/).

## 2. Load the sample dataset

Top toolbar → **File → Open** → **"Sample data"**.

LiquiTer immediately loads a typical stratigraphy (saturated silty sand
over gravel) with realistic seismic parameters (Italian seismic zone 2).

## 3. Inspect the results

In a few seconds LiquiTer:

- Computes **CSR** (Cyclic Stress Ratio) and **CRR** (Cyclic Resistance
  Ratio) for each depth
- Computes the **safety factor FSL = CRR / CSR** layer by layer
- Computes the **Liquefaction Potential Index LPI**
  ([Iwasaki et al. 1982](metodi.md#ipl-indice-del-potenziale-di-liquefazione))
- Estimates **post-seismic settlements** with Ishihara-Yoshimine

You see:

- **Results table**: for each depth step shows σ_v, σ'_v, r_d, CSR, CRR,
  FSL and the verdict (liquefiable / non-liquefiable)
- **FSL vs z plot**: vertical profile of the safety factor with the
  FSL = 1 threshold highlighted
- **LPI banner**: 0 (no risk) — 5 (low risk) — 15 (medium) — >15 (high)

## 4. Change method and compare

At the top, in **Analysis method**, try:

- **Seed** (1971) — the classic, on SPT
- **Tokimatsu** (1983) — on SPT, distinguishes clean / silty sands
- **Boulanger-Idriss** (2014) — on CPT (qc), the most recent
- **Andrus-Stokoe** — on Vs (shear-wave velocity)

Each method returns a slightly different FSL: comparing them helps you
gauge how robust the conclusion is.

## 5. Export

Top toolbar → **Export**:

- **Word report (.docx)** — technical report with tables, charts,
  parameters and conclusions
- **CSV** — raw data (depth, CSR, CRR, FSL) for further analysis in
  Excel / Python

---

## Next steps

- [**Complete workflow**](workflow.md) — a real project from start to finish
- [**Calculation methods**](metodi.md) — when to use which method, formulas
- [**Input data**](dati-input.md) — complete description of every field

---

*Page useful? Questions? [Contact us](mailto:info@geostru.ai?subject=Help%20LiquiTer%20NX%20-%20Quickstart).*
