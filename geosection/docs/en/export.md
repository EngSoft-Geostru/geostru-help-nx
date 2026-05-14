# Export — output formats

Once the section has been computed, you can export to 4 formats: **SVG**, **PNG**,
**DXF**, **PDF**. They live in the *Export* menu of the topbar.

## SVG (Scalable Vector Graphics)

- Vector format, can be reopened in **Inkscape**, **Illustrator**, browsers.
- Keeps all geometry as separate objects: stratigraphic polygons, contact
  lines, boreholes, labels, patterns.
- Typical size: 200-500 KB for a standard section.
- **When to use**: include in editable reports for follow-up retouching
  (e.g. change colours in Illustrator without going back to the app).

## PNG

- High-resolution bitmap (default 200 dpi, configurable up to 600 dpi).
- White or transparent background.
- **When to use**: previews, PowerPoint slides, quick email attachments.
  For formal printing prefer PDF or DXF.

## DXF (AutoCAD)

- Standard CAD vector format, openable in **AutoCAD**, **DraftSight**,
  **BricsCAD**, **LibreCAD**, **QGIS**.
- Separate layers for: topographic profile, stratigraphic contacts, water
  table, boreholes, labels, legend, polygons-by-layer.
- Coordinates: in metres, local plane system (X = progressive abscissa on
  the section, Y = absolute elevation in m a.s.l.).
- **When to use**: integrate the section in a CAD drawing of the project
  (e.g. urban plan, hydraulic-work design).

## Paginated PDF

- A4 / A3 / A2 / A1 page (selectable) with configurable title block:
  - header (project title, client, date, scale);
  - section at exact metric scale (e.g. 1:200, 1:500, 1:1,000);
  - stratigraphic soil table;
  - legend at the bottom;
  - company title block (logo + studio details).
- **When to use**: final document for the technical report or as attachment
  to sub-soil reports.

## PDF title-block configuration

The title block is set in *File → Project settings → Title block*:

- **Logo**: upload PNG/JPG (suggested 300×100 px).
- **Studio details**: name, address, VAT, responsible geologist.
- **Project details**: work title, client, town, date, references.
- **Scale**: set `1:200`, `1:500`, `1:1,000` or custom.
- **Orientation**: landscape or portrait.
- **Margins**: configurable in mm.

Studio details are saved in the browser preferences and reused on subsequent
projects.

## Coordinates and elevations in exports

All formats export the section with:
- **Origin** at bottom-left (x=0, y=minimum elevation).
- **X** increasing left to right (progressive abscissa on the trace).
- **Y** increasing upwards (absolute elevation in m a.s.l.).
- Units: **metres**.

For DXF this matters because other software (e.g. AutoCAD Civil 3D) expects
coordinates consistent with the rest of the drawing.

## Print workflow example

1. Generate the section (see [Workflow](workflow.md)).
2. Configure the title block (logo, scale 1:500, A3 landscape).
3. *Export → Paginated PDF* → download the PDF.
4. Verify the scale by printing a test page: measure a known distance on the
   section and compare with the title-block scale.
5. Attach the PDF to the technical report.

For a "live" version (CAD-editable) export **DXF** for the same project too
and include it in the delivery package.
