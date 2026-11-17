# Files, desktop projects and GeoDropbox

## The project lives in the session { #il-progetto-vive-in-sessione }

The project you are working on is on the server, in your session, and expires after **30 minutes of inactivity**. As long as the
browser tab stays open the session stays alive. If you close it, or leave it idle beyond the limit, the project is no longer in
memory: *The session has expired and the project is no longer in memory: reopen the saved file. Nothing was written or charged.*
appears.

To avoid losing your work, save it to a `.geotheisnx` file or to GeoDropbox.

## The File menu { #il-menu-file }

| Command | What it does |
|---|---|
| **New project** | clears the project; if there are changes that are not in a file it asks you first |
| **Open…** | opens a GeoTheis NX `.geotheisnx` file or a `.wtax` from the desktop program |
| *Examples* | opens a sample project (see below) |
| **Save** (Ctrl+S) | rewrites the open file; if there is none, asks where to save |
| **Save as…** (Ctrl+Shift+S) | saves the project to a new `.geotheisnx` file |

Next to the menu is the name of the file **Save** writes to. If the browser does not let you rewrite that file, *The browser did not
allow writing to the file: use «Save as».* appears.

## The `.geotheisnx` file { #il-file-geotheisnx }

It is a JSON text file, in SI units, that contains **only the input data** and your choices: well, site, stratigraphy, completion,
piezometers, test readings, excluded points, Cooper-Jacob intervals, type-curve adjustments, chosen critical discharge, confirmed
values. The results are not in the file: they are recalculated on opening, so an old file opened with a new version of the engine
gives the results of the new version.

A project file can be opened up to 8 MB.

## Desktop program projects (`.wtax`) { #progetti-del-programma-desktop-wtax }

**Open…** also accepts `.wtax` projects from GeoTheis desktop. After opening, *Desktop program project opened: check the data before
calculating.* appears, with the import notes.

What is imported:

- well and aquifer type, elevations (ground level, well head, static level, top and base, semi-pervious layer), radius and geometry
  of the well; the completion is proposed from the calculation scheme;
- drawing description (it becomes the project description) and view options;
- stratigraphy, with the soil name mapped to the catalogue;
- piezometers, named P1, P2… in the desktop order;
- discharge steps, pumping and recovery readings, stabilised drawdowns;
- the choices made in the desktop: critical discharge, reference discharge for the efficiency, method and assumed radius of the
  single wells, assumed Dupuit-Thiem radius, Theis and Hantush match points.

Discharges in m³/h and times in hours, minutes and seconds are converted to SI units. Zeros that in the desktop meant «no data»
(coordinates 0, 0; stabilised drawdowns, Q~c~, assumed radii at zero) become empty fields.

!!! warning "Warning"
    **The results saved in the `.wtax` are not imported**: GeoTheis NX recalculates everything with the correct literature formulas.
    For this reason the numbers may differ from those you read in the desktop. The differences and their reasons are in
    [Validation](validazione.md).

Notes you may find after opening:

- *The file does not state the well and aquifer type: they must be chosen before the calculation.* Choose them in the
  [Well](pozzo.md) tab.
- The desktop's «semilibera» or «semiartesiana» aquifer becomes *leaky (unconfined)* or *leaky (confined)*.
- **Recovery**: if the times in the file counted from the start of pumping, they are shifted to the pump stop; if the stop time is
  missing, the last pumping reading is assumed. The note says which rule was applied.
- Drawdowns in columns without a piezometer (piezometers removed in the desktop) are not imported; empty rows are ignored.
- Layers with a hatch taken from an image on the author's PC: the drawing uses the standard hatch of the soil. Unrecognised
  lithologies: generic hatch, to be corrected in the stratigraphy.
- *Constant-rate test: there are readings but the discharge is 0: it must be entered.*

Import limits:

- the desktop coordinates are **local coordinates**, not geographic: after opening, place the well on the map in the
  [Well](pozzo.md) tab if you need the map, nearby wells and the permit summary sheet;
- the desktop's stabilised drawdowns exist only for the well and for the first two piezometers;
- a file that is not a valid `.wtax`, or is truncated, does not open and the project in the session stays as it was;
- the file to open cannot exceed 32 MB (a real `.wtax` weighs a few kB).

## GeoDropbox { #geodropbox }

The **GeoDropbox** button in the top bar saves the project (the `.geotheisnx`) to one of your GeoDropbox projects, or opens a
`.geotheisnx` or a `.wtax` saved there.

From the [Report](relazione.md) tab, **Send to GeoDropbox** goes one step further: it creates a GeoDropbox project pinned on the
well, with the municipality and the general data, or uses one of your projects within 500 m of the well. The `.geotheisnx` file goes
into the «GeoTheis NX» folder and can be reopened from the GeoDropbox → Open button. A second send updates the same project
(**Update on GeoDropbox**). If the well has no coordinates the project is created without a pin.

Saving or sending to GeoDropbox is free; only the Word report costs credits, if you choose to attach it.

## Examples { #esempi }

From the **File** menu you open the sample projects of the desktop program. They open like a `.wtax`, with the same import notes.

- **Examples with tests**: projects with steps or a constant-rate test. The first is **CELICO**, a fully penetrating well in a confined
  aquifer with steps, constant-rate test, recovery, two piezometers and stabilised drawdowns (see the example in
  [Results](risultati.md#esempio)).
- **Single wells (known critical discharge)**: eight examples with only the well geometry, fully or partially penetrating, in the
  different aquifer types. When opened from the menu, their empty fields receive the desktop example values: Q~c~ 100 m³/h, s~c~ 5 m,
  R 150 m, in the [Test](prove.md) tab, where you can change them.

!!! note "Note"
    The example data are built to exercise the calculation, they do not describe a real aquifer. For instance in CELICO the P2
    readings are those of P1 multiplied by 0.4.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20GeoTheis%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/geotheis/docs/en/file.md).*
