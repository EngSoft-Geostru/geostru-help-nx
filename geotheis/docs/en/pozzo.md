# Well

The **Well** record describes the structure and its location: position and coordinates, soils encountered, aquifer type and elevations,
well geometry, completion and piezometers. On the left there are four panels, in this order:

1. **Site and coordinates**
2. **Log**
3. **Well and aquifer**, with four tabs: **Aquifer and levels**, **Calculation scheme**, **Completion**, **Job**
4. **Piezometers**

On the right, the **Well section** is redrawn as you type.

Only a few data are required for the calculation: the **aquifer type**, the aquifer **elevations**, the **well radius** and the
**distance** of each piezometer. The other data are used for the drawing, the report and the allowable discharge checks.

## How data is saved { #come-si-salvano-i-dati }

There is no “Save” button in the panels: each field is saved automatically in the session. An option, checkbox or drop-down list is
saved immediately; text is saved after a short pause in typing. Next to the panel title you can see the status: *Saving…*,
*Saved · hh:mm* or *Not saved*.

- Numbers can be entered with a comma or a decimal point.
- A value that is not a number remains in red with *Not a readable number: not saved.*
- Thicknesses, distances, diameters, radius, depths and lengths cannot be negative: a negative value remains in red with
  *Cannot be negative: not saved.* Elevations in m a.s.l. can be negative.
- An empty field means that no data has been entered, not zero.

!!! warning "Warning"
    *Saved* means saved in the session on the server, which expires after 30 minutes of inactivity. To keep the project,
    save it to a `.geotheisnx` file or to GeoDropbox: see [Files and GeoDropbox](file.md).

## Site and coordinates { #sito-e-coordinate }

The panel places the well on the map and gives its coordinates in all systems. The position is not used in the parameter calculation:
it is used for the report (map, coordinates, nearby wells), piezometer distances and links with the other NX apps.

### Map { #mappa }

Above the map:

- **Search a place (town, street, locality)** + **Search** centres the map on the place found. The well does not move: *Map centred
  on …. The well has not moved: click the exact point to place it.*
- **GPS position** places the well using the device GPS and reports the stated accuracy (±… m).
- **A click on the map** selects what clicking does: **navigation only**, **places the well** or **places the
  piezometer** (with a drop-down list for the piezometer to be placed).
- **Map** and **Satellite** change the base map.

Until the well is on the map, clicking is already in **places the well** mode; after the first click it returns to **navigation
only**, so you do not move the well by mistake. The well and piezometers can also be **dragged** on the map.

The legend below the map shows the **well**, **piezometers**, **ISPRA registered wells**, the dashed circle for the nearby-well
search radius and, when available, the radius of influence circle: *Project R = … m*, with its origin (*confirmed*,
*proposed by the program* or *assumed*).

### Position, municipality and elevation { #posizione-comune-e-quota }

When the well is on the map, the **Well** panel shows its position in sexagesimal degrees and the system in which the coordinates
were entered. The program then proposes:

- **Municipality**, **Province** and **Locality** from the Nominatim service (OpenStreetMap), **only in empty fields**. If the point
  is in another municipality, *The point is in …* appears with the **Use** button. All three fields can also be entered manually.
- The **Ground elevation from the DTM**: TINITALY (INGV) at 10 m; if it does not respond, Copernicus GLO-90 at 90 m, which is less accurate.

Below the DTM elevation is the **Ground level elevation (project data)**, namely the **Ground level** field on the
**Aquifer and levels** tab, with the difference from the DTM. The DTM elevation is only a proposal: the project survey data takes
precedence and changes only if you press **Use the DTM elevation**. If a service does not respond, **Retry elevation and municipality** repeats the request.

!!! note "Note"
    The DTM elevation is an average value for the model cell. A survey is required for levelling.

### Coordinates to enter { #coordinate-da-inserire }

To place a point from coordinates:

