# Relazione, DXF e crediti

La scheda **Relazione** raccoglie il lavoro in un documento Word e nel disegno DXF del pozzo. A sinistra trovi che cosa entra nella
relazione e i pulsanti per scaricarla; a destra l'**Anteprima**, gratuita. Sotto i pulsanti c'è il pannello **Prosegui con le altre
app NX** (GeoDropbox, CAD Tools, Atlante).

## Che cosa entra nella relazione

L'elenco **Che cosa entra nella relazione** ti dice, voce per voce, se il progetto ha i dati per quel capitolo:

| Con i dati | Senza |
|---|---|
| Posizione del pozzo: mappa, coordinate in tutti i sistemi, pozzi entro 500 m | Posizione del pozzo non indicata: niente mappa, coordinate e pozzi vicini |
| Stratigrafia e disegno del pozzo | Stratigrafia non inserita |
| Prova a gradini: curva caratteristica e portata critica | Nessuna prova a gradini: portata critica non calcolabile |
| Prova a portata costante: T, S e R con i metodi transitori | Nessuna prova a portata costante |
| Piezometri: S e raggio d'azione dai dati | Nessun piezometro: S non si ricava dai dati |

Una voce mancante non blocca il documento: il capitolo si salta o dice che cosa manca. Serve almeno un dato: la posizione o i dati
del pozzo, la stratigrafia o una prova. Con il progetto vuoto il pulsante resta spento e compare il messaggio *Il progetto è vuoto:
inserisci almeno la posizione o i dati del pozzo, la stratigrafia o una prova prima di generare la relazione.*

## Anteprima

L'anteprima è composta dal server con lo stesso codice del Word, sugli stessi numeri della scheda [Risultati](risultati.md): quello che
leggi è il testo che scaricherai. L'impaginazione è indicativa (*Impaginazione indicativa: il Word ha la sua.*). Il pulsante
**Aggiorna l'anteprima** la ricompone dopo una modifica. Il blocco «Codice di calcolo» c'è solo nel Word.

## Il documento Word

**Genera Word** scarica la relazione `.docx` nella lingua dell'interfaccia (italiano o inglese). Nel documento inglese i testi scritti
dal motore di calcolo (nomi dei metodi, motivazioni, avvisi) restano in italiano, e la copertina lo dichiara.

I capitoli, nell'ordine:

1. **Copertina** con il titolo *Relazione sulla prova di emungimento*, il nome del progetto, committente, opera, località, data della
   prova e tecnico; poi l'**Indice**.
2. **Dati generali**: progetto, descrizione, committente, opera, località, data della prova, esecutore, tecnico, note, e lo scopo
   della relazione.
3. **Ubicazione del pozzo**: estratto di mappa con il pozzo, i piezometri, i pozzi censiti, il cerchio dei 500 m e quello del raggio
   d'azione di progetto; le coordinate nel sistema in cui le hai inserite e negli altri, con la trasformazione di datum usata; la
   quota del terreno dal modello digitale (TINITALY, INGV) accanto alla quota del piano campagna.
4. **Pozzi preesistenti entro 500 m** dall'archivio nazionale delle indagini nel sottosuolo (L. 464/84), con codice, profondità,
   distanza e azimut. L'archivio è incompleto: «nessun pozzo censito» non vuol dire «nessun pozzo», e la relazione lo scrive.
5. **Pozzo, acquifero e stratigrafia**: dati del pozzo, tipo di falda e quote, spessore saturo H~1~ o spessore dell'acquifero b,
   livelli misurati, stratigrafia, completamento (perforazione, colonna, intercapedine, avampozzo, pompa), piezometri e la figura
   della sezione del pozzo con il cono di depressione.
6. **Dati della prova**: tabelle dei gradini di portata, della prova a portata costante (portata, durata, arresto della pompa), delle
   letture di pompaggio e di risalita e degli abbassamenti stabilizzati. Se hai indicato la portata critica nota, qui compare con la
   nota che Q~c~ e s~c~ non vengono da una prova a gradini.
7. **Elaborazione della prova**: la sintesi, poi un paragrafo per ogni metodo calcolato con riferimento bibliografico, formule,
   affidabilità, parametri (con l'intervallo al 95 % dove c'è), valori per serie e grafici; in fondo i **Metodi non applicati** con il
   motivo.
