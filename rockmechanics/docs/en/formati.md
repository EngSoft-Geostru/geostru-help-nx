# File formats

Rock Mechanics NX works on a single **project file** and communicates with the survey tools upstream and with the calculation documentation downstream. This page summarizes what you can import and what you can export.

## The project file

The project file saves the entire state of the work: the **geostructural survey** (discontinuity sets with the ISRM parameters, $S_u$ and RQD), the **classifications** adopted with their characteristic parameters and the **stability verifications** set up.

It is a GeoStru NX project file in text format (JSON structure), designed to be reopened at any time to resume or update the processing: you can save a survey, return to it later to add a classification or revise a verification, and regenerate the report without re-entering the data.

!!! tip "A single file for the entire study"
    Keep the project file together with the field drawings: it already contains the survey, classifications and verifications, so it is sufficient to reconstruct the entire calculation process.

## Survey import

The geostructural survey does not need to be re-entered by hand. Rock Mechanics NX interfaces with two GeoStru tools dedicated to survey acquisition and processing:

- **eGeo Compass** — acquisition of orientations directly in the field (dip direction and dip of the discontinuities), using the smartphone as a digital compass-clinometer.
- **GMS (GeoMechanical Survey)** — processing of the geomechanical survey: joint sets, ISRM parameters and organization of the station data.

The discontinuity sets and orientations surveyed with these tools are imported into the app without manual re-entry, ready for classification and verifications. For the complete picture of the workflow see [Complete workflow](workflow.md).

## Export

Downstream of the calculation, Rock Mechanics NX produces the documentation of the study:

- the geomechanical **calculation report** in **Word** format, with the survey data, the adopted classifications, the characteristic parameters and the stability verifications;
- the **graphical drawings** of the survey and the verifications (projections and survey diagrams, verification schemes).

Details on the content and generation are in [Export and report](export.md).

## What you can import / export

| Direction   | Content                                    | Source / destination              |
|-------------|--------------------------------------------|-----------------------------------|
| Import      | Orientations and discontinuity sets        | **eGeo Compass**                  |
| Import      | Geomechanical survey (ISRM parameters)     | **GMS (GeoMechanical Survey)**    |
| Open        | Survey, classifications and verifications  | GeoStru NX project file           |
| Save        | Complete project state                     | GeoStru NX project file           |
| Export      | Geomechanical calculation report           | **Word** document                 |
| Export      | Graphical drawings (survey and verifications) | Images / diagrams              |

## Related resources

Example figures, field files and reference material are collected on the [Resources and sample files](risorse.md) page.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20Rock%20Mechanics%20NX).*