1. **Point**: the **Well** or one of the piezometers;
2. **System**: one of the systems in the table below;
3. **Easting (m)** and **Northing (m)**, or **Longitude** and **Latitude** for geographic systems;
4. **Place**.

| System | EPSG |
|---|---|
| WGS84 geographic | 4326 |
| WGS84 / UTM zone 32N, 33N, 34N | 32632, 32633, 32634 |
| ETRS89 / UTM zone 32N, 33N, 34N | 25832, 25833, 25834 |
| RDN2008 / UTM zone 32N, 33N, 34N | 6707, 6708, 6709 |
| Roma40 / Gauss-Boaga West zone, East zone | 3003, 3004 |
| ED50 / UTM zone 32N, 33N, 34N | 23032, 23033, 23034 |
| Roma40 (Monte Mario) geographic, Greenwich | 4265 |
| ED50 geographic | 4230 |

For geographic systems, you can enter decimal degrees or degrees, minutes and seconds (for example `38°04'08" N`). The source system
is retained in the project and reported in the report.

The program checks the coordinates before placing the point:

- *Easting greater than Northing: they appear to be swapped. In Italy, Northing ranges from 4 to 5.2 million metres.*
- *The point is outside Italy: check the coordinate system and digits.*
- *The point is more than 9° from the central meridian of the system: the conversion loses precision (beyond one centimetre).*

### The well in all systems { #il-pozzo-in-tutti-i-sistemi }

The table lists the well in every system, with **East / Lon**, **North / Lat** and the datum **Transformation** used. The systems
for the zone containing the well are listed first; the others are under **Neighbouring zones and other systems**, marked *outside zone*
or *beyond the precision limit*.

The conversion uses 7 EPSG parameters: the error is of the order of one metre, up to a few metres (Sicily and Sardinia have their own
parameters; ED50 up to approximately 10 m). The official IGM conversion uses grid files.

### Piezometer positions { #posizione-dei-piezometri }

For each piezometer, the table compares the distance entered in the **Piezometers** panel (**r entered**) with the distance derived
from the coordinates (**r from coordinates**), together with the **Azimuth** from north and the **Status**:

| Status | Meaning |
|---|---|
| **not on the map** | the piezometer has no coordinates |
| **well missing** | the piezometer is on the map but the well is not: place the well first |
| **r to complete** | no distance had been entered: the program enters it from the coordinates |
| **consistent** | the two distances differ by no more than 1 m |
| **choose** | the two distances differ by more than 1 m: you choose which one applies |

When the status is **choose**, you have two buttons:

- **Use r from coordinates**: the piezometer distance becomes the calculated distance;
- **Move to the entered r**: the piezometer moves on the map to the entered distance, at the same azimuth.

**Remove from the map** removes the piezometer coordinates; the entered distance remains. An entered distance is never overwritten
without your choice.

A piezometer can be placed in three ways: click the map in **places the piezometer** mode, enter coordinates in **Coordinates to
enter**, or use **From distance and azimuth**: select the piezometer, enter **Distance from well (m)** and **Azimuth from north (°)**
and press **Place**. Distances and azimuths are calculated on the WGS84 ellipsoid (Vincenty formulae).

### Registered wells nearby { #pozzi-censiti-nei-dintorni }

The **Registered wells nearby (ISPRA, Law 464/84)** panel searches for boreholes in the national archive within the selected
**Radius (m)** (from 50 to 2,000 m, 500 m on opening). The search starts when you place the well; **Search** repeats it. The table shows
**Distance**, **Work**, **Depth**, **Water**, **Log**, **Municipality** and the link to the ISPRA **Record**.

!!! warning "Warning"
    The Law 464/84 archive is incomplete: “no registered wells” does not mean “no wells”. Wells not included in the archive can be found
    in regional land registers and geoportals.

### Check against a second source { #controlla-con-una-seconda-fonte }

