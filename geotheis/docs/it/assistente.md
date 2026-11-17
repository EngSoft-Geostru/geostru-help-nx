# Assistente AI

Il pulsante **Assistente** nella barra in alto apre la chat. L'assistente è un sistema di intelligenza artificiale che lavora sul
progetto aperto: legge dati e risultati, ti spiega metodi e limiti, e su tua richiesta scrive dati nelle schede o applica scelte
sui risultati. Se glielo chiedi, ti dice che è un'intelligenza artificiale.

## Che cosa sa fare

**Leggere e spiegare** (non cambia il progetto):

- leggere il progetto: dati generali, sito, falda e quote, pozzo, stratigrafia, piezometri, prove e letture;
- leggere i risultati del motore: metodi applicati e non applicabili con il motivo, valori con affidabilità e avvisi, confronto,
  valori di progetto proposti e portata concedibile;
- spiegare un metodo nel dettaglio: parametri con l'intervallo al 95 %, valori per serie, per Cooper-Jacob l'intervallo usato e u
  massimo;
- dirti, per ogni serie di Cooper-Jacob, quale tratto è in uso e perché;
- cercare i pozzi censiti nell'archivio ISPRA (L. 464/84) intorno al pozzo georeferenziato;
- consultare questo manuale per rispondere su comandi, avvisi e messaggi.

**Scrivere i dati**, quando glielo chiedi:

- dati del lavoro, tipo di falda e di pozzo, quote e geometria;
- stratigrafia, completamento (perforazione, colonna, intercapedine, avampozzo, pompa, livelli) e piezometri;
- letture della prova a gradini, del pompaggio e della risalita, anche **incollate in chat** da Excel, CSV o datalogger: le legge con lo
  stesso importatore della scheda Prova e ti riassume come ha interpretato tempi, unità e colonne;
- la **portata critica nota** (Q~c~, s~c~ e R presunto), solo se gli dai tu i valori;
- la posizione del pozzo da coordinate in WGS84, UTM o Gauss-Boaga (e gli altri sistemi della scheda Pozzo).

Puoi anche allegare un documento con la graffetta della chat (rapporto di prova, letture di campo, stratigrafia, schema di
completamento): l'assistente scrive nel progetto i dati che trova, senza completare quelli che mancano.

**Scelte sui risultati**: intervallo di Cooper-Jacob, esclusione o ripristino di punti, ritocco della curva tipo di Theis o Hantush,
conferma dei valori di progetto (la proposta, quelli di un metodo, o valori che indichi tu) e della portata. Sono le stesse scelte che
fai a mano nella scheda [Risultati](risultati.md).

## Propone, tu decidi

- **Le scelte sui risultati sono proposte.** L'assistente prima ti mostra l'effetto calcolato dal motore (per esempio la T che si
  otterrebbe con un altro intervallo) e la applica al progetto solo se gli chiedi esplicitamente di farlo.
- **I dati li scrive quando glieli chiedi**, senza una conferma in più: dopo, ti riassume che cosa ha scritto e dove. Controlla sempre le
  schede.
- **I numeri li calcola il motore.** L'assistente li legge e li cita con l'unità, il metodo da cui vengono e l'affidabilità; non li
  stima e non fa conti per conto suo.
- **Non cancella nulla.** Strati, completamento e letture si aggiungono; li sostituisce solo se lo chiedi esplicitamente. I piezometri
  si aggiungono o si correggono, mai si tolgono: per toglierne uno usa la scheda Pozzo. Escludere un punto non elimina la lettura.
- **Non genera la relazione Word né il DXF**: li scarichi tu dalla scheda [Relazione](relazione.md).

Dopo una modifica dell'assistente la pagina si aggiorna da sola. Mentre lavora il progetto è suo: se provi a cambiare qualcosa compare
*L'assistente sta lavorando sul progetto: attendi che abbia finito e riprova. Nulla è stato modificato.*

!!! tip "Suggerimento"
    Le azioni rapide della chat sono un buon inizio: **Spiegami i risultati**, **Il tratto di Cooper-Jacob va bene?**, **Theis o
    Hantush: quale scegliere?**, **Ci sono pozzi censiti vicini?**

## Costo e limiti

- Ogni messaggio all'assistente costa **3 crediti NX**.
- Un messaggio che finisce in errore, o che non produce risposta, **non si paga**. Ciò che l'assistente aveva già scritto nel progetto
  prima dell'errore resta.
- Rimandare lo stesso messaggio sullo stesso progetto dopo un errore è un nuovo tentativo; se nel frattempo il progetto è cambiato è un
  lavoro nuovo.
- Un messaggio può essere lungo al massimo 20 000 caratteri, file allegato compreso.
- In un messaggio l'assistente fa un numero limitato di operazioni. Se lo raggiunge te lo dice: ciò che ha fatto è nel progetto,
  scrivigli per proseguire.
- Se la sessione è scaduta, o se un altro messaggio è ancora in corso, il messaggio non parte e non si paga.
- C'è un limite mensile di utilizzo per applicazione: raggiunto quello, il messaggio non viene addebitato.

## Assistenza

Dalla chat puoi aprire un ticket di supporto (azione rapida **Apri un ticket di supporto**): finché il ticket è aperto i tuoi messaggi
vanno all'operatore, non all'assistente.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20GeoTheis%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/geotheis/docs/it/assistente.md).*
