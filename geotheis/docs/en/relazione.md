# Report, DXF and credits

The **Report** tab gathers your work into a Word document and the DXF drawing of the well. On the left you see what goes into the
report and the buttons to download it; on the right the **Preview**, which is free. Below the buttons is the **Continue with the
other NX apps** panel (GeoDropbox, CAD Tools, Atlante).

## What goes into the report { #che-cosa-entra-nella-relazione }

The **What goes into the report** list tells you, item by item, whether the project has the data for that chapter:

| With data | Without |
|---|---|
| Well position: map, coordinates in all systems, wells within 500 m | Well position not given: no map, coordinates or nearby wells |
| Stratigraphy and well drawing | Stratigraphy not entered |
| Step-drawdown test: characteristic curve and critical discharge | No step-drawdown test: critical discharge cannot be calculated |
| Constant-rate test: T, S and R with the transient methods | No constant-rate test |
| Piezometers: S and radius of influence from the data | No piezometer: S cannot be derived from the data |

A missing item does not block the document: the chapter is skipped or says what is missing. At least one piece of data is needed:
the position or the data of the well, the stratigraphy or a test. With an empty project the button stays disabled and the message
*The project is empty: enter at least the well position or data, the stratigraphy or a test before generating the report.* appears.

## Preview { #anteprima }

The preview is composed by the server with the same code as the Word document, on the same numbers as the [Results](risultati.md)
tab: what you read is the text you will download. The layout is indicative (*Indicative layout: Word paginates on its own.*). The
**Refresh preview** button recomposes it after a change. The «Calculation code» block is only in the Word document.

## The Word document { #il-documento-word }

**Generate Word** downloads the `.docx` report in the interface language (Italian or English). In the English document the texts
written by the calculation engine (method names, reasoning, warnings) stay in Italian, and the cover page says so.

The chapters, in order:

1. **Cover page** with the title *Pumping test report*, the project name, client, use, location, test date and engineer; then the
   **Contents**.
2. **General data**: project, description, client, use, location, test date, contractor, engineer, notes, and the purpose of the
   report.
3. **Well location**: map extract with the well, the piezometers, the registered wells, the 500 m circle and the circle of the
   design radius of influence; the coordinates in the system you entered them in and in the others, with the datum transformation
   used; the ground elevation from the digital elevation model (TINITALY, INGV) next to the ground level elevation.
4. **Existing wells within 500 m** from the Italian national archive of subsurface investigations (Law 464/84), with code, depth,
   distance and azimuth. The archive is incomplete: «no recorded well» does not mean «no well», and the report says so.
5. **Well, aquifer and stratigraphy**: well data, aquifer type and elevations, saturated thickness H~1~ or aquifer thickness b,
   measured levels, stratigraphy, completion (borehole, casing, annulus, well head chamber, pump), piezometers and the figure of the
   well section with the cone of depression.
6. **Test data**: tables of the discharge steps, of the constant-rate test (discharge, duration, pump stop), of the pumping and
   recovery readings and of the stabilised drawdowns. If you entered a known critical discharge, it appears here with the note that
   Q~c~ and s~c~ do not come from a step-drawdown test.
7. **Test analysis**: the summary, then a paragraph for each calculated method with bibliographic reference, formulas, reliability,
   parameters (with the 95 % interval where available), values per series and charts; at the end the **Methods not applied** with the
   reason.
8. **Comparison of methods**: T, K, S and R of each method, the deviations above threshold and the reference method.
9. **Design values and allowable discharge**: proposed values with the reasoning, any values confirmed by the engineer, critical
   discharge, optimal discharge, maximum tested discharge, allowable discharge, expected drawdown and the discharge used to draw the
   cone.
10. **Summary sheet for the abstraction permit**: coordinates, wells within 500 m, well type, diameters, screened sections, static
    level, critical discharge and requested discharge, with a map extract. It is designed for the hydrogeological report of the
    permit application.
11. **References**: only the sources of the calculated methods, plus the general reference text (Kruseman & de Ridder).
12. **Calculation code (NTC 2018 §10.2)**: software title and producer, version of the app and of the calculation engine, user
    licence in the name of your GeoStru NX account, **document code**, **verification** address on geostru.ai, reference to the
    engine validation document and fingerprint of the input data.

!!! note "Note"
    The report gives the values proposed by the program and those you confirmed in the Results tab. A sentence closes the design
    values chapter: the choice of values and of the discharge to request remains the professional's responsibility.

With the document code, anyone who receives the report can verify on geostru.ai that the document was issued by GeoTheis NX with
that data.

## Well DXF { #dxf-del-pozzo }

**Well DXF** downloads the well section as DXF, in metres, with distances on a linear scale. Each element is on its own layer:
STRATI, POZZO, FALDA, CONO, PIEZOMETRI, QUOTE, TESTI, TERRENO. The button becomes active when there is something to draw (depth,
borehole, stratigraphy or screen).

The same DXF can be downloaded from the **DXF** button above the well section, in the Well tab, where you can first adjust the
discharge and time of the cone. The **PNG** of the section is free.

## Continue with the other NX apps { #prosegui-con-le-altre-app-nx }

- **GeoDropbox** → **Send to GeoDropbox**: creates a project pinned on the well, or uses one of your projects within 500 m, and
  uploads the `.geotheisnx` file into the «GeoTheis NX» folder. You can tick **Also attach the Word report**: it is paid in credits
  like the download, and a Word document already paid for is not charged again. See [Files and GeoDropbox](file.md).
- **CAD Tools** → **Open in CAD Tools**: opens the well section in CAD Tools to complete it or lay it out. It is charged like the
  DXF; a DXF already downloaded is not charged again.
- **Atlante** → **Site dossier with Atlante**: the site dossier (geology, landslides, floods, seismicity) at the well location.

## Credits { #crediti }

Data, calculation, results, charts, on-screen drawings, map and preview are free. Only three actions use NX credits:

| Action | Credits |
|---|---|
| Word report (**Generate Word**, or attached when sending to GeoDropbox) | 10 |
| Well DXF (download or **Open in CAD Tools**) | 10 |
| Message to the AI assistant | 3 |

- **A failed operation is not charged.** If the Word document cannot be composed, if the document registry does not respond or if
  the file comes out empty, no credits are charged and the message says so.
- **Regenerating the same document is not charged again**: same data, same language and same engine version give the same Word
  document, which is produced without a charge. If you change a piece of data or the language, it is a new document.
- The same applies to the DXF: a drawing identical to one already paid for is not charged again, even if you open it in CAD Tools.
- With an insufficient balance the *Not enough credits for: …* window appears, with the credits needed and the balance; the project
  stays in the session while you top up.

!!! tip "Tip"
    Check everything in the preview, which is free, and generate the Word document only at the end. If after downloading you notice
    a mistake, correct it: the new Word document is a different document and uses credits again.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20GeoTheis%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/geotheis/docs/en/relazione.md).*