In **Check against a second source**, enter the coordinates of the same well obtained from another source (report, photo GPS,
land register), with their **System** and a **Threshold (m)** (10 m on opening), and press **Compare**. The program states whether the
two positions are within the threshold. If the difference is between 40 and 300 m, which is typical of the difference between datums
(Roma40 or ED50 versus WGS84), it adds that one of the two coordinates may have been entered in the wrong system. The comparison does
not modify the project.

### Links with the other NX apps { #collegamenti-con-le-altre-app-nx }

**Site dossier with Atlante**, at the top of the panel, opens Atlante NX at the well location: geology, constraints, hazards and
maps with references.

If you open GeoTheis NX from another NX app (Atlante, Hydrogeo, Maps) with a point, a banner appears proposing the position:
**Use this point** or **Ignore**. If the well already has a different position, the banner states how many metres away the new point is.
The point is never applied automatically.

## Log { #stratigrafia }

Layers are entered **from ground level downwards**, one per row, with their thickness. The log **is not used in the
calculation**: it is used for the section drawing and the report.

| Column | Unit | What you enter |
|---|---|---|
| **Soil** | — | the soil from the catalogue; determines the hatch pattern in the drawing |
| **Description** | — | free text (up to 400 characters) |
| **Thickness** | m | layer thickness, non-negative |
| **From – to** | m | depth to the top and bottom of the layer: calculated by the program from the thicknesses |
| **Colour** | — | tick the checkbox to use a custom colour instead of the soil hatch pattern |

The soils in the catalogue are: Clean sand, Silty sand, Clayey sand, Silty-clayey sand, Gravelly sand, Sandy gravel, Gravel, Silt,
Sandy silt, Clayey silt, Sandy-clayey silt, Clay, Organic soils, Rock, Other.

**Add layer** adds a row at the bottom; the **×** on the right removes it. At the top of the panel you can see the number of layers
and the total thickness.

If you open a desktop program file containing a soil that is not in the catalogue, the row shows *from desktop: “…”* and the soil is
**Other**: select the closest soil so that the drawing uses the correct hatch pattern.

## Well and aquifer { #pozzo-e-falda }

The panel has four tabs. It opens on the last tab you used.

### Aquifer and levels { #falda-e-quote }

**Aquifer type** determines which calculation methods apply. Until you select it, *The aquifer type has not yet been selected:
it is required to determine which calculation methods apply.* appears, and the methods in Results assume a confined aquifer.

| Option | Meaning |
|---|---|
| **Unconfined** | phreatic: the water surface is at atmospheric pressure and falls during pumping |
| **Confined** | artesian (confined): enclosed between two impervious layers, the water level rises above the top of the aquifer |
| **Leaky, unconfined** | beneath a semi-pervious layer that feeds it; free surface (“semi-unconfined” in the desktop version) |
| **Leaky, confined** | beneath a semi-pervious layer that feeds it; under pressure (“semi-artesian” in the desktop version) |

The Hantush method is calculated only for a leaky aquifer. See [Methods](metodi.md).

**Well penetration**:

- **Fully penetrating**: the screens extend through the full aquifer thickness;
- **Partially penetrating**: the screens extend through only part of it; **Screen – base** (TSI) and, for confined aquifers,
  **Blank between screen and base** (LC) are required on the **Calculation scheme** tab.

**Construction**: **Drilled** or **Dug (large diameter)**. This changes the well drawing.

**Elevations**, in m a.s.l., as in the desktop program:

| Field | Abbreviation | When it appears | What it is |
|---|---|---|---|
| **Ground level** | PC | always | ground elevation at the well |
| **Well head** | QTF | always | elevation of the top of the casing |
| **Static water level** | LS | always | elevation of the water level at rest |
| **Impervious top** | TI | confined aquifer (including leaky) or not selected | elevation of the top of the confined aquifer |
| **Impervious base** | SI | always | elevation of the aquifer base |
| **Top of semi-pervious layer** | TSP | leaky aquifers | elevation of the top of the semi-pervious layer |
| **Bottom of semi-pervious layer** | LSP | leaky aquifers | elevation of the base of the semi-pervious layer |

