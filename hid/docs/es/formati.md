# Formatos de archivo

## Proyecto `.hid`

HID guarda el proyecto en un archivo `.hid`, que es JSON legible con cualquier
editor de texto.

```json
{
  "schemaVersion": 2,
  "name": "Esempio 9.4 — Procedura dettagliata",
  "general": { "country": "IT", "region": "", "regulationVersion": "rr-2017" },
  "surfaces": [ { "description": "Area impermeabile", "areaM2": 4000, "runoffPost": 0.95 } ],
  "rainfall": { "kind": "twoParameters", "a": 35.04, "n": 0.421 }
}
```

El campo `schemaVersion` protege frente a la apertura de archivos producidos por
versiones más recientes de la app: si el número es más alto que el soportado, HID
rechaza el archivo en lugar de leerlo mal.

!!! note "Nota"
    Las entradas exigidas por la normativa viven en un diccionario
    `jurisdictionInputs`. Así es como añadir el soporte para un país nuevo no
    cambia el formato del archivo: los proyectos ya guardados siguen siendo
    legibles.

## Guardado y apertura

- **Guardar** descarga el `.hid` en tu ordenador.
- **Abrir** carga un `.hid` existente.
- **GeoDropbox** guarda y reabre el proyecto desde el espacio en la nube de
  GeoStru, accesible desde la misma barra de herramientas.

## Informe de cálculo

Desde el menú **Informe** eliges el formato:

| Formato | Extensión | Notas |
|---|---|---|
| Word | `.docx` | Siempre disponible |
| PDF | `.pdf` | Requiere el conversor del lado del servidor |
| Word 97 | `.doc` | Requiere el conversor del lado del servidor |

Si PDF y Word 97 no aparecen en el menú, el conversor no está disponible en ese
servidor: usa el formato Word.

El informe contiene referencias normativas, datos generales, superficies de
captación, curva IDF, parámetros hidrológicos, hietograma, dimensionamiento,
sistema de vertido, verificaciones finales e hidrograma, con los gráficos
incorporados.

!!! tip "Sugerencia"
    El informe sale en el idioma seleccionado en la barra de herramientas. Cambia
    el idioma antes de generarlo si lo entregas a un organismo extranjero.

---

*¿Has encontrado un error en esta página? [Comunícanoslo](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
