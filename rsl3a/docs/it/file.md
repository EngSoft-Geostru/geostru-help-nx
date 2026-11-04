# File, progetti del desktop e GeoDropbox

## Il file `.rsl3anx`

Il progetto vive in sessione sul server e scade dopo 30 minuti di inattività: salvalo. **File → Salva** (Ctrl+S) riscrive il file aperto,
**Salva con nome** ne crea uno nuovo. Il file è JSON e contiene solo i dati d'ingresso: i risultati si ricalcolano all'apertura.

## Progetti del programma desktop

**File → Apri** accetta anche i progetti `.rs3` e `.rs3a` di RSL III A desktop. L'app legge spettro, parametri, categorie, T~min~ e T~max~ e
**ricalcola** tutto secondo il testo dell'Ordinanza. Se il file era salvato con impostazioni diverse (η diverso da 1, stato limite diverso da
SLV, spettro verticale) un avviso lo dice. I risultati salvati nel file non si usano: possono essere vecchi, e il desktop leggeva la condizione
1 in modo diverso (vedi [Validazione e limiti](validazione.md)).

## GeoDropbox

Il pulsante **GeoDropbox** salva il progetto in un progetto GeoDropbox, o apre un `.rsl3anx` (o un `.rs3`) salvato lì.

## Esempio

**File → Esempio** carica San Severino Marche, microzona 13, con i parametri del report GeoStru PS.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20RSL%20III%20A%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/rsl3a/docs/it/file.md).*
