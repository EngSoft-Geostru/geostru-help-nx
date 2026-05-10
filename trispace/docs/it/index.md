# Trispace NX — CAD web 2D/3D + drone → GEOROCK3D

**Trispace NX** è il CAD web di GeoStru per il workflow **drone /
fotogrammetria / scanner 3D → analisi geotecnica**. Disegno 2D AutoCAD-like
(linee, polilinee, cerchi, archi, dim), import di nuvole di punti **LAS/LAZ**
con decimazione, **triangolazione TIN** + curve di livello + volumi, sezioni
2D, vista 3D della mesh, georeferenziazione, AI assistant integrato. Export
diretto in formato compatibile con **GEOROCK3D** (analisi caduta massi).

[**Apri Trispace NX**](https://nx.geostru.ai/trispace/){ .md-button .md-button--primary }
[Quickstart in 5 minuti](quickstart.md){ .md-button }

---

## Cosa fa, in sintesi

- **Disegno 2D**: linea, polilinea, cerchio, arco, testo, quotature, hatch — convenzioni AutoCAD
- **Import nuvole LAS/LAZ**: parser WASM `laz-perf`, decimazione voxel-grid, filtro per classification ASPRS
- **Mesh TIN**: triangolazione Delaunay server-side, decimazione, curve di livello, mappa pendenze, volumi cut/fill
- **Sezioni 2D** lungo polilinea con assi graduati
- **Vista 3D** Three.js della mesh con shading
- **Georeferenziazione** raster → coordinate metriche est/nord
- **DXF** import/export AutoCAD AC1015 con layer originali preservati
- **AI command line** — comandi locali (triangola, volume, decima, …) + chat libera con Anthropic
- **Wizard drone → GEOROCK3D**: 4 step LAS → filter → decima → export `.txt`

## Per chi

- **Geologi e ingegneri geotecnici** che lavorano con dati da drone /
  fotogrammetria / scanner 3D LiDAR e devono produrre mesh, curve, sezioni
- **Studi di consulenza** che integrano l'output drone in pareri di
  pericolosità (caduta massi, frane, opere di sostegno)
- **Tecnici di cantiere** che fanno calcoli volumetrici (sterro/riporto)
  da rilievo drone

## Come iniziare

1. Apri [`nx.geostru.ai/trispace/`](https://nx.geostru.ai/trispace/)
2. Drop di un file `.las`, `.dxf`, `.csv` (XYZ) o usa **Help → Risorse → file di esempio**
3. Se è LAS: filtra per classe → decima → triangola
4. Se è DXF: edita 2D, esporta
5. Esamina mesh, curve di livello, sezioni
6. Esporta DXF / GeoJSON / formato GEOROCK3D

[Vedi il workflow completo →](workflow.md)

## Capitoli del manuale

### Iniziare

- [**Quickstart**](quickstart.md) — 5 minuti dal primo accesso al primo TIN
- [**Workflow completo**](workflow.md) — drone → mesh → sezioni → export

### Importazione

- [**Importa file**](importa.md) — DXF, DWG, LAS/LAZ, CSV, GeoJSON, raster, satelliti

### Modellazione

- [**Modellazione 2D**](modellazione-2d.md) — comandi disegno (L · P · G · A · T · …),
  layer, snap, ortho
- [**Mesh + curve di livello**](mesh-triangolazione.md) — triangolazione TIN,
  curve di livello, pendenze, volumi cut/fill
- [**Sezioni e vista 3D**](sezioni-3d.md) — sezioni 2D lungo polilinea, render 3D mesh

### Workflow specifici

- [**AI assistant**](ai.md) — command line + chat libera + comandi locali
- [**Drone → GEOROCK3D**](drone-georock3d.md) — wizard 4 step per caduta massi

### Output

- [**Esportazioni**](esportazioni.md) — DXF, GeoJSON, formato GEOROCK3D `.txt`

### Riferimento

- [**FAQ**](faq.md) — domande frequenti
- [**Scorciatoie tastiera**](scorciatoie.md) — tasti dei tool

---

*Hai trovato un errore o vuoi suggerire un contenuto?
[Scrivici](mailto:info@geostru.ai?subject=Help%20Trispace%20NX) — grazie!*
