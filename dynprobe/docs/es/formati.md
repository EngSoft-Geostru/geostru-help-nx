# Formatos de archivo

## .dprobe — formato nativo NX

El archivo `.dprobe` es el formato de proyecto de Dynamic Probing NX. Es un archivo **JSON** en texto plano, legible con cualquier editor de texto. Contiene:

- Metadatos del proyecto (nombre, sitio, cliente, coordenadas)
- Lista de ensayos con todas las lecturas
- Biblioteca de instrumentos integrada en el archivo
- Estratigrafía interpretada (estratos, profundidades, tipo, γ)
- Ajustes de correlaciones (autores preferidos)
- Resultados calculados (correlaciones, categoría de subsuelo, capacidad portante, estimación de parámetros)

El archivo es **autónomo y portátil**: cópialo a otro PC, ábrelo en Dynamic Probing NX — todo funciona sin configuración adicional.

## .dypx — formato escritorio GeoStru (importación)

El archivo `.dypx` es el formato de exportación en texto del escritorio GeoStru Dynamic Probing. Dynamic Probing NX puede importarlo desde la pantalla inicial con **Importar .dypx…**. Durante la importación se leen:

- Todos los ensayos con las lecturas de golpes
- Los datos del instrumento (tipo, β si está presente)
- Las coordenadas de los ensayos (si están guardadas en el archivo de escritorio)

La estratigrafía y las correlaciones no se importan desde el escritorio — deben reintroducirse en NX.

## CSV datalogger

Muchos dataloggers para ensayos dinámicos exportan los datos en formato CSV o TXT. Dynamic Probing NX reconoce automáticamente el formato si las columnas están estructuradas como:

```
profundidad, golpes
0.10, 8
0.20, 9
0.30, 11
...
```

Las columnas pueden estar separadas por coma, punto y coma o tabulador. Si el archivo tiene un encabezado con las coordenadas del sitio (lat, lon, cota), se leen automáticamente.

Para importar: en la pestaña **Lecturas** del editor, haz clic en **Importar lecturas desde archivo…** y selecciona el CSV. Como alternativa, pega el contenido directamente en el campo de texto del modal.

## AGS4 (.ags)

Dynamic Probing NX exporta en formato AGS4 (v4.2) pero no importa desde AGS4. Ver [Exportación →](export.md).
