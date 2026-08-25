# Sections and profiles

Maps NX derives an elevation profile in **two different ways**, which answer
different questions.

## Profile from the points

It puts the vertices you clicked in chainage order and plots their elevations.

- Abscissa: the running chainage of the coordinate table.
- Ordinate: the elevation of each vertex.
- The profile **jumps** from one vertex to the next: between two vertices it does
  not describe the terrain.

You get it by opening the **Elevation profile** tab in the bottom dock, or from
**Analysis › Section from points**.

## Section along the track

It resamples the drawn polyline at a **regular step** and asks for the elevation
at every sample. This is the section proper.

- The profile follows the terrain between the vertices too.
- The step adapts to the length of the track, aiming at about 200 samples: a
  fixed step on a 5 km alignment would produce tens of thousands of elevation
  requests.
- Every sample carries chainage, elevation, geographic **and** projected
  coordinates.

You get it from **Analysis › Section along track**. It needs a drawn polyline.

!!! tip "Which one to use"
    For a section that goes into a report, use **Section along track**. The
    profile from the points is rather a quick check on the elevations of the
    vertices you placed.

## Provenance

The chart title reports the length of the track, the sampling step and the source
of the elevations.

This is not decoration: **a section without its provenance cannot be verified**.
In a report you must be able to state where the elevations came from and at what
step they were taken.

## Exporting the profile

The **Section profile** format, in the export format list, produces the profile
file. See [Export and coordinates](esportazione.md).

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Maps%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/maps/docs/en/sezioni.md).*
