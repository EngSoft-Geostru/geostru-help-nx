# Interpreted stratigraphy

## What it is

The interpreted stratigraphy is the subsoil model derived from the test readings. You define a number of layers — each with a lower depth, a soil type and unit weights γ and γ_sat — and the software computes for each the representative N_SPT value, from which the geotechnical correlations are then derived.

## How to enter it

In the **Interpreted stratigraphy** tab of the Editor:

1. The first layer starts at 0 m. Set its lower depth (e.g. 2.50 m).
2. Click **+ Add layer** to create the next layer.
3. For each layer:
   - Set the **lower depth** (m from ground level).
   - Choose the **soil type**: `COES` (cohesive), `INCO` (non-cohesive) or both if mixed — the type determines which correlations are applied.
   - Enter **γ** (dry or natural unit weight) and **γ_sat** (saturated unit weight) in kN/m³.
   - Optionally enter **clay (%)** and the lithological **description**.

## The 7 N_SPT aggregation methods

For each layer, the readings falling within its depth range are aggregated using the method chosen by the user. The available methods are:

| Method | When to use it |
|---|---|
| **Mean** | Homogeneous soil, limited variability |
| **Minimum** | Conservative approach — the worst value is used |
| **Maximum** | Upper bound estimate (e.g. for tip bearing capacity) |
| **Mean − 1σ** | Statistically conservative approach |
| **Mean + 1σ** | Statistically non-conservative approach |
| **RNC** (normal distribution) | Characteristic value in probability according to EC7 §2.4.5.2 |
| **RC** (log-normal distribution) | Like RNC but with log-normal distribution — preferable for N_SPT with low values |

The method is set in the N_SPT column header of the stratigraphy table, and applies to all layers simultaneously.

!!! info "Which is the right method?"
    EC7 (and NTC §6.2.2) specifies using the **characteristic value** of the parameter, defined as the value with a 5% probability of being exceeded on the conservative side. The RNC and RC methods approach this statistical definition. For small samples (< 6 readings per layer) the mean remains the most robust reference.

## N_DPM → N_SPT conversion

For continuous tests, the layer N_SPT is obtained from N_DPM by applying the β coefficient (see [Instruments →](strumenti.md)). The product N_DPM × β is the equivalent N_SPT for each reading; the aggregation is then applied to these equivalent values.

## Σ layers / test badge

At the bottom of the stratigraphy screen the badge shows:

```
Σ layers  X.XX m  /  test  Y.YY m
```

- **Green** (✓): the sum of layer depths matches the test depth — the stratigraphy covers the entire test without gaps.
- **Yellow** (⚠): discrepancy between Σ layers and test depth — check that the last layer reaches the end of the test.
