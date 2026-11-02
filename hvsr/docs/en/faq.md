# FAQ

## My project has disappeared

The project lives in the session and expires after 30 minutes of inactivity or at a restart. Save the `.hvsrnx` often with **File → Save**.

## I have no file to try

Choose **File → Open the example**: it is a 20-minute recording with a ready-made model. The [Tutorial](tutorial.md) uses it step by step.

## Can I open desktop projects?

Yes, `.hvsrx` files. `.ehv` files must first be saved as `.hvsrx` from the desktop program.

## My instrument is not among the formats

Export from the instrument's software to SAF or text. SEG-2 is read directly.

## f~0~ differs from my old project

Curves saved in projects from years ago do not match those today's desktop program recalculates from the same data. In addition HVSR NX always averages over the included windows. See
[Validation](validazione.md).

## The filter keeps more windows than the desktop program

That is intended: the desktop filter had a defect and deleted good windows. Read f~0~ again after the filter anyway.

## f~0~ equals f min

The maximum is on the edge of the band: it is not a peak. Widen the band or narrow it around the peak you care about.

## The curve is reliable but the peak is not clear

These are two different judgements: the measurement is good and the peak is low or broad. It may indicate a low contrast: report f~0~ with that reservation.

## Search gives a different model each run

It depends on the starting model and the seed. Turn on **Fixed seed** to repeat the same run. If different models have a similar misfit, the data cannot tell them apart.

## Can I get the category from H/V alone?

No, not reliably: the curve depends on the ratio between V~s~ and H. Fix at least one layer with independent data.

## The category differs from the desktop program

The V~s,eq~ calculation was corrected: see [Validation](validazione.md).

## Can I combine HVSR and MASW?

Joint inversion is not yet in HVSR NX. For now use the [MASW NX](https://help.nx.geostru.ai/masw/) result to fix the layers.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20HVSR%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/hvsr/docs/en/faq.md).*
