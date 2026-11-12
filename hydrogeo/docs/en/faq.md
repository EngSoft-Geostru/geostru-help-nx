# FAQ

## General

### Do I need to install anything?

No. Hydrogeo NX runs in the browser at
[nx.geostru.ai/hydrogeo](https://nx.geostru.ai/hydrogeo/), on Windows, Mac and Linux.

### Why is the map empty when I open the app?

There are more than 6,000 stations: the map shows the ones you search for. Open the
assistant and ask, for example, "Find stations in Calabria". See [AI assistant](assistente.md).

### Does Hydrogeo NX compute Gumbel, TCEV or rainfall curves?

No. Hydrogeo NX provides the data; the statistical analysis is in Runoff Lab NX, which imports
the series directly. See [Links with the other NX apps](integrazioni.md).

## Stations

### Where do the data come from?

From ISPRA (Hydrological Annals) and twelve regional services. The list is in
[Data sources and limits](fonti.md); every station shows its source in its sheet.

### I cannot find stations in my area

Widen the search radius or drop the filter on years of data. Some historical stations have no
coordinates and do not appear on the map, but the assistant finds them by name. If a source is
really missing, write to us: see [Data sources and limits](fonti.md).

### The station has no 1-hour data

Not every station has every duration. Historical stations often have only the 24-hour
maximum; short durations need a recording rain gauge. Look for a nearby station with "Hourly
rainfall" under **Data type**.

### How many years of data do I need?

The [relevance](mappa.md#relevance) helps: 20 years or more is good, 10 to 20 medium, under 10
low. For a robust statistical analysis aim for at least 20–30 years, or use a nearby station
with a longer record.

### Two stations with the same name: which one do I choose?

They are different stations, often an old Annals station and a new regional one. Compare
period, years of data and source in the sheet.

## Data and credits

### I closed the browser: do I have to unlock the station again?

Yes. An unlock stays active in the browser tab where you made it. Export the data you need
before closing. See [Access and credits](crediti.md).

### Is a repeated export charged twice?

Not if you repeat it identically shortly afterwards (within the same 15-minute window). Later
on it is a new export. An operation that returns no data is never charged.

### Is the PDF available in English?

No, the **PDF Report** is in Italian. For other uses export to CSV or Excel.

## Other apps

### How do I take the data into Runoff Lab NX?

In Runoff Lab NX: **Import → From Hydrogeo NX…**, search for the station and click it. See
[Links with the other NX apps](integrazioni.md).

### Does Runoff Lab NX open the PLV file?

No: Runoff Lab NX imports stations directly from Hydrogeo NX, with no file. The PLV is for the
GeoStru desktop software.

## Is your question missing?

[Write to us](mailto:info@geostru.ai?subject=Hydrogeo%20NX%20FAQ) or open a ticket from the
[assistant](assistente.md): we will add it here.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Hydrogeo%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/hydrogeo/docs/en/faq.md).*
