# Probabilistic analyses

These analyses estimate the parameters of a probability distribution
that describes the extreme-rainfall regime, and use it to extract the
expected heights for assigned return periods \(T\).

All methods assume that the **annual maxima** for a fixed duration are
independent realisations of the same random variable.

## Gumbel (EV1)

The 2-parameter Gumbel distribution describes the maxima of large samples:

$$
F(h) = \exp\!\left[-\exp\!\left(-\frac{h - \mu}{\beta}\right)\right]
\qquad
h(T) = \mu - \beta \ln\!\left[-\ln\!\left(1 - \frac{1}{T}\right)\right]
$$

Two available estimators:

- **Method of moments**. Fast, robust.
  \(\beta = s \sqrt{6}/\pi\), \(\mu = \bar{h} - \gamma\,\beta\) (\(\gamma \approx 0.5772\) Euler-Mascheroni constant).
- **Maximum Likelihood (ML)**. Iterative, slightly more efficient.

## GEV — Generalized Extreme Value (L-moments)

A family that generalises Gumbel: it includes a **shape parameter \(\kappa\)** allowing
heavy tails (\(\kappa > 0\)) or bounded tails (\(\kappa < 0\)).

$$
F(h) = \exp\!\left[-\left(1 - \kappa\,\frac{h - \xi}{\alpha}\right)^{1/\kappa}\right]
$$

The three parameters \((\xi, \alpha, \kappa)\) are estimated via **L-moments**
(Hosking 1990) — more robust than classical moments for small samples.

Heights h(T):

$$
h(T) = \xi + \frac{\alpha}{\kappa}\!\left[1 - \left(-\ln(1 - 1/T)\right)^{\kappa}\right]
$$

!!! tip "GEV vs Gumbel?"
    Prefer GEV when the series has few years and unusual extreme values.
    For series with >50 years and no "fat tails", Gumbel is usually enough
    and easier to justify in a report.

## Pearson III (method of moments — Foster/Kite)

A 3-parameter distribution (\(\bar{h}, s, C_s\) = mean, standard deviation,
skewness) historically popular in the Anglo-Saxon world:

$$
h(T) = \bar{h} + K_T(C_s) \cdot s
$$

with \(K_T\) a tabulated frequency factor (Wilson-Hilferty's formula for
analytical computation).

Useful when the series has marked skewness and Gumbel underestimates the tail.

## TCEV — Two-Component Extreme Value (VA.PI. — Italy)

Regional model for Italy based on the **VA.PI.** programme (Valutazione delle
Piene in Italia, CNR-GNDCI). Distinguishes **ordinary** and **extraordinary**
events by admitting two superposed EV1 components.

$$
F(h) = \exp\!\left[-\Lambda_1 e^{-h/\theta_1} - \Lambda_2 e^{-h/\theta_2}\right]
$$

The 4 parameters \((\Lambda_1, \theta_1, \Lambda_2, \theta_2)\) are hard to
estimate pointwise: Runoff Lab NX implements the classical **4 regionalisation
levels**:

| Level | What's fixed | What's estimated |
|-------|--------------|-------------------|
| **0 — pointwise** | no regional parameter | all 4 from the station (poor under 30 years) |
| **1 — regional** | \(\Lambda^* = \Lambda_2/\Lambda_1\), \(\Theta^* = \theta_2/\theta_1\) | the remaining 2 from the station |
| **2** | as level 1 + \(\Lambda_1\) | only \(\theta_1\) |
| **3** | all shape parameters regional; \(\theta_1\) from scale | non-dimensional + local scale |

The VA.PI. dataset is loaded for known Italian regions. For regions or
countries not covered, the TCEV option is hidden when the interface
language is not Italian.

!!! note "When TCEV makes sense"
    TCEV captures well the upper tail of catastrophic events typical of the
    Italian climate (convective floods on small basins). Many basin
    authorities recommend it for Hydraulic Vigilance and PAI plans.

## Goodness-of-fit tests

For each analysis the software runs two tests:

- **Kolmogorov-Smirnov** (KS): maximum distance between empirical and
  theoretical CDF. Compared to the 5% critical value.
- **Pearson χ²**: comparison on frequency classes.

Both are **not rejected at 5%** if p-value > 0.05. A single distribution
that passes both is preferable to two that each fail one.

## Reference bibliography

- Gumbel E.J. (1958), *Statistics of Extremes*, Columbia University Press.
- Hosking J.R.M. (1990), *L-moments: analysis and estimation of distributions
  using linear combinations of order statistics*, J. Royal Stat. Soc. B 52.
- Kite G.W. (1977), *Frequency and Risk Analyses in Hydrology*, Water Resources Publ.
- Rossi F., Versace P. (1982), *Criteri e metodi per l'analisi statistica delle
  piene*, CNR-PFC, Italy.
- VA.PI. programme — CNR-GNDCI, *Valutazione delle Piene in Italia*, regional reports.
