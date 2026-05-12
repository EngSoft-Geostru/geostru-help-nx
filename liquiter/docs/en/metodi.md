# Calculation methods

LiquiTer NX implements **4 semi-empirical methods** to compute CRR
(Cyclic Resistance Ratio), and hence the liquefaction safety factor. The
choice depends on the **in-situ test available**:

| In-situ test | Recommended method |
|---|---|
| **SPT** (Standard Penetration Test) | Seed (1971), Tokimatsu (1983) |
| **CPT** (Cone Penetration Test) | Boulanger-Idriss (2014) |
| **Cross-hole / Down-hole** (Vs) | Andrus-Stokoe (2000) |

All methods compute CSR in the same way (Seed-Idriss 1971); only the way
CRR is estimated changes.

## CSR — Cyclic Stress Ratio

Common to all methods:

$$
\text{CSR} = 0{,}65 \cdot \frac{a_{\max}}{g} \cdot \frac{\sigma_v}{\sigma'_v} \cdot r_d
$$

where:

- **a_max** = peak ground acceleration
- **σ_v / σ'_v** = total / effective stress at depth z
- **r_d** = depth reduction coefficient (Liao-Whitman 1986 or
  Idriss-Boulanger 2008 depending on the method)

## 1. Seed (1971)

**On SPT — the classic method, still the most used in Italy.**

CRR is estimated from **N1,60,cs** (SPT number corrected for: energy,
confining pressure, fines content "clean-sand equivalent") using the
original Seed et al. (1985) semi-empirical curve.

### When to use it

- You have SPT as the main in-situ test
- The site contains sands / silty sands
- You want a result comparable with historical Italian literature

### Limitations

- Does not clearly distinguish clean and silty sands (the clean-sand
  correction is approximate)
- Base curve derived from M = 7.5 earthquakes — apply the MSF scaling
  factor for other magnitudes

### References

- Seed H.B., Idriss I.M. (1971) — *Simplified procedure for evaluating soil
  liquefaction potential*. JGED, ASCE
- Seed H.B., Tokimatsu K., Harder L.F., Chung R.M. (1985) — *Influence of
  SPT procedures in soil liquefaction resistance evaluations*. JGED

## 2. Tokimatsu (1983)

**On SPT — variant that distinguishes clean/silty sands with dedicated curves.**

Same logic as Seed but uses:

- **Separate** CRR(N1) curves for clean and silty sands
- A different correction for confining pressure

### When to use it

- You have SPT + good grain-size characterisation (you know well whether
  the sand is clean or silty)
- You want to compare with Seed for verification

### References

- Tokimatsu K., Yoshimi Y. (1983) — *Empirical correlation of soil
  liquefaction based on SPT N-value and fines content*. Soils and Foundations

## 3. Boulanger-Idriss (2014)

**On CPT — the most recent method, recommended when you have continuous CPT.**

CRR is estimated from **qc1N,cs** (normalised, clean-sand equivalent CPT
resistance) using the Boulanger-Idriss (2014) curve.

Advantages over SPT:

- Continuous profile along the vertical (every 1-2 cm), not in 1-m steps
- More repeatable measurement (operator-independent)
- Fines-content corrections based on Ic (soil-behaviour type index) —
  more robust

### When to use it

- You have CPT (CPTU if possible)
- You want a "continuous" calculation along the vertical
- International state of the art

### References

- Boulanger R.W., Idriss I.M. (2014) — *CPT and SPT based liquefaction
  triggering procedures*. UC Davis Report UCD/CGM-14/01
- Idriss I.M., Boulanger R.W. (2008) — *Soil liquefaction during earthquakes*.
  EERI Monograph

## 4. Andrus-Stokoe (2000)

**On Vs — useful when you have cross-hole/down-hole or passive seismic data.**

CRR is estimated from **Vs1,cs** (normalised, clean-sand equivalent Vs)
using the Andrus-Stokoe (2000) curve.

### When to use it

- You have shear-wave velocity Vs (cross-hole, down-hole, passive
  seismic, MASW)
- The layer is gravelly or contains cobbles (problematic for SPT/CPT)
- The site is on a slope where SPT/CPT are difficult

### Limitations

- Vs is less sensitive to small density variations than SPT/CPT
- Lower reliability in very loose sands

### References

- Andrus R.D., Stokoe K.H. (2000) — *Liquefaction resistance of soils from
  shear-wave velocity*. JGGE, ASCE

## Scaling factors

All methods apply **correction factors** to the raw FSL:

### MSF — Magnitude Scaling Factor

Corrects for shaking duration, since the base CRR curves are for
M = 7.5. For smaller M the earthquake is shorter → fewer cycles → higher
CRR:

$$
\text{MSF} = \left(\frac{M_w}{7{,}5}\right)^{-2{,}56}
$$

(Idriss 1999 formulation, accepted by NTC 2018)

### K_σ — Overburden Correction

Corrects for confining pressure. For σ'_v > 100 kPa CRR decreases
(loose sands) or slightly increases (dense sands):

$$
K_\sigma = 1 - C_\sigma \cdot \ln\left(\frac{\sigma'_v}{p_a}\right)
$$

with C_σ a function of DR (relative density).

### K_α — Static Shear Stress Correction

For slopes (in LiquiTer not implemented — horizontal ground assumed).

## FSL — Safety factor

$$
\text{FSL} = \frac{\text{CRR} \cdot \text{MSF} \cdot K_\sigma}{\text{CSR}}
$$

Liquefaction threshold: **FSL < FSL_limit** (default 1.25 for NTC 2018,
1.0 for EC8).

## LPI — Liquefaction Potential Index

Iwasaki et al. (1982) — integrates the "deficit" FSL < 1 over the top
20 m:

$$
\text{IPL} = \int_0^{20} F(z) \cdot w(z) \, dz
$$

with:

- F(z) = `1 - FSL(z)` if FSL < 1, otherwise 0
- w(z) = `10 - 0.5 z` (weight linearly decreasing with depth)

| LPI | Liquefaction risk |
|---|---|
| 0 | Negligible |
| 0–5 | Low |
| 5–15 | Medium |
| > 15 | High |

## Post-seismic settlements (Ishihara-Yoshimine 1992)

For each liquefiable layer, the volumetric settlement ε_v is a function of:

- FSL of the layer
- Relative density DR (estimated from N1,60 or qc1N)

The **total settlement** is the sum of the contributions of each
liquefiable layer, integrated along the vertical.

LiquiTer shows:

- **Per-layer settlement** (cm)
- **Total settlement at ground level** (cm)
- **Differential settlement** (if relevant)

### References

- Ishihara K., Yoshimine M. (1992) — *Evaluation of settlements in sand
  deposits following liquefaction during earthquakes*. Soils and Foundations

---

## Which method to choose — summary

| Situation | Method |
|---|---|
| SPT as the only in-situ test (most common case in Italy) | **Seed** or **Tokimatsu** |
| You have continuous CPT/CPTU | **Boulanger-Idriss** (state of the art) |
| You have Vs (cross-hole, down-hole, MASW) | **Andrus-Stokoe** |
| You want a multi-method comparison | Run all of them, compare LPI |
| Gravelly site or with cobbles | **Andrus-Stokoe** (Vs little affected by grain size) |

---

*Page useful? [Contact us](mailto:info@geostru.ai?subject=Help%20LiquiTer%20NX%20-%20Methods).*
