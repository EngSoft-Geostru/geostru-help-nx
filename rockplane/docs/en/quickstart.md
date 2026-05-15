# Quickstart — your first project in 5 minutes

Goal: open the app, analyse a sample case, understand how to read the factor of safety (FS).

## 1. Open the app

Go to [nx.geostru.ai/rockplane](https://nx.geostru.ai/rockplane/). The software loads with a set of **default parameters** (a 30 m high slope, β=60°, α=35°) that immediately give you a visible wedge on the right.

## 2. Fill in the Project details (optional for the quickstart)

At the top, click **"Project details"** to expand it. Enter:

- **Description**: e.g. *"SS-18 km 42 slope"*
- **Lat / Lon**: leave 41.9028 / 12.4964 (Rome) for now
- **Site**: location
- **Date**: today

No other field is required to run the calculation.

## 3. Change α to see FS change

In the **Block geometry** card, change `α · failure plane dip` from 35° to 50°. On the right panel you will see **FS drop** in real time (150 ms debounce). Colour of the number:

- 🟢 **green** when FS ≥ 1.30 (Allowable Stress criterion)
- 🟡 **orange** when 1.0 ≤ FS < 1.30 (marginal)
- 🔴 **red** when FS < 1.0 (unstable)

## 4. Click "α crit" to find the critical angle

Next to the α field is the **`α crit`** button: click to run an automatic **sweep** of the α dip over the kinematically admissible range. The software finds the α that minimises FS and sets it. A blue banner shows `α crit ≈ XX.X°  ·  FS_min = X.XXX  ·  range […°…°]`.

[Learn more →](alfa-critico.md)

## 5. Add a passive nail

Go to **step 3 (Reinforcement)**:

1. Click **"+ add reinforcement"** → **Passive nail**
2. Type from the catalogue = **B** (cemented passive bar)
3. Position Yt = 15 m (at mid-height of the slope face)
4. Horizontal spacing = 2.5 m
5. Inclination Δ = 15° (downward, into the rock)

FS rises. Below, in the right panel, the **"Design resistances · nails / anchors"** card appears with the full nail capacity breakdown if you enabled the NTC calculation on the type.

## 6. Change the code

At the top, in the **Project details** card, there is the **Code** selector. Try the options:

- **Characteristic values (γ = 1.0)** → all green chips (unit γ factors, FS_req = 1.30)
- **NTC 2018 — A2+M2+R2** → γ<sub>φ'</sub>=γ<sub>c'</sub>=1.25, γ<sub>R</sub>=1.10
- **EC7 DA2** → γ<sub>G</sub>=1.35 (amplifies the weight)

FS is recomputed with the new factors. The **"γ applied"** chip strip below the selector always shows the effective values.

## 7. Export the calculation report

Menu **Export → Calculation report (Word)**. The software produces a `.docx` report including:

- Cover and code framework
- Input data
- Computed geometry
- **Design resistances** of nails/anchors with breakdown and NTC-style checks
- Forces on the plane
- Result with FS comparison
- Annex A — Code validation (97/97 tests)
- Bibliography

[Read more about Output →](export.md)

---

## Got the flow?

Great! Now move on to the [full workflow](workflow.md) for a realistic case with water, seismic and a complete reinforcement scheme.
