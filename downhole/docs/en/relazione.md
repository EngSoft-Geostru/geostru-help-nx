# Report, DXF and credits

The **Report** tab produces the two deliverables of the test: the **Word report** and the
**DXF drawings** of the charts. Together with messages to the assistant, these are the
actions of the app that use credits. The **preview** of the report, on the right, is free.

![Report tab: on the left the five sections that can be switched on and the summary of what the document will contain, on the right the paginated preview that opens with the general data](img/21-relazione.png)

## Before you generate

Check three things, all free:

1. the fields of the **General data** tab (client, site, location, date, operator, person
   in charge, description, notes, WGS84 coordinates and altitude): they open the document;
2. the seismic layers and V~s,eq~ in the [Processing](elaborazione.md) tab;
3. the **What the report will contain** box: number of measurements, seismic layers of both
   methods, descriptive layers, figures and V~s,eq~ of both methods.

Then look at the **preview**: it is the document as it will come out.

If the measurements are missing or contain errors, **Generate Word** is disabled and a note
says what to fix.

## The preview

The **Report preview** card shows the document laid out page by page, with the same texts,
tables and figures as the Word file: the server composes it with the same code. It follows
the section switches as soon as you change them, even before you save them.

Compared with the Word file only the **page numbers** and the **Calculation software** block
are missing; the block exists only in the issued document (see below). The preview uses no
credits.

## How the report is organised

The document has no cover page. In order:

1. **General data** — the table with the fields of the General data tab, including latitude
   and longitude (WGS84) and altitude in m above sea level. Empty fields are left out; if
   they are all empty, the document starts from the next chapter;
2. the chosen **sections** (table below) and the **processing of the measurements**, the
   table of corrected times, which is always there;
3. **Calculation software** — the block that identifies the software and the document;
4. the **contents**, at the end.

## Report sections

Five switches choose what to include.

| Section | Content |
|---|---|
| **Theoretical notes** | The test, the procedure, the two methods, the elastic parameters, V~s,eq~, the limits and the references. |
| **Input data (geometry, measurements, test layout)** | Geometry, table of measured times, test layout. |
| **Direct method (seismic layers, parameters, travel-time curves)** | V~s,eq~, seismic layers, parameters per layer, travel-time curves. |
| **Interval method (values per receiver, averages, five profiles)** | V~s,eq~, parameters per measurement interval, seismic layers and average values, the five profiles (velocity, γ, ν, G·E~d~, E·E~v~). |
| **Stratigraphy (water table, layers, column)** | Water table, layers and column. Included only if the Stratigraphy tab has at least one layer. |

The options are saved with the project: press **Save options**, or switch tab and the app
saves them for you.

## Generate Word

**Generate Word** produces a `.docx` file and the browser downloads it.

- The report is written **in the interface language**: to have it in English, switch
  language from the selector at the top before generating it.
- The figures are the same drawings you see on screen.
- On opening, Word may ask to update the fields: accept, and the table of contents gets its
  page numbers. Otherwise right-click the contents → **Update field**.
- Values that cannot be computed stay “--”, as on screen; the warnings of the calculation
  are reported in the document.

The document is an ordinary Word file: you can edit it, add your logo, convert it to PDF
from your word processor.

### The “Calculation software” block

The last chapter of the report, **Calculation software** (in the Italian report *Codice di
calcolo (NTC 2018 §10.2)*), is a table written by the software with what section 10.2 of the
Italian building code asks to state:

- title of the software and producer;
- app version, version of the **calculation engine** and code revision;
- licence of use, in the name of whoever generated the document;
- **document code**, in the form `NX-…-XXXX-XXXX`, and the address where it can be checked;
- the reference to the [validation](validazione.md) of the engine;
- the fingerprint of the input data.

The code is registered on geostru.ai when you generate the Word file: anyone who receives
the report can check, at the address printed in the block, that the document was issued by
Downhole NX with that version. The check says that the document was **issued**, not that the
input data are correct: those remain the responsibility of whoever signs.

If the document register does not respond, the report **is not produced** and nothing is
charged: try again in a few minutes.

## DXF drawing

In the **DXF drawing** card choose the **Drawing to export** and press **Export DXF**:

- Test layout
- Travel-time curves and seismic layers of the direct method
- Interval velocity profile
- Interval unit weight profile
- Interval Poisson's ratio profile
- Interval G and Ed moduli profile
- Interval E and Ev moduli profile
- Stratigraphic column

Each export produces **one** drawing, with one layer per role (axes, grid, points,
travel-time curves, layers, dimensions, texts), in the same units and colours you see on
screen. Texts are in the interface language.

If the chosen drawing is empty (for instance the stratigraphic column with no layers), the
app says so and exports nothing.

## Credits

### What uses them

| Action | When it is charged |
|---|---|
| **Generate Word** | Once the document has been produced. |
| **Export DXF** | Once the file has been produced. |
| **Message to the assistant** | When the answer arrives. |

### What is free

Uploading traces, picking times, filling in the measurements, processing, inserting and
moving seismic layers, viewing all charts and tables on screen, filling in the stratigraphy,
viewing the report preview, saving and opening the project, opening the examples.

### How much they cost

This manual does not quote prices: they change with the price list, published on
[geostru.ai](https://www.geostru.ai/). Your **balance** is in the user menu, at the top
right.

If the balance is not enough, the app generates nothing and shows a strip with the **credits
needed**, the **balance** and the **Buy credits** button. The project stays in the session:
top up and try again.

### If something goes wrong

**If an operation fails, nothing is charged.** That holds for every case the app can run
into:

- an error while generating the Word or the DXF file;
- invalid measurements or an empty drawing;
- expired session: the app says so and neither writes nor charges anything;
- credit service or document register unreachable: try again in a few minutes;
- assistant not available, or answer not received.

The full conditions (validity of credits, refunds) are in the
[Terms of Service](https://geostru.ai/en/terms-of-service/).

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Downhole%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/downhole/docs/en/relazione.md).*
