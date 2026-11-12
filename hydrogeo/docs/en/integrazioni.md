# Links with the other NX apps

Hydrogeo NX is the data step of a chain that goes from the project site to the design of the
works, with **one account** and **one credit wallet**.

```text
Atlante NX → Hydrogeo NX → Runoff Lab NX → HID NX
  site         rainfall       statistics and   hydraulic
               data           curve h = a·tⁿ   invariance
```

## Atlante NX → Hydrogeo NX

In [Atlante NX](https://help.nx.geostru.ai/atlante/en/) you describe the project site. Among
the apps suggested for the hydraulic, agronomic and geological profiles is Hydrogeo NX: the
link opens the map **centred on the site**, with the red **Sito (Atlante NX)** marker.

From there ask the [assistant](assistente.md) for the nearby stations, for example "Rain
gauges within 20 km of the site with at least 20 years of data".

## Hydrogeo NX → Runoff Lab NX

[Runoff Lab NX](https://help.nx.geostru.ai/runofflab/en/) runs the statistical analysis that
Hydrogeo NX does not.

1. In Runoff Lab NX open **Import → From Hydrogeo NX…**.
2. Search for the station by name and press **Search**.
3. Click the station: the series of **annual maxima by duration** reach the study, together
   with the station details.

There is no file to download and upload again. Stations with daily rainfall only appear
greyed out, with a "daily rainfall only" note, because they have no series of maxima to
analyse.

In Runoff Lab NX you then fit the probability distributions (Gumbel by moments or maximum
likelihood, GEV, Pearson III, TCEV at levels 0 to 3) and obtain the rainfall
depth-duration-frequency curves h = a·tⁿ, design storms and hydrographs.

Importing a station uses Hydrogeo NX credits; an import that brings no series is not charged.

## Runoff Lab NX → HID NX

The **a** and **n** parameters of the curve are the rainfall data that
[HID NX](https://help.nx.geostru.ai/hid/en/) needs to size the attenuation works required by
**hydraulic invariance**. You enter them by hand in HID NX, in the **Rainfall
depth-duration-frequency curve** section.

## GeoDropbox NX

Runoff Lab NX studies are saved in **GeoDropbox NX**, the GeoStru cloud for projects, next to
the other project files.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Hydrogeo%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/hydrogeo/docs/en/integrazioni.md).*
