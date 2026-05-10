# Mesh, curve di livello e volumi

La **TIN** (Triangulated Irregular Network) è il modello digitale del terreno
generato dai punti quotati. Da lei derivano curve di livello, mappa pendenze,
volumi cut/fill, sezioni 2D e vista 3D.

## Triangolazione TIN

### Comando

Nella riga AI: `triangola` (alias: `triangulate`, `mesh`, `tin`).

### Cosa succede

1. Trispace raccoglie tutti i punti quotati attivi (`PointEntity` con `z` +
   `elevationMarkers` legacy)
2. Manda i punti al server (`POST /api/analysis/triangulate`)
3. Server fa **Delaunay 2.5D**: proietta i punti su XY, triangola in 2D,
   solleva i triangoli con le quote Z originali
4. Riceve gli **indici dei triangoli** `[a, b, c]` e li renderizza sul canvas

Tipico tempo di elaborazione: < 1 s per 5 000 punti, ~3 s per 50 000 punti.

### Quanti punti servono

| Punti | Uso |
|---|---|
| 50–500 | Schizzo veloce, dettaglio basso |
| 500–5 000 | TIN media qualità per sezioni e volumi |
| 5 000–50 000 | Modello dettagliato per progettazione |
| > 50 000 | Necessario decimare (la TIN è troppo densa per visualizzazione interattiva) |

### Editing della mesh

Trispace **non** offre edit triangoli (eliminare bordi, swap, ricalcolare
locali). La mesh è un risultato derivato dai punti — se vuoi modificarla,
edita i punti (sposta, aggiungi, elimina) e ri-triangola.

## Curve di livello

### Comando

Riga AI: `curve` (alias: `curve di livello`, `contours`).

Passo automatico calcolato in base al range Z. Per fissarlo:

`curve 0.5` → curve ogni 0.5 m
`curve 1` → curve ogni metro
`curve 5` → curve ogni 5 m

### Algoritmo

Per ogni triangolo della TIN:

1. Trova la quota minima `z_min` e massima `z_max`
2. Per ogni livello `Δz`, `2Δz`, `3Δz` ... che cade tra z_min e z_max:
   - Trova le **2 intersezioni** del piano orizzontale Z = livello con i 3
     bordi del triangolo
   - Genera un **segmento** (linea) sulla mesh
3. Concatena i segmenti con bordi adiacenti per ottenere **polilinee chiuse**

### Stile cartografico

- **Curve principali**: ogni 5×passo (più spesse, etichetta della quota)
- **Curve secondarie**: il resto (più sottili)

## Pendenze (mappa colorata)

Riga AI: `pendenze` (alias: `slope`).

Per ogni triangolo, calcola l'angolo di **massima pendenza** (in gradi
rispetto all'orizzontale):

- Verde 🟢 < 10° (terreno facile)
- Giallo 🟡 10–20° (medio)
- Arancio 🟠 20–30°
- Rosso 🔴 > 30° (ripido / instabile)

Utile per analisi di **suscettibilità a frane superficiali** in via
preliminare.

## Volumi cut/fill

### Comando

Riga AI: `volume 100` → calcola rispetto al piano `Z = 100`.

Senza argomento, default piano = quota minima della mesh.

### Algoritmo

Per ogni triangolo:

1. Calcola il **volume del prisma** definito da:
   - Base: il triangolo proiettato sul piano XY
   - Altezza: distanza media dei 3 vertici dal piano di progetto
2. Se l'altezza media è positiva (vertici sopra il piano) → **fill**
   (riporto, materiale che servirebbe per arrivare al piano)
3. Se negativa → **cut** (sterro, materiale da rimuovere)

### Output

- **V_cut** (sterro) in m³
- **V_fill** (riporto) in m³
- **V_net = V_fill − V_cut** in m³ (positivo = serve materiale; negativo =
  esce materiale)

### Cut/fill colormap

Sulla mesh:

- 🔴 Rosso = sterro (più scuro = più sterro)
- 🔵 Blu = riporto
- ⚪ Bianco = già al piano (entro tolleranza)

Utile per visualizzare graficamente dove serve scavare e dove servono i
riporti.

## Riferimenti algoritmici

- **Delaunay 2.5D**: librerie standard (Qhull, MIConvexHull). Trispace
  server-side usa una libreria .NET equivalente.
- **Curve di livello**: marching segments (analoga al *marching squares*
  ma su triangoli)
- **Volumi**: sommatoria di volumi di prismi triangolari (tetraedri se piano
  inclinato)

## Limiti

- TIN è **2.5D** (una quota per X,Y) — non rappresenta strapiombi, grotte,
  edifici sospesi
- Per **strapiombi e geometrie complesse 3D** servirebbe una mesh 3D vera
  (es. Open3D, MeshLab) — fuori scope di Trispace
- Decima sempre prima di triangolare — nuvole > 50k punti rallentano
  parecchio

---

## Vedi anche

- [Workflow completo](workflow.md) — la TIN nel ciclo intero
- [Sezioni e 3D](sezioni-3d.md) — sezioni e vista 3D dalla TIN
- [Drone → GEOROCK3D](drone-georock3d.md) — workflow specifico per caduta massi

---

*Pagina utile? [Scrivici](mailto:info@geostru.ai?subject=Help%20Trispace%20NX%20-%20Mesh).*
