# The complete workflow

A real case, from the project site to the rainfall curve and the design of the works.

```text
Atlante NX          Hydrogeo NX                     Runoff Lab NX               HID NX
──────────          ───────────                     ─────────────               ──────
project site      → nearby stations → annual     → probability              → attenuation for
                    sheet and          maxima       distributions, curve       hydraulic
                    relevance                       h = a·tⁿ, design storms    invariance
```

## 1. The site

If you use [Atlante NX](https://help.nx.geostru.ai/atlante/en/), its link to Hydrogeo NX
opens the map **centred on the site** and marks it with the "Sito (Atlante NX)" marker.
Otherwise start from the name of the town or from the coordinates.

## 2. Candidate stations

Ask the assistant for the stations around the site, with a radius and a minimum record
length:

```text
Rain gauges within 20 km of 43.11, 12.39 with at least 20 years of data
```

You can also filter by region, province, basin, source, instrument and elevation. See
[AI assistant](assistente.md).

## 3. Choosing the station

For each candidate open the sheet and compare:

- **distance and elevation** from the site, and whether it lies in the **same basin**;
- **years of data** and **period**: a long and recent record is better;
- **relevance**: good from 20 years, medium from 10 to 20, low under 10;
- **data types**: maxima by duration need the "Hourly rainfall" entry.

Some stations hold daily rainfall only, with no maxima by duration: they are fine for monthly
precipitation, not for the rainfall curve.

## 4. The data

Unlock the station and check the [tables](dati.md): missing years, dashes in the short
durations of the oldest years, extreme events. The values are those published by the source,
without corrections.

## 5. The export

From the **Export** menu choose the format: CSV or Excel for your own calculations, **PDF
Report** to attach to the technical report, **PLV GeoStru** for the GeoStru desktop software.
See [Exports and formats](formati.md).

## 6. The statistics

In [Runoff Lab NX](https://help.nx.geostru.ai/runofflab/en/) use **Import → From Hydrogeo
NX…**, search for the station by name and import it: the series of maxima by duration reach
the study without going through a file. There you fit Gumbel, GEV, Pearson III or TCEV and
obtain the curve h = a·tⁿ.

## 7. The design

The **a** and **n** parameters of the curve are the rainfall data that
[HID NX](https://help.nx.geostru.ai/hid/en/) needs to size the attenuation works required by
hydraulic invariance.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Hydrogeo%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/hydrogeo/docs/en/workflow.md).*
