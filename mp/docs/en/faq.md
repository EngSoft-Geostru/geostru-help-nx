# FAQ

**Does MP NX compute pile groups?**
No. It computes the single pile and the single micropile: no group efficiency and no group
effect on settlements. The full list of what it does not cover is on the
[home page](index.md).

**Do I have to factor the loads, or does the program do it?**
You do. Loads are **design values**: MP NX does not apply γ~F~ to the actions. The name of
the combination is a label. See [Loads, combinations and design code](combinazioni.md).

**In which direction is F~x~ positive?**
From right to left. F~y~ is positive downwards and M is positive clockwise: it is the
convention of the MP desktop program. The action scheme above the pile head, in the preview,
shows you the direction before you calculate.

**Why does the Settlements tab say "No settlement computed"?**
The combination chosen in the **Settlement options** has no vertical load. Assign F~y~ in
that combination, choose another one, or enter the **Load** Q. See
[Settlements](cedimenti.md).

**Why is the resisting moment lower than in the design charts?**
With **NTC 2018 (non-dissipative seismic)** M~u~ is the **first-yield** moment, lower than
the moment at failure: it is intended. To compare with the charts choose **NTC
(ultimate)**. See [Sections and reinforcement](armature.md).

**The FEM analysis and Sections and reinforcement tabs are empty.**
The FEM analysis is not enabled. Tick **Run the FEM analysis and the section design with
Calculate** in the **Reinforcement and FEM analysis** card and recalculate. If it was
enabled, read the messages at the bottom of the **Ultimate load** tab: the FEM may have
failed, and in that case its credit has not been charged.

**Broms' H~max~ is missing.**
M~y~ is 0 and the FEM analysis is off, so the program has no ultimate moment to use. Enter
M~y~ in the **Materials and reinforcement** card or enable the FEM.

**I entered c~u~ but the result does not change.**
Check that you ticked **Undrained condition** in the layer properties. Without the box the
layer is computed in the drained condition with φ and c′. See
[Stratigraphies and water table](stratigrafia.md).

**The calculation stops with a message about the water table.**
Two causes: the water table depth coincides with a layer boundary, or a layer below the
water table has no saturated unit weight γ~sat~.

**My results differ by 1–2 % from those of the desktop program.**
It is almost always the materials archive: unit weight and elastic modulus of concrete
differ between the SI archive and the technical archive of the desktop. Put the values you
want to compare in the project archive. See [Code validation](validazione.md).

**Does changing the cage rules cost credits?**
No. Stock bar, lap, starter bars, spiral and stiffening rings redraw the cage from the
result already computed, with no recalculation and no charge.

**Did I pay for an operation that failed?**
No. Credits are charged only when the operation succeeds: calculation without errors, file
produced, assistant answer delivered.

**Where are the example projects?**
Under the **?** button, **Resources** tab: they download as `.mpnx` files and open with
**File → Open**. See [Example projects](esempi.md).

**Does the project stay saved if I close the browser?**
The app keeps the state in the session while you work, but the real project is the `.mpnx`
file. Save it with **File → Save** or to **GeoDropbox** before closing.

**Which languages are available?**
Interface and report are in Italian and English. Change language from the selector at the
top right.

**The 3D view does not appear.**
It needs WebGL. If the browser does not support it or has it disabled, the app says so in
place of the view.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20MP%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mp/docs/en/faq.md).*
