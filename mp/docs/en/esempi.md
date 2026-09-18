# Example projects

MP NX ships eight ready-made projects: three design examples and five validation cases,
compared figure by figure with the MP desktop program.

## How to open them

1. In the app press the **?** button at the top right and open the **Resources** tab.
2. Under **Example projects** and **Validation cases** click the project: the browser
   downloads an `.mpnx` file.
3. **File → Open** and choose the downloaded file. The app goes back to the **Parameters**
   tab with the example data.
4. Press **Calculate**.

An example is a project like any other: edit it and save it under another name.

## Design examples

### Bored pile — NTC 2018

`palo-trivellato-ntc2018.mpnx` — Bored pile Ø 0.80 m, L = 15 m, with a pad footing founded
at 1 m. **Two investigation verticals** (boreholes S1 and S2, three layers each) and water
table at 4.5 m. Combinations "SLU A1+M1+R3" and "SLE rara", M~y~ = 350 kNm assigned.

It shows the NTC chain with several verticals: ξ~3~ and ξ~4~ for n = 2, minimum and mean,
R~k~ and R~d~. The settlement is computed on the serviceability combination.

### Driven pile in clay with water table

`palo-infisso-argilla.mpnx` — Driven pile Ø 0.50 m, L = 18 m, hinged head. Two clay layers
in the **undrained condition**, the first one in **negative skin friction**, over a dense
sand; water table at 1 m. Three combinations, one of them in **tension** (F~y~ = −150 kN),
and **Okamoto seismic correction** with a/g = 0.15. Terzaghi's N~q~.

It shows how to read the negative skin friction subtracted from Q, the tension check and the
seismic reduction.

### Pile socketed in rock

`palo-in-roccia.mpnx` — Pile Ø 1.00 m, L = 12 m, with a connecting beam founded at 1.5 m.
Slope debris over two **rock layers** (R~c~ = 5 and 15 MPa, RQD = 45 and 85 %). Design code
**Eurocode 7**, Hansen's N~q~, M~y~ = 900 kNm, surcharge q~pc~ = 10 kN/m².

It shows the shaft resistance τ = α·R~c~ᵏ and the base in rock with k~sq~ from the RQD.

## Validation cases

They are transcriptions of files of the MP desktop program. They use the **Classical
theory** with global factors of 2.5. The expected results are in
[Code validation](validazione.md).

### Bowles example 16.3

`ex16-3-bowles.mpnx` — Bored pile Ø 0.30 m, 23 m in the ground and 7 m of protrusion, in
soft undrained clay (c~u~ = 12 kPa, α = 1). N~q~ assigned as zero, K = 0.8 assigned.

It has no design actions: it serves the comparison on the ultimate load. This is why the
Settlements tab stays empty. Base and shaft match the desktop; the pile weight differs by
2 % because of the concrete unit weight in the two archives.

### Bowles example 16.10

`ex16-10-bowles.mpnx` — Bored pile Ø 0.40 m, L = 15.9 m, in dense sand (φ = 32°).
Berezantsev's N~q~ with the corrected angle ¾ φ + 10°, horizontal force of 140 kN at the
head, Poulos and Davis settlement with Q = 100 kN. The file carries the assigned K~s~ of the
textbook (A~s~ = 4 927, B~s~ = 58 620, n = 1, 16 elements).

In the file the FEM analysis is off: enable it in the **Reinforcement and FEM analysis**
card to reproduce moments, shears and displacements node by node.

### Desktop Example1

`example1-desktop.mpnx` — Bored pile Ø 0.60 m, L = 12 m, three clay layers, beam founded at
1 m. Horizontal force at z = 1 m, **FEM enabled** with constant Bowles K~s~ and 9 elements,
**ULS check** with 8 Ø 16 and Ø 10 stirrups, structural code "NTC (ultimate)".

It is the most complete case: ultimate load, node-by-node FEM, section check. The materials
archive of the project reproduces the technical archive of the desktop.

### Desktop Pile immersed

`pile-immersed-desktop.mpnx` — The same pile, with **4 m above ground** and the water level
**2 m above ground level** (water table depth −2 m). Clays in the undrained condition with
c~u~ = 196 kPa. Three horizontal forces on the free length; FEM off.

It shows the total stress at the toe with the water column, and the protrusion.

### Desktop DPHS1 micropiles

`dphs1-micropiles-desktop.mpnx` — **Tubifix micropile** with a 114.3 × 10 mm tube: drill
hole Ø 0.20 m, 2 m shaft and Ø 0.40 × 6 m bulb, IRS grouting, shaft resistance with
**modified Mayer**. Three layers, two undrained, water table at 2.9 m. M~y~ = 39.68 kNm
assigned, axial load of 100 kN.

!!! note "Reinforcement weight"
    The file reproduces the desktop, which has the reinforcement weight at 0. If you pick
    the tube from the series, the **Reinforcement weight** field is filled from the geometry
    (0.252 kN/m), W rises from 20.42 to 22.44 kN and Q drops from 383.79 to 381.77 kN.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20MP%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mp/docs/en/esempi.md).*
