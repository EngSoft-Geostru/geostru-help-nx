# Quickstart — il tuo primo TIN in 5 minuti

In 5 minuti vedi Trispace al lavoro su una nuvola di punti LAS reale.

## 1. Apri l'app

Vai su [`nx.geostru.ai/trispace/`](https://nx.geostru.ai/trispace/).

## 2. Carica un esempio

Toolbar → **Help (?)** → **Risorse · file di esempio** → scegli
*"Costone roccioso · LAS demo"* (~30k punti, classificati).

L'esempio si carica nel canvas come **nuvola di punti** colorata per
classification ASPRS:

- 🟢 Terreno (classe 2)
- 🟫 Vegetazione bassa/alta (classi 3, 5)
- 🟦 Edificato (classe 6)
- 🔴 Rumore / outlier (classe 7)

## 3. Filtra per "solo terreno"

Nel **Pannello di importazione LAS** che si apre:

1. Spunta solo **classe 2 (Ground)** → la nuvola si ridurrà a ~10-15k punti
2. Premi **Decima a 5000 punti** (voxel-grid uniforme)
3. **Importa nel CAD**

Ora hai una nuvola di punti pulita, terra-only, decimata.

## 4. Triangola

Nella riga AI in basso digita: `triangola` (o `triangulate`, `mesh`, `tin`).

In ~1 secondo Trispace:

1. Manda i punti al server (endpoint `/api/analysis/triangulate`)
2. Server fa **Delaunay 2.5D** sui punti (proiezione XY, triangolazione, lift Z)
3. Client riceve gli indici dei triangoli + li renderizza sul canvas

Vedi la **TIN mesh** sovrapposta alla nuvola, linee semitrasparenti.

## 5. Curve di livello + 3D

Nella riga AI digita:

- `curve` → mostra le **curve di livello** (isoipse) sulla TIN, passo
  automatico in base al range Z
- `3d` → apre la **vista 3D** della mesh in Three.js (orbita libera, shading)

In 3 click hai mesh + curve + visualizzazione 3D.

## 6. Calcola un volume

Nella riga AI digita: `volume 100`.

Trispace calcola il **volume cut/fill** rispetto al piano Z = 100 (o un altro
piano di progetto). Output:

- **Volume di sterro** (parte sopra il piano) in m³
- **Volume di riporto** (parte sotto) in m³
- **Cut/fill map** colorata sulla mesh (rosso = sterro, blu = riporto)

## 7. Esporta

Toolbar → **File → Esporta**:

- **DXF** — la mesh + curve + entità 2D in formato AutoCAD AC1015
- **GeoJSON** — entità georeferite per QGIS / ArcGIS
- **GEOROCK3D `.txt`** — i punti decimati nel formato `id;X;Y;Z`
  direttamente caricabile in `Forms/ImportaPunti.cs` di GEOROCK3D

---

## Prossimi passi

- [**Workflow completo**](workflow.md) — un progetto reale dall'inizio alla fine
- [**Drone → GEOROCK3D**](drone-georock3d.md) — il wizard a 4 step dedicato
- [**AI assistant**](ai.md) — la riga AI può fare molto di più

---

*Pagina utile? Hai dubbi? [Scrivici](mailto:info@geostru.ai?subject=Help%20Trispace%20NX%20-%20Quickstart).*
