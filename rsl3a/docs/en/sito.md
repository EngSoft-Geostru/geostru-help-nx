# Site

## General data

Description, client, construction site, designer, geologist, the microzonation study the spectrum comes from, and date go into the report. The
**engineering firm** (heading, address, contacts, VAT number) appears on the cover. Press **Save** to write them into the project; when you
switch tabs the form saves itself.

## Position

Type an address or a place and press **Search**, or click on the map or drag the marker: latitude and longitude (WGS84) are updated. The
coordinates are used by **Compute from site**.

## Seismic parameters

The Ordinance compares the MS3 spectrum with the code spectrum for **T~R~ = 475 years**. For this reason:

- **Compute from site** queries the GeoStru Seismic Parameters service with **nominal life 50 years and class II**, whatever the nominal life and
  class of the structure: the SLV row thus has T~R~ = 475 years;
- **Import GeoStru PS report** reads the text report of the Seismic Parameters program (UTF-16 too). If the report was made with another
  nominal life or class, the SLV row is not at 475 years and the app tells you;
- you can fill in the table **by hand** and apply it with **Apply values**. A row left completely empty means «no data».

The **SLV** row is the one used by the comparison and is highlighted. The other rows are for information and go into the report.

!!! note "Nominal life and use class"
    They are for information only. Class I: according to the Ordinance the simplified approach is allowed in any case. Classes III and IV: the
    comparison is still made with the 475-year spectrum.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20RSL%20III%20A%20NX) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/rsl3a/docs/en/sito.md).*
