# Import — accepted formats and workflow

GeoSection NX accepts several formats for the two main inputs — the **topographic
profile** and the **boreholes**. Most can also be imported via the AI chat when
the file doesn't follow a standard format.

## Topographic profile

### CSV

One `X,Z` pair per row (X distance in m, Z elevation in m a.s.l.):

```
0,120
10,118.5
30,115
60,109.2
100,103
```

Allowed separators: comma, semicolon, tab, space. Decimal `.` or `,`.
Open *Import profile → CSV tab*, paste, confirm.

### Raster image (BMP / PNG / JPG)

Load a scan of a paper section (e.g. PRG, PAI, old urban plans). In the
**Img tab** of the Import profile modal:

1. Load the image.
2. Set the 4 calibration points (origin + 3 known X/Z points) by clicking
   the grid that appears.
3. The image is **georeferenced** and becomes the section background; the
   profile polyline is then traced manually on the grid or extracted via
   AI vision.

### DXF (LWPOLYLINE)

Open *Import profile → DXF tab*, load the `.dxf`. GeoSection looks for
lightweight polylines (LWPOLYLINE) on the `PROFILO` layer or the first
available one, sorts them by ascending X and imports them as the topographic
line. If the file has multiple polylines, the app asks you to choose.

## Boreholes

### AGS4

[AGS4](https://www.ags.org.uk/) is the international standard for geotechnical
data exchange. *File → Import boreholes → AGS4* reads the `LOCA` (metadata),
`GEOL` (stratigraphy) and `WSTK` (water) groups and populates boreholes +
water-table levels.

### CSV / TSV

For files from spreadsheets. Expected schema:

```
hole_id,x,y,quota,depth_top,depth_bot,layer,description
SD1,1024.5,3850.2,118,0,1.5,topsoil,Topsoil
SD1,1024.5,3850.2,118,1.5,4.2,clay,Silty clay
SD1,1024.5,3850.2,118,4.2,8.0,sand,Gravelly sand
SD2,1090.1,3855.4,115,0,2.0,clay,Clay
```

- `hole_id`: borehole identifier (string).
- `x, y`: planar coordinates (any reference system, as long as consistent with the trace).
- `quota`: absolute elevation of the borehole top (m a.s.l.).
- `depth_top, depth_bot`: layer depth from ground level (m).
- `layer`: layer code/tag (used to group colours in legend).
- `description`: textual description of the layer.

CSV separators: `,`, `;`, tab. TSV: tab. Decimal `.` or `,`.

### AI Import (free formats)

When the file has Italian headers, comma decimals, blank rows, extra columns,
or is a PDF scan of a historical borehole — use **Import with AI**:

1. Modal *File → Import with AI*.
2. Drag-drop file or paste text (Excel-friendly).
3. The AI auto-recognises schema, separators, language, drops known noise rows.
4. Preview of extracted values — editable before confirmation.

Costs a few NX credits per call; visible on the wallet chip before confirmation.

## Ready samples

In the **Info → Resources** modal you'll find packaged samples for each format:
- 2 profile examples (DXF + raster image);
- 3 borehole examples (AGS4 + CSV + TSV);
- 6 AI examples to test the chat (real "messy" formats).
