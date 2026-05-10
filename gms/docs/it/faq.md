# FAQ — domande frequenti

## Generali

### GMS NX è gratuito?

GMS NX è incluso nella **suite GeoStru NX** con un piano *freemium*:

- **Free** — accesso illimitato all'app, calcoli completi, stereonet
  2D/3D, esportazione CSV
- **Subscription** — sblocca: report Word, esportazione DXF,
  AI Import, import nuvole 3D, batch import multi-file, supporto
  prioritario

Per dettagli aggiornati visita [`geostru.ai`](https://www.geostru.ai/)
o scrivi a info@geostru.ai.

### Devo installare qualcosa?

**No**. GMS NX è una **web app**: si apre da
[`nx.geostru.ai/gms/`](https://nx.geostru.ai/gms/) in qualsiasi
browser moderno (Chrome, Edge, Safari, Firefox). Funziona su PC
Windows / Mac / Linux, su tablet, su smartphone.

### Funziona offline?

**Parzialmente**. Una volta caricata, l'app continua a funzionare
anche senza connessione **per il calcolo locale** (stereonet, Fisher,
Markland, k-means). Ma:

- L'**AI Import** richiede connessione (chiama Gemini)
- L'**Import nuvole 3D** richiede connessione (server-side RANSAC)
- Il **Trasferimento via codice** richiede connessione
- Il **Salvataggio in cloud** non esiste — si salva sempre localmente

Se devi lavorare in cantiere senza segnale: scarica prima un
`.gms` di esempio per "scaldare" la cache PWA, poi fai
*File → Salva* per memorizzare in IndexedDB.

### I miei dati vengono inviati a server GeoStru?

**No, per default**. I calcoli avvengono nel **browser** (lato
client), e i progetti `.gms` restano **sul tuo PC**.

I server GeoStru vengono coinvolti solo se attivi:

- **Codice di trasferimento** (i dati Compass passano per i nostri
  server, TTL 30 giorni, poi cancellati)
- **AI Import** (i file vanno a Google Gemini per l'estrazione, non
  vengono conservati)
- **Import nuvole 3D** (server-side per RANSAC, ma la nuvola viene
  cancellata a fine elaborazione)

Per dati riservati, evita queste 3 funzioni e lavora con import
manuale + file `.gms`.

---

## Misurazioni

### β e α — quale viene per primo?

Per convenzione GeoStru (e ISRM italiana), si scrive **β/α** =
**immersione/inclinazione**. Esempio: `165/72` significa β=165°,
α=72°.

In molta letteratura anglosassone si scrive invece **dip/dip
direction**, che corrisponde a **α/β** (inverso!). Se importi dati
da fonti in inglese, **controlla due volte** quale convenzione usano.

GMS NX nelle import accetta entrambe le notazioni (header CSV
flessibile), ma in tabella e nei calcoli le colonne sono sempre
*Imm. β° | Incl. α°* nell'ordine GeoStru.

### Come calcolo l'angolo d'attrito φ?

φ è una proprietà del **materiale roccioso lungo il giunto**, non del
giunto in sé. Stime tipiche:

- **Roccia sana, giunto pulito** (granito, basalto, calcare massivo):
  **35–40°**
- **Roccia con riempimento calcite o sabbia**: **30–35°**
- **Roccia con riempimento argilloso**: **20–28°**
- **Argille, scisti alterati**: **10–18°**

Stime di campo: prova del gradino (versante stabilizzato a un certo
α) o prova di taglio in laboratorio (Hoek shear box).

In dubbio, fai **2 calcoli con φ = 25° e φ = 35°** per vedere
quanto cambia la conclusione (analisi di sensibilità).

---

## Analisi e risultati

### Quante misure servono per un'analisi affidabile?

**Minimo 30** giaciture per avere una statistica Fisher significativa.
Sotto 30 puoi comunque calcolare ma `k` e `α₉₅` sono poco affidabili
e il k-means tende a sovra-adattarsi.

**Numero ideale**: 50–150 giaciture per fronte, distribuite su una
linea di scansione di 10–30 m.

### Il banner è verde ma so che il versante è instabile. Perché?

Markland è un test **necessario ma non sufficiente**. Risponde a:
*"esiste un meccanismo di rottura geometricamente compatibile?"* —
non a *"il versante crollerà?"*.

Cause comuni di "verde ma instabile":

- **Erosione progressiva** — non un singolo cinematismo, ma
  alterazione lenta delle pareti
- **Fenomeni dinamici** — sisma o pioggia intensa che cambiano
  effettivamente la stabilità
- **Ribaltamenti flessurali** — non valutati da Markland classico
- **Rotture circolari** in roccia molto fratturata (R&Q-Bishop)
- **Cinematismi 3D complessi** che 2D di Markland non vede

GMS produce input geometrici. L'interpretazione finale è del
geologo / ingegnere.

### Posso confidarmi al 100% sul k-means automatico?

**No**. Il k-means è uno strumento esplorativo. Sempre da verificare:

1. Il numero `N` di famiglie scelto è ragionevole?
2. Le famiglie restituite hanno **k > 30** e **R̄ > 0.95**?
3. La mappa isodensità conferma visivamente i cluster?
4. L'esperienza di campo concorda con quanto visto?

Se anche solo uno di questi controlli fallisce, prova `N ± 1` o passa
alle **famiglie attese**.

### Lo stereonet 3D si blocca, perché?

Three.js (la libreria 3D) richiede WebGL. Se il browser ha WebGL
disabilitato o la GPU del PC è molto vecchia (>10 anni), il viewer
3D può rallentare o non avviarsi. Soluzioni:

- Aggiorna il browser all'ultima versione
- Abilita "*accelerazione hardware*" nelle impostazioni del browser
- Su PC molto vecchi, lavora in modalità **2D** (stereonet 2D è
  CPU-only, va sempre)

---

## Compass (tablet)

### Compass legge β/α completamente sbagliati. Cosa controllo?

1. **Calibrazione magnetometro** — fai il "disegno a 8" in aria
   per 5 secondi
2. **Interferenze metalliche** — allontanati 1-2 m da auto, cancelli,
   armadi metallici, cavi elettrici, pacchetti di cavi sotterranei
3. **Custodia magnetica** — alcune cover (in particolare quelle con
   chiusura magnetica per iPad) influenzano il magnetometro: tieni
   il dispositivo aperto e libero
4. **HTTPS richiesto** — verifica di essere su `https://` non su
   `http://`. Su iOS i sensori non si attivano se sei in HTTP.

### Posso usare Compass su Android?

Sì, su **Chrome Android** (versione recente). Su **Firefox Android**
l'accesso al magnetometro è dietro flag sperimentale, sconsigliato.

### E su iPad / iPhone?

Sì, su **Safari iOS 13+**. Al primo accesso iOS chiede il permesso
ai sensori — tocca *Consenti*.

---

## AI Import

### L'AI ha estratto male le giaciture. Cosa faccio?

1. **Verifica la nota all'AI** — le istruzioni che hai dato erano
   chiare? *"Le giaciture sono in formato dip/dip-direction"* è meglio
   di *"sono dati strutturali"*
2. **Migliora la sorgente** — se è una foto sfocata, riscatta in luce
   diffusa
3. **Modifica nell'anteprima** — i valori sbagliati si correggono
   manualmente prima di confermare
4. **Riprova senza la nota** — a volte la nota in italiano confonde
   quando il file è in inglese; rilancia senza note

### L'AI è gratuita?

L'AI Import usa la chiave Gemini di GeoStru. Per gli utenti
*Subscription* è inclusa con **limite di utilizzo generoso** (alcune
centinaia di estrazioni al mese). Per gli utenti *Free* è disponibile
con limite più ristretto.

---

## Trasferimento codice

### Il codice non funziona, "codice non valido"

- Verifica che siano passati meno di **30 giorni** dalla generazione
- Riconta i caratteri (devono essere **8**, esclusi i trattini)
- Non confondere `0` (zero) con `O` (lettera o), `1` con `l`/`I` —
  l'alfabeto Crockford evita queste confusioni
- Rigenera il codice dal tablet (in Compass: *Trasferisci al PC* →
  nuovo codice)

### Posso usare lo stesso codice 2 volte?

Sì, entro la TTL di 30 giorni. Utile per importare lo stesso rilievo
su più PC.

---

## Nuvola di punti 3D

### Il mio file `.las` non si apre

GMS supporta solo **`.ply` ASCII**, **`.obj`**, **`.xyz`/`.txt`**.
Per i `.las` LiDAR binari devi prima convertire in CloudCompare:
*File → Open LAS → Save as → PLY → ASCII*.

Il supporto nativo `.las` / `.e57` è in roadmap.

### RANSAC trova 0 piani

- Riduci **Punti minimi per piano** (es. da 100 a 30)
- Aumenta **Tolleranza** (es. da 0.05 a 0.10 m)
- Verifica che la nuvola non sia composta da **superfici
  cilindriche/sferiche** (es. tronchi, blocchi tondi): RANSAC trova
  solo piani

### RANSAC trova 50 piani spurî

- Aumenta **Punti minimi per piano** (es. da 100 a 500)
- Riduci **Tolleranza** (es. da 0.05 a 0.02 m)
- Riduci **Numero massimo di piani** (es. 4-6 invece di 8)

---

## Esportazioni

### Il Report Word non si apre

- Verifica di avere **Microsoft Word 2016+**, **LibreOffice 6+**, o
  **Google Docs**
- Versioni vecchie di Word possono dare errori di compatibilità
- Apri con LibreOffice come fallback (gratuito, gestisce sempre il
  `.docx`)

### Voglio personalizzare il template Word

Per ora il template è centralizzato lato server. Per un template
custom (logo studio, intestazione personale, font diverso) scrivi a
info@geostru.ai — possiamo configurare un template dedicato per il
tuo studio.

---

## Manca la mia domanda

[Scrivici](mailto:info@geostru.ai?subject=Help%20GMS%20NX%20-%20FAQ)
e la aggiungiamo qui. Le FAQ vivono e crescono con le domande
ricorrenti dei nostri utenti.
