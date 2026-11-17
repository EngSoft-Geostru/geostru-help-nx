# Frequently asked questions

More questions about interpreting the results are in [Results → Frequently asked questions](risultati.md#domande-frequenti).

**How much does it cost to use GeoTheis NX?**
Data, calculations, results, charts, on-screen drawings, the map and the report preview are free. The Word report
(10 credits), the well DXF (10) and each message to the assistant (3) cost NX credits. A failed operation is not charged,
and regenerating the same document with the same data is not charged again. See [Report and credits](relazione.md#crediti).

**Do I have to press a button to calculate?**
No. The results update automatically whenever the data or choices change, in the [Results](risultati.md) tab.

**Why are my results different from those of the desktop program?**
The desktop version had some formula errors (for example, the Cooper-Jacob T was 24 times smaller on CELICO, and the Theis
type curve was shifted), which were corrected in the desktop version on 15/11/2026. GeoTheis NX uses formulas from the
literature and recalculates everything: results saved in the `.wtax` file are not imported. Every difference is explained in
[Validation](validazione.md#differenze-dal-programma-desktop).

**Can I open my `.wtax` projects?**
Yes, with **File → Open…**. The well, elevations, stratigraphy, piezometers, steps, pumping and recovery readings, and the
choices made in the desktop version are imported. Check the notes that appear after opening, particularly the aquifer type
and recovery times. The desktop coordinates are local: if you need the map and nearby wells, position the well in the
[Well](pozzo.md) tab. Details in [File](file.md#progetti-del-programma-desktop-wtax).

**I closed the browser and the project is gone.**
The project remains in the session for 30 minutes of inactivity. Reopen the `.geotheisnx` file you saved, or the project on
GeoDropbox. Save often with **Save** (Ctrl+S).

**I only have a constant-rate test on the well, with no piezometers. What do I get?**
Indicative T from Cooper-Jacob and from recovery; no S, because it is not reliable when derived from the pumping well. The
proposed allowable discharge is that of the test. For S and the radius of influence, readings from at least one piezometer
are required.

**I did not perform a step-drawdown test, but I know the critical discharge.**
Enter Q~c~, s~c~ and the assumed radius of influence in the *Known critical discharge* box of the [Test](prove.md) tab: the
program performs the single-well calculations, which give indicative T and K, and proposes 0.9·Q~c~ as the allowable
discharge, stating that Q~c~ was provided by you. If there is also a valid step, the step-drawdown test takes precedence.

**Why does Hantush not appear?**
Hantush is calculated only if the aquifer type is leaky (Well tab) and there are pumping readings from a piezometer. If the
fitting finds negligible r/B, leakage is not visible in the data and the values coincide with Theis.

**Why does an unconfined aquifer produce a warning with Theis and Cooper-Jacob?**
Those methods assume a confined aquifer. The program still calculates, but without correcting the saturated thickness: the
values are reliable as long as the drawdown is small compared with H~1~. See [Theoretical background](teoria.md#validita-dei-risultati).

**Are recovery times measured from the start or from shutdown?**
From pump shutdown (t′). Enter the shutdown time in the Test tab; if it is missing, the program assumes the last pumping
reading. If you paste clock times, enter the shutdown time.

**What does “to be verified” mean for some methods for partially penetrating wells?**
It means that the formula, taken from the desktop program, has not yet been verified against the reference text (Muskat,
Girinski, “L/b − L/2r” and Chiesa's types B and C). The program calculates it and the report states this: use it only for
comparison.

**Can the assistant decide the design values for me?**
No. It shows you the effect of the choices and applies them only if you explicitly ask it to; the engine calculates the
numbers. The choice of design values and of the discharge to request remains yours. See [Assistant](assistente.md).

**The report says “no boreholes recorded within 500 m”. Is that sufficient for the application?**
No. The ISPRA archive contains only boreholes reported under Law 464/84 and is incomplete: pre-existing wells must be
verified on site and with the competent authorities.

**What language is the report produced in?**
In the interface language, Italian or English. In the English document, texts written by the engine (method names,
explanations, warnings) remain in Italian, and the cover page states this.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20GeoTheis%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/geotheis/docs/en/faq.md)*
