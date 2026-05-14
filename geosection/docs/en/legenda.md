# Legend and geological symbology

GeoSection NX generates the section with an **automatic legend** listing all
present layers, grouped by code. You can customise colours, patterns and order.

## Automatic generation

Each distinct layer present in the boreholes (`layer` field in CSV / `LITH_CODE`
in AGS4) generates a **legend entry** with:

- **Layer code** (tag, max 8 characters);
- **Description** (taken from the first occurrence in boreholes);
- **Colour** auto-assigned (16-colour standard palette);
- **Pattern** (solid by default);
- **Mean thickness** computed from the boreholes (informative).

The legend appears **to the right of the section** in the standard layout, but
can be moved below or disabled in *Layout → Legend*.

## Customisation

Panel *Legend → Edit*:

| Field | What it does |
|---|---|
| **Colour** | Click the swatch → colour picker; or type hex code |
| **Pattern** | Selection from ISO/UNI standard patterns: dotted (sand), horizontal dashes (clay), small triangles (gravel), wavy (silt), zig-zag (limestone), diamonds (gypsum) |
| **Description** | Editable (default = first text read from the borehole) |
| **Order** | Drag to reorder; affects the printed legend |
| **Visibility** | Checkbox: hide legend entries you don't want (e.g. surface topsoil) |

## Manual entries

For entries not in the boreholes but you want documented in the legend
(e.g. "Hypothetical bedrock"):

1. *Legend → Add entry*.
2. Code + description + colour + pattern.
3. The entry appears in the legend but **does not generate polygons** on the
   section — it stays purely documentary.

## ISO/UNI standard symbology

Available patterns follow [UNI 8842](https://www.uni.com/) and
[ISO 14689](https://www.iso.org/standard/72048.html):

| Pattern | Typical lithology |
|---|---|
| Dense dots | Sand |
| Sparse dots + dashes | Silty sand |
| Horizontal dashes | Clay / Silty clay |
| Crossed dashes | Silt |
| Small triangles | Gravel |
| Bricks | Stiff clay / Marl |
| Zig-zag | Limestone |
| Diamonds | Gypsum |
| Empty white | Fill / anthropogenic |
| Crosses | Crystalline bedrock (granite, gneiss) |

Patterns are rendered as SVG patterns: they scale correctly in PDF and DXF
prints (up to 1:1,000 without pixelation).

## Saving the style as a template

The legend style is part of the `.geosection` file: saving the project saves
colours/patterns/order too. To reuse on other projects:

1. *File → Save As* → save a "template" project.
2. On new projects: *File → Open style template* (loads only the legend,
   no data).

Useful for consultancies that want to standardise the presentation of
geological sections across different reports.
