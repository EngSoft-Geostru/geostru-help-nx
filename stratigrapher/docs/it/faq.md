# FAQ — domande frequenti

## Generali

### Stratigrapher NX è gratuito?

Stratigrapher NX è incluso nella suite **GeoStru NX** con piano *freemium*.
Per dettagli aggiornati visita [`geostru.eu`](https://www.geostru.eu/).

### Devo installare qualcosa?

No — è una web app accessibile da
[`nx.geostru.ai/stratigrapher/`](https://nx.geostru.ai/stratigrapher/).

## Templates

### Quali template sono disponibili?

- **Sondaggio standard** — colonna stratigrafica generica
- **DPSH** — penetrometro dinamico super-pesante (colpi/10 cm)
- **CPT/CPTU** — penetrometro statico (qc, fs, U se CPTU)
- **Piezometro** — sondaggio attrezzato con letture progressive del livello
  freatico
- **Inclinometro** — sondaggio attrezzato per misurare movimenti laterali

Ogni template parte con campi pre-configurati per quel tipo di prova; puoi
mescolarli (es. sondaggio standard + tubo piezometrico + SPT in profondità).

## Stratigrafia

### Posso importare la stratigrafia da CSV?

Sì. Formato:

```csv
top,base,litologia,simbolo,colore,note
0.0,2.5,sabbia limosa,SM,#e6c894,
2.5,8.0,argilla compatta,CL,#a5715f,OCR ~ 1.5
```

**File → Importa CSV** → seleziona il file → la tabella strati si popola.

### La libreria simboli non ha quello che mi serve

Stratigrapher include la libreria **UNI 11531 / ISO 14689** standard. Se ti
manca un simbolo specifico per una geologia particolare:

- Usa il simbolo "Generic" + descrizione testuale nelle note
- Oppure scrivici a `info@geostru.eu` — possiamo aggiungere simboli alla
  libreria

## Prove in sito

### Quale formato CPT è supportato?

Stratigrapher legge i formati comuni:

- **Pagani** (formato testuale `.pag`)
- **AP van den Berg** (`.gef` GEF Dutch standard)
- **Geotech** (varie estensioni)
- **CSV generico** con header `depth, qc, fs, u2`

Per formati non standard, esporta come CSV dal tuo software CPT prima di
importare.

### SPT — energia di calibrazione

L'**N1,60** richiede di sapere l'**energia liberata dal martello** durante
la prova SPT. Stratigrapher usa di default ER = 60% (Italia, USA standard).
Se hai prove con martello automatico (ER ~ 80%), modifica nel pannello
*Opzioni SPT*.

## Foto carote

### Le foto sono troppo pesanti per il PDF

Stratigrapher comprime automaticamente le foto a max 1024 px lato lungo,
~80-150 kB ciascuna. Il PDF finale è tipicamente < 5 MB anche per sondaggi
profondi (50+ m).

Per qualità ancora migliore (stampa A3): nelle Opzioni → Export PDF imposta
risoluzione 300 DPI invece di 150 DPI default.

### Posso usare il PDF su tablet in cantiere?

Sì — il PDF è leggibile da qualsiasi reader. Però per **modifiche live in
cantiere** ti conviene tenere il browser aperto su Stratigrapher e usare
**Salva nel browser** (autosave LocalStorage) — modifichi la stratigrafia
mentre carotag, alleghi le foto al volo, ecc.

## Esportazioni

### `.borehole` JSON — cosa contiene?

Tutto: anagrafica, stratigrafia, falda, prove in sito, piezometro,
inclinometro, foto (in base64). È un formato **self-contained** —
ricaricabile in Stratigrapher per riprendere il lavoro o importabile
in **GeoSection** / **LiquiTer**.

### Posso esportare in formati di altri software?

In arrivo: export per AGS4 (AGS Format Data Transfer Standard),
LogStrati (formato GeoStru desktop), ASTM D5434.

Per richieste specifiche scrivici a `info@geostru.eu`.

## Manca la mia domanda

[Scrivici](mailto:info@geostru.ai?subject=Help%20Stratigrapher%20NX%20-%20FAQ)
e la aggiungiamo qui.
