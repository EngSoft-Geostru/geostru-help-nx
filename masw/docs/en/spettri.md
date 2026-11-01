# Spectra and picking

## Computing the spectrum

Set **f min**, **f max**, **v min**, **v max** and **dv**, then press **Calcola (Compute)**. The Nyquist frequency is
shown at the top right: **f max** must stay below it. Steps too fine over wide ranges are refused with a message.

The map has frequency on the x axis and phase velocity on the y axis. Where a real wave exists a **ridge** forms: read
left to right it descends, and it is the dispersion curve you are looking for.

![f-v spectrum](img/03-spettri.png)

**Colours** and **Levels** change the drawing only, not the calculation.

## Apparent curve and regression

The maxima of each column appear over the map: blue if used, orange if excluded. The black curve is the polynomial of
the chosen **degree** (2 to 10). Maxima equal to the curve's minimum or maximum drop out of the regression by themselves.

With **Escludi (Exclude)** drag a rectangle over points to remove, **Includi (Include)** puts them back, and
**Reincludi tutti** clears all exclusions.

## Picking

The **picking** is the list of (f, v) points that enter the inversion. Each point belongs to a **mode**: 0 is the
fundamental, 1 to 4 are the higher ones.

| Tool | Gesture |
|---|---|
| **Aggiungi (Add)** | click on the map; drag vertically to widen the uncertainty bar |
| **Sposta (Move)** | drag a point |
| **Elimina (Delete)** | click on a point |
| **Automatico (Automatic)** | **N. points** on the ridges of the map, also on several modes |
| **Nuova selezione (New selection)** | clears the picking, after confirming on the page |

Below the chart you read f, v and the wavelength λ = v/f at the cursor.

!!! warning "Picking is your choice"
    **Automatic** follows the ridges of the map, not the physics. Check it on the map: taking a higher mode for the fundamental
    overestimates V~s~.

## The table

**Curva di dispersione (Dispersion curve)** lists the points of the current mode. You can correct f, v and mode; Del on a
cell removes the row. Pasting rows `f⇥v` or `f⇥v⇥mode` from Excel **replaces the whole picking**. **Copy** sends the points
to the clipboard.

## Synthetic model

Write a trial layered profile and **Mostra curve (Show curves)** draws the curves it would produce over the map. It helps
judge at a glance whether a profile is plausible.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20MASW%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/masw/docs/en/spettri.md).*
