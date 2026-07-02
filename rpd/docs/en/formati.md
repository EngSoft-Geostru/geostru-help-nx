---
title: File formats and export
---

# File formats and export

## Project: `.rpdnx` file

An RPD NX project is saved as an **`.rpdnx`** file (JSON format) that contains all the data: general data, geometry, layering, subgrade, traffic, geogrid and method.

From the **File** menu:

- **New** — starts from an empty project (asks for confirmation if there are unsaved changes);
- **Open** — loads an `.rpdnx` from your computer;
- **Save** — downloads the project as `.rpdnx`.

!!! note "«Unsaved» badge"
    When you change the data, the **Unsaved** badge appears next to the menus. Before *New* or *Open*, RPD NX warns you if there are unsaved changes. The badge disappears after saving.

## GeoDropbox

With **GeoDropbox** (the icon in the top bar) you save and reopen projects from the **GeoStru cloud**, so you can find them again from any device.

## Calculation report

From the **Report** menu you generate the complete calculation document:

- **Word (.docx)**
- **PDF (.pdf)**

The report includes the project data, the method, the results and the verification quantities.

## Exporting the cross-section

From the **Export** menu:

- **Project (.rpdnx)** — the same as saving;
- **2D cross-section (.svg)** — the vector drawing of the cross-section, reusable in other programs or in the report.

## Sample projects

From the app's info modal (**?** menu → *Resources*) you can download ready-made sample projects:

- `aashto.rpdnx` — example with the empirical AASHTO 1993 method;
- `ivanov.rpdnx` — example with the rational Ivanov method.

Open them with **File → Open** to explore a real case.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20RPD%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/rpd/docs/en/formati.md).*