8. **Confronto fra i metodi**: T, K, S e R di ogni metodo, gli scarti oltre soglia e il metodo di riferimento.
9. **Valori di progetto e portata concedibile**: valori proposti con la motivazione, eventuali valori confermati dal tecnico,
   portata critica, portata ottimale, portata massima provata, portata concedibile, abbassamento previsto e la portata con cui è
   disegnato il cono.
10. **Scheda per l'istanza di concessione**: coordinate, pozzi entro 500 m, tipo di pozzo, diametri, tratti filtranti, livello
    statico, portata critica e portata richiesta, con un estratto di mappa. È pensata per la relazione idrogeologica dell'istanza.
11. **Bibliografia**: solo le fonti dei metodi calcolati, più il testo di riferimento generale (Kruseman & de Ridder).
12. **Codice di calcolo (NTC 2018 §10.2)**: titolo e produttore del software, versione dell'app e del motore di calcolo, licenza
    d'uso intestata al tuo account GeoStru NX, **codice documento**, indirizzo di **verifica** su geostru.ai, riferimento al
    documento di validazione del motore e impronta dei dati d'ingresso.

!!! note "Nota"
    La relazione riporta i valori che il programma propone e quelli che hai confermato nella scheda Risultati. Una frase chiude il
    capitolo dei valori di progetto: la scelta dei valori e della portata da richiedere resta del professionista.

Con il codice documento chiunque riceva la relazione può verificare su geostru.ai che il documento è stato emesso da GeoTheis NX con
quei dati.

## DXF del pozzo

**DXF del pozzo** scarica la sezione del pozzo in DXF, in metri, con le distanze in scala lineare. Ogni elemento sta sul suo layer:
STRATI, POZZO, FALDA, CONO, PIEZOMETRI, QUOTE, TESTI, TERRENO. Il pulsante si accende quando c'è qualcosa da disegnare
(profondità, perforazione, stratigrafia o filtro).

Lo stesso DXF si scarica dal pulsante **DXF** sopra la sezione del pozzo, nella scheda Pozzo, dove puoi prima regolare portata e tempo
del cono. Il **PNG** della sezione è gratuito.

## Prosegui con le altre app NX

- **GeoDropbox** → **Invia a GeoDropbox**: crea un progetto con il pin sul pozzo, o usa uno dei tuoi progetti entro 500 m, e ci carica
  il file `.geotheisnx` nella cartella «GeoTheis NX». Puoi spuntare **Allega anche la relazione Word**: è a crediti come il download,
  e un Word già pagato non si ripaga. Vedi [File e GeoDropbox](file.md).
- **CAD Tools** → **Apri in CAD Tools**: apre la sezione del pozzo in CAD Tools per completarla o impaginarla. Si paga come il DXF; un
  DXF già scaricato non si ripaga.
- **Atlante** → **Fascicolo del sito con Atlante**: il fascicolo del sito (geologia, frane, alluvioni, sismicità) sul punto del pozzo.

## Crediti

Dati, calcolo, risultati, grafici, disegni a video, mappa e anteprima sono gratuiti. Consumano crediti NX solo tre azioni:

| Azione | Crediti |
|---|---|
| Relazione Word (**Genera Word**, o allegata all'invio a GeoDropbox) | 10 |
| DXF del pozzo (download o **Apri in CAD Tools**) | 10 |
| Messaggio all'assistente AI | 3 |

- **Un'operazione fallita non si paga.** Se il Word non si compone, se il registro dei documenti non risponde o se il file risulta
  vuoto, nessun credito viene addebitato e il messaggio lo dice.
- **Rigenerare lo stesso documento non si ripaga**: stessi dati, stessa lingua e stessa versione del motore danno lo stesso Word, che
  esce senza addebito. Se cambi un dato o la lingua, è un documento nuovo.
- Lo stesso vale per il DXF: un disegno identico a uno già pagato non si ripaga, anche se lo apri in CAD Tools.
- Con il saldo insufficiente compare la finestra *Crediti insufficienti per: …* con i crediti che servono e il saldo; il progetto resta
  in sessione mentre ricarichi.

!!! tip "Suggerimento"
    Controlla tutto nell'anteprima, che è gratuita, e genera il Word solo alla fine. Se dopo il download ti accorgi di un errore,
    correggilo: il Word nuovo è un documento diverso e consuma crediti di nuovo.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20GeoTheis%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/geotheis/docs/it/relazione.md).*
