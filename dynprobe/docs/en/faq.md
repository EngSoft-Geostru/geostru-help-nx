# Frequently asked questions

## General

??? question "What is the difference between Dynamic Probing NX and the Dynamic Probing desktop?"
    The GeoStru Dynamic Probing desktop is the historical Windows version. Dynamic Probing NX is the web version, accessible from any browser without installation. The main features are equivalent; NX adds multi-test support (management of an entire site with N tests), the interactive map, AGS4 export and integration with GeoSection NX. Desktop data can be imported into NX via the `.dypx` format.

??? question "Is data saved on the server?"
    No — Dynamic Probing NX is **local-first**: project data resides in your browser (localStorage) and is saved to your PC only when you export the `.dprobe` file. No project data is sent to GeoStru servers.

??? question "Can I use it offline?"
    An internet connection is required for the initial loading of the app. Once loaded, the app also works offline for data entry and calculations (except for generating the Word report, which requires a connection).

??? question "Is there a mobile version?"
    The app is designed for desktop/tablet. On smartphones navigation works but entering readings on very small screens is inconvenient.

## Instruments and readings

??? question "How do I add an instrument that is not in the catalogue?"
    Go to **Instruments** from the navigation bar → **+ Add instrument**. Enter: name, type (DPL/DPM/DPH/DPSH), hammer mass (kg), drop height (m), cone diameter (mm), cone angle (°), advancement step (m), and the β coefficient. The instrument is saved in the project file.

??? question "My CSV is not recognised correctly. How should I format it?"
    Make sure the first two columns are depth (m) and blow count (integer), separated by comma, semicolon or tab. Remove header rows that do not follow this format, or enter them as comments with `#` at the beginning of the line. If coordinates are in the header, use the format: `# lat=41.9028 lon=12.4964 elevation=120`.

??? question "Can I exclude readings from the calculation?"
    Yes — in the Readings tab, each row has a checkbox to exclude it. Excluded readings do not enter the N_SPT aggregation per layer or the correlations. Useful for discarding anomalous values (early refusal, drilling fluid loss).

## Stratigraphy

??? question "How do I choose the N_SPT aggregation method?"
    It depends on the objective. For a conservative mean estimate use **Mean − 1σ**. For the EC7 characteristic value use **RNC** (normal distribution) or **RC** (log-normal). If you have few readings per layer (< 4), prefer simple Mean or Minimum. See [Stratigraphy →](stratigrafia.md) for the complete description of the 7 methods.

??? question "The Σ layers badge is yellow — what does it mean?"
    The sum of the lower depths of the layers does not match the test depth. Check that the last layer reaches exactly the depth at end of test (e.g. if the test is 12.00 m, the lower boundary of the last layer must be 12.00 m).

## Correlations

??? question "Why are some correlation values shown as —?"
    For some soil type / author combinations the parameter is not defined. For example, Dr (relative density) is only defined for non-cohesive soils: in cohesive layers the cell shows —. Similarly, Cu (undrained cohesion) is only defined for cohesive soils.

??? question "Can I enter laboratory values instead of correlations?"
    Currently the app uses N_SPT correlations as the primary source. For bearing capacity calculation you can enter Cu or φ directly in the layer fields in the stratigraphy — those values replace the correlated ones.

## Export and report

??? question "Is the Word report editable?"
    Yes — it is a standard `.docx` file opened in Word, LibreOffice or Google Docs. You can customise the header, add your firm's logo and edit the descriptive text. The numerical tables are static data (not Excel formulas).

??? question "Can I export to PDF?"
    Not directly from the app. Open the generated `.docx` in Word and use **File → Print → Save as PDF**.

??? question "AGS4: which groups are exported?"
    The following groups are included: TRAN (transmission data), PROJ (project), LOCA (test locations), GEOL (stratigraphy), DPRG (dynamic test parameters), DPRB (blow count readings). Correlations and bearing capacity are not exported — these processed results are not part of the AGS4 standard for dynamic tests.
