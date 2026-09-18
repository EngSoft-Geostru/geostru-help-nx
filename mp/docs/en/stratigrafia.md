# Stratigraphies and water table

The ground is described in the **Stratigraphies and investigation verticals** card; the
water table has its own card. The surcharge at ground level q~pc~ is in the **Pile** card.

## Investigation verticals

Each stratigraphy is a **vertical**: a borehole, a test, a design profile. The **Vertical**
button adds as many as you need.

The **Investigation vertical** box decides whether the stratigraphy enters the calculation.
For each marked vertical the program computes the ultimate load; the number n of verticals
sets the correlation factors ξ~3~ and ξ~4~, and the characteristic resistance is
R~k~ = min(Q~mean~/ξ~3~, Q~min~/ξ~4~). Unmarked stratigraphies are used for the drawing
only.

If no stratigraphy is marked, the program uses the first one and says so in the messages.

## Layer parameters

Each row is a layer, from top to bottom. The arrows move the row, then come **Duplicate**
and **Delete**; the small coloured square picks the colour in the drawing.

| Column | Meaning | Unit |
|---|---|---|
| **s** | thickness | m |
| **γ** | unit weight | kN/m³ |
| **γ~sat~** | saturated unit weight, used below the water table | kN/m³ |
| **φ** | friction angle | ° |
| **c** | effective cohesion c′ | kPa |
| **α** | adhesion: multiplies the cohesion in the shaft resistance (α·c) | – |
| **E** | elastic modulus of the soil, used by the Poulos and Davis settlement | MPa |

The arrow at the start of the row opens the **Layer properties**: Poisson's ratio ν and the
oedometric modulus E~ed~ (needed by the Chiarugi-Maia subgrade modulus in the
[FEM](fem.md)), the undrained shear strength c~u~, the rock strength R~c~ and RQD, and three
boxes.

![Stratigraphies and investigation verticals card with one vertical of two layers, and the Water table card below](img/04-stratigrafie.png)

### Undrained condition

With **Undrained condition** the layer is computed with φ = 0, c = c~u~ and the saturated
unit weight. At the base N~q~ = 1 and N~c~ is that of the chosen method for φ = 0 (9 with
Berezantsev); along the shaft the resistance is α·c~u~.

**c′ and c~u~ are two separate fields.** Column **c** is the effective cohesion, used in the
drained condition; **c~u~** sits in the layer properties and is enabled by the box. So one
layer keeps both values and you can switch between conditions without retyping them.

!!! note "Files saved before September 2026"
    In an undrained layer with c~u~ = 0 the program uses the value of column **c**. This
    serves projects saved when there was a single field, which would otherwise change their
    results on their own. In new projects enter c~u~ in its own field.

### Rock layer

**Rock layer** enables **R~c~** (uniaxial compressive strength, in MPa) and **RQD** (in %).
The frictional term is cancelled and the shaft resistance is τ = α·R~c~ᵏ, with the exponent
k entered in the **Code and partial factors** card (field **k rock**). When the toe is in
rock, Q~p~ = A·R~c~·k~sq~·d~r~, with d~r~ a depth factor and k~sq~ from the RQD:

| RQD [%] | > 90 | 75–90 | 50–75 | 25–50 | ≤ 25 |
|---|---|---|---|---|---|
| k~sq~ | 1.00 | 0.75 | 0.30 | 0.10 | 0.05 |

### Negative skin friction

With **Negative skin friction** the layer drags the pile downwards: it does not contribute
to the shaft resistance and its adhesion is subtracted from the net ultimate load. In the
**Ultimate load** tab the subtracted value is shown in brackets next to Q.

## Water table

In the **Water table** card choose **Present** and enter the **Water table depth** from
ground level. Below the water table the program uses γ′ = γ~sat~ − γ~w~: if γ~sat~ is
missing in a submerged layer, the calculation stops with a message.

A **negative** depth puts the water level **above ground level**: all layers are submerged
and the water column γ~w~·|z| is added to the stress. This is the case of piles in a river
bed or at a quay; the "Pile immersed" example shows it with 2 m of water.

!!! warning "Water table on a layer boundary"
    The water table depth must not coincide with the boundary between two layers: the
    calculation stops. Move the water table by a centimetre or split the layer.

## Surcharge

**q~pc~**, in the **Pile** card, is a uniform surcharge at ground level, in kN/m². It adds
to the effective vertical stress at the toe, σ′~v~, on which the base resistance depends.

## Paste layers

If you have the stratigraphy in a spreadsheet, use the clipboard button in the header of the
vertical. The **Paste layers** window opens: paste the copied rows, one per layer, with the
columns in this order.

```text
description; thickness [m]; γ [kN/m³]; γsat [kN/m³]; φ [°]; c [kPa]; α; E [MPa]
```

Columns may be separated by tab, semicolon or comma; decimals may use a comma. The
description is optional and missing columns keep the values of the first row. The window
shows the **Rows detected** before you confirm, and you choose whether to **append** to or
**replace** the existing layers. Properties not in the list (c~u~, R~c~, RQD, boxes) are
then completed by hand.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20MP%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mp/docs/en/stratigrafia.md).*
