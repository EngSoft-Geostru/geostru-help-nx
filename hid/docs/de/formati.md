# Dateiformate

## Projekt `.hid`

HID speichert das Projekt in einer `.hid`-Datei, die JSON enthält und mit jedem
Texteditor lesbar ist.

```json
{
  "schemaVersion": 2,
  "name": "Esempio 9.4 — Procedura dettagliata",
  "general": { "country": "IT", "region": "", "regulationVersion": "rr-2017" },
  "surfaces": [ { "description": "Area impermeabile", "areaM2": 4000, "runoffPost": 0.95 } ],
  "rainfall": { "kind": "twoParameters", "a": 35.04, "n": 0.421 }
}
```

Das Feld `schemaVersion` schützt vor dem Öffnen von Dateien, die mit neueren
Versionen der App erzeugt wurden: Ist die Nummer höher als die unterstützte,
weist HID die Datei zurück, statt sie fehlerhaft einzulesen.

!!! note "Hinweis"
    Die vom Regelwerk geforderten Eingaben liegen in einem Wörterbuch
    `jurisdictionInputs`. Dadurch ändert die Unterstützung eines neuen Landes das
    Dateiformat nicht: Bereits gespeicherte Projekte bleiben lesbar.

## Speichern und Öffnen

- **Speichern** lädt die `.hid`-Datei auf Ihren Rechner herunter.
- **Öffnen** lädt eine vorhandene `.hid`-Datei.
- **GeoDropbox** speichert das Projekt im GeoStru-Cloudspeicher und öffnet es
  wieder; erreichbar über dieselbe Werkzeugleiste.

## Berechnungsbericht

Im Menü **Bericht** wählen Sie das Format:

| Format | Erweiterung | Anmerkungen |
|---|---|---|
| Word | `.docx` | Immer verfügbar |
| PDF | `.pdf` | Erfordert den serverseitigen Konverter |
| Word 97 | `.doc` | Erfordert den serverseitigen Konverter |

Wenn PDF und Word 97 nicht im Menü erscheinen, ist der Konverter auf diesem
Server nicht verfügbar: Verwenden Sie dann das Word-Format.

Der Bericht enthält normative Verweise, allgemeine Daten, Einzugsflächen,
Regenhöhenlinie, hydrologische Parameter, Regenganglinie, Bemessung,
Ableitungssystem, abschließende Nachweise und Abflussganglinie, jeweils mit
eingebetteten Diagrammen.

!!! tip "Hinweis"
    Der Bericht wird in der in der Werkzeugleiste ausgewählten Sprache erzeugt.
    Wechseln Sie die Sprache vor der Erzeugung, wenn Sie ihn bei einer
    ausländischen Behörde einreichen.

---

*Haben Sie auf dieser Seite einen Fehler gefunden? [Melden Sie ihn uns](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
