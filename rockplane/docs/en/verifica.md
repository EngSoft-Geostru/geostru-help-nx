# Code approach · partial factors

The user chooses the verification approach from a dropdown. Each approach defines the partial factors γ applied to actions and resistances, and the required FS.

## Available approaches

| Code | Set | γ<sub>G</sub> | γ<sub>Q</sub> | γ<sub>φ</sub> | γ<sub>c</sub> | γ<sub>R</sub> | Required FS |
|---|---|---|---|---|---|---|---|
| Characteristic (TA) | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.30 (default, user-set) |
| **NTC 2018** (A2+M2+R2) | A2+M2+R2 | 1.00 | 1.30 | 1.25 | 1.25 | 1.10 | 1.00 |
| EC7 — DA1 Comb. 1 | A1+M1+R1 | 1.35 | 1.50 | 1.00 | 1.00 | 1.00 | 1.00 |
| EC7 — DA1 Comb. 2 | A2+M2+R2 | 1.00 | 1.30 | 1.25 | 1.25 | 1.00 | 1.00 |
| EC7 — DA2 | A1+M1+R2 | 1.35 | 1.50 | 1.00 | 1.00 | 1.10 | 1.00 |
| EC7 — DA3 | A2+M2+R3 | 1.00 | 1.30 | 1.25 | 1.25 | 1.00 | 1.00 |

## Applied factors

The **"γ applied"** chip strip immediately below the code selector shows the partial factors that are currently in use. Chips with γ = 1.00 are highlighted in green.

## NTC 2018 §6.8 (Italian code)

The standard approach for natural slope stability under NTC 2018 is **Approach 1 Combination 2 (A2+M2+R2)**:

- γ<sub>G</sub> = 1.00, γ<sub>Q</sub> = 1.30 — actions reduced (the weight is NOT amplified)
- γ<sub>φ</sub> = γ<sub>c</sub> = 1.25 — material reduced (friction and cohesion reduced)
- γ<sub>R</sub> = 1.10 — resistance reduced (natural slopes); 1.20 for cut faces

Required FS in this set is 1.00 (since the partial factors are already applied; equivalent to ~1.30 in the characteristic equivalent).

## When to use which

- **Characteristic (TA)**: pre-design, comparison with literature, numerical verifications, didactic. NOT for executive design.
- **NTC 2018 A2+M2+R2**: standard for Italian projects.
- **EC7 DA1 Comb. 1 / DA2**: high γ<sub>G</sub> = 1.35 — amplifies the weight as an unfavourable action. Conservative.
- **EC7 DA1 Comb. 2 / DA3**: parallel of NTC, reduces materials but not weight. More common in continental practice.

## Required FS

For Allowable Stress (TA), the user can manually set the required FS (default 1.30 for slopes per NTC §6.8). For all NTC/EC7 approaches, the partial factors include the safety margin already, so FS<sub>req</sub> = 1.00 (or 1.10 for NTC R2).

## Verification result

The right panel shows:

\[ FS = \tau / |S| \]

compared with FS<sub>req</sub>:

- ✓ **green** — verified (FS ≥ FS<sub>req</sub>)
- ✗ **red** — not verified

The overturning verification F<sub>r</sub> (moments around the toe) is shown below as a separate check.
