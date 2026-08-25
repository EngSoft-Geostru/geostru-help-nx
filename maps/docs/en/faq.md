# FAQ

### How accurate are the elevations?

They come from a digital terrain model of global coverage, typically on a grid of
about 30 metres. They suit feasibility and preliminary design; they do not replace
a topographic survey. See [Elevations and terrain model](quote.md).

### A point shows elevation 0.00 — is it at sea level?

Not necessarily. Zero is also the value of a point that was **never sampled**, or
whose elevation could not be retrieved. Fetch the elevations again and read the
status bar: it says how many points were actually updated.

### In what reference system do I get the data?

The map works in geographic WGS84. The NEZ and DXF exports project to UTM. See
[Export and coordinates](esportazione.md).

### Can I import a track I already have?

Yes. Paste or attach a list of coordinates, or hand the assistant a document
containing them: it extracts and draws them. Projects saved in the cloud reopen
exactly as you left them.

### What is the difference between the two ways of making a section?

The profile from the points puts the vertices you clicked in chainage order. The
section along the track resamples the line at a regular step, so it follows the
terrain between the vertices too, and it carries its step and elevation source
with it. See [Sections and profiles](sezioni.md).

### How fine should the mesh grid be?

No finer than the data underneath it. As you change rows and columns, Maps NX
shows the resulting spacing in metres: once it drops well below the resolution of
the model, the extra nodes add no information.

### Does the DXF open in my CAD?

Yes: the export writes points and polylines as real entities, not as an image.

### The drawing does not appear on the map

Switch the base map or nudge the view: the drawing is redrawn as soon as the map
is ready. If it persists, reload the page — no work is lost, because the session
is preserved.

### How is it billed?

Maps NX runs on GeoStru NX **credits**: you buy a package and each chargeable
action draws from it. If the action fails, nothing is charged.

### Which languages is it available in?

The interface is in Italian, English, German, French, Spanish, Romanian and
Danish. Switch it from the selector at the top right.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Maps%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/maps/docs/en/faq.md).*
