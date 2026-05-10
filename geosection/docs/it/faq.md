# FAQ — domande frequenti

## Generali

### GeoSection NX è gratuito?

GeoSection NX è incluso nella suite **GeoStru NX** con piano *freemium*.
Per dettagli aggiornati visita [`geostru.ai`](https://www.geostru.ai/) o
scrivi a `info@geostru.ai`.

### Devo installare qualcosa?

No — è una web app accessibile da
[`nx.geostru.ai/geosection/`](https://nx.geostru.ai/geosection/) con
qualsiasi browser moderno.

## Sondaggi

### Posso importare sondaggi da Stratigrapher?

Sì. **Stratigrapher NX** è il software companion per le **colonne
stratigrafiche**. Esporta i sondaggi come `.json` (formato GeoStru
Stratigraphy) → in GeoSection apri **File → Importa sondaggi** → seleziona
il file → i sondaggi entrano con stratigrafia + falda + foto carote già
strutturate.

### Posso creare sondaggi da CSV?

Sì. Formato accettato:

```csv
nome,lat,lon,quota_pc,profondita_top,profondita_base,litologia,falda
S1,41.9028,12.4964,120.5,0,2.5,sabbia limosa,1.8
S1,41.9028,12.4964,120.5,2.5,8.0,argilla,
```

Header obbligatori: `nome`, `lat`/`lon` o `E`/`N`, `quota_pc`,
`profondita_top`, `profondita_base`, `litologia`. Il sondaggio è
identificato dal `nome` — più righe con lo stesso nome sono strati di
stesso sondaggio.

### Quanti sondaggi servono per una sezione?

Minimo **2 sondaggi** per generare una sezione (uno a un'estremità,
uno all'altra). Per buone sezioni servono almeno **3-5 sondaggi**
distribuiti lungo la traccia.

## Sezione

### L'interpolazione automatica degli orizzonti è sbagliata

Possibili cause:

- **Sondaggi troppo distanti** (>200 m senza pozzi intermedi) → l'interpolazione
  lineare diventa speculativa. Aggiungi sondaggi intermedi se possibile.
- **Stratigrafia molto variabile** (lente di sabbia, paleoalveo) → l'interpolazione
  lineare non cattura le variazioni laterali. Editi manualmente trascinando
  gli orizzonti.
- **Quote piano campagna sbagliate** → controlla che le quote dei sondaggi
  siano corrette.

### Posso aggiungere annotazioni alla sezione?

Sì, dopo aver generato la sezione, hai tool di annotazione:

- **Testo** — etichette, note, riferimenti
- **Frecce** — indicare direzioni di flusso, di scivolamento
- **Simboli geologici** — faglie, contatti, dischi piegamento
- **Linee/polilinee** — orizzonti aggiuntivi (es. tetto roccioso supposto)

## Esportazione

### Quale formato per la relazione tecnica?

- **PDF impaginato** è il più diffuso (titolo + sezione + tabella + foto)
- **SVG** se vuoi modificare graficamente in Inkscape/Illustrator
- **DXF** se la sezione deve entrare in tavole CAD esistenti

### Le foto carote nel PDF sono sgranate

Aumenta la **risoluzione di export** in Opzioni → Export PDF → 300 DPI per
stampa professionale (default 150 DPI per peso file).

## Manca la mia domanda

[Scrivici](mailto:info@geostru.ai?subject=Help%20GeoSection%20NX%20-%20FAQ)
e la aggiungiamo qui.
