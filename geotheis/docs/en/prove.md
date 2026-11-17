# Test

The **Test** tab collects the pumping test measurements: the **step-drawdown test**, the **constant-rate test** with **recovery**,
the **stabilised drawdowns** and, if you do not have a step-drawdown test, the well's **known critical discharge**. Every value you
enter is saved automatically; the [Results](risultati.md) are updated with the new data.

The tab has two panels:

1. **Step-drawdown test**, with the panel for pasting steps and the *Known critical discharge (without step-drawdown test)* section;
2. **Constant rate and recovery**, with the test discharge, stabilised drawdowns, pumping readings and recovery readings.

You do not need both tests. The [method catalogue](metodi.md#quali-dati-per-quali-metodi) explains which methods are calculated
from which data.

!!! note "Note"
    Piezometers are entered on the **Well** tab (name and distance r from the well axis): see [Well](pozzo.md). Each piezometer
    adds an **s** *name* column to all the tables on this tab; hover over the heading to see its distance. If you remove a
    piezometer, its readings are removed too.

## Units, times and numbers { #unita-tempi-e-numeri }

At the top of each panel, choose how to read and enter the tables:

| Control | Choices | Default |
|---|---|---|
| **Times in** | h:mm:ss, s, min, h | h:mm:ss |
| **Discharges in** | l/s, m³/h, l/min, m³/s | l/s |

This is a display preference, not project data: it applies to this browser and is remembered. When you change it, the program first
saves what you have entered, then reloads the page with the converted values. Calculations always use seconds and m³/s.

Rules common to all tables:

- **Times.** Enter them as `1:30:00`, `90 min`, `2h` or as a number in the selected unit. `8:20` means 8 h 20 min (clock convention,
  not minutes and seconds). The abbreviations `1h30m15s`, `1h 30'`, `45 min`, `90 s`, `2 g` or `2d`, and `30"` for seconds are also
  accepted. With **Times in** set to h:mm:ss, a number without a unit means **minutes**.
- **Drawdowns** in m, positive downwards. An empty cell means no measurement was taken, not zero.
- **Numbers.** Both decimal commas and decimal points are accepted; the typographic minus sign «−» and exponential notation
  (`1,2E-03`) are also accepted.
- A completely empty row is not saved.

A value that cannot be parsed remains on screen marked in red and **is not saved**: the reason appears below the field (*Not a
readable number: not saved.* or *Cannot be negative: not saved.*). Discharges, critical drawdown and assumed radius cannot be
negative; a negative time cannot be parsed.

## Step-drawdown test { #prova-a-gradini-di-portata }

One row per step: the **end-of-step reading**, with the time since the start of the test and the **cumulative** drawdowns (those
measured at the end of the step relative to the static water level, not the increment for that step alone).

| Column | Unit | Meaning |
|---|---|---|
| **#** | — | step number |
| **Date** | text | reading date, free text (up to 40 characters); not used in calculations |
| **Time** | **Times in** unit | time from the start of the test to the end-of-step reading |
| **Discharge** | **Discharges in** unit | step discharge; non-negative |
| **s well** | m | drawdown in the pumping well at the end of the step |
| **s** *piezometer* | m | drawdown in the piezometer at the end of the step (one column per piezometer) |

**Add step** adds a row; the **×** on the right removes it. **Paste from Excel or CSV** opens the panel described below.

A step is **valid** if both its discharge and well drawdown are positive. Only valid steps are used for the characteristic curve:

- with **2** valid steps at different discharges, B and C are calculated (Jacob's characteristic curve);
- with **3** or more, Rorabaugh is also calculated (free exponent n);
- piezometer drawdowns are used by distance-based step methods and test stations.

**Time** is only used by Cooper-Jacob for test stations. The **critical discharge** is not entered here: it is selected on the
characteristic curve in the [Results](risultati.md#portata-concedibile).

!!! tip "Tip"
    Enter the steps in increasing discharge order, as they were performed. If the datalogger records one reading per minute, do not
    copy them manually: paste them with **Group readings into steps** and the program keeps the last reading at each discharge.

## Known critical discharge (without step-drawdown test) { #portata-critica-nota-senza-prova-a-gradini }

If there is no step-drawdown test but you know the well's critical discharge (from tests in nearby areas or from commissioning),
enter it here together with its critical drawdown. The **single wells** method derives T and K from the well geometry, Q~c~ and s~c~,
and the assumed radius of influence.

| Field | Unit | Meaning |
|---|---|---|
| **Critical discharge Qc** | **Discharges in** unit | declared critical discharge |
| **Critical drawdown sc** | m | drawdown in the well at the critical discharge |
| **Assumed radius of influence R** | m | radius of influence to assume; also used for single wells in the step-drawdown test |

All three values are required. They are declared values, not measured ones: single wells use them as steady-state conditions and give
**indicative** values; the report states that Q~c~ and s~c~ were supplied by you. With a known critical discharge, the program also
proposes the allowable discharge (0.9·Q~c~): see [Allowable discharge](risultati.md#portata-concedibile).

The badge next to the title shows the status:

- **used without steps**: there are no valid steps, so the known critical discharge is used;
- **not used: the test applies**: there is at least one valid step. The critical discharge from the step-drawdown test, selected on
  the s(Q) graph in the Results, applies. **Critical discharge Qc** and **Critical drawdown sc** remain saved but read-only;
  **Assumed radius of influence R** remains editable, because single wells also need it with a step-drawdown test.

!!! warning "Warning"
    Single wells are not calculated for a leaky aquifer, or if you have not specified on the **Well** tab whether the well is fully
    penetrating or partially penetrating. The allowable discharge from the known critical discharge, however, is still proposed.

## Constant rate and recovery { #portata-costante-e-risalita }

### Test discharge and stabilised drawdowns { #portata-della-prova-e-abbassamenti-stabilizzati }

| Field | Unit | Meaning |
|---|---|---|
| **Test discharge** (Q) | **Discharges in** unit | constant pumping discharge; non-negative |
| **Stabilised drawdowns** → **s well** | m | steady-state drawdown in the well |
| **Stabilised drawdowns** → **s** *piezometer* | m | steady-state drawdown in each piezometer |

Without a positive **Test discharge**, no constant-rate method is calculated, even if readings are present. Stabilised drawdowns
(*steady state, for Dupuit-Thiem*) are used by the steady-state Dupuit-Thiem method and to derive the radius of influence from Thiem's
straight line; a piezometer with zero stabilised drawdown is excluded (it is beyond the radius of influence or was not affected).

### Pumping { #pompaggio }

Readings during pumping: **t** since the start of pumping, **s well** and **s** for each piezometer, in m. **Add reading** adds a
row, and the **×** removes it.

- Readings in **piezometers** give T **and** S (Theis, Cooper-Jacob, distance-drawdown, Hantush in a leaky aquifer).
- Readings in the **well** alone give T; S from the well is not reliable.
- Distance-drawdown requires at least two piezometers at different distances read **at the same time**.

Readings with missing, zero or negative times or drawdowns are not used in the straight lines or fitting (the logarithm of zero does
not exist).

### Recovery { #risalita }

After the pump stops: **t′** since the stop and the **residual drawdown** s′ in the well and piezometers.

The stop time is needed to calculate t/t′ with t = t~stop~ + t′:

- **Pump stopped at the last pumping reading** (checkbox, default): the stop is the time of the last pumping reading, shown in
  parentheses;
- clear the checkbox and enter **Pump stop, from start** if the pump stopped after the last reading.

Recovery is only calculated if pumping readings are also present. Zero residual drawdown is excluded from the straight line.

!!! example "Example"
    Pumping for 8 hours with the last reading at `7:55:00` and the pump switched off at `8:00:00`: clear the checkbox and enter
    `8:00:00` in **Pump stop, from start**. Recovery readings start at t′ = `0:00:30`, `0:01:00`… from the stop, not from the start
    of the test.

## Data to check { #dati-da-verificare }

A **Data to check** banner may appear below the title of the two panels. It does not prevent saving: it flags data that is probably
incorrect.

| Warning | Where | What to check |
|---|---|---|
| *Pumping readings are not in time order (row …)* | pumping | a mistyped time; calculations still use the times |
| *Repeated pumping times (rows …)* | pumping | duplicate rows |
| *Drawdown of … m at row …: this is not a physically possible value.* | steps, pumping | over 1,000 m: typing error or units |
| *Drawdown of … m at row …: the water level would fall below the bedrock …* | steps, pumping | well drawdown greater than static water level − bedrock; also check the elevations in [Well](pozzo.md) |
| *The specified pump stop is before the last pumping reading* | recovery | the stop time |

## Pasting from Excel or CSV { #incollare-da-excel-o-csv }

Every table has a **Paste from Excel or CSV** button: a panel opens below the table (*Paste steps*, *Paste pumping readings*, *Paste
recovery readings*). Copy the columns from the spreadsheet or datalogger file and paste them into the text box.

1. Paste the text, **including the header row** if you have it.
2. If necessary, set the options (table below).
3. Click **Preview**: the program shows how it has parsed the text and does not write anything.
4. Check the preview and, in the **Goes to** column, which series each measurement column belongs to (**Well**, a piezometer or
   **— ignore —**). Changing a choice rebuilds the preview.
5. Click **Replace readings** (the table is replaced by the pasted data) or **Append to readings** (the readings are added to the
   existing ones and sorted by time). The page reloads with the new data.

| Option | Choices | When needed |
|---|---|---|
| **Times are** | *auto-detect*, *elapsed times*, *clock times* | if automatic detection is wrong |
| **Unit of numeric times** | *from header*, s, min, h | times written as numbers without a unit in the header |
| **Unit of discharges** | *from header*, l/s, m³/h, l/min, m³/s | only for steps, if the header has no unit |
| **Pumping start** (**Pump stop** for recovery) | time, or date and time (e.g. `08:30`, `12/03/2026 08:30`) | times expressed as clock times; hidden with *elapsed times* |
| **Static water level** | m, same datum as the water-level columns | water-level columns (depth to water) instead of drawdowns |
| **Group readings into steps** | checkbox | only for steps: one reading per datalogger row |

The preview shows the number of readings (and, for steps, the number of steps), how the times were parsed, the content and unit of
each column, the **first rows as they will be saved** (time in h:mm:ss and in the table unit) and any warnings.

!!! example "Example"
    Pumping readings with times in minutes, the well and a piezometer:

    ```text
    t (min)	s pozzo (m)	s P1 (m)
    1	0,42	0,05
    2	0,58	0,09
    ```

    Steps from the datalogger, with date and time:

    ```text
    Data	Ora	Q (l/s)	s pozzo (m)	s P1 (m)
    12/03/2026	10:00	2	0,85	0,21
    ```

### How the text is parsed { #come-legge-il-testo }

- **Separator**: tab (copy from Excel), then semicolon, then spaces or comma. With comma as the separator, the decimal separator must
  be a point.
- **Header**: the rows before the first data row. Text rows among the data are ignored, with a warning.
- **Cells**: numbers, times (`h:mm` or `h:mm:ss`), dates (`dd/mm/yyyy`, `dd-mm-yyyy`, `dd.mm.yyyy`, `yyyy-mm-dd` and variants) or
  date and time in the same cell.
- **Columns**, from the header: *discharge* (Q, portata, flow… or a unit such as l/s), *time* (t, tempo, time, ora, orario,
  trascorso, durata…), *date*, *level* (livello, profondità, soggiacenza, depth, level…; converted to drawdowns), otherwise
  *drawdown*. Without a header, the first numeric column is time and the others are drawdowns.
- **Units** from the header: for times s, min, h (also secondi, minuti, ore); for discharges l/s, m³/h (also mc/h), l/min, m³/s; for
  drawdowns cm and mm, otherwise m. Without units, times are in **minutes** and discharges in **l/s**, with a warning.
- **Clock times versus elapsed times** (*auto-detect*): with a date, they are clock times; then the header decides (*trascorso*,
  *durata* versus *ora*, *orario*); plain numbers are elapsed times; `h:mm:ss` values are clock times if they go backwards (midnight)
  or if the first reading is more than one hour after midnight with a short interval (08:30, 08:31…).
- **Clock times**: elapsed time is the time minus **Pumping start**. Without a date, a time earlier than the previous one belongs to
  the next day. Readings before the start are discarded, with a warning.
- **Levels**: s = L − L~0~, where L~0~ is the specified **Static water level**; otherwise the last reading with the pump stopped
  (before the start), otherwise the first reading. The warning states which was used.
- **Series**: a column goes to the piezometer whose name or abbreviation appears in the header, or to the well with *pozzo*, *well* or
  *PW*; the others go, in order, to the well and unassigned piezometers.

!!! warning "Warning"
    With clock times you **must** specify **Pumping start** (or **Pump stop** for recovery). Without it, the preview assumes the first
    reading as the start and says so; confirmation, however, is refused: the first reading would become t = 0 with a drawdown already
    measured, which is not possible.

!!! tip "Tip"
    Always paste the header row with units (`t (min)`, `Q (l/s)`, `s P1 (m)`). Without a header and without a date column, a
    discharge column is not recognised and would be read as drawdown.

**Group readings into steps**. The datalogger records one reading per row. With the checkbox selected, for each constant-discharge
interval the last reading before the discharge change is kept, as in the desktop program; intervals with zero discharge are discarded.
Without the checkbox, each pasted row becomes a step.

For pumping readings, if the text has a discharge column with a single value and **Test discharge** is empty, the discharge is also
entered there.

## Frequently asked questions { #domande-frequenti }

**I entered `90` as the time and see `1:30:00`.**
With **Times in** set to h:mm:ss, a number means minutes. Enter `90 s` if you meant seconds, or change **Times in**.

**Why is a step not used in the characteristic curve?**
Its discharge or well drawdown is missing, or one of the two is not positive. The program reports this in the characteristic curve
warnings in the [Results](risultati.md).

**Recovery is not calculated.**
You need the **Test discharge**, pumping readings and the stop time: leave **Pump stopped at the last pumping reading** selected or
enter the stop time.

**Piezometers do not appear in the tables.**
Add them on the [Well](pozzo.md) tab, with their distance from the well.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20GeoTheis%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/geotheis/docs/en/prove.md)*
