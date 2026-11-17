# GeoTheis NX

**GeoTheis NX** interprets **pumping tests** on water wells: the step-drawdown test and the constant-rate test with recovery,
measured in the pumped well and in the piezometers. From the data it derives the aquifer parameters, transmissivity (T),
hydraulic conductivity (K), storativity (S) and radius of influence (R), proposes the **allowable discharge** and writes the
Word report.

While you describe the well, the section is drawn live next to the fields: stratigraphy, casing, screens, water levels and cone of
depression.

[**Open GeoTheis NX**](https://nx.geostru.ai/geotheis/){ .md-button .md-button--primary }

## What it does { #che-cosa-fa }

1. **Places the well** on the map, with coordinates in WGS84, UTM (WGS84, ETRS89, RDN2008, ED50) and Gauss-Boaga, the ground
   elevation from the digital terrain model and the ISPRA registered wells nearby.
2. **Describes the well**: stratigraphy, aquifer type, aquifer elevations, calculation scheme, completion (borehole, casing with
   screens, annulus, conductor casing, pump) and piezometers.
3. **Collects the tests**: pumping steps and constant-rate test with recovery, also pasted from a spreadsheet.
4. **Calculates every method** the data allow: characteristic curve and Rorabaugh on the steps, Theis, Cooper-Jacob, recovery,
   Hantush, Dupuit-Thiem, distance-drawdown, single wells. It compares them and proposes the **design value**, with the
   reasoning.
5. **Produces the Word report** with data, methods, charts, comparison and allowable discharge, and the well section as DXF.

The calculation updates by itself at every change: there is no "Calculate" button. The program uses the formulas from the
literature; where the GeoTheis desktop program had different formulas, the app follows the literature. The differences are listed
in [Validation](validazione.md).

## Who it is for { #a-chi-serve }

Geologists and engineers who run or interpret well tests: acceptance testing of a new well, checking the sustainable yield, a
groundwater abstraction permit application, a hydrogeological study of an aquifer.

## The four tabs { #le-quattro-schede }

The work follows four tabs in a row. At the bottom of each tab, the button with the name of the next tab takes you forward.

| Tab | Under the name | What you do |
|---|---|---|
| 1. [**Well**](pozzo.md) | Site, stratigraphy, completion, piezometers | location, soils, aquifer, elevations, well geometry, piezometers; on the right the live well section |
| 2. [**Test**](prove.md) | Step test, constant rate and recovery | readings of the step-drawdown test and of the constant-rate test; alternatively the known critical discharge |
| 3. [**Results**](risultati.md) | Applicable methods and comparison | calculated methods, comparison, design value, allowable discharge, choices on the charts |
| 4. [**Report**](relazione.md) | Preview, Word and DXF | free preview, Word and DXF for credits, sending to the other NX apps |

At the top of the page is the **Project name**: it names the file and the report.

## What is free and what uses credits { #che-cosa-e-gratuito-e-che-cosa-consuma-crediti }

Entering data, calculating, viewing charts, drawings and the map is **free**. Only three actions use NX credits:

| Action | Credits |
|---|---|
| Word report (**Generate Word**) | 10 |
| Well section as DXF (**DXF**, **Well DXF**, or **Open in CAD Tools**) | 10 |
| One message to the **Assistant** | 3 |

These are the rates in force at the time of writing and may change.

- A **failed operation is not charged**: if the Word file or the DXF cannot be composed, the message says so and no credit is
  charged.
- **Generating the same Word file again** (same data, same language) is not charged again; the same applies to a DXF already
  downloaded.
- If your balance does not cover the cost, *Not enough credits for: …* appears with the balance and the **Buy credits** button.
  The project stays in the session: top up your balance and try again.

## Session and saving { #sessione-e-salvataggio }

The project lives **in a session on the server**. Every field saves itself to the session as you type, but the session expires
after **30 minutes of inactivity**: to keep your work, save it to a `.geotheisnx` file (**File** menu → **Save** or **Save
as…**) or to **GeoDropbox**. With **File** → **Open…** you reopen a `.geotheisnx` file or a `.wtax` project from the desktop
program. Details in [Files and GeoDropbox](file.md).

!!! warning "Warning"
    *Saved* next to the title of a panel means saved to the session, not to a file. If the session expires, data not saved to a
    file are lost.

## Manual map { #mappa-del-manuale }

| Chapter | Contents |
|---|---|
| [Quick start](quickstart.md) | from the CELICO example to the results and the report preview, in 5 minutes |
| [Workflow](workflow.md) | a real project, from start to report, with all the options |
| [Well](pozzo.md) | site and coordinates, stratigraphy, aquifer and elevations, calculation scheme, completion, piezometers, section |
| [Tests](prove.md) | step-drawdown test, constant rate and recovery, paste from Excel, known critical discharge |
| [Methods](metodi.md) | the interpretation methods, the data they need, their assumptions |
| [Results](risultati.md) | the Results tab: design value, allowable discharge, comparison, choices on the charts |
| [Report](relazione.md) | preview, Word, DXF, links with the other NX apps |
| [Files and GeoDropbox](file.md) | saving, opening, importing desktop `.wtax` files |
| [Assistant](assistente.md) | what the AI assistant can do and what it costs |
| [Theory](teoria.md) | formulas and references |
| [Glossary](glossario.md) | the terms of well testing |
| [Validation](validazione.md) | test cases, comparisons with the desktop program, limits |
| [Frequently asked questions](faq.md) | the most common doubts |

Start from the [Quick start](quickstart.md).

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20GeoTheis%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/geotheis/docs/en/index.md).*
