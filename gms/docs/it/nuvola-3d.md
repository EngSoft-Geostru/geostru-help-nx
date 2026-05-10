# Nuvola di punti 3D — estrazione automatica dei piani

GMS NX importa **nuvole di punti 3D** prodotte da Matterport, droni
fotogrammetrici o LiDAR terrestre, e ne estrae automaticamente i
**piani delle discontinuità** con il loro β/α e un indice di planarità.
Niente AI: solo geometria pura (RANSAC + PCA).

## Quando usarlo

- ✅ Hai una **scansione Matterport** del fronte roccioso
- ✅ Hai una **fotogrammetria da drone** processata in Pix4D / Metashape /
  Agisoft → nuvola densa
- ✅ Hai una **scansione LiDAR terrestre** (TLS) di un versante
- ✅ Vuoi rilevare giaciture su versanti **inaccessibili** (falesia
  marina, parete sopra strada di transito, gallerie pericolose)

- ❌ Hai solo **foto 2D** di un fronte → l'AI non estrae piani da una
  singola foto, e neanche RANSAC. Servono almeno 50-100 punti 3D per
  piano.
- ❌ Hai una **mesh chiusa** (modello CAD, BIM): RANSAC trova solo le
  facce planari grandi, perde le geometrie complesse.

## Apertura

Dal menu in alto:

1. **File → Importa da → Importa nuvola 3D…**

Si apre il modal **"Importa nuvola 3D · estrazione piani"**.

## Procedura

### 1. Carica la nuvola

Trascina il file nell'area di drop, oppure clicca per sfogliare:

| Formato | Tipo | Note |
|---|---|---|
| `.ply` | ASCII | Lo standard per fotogrammetria. **Solo ASCII**, non binario. |
| `.obj` | mesh / point set | Vengono usati solo i vertici, le facce sono ignorate |
| `.xyz` | text 3 colonne | `X Y Z` separati da spazio o tab |
| `.txt` | text 3 colonne | Stesso formato di `.xyz` |
| `.csv` | text con header | Header `X,Y,Z` (case-insensitive) |

**Limite di dimensione**: 60 MB per file. Per nuvole più grandi,
ricampiona in CloudCompare (sub-sampling spaziale) prima di
caricare.

Il viewer 3D mostra subito la nuvola (Three.js, orbita libera con
mouse).

### 2. Imposta i parametri RANSAC

Sotto la drop area:

- **Tolleranza** (default `0.05 m`) — distanza massima punto–piano
  perché il punto sia considerato *inlier* del piano. Per nuvole
  precise (LiDAR) usa `0.01-0.02 m`. Per fotogrammetria meno precisa
  o nuvole rumorose usa `0.05-0.10 m`.
- **Punti minimi per piano** (default `100`) — soglia di inliers sotto
  cui un piano viene scartato. Più alto = solo piani grandi/forti, più
  basso = anche piani piccoli (rischio falsi positivi).
- **Numero massimo di piani** (default `8`) — quanti piani estrarre
  prima di fermarsi. Aumenta se ti aspetti tante famiglie diverse.

### 3. Premi "Estrai piani"

GMS:

1. Esegue **RANSAC** iterativo: a ogni round campiona 3 punti casuali,
   calcola il piano che li unisce, conta gli inliers entro tolleranza.
2. Itera 200-500 volte e tiene il piano con più inliers.
3. **Rimuove** quegli inliers dalla nuvola (tutti i punti del piano
   non sono più disponibili per i prossimi piani).
4. Per ogni piano accettato calcola la **direzione normale precisa**
   con PCA (Jacobi eigendecomposition) sul cluster di inliers, poi
   converte la normale in (β, α).
5. Ripete fino a esaurire i piani significativi o raggiungere il
   numero massimo richiesto.

Tempo tipico: **3-15 secondi** per nuvole di 10 000 - 100 000 punti.

### 4. Verifica e seleziona

Si popola la **lista piani trovati** a destra. Per ogni piano:

