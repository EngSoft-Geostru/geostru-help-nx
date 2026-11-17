# Quick start (5 minutes)

You get to the results and to the report preview with the **CELICO** example, which the program has ready: a complete well in a
confined aquifer with a step-drawdown test, a constant-rate test with recovery and two piezometers. You do not have to type any data.
With your own data the steps are the same: you find them in full in the [Workflow](workflow.md).

## 1. Open the example { #1-apri-lesempio }

Open [nx.geostru.ai/geotheis](https://nx.geostru.ai/geotheis/). In the top bar open the **File** menu: under **Open…** there is
the **Examples with tests** list. Choose **CELICO**, the first one.

If the project on screen has changes that are not in a file, the program tells you: *The project has changes that are not in a
file: if you continue, they will be lost.* Choose **Save first** or **Continue without saving**.

The app goes back to the **Well** tab with the strip *Example «CELICO» opened: it is a desktop program file, read as a .wtax.*
Below it, **More import notes** lists what the desktop file reader noticed: read them when you open one of your own `.wtax`
files.

!!! note "Note"
    The examples are the files of the GeoTheis desktop program. The CELICO data are built to test the calculation; they do not
    describe a real aquifer.

## 2. Look at the well { #2-guarda-il-pozzo }

In the **Well** tab scroll through the panels on the left; on the right the **Well section** is already drawn.

- **Site and coordinates**: CELICO has no geographic position, so the well is not on the map. With your own well, click the map
  at the well location.
- **Stratigraphy**: the layers from ground level downwards.
- **Well and aquifer**, **Aquifer and levels** tab: aquifer type **Confined**, penetration **Fully penetrating**, elevations in
  m a.s.l. (ground level 98, static level 93, aquifer top 91, base 84). In the **Calculation scheme** tab the **Well radius**
  r~w~ = 0.5 m.
- **Piezometers**: P1 at 23.5 m and P2 at 42.4 m from the well axis.

Above the section, move the two sliders **Discharge Q** and **Time t**: the cone of depression moves with them.

Press **Test** at the bottom of the page.

## 3. Look at the test { #3-guarda-la-prova }

The **Test** tab has two panels:

- **Step-drawdown test**: 3 steps, one row per step with the time, the discharge and the drawdowns in the well and in the
  piezometers;
- **Constant rate and recovery**: the **Test discharge**, the **Steady-state drawdowns**, the **Pumping** and **Recovery**
  readings.

Discharges are in l/s and times in h:mm:ss. To see the CELICO discharges in m³/h, as in the desktop file, change **Discharges
in**: it only changes the display. Details in [Tests](prove.md).

Press **Results**.

## 4. Read the results { #4-leggi-i-risultati }

The **Results** tab calculates by itself every method the data allow.

1. In **Test results** read the two columns: **Methods calculated** and **Not applicable to the data**, each with its reason.
2. In the **Design value** panel the program proposes **Theis (fitting automatico)**, Theis with automatic fitting, with the
   reasoning: it agrees with Cooper-Jacob. The radius of influence R = 76.5 m comes from the Thiem line on the piezometers.
3. In the **Allowable discharge** panel you find Q~c~, Q~ott~ and the proposed discharge. In CELICO the proposal is lower than
   0.9·Q~c~ because the pumping level must not fall below the top of the confined aquifer: the reasoning says so.
4. The **Comparison of methods** flags that the step-test methods give much higher T than the constant-rate methods. Open the
   method tabs to see the charts.

If the proposal convinces you, press **Confirm the proposal**. Everything you do in this tab is free. The tab is explained in
[Results](risultati.md).

Press **Report**.

## 5. Look at the report preview { #5-guarda-lanteprima-della-relazione }

The **Report** tab shows what goes into the document and, below, the **Preview**: it is the same text as the Word file, with an
indicative layout. The preview is free.

**Generate Word** downloads the report and uses credits; **Well DXF** downloads the well section as DXF, also for credits.
See [Report](relazione.md).

## 6. Save { #6-salva }

The project is in the session and expires after 30 minutes of inactivity. To keep it use **File** → **Save as…**: you download a
`.geotheisnx` file that you reopen with **File** → **Open…**. Alternatively, save it to **GeoDropbox**. See [Files and
GeoDropbox](file.md).

## Next steps { #passi-successivi }

For your own well start from **File** → **New project** and follow the [Workflow](workflow.md). The fields of the Well tab are
described in [Well](pozzo.md).

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20GeoTheis%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/geotheis/docs/en/quickstart.md).*
