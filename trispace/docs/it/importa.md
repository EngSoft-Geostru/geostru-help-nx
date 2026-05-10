# Importa file

Trispace NX accetta **drag & drop** sul canvas o **File → Apri** dalla toolbar.

## Formati supportati

| Tipo | Formato | Note |
|---|---|---|
| **CAD** | `.dxf` (AutoCAD AC1015+) | Round-trip completo: entità + layer originali preservati |
| **CAD** | `.dwg` | Conversione server-side via libreria DWG → DXF |
| **Nuvole punti** | `.las` (LAS 1.2/1.4) | Parser browser via `laz-perf` WASM |
| **Nuvole punti** | `.laz` (LAS compresso) | Stesso parser, decompressione streaming |
| **Punti** | `.csv`, `.txt` | Header `X,Y,Z` o `lat,lon,Z` (auto-detect) |
| **Vettoriale GIS** | `.geojson` | Coordinate metriche o WGS84 |
| **Project nativo** | `.cadproj` | Stato completo Trispace (entità + layer + georef + mesh) |
| **Raster** | `.png`, `.jpg`, `.tif` + worldfile | Cartografia di sfondo, georeferita |

## DXF / DWG

### Cosa importa

- **Entità geometriche**: LINE, LWPOLYLINE, CIRCLE, ARC, ELLIPSE, SPLINE,
  TEXT, MTEXT, DIMENSION, INSERT (block)
- **Layer originali** con i loro attributi (colore, linetype, frozen/lock)
- **3DFACE** → triangoli mesh
- **POINT** → entità punto

Il client estrae i layer originali nel **secondo pannello laterale** (oltre
ai *DrawnLayer* dei tuoi disegni nuovi). I due si gestiscono separati: layer
DXF restano "letti" come imported, i tuoi nuovi disegni vivono nei
DrawnLayer.

### Cosa NON importa (limitazioni)

- **Block reference (INSERT) annidati** — solo top-level
- **Hatch patterns custom** — pattern standard ANSI31 ecc. supportati
- **3D solid / surface ACIS** — non supportato (Trispace è prevalentemente 2D
  + mesh TIN)
- **Layout multipli** — solo Model space

## LAS / LAZ

### Workflow tipico

1. Drop del file → si apre il pannello **Importa LAS**
2. Vedi: numero punti totali, range Z, header info
3. **Filter classification** ASPRS (vedi sotto)
4. **Decima** (voxel-grid o random)
5. **Importa nel CAD** → diventa una nuvola di `PointEntity` in un layer
   dedicato

### Classification ASPRS

LAS standard contiene una classificazione per ogni punto. Le classi più
usate:

| Codice | Nome | Significato |
|---|---|---|
| 0 | Created, Never Classified | Punti non processati |
| 1 | Unclassified | Default, non riconosciuto |
| 2 | **Ground** | **Terreno reale** ← per geotecnica usa SOLO questo |
| 3 | Low Vegetation | Erba, arbusti |
| 4 | Medium Vegetation | Cespugli |
| 5 | High Vegetation | Alberi |
| 6 | Building | Edifici |
| 7 | Low Point (noise) | Outlier sotto il terreno |
| 9 | Water | Acqua |
| 10 | Rail | Ferrovia |
| 11 | Road Surface | Strada |

Per la maggior parte dei calcoli geotecnici (mesh, curve, volumi) ti serve
**solo classe 2 (Ground)**. Spunta solo quella e ottieni il "bare earth"
del rilievo.

### Decimazione

Trispace offre **2 strategie**:

- **Voxel grid** (default) — divide lo spazio in celle di lato `step` e
  tiene il centroide di ogni cella. Decima in modo **uniforme spaziale**
  (preserva la geometria).
- **Random** — sceglie N punti casuali. Più veloce ma può creare aree dense
  e aree vuote — sconsigliato per TIN.

Suggerimento `step` automatico: Trispace stima un valore in base alla
densità della nuvola e al target di punti che vuoi.

### Limiti dimensione

- Max 500k punti caricabili nel browser (memoria JS)
- File `.las` di 100-500 MB sono OK in streaming
- Per nuvole > 10M punti → pre-decima con CloudCompare a 100-500k punti
  prima di drop in Trispace

## CSV / TXT

### Formati riconosciuti

```csv
# Variante 1: solo coordinate locali
X,Y,Z
142.3,87.5,124.6
145.8,89.2,124.8
...

# Variante 2: coordinate WGS84 (richiede georef attiva)
lat,lon,z
41.9028,12.4964,124.6
41.9030,12.4966,124.8

# Variante 3: con id
id,X,Y,Z
P1,142.3,87.5,124.6
P2,145.8,89.2,124.8
```

Il separatore può essere virgola `,`, punto e virgola `;` o tab. Encoding
UTF-8 (consigliato) o ANSI.

## Raster + worldfile

Per usare una **mappa di sfondo georeferita**:

1. Drop di un'immagine `.png` / `.jpg` / `.tif`
2. Drop del relativo **worldfile**: stesso nome con estensione `.pgw` /
  `.jgw` / `.tfw` (o `.wld`)

Il worldfile contiene 6 numeri (resolution X, rotation X/Y, resolution Y, X
top-left, Y top-left). Trispace usa quei numeri per **posizionare il raster
in coordinate metriche**.

Senza worldfile: l'immagine è caricata ma **non georeferita** (resta in
coordinate pixel locali).

## Project nativo `.cadproj`

Il `.cadproj` è il formato di salvataggio completo di Trispace. Contiene:

- Tutte le entità disegnate
- Tutti i layer (DrawnLayer + DXF imported)
- Georeferenziazione attiva (origine + scale)
- Mesh triangolata se presente
- Punti quotati
- Raster di sfondo (in base64)

**File → Salva con nome…** scarica un `.cadproj`. Riapri con **File → Apri**
ovunque (PC diversi, sessioni diverse).

---

## Vedi anche

- [Workflow completo](workflow.md) — come usare i vari import
- [Mesh + curve](mesh-triangolazione.md) — cosa fare con i punti decimati
- [Drone → GEOROCK3D](drone-georock3d.md) — il wizard dedicato

---

*Pagina utile? [Scrivici](mailto:info@geostru.ai?subject=Help%20Trispace%20NX%20-%20Importa).*
