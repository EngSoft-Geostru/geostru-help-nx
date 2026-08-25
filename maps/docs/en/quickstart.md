# Quick start (5 minutes)

A full round trip: from a place name to a DXF file.

## 1 · Find the site

Type the place name or an address in the top bar and press **Enter**. The map
flies there and zooms in.

Top left on the map you will find the three base maps: **road**, **satellite**
and **terrain**. Switch them whenever you like — your drawing stays.

## 2 · Draw a track

In the sidebar pick **Polyline**, then click on the map to place the vertices.
While you draw, an elastic segment follows the cursor and the status bar at the
bottom counts the vertices.

To close: **double click** or **Enter**. To cancel: **Esc**.

!!! tip "Polygons"
    With the **Polygon** tool the first vertex turns white: clicking it closes
    the ring, as in any GIS.

## 3 · Fetch the elevations

Press **Elevations** in the top bar. The *Elevation* column of the table fills in
and the elevation range appears in the sidebar.

If you would rather have every new point arrive already sampled, tick **Sample
elevation on new points** in the sidebar.

!!! note "If something does not arrive"
    A message appears **only** if some elevation could not be retrieved, and it
    tells you how many points are affected. Those points are left without an
    elevation — they are not at sea level.

## 4 · Look at the profile

In the bottom dock switch to the **Elevation profile** tab: the chart draws
itself, provided the elevations are there.

## 5 · Export

In the sidebar choose the **Format** and press **Export**. For the CAD pick
**AutoCAD (DXF)**; for projected coordinates, **North/East/Elevation (UTM)**.

!!! info "Cost"
    Each export consumes **10 credits**, whatever the format. If the export
    fails, nothing is charged.

## Then

- Save the project to the cloud with **GeoDropbox**, from the top bar.
- **File › Load example** opens a ready-made track, if you want to try without
  drawing.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Maps%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/maps/docs/en/quickstart.md).*
