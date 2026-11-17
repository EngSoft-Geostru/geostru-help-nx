# GeoTheis NX

**GeoTheis NX** interpreta le **prove di emungimento** sui pozzi per acqua: la prova a gradini di portata e la prova a portata
costante con la risalita, misurate nel pozzo e nei piezometri. Dai dati ricava i parametri dell'acquifero, trasmissività (T),
permeabilità (K), coefficiente di immagazzinamento (S) e raggio d'azione (R), propone la **portata concedibile** e scrive la
relazione Word.

Mentre descrivi il pozzo, la sezione si disegna dal vivo accanto ai campi: stratigrafia, colonna, filtri, livelli e cono di
depressione.

[**Apri GeoTheis NX**](https://nx.geostru.ai/geotheis/){ .md-button .md-button--primary }

## Che cosa fa

1. **Posiziona il pozzo** sulla mappa, con le coordinate in WGS84, UTM (WGS84, ETRS89, RDN2008, ED50) e Gauss-Boaga, la quota del
   terreno dal modello digitale e i pozzi censiti ISPRA nei dintorni.
2. **Descrive il pozzo**: stratigrafia, tipo di falda, quote dell'acquifero, schema di calcolo, completamento (perforazione,
   colonna con filtri, intercapedine, avampozzo, pompa) e piezometri.
3. **Raccoglie le prove**: gradini di portata e prova a portata costante con risalita, anche incollate da un foglio di calcolo.
4. **Calcola tutti i metodi** che i dati consentono: curva caratteristica e Rorabaugh sui gradini, Theis, Cooper-Jacob, risalita,
   Hantush, Dupuit-Thiem, distanza-abbassamento, pozzi singoli. Li confronta e propone il **valore di progetto**, con la
   motivazione.
5. **Produce la relazione** Word con dati, metodi, grafici, confronto e portata concedibile, e la sezione del pozzo in DXF.

Il calcolo si aggiorna da solo a ogni modifica: non c'è un pulsante «Calcola». Il programma usa le formule di letteratura; dove
il programma desktop GeoTheis aveva formule diverse, l'app segue la letteratura. Le differenze sono elencate in
[Validazione](validazione.md).

## A chi serve

Ai geologi e agli ingegneri che eseguono o interpretano prove di pozzo: collaudo di un pozzo nuovo, verifica della portata
emungibile, istanza di concessione di derivazione, studio idrogeologico di un acquifero.

## Le quattro schede

Il lavoro segue quattro schede in fila. In fondo a ogni scheda il pulsante con il nome della scheda successiva ti porta avanti.

| Scheda | Sotto il nome | Che cosa fai |
|---|---|---|
| 1. [**Pozzo**](pozzo.md) | Sito, stratigrafia, completamento, piezometri | posizione, terreni, falda, quote, geometria del pozzo, piezometri; a destra la sezione del pozzo dal vivo |
| 2. [**Prova**](prove.md) | Gradini, portata costante e risalita | letture della prova a gradini e della prova a portata costante; in alternativa la portata critica nota |
| 3. [**Risultati**](risultati.md) | Metodi applicabili e confronto | metodi calcolati, confronto, valore di progetto, portata concedibile, scelte sui grafici |
| 4. [**Relazione**](relazione.md) | Anteprima, Word e DXF | anteprima gratuita, Word e DXF a crediti, invio alle altre app NX |

In testa alla pagina c'è il **Nome del progetto**: dà il nome al file e alla relazione.

## Che cosa è gratuito e che cosa consuma crediti

Inserire i dati, calcolare, vedere grafici, disegni e mappa è **gratuito**. Consumano crediti NX solo tre azioni:

| Azione | Crediti |
|---|---|
| Relazione Word (**Genera Word**) | 10 |
| Sezione del pozzo in DXF (**DXF**, **DXF del pozzo**, oppure **Apri in CAD Tools**) | 10 |
| Un messaggio all'**Assistente** | 3 |

Le tariffe sono quelle in vigore al momento della stesura e possono cambiare.

- Un'operazione **fallita non si paga**: se il Word o il DXF non si compone, il messaggio lo dice e nessun credito è addebitato.
- **Rigenerare lo stesso Word** (stessi dati, stessa lingua) non si ripaga; lo stesso vale per un DXF già scaricato.
- Se il saldo non copre il costo compare *Crediti insufficienti per: …* con il saldo e il pulsante **Acquista crediti**. Il progetto
  resta in sessione: ricarica il saldo e riprova.

## Sessione e salvataggio

Il progetto vive **in sessione sul server**. Ogni campo si salva da solo nella sessione mentre scrivi, ma la sessione scade dopo
**30 minuti di inattività**: per conservare il lavoro salvalo in un file `.geotheisnx` (menu **File** → **Salva** o **Salva con
nome…**) oppure su **GeoDropbox**. Con **File** → **Apri…** riapri un file `.geotheisnx` o un progetto `.wtax` del programma
desktop. Dettagli in [File e GeoDropbox](file.md).

!!! warning "Attenzione"
    *Salvato* accanto al titolo di un riquadro vuol dire salvato nella sessione, non in un file. Se la sessione scade, i dati
    non salvati in un file si perdono.

## Mappa del manuale

| Capitolo | Contenuto |
|---|---|
| [Guida rapida](quickstart.md) | dall'esempio CELICO ai risultati e all'anteprima della relazione, in 5 minuti |
| [Flusso di lavoro](workflow.md) | un progetto reale, dall'inizio alla relazione, con tutte le opzioni |
| [Pozzo](pozzo.md) | sito e coordinate, stratigrafia, falda e quote, schema di calcolo, completamento, piezometri, sezione |
| [Prove](prove.md) | prova a gradini, portata costante e risalita, incolla da Excel, portata critica nota |
| [Metodi](metodi.md) | i metodi d'interpretazione, i dati che richiedono, le loro ipotesi |
| [Risultati](risultati.md) | la scheda Risultati: valore di progetto, portata concedibile, confronto, scelte sui grafici |
| [Relazione](relazione.md) | anteprima, Word, DXF, collegamenti con le altre app NX |
| [File e GeoDropbox](file.md) | salvare, aprire, importare i `.wtax` del desktop |
| [Assistente](assistente.md) | che cosa può fare l'assistente AI e quanto costa |
| [Cenni teorici](teoria.md) | formule e bibliografia |
| [Glossario](glossario.md) | i termini della prova di pozzo |
| [Validazione](validazione.md) | casi di prova, confronti con il desktop, limiti |
| [Domande frequenti](faq.md) | i dubbi più comuni |

Inizia dalla [Guida rapida](quickstart.md).

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20GeoTheis%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/geotheis/docs/it/index.md).*
