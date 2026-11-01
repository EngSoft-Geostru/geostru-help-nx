# FAQ

## Traces and formats

**Which trace files can I load?**
SEG-2, SEG-Y, SU (Seismic Unix), Ambrogeo (`.dta`), SARA Doremi (`.drm`), Dolang and ASCII with
the traces in columns, up to 64 MB per file and 512 traces per project. Easy-MASW desktop
`.mswx` projects are opened with **File → Open…**. See [Traces](tracce.md#import-traces).

**My format is not in the list. What do I do?**
Export the traces from the instrument software to SEG-2, SEG-Y or a text file with one column
per trace. If you already have the dispersion curve, you can also paste it straight into the
picking table.

**I recorded two lines offset by half a spacing. How do I merge them?**
Load the first, then choose **Interleave** in **Add** and load the second: the traces
alternate. Then halve dx in the **Acquisition** card.

**I have several shots on the same geometry. Can I add them up?**
Yes: load the first, then choose **Sum** and load the others, one at a time. The traces are
added sample by sample (stacking).

**A trace is noisy or dead.**
Untick **Use in spectrum** in its row: the spectrum ignores it, and the phase accounts for the
real position of the other geophones.

**I loaded the wrong file.**
**Undo** (Ctrl+Z) in the **Traces** card goes back to the previous state. To start over there
is **Remove all**.

## Spectrum and picking

**The map is all red at low frequencies.**
Each column is normalised to its maximum: where the signal is weak, noise also turns "red".
Raise **f min** to the useful lower limit of the geophones (often 3–5 Hz) and recompute.

**Automatic picking skipped a stretch, or put a stretch on the wrong mode.**
That is normal: it follows the ridges it sees. Complete by hand with **Add**, move points with
**Move**, change a point's mode from the table. The [synthetic model](spettri.md#synthetic-model)
helps tell which ridge is the fundamental and guides the automatic mode assignment.

**How do I tell whether a ridge is a higher mode?**
A higher mode lies at higher velocities than the fundamental at the same frequency and
usually appears at high frequencies, where the fundamental loses energy. Comparing with the
curves of the synthetic model and a sudden upward jump of the ridge are the most useful clues.

**How deep does the survey reach?**
Of the order of half the longest reliable wavelength in the picking. Move the cursor over the
map: the line at the bottom shows λ = v/f.

**I lost the picking by mistake.**
**Undo** (Ctrl+Z) goes back up to 100 changes, as long as you do not change tab.

## Inversion

**Where do I start with the initial model?**
From **Propose layers**: thicknesses from the picking wavelengths and V~s~ from the curve.
Then adjust the bounds where you have information (a borehole, the water table depth).

**Every time I rerun the inversion the profile changes a little.**
That is expected: the search starts from random points and the inversion is not unique. If
different profiles have similar misfit, the picking is not enough to tell them apart: compare
the solutions with **Sort by** and choose the most plausible.

**What does "Modes to display" mean?**
How many theoretical curves to draw for the solution on screen. It does not change the
calculation: the inversion always uses every mode in the picking.

**The inversion stopped halfway.**
If you closed the page or pressed **Stop**, the run is neither delivered nor charged. If you
changed picking or layers during the calculation, the result was discarded, with no charge.
Run it again.

**Run inversion says the calculation is too long.**
The product of iterations, picked points and layers has a cap: reduce one of the three.

## Category and results

**The category does not appear: "The velocity falls exactly on the limit between two categories".**
V~s,eq~ is exactly 100, 360 or 800 m/s, a value the NTC table assigns to no range. Check the
model: a minimal difference in the layers is enough.

**Why did the desktop give E and MASW NX gives C on the same project?**
A rounding defect of the desktop in computing H: with H = 29.999998 m instead of 30 the site
appeared to have bedrock within 30 m. See
[Differences from the desktop program](validazione.md#differences-from-the-desktop-program).

**Can I use G~0~ or E in a settlement calculation?**
Not directly: they are small-strain dynamic moduli. They must be reduced according to the
strain level of the structure.

**NSPT or Qc appear as N/A.**
The layer's V~s~ takes the correlation outside its range (NSPT above 100, Qc above 5,000 kPa).
The half-space has no correlations because it has no mid-depth.

**The unit weight is in kN/m³ but in the parameter table I see 1800.**
On screen weights are in kN/m³; the parameter table shows the density ρ in kg/m³, the value
that enters the modulus formulas (17.65 kN/m³ ↔ 1,800 kg/m³).

## Report, files and credits

**The report comes out in Italian.**
It is written in the interface language: change the language from the selector at the top and
generate it again.

**I generated the same report twice. Did I pay twice?**
No: the same document, with the same data and language, is not charged again.

**I closed the browser and the project is gone.**
The project lives in the session for 30 minutes after the last activity. Reopen the saved
`.maswnx`, or the project from GeoDropbox. See [Files](file.md).

**The saved file does not contain the traces.**
The samples exceed 30 MB: the file carries only the references to the traces on the server.
Always keep the instrument's original files to load them again.

**How much does an inversion or a report cost?**
Prices are in the price list on [geostru.ai](https://www.geostru.ai/). An operation that fails
costs nothing. See [Credits](relazione.md#credits).

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20MASW%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/masw/docs/en/faq.md).*
