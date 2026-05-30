# File formats

## .dprobe — native NX format

The `.dprobe` file is the project format of Dynamic Probing NX. It is a plain **JSON** file, readable with any text editor. It contains:

- Project metadata (name, site, client, coordinates)
- List of tests with all readings
- Instrument library embedded in the file
- Interpreted stratigraphy (layers, depths, type, γ)
- Correlation settings (preferred authors)
- Computed results (correlations, subsoil category, bearing capacity, parameter estimation)

The file is **self-contained and portable**: copy it to another PC, open it in Dynamic Probing NX — everything works without additional configuration.

## .dypx — GeoStru desktop format (import)

The `.dypx` file is the text export format of the GeoStru Dynamic Probing desktop. Dynamic Probing NX can import it from the home screen with **Import .dypx…**. During import the following are read:

- All tests with blow count readings
- Instrument data (type, β if present)
- Test coordinates (if saved in the desktop file)

Stratigraphy and correlations are not imported from the desktop — they must be re-entered in NX.

## CSV datalogger

Many dataloggers for dynamic tests export data in CSV or TXT format. Dynamic Probing NX automatically recognises the format if the columns are structured as:

```
depth, blows
0.10, 8
0.20, 9
0.30, 11
...
```

Columns can be separated by comma, semicolon or tab. If the file has a header with site coordinates (lat, lon, elevation), they are read automatically.

To import: in the **Readings** tab of the editor, click **Import readings from file…** and select the CSV. Alternatively, paste the content directly into the text field of the modal.

## AGS4 (.ags)

Dynamic Probing NX exports in AGS4 format (v4.2) but does not import from AGS4. See [Export →](export.md).
