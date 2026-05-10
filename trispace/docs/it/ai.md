# AI assistant — riga di comando + chat

La **riga AI** in fondo a Trispace (sopra la status bar) è il tuo
*command-line* unificato: comandi locali rapidi + chat libera con un modello
Claude (Anthropic) integrato.

## Cosa puoi fare

### 1. Comandi locali (riconosciuti via regex)

Eseguiti **istantaneamente** lato client, senza chiamare l'AI:

| Comando | Cosa fa | Alias |
|---|---|---|
| `triangola` | Triangola la TIN dai punti quotati | `triangulate`, `mesh`, `tin` |
| `quota` | Inserisce un punto quotato (tool N) | — |
| `volume 100` | Calcola V_cut/V_fill rispetto a Z=100 | — |
| `curve` | Genera curve di livello | `curve di livello`, `contours` |
| `curve 0.5` | Curve a passo 0.5 m | — |
| `decima 5000` | Decima la nuvola a 5000 punti | — |
| `decima passo 0.5` | Decima con voxel grid passo 0.5 m | — |
| `pendenze` | Mappa pendenze colorata | `slope` |
| `3d` | Apre la vista 3D | — |
| `report` | Genera report Word | — |
| `georef` | Apre il wizard di georeferenziazione | — |
| `punti xyz x,y,z…` | Inserisce punti dalle coordinate digitate | — |
| `cancella punti` | Rimuove tutti i punti quotati | — |
| `aiuto` | Mostra questa lista | `help` |

### 2. Comandi disegno (AutoCAD-like)

| Comando | Cosa fa |
|---|---|
| `linea` / `line` | Avvia tool Linea |
| `polilinea` / `polyline` / `pline` | Avvia tool Polilinea |
| `cerchio` / `circle` | Avvia tool Cerchio |
| `arco` / `arc` | Avvia tool Arco |
| `testo` / `text` | Avvia tool Testo |
| `sezione` / `section` | Avvia tool Sezione |

### 3. Chat libera (fallback su Claude)

Se il testo digitato **non corrisponde** a nessun comando locale, viene
mandato in **streaming** all'endpoint `POST /api/ai/chat` (Anthropic SDK).

Esempi:

- *"Quanti m³ servono per livellare la zona dove il terreno è sotto 120?"*
  → Claude usa **tool calling** per: leggere la mesh, calcolare il volume di
  fill, restituire il numero
- *"Genera 50 punti casuali su un'area di 100×100 con quote tra 100 e 105"*
  → Claude inserisce i punti via tool calling
- *"Spiega come funziona la triangolazione Delaunay"* → risposta libera
  testuale

## Tool calling

L'AI ha accesso a **funzioni interne** dello store (Zustand) tramite
tool calling. Le principali:

- `addPoint(x, y, z)` — aggiunge un punto quotato
- `addLine(x1, y1, x2, y2)` — disegna una linea
- `addCircle(cx, cy, r)` — disegna un cerchio
- `triangulate()` — triangola la TIN
- `computeVolume(planeZ)` — calcola volumi
- `setActiveLayer(name)` — cambia layer attivo

Quindi puoi chiedere in linguaggio naturale:

> *"Disegna 3 linee rosse che formino un triangolo equilatero centrato in
> (50, 50) con lato 20"*

→ L'AI calcola le coordinate dei vertici, crea un layer rosso, disegna le 3
linee.

## Suggerimenti contestuali

Sopra la riga AI, quando il campo è **focused e vuoto**, compaiono dei
**chip di suggerimenti** ricalcolati in base allo stato corrente:

- Se hai punti ma non TIN → suggerisce `triangola`
- Se hai TIN ma non curve → suggerisce `curve`
- Se hai mesh ma niente volume → suggerisce `volume`
- Se hai LAS appena importato → suggerisce `decima 5000`

Click sul chip → il comando si compila nella riga.

## Streaming risposte

Le risposte AI sono in **streaming**: vedi il testo generato carattere per
carattere, niente attesa della risposta completa. Se la risposta richiede
tool calling, vedi gli step del tool prima del testo finale.

## Cronologia

Apri il **ChatPopover** (icona in basso a destra della riga AI) per vedere
la cronologia delle conversazioni. Le conversazioni precedenti **non**
restano nel context — ogni risposta parte fresca, ma puoi rileggerle.

Per resettare completamente: **clear chat** dal menu del ChatPopover.

## Allegati (📎)

Click sull'icona graffetta a sinistra della riga: puoi allegare un'**immagine
o uno screenshot** alla domanda. Utile per:

- *"Qui c'è un errore [allega screenshot] — cosa significa?"*
- *"Riconosci questa stratigrafia [allega foto del log]"* → l'AI usa la
  vision di Claude per descrivere

## Limiti

- **Conversazione singola**: ogni risposta parte fresca, niente memoria di
  lungo periodo
- **Costo**: ogni chat libera consuma crediti (Anthropic API). Comandi
  locali sono gratuiti.
- **Tool calling soggetto a errori**: se l'AI sbaglia coordinate o nomi di
  layer, controlla l'output prima di continuare a costruire sopra

## Privacy

- I **comandi locali** non lasciano il browser
- Le **chat libere** mandano il testo (e gli allegati se presenti) alla API
  di Anthropic. Non condividiamo storia con terzi al di fuori di Anthropic.
- Per dati riservati, evita la chat libera

---

## Vedi anche

- [Modellazione 2D](modellazione-2d.md) — comandi disegno tradizionali
- [Mesh + curve](mesh-triangolazione.md) — comandi `triangola`, `curve`, `volume`
- [Drone → GEOROCK3D](drone-georock3d.md) — wizard dedicato (alternativa all'AI)

---

*Pagina utile? [Scrivici](mailto:info@geostru.ai?subject=Help%20Trispace%20NX%20-%20AI).*
