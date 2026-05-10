# AI Import — estrai giaciture da foto, PDF, Excel, testo

L'**AI Import Wizard** usa Gemini (Google) per estrarre **automaticamente**
le triplette `distanza | β | α` da fonti dati *non strutturate*:

- **Foto del taccuino di campo** (jpg/png da smartphone)
- **PDF di rilievi precedenti** (anche scannerizzati)
- **Excel con header strani**, fogli con celle unite, layout creativi
- **Testo libero** copiato da email, chat, report

L'AI è una scorciatoia per **i casi disordinati**. Se hai già un CSV
strutturato pulito, usa **File → Importa da CSV / TXT generico** —
è più veloce e prevedibile.

## Quando ha senso usarlo

- ✅ Hai una **foto del taccuino** scarabocchiato a mano
- ✅ Hai un **PDF** con tabelle di giaciture (anche scannerizzato come immagine)
- ✅ Hai un **vecchio Excel** con layout improbabile
- ✅ Hai un **testo libero** del tipo *"Sul versante Nord ho misurato il
  primo giunto a 165/72, poi a metro 5 un altro a 170/68, …"*

- ❌ Hai un CSV pulito → usa l'import diretto
- ❌ Hai un `.gms` → usa **File → Apri**
- ❌ Hai foto di **fronti rocciosi** (non di tabelle): l'AI non
  estrae giaciture dalla geometria della parete; usa
  [Nuvola di punti 3D](nuvola-3d.md) per quello

## Apertura

Da GMS NX:

1. Toolbar in alto → **File → Importa da → Foto/PDF (AI)**
2. Si apre il **modal AI Import**

Oppure dall'**empty state** (schermata progetto vuoto):

1. Card **"Importa con AI"**

## Procedura

### 1. Carica i file

Trascina (drag&drop) o clicca **"Sfoglia"** per selezionare:

- **PNG / JPG** — foto, scansioni
- **PDF** — anche multipagina, anche ibrido testo + immagini
- **XLSX / XLS** — fogli Excel
- **CSV / TXT** — testi grezzi
- **Più file insieme** — l'AI processa il batch e unisce i risultati

Limite di dimensione: **20 MB per file**.

### 2. Aggiungi un'eventuale nota all'AI

Campo **"Note per l'AI (opzionale)"**:

> *"Le giaciture sono in formato dip/dip-direction (non immersione/dip),
> conviene invertire le colonne. Le distanze sono in centimetri, da
> convertire in metri."*

Le note sono **istruzioni in linguaggio naturale** che l'AI seguirà
durante l'estrazione. Utili per convenzioni non standard, unità di
misura, o per dire all'AI di **ignorare** righe che non sono giaciture.

### 3. Premi "Estrai con AI"

GMS:

1. Manda i file + nota a Gemini 2.5 Flash con un **prompt strutturato**
   (Italian) e uno **schema JSON forzato** (`responseSchema`).
2. Gemini analizza i contenuti (OCR + comprensione tabellare + parsing
   testuale) e restituisce un array di giaciture con campi tipizzati:
   `distance`, `dipDirection` (β), `dip` (α), `family` (opzionale),
   `notes` (opzionale).
3. GMS valida il JSON, scarta righe con valori fuori range
   (β ∉ [0,360] o α ∉ [0,90]).
4. Mostra un'**anteprima tabellare** con le righe estratte.

Tempo tipico: **5-15 secondi** per un file di poche pagine, fino a
**40-60 secondi** per PDF lunghi o batch grossi.

### 4. Verifica e conferma

Nell'anteprima:

- **Spunta** le righe da importare (default: tutte)
- **Modifica** valori sbagliati direttamente nella tabella
- **Elimina** le righe spurie
- Premi **"Aggiungi al progetto"**

Le giaciture confermate entrano nella tabella *Discontinuità* di GMS
**aggiungendosi** a quelle eventualmente già presenti.

## Cosa l'AI sa estrarre bene

- Tabelle con header chiaramente etichettati (`β`, `α`, `dip`,
  `direzione`, `inclinazione`, `imm`, `incl`, …)
- Triplette `distanza | imm | incl` su righe regolari
- Coppie `imm/incl` o `dip/dipdir` separate da `/` o spazio
- Formati misti `12.5 m → 165° / 72°` o equivalenti
- Note in colonne separate (rugosità, riempimento, persistenza, …)
  → entrano nel campo `notes` della giacitura

## Cosa l'AI fa fatica a estrarre

- **Diagrammi grafici** (stereonet di altri software, rose dei venti):
  l'AI riconosce che è uno stereonet ma non riesce a estrarre i poli
  con precisione utile. **Non funziona** per "ridigitalizzare" un
  vecchio stereonet pubblicato.
- **Foto sfocate o in cattiva illuminazione**: l'OCR fallisce su
  testo poco leggibile. Riscatta la foto in luce diffusa.
- **Scrittura a mano molto personale**: l'OCR cerca di indovinare ma
  il margine d'errore può essere alto. **Verifica sempre l'anteprima**.
- **Rilievi in convenzioni esotiche** (apparent dip, strike + dip
  con regola della mano destra, …): meglio convertire a mano in
  immersione/dip prima di passarle all'AI.

## Configurazione e costi

L'AI Import usa la **chiave Gemini di GeoStru**, già configurata sul
server. Non devi fornire la tua. Il limite di utilizzo per utente è
generoso ma non illimitato — chi ha esigenze massive può richiedere
un piano custom (info@geostru.eu).

Modello in uso: **Gemini 2.5 Flash** con `responseSchema` strutturato
(estrazione tipata e validata).

## Privacy

I file caricati transitano attraverso i server Google (Gemini API).
GMS **non li conserva** dopo l'estrazione (i file sono cancellati al
termine della sessione). Se i tuoi dati sono **riservati** (perizie
giudiziali, siti militari, …) preferisci l'import manuale.

---

## Vedi anche

- [Cosa si misura](rilievo.md) — convenzioni che l'AI conosce
- [Formati file](formati.md) — alternative strutturate al CSV/TXT
- [Workflow completo](workflow.md) — l'AI Import nel ciclo intero

---

*Pagina utile? [Scrivici](mailto:info@geostru.ai?subject=Help%20GMS%20NX%20-%20AI%20Import).*
