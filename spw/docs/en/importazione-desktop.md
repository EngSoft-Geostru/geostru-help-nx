# Desktop import

SPW NX opens `.spwx` projects from the desktop program and converts them to the native model. The original project is not modified.

## How to import

1. Save current work if you want to keep it.
2. Choose **File → Open…** and select the `.spwx`.
3. Wait for the conversion.
4. Read the **Import report** in the **Project** step.
5. Check the ten steps and calculate again.

You can open an example from the **File** menu: it follows the same import path and receives the same report.

## The import report

The report retains file name, date, summary and individual notes. It remains associated with the project when you save it as `.spwnx`.

| Group | Meaning |
|---|---|
| Not imported | data that do not enter the native model |
| Assumed | choice made to represent a desktop value |
| Note | information about conversion, without direct data loss |

The summary counts stages, events, merged or split combinations and read segments. Open each group and check the entries concerning your project.

## What changes in the model

### One wall type

The desktop program can describe segments with different sections. SPW NX uses one type for the full height. Import selects a reference section and the report lists segments not retained.

The weight of upper segments may become a head load. Elements outside the selected section may not be imported. Check the drawing and wall before calculation.

### One stratigraphy

The native model uses the project stratigraphy for every stage. If the desktop contains stage variants, the report reports the differences and states which stratigraphy was retained.

The same principle applies to calculation slopes and assigned subgrade reaction moduli that change between stages.

### Project combinations

In the desktop program, factors can change from one stage to another. In SPW NX combinations belong to the project.

Import merges equivalent configurations. It splits incompatible ones and limits their scope to the relevant stages. An unrepresentable factor is reported and must not be reconstructed by hand without verification.

### Stages as events

Stages become ordered events. The state of a support or load follows installation, application and removal. It no longer depends on a factor used to enable it in a single combination.

The history is incremental: an installed support enters the wall in the condition reached by previous stages.

### Seismic action and water

Seismic coefficients are referred to the site and limit state. A static combination containing seismic data is reported. Check type and scope after import.

The desktop flow net is not transferred as a drawing. Available regime and hydraulic data are reported in the native model.

## What is lost or recalculated

- Saved **results** are not imported: the project must be recalculated.
- Desktop **final reinforcement** is not imported: it is derived from the new analysis.
- Views, zoom, colours and graphic customisation are not part of the imported project.
- Stage-specific stratigraphy variants do not enter the single-stratigraphy model.
- Segments do not remain as segments: the report choices and warnings apply.
- Unrepresentable section or load types may be converted with an approximation or excluded with a note.

!!! warning "Warning"
    A completed import does not prove that the model is equivalent to the desktop one. The report and a new calculation are part of the check.

## Differences in results

Even with the same main data, results may change because of stage history, factor application, seismic action and hydraulic checks. Differences must not be hidden or corrected by forcing numerical agreement.

Read [Validation](validazione.md) for the meaning of comparison levels and [Methods](metodi.md) for assumptions and limits.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai) or open a [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/spw/docs/en/importazione-desktop.md).*
