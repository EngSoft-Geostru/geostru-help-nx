# Files, desktop projects and GeoDropbox

## The File menu

| Item | What it does |
|---|---|
| New project | clears the project |
| Open… | opens a `.hvsrnx` or `.hvsrx` file |
| Save (Ctrl+S) | overwrites the open file; if there is none, asks where to save |
| Save as… (Ctrl+Shift+S) | saves to a new `.hvsrnx` file |
| Open the example | loads the demonstration project |
| Export to CSV | **H/V curve**, **Mean spectra**, **Traces**: see [Report](relazione.md) |

If the project has changes that are not in a file, before **New project**, **Open…** or **Open the example** a strip asks **Save first**, **Continue without saving** or **Cancel**.

## Saving

The project lives in the session on the server and **disappears after 30 minutes of inactivity or at a restart**. Save it from the **File** menu: you get a `.hvsrnx` file with data,
windows, parameters, models and traces. Above 30 MB the traces remain references and the save says so.

## Opening

| Format | What it is | In HVSR NX |
|---|---|---|
| `.hvsrnx` | HVSR NX project | open and save |
| `.hvsrx` | Easy HVSR desktop project | open, from **File → Open…** or from the box in the **Traces** tab |
| `.ehv` | old binary desktop format | does not open: save it as `.hvsrx` from the desktop program |

A `.hvsrx` brings traces, windows with their selection, parameters and models. **Curves and checks are recalculated**: projects from 2011-2015 may contain curves different from those
that come out today from the same data, and the reference is the recalculation. In old projects windows may last 32 s and not be contiguous.

## Traces

| Format | Notes |
|---|---|
| `.saf` | `KEY = value` lines, then 3 columns. Order V, N, E. If the file has a non-numeric reading the app stops and tells you |
| `.txt`, `.asc`, `.csv`, `.dat` | text: you indicate row, column, separator and F~s~ |
| `.sg2`, `.seg2`, `.dat` | SEG-2 with at least 3 traces, which you assign to the components. `DESCALING_FACTOR` is not applied, irrelevant to the H/V ratio |

Other instrument formats are not read: export from there to SAF or text.

## GeoDropbox

From the **GeoDropbox** button at the top you save the `.hvsrnx` to one of your projects and open a `.hvsrnx` or `.hvsrx` from there.

## Limits

Files up to 64 MB at a time. More samples than the server can process are rejected with a message.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20HVSR%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/hvsr/docs/en/file.md).*
