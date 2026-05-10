# Modellazione 2D

Disegno CAD AutoCAD-like nel browser: linee, polilinee, cerchi, archi,
testo, quotature. Convenzioni famigliari per chi viene da AutoCAD/BricsCAD
+ ottimizzazioni per il workflow web.

## Layout dei comandi

### Toolbar disegno

In alto, sotto la TopBar, una toolbar a tre gruppi:

- **DRAW** — disegno (linea, polilinea, cerchio, arco, …)
- **MODIFY** — modifica (sposta, copia, ruota, specchia, trim, …)
- **VIEW** — viste (zoom estensione, fit, layer, snap, ortho)

### Riga AI in basso

La **riga AI** in fondo (sopra la status bar) accetta:

- **Comandi locali** (regex riconosciuti): `triangola`, `volume 100`,
  `curve`, `decima 5000`, `quota`, `3d`, `report`, ecc.
- **Comandi disegno** in inglese o italiano: `line`, `linea`, `polyline`,
  `circle`, ecc.
- **Chat libera** con AI Anthropic: descrizioni, domande di geometria, ecc.

[Approfondisci AI →](ai.md)

## Tasti dei tool (single-key shortcut)

L'UI è in italiano, quindi i tasti seguono la **prima lettera della parola
italiana**:

| Tool | Tasto | Tool | Tasto |
|---|---|---|---|
| Linea | **L** | Sposta | **M** |
| Punto | **N** | Copia | **C** |
| Polilinea | **P** | Specchia | **Y** |
| Cerchio | **G** | Ruota | **R** |
| Arco | **A** | Trim | **T** |
| Testo | **T** | Estendi | **X** |
| Sezione | **S** | Offset | **O** |
| Distanza | **D** | Stretch | **E** |
| Selezione | **Esc** | Pan | **Spazio** |

Premi il tasto → entri nel tool → seguì il prompt nella status bar in basso.

[Lista completa scorciatoie →](scorciatoie.md)

## Workflow tipico — disegna una linea

1. Premi **L** (oppure click su Linea in toolbar)
2. Status bar mostra: *"Linea: clicca punto iniziale"*
3. Click nel canvas → punto iniziale fissato
4. Status bar: *"Linea: clicca punto finale"*
5. Muovi il mouse — vedi l'**anteprima ghost** (linea gialla traslucida)
6. Click finale → linea creata
7. Status bar: *"Linea: clicca punto finale (Esc per terminare)"* — puoi
   continuare a tracciare segmenti dal punto finale come "polilinea spezzata"
8. **Esc** per uscire dal tool

## Snap automatici

Sempre attivi (toggle globale F8):

- **End** (endpoint) — fine di linea/polilinea
- **Mid** (midpoint) — metà di un segmento
- **Vertex** — vertice di polilinea
- **Center** (centro) — centro di cerchio/arco
- **Quadrant** — N/E/S/W di cerchio
- **Perpendicular** — perpendicolare a un altro segmento (mentre disegni)
- **Intersection** — intersezione tra entità

Quando lo snap è attivo vedi un **marker giallo** + label `END`/`MID`/`CEN` ecc.

## Ortho mode (F8 nei nostri shortcut)

Vincola il cursore a multipli di 90° dal punto di partenza. Utile per
disegnare orizzontali/verticali precise.

## Modify tools — flow AutoCAD-like

Sposta, Copia, Specchia, Ruota seguono il flow standard:

1. **Tool** (es. M = Move)
2. **Click sull'entità** → la seleziona
3. **Click base point**
4. **Muovi mouse** → anteprima fantasma (gialla traslucida)
5. **Click destinazione** → operazione completata

A ogni step la status bar in basso mostra il prompt esatto del prossimo
input richiesto.

## Layer manager

**Sidebar di sinistra** → pannello *DrawnLayer*. Per ogni layer:

- 🎨 **Color** (click per cambiare)
- 👁 **Eye** (toggle visibilità)
- 🔒 **Lock** (toggle modifica)
- **Nome**
- **Count** entità

Il **layer attivo** è evidenziato. Le entità che disegni vanno nel layer
attivo. Il layer attivo si cambia con **click** sul nome.

Se hai importato un DXF, i suoi layer vivono in un secondo pannello
*Imported (DXF)* — separato dai DrawnLayer per chiarezza.

## Properties panel (top-right)

Quando selezioni un'entità, in alto a destra appare un pannello
**Properties** contestuale:

- **Linea**: lunghezza, angolo, layer
- **Polilinea**: numero vertici, lunghezza totale, area (se chiusa)
- **Cerchio/Arco**: centro, raggio, angolo (per arco)
- **Punto**: coordinate, **Z editabile** (per quotature)
- **Testo/MText**: contenuto, dimensione, font
- **Dimension**: prefix, suffix, decimals, textHeight

Modifiche istantanee, undo/redo (Ctrl+Z/Y) supportato.

## Quotature

Tool **Distanza** (D): tra 2 punti, mostra la lunghezza. Per inserire una
quota permanente come entità DXF, tool **DIM** (toolbar):

- **Lineare** — distanza tra 2 punti, allineata o orizzontale/verticale
- **Allineata** — distanza diretta tra 2 punti, paralela alla linea ideale
- **Angolare** — angolo tra 2 segmenti
- **Radiale** — raggio di un cerchio/arco
- **Diametrale** — diametro

Le quote vengono salvate come entità `DimensionEntity` e si esportano
correttamente in DXF.

## Punti quotati

Per **quote di terreno** (rilievo, GPS in cantiere, sondaggi):

1. Drop di un CSV `X,Y,Z` o tasto **N** (Punto) per inserire manualmente
2. I punti hanno **Z editabile** nel Properties panel
3. Renderizzati come **marker ambra** con label della quota
4. Esportati in DXF come `POINT` con `z` valore

I punti quotati sono **input principale** per la triangolazione TIN.

## Hatch (riempimenti)

Tool **Hatch** in toolbar: seleziona un'area chiusa (polilinea chiusa o
cerchio) e applica un pattern. Pattern supportati:

- **Solid** — tinta unita
- **ANSI31** — diagonali (terreno, sezione)
- **ANSI32** — incrociato
- **AR-CONC** — calcestruzzo (puntini)
- **AR-SAND** — sabbia

## Salva il progetto

**File → Salva** o **Ctrl+S** → autosave nel browser (LocalStorage).

**File → Salva con nome** o **Ctrl+Shift+S** → scarica un `.cadproj`
(JSON) che contiene tutto: entità, layer, georef, mesh, raster, punti
quotati.

---

## Vedi anche

- [Mesh + curve](mesh-triangolazione.md) — dopo aver disegnato i punti, triangola
- [Sezioni e 3D](sezioni-3d.md) — visualizza in sezione/3D
- [AI assistant](ai.md) — comandi avanzati via chat
- [Scorciatoie](scorciatoie.md) — lista completa dei tasti

---

*Pagina utile? [Scrivici](mailto:info@geostru.ai?subject=Help%20Trispace%20NX%20-%20Modellazione%202D).*
