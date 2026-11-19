# Formats and data exchange

## SPW NX project: `.spwnx`

The `.spwnx` is the native project file. It contains inputs: general data, site, ground, wall, elements, combinations, stages, options and import report.

It does not store calculation results. Calculate again after opening. A newer program version may therefore produce different results according to the documented validation.

Use **File → Save** to update the current file. Use **Save as…** to create a new one.

## Desktop project: `.spwx`

The `.spwx` is opened read-only with **File → Open…**. SPW NX creates a native project and a report of the choices made.

To keep the imported result, save a `.spwnx`. The desktop file remains unchanged. See [Desktop import](importazione-desktop.md).

## Word report

The report is a `.docx` document with project data, up-to-date results, checks, reinforcement and the “Calculation software” block. It includes combination exceptions and the import report when present. The document properties carry the author and the data fingerprint.

It is generated from the **Report and export** step only with a complete and current calculation and costs 10 credits. The **Free preview** shows the same content on screen. The report is in the interface language.

## DXF drawing

The `.dxf` transfers the wall or results drawing to a CAD program. From the **Report and export** step choose the full drawing (section, stages and envelopes) or the wall section only. **DXF · 10 credits** in the Results step exports the diagram on screen.

A view without content produces no file and uses no credits. Check that the drawing refers to the intended combination and stage.

## CAD Tools

The **CAD Tools** button of the Report and export step takes the wall views to the editing environment, in a new tab. The operation uses the same rate as DXF.

## Computo NX and PDM NX

The **Computo NX** and **PDM NX** buttons of the Report and export step take the project to the bill of quantities and to the maintenance plan. Before the transfer to Computo NX you can open **Quantity parameters and preview**, check the quantities and untick the items you do not need. The links do not replace checking the transferred data.

## Entry from Atlante NX

From an Atlante NX dossier you can open SPW NX with the site position already chosen. If the project has no position, it receives it at once with a notice. If it already has a different one, the Report and export step asks whether to replace or keep it. After replacing it, request the site seismic parameters again.

## GeoDropbox

The **GeoDropbox** button opens and saves the `.spwnx` in a GeoDropbox project. Saving the project is free. If you choose to attach a paid report, the report rate applies.

## Units and contents

The project uses SI units. Elevations and lengths are in metres, forces in kN, pressures in kPa and unit weights in kN/m³. Bars and tubular sections have dimensions in millimetres where indicated.

Elevations are absolute and positive upwards. Many results refer to one metre of wall. Section checks report values per element instead.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/spw/docs/en/formati.md).*
