# File, progetti del desktop e GeoDropbox

## Il menu File

| Voce | Che cosa fa |
|---|---|
| Nuovo progetto | svuota il progetto |
| Apri… | apre un `.hvsrnx` o un `.hvsrx` |
| Salva (Ctrl+S) | riscrive il file aperto; se non c'è, chiede dove salvare |
| Salva con nome… (Ctrl+Shift+S) | salva in un nuovo file `.hvsrnx` |
| Apri l'esempio | carica il progetto dimostrativo |
| Esporta in CSV | **Curva H/V**, **Spettri medi**, **Tracce**: vedi [Relazione](relazione.md) |

Se il progetto ha modifiche che non stanno in un file, prima di **Nuovo progetto**, **Apri…** o **Apri l'esempio** una striscia chiede **Salva prima**, **Continua senza salvare**
o **Annulla**.

## Salvare

Il progetto vive in sessione sul server e **sparisce dopo 30 minuti di inattività o a un riavvio**. Salvalo dal menu **File**: ottieni un file
`.hvsrnx` con dati, finestre, parametri, modelli e tracce. Oltre i 30 MB le tracce restano riferimenti e il salvataggio lo dice.

## Aprire

| Formato | Che cos'è | In HVSR NX |
|---|---|---|
| `.hvsrnx` | progetto di HVSR NX | apri e salvi |
| `.hvsrx` | progetto di Easy HVSR desktop | apri, da **File → Apri…** o dal riquadro della scheda **Tracce** |
| `.ehv` | vecchio formato binario del desktop | non si apre: salvalo come `.hvsrx` dal desktop |

Da un `.hvsrx` arrivano tracce, finestre con la loro selezione, parametri e modelli. **Curve e verifiche si ricalcolano**: i progetti del 2011-2015
possono contenere curve diverse da quelle che escono oggi dagli stessi dati, e il riferimento è il ricalcolo. Nei progetti vecchi le finestre possono
durare 32 s e non essere contigue.

## Tracce

| Formato | Note |
|---|---|
| `.saf` | righe `CHIAVE = valore`, poi 3 colonne. Ordine V, N, E. Se il file ha una lettura non numerica l'app si ferma e te lo dice |
| `.txt`, `.asc`, `.csv`, `.dat` | testo: indichi riga, colonna, separatore e F~s~ |
| `.sg2`, `.seg2`, `.dat` | SEG-2 con almeno 3 tracce, che assegni alle componenti. `DESCALING_FACTOR` non si applica, ininfluente sul rapporto H/V |

Altri formati di strumento non si leggono: esporta da lì in SAF o in testo.

## GeoDropbox

Dal pulsante **GeoDropbox** in alto salvi il `.hvsrnx` in un tuo progetto e apri da lì un `.hvsrnx` o un `.hvsrx`.

## Limiti

File fino a 64 MB per volta. Più campioni di quanti il server possa elaborare vengono rifiutati con un messaggio.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20HVSR%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/hvsr/docs/it/file.md).*
