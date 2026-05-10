# Esportazioni

Trispace esporta in **3 formati principali** + il file di progetto nativo.

## DXF (AutoCAD AC1015)

**File → Esporta → DXF** o riga AI: `esporta dxf`.

### Cosa contiene

- **Tutte le entità 2D** (linee, polilinee, cerchi, archi, testo, dimensioni)
- **Layer** dei tuoi disegni (DrawnLayer)
- **Mesh TIN** come 3DFACE (un face per triangolo) se hai triangolato
- **Curve di livello** come polilinee se calcolate
- **Punti quotati** come POINT con `z` valore
- **Hatch** se presenti

### Compatibilità

DXF AC1015 (AutoCAD 2000) — il più universale. Compatibile con:

- AutoCAD (qualsiasi versione 2000+)
- BricsCAD
- DraftSight
- LibreCAD (gratuito)
- QCAD (gratuito)
- BIM tools (Revit import via DWG converter)

### Subclass marker

Trispace mantiene tutti i **subclass marker** AC1015 corretti (`AcDbEntity`,
`AcDbLine`, `AcDbCircle`, ecc.) — il DXF si apre correttamente in qualsiasi
software CAD senza warning.

## GeoJSON

**File → Esporta → GeoJSON** o riga AI: `esporta geojson`.

### Cosa contiene

- Entità 2D (line, polyline, polygon, point) come **Feature** GeoJSON
- Coordinate in WGS84 se georef attiva, altrimenti coordinate locali
- Properties: layer, color, attributi geometrici (length, area)

### Compatibilità

- **QGIS** (drag-drop, riconosciuto auto)
- **ArcGIS Online / ArcGIS Pro**
- **Mapbox** / **Leaflet**
- **PostGIS** import via `ST_GeomFromGeoJSON`

### Limitazioni

- **Mesh TIN** non viene esportata (GeoJSON non supporta nativamente
  triangoli 3D)
- **Hatch / dimensioni** non hanno equivalente GeoJSON

Per esportare la mesh in GIS, usa DXF (le 3DFACE sono leggibili da QGIS
con plugin DXF Importer).

## GEOROCK3D `.txt`

**File → Esporta → GEOROCK3D** o riga AI: `esporta georock3d`.

Formato testuale `id;X;Y;Z` direttamente caricabile in GEOROCK3D
desktop → `Forms/ImportaPunti.cs`.

```
1;142.355;87.521;124.6
2;145.812;89.225;124.8
...
```

[Vedi workflow Drone → GEOROCK3D →](drone-georock3d.md)

## CSV punti

**File → Esporta → CSV** o riga AI: `esporta csv`.

Tabella semplice `X,Y,Z` per analisi in Excel / Python.

## File di progetto `.cadproj`

**File → Salva con nome…** o **Ctrl+Shift+S**.

Il `.cadproj` è il **formato nativo** di Trispace (JSON). Contiene **tutto**:

- Entità 2D + layer (DrawnLayer)
- Layer DXF imported (con i loro attributi originali)
- Mesh triangolata (indici dei triangoli)
- Punti quotati
- Georeferenziazione attiva (origine, scala)
- Raster di sfondo (in base64, può essere pesante)
- Sezioni 2D salvate

**File → Apri** → seleziona un `.cadproj` → ripristina lo stato esatto.

Quando usarlo:

- **Backup completo** della sessione
- **Continuare il lavoro** in un'altra sessione (anche su PC diverso)
- **Condividere il progetto** con un collega che ha Trispace

## Salva nel browser (autosave)

Senza scaricare nulla, **Ctrl+S** salva uno snapshot del progetto in
**LocalStorage** del browser. Riapre Trispace → recupera l'ultimo stato.

⚠️ Limite: LocalStorage ha ~5 MB, quindi raster pesanti possono saturare.
In caso di errore "QuotaExceeded", scarica `.cadproj` e ricarica.

---

## Vedi anche

- [Workflow completo](workflow.md) — esportazioni nel ciclo intero
- [Drone → GEOROCK3D](drone-georock3d.md) — wizard dedicato
- [Modellazione 2D](modellazione-2d.md) — entità DXF disegnate

---

*Pagina utile? [Scrivici](mailto:info@geostru.ai?subject=Help%20Trispace%20NX%20-%20Esportazioni).*
