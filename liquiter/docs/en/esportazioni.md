# Exports — Word, CSV

At the end of an analysis LiquiTer NX produces 2 outputs, accessible
from the toolbar:

## Word report (.docx)

The **Word report** is a pre-formatted technical report, compliant with
NTC 2018 chap. 7.11.3.4.

### What it contains

1. **Cover page** with: title, description, site, operator, date, GPS map
2. **Input data summary**:
   - Stratigraphy table (γ, N-SPT, qc, Vs, % clay)
   - Seismic parameters (a_g, Mw, code, ground category, S_S, S_T)
   - Water table depth
3. **Calculation methodology**:
   - Normative reference
   - Selected method + formulas
   - Values of the correction coefficients (r_d, MSF, K_σ)
4. **Results**:
   - Table by depth (z, σ_v, σ'_v, CSR, CRR, FSL, verdict)
   - FSL vs z plot
   - LPI and risk classification
   - Per-layer settlements + total settlement
5. **Conclusions**:
   - Site susceptibility summary
   - Any recommendations (mitigation, further investigation)

### Compatibility

Opens in:

- **Microsoft Word** 2016+
- **LibreOffice Writer** 6+
- **Google Docs** (uploaded to Drive)
- **Pages** (macOS)

Charts are embedded PNG at 300 DPI.

### Customising the template

If you need a custom corporate layout (firm logo, specific fonts), contact
[info@geostru.ai](mailto:info@geostru.ai) — we can configure a dedicated
template for your studio.

## CSV — raw data

Tabular export in CSV (UTF-8 BOM encoding, comma separator), compatible
with Excel / LibreOffice / Google Sheets / Python.

### Columns included

```
z, sigma_v, sigma_v_eff, r_d, CSR, CRR, FSL, MSF, K_sigma, verdict, IPL_contrib, settlement_cm
```

### When it makes sense

- **Sensitivity analysis** — export CSV with the results of Seed,
  Tokimatsu, Boulanger and produce comparative charts in Excel
- **Combine with other surveys** — liquefaction comparison across
  multiple sites
- **Custom recomputation** in Python (e.g. compute settlements with
  alternative methods such as Cetin)
- **Long-term archival** in a forever-readable format

---

## FSL and LPI interpretation

The FSL and LPI values **are not a verdict**: they must be read with
judgement.

### FSL — depth-by-depth safety factor

| FSL | Meaning | Action |
|---|---|---|
| > 1.5 | Stable with margin | None |
| 1.25 – 1.5 | Stable (NTC margin) | None |
| 1.0 – 1.25 | Close to the limit | Investigate further, consider mitigation |
| < 1.0 | Liquefiable | Mitigation required |

### LPI — overall site index

Iwasaki et al. (1982):

| LPI | Risk | Typical decision |
|---|---|---|
| 0 | Negligible | Standard construction |
| 0–5 | Low | Standard construction, watch foundations |
| 5–15 | Medium | Mitigation recommended or stiff raft |
| > 15 | High | Mitigation mandatory (jet grouting, drains, piles) |

!!! warning "Final decision is the professional's"
    LiquiTer produces **geometric / statistical input** for the report.
    The final decision (site OK / mitigation needed / which mitigation
    type) lies with the engineer / geologist who signs the project.
    Liquefaction susceptibility must be combined with seismic-risk
    assessment, the nominal-life class of the structure, the criticality
    of the foundations.

---

## See also

- [Complete workflow](workflow.md) — export in the full cycle
- [Calculation methods](metodi.md) — FSL and LPI interpretation
- [FAQ](faq.md) — questions on exports

---

*Page useful? [Contact us](mailto:info@geostru.ai?subject=Help%20LiquiTer%20NX%20-%20Exports).*
