# FAQ — domande frequenti

## Generali

### Computo NX è gratuito?

Computo NX è incluso nella suite **GeoStru NX** con piano *freemium*. Comandi
locali (catalogo, edit voci, export) sono accessibili nel piano Free.
La **chat AI** consuma crediti per token. Per dettagli aggiornati visita
[`geostru.eu`](https://www.geostru.eu/).

### Devo installare qualcosa?

No — è una web app accessibile da
[`nx.geostru.ai/computo/`](https://nx.geostru.ai/computo/) con qualsiasi
browser moderno.

## Prezzari

### Quali prezzari sono disponibili?

Al momento:

- **CAL25** (Calabria 2025) — completo, ufficiale

In arrivo: gli altri prezzari regionali italiani principali. Per richieste
specifiche scrivici a `info@geostru.eu`.

### Posso caricare un prezzario custom?

Non al momento via UI — i prezzari sono centralizzati lato server. Per
prezzari aziendali custom, contatta `info@geostru.eu`: possiamo configurare
un prezzario dedicato.

## Import AI

### Il PDF è stato letto male, mancano voci

Cause comuni:

- PDF è una **scansione di bassa qualità** → l'OCR fa fatica. Riscannerizza
  in alta risoluzione (300+ DPI) o usa un PDF testuale (esportato dal
  software originale).
- **Layout grafico complesso** (caselle decorative, watermark) confonde l'AI.
  Prova a "pulire" il PDF (rimuovi watermark) prima di drop.
- **Voci troppo brevi o ambigue** → l'AI non trova un match nel prezzario.
  In quel caso aggiunge la voce con stato "Da verificare" — modifica il
  match manualmente cercando nel catalogo.

### L'AI ha sbagliato le quantità

Verifica sempre le quantità che propone — l'AI può sbagliare a leggere
numeri specialmente in PDF scansionati. Click sulla riga → editi a mano la
quantità.

### Posso usare l'AI in modo gratuito?

L'AI consuma **crediti** (token Anthropic). Il piano Free include una
quota mensile di crediti, sufficiente per qualche estrazione di dimensione
media. Per uso intensivo serve l'abbonamento.

## Calcolo / Output

### Quale formato esporto per l'inviodo all'Ente?

Dipende dal capitolato della gara/appalto. In generale:

- **PDF impaginato** è il più diffuso e accettato ovunque
- **Excel** se l'Ente vuole un formato editabile
- **XPWE** se richiede uno standard di interscambio (Pubblica Amministrazione
  italiana)

In dubbio, esporta in tutti e 3 — sono pochi click e copri tutti i casi.

### Posso applicare uno sconto / ribasso d'asta?

Sì — in fondo alla tabella del computo, sezione **Riepilogo**, inserisci la
percentuale di sconto. Si applica al totale lordo e ricalcola il netto.

### IVA?

Aliquote IVA configurabili per opera (default 22%, 10% per ristrutturazioni
agevolate, ecc.).

## Manca la mia domanda

[Scrivici](mailto:info@geostru.ai?subject=Help%20Computo%20NX%20-%20FAQ) e la
aggiungiamo qui.
