# Workflow

A complete project, in the order of the tabs. The calculation runs at every change and the results always match the data on screen: there is
no «Compute» button, and switching tabs recomputes nothing.

1. **Site** — Fill in the general data (description, client, construction site, designer, geologist, microzonation study, date) and the firm
   that signs the report. Place the site: the address search uses OpenStreetMap and you can drag the marker. Set the nominal life and the use
   class of the structure: they are for information only, the comparison is always at 475 years. Get the seismic parameters from the service,
   from a GeoStru PS report or by hand. → [Site](sito.md)
2. **MS3 spectrum** — Import the file of the study with the preview. Check the warnings (discarded lines, suspect unit, missing point at 0.01 s)
   and the regularisation table. → [MS3 spectrum](spettro-ms3.md)
3. **Comparison** — Choose the subsoil and topographic categories of the building site and the periods T~min~ and T~max~ of the building. Read the
   value of the two conditions, the outcome and the warnings. → [Comparison](confronto.md)
4. **Report** — Free preview, Word for credits, free CSV. → [Report and credits](relazione.md)
5. **Save** — The project lives in a session on the server: save it to a `.rsl3anx` file (File → Save) or to GeoDropbox. → [Files and GeoDropbox](file.md)

You can also open a project of the desktop program (`.rs3`, `.rs3a`): the app reads its inputs and recomputes everything according to the text
of the Ordinance.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20RSL%20III%20A%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/rsl3a/docs/en/workflow.md).*
