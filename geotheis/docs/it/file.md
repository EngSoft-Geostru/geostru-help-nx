# File, progetti del desktop e GeoDropbox

## Il progetto vive in sessione

Il progetto su cui lavori sta sul server, nella tua sessione, e scade dopo **30 minuti di inattività**. Finché la scheda del browser
resta aperta la sessione resta viva. Se la chiudi, o la lasci ferma oltre il limite, il progetto non è più in memoria: compare *La
sessione è scaduta e il progetto non è più in memoria: riapri il file salvato. Non è stato scritto né addebitato nulla.*

Per non perdere il lavoro salvalo in un file `.geotheisnx` o su GeoDropbox.

## Il menu File

| Comando | Che cosa fa |
|---|---|
| **Nuovo progetto** | svuota il progetto; se ci sono modifiche che non sono in un file te lo chiede prima |
| **Apri…** | apre un file `.geotheisnx` di GeoTheis NX oppure un `.wtax` del programma desktop |
| *Esempi* | apre un progetto d'esempio (vedi sotto) |
| **Salva** (Ctrl+S) | riscrive il file aperto; se non c'è, chiede dove salvare |
| **Salva con nome…** (Ctrl+Shift+S) | salva il progetto in un nuovo file `.geotheisnx` |

Accanto al menu compare il nome del file su cui scrive **Salva**. Se il browser non ti lascia riscrivere quel file compare *Il browser
non ha concesso di scrivere sul file: usa «Salva con nome».*

## Il file `.geotheisnx`

È un file di testo JSON, in unità SI, che contiene **solo i dati d'ingresso** e le tue scelte: pozzo, sito, stratigrafia,
completamento, piezometri, letture delle prove, punti esclusi, intervalli di Cooper-Jacob, ritocchi delle curve tipo, portata
critica scelta, valori confermati. I risultati non sono nel file: si ricalcolano all'apertura, quindi un file vecchio aperto con una
versione nuova del motore dà i risultati della versione nuova.

Un file di progetto si apre fino a 8 MB.

## Progetti del programma desktop (`.wtax`)

**Apri…** accetta anche i progetti `.wtax` di GeoTheis desktop. Dopo l'apertura compare *Progetto del programma desktop aperto:
controlla i dati prima di calcolare.*, con le note dell'importazione.

Che cosa si importa:

- tipo di pozzo e di falda, quote (piano campagna, bocca, livello statico, tetto e substrato, semipermeabile), raggio e geometria del
  pozzo; il completamento si propone dallo schema di calcolo;
- descrizione del disegno (diventa la descrizione del progetto) e opzioni della vista;
- stratigrafia, con il nome del terreno ricondotto al catalogo;
- piezometri, chiamati P1, P2… nell'ordine del desktop;
- gradini di portata, letture di pompaggio e di risalita, abbassamenti stabilizzati;
- le scelte fatte nel desktop: portata critica, portata di riferimento dell'efficienza, metodo e raggio presunto dei pozzi singoli,
  raggio presunto di Dupuit-Thiem, punti di coincidenza di Theis e Hantush.

Le portate in m³/h e i tempi in ore, minuti e secondi si convertono in unità SI. Gli zeri che nel desktop volevano dire «non dato»
(coordinate 0, 0; abbassamenti stabilizzati, Q~c~, raggi presunti a zero) diventano campi vuoti.

!!! warning "Attenzione"
    **I risultati salvati nel `.wtax` non si importano**: GeoTheis NX ricalcola tutto con le formule corrette di letteratura. Per
    questo i numeri possono differire da quelli che leggevi nel desktop. Le differenze e i loro motivi sono in
    [Validazione](validazione.md).

Note che puoi trovare dopo l'apertura:

- *Il file non indica il tipo di pozzo e di falda: vanno scelti prima del calcolo.* Sceglili nella scheda [Pozzo](pozzo.md).
- La falda «semilibera» o «semiartesiana» del desktop diventa *semiconfinata (libera)* o *semiconfinata (in pressione)*.
- **Risalita**: se i tempi del file contavano dall'inizio del pompaggio, vengono riportati all'arresto della pompa; se manca
  l'istante d'arresto si assume l'ultima lettura di pompaggio. La nota dice quale regola è stata applicata.
- Abbassamenti in colonne senza piezometro (piezometri tolti nel desktop) non importati; righe vuote ignorate.
- Strati con un retino preso da un'immagine sul PC dell'autore: nel disegno si usa il retino standard del terreno. Litologie non
  riconosciute: retino generico, da correggere nella stratigrafia.
- *Prova a portata costante: le letture ci sono ma la portata è 0: va inserita.*

Limiti dell'importazione:

- le coordinate del desktop sono **coordinate locali**, non geografiche: dopo l'apertura posiziona il pozzo sulla mappa nella scheda
  [Pozzo](pozzo.md) se ti servono mappa, pozzi vicini e scheda per l'istanza;
- gli abbassamenti stabilizzati del desktop esistono solo per il pozzo e per i primi due piezometri;
- un file che non è un `.wtax` valido, o è troncato, non si apre e il progetto in sessione resta com'era;
- il file da aprire non può superare 32 MB (un `.wtax` reale pesa pochi kB).

## GeoDropbox

Il pulsante **GeoDropbox** nella barra in alto salva il progetto (il `.geotheisnx`) in un tuo progetto GeoDropbox, oppure apre un
`.geotheisnx` o un `.wtax` salvato lì.

Dalla scheda [Relazione](relazione.md), **Invia a GeoDropbox** fa un passo in più: crea su GeoDropbox un progetto con il pin sul
pozzo, il comune e i dati generali, oppure usa uno dei tuoi progetti entro 500 m dal pozzo. Il file `.geotheisnx` va nella cartella
«GeoTheis NX» e si riapre dal pulsante GeoDropbox → Apri. Un secondo invio aggiorna lo stesso progetto (**Aggiorna su GeoDropbox**).
Se il pozzo non ha coordinate il progetto nasce senza pin.

Salvare o inviare a GeoDropbox è gratuito; costa solo la relazione Word, se scegli di allegarla.

## Esempi

Dal menu **File** apri i progetti d'esempio del programma desktop. Si aprono come un `.wtax`, con le stesse note dell'importazione.

- **Esempi con prove**: progetti con gradini o prova a portata costante. Il primo è **CELICO**, un pozzo completo in falda confinata
  con gradini, prova a portata costante, risalita, due piezometri e abbassamenti stabilizzati (vedi l'esempio in
  [Risultati](risultati.md#esempio)).
- **Pozzi singoli (portata critica nota)**: otto esempi con la sola geometria del pozzo, completo o incompleto, nei diversi tipi di
  falda. Aperti dal menu ricevono nei campi vuoti i valori d'esempio del desktop: Q~c~ 100 m³/h, s~c~ 5 m, R 150 m, nella scheda
  [Prova](prove.md), dove puoi cambiarli.

!!! note "Nota"
    I dati degli esempi sono costruiti per provare il calcolo, non descrivono un acquifero reale. Ad esempio in CELICO le letture di
    P2 sono quelle di P1 moltiplicate per 0,4.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20GeoTheis%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/geotheis/docs/it/file.md).*