| Colonna | Significato |
|---|---|
| **n°** | progressivo (ordine di estrazione = ordine di importanza) |
| **Imm. β°** | direzione di immersione del piano |
| **Incl. α°** | inclinazione |
| **Inliers** | numero di punti che sostengono il piano |
| **RMS** | scarto quadratico medio punti–piano (m) — più basso = piano più planare |
| **Planarità** | indicatore PCA: `1 - λ₃/λ₁` — `100%` = perfettamente piano, `<80%` = sospetto |

Nel viewer 3D ogni piano è un **disco semitrasparente colorato** sulla
nuvola: puoi vederne la posizione e l'orientazione.

**Spunta** i piani che vuoi importare (default: tutti).

### 5. Aggiungi al progetto

Premi **"Aggiungi i piani selezionati"**:

- Ogni piano selezionato diventa una **giacitura** in tabella
  *Discontinuità*, con β e α già calcolati
- Nelle **note** del giunto GMS scrive: `Estratto da nuvola 3D · n inliers · planarità XX%`
- I giunti rimangono **non assegnati** ad alcuna famiglia (puoi farlo
  poi manualmente o col k-means automatico)

## Tarare RANSAC sui propri dati

La qualità dell'estrazione dipende **molto** dai parametri RANSAC.
Strategia consigliata:

1. **Prova con i default**. Se trovi 3-8 piani con planarità >90% e
   RMS basso, sei a posto.
2. Se trovi **troppi piani** (rumore): aumenta *Punti minimi* o riduci
   la *Tolleranza*.
3. Se trovi **troppo pochi piani** (mancano facce evidenti): riduci
   *Punti minimi* o aumenta la *Tolleranza*.
4. Se i piani estratti hanno **β/α molto diversi tra loro** mentre
   sull'occhio sono simili: la nuvola è troppo rumorosa, ricampiona
   o filtra in CloudCompare prima.

!!! tip "Workflow misto: nuvola + Compass"
    Spesso conviene combinare: estrai i **piani principali** dalla
    nuvola 3D (le grandi facce planari del versante, scivolose da
    raggiungere a piedi) e poi integra con **misure puntuali Compass**
    sui giunti accessibili a mano. Ottieni così copertura completa
    + dati di dettaglio dove servono.

## Pre-processing in CloudCompare (opzionale ma consigliato)

Per nuvole grandi o rumorose, un pre-processing in **CloudCompare**
(gratuito, opensource) prima di esportare in `.ply` ASCII migliora
moltissimo i risultati:

1. **Sub-sampling spaziale** (es. `0.01 m`) — riduce numero di punti
   senza perdere dettaglio
2. **SOR filter** (Statistical Outlier Removal) — toglie i punti
   spurii volanti
3. **Crop** della sola zona di interesse — niente cielo, niente
   alberi, niente strada

## Limitazioni note

- **Solo `.ply` ASCII**: il formato binario non è supportato. In
  CloudCompare: *Save as → PLY → ASCII*.
- **Niente classificazione**: GMS non distingue *strato vs frattura
  vs faglia*. Tutti i piani vengono importati come "discontinuità".
  L'interpretazione resta del geologo.
- **Niente .las / .e57 / .glb**: i formati LiDAR binari e Matterport
  nativi non sono ancora supportati. Convertili in `.ply` ASCII via
  CloudCompare o tool simile.
- **Sistema di coordinate**: GMS usa il sistema della nuvola "così
  com'è". Se la tua nuvola è georeferenziata (es. WGS84 UTM), GMS la
  tratta come nuvola locale — la geolocalizzazione dei piani sulla
  mappa va fatta a mano in *Dati progetto*.

---

## Vedi anche

- [Cosa si misura](rilievo.md) — il rilievo manuale alternativo
- [GMS Compass](compass.md) — misure complementari da tablet
- [Workflow completo](workflow.md) — la nuvola nel ciclo intero
- [Formati file](formati.md) — dettagli di tutti i formati supportati

---

*Pagina utile? [Scrivici](mailto:info@geostru.ai?subject=Help%20GMS%20NX%20-%20Nuvola%203D).*
