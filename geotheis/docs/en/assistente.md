# AI assistant

The **Assistant** button in the top bar opens the chat. The assistant is an artificial intelligence system that works on the open
project: it reads data and results, explains methods and limits to you and, on your request, writes data into the tabs or applies
choices to the results. If you ask, it tells you it is an artificial intelligence.

## What it can do { #che-cosa-sa-fare }

**Read and explain** (does not change the project):

- read the project: general data, site, aquifer and elevations, well, stratigraphy, piezometers, tests and readings;
- read the engine results: methods applied and not applicable with the reason, values with reliability and warnings, comparison,
  proposed design values and allowable discharge;
- explain a method in detail: parameters with the 95 % interval, values per series, for Cooper-Jacob the interval used and the
  maximum u;
- tell you, for each Cooper-Jacob series, which segment is in use and why;
- search the registered wells in the ISPRA archive (Law 464/84) around the georeferenced well;
- consult this manual to answer about commands, warnings and messages.

**Write data**, when you ask:

- job data, aquifer and well type, elevations and geometry;
- stratigraphy, completion (borehole, casing, annulus, well head chamber, pump, levels) and piezometers;
- step-drawdown, pumping and recovery readings, including those **pasted in the chat** from Excel, CSV or a datalogger: it reads them
  with the same importer as the Test tab and summarises how it interpreted times, units and columns;
- the **known critical discharge** (Q~c~, s~c~ and assumed R), only if you give it the values;
- the well position from coordinates in WGS84, UTM or Gauss-Boaga (and the other systems of the Well tab).

You can also attach a document with the chat paperclip (test report, field readings, stratigraphy, completion diagram): the assistant
writes into the project the data it finds, without filling in those that are missing.

**Choices on the results**: Cooper-Jacob interval, excluding or restoring points, type-curve adjustment for Theis or Hantush,
confirmation of the design values (the proposal, those of a method, or values you give) and of the discharge. These are the same
choices you make by hand in the [Results](risultati.md) tab.

## It proposes, you decide { #propone-tu-decidi }

- **Choices on the results are proposals.** The assistant first shows you the effect calculated by the engine (for example the T
  that would be obtained with a different interval) and applies it to the project only if you explicitly ask it to.
- **It writes data when you ask**, without a further confirmation: afterwards it summarises what it wrote and where. Always check the
  tabs.
- **The numbers are calculated by the engine.** The assistant reads them and quotes them with the unit, the method they come from and
  the reliability; it does not estimate them and does not do its own calculations.
- **It does not delete anything.** Layers, completion and readings are added; it replaces them only if you explicitly ask. Piezometers
  are added or corrected, never removed: to remove one use the Well tab. Excluding a point does not delete the reading.
- **It does not generate the Word report or the DXF**: you download them from the [Report](relazione.md) tab.

After a change by the assistant the page refreshes by itself. While it is working, the project is its own: if you try to change
something, *The assistant is working on the project: wait until it has finished and try again. Nothing was changed.* appears.

!!! tip "Tip"
    The chat quick actions are a good start: **Explain the results**, **Is the Cooper-Jacob segment right?**, **Theis or Hantush:
    which one?**, **Are there registered wells nearby?**

## Cost and limits { #costo-e-limiti }

- Each message to the assistant costs **3 NX credits**.
- A message that ends in an error, or that produces no answer, **is not charged**. What the assistant had already written into the
  project before the error stays.
- Resending the same message on the same project after an error is a new attempt; if the project has changed in the meantime it is a
  new job.
- A message can be at most 20,000 characters long, attached file included.
- In one message the assistant performs a limited number of operations. If it reaches the limit it tells you: what it has done is in
  the project, write to it to continue.
- If the session has expired, or if another message is still in progress, the message is not sent and not charged.
- There is a monthly usage limit per application: once it is reached, the message is not charged.

## Support { #assistenza }

From the chat you can open a support ticket (quick action **Open a support ticket**): while the ticket is open your messages go to
the operator, not to the assistant.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20GeoTheis%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/geotheis/docs/en/assistente.md).*
