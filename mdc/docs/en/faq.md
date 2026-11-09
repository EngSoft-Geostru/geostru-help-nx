# FAQ

**Can I open my MDC desktop projects?**
Yes, `.mdcx` files open with **File → Open…** or from GeoDropbox. The inputs are imported and the results recalculated. See
[Files, desktop projects and GeoDropbox](file.md).

**Why are the safety factors different from the desktop?**
Where the desktop was wrong MDC NX corrects it: with the water table (uplift), with the passive thrust, with the seismic action. The list is in
[Validation and limits](validazione.md).

**Which codes can I use?**
The first release computes with NTC 2018, NTC 2008 and the Eurocodes. The other desktop codes are read from the files and stay in the
project, with a warning; their calculation is coming.

**Can I change the combinations?**
The combinations generated from the code are read-only; **Customise**, in the Load combinations step, copies them into the project and makes
them editable. **Back to the code** regenerates them.

**The seismic combinations have k~h~ = 0: why?**
The wall coefficients have not been written yet. In the Code and seismic action step press **Calculate from the site** and then **k_h and
k_v from the site parameters (ULS-LS)**, or type them by hand. If the site parameters are already there, the calculation uses the site
k~h~ and k~v~ for the seismic combinations left at zero anyway, and says so in the warnings. See [Code and seismic action](sisma.md).

**The wall fails in sliding: what do I do?**
Widen the base, choose the foundation with shear key or incline the founding plane. Count on the passive thrust at the toe only if the soil
in front of the wall will stay in place for the whole life of the structure. See [Combinations and checks](verifiche.md).

**How do I enter the loads of the front shelf?**
As point loads in the [Loads](carichi.md) step, with the point of application on the shelf.

**Can I edit the bars by hand?**
Not yet: the reinforcement is always designed on the envelope, within the limits of the "Design reinforcement" panel. Manual editing is
coming.

**Gabions, counterforts, global stability?**
Not yet: they come with the second release. Meanwhile global stability must be checked separately with a slope stability program, as the
report also says.

**Where do the seismic parameters come from?**
From the site coordinates, with the GeoStru Seismic Parameters service. See [Code and seismic action](sisma.md).

**What does it cost?**
Modelling, calculation and checks are free; Word report, section DXF and messages to the assistant use credits. A failed operation is not
charged, and regenerating the same document with the same data is not charged again.

**Is the project saved automatically?**
No: the project lives on the server while you work and expires after a period of inactivity. Save it as `.mdcnx` or to GeoDropbox.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20MDC%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mdc/docs/en/faq.md).*