Only the elevations required for the selected aquifer type are shown; the others remain saved. From the elevations, the program derives:

$$
H_1 = LS - SI \qquad b = TI - SI
$$

where H~1~ is the saturated thickness (unconfined aquifer) and b is the confined aquifer thickness. The elevations are also used for
the allowable discharge checks: with a confined aquifer, the dynamic water level must not fall below the top. See [Results](risultati.md).

### Calculation scheme { #schema-di-calcolo }

The scheme is the geometry used by the formulae for **single wells**, as in the desktop program. It remains an explicit item of data,
separate from the drawn completion: the two may not coincide.

| Field | Abbreviation | Unit | When it appears | What it is |
|---|---|---|---|---|
| **Well radius** | r~w~ | m | always | radius used in the calculation (not the diameter) |
| **Total depth** | — | m | always | from ground level, for the drawing |
| **Blank between head and screen** | LFC | m | always | length of blank casing above the screen, measured from the well head |
| **Screen length** | LTF | m | always | length of the screened section |
| **Screen – base** | TSI | m | partially penetrating well | distance between the bottom of the screen and the impervious base |
| **Blank between screen and base** | LC | m | partially penetrating well in a confined aquifer (including leaky) | blank section below the screen |

The well radius is also used for drawdown in the well and the cone of depression.

**Propose completion from scheme** fills in the blank casing, screen and drilling on the **Completion** tab based on the scheme;
annulus, well chamber, pump and levels remain unchanged. The ground level elevation, well head elevation and screen length are required.
If casing already exists, the program asks for confirmation: *The current casing and drilling will be replaced by those proposed by
the scheme.* → **Replace** or **Cancel**.

### Completion { #completamento }

The completion describes the well **as built**, for the drawing and the report. Depths are in m from ground level, positive downwards;
diameters are in mm. Each table has its own **Add section** button (or **Add level**) and a **×** to remove the row.

**Drilling**: one section for each drilling diameter.

| Column | Unit |
|---|---|
| **From**, **To** | m from ground level |
| **Diameter** | mm |

**Casing: blank, screens, sump**: sections of the casing string, including multiple screens.

| Column | Unit | Notes |
|---|---|---|
| **Type** | — | **Blank**, **Screen** or **Sump** |
| **From**, **To** | m from ground level | |
| **Outer Ø** | mm | outside diameter of the casing |
| **Wall** | mm | wall thickness |
| **Material** | — | free text |
| **Screen type** | — | only for **Screen** sections |
| **Slot** | mm | screen aperture, only for **Screen** sections |

**Annulus**: the space between the borehole and the casing.

| Column | Unit | Notes |
|---|---|---|
| **Type** | — | **Grout**, **Clay seal** or **Gravel pack** (proposed for a new row) |
| **From**, **To** | m from ground level | |
| **Material or note** | — | free text |

**Well chamber** and **Pump** are enabled with their checkboxes; if unticked, the fields remain but are not used.

| Well chamber | Unit |
|---|---|
| **Bottom depth** | m |
| **Diameter** | mm |

| Pump | Unit | Notes |
|---|---|---|
| **Intake depth** | m from ground level | used in the allowable discharge check |
| **Rated flow** | l/s | |
| **Power** | kW | |
| **Description** | — | free text |

Intake depth is not only drawing data: the proposed allowable discharge keeps the intake at least 1 m below the dynamic water level.
See [Results](risultati.md).

**Measured levels**: water level measurements in the well, for the drawing and the report.

| Column | Unit | Notes |
|---|---|---|
| **Type** | — | **Static** or **Dynamic** |
| **Depth** | m from ground level | |
| **Date** | — | free text |
| **Note** | — | free text |

!!! note "Note"
    The static water level used in the calculation is the **Static water level** elevation (LS) on the **Aquifer and levels** tab,
    in m a.s.l. The measured levels in the completion are used for the drawing and the report.

### Job { #lavoro }

The job data are included in the report; none are used in the calculation.

