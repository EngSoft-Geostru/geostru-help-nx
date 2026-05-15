# Wedge geometry

The wedge is a 2D rigid body analysed per metre of development along the crest.

## Frame and notation

| Symbol | Meaning |
|---|---|
| **O** | toe of the slope, origin of the coordinate system (0, 0) |
| **+X** | toward the mountain (intact rock) |
| **+Y** | vertical, upward |
| **B** | crest of the slope face |
| **C** | top of the failure plane on the upper bench |
| **D** | top of the tension crack (only with TC) |

## Input parameters

| Parameter | Symbol | Units | Notes |
|---|---|---|---|
| Slope height | H | m | from toe O to crest B |
| Slope face dip | β | ° | typically 60–90° for rock |
| Failure plane dip | α | ° | from horizontal; must satisfy α < β (daylighting) |
| Upper face dip | ψ | ° | 0 = horizontal bench; positive = rising toward the mountain |
| Block depth | B | m | length perpendicular to the section; scales results to totals |

## Tension crack (optional)

Toggle to define a TC and fill in:

- **T** — distance of the TC from the crest [m]
- **θ** — crack dip [°] (90° = vertical, 70° = back-tilted, etc.)

The TC introduces an extra water force V in the joint (if Zt > 0) and shortens the failure plane.

## Computed geometry

The right column shows:

- **L** failure plane length (O → C without TC, O → D with TC)
- **M** upper bench length (B → C or B → D)
- **Q** tension crack length
- **A** wedge area (per metre of section)
- **(x<sub>g</sub>, y<sub>g</sub>)** centroid coordinates
- **W** weight per metre = γ · A

## α critical

Use the **α crit** button to automatically find the failure plane dip that minimises FS within the kinematically admissible range. [Read more →](alfa-critico.md)
