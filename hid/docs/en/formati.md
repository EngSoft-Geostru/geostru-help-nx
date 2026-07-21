# File formats

## `.hid` project

HID saves the project in a `.hid` file, which is JSON readable with any text
editor.

```json
{
  "schemaVersion": 2,
  "name": "Esempio 9.4 — Procedura dettagliata",
  "general": { "country": "IT", "region": "", "regulationVersion": "rr-2017" },
  "surfaces": [ { "description": "Area impermeabile", "areaM2": 4000, "runoffPost": 0.95 } ],
  "rainfall": { "kind": "twoParameters", "a": 35.04, "n": 0.421 }
}
```

The `schemaVersion` field protects against opening files produced by newer
versions of the app: if the number is higher than the supported one, HID refuses
the file instead of misreading it.

!!! note "Note"
    The inputs required by the regulation live in a `jurisdictionInputs`
    dictionary. That is how adding support for a new country does not change the
    file format: projects already saved remain readable.

## Saving and opening

- **Save** downloads the `.hid` to your computer.
- **Open** loads an existing `.hid`.
- **GeoDropbox** saves and reopens the project from the GeoStru cloud space,
  reachable from the same toolbar.

## Calculation report

From the **Report** menu choose the format:

| Format | Extension | Notes |
|---|---|---|
| Word | `.docx` | Always available |
| PDF | `.pdf` | Requires the server-side converter |
| Word 97 | `.doc` | Requires the server-side converter |

If PDF and Word 97 do not appear in the menu, the converter is not available on
that server: use the Word format.

The report contains regulatory references, general data, drainage areas, rainfall
curve, hydrological parameters, hyetograph, sizing, discharge system, final
checks and hydrograph, with the charts embedded.

!!! tip "Tip"
    The report comes out in the language selected in the toolbar. Change the
    language before generating it if you are submitting it to a foreign
    authority.

---

*Found an error on this page? [Let us know](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
