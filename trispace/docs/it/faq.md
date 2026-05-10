# FAQ — domande frequenti

## Generali

### Trispace è gratuito?

Trispace NX è incluso nella suite **GeoStru NX** con piano *freemium*.
Comandi locali (disegno 2D, triangolazione, curve, sezioni) sono accessibili
nel piano Free. La **chat libera AI** consuma crediti per token.

### Devo installare qualcosa?

No — è una web app, si apre da [`nx.geostru.ai/trispace/`](https://nx.geostru.ai/trispace/).

### Funziona offline?

Parzialmente:

- Comandi disegno 2D, snap, edit entità → ✅ offline (tutto client-side)
- Triangolazione TIN → ❌ richiede server (`/api/analysis/triangulate`)
- Chat AI libera → ❌ richiede server
- Salvataggio `.cadproj` come download → ✅ offline

## Importazione

### Il LAS è troppo grande, non si carica

LAS oltre 500 MB rallentano il browser. Soluzione:

- Pre-decima con **CloudCompare** (gratuito): `Edit → Subsample → Spatial`
- Filtra in CloudCompare per solo `Classification = 2 (Ground)` prima
- Poi importa il `.las` decimato in Trispace

### Il DWG non si importa

Trispace converte DWG → DXF lato server. Se il file:

- È protetto da password → non funziona
- È molto recente (DWG 2025+) → la libreria può non riconoscere il formato
- Contiene **3D solid ACIS** → vengono ignorati (non supportati)

In quei casi, apri il DWG in AutoCAD/BricsCAD/DraftSight e fai **Save as
DXF AC1015** (formato 2000), poi importa in Trispace.

### CSV non viene riconosciuto

Verifica che la prima riga sia un **header** con uno di questi pattern:

```csv
X,Y,Z
lat,lon,Z
id,X,Y,Z
```

Separatore: virgola `,`, punto e virgola `;` o tab. Encoding: UTF-8 o ANSI.

Se il CSV non ha header (solo numeri), aggiungilo manualmente in Notepad
prima di drop.

## Modellazione

### Come faccio un cerchio per centro + raggio?

Tool **G** (Cerchio) → click sul centro → muovi mouse (anteprima) → click sul
bordo. Il raggio è la distanza tra i 2 click. Per **digitare il raggio**: dopo
il primo click, scrivi il valore in tastiera (es. `15.5`) e premi Invio.

### I miei disegni svaniscono al refresh

Trispace fa autosave nel **LocalStorage** del browser. Se hai disabilitato
i cookie / cancellato i dati del sito, l'autosave si svuota.

Per persistenza affidabile: **Ctrl+Shift+S** → scarica un `.cadproj` → tienilo
sul disco / Drive.

## Mesh / TIN

### Triangolazione lentissima

Riduci i punti. Per 50 000 punti la TIN richiede ~3 secondi. Per 500 000
punti → minuti, e il browser potrebbe diventare unresponsive. Decima
prima a 5-50k punti.

### La TIN ha "buchi" o triangoli strani

La triangolazione **Delaunay 2.5D** richiede una distribuzione di punti
ragionevolmente regolare. Cause comuni di mesh strana:

- Punti **disposti su una linea retta** in pianta (collinear) → degenerazione
  numerica
- **Outlier** con quote anomale (z = 0 o z = 10000) → spegne tutto il
  rendering. Filtra outlier prima.
- Gruppi di punti **isolati** (clusters distanti) → la mesh include
  triangoli "lunghi" tra cluster diversi

Soluzione: filtra outlier in CloudCompare con **SOR filter** (Statistical
Outlier Removal) prima di importare.

### Posso editare la mesh manualmente?

No, Trispace non offre **edit triangoli**. La mesh è derivata dai punti — se
vuoi cambiarla, edita i punti (sposta, aggiungi, elimina) e ri-triangola.

## Vista 3D

### La vista 3D non si apre

Three.js richiede **WebGL**. Verifica:

- Il browser supporta WebGL (Chrome, Firefox, Edge, Safari recenti — sì)
- Hardware acceleration **abilitato** nelle impostazioni del browser
- GPU non troppo vecchia (>10 anni può dare problemi)

In `chrome://gpu` puoi vedere se WebGL è OK.

### La 3D è scattosa con tante triangoli

Decima la mesh. Riga AI: `decima mesh 50000` (target 50k triangoli).

## AI assistant

### L'AI ha calcolato male un volume

Verifica con il **comando locale** `volume 100`. Se l'AI usa il tool
calling correttamente, dovrebbe restituire lo stesso valore. Se è
diverso, è un bug dell'orchestrazione tool — segnalalo.

### Posso usare l'AI senza connessione internet?

No — la chat libera richiede connessione (Anthropic API). I **comandi
locali** (es. `triangola`, `curve`, `volume`) funzionano offline perché non
chiamano l'AI.

### Chi vede le mie chat?

Le chat libere passano per la **API di Anthropic**. Anthropic non
addestra i suoi modelli sui dati API per default (vedi loro privacy
policy). GeoStru non conserva il contenuto delle chat.

## Esportazioni

### Il DXF non si apre in AutoCAD

Verifica versione AutoCAD: AC1015 (Trispace export) richiede AutoCAD
2000+ (ovunque ormai). Se persiste, prova ad aprirlo in **LibreCAD** o
**DraftSight** — uno dei due lo aprirà sicuramente.

### Voglio i layer originali del DXF importato

Funziona già: i layer DXF imported vivono in un **secondo pannello laterale**
distinto dai DrawnLayer. Quando esporti, sia DrawnLayer che imported layer
vanno nel DXF.

## Manca la mia domanda

[Scrivici](mailto:info@geostru.ai?subject=Help%20Trispace%20NX%20-%20FAQ)
e la aggiungiamo qui.
