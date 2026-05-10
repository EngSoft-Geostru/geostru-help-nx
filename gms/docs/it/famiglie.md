# Famiglie di discontinuità

I giunti rilevati su un fronte roccioso non sono distribuiti a caso:
si raggruppano in **famiglie** (joint sets) di orientazione simile,
generate dalle stesse fasi tettoniche o dagli stessi processi di
rilascio tensionale. Identificare correttamente le famiglie è il
primo passo dell'analisi cinematica.

GMS NX offre **due strategie complementari**, che possono coesistere
nello stesso progetto.

## A. Suddivisione automatica (k-means sferico)

GMS raggruppa i poli sulla sfera unitaria con un **k-means sferico**:
la distanza tra due poli è l'**angolo polo–polo** (non la distanza
euclidea piana sul disco).

### Come si attiva

Tab **Famiglie**:

1. Imposta **Numero famiglie** (default `4`)
2. Lascia attivo il toggle **"Suddivisione automatica"**
3. Premi **Calcola**

GMS:

1. Inizializza i centri con **k-means++** (i centri iniziali sono il
   più lontani possibile tra loro per evitare convergenza a minimi
   locali poveri).
2. Itera: assegna ogni polo al centro angolarmente più vicino,
   ricalcola il centro come **media Fisher** dei poli del cluster,
   ripete fino a convergenza (max 50 iterazioni).
3. Per ogni cluster calcola: **vettore medio**, **k**, **α₉₅**, **R̄**.

### Quanti cluster?

La scelta di `N` non è banale. Suggerimenti pratici:

- **3–4 famiglie** è il caso più comune (1 stratificazione + 2-3
  sistemi di giunti tettonici)
- **5–6 famiglie** se il rilievo è grande e l'ammasso è molto
  fratturato
- **2 famiglie** in falesie omogenee con stratificazione + 1 sistema
  di giunti
- **>6** raramente utile; produce cluster con pochi poli e statistica
  Fisher inaffidabile

!!! tip "Quando il k-means non basta"
    Se GMS ti propone una famiglia con **2-3 poli** e **k < 5**, sospetta
    che quella "famiglia" non sia una vera famiglia ma rumore. Riduci
    `N` di 1 e rilancia. Oppure passa a **famiglie attese**.

### Statistica Fisher per cluster

Per ogni famiglia, GMS riporta nella tab **Statistica**:

| Indicatore | Significato |
|---|---|
| **n** | numero di poli nel cluster |
| **β / α** | direzione e inclinazione del polo medio |
| **R̄** | modulo del vettore risultante normalizzato (0 = isotropo, 1 = perfettamente concentrato) |
| **k** | parametro di concentrazione di Fisher (alto = serrato) |
| **α₉₅** | semi-apertura del cono di confidenza al 95% (gradi) |

Soglie indicative:

- **R̄ > 0.95** → cluster ben definito
- **k > 30** → famiglia matematicamente "vera"
- **α₉₅ < 5°** → polo medio molto preciso

## B. Famiglie attese (centri pre-orientati)

A volte conosci già le famiglie da un rilievo precedente, dalla
letteratura di zona (perizia regionale, atlante geologico) o da una
campagna a parte. Vuoi che GMS **classifichi i giunti correnti** in
quelle famiglie, non che le scopra ex novo.

### Come si attiva

Tab **Famiglie**:

1. Premi **+ Aggiungi famiglia attesa**
2. Inserisci **nome** (es. `K1 — stratificazione`), **dip α**, **dip-direction β**
3. Eventualmente imposta **colore** e **note**
4. Ripeti per ogni famiglia attesa
5. Imposta **Tolleranza** (default `30°`) — l'angolo polo–centro massimo
   per cui un giunto viene assegnato
6. Premi **Assegna giunti alle famiglie attese**

GMS:

1. Per ogni giunto, calcola l'angolo tra il suo polo e il polo di ogni
   famiglia attesa (1-NN sferico).
2. Assegna alla famiglia con angolo minimo, **purché** entro la
   tolleranza.
3. I giunti **oltre tolleranza** restano disponibili per il k-means
   automatico (se attivo).

### Quando è utile

- **Confronto temporale** — hai un rilievo del 2020 e uno del 2026
  sullo stesso versante; vuoi vedere se i nuovi giunti appartengono
  alle famiglie note o se ne è apparsa una nuova
- **Continuità di studio** — i tuoi colleghi hanno definito le
  famiglie del bacino e tu le devi adottare
- **Pochi dati** — se hai solo 10-15 giunti, il k-means non ha massa
  critica; meglio agganciarli a famiglie già caratterizzate

## C. Modalità mista (consigliata)

Le due strategie **convivono**. Configurazione tipica:

1. Definisci 1-2 famiglie attese (le più sicure: stratificazione,
   sistema principale)
2. Lascia il k-means automatico attivo con `N = 3` o `N = 4`
3. **Calcola**

GMS prima assegna i giunti alle famiglie attese (entro tolleranza),
poi applica il k-means **solo ai giunti residui**. Risultato:
classificazione *guidata* dove sei sicuro, *esplorativa* sul resto.

## Cylindrical Best Fit (Vollmer / Woodcock)

Indipendentemente dalla suddivisione in famiglie, GMS calcola il
**Cylindrical Best Fit** dell'intero dataset: l'ipotesi è che i poli
giacciano su un **cerchio massimo** (significherebbe che le
discontinuità sono parallele a un asse comune, tipico delle pieghe
cilindriche).

Risultati nella tab **Statistica**:

- **Asse di piegatura β/α** — la direzione e il plunge dell'asse
  comune
- **Indici di Woodcock K e C**:
  - `K = ln(λ₁/λ₂) / ln(λ₂/λ₃)` — forma del cluster (cluster vs
    girdle)
  - `C = ln(λ₁/λ₃)` — intensità del fabric

Soglie classiche (Woodcock 1977):

| K | C | Interpretazione |
|---|---|---|
| >1 | >2 | cluster forte (1 sola famiglia dominante) |
| <1 | >2 | girdle forte (poli su un cerchio massimo → piegatura cilindrica) |
| ≈1 | <2 | random (rilievo non organizzato) |

## Stella di immersione

La **stella di immersione** (rosa polare delle β) è disponibile nella
tab **Statistica**: mostra la distribuzione delle direzioni di
immersione su 360°, indipendentemente dalle famiglie. È utile per
identificare *direzioni preferenziali* anche quando la classificazione
in famiglie è confusa.

---

## Vedi anche

- [Stereonet](stereonet.md) — visualizzazione dei poli e ciclografiche
- [Test di Markland](markland.md) — uso delle famiglie nella verifica
  cinematica
- [Workflow completo](workflow.md) — le famiglie nel ciclo intero

---

*Pagina utile? [Scrivici](mailto:info@geostru.ai?subject=Help%20GMS%20NX%20-%20Famiglie).*
