# Tutorial: complete analysis

The tutorial repeats an analysis from start to finish, with the numbers you must find at each step. It uses the recording of the example project, 1200 s at 128 Hz, which you
open from the app without any file.

!!! note "With your own file"
    The sequence is the same. Import the file in the **Traces** tab, see [Traces](tracce.md), and restart from step 2: a new project already has window length 20 s, short
    period 1 s, band 0.5–15 Hz and step 0.15, so those boxes need no change. The numbers will be your own.

## 1. Open the example

Choose **File → Open the example**, or the **Open the example** button in the empty **Traces** tab. If the open project has unsaved changes, a strip asks **Save first**,
**Continue without saving** or **Cancel**.

In the **Traces** tab you find F~s~ = 128 Hz, 153,600 samples, 1200 s. The project already has windows, parameters and a model, obtained with different choices from these: you
replace them in the following steps.

## 2. Create the windows

In the **Selection** tab enter **Window length** = 20 and leave **Overlap** = 0, **Start time** = 0 and **End time** empty. Press **Select**: you get **59 windows**.

In the **Spectral analysis** tab enter **f min** = 0.5 and **Step** = 0.15, then press **Update**. The rest is already right: f max 15, **Triangular, proportional bandwidth**
smoothing, **Width** 10 %, **Arithmetic mean**.

With these windows the curve gives **f~0~ = 5.75 Hz** and **A~0~ = 3.498**. In the **H/V spectrum** tab, with **As the desktop**, the curve is reliable (3 of 3) and the peak is not
clear (4 of 6).

## 3. Apply the filter

Go back to the **Selection** tab. In the **STA/LTA filter** enter **Short period (STA)** = 1, leave **Upper limit** = 3, **Lower limit** = 0.1 and **Consider residual windows** on,
then press **Filter**. The message says "29 windows removed, 30 left": **30 windows** remain.

Many windows drop out. See where the gaps are on the seismograms and on the stationarity map, and decide whether to recover a stretch with **Add**.

## 4. Read the spectrum

In the **Spectral analysis** tab the parameters stay those of step 2. In the **H/V spectrum** tab you now find:

| Quantity | Value |
|---|---|
| f~0~ | 5.75 Hz |
| A~0~ | 4.140 |
| Curve, **As the desktop** | 3 of 3 |
| Peak, **As the desktop** | 6 of 6 |
| Peak, **SESAME 2004 text** | 4 of 6, on the geometric curve with A~0~ = 3.633 |

Press **SESAME 2004 text** and see which criteria fail: the filter made the peak clear for the desktop, not for the text. In the report you will have to say which ones you used. To
continue, go back to **As the desktop**.

## 5. Write the model

The first layer is assumed known from a borehole. In the **Stratigraphic model** press **Automatic search**, so that limits and locks appear, and check the table. The example already
has the limits and locks of this table: you only need to rewrite the starting H and V~s~.

| Layer | H | V~s~ | Limits |
|---|---|---|---|
| 1 | 2 m, locked | 120 m/s, locked | – |
| 2 | 5 m | 200 m/s | H up to 20 m, V~s~ up to 500 m/s |
| 3, half-space | – | 500 m/s | V~s~ from 400 to 900 m/s |

Turn on **Normalise the ellipticity** above the curve, so that the two curves compare on the same scale. Press **Synthesise**: the initial misfit is **0.4180**.

## 6. Run the Search

Leave **Iterations** = 1000 and **Fixed seed** on, then press **Search**. The result:

| Quantity | Value |
|---|---|
| Layer 2 | 11.51 m at 274.4 m/s |
| Half-space | 721.2 m/s |
| Misfit | 0.1954 |
| Ellipticity peak | 6.05 Hz |

The peak is 5 % from f~0~, below the 15 % threshold beyond which the app flags it. Among the **Suggestions** the one on the model length remains: it reaches 13.5 m.

## 7. Read the category

In the **Results** box: **V~s,eq~ = 368.23 m/s**, H = 30 m, **category B**.

Stop here before writing it down. V~s,eq~ lies just over 2 % from the boundary with category C and depends on the V~s~ of the half-space, extended from 13.5 to 30 m without the
measurement constraining it. Press **Store**, change the half-space limits, repeat the Search and compare: if the models explain the curve equally well and change category, you
need independent data.

## 8. Generate the report

In the **Report** tab check the **Preview** and press **Generate Word**. **Export DXF** gives the sheet with column, profile and curve.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20HVSR%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/hvsr/docs/en/tutorial.md).*
