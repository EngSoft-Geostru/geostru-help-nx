# Cosa si misura — guida al rilievo geomeccanico

GMS NX lavora con i dati che provengono dal **rilievo strutturale** lungo
linee di scansione. Questa pagina riassume *cosa* misurare in campo e *come*
poi inserirlo nel programma.

## Le grandezze fondamentali: β e α

Ogni piano di discontinuità (giunto, frattura, faglia, stratificazione,
schistosità) si descrive con due angoli:

- **Immersione (dip direction, β)** — direzione della massima pendenza, in
  gradi rispetto al Nord. Range **0–360°**.
- **Inclinazione (dip, α)** — inclinazione del piano sul piano orizzontale,
  in gradi. Range **0–90°**.

!!! info "Convenzione GeoStru"
    GMS NX usa la coppia (immersione **β**, inclinazione **α**) — la stessa
    di tutta la suite GeoStru desktop, di eGEOCompass e dei manuali ISRM
    italiani. La notazione "*dip / dip direction*" che si incontra in molta
    letteratura anglosassone è equivalente: corrisponde a (α, β).

### Come si misura con la bussola

Bussola di geologo (Brunton, Freiberger, Silva Geo) appoggiata sul piano:

1. Orienta la bussola con la **base sul piano**, livella la bolla.
2. Leggi sulla **rosa graduata** la direzione di immersione (β).
3. Leggi sull'**inclinometro** l'angolo di inclinazione (α).
4. Se non sei sicuro che il piano sia "vero" (può essere un giunto curvo,
   una superficie di scivolamento, una stratificazione disturbata),
   ripeti la misura in 2-3 punti diversi della stessa superficie e
   prendi la media — o registra entrambe le coppie.

### Come si misura con il tablet (GMS Compass)

Apri [GMS Compass](compass.md) sul tablet, **appoggi il dispositivo
sul piano** in modalità landscape, premi il pulsante centrale: l'app
legge i sensori (accelerometro + magnetometro), calcola β e α e li
aggiunge alla lista. Vedi la pagina dedicata per la procedura completa.

## Linea di scansione

In un rilievo geomeccanico standard si traccia una **linea di scansione**
sul fronte (di solito 10-30 m, materializzata con metro o cordella):
ogni discontinuità che la interseca viene rilevata e registrata con la
sua **distanza progressiva** dall'origine.

Cosa registrare per la linea:

- **Coordinate dell'origine** (lat/long GPS o WGS84)
- **Azimut della linea** (0–360°, direzione che la linea segue, in gradi
  rispetto al Nord)
- **Lunghezza totale** (per documentazione)

Inserendo questi 3 valori in *Dati progetto → Sito GPS*, GMS NX abilita
il pulsante **"Geolocalizza giunti dalle distanze"** che calcola
automaticamente le coordinate WGS84 di ogni giacitura a partire dalla
sua distanza progressiva.

!!! tip
    La linea di scansione è opzionale ma fortemente consigliata: senza,
    GMS calcola comunque stereonet e famiglie ma la **mappa** risulta
    vuota o limitata ai punti inseriti manualmente.

## Parametri ISRM aggiuntivi (modalità *Dettagli completi*)

Per ogni giunto, oltre a β e α, puoi registrare i parametri ISRM
classici (tab *Discontinuità* → toggle *"Dettagli completi"*):

| Campo | Significato | Range tipico |
|---|---|---|
| **Distanza** | progressiva lungo la linea (m) | 0 – L_linea |
| **Spaziatura** | distanza al giunto precedente della stessa famiglia (m) | 0.01 – 10+ |
| **Persistenza** | lunghezza visibile del piano (m) | 0.1 – 30+ |
| **Apertura** | distanza tra le 2 superfici (mm) | 0 – 100+ |
| **Riempimento** | natura del materiale che riempie il giunto | argilla, calcite, vuoto, … |
| **Rugosità** | JRC visivo o categorico (Barton 0–20) | 0 – 20 |
| **Alterazione** | grado di alterazione delle pareti (W1–W5 ISRM) | W1 – W5 |
| **Acqua** | presenza d'acqua (assente / umido / gocciola / fluente) | — |
| **Note** | testo libero | — |

