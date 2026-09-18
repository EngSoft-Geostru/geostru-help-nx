# Ultimate load

MP NX computes the ultimate vertical load with **static formulae**, for each investigation
vertical and each combination, then applies the ξ factors and the γ~R~ factors. This page
explains the choices in the **Pile** card and how to read the **Ultimate load** tab.

## Net ultimate load

In **compression**:

Q = Q~p~ + Q~s~ − W − Q~neg~

with Q~p~ the base resistance, Q~s~ the shaft resistance, W the pile weight and Q~neg~ the
adhesion of the layers in negative skin friction. In **tension** the base does not work:
Q = Q~s~ + W.

## Base resistance

Q~p~ = A·(σ′~v~·N~q~ + c·N~c~), with σ′~v~ the effective vertical stress at the toe,
including the surcharge q~pc~. N~q~ and N~c~ depend on the **Method for N~q~**:

| Method | N~q~ | N~c~ |
|---|---|---|
| **Berezantsev** | function of φ and L/D; for D > 0.8 m interpolation on L/D | (N~q~ − 1)/tan φ; 9 for φ = 0 |
| **Berezantsev (L/D = 32)** | 0.48·exp(4.97·tan φ) | as above |
| **Terzaghi** | Terzaghi's formula (1943) | (N~q~ − 1)/tan φ, minimum 5.7 |
| **Janbu** | function of φ and of the relative density D~r~ (ψ = 60° + 0.45·D~r~) | (N~q~ − 1)/tan φ; 5.74 for φ = 0 |
| **Hansen** | exp(π·tan φ)·tan²(45° + φ/2) with shape and depth factors | with the same factors; 5.14 for φ = 0 |
| **Vesic** | function of φ and of the rigidity index I~r~ = 1.7·D~r~ | (N~q~ − 1)/tan φ |
| **N~q~ utente** (user value) | the value of the **N~q~ assigned** field | (N~q~ − 1)/tan φ; 9 for φ = 0 |

With Janbu and Vesic the **D~r~** field appears, the relative density in %. The full
formulae and the control values at φ = 30° are in the [validation document](validazione.md).

The **Friction angle for the shaft resistance** field corrects φ before the calculation: φ,
φ − 3° (bored), ¾ φ + 10° (driven) or (φ + 40°)/2. The corrected angle also enters N~q~: in
Bowles' example 16.10, φ = 32° becomes 34° at the toe.

## Shaft resistance

Q~s~ = π·D·Σ (K·tan δ·σ′~v,mean~ + α·c)·t, summed over the layers of thickness t.

- **Earth pressure coefficient K**: 0.5; 1; 1 − sin φ; 1 − tan² φ; or **User value**.
- **Soil-pile friction angle**: δ = φ, ⅔ φ, ¾ φ, 20° or 25°.
- **α** and **c** (or **c~u~**) come from the [layer](stratigrafia.md).

In rock layers the frictional term is zero and τ = α·R~c~ᵏ. The adhesion above the founding
plane of the footing is removed. For tapered driven piles the taper factor F~w~ applies.

!!! note "K is computed with the unreduced φ"
    With K = 1 − sin φ or 1 − tan² φ the program uses the friction angle of the layer, not
    the one reduced by the M factors or corrected for driving. It is the behaviour of the
    desktop program, declared in the validation document.

## From Q to R~k~ and R~d~

For each combination the program computes Q~p~ and Q~s~ on all the verticals, then:

1. takes minimum and mean, and with ξ~3~ and ξ~4~ obtains **R~k,p~** and **R~k,s~**;
2. divides by γ~b~ and γ~s~ and subtracts the weight:
   **R~d~ = R~k,p~/γ~b~ + R~k,s~/γ~s~ − W**;
3. compares with the action: **FS~v~ = R~d~/|E~d,v~|**.

The weight W is that of the first vertical. The factors are described in
[Loads, combinations and design code](combinazioni.md).

## Ultimate lateral load (Broms)

H~max~ is computed with **Broms'** method, in Viggiani's formulation: cohesive soils (with
c~u~) and cohesionless soils (with Rankine's K~p~), **free or fixed head** according to the
**Head restraint** in General data. The mechanism depends on the ultimate moment of the
section M~y~ and is shown in the table as **Short pile**, **Intermediate pile** or **Long
pile**.

Where M~y~ comes from:

- if you enter **M~y~** in the Materials and reinforcement card, your value prevails;
- if M~y~ = 0 and the **FEM analysis is enabled**, the ultimate moment of the reinforced
  section at N = 0, computed by the program, is used;
- for the **tubular micropile** with M~y~ = 0 the moment of the composite tube + grout
  section is used;
- if M~y~ = 0 and the FEM is off, the lateral check is not performed.

The design resistance is R~d,h~ = R~k,h~/γ~T~ and the check FS~h~ = R~d,h~/E~d,h~.

## Seismic correction

With a/g > 0 in the **Seismic action** card the ultimate load is reduced with one of three
methods:

| Method | Correction |
|---|---|
| **Vesic** | φ reduced by 2° |
| **Okamoto** | base and cohesive shaft term multiplied by 1 − a/g |
| **Sano** | φ reduced by atan(a/(g·√2)) |

Vesic and Sano restart from the unreduced angle φ: with the M2 factors the reduction of φ is
not cumulated. This too is declared in the validation document.

## Reading the Ultimate load tab

At the top is the outcome, **Check satisfied** or **Check NOT satisfied**, with the
**Governing combination**, that is the one with the lowest safety factor. The four tiles
report R~d~, E~d~, R~k~ and the **Safety factor** on a scale from 1 to 3.

Then comes one card per combination. The header says whether it is in **Compression** or
**Tension** and reports E~d,v~ and E~d,h~. The table has one row per vertical:

| Column | Meaning |
|---|---|
| N~q~, N~c~ | bearing capacity factors used |
| φ~p~, c~p~ | friction angle and cohesion at the toe, after corrections and factors |
| σ′~v,p~ | vertical stress at the toe |
| Q~p~, Q~s~, W | base, shaft, pile weight |
| Q | net ultimate load; in brackets the negative skin friction subtracted |
| H~max~, Mechanism | Broms' ultimate lateral load and mechanism |

Below the table, four groups: **Investigation verticals** (n, ξ~3~, ξ~4~, minimum, mean and
maximum of Q~p~ and Q~s~), **Characteristic resistances**, **Design resistances** with γ~b~,
γ~s~ and FS~v~, and **Ultimate lateral load (Broms)** with FS~h~. Any messages from the
calculation appear at the bottom.

![Ultimate load tab: outcome, governing combination, R_d, E_d, R_k and FS tiles, and the table of verticals](img/10-carico-limite.png)

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20MP%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mp/docs/en/carico-limite.md).*
