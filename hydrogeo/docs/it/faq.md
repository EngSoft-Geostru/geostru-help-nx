# FAQ — domande frequenti

## Generali

### Hydrogeo NX è gratuito?

Hydrogeo NX è incluso nella suite **GeoStru NX** con piano *freemium*.
Ricerca + visualizzazione dati sono accessibili nel piano Free; analisi
statistica avanzata e export PDF/PLV richiedono Subscription. Per
dettagli aggiornati visita [`geostru.eu`](https://www.geostru.eu/).

### Devo installare qualcosa?

No — è una web app accessibile da
[`nx.geostru.ai/hydrogeo/`](https://nx.geostru.ai/hydrogeo/).

## Stazioni

### Mancano stazioni nella mia zona

Il database copre 19 regioni italiane. Per regioni non ancora integrate
(o per zone con stazioni private), scrivici a `info@geostru.eu` —
valutiamo l'aggiunta delle fonti.

### La stazione che ho selezionato non ha dati per durata 1h

Non tutte le stazioni hanno tutte le durate. Le **stazioni storiche
ISPRA** hanno tipicamente durate "lunghe" (1, 3, 6, 12, 24 h), mentre le
**stazioni regionali moderne** spesso forniscono anche durate "brevi"
(15 min, 30 min) utili per il calcolo di fognature urbane.

In assenza di dati per la durata che ti serve:

- Usa la **statistica spaziale** del territorio per estrapolare
- Usa una stazione vicina con la durata richiesta
- Considera la **stazione più rappresentativa** entro 30 km

## Statistica

### Quanti anni servono per Gumbel?

Minimo **15-20 anni** di osservazioni continue. Sotto 15 anni la
statistica è inaffidabile. Sopra **30 anni** è considerata "buona".
Sopra 50 anni "ottima".

Se la stazione ha pochi anni, considera di:

- Usare una stazione vicina con più anni
- Usare la **distribuzione areale** dei parametri (per zona, non per
  singola stazione)

### Gumbel EV1 vs TCEV — quando usare cosa?

- **Gumbel EV1**: piogge omogenee (un solo regime climatico nel sito).
  Buono per la maggior parte dei siti italiani.
- **TCEV**: piogge bimodali (sito influenzato sia da convettive estive
  che da fronti invernali). Tipico in **zone alpine** o in **siti
  costieri esposti**.

Verifica con il **test KS**: se Gumbel non passa il test, prova TCEV.

### Cosa succede per T molto grandi (T = 500, 1000)?

L'estrapolazione a T molto grandi è **incerta**:

- Con 30 anni di dati, T = 100 è già un'estrapolazione di 3× → margine
  di errore 20-30% sull'altezza
- T = 500-1000 è ai limiti del significato fisico. Per opere con vita
  utile lunga (dighe, ferrovie), la NTC raccomanda di usare metodi
  multi-stazione + variabilità areale.

## Curve IDF

### Quale tempo di ritorno scelgo?

Dipende dall'opera:

- **Fognature urbane**: T = 5-10 anni (NTC sezione idraulica)
- **Strade**: T = 25 anni
- **Ponti**: T = 100-200 anni (a seconda della classe)
- **Dighe**: T = 1000-10000 anni

Verifica sempre il **capitolato** del committente.

## Esportazione

### Cos'è il formato PLV?

PLV = "Pluvio" — formato testuale standard GeoStru per i dati
pluviometrici. Caricabile da:

- **Runoff Lab NX** (web)
- **Idroclima** (desktop GeoStru)
- Software esterni che supportano PLV (alcuni software italiani di
  calcolo idraulico)

### Posso esportare in formato standard internazionale?

Per ora i formati supportati sono CSV / Excel / PDF / PLV. In arrivo:
**JSON-LD** schema idrologico, **WaterML** (OGC standard).

## Manca la mia domanda

[Scrivici](mailto:info@geostru.ai?subject=Help%20Hydrogeo%20NX%20-%20FAQ)
e la aggiungiamo qui.
