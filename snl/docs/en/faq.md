# Frequently asked questions

**Does the analysis use credits?**
No. The analysis, the results and the on-screen drawings are free; the Word report, the DXF drawing and the assistant messages use credits. See [Credits](crediti.md).

**Where do I enter the excavation stages?**
Nowhere: SNL NX creates one per nail, in order of depth. A stage excavates down to halfway between one nail and the next, the last one down to the toe. See [Theory](teoria.md#excavation-stages).

**Why are the nails in the analysis in a different order from my list?**
The analysis always takes them in order of depth. The list in the Nails step stays as you wrote it; **Sort by depth** reorders it.

**Are diameters in millimetres?**
No, in metres: a 32 mm bar is written 0.032. If a value is not plausible, the Nails step flags it.

**Why is the failure check of a nail the same in every stage?**
The nail force is computed once, on the finished wall; in each stage the effective length changes, so pull-out changes but tensile failure does not.

**I chose Rankine but the analysis uses Coulomb.**
With kh > 0 the thrust is always computed with Coulomb / Mononobe-Okabe, whatever the choice.

**How do I choose kh and kv?**
In the Project step: calculate the site parameters and apply the proposal kh = βm·amax/g, kv = ±0.5·kh, or type them by hand. The choice remains yours; the sign of kv can change the outcome.

**The factor A of the load does not change with the category.**
That is intended: the category describes the load, the factor A is typed by hand for each load.

**Why does sliding fail with a high water table?**
The water thrust on the inner side of the block and the uplift at its base greatly reduce the margin, and the facing is taken as impermeable. Check the water table depth, Bl and the foundation soil parameters.

**Does SNL NX check global stability?**
No. For surfaces passing behind or below the nails use a slope stability program, such as GeoStru Slope. See [Validation and limits](validazione.md).

**What about the facing section?**
SNL NX gives pressure, shear and moment; the check of the reinforced concrete section and of the nail head is done separately.

**Why is the result «out of date»?**
You changed a value that enters the analysis (levels, soil, loads, nails, factors, kh, kv). Press **Calculate** again. Changing general data, design office or site does not make the result obsolete.

**After importing a .snl the results do not match those in the file.**
Saved results are not imported: they are recalculated. Some differences come from corrections to the method. Read the report and [Validation and limits](validazione.md).

**I lost the project.**
The project stays in the session for 30 minutes of inactivity. Save it often to a `.snlnx` or to GeoDropbox.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/snl/docs/en/faq.md).*
