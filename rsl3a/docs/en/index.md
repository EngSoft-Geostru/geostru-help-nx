# RSL III A NX

**RSL III A NX** applies **Ordinance no. 55 of 24/04/2018** of the Extraordinary Commissioner for the reconstruction (2016 earthquake), Annex 1 and
Appendix 1. In municipalities with a **level 3 Seismic Microzonation (MS3)** study, the designer must check whether the response spectrum of the
study is more severe than the one given by the **simplified approach** of NTC 2018. RSL III A NX performs this check and puts it in a Word
report.

The work is short: one file (the MS3 spectrum), the seismic parameters of the site, the subsoil category and two periods of the building. The
server computes the rest, at every change.

## What it does

1. **Regularises** the MS3 spectrum into the four-branch shape of NTC (Appendix 1): T~A~, SA~m~, T~V~, SV~m~, T~B~, T~C~, T~D~, a~max~, F~0~.
2. Computes the **NTC 2018 simplified spectrum** of the site for **T~R~ = 475 years**, η = 1, horizontal component.
3. **Compares** the two spectra over the interval **[T~min~, 2·T~max~]** with the two conditions of the Ordinance: pointwise exceedance above 30 %
   and exceedance of the integral above 20 %.
4. Gives the **outcome**: simplified approach can be used, further investigations required, or comparison not applicable (2·T~max~ > 1.1 s).
5. Produces the **Word report** with the text of the Ordinance, the data, the charts, the parameters and the value of the two conditions.

## Who it is for

Designers and geologists working on the reconstruction in the areas hit by the 2016 earthquake, who must decide for a building whether to use
the code spectrum or whether further investigations are required and, if needed, a local seismic response analysis (with GeoStru RSL III).

## The four tabs

| Tab | What you do |
|---|---|
| [Site](sito.md) | general data, position on the map, parameters a~g~, F~0~, T~c~* |
| [MS3 spectrum](spettro-ms3.md) | import of the study file, regularisation |
| [Comparison](confronto.md) | categories, T~min~ and T~max~, chart, conditions, outcome |
| [Report](relazione.md) | preview and Word |

Start from the [Quick start](quickstart.md). Before using the outcome in a project, read [Validation and limits](validazione.md).

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20RSL%20III%20A%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/rsl3a/docs/en/index.md).*
