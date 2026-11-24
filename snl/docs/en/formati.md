# Formats

## SNL NX project (.snlnx)

The working format. It contains **only the inputs**: general data, design office, site and seismic parameters, geometry, layers, water table, loads, nails, factors, kh and kv, and the import report if the project comes from a `.snl`. Results are not saved: they are recalculated after opening, free of charge.

- **File → Save** overwrites the open file; if there is none, it asks where to save;
- **File → Save as…** creates a new `.snlnx` file;
- **File → Open…** opens a `.snlnx` or a `.snl`.

The name of the file that «Save» writes to appears in the bar.

## .snl files

SNL `.snl` projects open with **File → Open…** and are converted into the SNL NX model with an import report. SNL NX does not write `.snl` files. See [Importing](importazione.md).

## Word report (.docx)

From the **Report and export** step, with a complete and up-to-date analysis. It contains the project data, the assumptions, the results by stage and by nail, sliding, the drawings and the **«Calculation code»** block required by §10.2 of NTC 2018: application, version, calculation engine, validation and a **document code** that can be checked on geostru.ai. It uses 10 credits.

## DXF drawing

The wall section to scale, with separate layers for wall, facing, soil, water table, loads, nails, dimensions and texts. The file carries the GeoStru signature in comments, ignored by CAD programs. It uses 10 credits.

## GeoDropbox

With the **GeoDropbox** button you save the `.snlnx` project to a GeoDropbox project and open it from there, also from another computer.

## On-screen drawing

The drawing in the centre (section and result views) is free and updated at every change. You do not need to download anything to check the model.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/snl/docs/en/formati.md).*
