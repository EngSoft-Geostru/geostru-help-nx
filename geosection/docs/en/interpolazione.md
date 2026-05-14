# Section interpolation

Once the topographic profile is loaded and at least 2 boreholes are in,
GeoSection builds the **continuous geological section** by interpolating
stratigraphic contacts between the boreholes projected onto the trace.

## Borehole projection on the trace

Each borehole has coordinates `(x, y)` in the plane. The section trace is a
polyline on the same plane. The projection is the **orthogonal distance** of
the borehole onto the nearest segment of the polyline:

- progressive distance along the trace: x-coordinate of the perpendicular foot;
- lateral distance: how far the borehole is from the trace (shown in legend
  — a borehole >50 m off trace should be assessed cautiously).

Boreholes appear in the section as **vertical columns** at their projected
abscissa, with the head at the indicated elevation and layers coloured by depth.

## Stratigraphic contact interpolation

The classical algorithm is **piecewise linear interpolation** between
matching contacts (same `layer` code) of adjacent boreholes:

1. For each borehole the **absolute elevations** of contacts are computed
   (head_elevation - depth).
2. Between two adjacent boreholes that both have a contact for layer X,
   a straight segment is drawn joining them.
3. If one is missing, the contact **extends horizontally** to the domain edge
   or to the next borehole where it reappears.

The result is a series of **stratigraphic polygons** filling the section
between the topography and contacts.

## AI: automatic section description

Pressing *AI → Describe section* sends a text summary of the geometry to the
multimodal model:
- number of layers and their codes;
- stratigraphic succession (top to bottom);
- presence of lenses, heteropies, recognisable discontinuities;
- water-table depth and extent.

Returns a descriptive paragraph to paste into the technical report. Uses
Gemini 1.5 Pro server-side.

!!! note "When the AI gets it wrong"
    The AI interpretation is **descriptive**, not geomechanical: it describes
    what it sees on the section, it doesn't replace the geologist's judgement.
    On sections with very thin layers (<50 cm) or distant boreholes (>200 m)
    the description tends to over-generalise.

## Water table

If the boreholes carry the water-table level (`wstk_depth` field in AGS4 or
analogous column in CSV), GeoSection draws a **blue zigzag line** joining the
water levels of adjacent boreholes. It does not interpolate between permeable
and impermeable layers — it's a pure geometric projection.

To manually edit the water table: panel *Discontinuities → Water table* →
edit points.

## Lenses and manual contacts

For cases the linear algorithm doesn't handle well (closed lenses, layer
missing in the middle due to erosional discordance) you use **manual contacts**:

1. Panel *Stratigraphy → Contacts*.
2. Add a contact by entering progressive abscissa (m) + elevation (m a.s.l.) +
   upper/lower layer.
3. The section regenerates automatically including the manual contact.

This lets you represent lenses, unconformities, faults, intrusions —
even when the boreholes don't intercept them directly.
