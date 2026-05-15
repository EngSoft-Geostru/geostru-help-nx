# External load E

A generic concentrated action applied at the wedge centroid. Use it to model road embankments, foundations of buildings, traffic loads, or vertical anchor reactions.

## Parameters

| Parameter | Symbol | Units | Notes |
|---|---|---|---|
| Magnitude | E | kN/m | per metre along the section direction |
| Inclination | δ | ° | δ=0° horizontal toward the valley (unfavourable) · δ=90° vertical ↓ (weight) · δ=−90° upward (anchor reaction) |
| Load type | — | — | **Permanent** (γ<sub>G</sub>) for structural weight, or **Variable** (γ<sub>Q</sub>) for traffic/snow/accidental |

## Sign convention

- **δ = 0°**: horizontal, toward the valley (negative X direction). Typically unfavourable — destabilises the wedge.
- **δ = 90°**: vertical down (gravity-like). Acts as an extra weight applied at the centroid.
- **δ = −90°**: vertical up. Models a vertical anchor reaction (rare, but possible for cable-stayed structures).
- **0 < δ < 90°**: tilted downward toward the valley (typical for embankments).
- **90 < δ < 180°**: pushing toward the mountain — unusual, but supported.

## Components

$$E_x = -E \cdot \cos\delta, \quad E_y = -E \cdot \sin\delta$$

The minus signs follow the "load pulling the wedge toward the valley" convention. Both E<sub>x</sub> and E<sub>y</sub> enter the global F<sub>x</sub>, F<sub>y</sub> together with the other actions.

## Partial factor

- **Permanent** load → multiplied by γ<sub>G</sub> (1.00 for NTC A2, 1.35 for EC7 DA1 C1 / DA2)
- **Variable** load → multiplied by γ<sub>Q</sub> (1.30 for NTC A2, 1.50 for EC7 DA1 C1 / DA2)

## On the section

E is drawn as an orange arrow from the wedge centroid G, oriented at angle δ from horizontal. If E is much smaller than W, the arrow is artificially elongated to remain visible (minimum 50 px); the label always shows the real magnitude.

## When to use

- **Road or rail embankment** on top of the wedge: E ≈ 30–100 kN/m, δ ≈ 90° (vertical), permanent
- **Building foundation**: E from the structural design, δ ≈ 90°, permanent
- **Traffic load**: E ≈ 10–25 kN/m, δ ≈ 90°, variable
- **Snow load**: E from snow code, δ ≈ 90°, variable
- **Inclined anchor reaction** (rare): E from the anchor pull, δ between −90° and 0°, permanent