!!! note "Quanto è davvero necessario?"
    Per il **test di Markland** servono solo β e α per ogni giunto, più
    pendio e angolo d'attrito. I parametri ISRM aggiuntivi sono opzionali
    e servono per:
    
    - documentare il rilievo nel report Word
    - alimentare valutazioni RMR/Q che farai a mano o in altri programmi
    - giustificare la scelta dell'angolo d'attrito φ effettivo

## Indizi di scivolamento attivo

Mentre rilevi le giaciture, annota nelle note dei singoli giunti gli
indizi di **movimento attivo o recente**:

- **Strie di scivolamento** (slickenside) — se presenti, indicano
  movimenti antichi/attivi e la direzione del trend
- **Specchi di faglia** — superfici lisce, lucide
- **Brecce di faglia** o **cataclasiti** lungo il giunto
- **Acqua in pressione** che fuoriesce dal giunto
- **Vegetazione disturbata o assente** lungo la traccia
- **Materiale incoerente** (argilla, sabbia) all'imbocco del giunto

Questi indizi non entrano nel calcolo automatico ma sono fondamentali
nell'**interpretazione**: un cuneo cinematicamente possibile (Markland
"ipotetico") che ha **strie attive** è un cinematismo *probabile*, non
solo possibile.

## Modalità di campagna

### Da solo, con bussola

Lavora in coppie (operatore + assistente) o registra in un taccuino
le triplette `distanza | β | α` e poi inseriscile in GMS NX a fine
giornata da **Discontinuità → + Aggiungi riga** o da
**File → Importa da CSV/TXT generico**.

### Da solo, con tablet

Apri [GMS Compass](compass.md) sul tablet. Per ogni piano:

1. Appoggia il tablet **landscape, schermo verso l'alto**, in
   contatto con la superficie
2. Premi il **bottone centrale**
3. Compass salva la coppia β/α e attende il prossimo piano
4. A fine rilievo, **"Trasferisci al PC"** genera un codice
   8-caratteri da digitare in GMS NX

Vedi [Trasferimento al PC](trasferimento.md).

### Foto al taccuino, AI alla scrivania

Se sul campo non hai potuto digitare e hai solo un **taccuino con la
lista numerica delle misure** (o un PDF restituito da un altro
software, o una vecchia tabella Excel), usa
[**AI Import**](ai-import.md): scatti una foto con il telefono,
GMS estrae automaticamente le triplette e popola la tabella.

### Scansione 3D (Matterport, drone, LiDAR)

Se invece di rilevare con la bussola hai una **nuvola di punti 3D**,
GMS può estrarre i piani principali in automatico via RANSAC. Vedi
[Nuvola di punti 3D](nuvola-3d.md).

---

## Cosa NON misura GMS NX (al momento)

GMS NX si concentra sulla parte **geometrica e cinematica** del rilievo.
Non calcola:

- Indici globali dell'ammasso roccioso (RMR Bieniawski, Q Barton, GSI Hoek)
  — vanno valutati a parte sui parametri ISRM esportabili in CSV
- Resistenza al taglio del giunto (Barton-Bandis) — usa l'angolo
  d'attrito φ già conosciuto o stimato
- Stabilità globale (Sarma, Bishop, FEM) — usa Slope/Loadcap o un
  software FEM dedicato

GMS produce in **input** per quei calcoli: famiglie, giaciture medie,
parametri ISRM, mappa GPS.

---

*Pagina utile? [Scrivici](mailto:info@geostru.ai?subject=Help%20GMS%20NX%20-%20Rilievo).*
