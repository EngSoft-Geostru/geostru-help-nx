# Frequently asked questions

**Does calculation use credits?**
No. On-screen calculation, diagrams, envelopes and checks are free. Word, DXF, CAD Tools and the assistant use credits. See [Credits](crediti.md).

**Why must I define combinations before stages?**
Because each combination must follow the same construction history. The scope selects stages to verify without creating different factors inside every stage.

**Can I change stratigraphy between stages?**
No. SPW NX uses one stratigraphy throughout the project. Variants in a desktop file are reported in the import report.

**Can I use different sections along the wall?**
No. The project has one type for the full height. A segmented desktop file requires the reference choice stated in the report.

**I defined an anchor but it is not active in the drawing. Why?**
A definition in the Elements step does not install it. Add the **Install anchor** event in the correct stage.

**What is the difference between preload and a combination factor?**
Preload is a force of the anchor or its prestressing event. The combination factor belongs to the matrix and derives from the combination rule.

**Why is there no deflection with LEM?**
LEM studies limit equilibrium and does not compute displacements. Use FEM for displacements and the SLS check.

**Why does a combination not appear in the envelopes?**
It may be disabled or incomplete. Check the outcome and warnings in the Calculation step.

**What does “Not calculated” mean?**
The check has no outcome. It does not mean “passed”. Check data, combination type and the limits stated on the page.

**Why have results become out of date?**
You changed one or more inputs after calculation. Calculate again before using results, report or results export.

**Why are imported results different from the desktop ones?**
Saved results are not imported. The new model handles stage history, combinations, seismic action and some data differently. Read the report and [Validation](validazione.md).

**The Download Word button is disabled.**
A complete and up-to-date calculation is missing. The message above the buttons says so. Calculate again and return to the step. The **Free preview** remains available.

**I pressed Computo NX but nothing happened.**
The browser may block the new tab. Allow pop-ups for the site and try again. If the service does not respond, a message appears and nothing is charged.

**Where can I find the method formulas?**
The manual describes assumptions, use and limits without reporting engine equations. For theory use the [public bibliography](metodi.md#bibliografia-essenziale).

**Can the assistant fill in missing data?**
No, it does not invent parameters or elevations. It can write data you provide and point out missing data.

**The project disappeared after a pause.**
The session expires after 30 minutes of inactivity. Reopen the saved `.spwnx` or the project from GeoDropbox.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/spw/docs/en/faq.md).*
