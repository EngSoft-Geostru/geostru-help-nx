# Workflow

A complete project, in the order of the four tabs: **Well** → **Test** → **Results** → **Report**. Every field saves itself to the
session as you type and the calculation updates at every change: there is no "Calculate" button. You can go back to an earlier
tab at any time; the results follow the data.

## 0. Start a project { #0-inizia-un-progetto }

From the **File** menu:

- **New project** empties the session;
- **Open…** reopens a GeoTheis NX `.geotheisnx` file or a `.wtax` file from the desktop program. With a `.wtax` you get
  *Desktop program project opened: check the data before calculating.*, with the import notes;
- **Examples with tests** and **Single wells (known critical discharge)** open the examples of the desktop program.

If the project on screen has changes that are not in a file, the program first asks whether to save them. Type the **Project
name** at the top of the page (for example *Well P1 — Rossi farm*): it names the file and the report.

## 1. Well tab { #1-scheda-pozzo }

There are four panels on the left; on the right the **Well section** is redrawn at every save. All the fields are described in
[Well](pozzo.md).

1. **Site and coordinates** — Search for the town or the street, then click the exact spot of the well, or use **GPS position**
   or type the coordinates in one of the systems offered (WGS84, UTM, Gauss-Boaga, ED50). The program suggests the municipality
   and the ground elevation from the digital terrain model (DTM): the project's ground level changes only if you press **Use the
   DTM elevation**. Check the **Registered wells nearby** (ISPRA archive). If you have the well coordinates from another source,
   compare them in **Check against a second source**.
2. **Stratigraphy** — One layer per row, from ground level downwards: soil, description, thickness. It is used for the drawing
   and the report, not for the calculation.
3. **Well and aquifer** — Four tabs:
    - **Aquifer and levels**: **Aquifer type**, **Well penetration**, **Construction** and the elevations in m a.s.l. The aquifer
      type decides which methods apply: always choose it.
    - **Calculation scheme**: well radius, depth, blank between head and screen, screen length and, for partially penetrating
      wells, the data towards the base. This is what the formulas use.
    - **Completion**: borehole, casing (blank, screens, sump), annulus, conductor casing, pump, measured levels. To get going
      quickly, press **Propose completion from scheme** in the **Calculation scheme** tab.
    - **Job**: client, project, test date, contractor, engineer, description and notes for the report.
4. **Piezometers** — Name and **Distance** r from the well axis for each piezometer: the distance is the only piezometer input
   used by the calculation. Elevations and screen are for the drawing. Without piezometers the test is analysed on the pumped
   well only, and S cannot be derived reliably.

If something does not add up (static level above ground level, aquifer top below the base, a radius of 5 m…) the **Data to
check** strip appears. It does not block anything: it asks you to check.

## 2. Test tab { #2-scheda-prova }

Two panels, described in [Tests](prove.md):

1. **Step-drawdown test** — One row per step, with the end-of-step reading: time from the start of the test, discharge and
   cumulative drawdowns in the well and in the piezometers. Choose the units in **Times in** and **Discharges in**. With **Paste
   from Excel or CSV** you copy the columns from a spreadsheet or from the datalogger.
2. **Constant rate and recovery** — **Test discharge**, **Steady-state drawdowns** (at steady state, for Dupuit-Thiem),
   **Pumping** readings (t from the start of pumping) and **Recovery** readings (t′ since the pump stopped), in the well and in
   the piezometers.

If you do not have a step-drawdown test but you know the critical discharge of the well, fill in the **Known critical discharge
(no step-drawdown test)** panel: together with the well geometry it feeds the single-well methods, which give indicative T and K.

## 3. Results tab { #3-scheda-risultati }

1. Read **Methods calculated** and **Not applicable to the data**: a missing method has its reason written next to it.
2. Check the **Comparison of methods** and the **Deviations to check**.
3. Open the method tabs. On the charts, exclude anomalous readings with a click, narrow the Cooper-Jacob interval, adjust the
   Theis or Hantush type curve if needed.
4. With a step-drawdown test, choose the **critical discharge** on the characteristic curve.
5. Confirm the **Design value** (T, K, S, R) and the **Allowable discharge**, or choose another method or type the operating
   discharge.

Everything is free. Details are in [Results](risultati.md); the methods and their assumptions in [Methods](metodi.md).

## 4. Report tab { #4-scheda-relazione }

1. Read **What goes into the report**: each item says whether the data are there (position, stratigraphy, steps, constant rate,
   piezometers).
2. Check the **Preview**, which is free: it is the same text as the Word file.
3. **Generate Word** to download the report, **Well DXF** for the section as DXF: both use credits.
4. In **Continue with the other NX apps** send the well to GeoDropbox, open the section in CAD Tools or the site dossier in
   Atlante.

See [Report](relazione.md).

## 5. Save { #5-salva }

The project lives in the session and expires after 30 minutes of inactivity. Save it with **File** → **Save** (Ctrl+S) or **Save
as…** (Ctrl+Shift+S) to a `.geotheisnx` file, or to **GeoDropbox**. See [Files and GeoDropbox](file.md).

!!! tip "Tip"
    The **Assistant** at the top reads the project and the results and can enter data for you: pasted readings, stratigraphy,
    piezometers, well coordinates. Each message uses credits. See [Assistant](assistente.md).

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20GeoTheis%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/geotheis/docs/en/workflow.md).*
