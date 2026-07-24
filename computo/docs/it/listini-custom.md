# Listini custom (prezzari personali)

Oltre ai prezzari regionali ufficiali, Computo NX può prezzare le voci
usando i **tuoi listini personali** — i listini dei fornitori e i tuoi prezzi
storici — mantenuti in **GeoStru GeoDropbox** e letti **in tempo reale**.

!!! warning "Funzione a pagamento — richiede un abbonamento GeoDropbox"

    I listini custom (livelli **Fornitore** e **Interno**) sono disponibili
    **solo con un abbonamento attivo a GeoStru GeoDropbox**.

    Senza abbonamento Computo NX continua a funzionare normalmente, ma prezza
    **solo dai prezzari regionali** (vedi [Workflow completo](workflow.md)).
    Quando apri il selettore GeoDropbox trovi l'invito ad attivare
    l'abbonamento su [`geostru.ai`](https://www.geostru.ai/).

[**Apri Computo NX**](https://nx.geostru.ai/computo/){ .md-button .md-button--primary }
[Attiva GeoDropbox](https://www.geostru.ai/){ .md-button }

---

## L'idea in breve

I listini **vivono in GeoDropbox**, non dentro Computo:

- Carichi i file dei prezzi (Excel, CSV, PDF, Word) nei tuoi **progetti GeoDropbox**.
- GeoDropbox estrae automaticamente le singole voci (codice, descrizione,
  U.M., prezzo, data).
- Computo li **legge in tempo reale**: nessun import, nessuna copia. Aggiorni
  un file su GeoDropbox → alla ricerca successiva Computo usa già il nuovo prezzo.

Il collegamento è **per progetto**: ogni progetto GeoDropbox ha il **suo**
listino. Aprendo il progetto A, Computo usa i prezzi di A; aprendo il
progetto B, quelli di B.

---

## I tre livelli di prezzo (la "cascata")

Quando chiedi all'assistente di prezzare una lavorazione descrittiva, Computo
cerca il prezzo migliore in **quest'ordine** e si ferma al **primo riscontro**:

| Priorità | Livello | Da dove arriva | Disponibilità |
|---|---|---|---|
| **1** | **Fornitore** | listino fornitore del progetto attivo | abbonamento GeoDropbox |
| **2** | **Interno** | i tuoi prezzi storici del progetto attivo | abbonamento GeoDropbox |
| **3** | **Regionale** | prezzario ufficiale, scelto sulla **regione del progetto** | sempre |

!!! info "Il livello regionale è sempre attivo"

    Se una voce non è nei tuoi listini custom (o non hai l'abbonamento),
    Computo ripiega automaticamente sul **prezzario regionale** — così hai
    comunque un prezzo di riferimento ufficiale.

---

## Flusso di lavoro passo-passo

### 1. Attiva l'abbonamento GeoDropbox

Serve un **abbonamento GeoDropbox attivo** (sblocca i livelli Fornitore e
Interno) e un **pacchetto crediti** (per l'estrazione automatica dei documenti
e per l'assistente AI). Attiva tutto da [`geostru.ai`](https://www.geostru.ai/).

### 2. Carica i listini in un progetto GeoDropbox

In [GeoDropbox](https://geodropbox.ai/) apri (o crea) il **progetto** della tua
commessa e carica i file dei prezzi nelle cartelle.

**Il livello dipende dal nome della cartella:**

| Cartella | Livello assegnato |
|---|---|
| nome che **contiene "forn"** (es. `Fornitori`, `Listini fornitore`) | **Fornitore** (priorità 1) |
| **qualsiasi altro** nome (es. la cartella predefinita `Computi e costi`) o nessuna cartella | **Interno / storico** (priorità 2) |

!!! tip "Non servono cartelle con nomi fissi"

    - La cartella predefinita **`Computi e costi`** va già bene: i file che ci
      metti diventano automaticamente il tuo **listino interno**.
    - Per un **listino fornitore**, crea una cartella con **"forn" nel nome**
      (es. `Fornitori`) e caricaci i listini dei fornitori.

**Formati riconosciuti come documento-prezzi:** `.xlsx`, `.csv`, `.pdf`, `.docx`.
Le immagini/foto vengono ignorate (non contengono righe di prezzo). Per i PDF
scansionati serve che l'OCR di GeoDropbox produca del testo.

**L'estrazione è automatica:** appena carichi un file parte in background
l'estrazione delle voci prezzo — non c'è nessun pulsante da premere. Attendi
che il file risulti elaborato (da pochi secondi a qualche minuto, secondo la
dimensione).

### 3. Collega il progetto in Computo

1. Apri [`nx.geostru.ai/computo/`](https://nx.geostru.ai/computo/).
2. Nell'intestazione, clicca il pulsante **GeoDropbox** e **seleziona il
   progetto** dove hai caricato i listini.
3. Compaiono:
      - l'**indicatore del progetto attivo** (il nome del progetto);
      - il badge verde **✨ Listini custom** se l'abbonamento è attivo
        (altrimenti l'invito ad abbonarti).

Dallo stesso pulsante puoi anche **salvare e riaprire il computo** sul progetto
GeoDropbox (vedi sotto).

### 4. Prezza con l'assistente AI

Nella chat, **descrivi la lavorazione** — **senza** indicare id o nome del
listino:

> *"Prezzami 120 m di cavo FG16OR16 3x2,5 mmq"*

L'assistente:

1. Cerca in cascata: **Fornitore → Interno → Regionale**, e prende il primo
   riscontro.
2. Ti mostra **prezzo, fonte** (il nome del file di listino) **e data del prezzo**,
   indicando il **livello** usato.
3. **Aggiunge la voce al computo** con la quantità richiesta.

!!! example "Esempio"

    Con un listino interno che contiene *"Cavo FG16OR16 3x2,5 posa in tubo — 3,20 €/m"*,
    alla richiesta *"prezzami 120 m di cavo FG16OR16 3x2,5"* l'assistente
    risponde **3,20 €/m** (fonte: il tuo file di listino, data del prezzo) e
    inserisce la voce a **120 × 3,20 = 384,00 €**, livello **Interno**.

    Chiedendo invece *"prezzami uno scavo di sbancamento"* — voce non presente
    nei tuoi listini — la cascata ripiega sul **prezzario regionale**.

### 5. Aggiorna o rimuovi un listino

Tutto è **in tempo reale**, senza re-import:

- **Prezzo cambiato?** Carica il file aggiornato su GeoDropbox → alla ricerca
  successiva Computo usa già il nuovo prezzo.
- **Listino da togliere?** Cancella il file su GeoDropbox → sparisce dalla cascata.

Gestisci i listini **solo su GeoDropbox** (carica / scarica / cancella i file):
Computo li **legge**, non li duplica.

### 6. Salva il computo sul progetto

Dal pulsante **GeoDropbox** nell'intestazione puoi **salvare il computo** nel
progetto attivo e **riaprirlo** in un secondo momento — così input, listino e
preventivo restano insieme, sulla stessa commessa.

---

## La regione del progetto

Il **livello Regionale** viene scelto in base alla **regione del progetto**
GeoDropbox (dalla posizione geolocalizzata del progetto):

- Se il progetto ha una regione → Computo usa il **prezzario di quella regione**.
- Se non ce l'ha (o non hai un progetto aperto) → cerca **su tutti i prezzari
  regionali** disponibili.

Puoi comunque indicare tu la regione nella richiesta all'assistente, se serve.

---

## Cosa succede senza abbonamento o senza progetto

| Situazione | Comportamento |
|---|---|
| **Nessun abbonamento GeoDropbox** | Livelli Fornitore/Interno disattivati → solo **Regionale** + invito all'abbonamento |
| **Abbonato, ma nessun progetto aperto** | Solo **Regionale**; l'assistente può suggerirti di aprire un progetto per usare i listini custom |
| **Voce non nei listini custom** | Fallback automatico al **Regionale** della regione del progetto |

In tutti i casi Computo NX **non si blocca**: al massimo prezza dal prezzario
regionale.

---

## Esportazione

Quando esporti il preventivo (PDF / Excel), ogni voce riporta **prezzo, fonte
e data del prezzo**: così il committente vede da quale listino (e di quando)
arriva ciascun importo.

---

## Risoluzione problemi

L'assistente **non trova** una voce che so essere nel listino:

- **Estrazione non ancora finita** — hai appena caricato il file: attendi
  1–2 minuti e riprova.
- **Formato non riconosciuto** — il file non è `.xlsx/.csv/.pdf/.docx`, oppure
  è un PDF/immagine senza testo (OCR non riuscito).
- **Progetto non selezionato** — controlla l'indicatore del progetto attivo
  nell'intestazione.
- **Badge non verde** — l'abbonamento GeoDropbox non risulta attivo: i livelli
  custom sono disattivati.
- **Descrizione troppo diversa** — prova parole chiave più vicine a quelle del
  listino.

---

*Pagina utile? [Scrivici](mailto:info@geostru.ai?subject=Help%20Computo%20NX%20-%20Listini%20custom).*
