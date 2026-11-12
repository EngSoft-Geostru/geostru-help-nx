# Domande frequenti

## Generali

### Devo installare qualcosa?

No. Hydrogeo NX funziona nel browser all'indirizzo
[nx.geostru.ai/hydrogeo](https://nx.geostru.ai/hydrogeo/), su Windows, Mac e Linux.

### Perché la mappa è vuota quando apro l'app?

Le stazioni sono più di 6.000: la mappa mostra quelle che cerchi. Apri l'**Assistente** e
chiedi, per esempio, «Trova stazioni in Calabria». Vedi [Assistente AI](assistente.md).

### Hydrogeo NX calcola Gumbel, TCEV o le curve di possibilità pluviometrica?

No. Hydrogeo NX fornisce i dati; l'analisi statistica è in Runoff Lab NX, che importa le
serie direttamente. Vedi [Collegamenti con le altre app NX](integrazioni.md).

## Stazioni

### Da dove vengono i dati?

Da ISPRA (Annali Idrologici) e da dodici servizi regionali. L'elenco è in
[Fonti e limiti dei dati](fonti.md); ogni stazione indica la sua fonte nella scheda.

### Non trovo stazioni nella mia zona

Allarga il raggio della ricerca o togli il filtro sugli anni di dati. Ricorda che alcune
stazioni storiche non hanno coordinate e non compaiono sulla mappa, ma l'assistente le trova
per nome. Se manca davvero una fonte, scrivici: vedi [Fonti e limiti dei dati](fonti.md).

### La stazione non ha dati di 1 ora

Non tutte le stazioni hanno tutte le durate. Le stazioni storiche hanno spesso solo il
massimo di 24 ore; le durate brevi richiedono un pluviografo. Cerca una stazione vicina con
la voce «Pioggia oraria» in **Tipo dati**.

### Quanti anni di dati servono?

La [rilevanza](mappa.md#la-rilevanza) aiuta: da 20 anni in su è buona, da 10 a 20 media,
sotto i 10 bassa. Per un'analisi statistica solida punta ad almeno 20–30 anni, oppure usa una
stazione vicina con una serie più lunga.

### Due stazioni con lo stesso nome: quale scelgo?

Sono stazioni diverse, spesso una vecchia stazione degli Annali e una nuova stazione
regionale. Confronta periodo, anni di dati e fonte nella scheda.

## Dati e crediti

### Ho chiuso il browser: devo sbloccare di nuovo la stazione?

Sì. Lo sblocco resta attivo nella scheda del browser in cui l'hai fatto. Esporta i dati che
ti servono prima di chiudere. Vedi [Accesso e crediti](crediti.md).

### Un'esportazione ripetuta costa due volte?

Se la ripeti identica a breve distanza (nella stessa finestra di 15 minuti), no. Più tardi è
una nuova esportazione. Un'operazione che non restituisce dati non viene mai addebitata.

### Il PDF è disponibile in inglese?

No, il **PDF Report** è in italiano. Per gli altri usi esporta in CSV o Excel.

## Altre app

### Come porto i dati in Runoff Lab NX?

In Runoff Lab NX: **Importa → Da Hydrogeo NX…**, cerca la stazione e fai clic. Vedi
[Collegamenti con le altre app NX](integrazioni.md).

### Il file PLV si apre in Runoff Lab NX?

No: Runoff Lab NX importa le stazioni direttamente da Hydrogeo NX, senza file. Il PLV serve
ai software desktop GeoStru.

## Manca la tua domanda?

[Scrivici](mailto:info@geostru.ai?subject=Hydrogeo%20NX%20FAQ) o apri un ticket
dall'[assistente](assistente.md): la aggiungiamo qui.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Hydrogeo%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/hydrogeo/docs/it/faq.md).*
