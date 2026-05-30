# Export and report

## Word report (.docx)

The Word report is the complete calculation report, ready to be attached to the project documentation. It is generated from the **Export → Report** menu.

The document includes:

- Header with site data (name, client, coordinates, date)
- Instrument sheet: type, technical parameters, β used
- Blow count N/depth profile (chart)
- Stratigraphy table: layers, depths, soil type, N_SPT per layer
- Geotechnical correlations table for each layer (selected authors)
- Subsoil category: V_s,eq, assigned category, layer table
- Foundation bearing capacity (if computed): comparative method table
- EC7 / NTC §6.2.2 characteristic values (if computed)

## AGS4 (.ags)

The **AGS4** format is the open standard for geotechnical data exchange (AGS Data Format v4.2). Export it from **Export → AGS4** to share test data with other software or with the client.

Groups included in the AGS4 export: TRAN, PROJ, LOCA, GEOL, DPRG (dynamic test parameters), DPRB (readings).

## GeoSection (.geosection)

Export tests with their interpreted stratigraphy to **GeoSection NX** to build the geological section. From **Export → GeoSection**: select the tests to include (those with coordinates), click **Export**. The `.geosection` file opens directly in the GeoSection app.

## Site plan (PNG image)

If tests have coordinates assigned, **Export → Site plan (image)** produces a PNG image of the site plan with the position of the tests, elevations and distances between tests. Available only with at least 2 georeferenced tests.

## KMZ (Google Earth)

The **Export → KMZ** menu generates a file viewable in Google Earth with the position of all georeferenced tests in the project.

## Project file (.dprobe)

The `.dprobe` file is the native format of Dynamic Probing NX — a human-readable JSON containing all project information (tests, instruments, stratigraphy, correlations, site data). It is saved from **File → Save** and reopened from the Home with **Open file…**.

!!! tip "Desktop compatibility"
    You can import a `.dypx` file (text format from the GeoStru Dynamic Probing desktop) from the Dynamic Probing NX Home. The NX `.dprobe` file cannot be opened with the desktop version.
