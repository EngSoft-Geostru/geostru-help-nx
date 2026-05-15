# Material

Defines the unit weight of the wedge and the shear strength criterion on the failure plane.

## Common parameters

| Parameter | Symbol | Units | Notes |
|---|---|---|---|
| Block unit weight | γ | kN/m³ | rock density × g; typical 22–28 kN/m³ |

## Strength criteria

Two criteria are available, selected via radio button.

### Mohr-Coulomb (linear, default)

$$\tau = c + \sigma_n \cdot \tan\varphi$$

| Parameter | Symbol | Units | Typical |
|---|---|---|---|
| Cohesion on plane | c | kPa | 0–50 (often 0 for clean joints) |
| Peak friction angle | φ | ° | 25–45 |

This is the classical Hoek-Bray model. Use it for clean joints where dilation is negligible or for first-pass design.

### Barton-Bandis (non-linear)

$$\tau = \sigma_n \cdot \tan\left(\varphi_b + JRC \cdot \log_{10}\!\frac{JCS}{\sigma_n}\right)$$

| Parameter | Symbol | Units | Notes |
|---|---|---|---|
| Basic friction angle | φ<sub>b</sub> | ° | smooth rock: 25–35° (siliceous), 30–38° (carbonate). From tilt-test. |
| Joint Roughness Coefficient | JRC | – | 0–4 smooth, 4–8 wavy, 8–12 wavy-rough, 12–16 rough, 16–20 very rough. From Barton-Choubey 1977 charts. |
| Joint Compressive Strength | JCS | MPa | 50–200 MPa intact rock, 5–30 MPa weathered. From Schmidt hammer or ≈ UCS. |

The roughness dilation term **i<sub>eff</sub> = JRC · log₁₀(JCS/σ<sub>n</sub>)** is added to φ<sub>b</sub> to obtain the mobilised friction angle. At low normal stress (near the crest) i<sub>eff</sub> can be very large; it is clamped to 70° to avoid logarithm divergence.

The diagnostics panel under the section view shows σ<sub>n</sub>, i<sub>eff</sub>, φ<sub>b</sub>+i<sub>eff</sub> and the resulting τ on the plane.

## When to use which

- **Mohr-Coulomb**: cohesion known from test, or rough preliminary analysis.
- **Barton-Bandis**: rough rock joints at low confining stress (typical in rock slopes), where dilation makes the joint stronger than its base friction suggests. More representative for real rock.

[See full coefficient tables →](verifica.md)
