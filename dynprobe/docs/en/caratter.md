# Characteristic values EC7 / NTC §6.2.2

## Why characteristic values

European (EC7 §2.4.5.2) and Italian (NTC 2018 §6.2.2) geotechnical standards require designing on the **characteristic values** of parameters, not on mean values. The characteristic value accounts for the natural variability of the soil and sampling uncertainty.

## How the calculation works

Dynamic Probing NX estimates the characteristic value of N_SPT for each layer by applying statistical methods to the series of N values collected in the layer. The available methods are:

| Method | Description |
|---|---|
| **Normal** | Estimate based on mean and standard deviation with Gaussian distribution |
| **Lognormal** | Useful when N_SPT has an asymmetric distribution (common with low values) |
| **Student-t** | Corrected for small samples (n < 30) — accounts for uncertainty in the mean |

The confidence level applied corresponds to that indicated by EC7 for the lower characteristic value (5th percentile, conservative side).

## How to use it

In the **Parameter estimation** tab of the Editor:

1. Select the statistical method (Normal / Lognormal / Student-t).
2. For each layer the following are shown: mean, standard deviation, sample size and computed characteristic value.
3. The characteristic N_SPT value is propagated to the correlations to obtain characteristic values of Cu, φ, Mo, Ey, etc.

!!! info "Minimum samples"
    With fewer than 3 readings per layer the statistical calculation has low significance. The app flags cases with n < 3 with a warning — in these cases it is preferable to use a conservative engineering approach (e.g. minimum of observed values).

## Characteristic values in the report

The exported Word report includes the table of characteristic values with the method used, sample size and resulting value — ready to be attached to the geotechnical report.