| Field | Notes |
|---|---|
| **Client** | |
| **Project or well use** | for example irrigation, industrial, water supply |
| **Test date** | free text |
| **Contractor** | |
| **Responsible engineer** | |
| **Description** | free text |
| **Notes** | free text |

## Piezometers { #piezometri }

One piezometer per row. The **distance r from the well axis** is the only piezometer data used in the calculation; elevations and
screen are used for the drawing.

| Column | Unit | What it is |
|---|---|---|
| **Name** | — | the name shown in tables, charts and the report (up to 40 characters) |
| **Distance** | m | distance r from the well axis, non-negative |
| **Ground level** | m a.s.l. | ground level elevation at the piezometer |
| **Head elevation** | m a.s.l. | elevation of the top of the piezometer |
| **Depth** | m | piezometer depth |
| **Screen from**, **Screen to** | m | screened section |
| **Map** | — | *placed* if the piezometer has coordinates, otherwise — |

Next to the name is an identifier (P1, P2…) assigned automatically by the program: test readings are linked to this identifier, not
to the table row. If you leave the name empty, the identifier is used.

**Add piezometer** adds a row. The **×** removes the piezometer after confirmation: *Remove …? Its test readings will also be lost.*
The readings of the other piezometers remain unchanged.

The map position is set in the **Site and coordinates** panel. If the well and piezometer are on the map, the distance is derived from
the coordinates only when you have not entered it yourself; otherwise you choose which one applies (see [Piezometer
positions](#posizione-dei-piezometri)).

Without piezometers, *No piezometers: the test is analysed using the well alone.* appears. From the pumping well alone, T can be derived,
but not S reliably. See [Methods](metodi.md).

## Data to check { #dati-da-verificare }

After every save, the program checks that the data in the **Well and aquifer** panel are consistent. If something is inconsistent,
the **Data to check** banner appears at the top of the panel. This is not a rejection: the data remain saved and the calculation proceeds.

| Warning | When |
|---|---|
| *The static water level is … m above ground level: is this a flowing artesian well? Otherwise, check the elevations.* | LS > PC |
| *The impervious base is at the same elevation as the static water level or higher: the aquifer would have no saturated thickness. Check the elevations.* | SI ≥ LS |
| *The top of the aquifer is not above the base: the thickness b = TI − SI would be zero or negative. Check the elevations.* | confined aquifer, TI ≤ SI |
| *The top of the aquifer is above ground level: check the elevations.* | non-unconfined aquifer, TI > PC |
| *The top of the semi-pervious layer is not above its base: check the elevations.* | leaky aquifer, TSP ≤ LSP |
| *The well radius is zero: it is required for drawdown in the well and the cone of depression.* | r~w~ = 0 |
| *Well radius of … m: is this the radius, not the diameter? (in metres)* | r~w~ > 5 m |
| *The well head is more than 5 m below ground level: check the elevations.* | QTF < PC − 5 m |

The same checks for readings appear in the Test record. See [Tests](prove.md).

## Well section { #sezione-del-pozzo }

On the right of the record, the **Well section** is generated on the server after every save: log with hatch patterns, drilling,
casing with screens and sump, annulus, well chamber, pump, levels, aquifer top and base, semi-pervious layer, piezometers and cone of
depression. Piezometers are projected onto the section plane at their distance from the well; the well width is not to scale and the
note below the drawing states by how much.

Controls:

- **Discharge Q** and **Time t**: two sliders that move the cone of depression. They work when T and S (or the test results) are available.
- **Distances**: **Log** or **Linear** scale for distances from the well.
- Scroll wheel to zoom, drag to pan; **Fit** (or double-click the drawing) returns to the full view.
- **PNG**: image of the section, free of charge.
- **DXF**: the section in DXF format, in metres, with layers. This uses credits; if the DXF is not generated, no charge is made.

The cone is drawn using the current project values and the operating discharge, as explained in [Results](risultati.md#cono-di-depressione).

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20GeoTheis%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/geotheis/docs/en/pozzo.md).*
