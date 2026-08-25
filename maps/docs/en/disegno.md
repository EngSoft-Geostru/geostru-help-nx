# Drawing on the map

Three tools — point, polyline, polygon — and a handful of gestures.

## The tools

| Tool | What it is for | Minimum |
|---|---|---|
| **Point** | standalone points: boreholes, benchmarks, stations | 1 |
| **Polyline** | a track: road, section line, alignment | 2 vertices |
| **Polygon** | an area: survey perimeter, mesh area | 3 vertices |

Pick them from the sidebar or from the **Draw** menu.

## The gestures

| Gesture | Effect |
|---|---|
| click on the map | places a vertex |
| double click | places the last vertex and **closes** the geometry |
| **Enter** | closes the geometry |
| **Esc** | cancels the drawing in progress |
| click on the first vertex (polygon) | closes the ring |

While you draw, a dashed segment follows the cursor: it shows where the next side
will fall, and on a polygon the closing side as well. The status bar counts the
vertices and reminds you how to close.

!!! tip "A double click places, it does not discard"
    Double-clicking on a new spot makes that spot the final vertex. Double-click
    **on top of the last vertex you placed** and the geometry closes without
    duplicating it.

## Editing what you drew

- **Drag a vertex** to move it: table, distances and area update.
- **Zoom to a point** and **Delete** are the two buttons at the end of each row
  in the coordinate table.
- Removing a vertex renumbers the remaining ones, so the track does not fall
  apart. If you drop below the minimum (2 for a polyline, 3 for a polygon) the
  whole geometry is removed.
- **Clear** empties the map. It cannot be undone, so you are asked to confirm.

## Drawing without clicking

You do not have to draw by hand:

- **File › Open** reloads a saved project (`.gmap`).
- **File › Load example** opens a ready-made track.
- **GeoDropbox** reopens a project from the cloud.
- The **AI assistant** draws for you: paste it a list of coordinates or attach a
  document containing them, and it places them on the map. It converts degrees,
  minutes and seconds on its own, and when the column order is ambiguous it
  states which reading it assumed instead of guessing silently.

## The measurements

The **Measurements** panel in the sidebar updates points, total distance, area
and elevation range live. The same values appear in the status bar at the bottom:
they are always the same number, computed once.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Maps%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/maps/docs/en/disegno.md).*
