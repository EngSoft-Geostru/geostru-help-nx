# File, progetti del desktop e GeoDropbox

Mentre lavori il progetto vive **sul server, nella tua sessione**. La copia che resta a te
è il file **`.dhnx`**: salvalo prima di uscire.

## Il menu File

| Voce | Che cosa fa |
|---|---|
| **Nuovo progetto** | Svuota il progetto in sessione. |
| **Apri…** | Apre un file `.dhnx`, oppure un `.dwhx` / `.dwh` del programma desktop. |
| **Salva** (Ctrl+S) | Riscrive il file aperto o salvato per ultimo; se non ce n'è uno, fa come **Salva con nome**. |
| **Salva con nome…** (Ctrl+Maiusc+S) | Salva il progetto in un nuovo file `.dhnx`. |
| **Apri l'esempio** | Carica il progetto di esempio del desktop: 30 ricezioni, 5 sismostrati. |

Nuovo, Apri ed esempio **sostituiscono** il progetto in sessione. Se c'è qualcosa da
perdere, una striscia sotto la barra chiede conferma: ciò che non hai salvato in un file
andrà perso.

![Menu File aperto: Nuovo progetto, Apri con le estensioni .dhnx .dwhx .dwh, Salva con Ctrl+S, Salva con nome con Ctrl+Shift+S e Apri l'esempio](img/02-menu-file.png)

### Salva e Salva con nome

Nei browser che permettono a una pagina di scrivere un file scelto dall'utente (Chrome,
Edge):

- **Salva con nome…** apre la finestra del sistema con il nome proposto dall'app (il
  cantiere, o il committente) e scrive il file dove scegli;
- da quel momento il nome del file compare nella barra in alto, accanto al menu **File**:
  è il file su cui scrive **Salva**;
- **Salva** lo riscrive senza chiedere nulla. La prima volta dopo una riapertura il browser
  può chiedere il permesso di modificare il file;
- **Apri…** di un `.dhnx` fa la stessa cosa: il file aperto diventa quello di **Salva**.

Dopo il salvataggio una striscia conferma *«Progetto salvato in …»*.

Negli altri browser **Salva** e **Salva con nome…** scaricano il file nella cartella dei
download.

Il file resta legato al **progetto** che hai aperto: se crei un progetto nuovo, apri
l'esempio o la sessione scade, il nome sparisce dalla barra e **Salva** chiede di nuovo dove
salvare. Così un progetto vuoto non sovrascrive mai il file buono.

Un `.dwhx` / `.dwh` del desktop aperto qui non diventa il file di **Salva**: il primo
salvataggio chiede il nome del nuovo `.dhnx`.

## Il file .dhnx

Il file `.dhnx` contiene tutto il progetto:

- dati generali, geometria e tabella delle misure;
- opzioni (metodo, peso di volume, profondità della V~s,eq~);
- sismostrati dei due metodi e stratigrafia;
- le righe della scheda Tracce, i **tempi scelti** e le opzioni della vista;
- le sezioni scelte per la relazione;
- le **tracce**, entro il limite descritto sotto.

I risultati non sono nel file: si ricalcolano all'apertura, sempre con la versione corrente
del programma.

Prima di salvare, l'app registra la scheda che hai a video: nel file c'è anche l'ultima
modifica.

### Le tracce nel file

Le tracce viaggiano dentro il `.dhnx` finché non superano, tutte insieme, i **30 MB**.

Oltre quel limite il file porta solo i **riferimenti** alle tracce: righe, profondità e
tempi scelti ci sono, le registrazioni no. L'app te lo dice due volte: nella scheda Tracce,
appena il rilievo supera il limite, e al momento del salvataggio.

Riaprendo un file così, la scheda Tracce elenca i file da ricaricare. **Trascina di nuovo
gli stessi file**: si ricollegano alle loro righe, senza crearne di nuove, e i tempi scelti
sono ancora al loro posto.

!!! tip "Tieni i file originali"
    Conserva sempre i file di acquisizione originali insieme al `.dhnx`: sono la sola copia
    sicura delle tracce quando il rilievo è grande.

Un file `.dhnx` si apre fino a 40 MB.

## I progetti di esempio

Due esempi si scaricano dal pulsante **?**, scheda **Risorse**, voce **Progetto di
esempio**:

| File | Che cosa contiene |
|---|---|
| `ExDefault.dhnx` | L'esempio del programma desktop: 30 ricezioni a passo 1 m, offset 2,6 m, cinque sismostrati. Senza tracce. È lo stesso progetto di **File → Apri l'esempio**. |
| `ex-tracce-seg2.dhnx` | Una prova reale con le **tracce SEG-2** dentro: 31 file a tre canali, uno per profondità da 1 a 31 m, offset 1,5 m, tempi già scelti e sismostrati dei due metodi. Serve a provare la scheda Tracce. |

Scarica il file e aprilo con **File → Apri…**.

![Aiuto di Downhole NX, scheda Risorse: le funzionalità, i due progetti di esempio da scaricare, crediti e sessione, risorse online](img/35-aiuto-risorse.png)

## Aprire un progetto del desktop

**File → Apri…** legge anche i progetti del programma desktop Downhole: `.dwhx` e `.dwh`,
fino a 2 MB. Il progetto viene convertito; il file originale non viene modificato, e l'app
non scrive file del desktop.

**Che cosa viene importato**

- geometria della prova e tabella delle misure (profondità, T~p~, T~s~);
- peso di volume automatico o assegnato, con i valori di γ per misura;
- sismostrati del metodo diretto e del metodo intervallo: base, litologia, descrizione,
  colore;
- stratigrafia e profondità della falda;
- dati generali: committente, cantiere, località, data, operatore, responsabile,
  descrizione, note, coordinate.

**Che cosa non viene importato**

| Non importato | Che cosa succede |
|---|---|
| Retini fatti con un file immagine | Erano percorsi sul disco di chi ha creato il progetto. Resta il retino della litologia. |
| Logo | Aggiungilo nel documento Word. |
| Colori dei grafici, impostazioni del DXF, margini e altezze dei testi, posizioni delle legende | Sono impostazioni del programma desktop, non della prova. |
| Dati anagrafici dello studio | Non sono usati. |
| Risultati salvati (intercette, pesi di volume) | Si ricalcolano. |
| Tracce e file di acquisizione del desktop (`.dsgx`) | Ricarica i file SEG-2 o di testo nella scheda [Tracce](tracce.md). |

Dopo l'apertura, strisce azzurre in alto elencano ciò che non è entrato o è stato corretto.
La più frequente: *«La base del sismostrato … (30,11 m) era oltre l'ultima misura ed è stata
riportata a 30 m»*. Il desktop poneva la base dell'ultimo strato alla distanza inclinata
dell'ultima ricezione; Downhole NX la riporta alla sua profondità.

!!! note "I numeri possono differire da quelli del desktop"
    Sullo stesso file alcuni risultati cambiano, perché Downhole NX corregge alcuni difetti
    del programma desktop. Ragione ed effetto di ogni differenza sono in
    [Validazione e differenze dal desktop](validazione.md#differenze-dal-programma-desktop).

## GeoDropbox

Il pulsante **GeoDropbox**, nella barra in alto, apre i tuoi progetti nel cloud GeoStru:

- **salva** il progetto corrente come `.dhnx` in un progetto GeoDropbox;
- **apre** un `.dhnx`, o un `.dwhx` / `.dwh` del desktop, salvato lì.

Così ritrovi il lavoro da qualunque postazione e lo condividi con lo studio. Come per
**Salva**, l'app registra prima la scheda a video. GeoDropbox è un servizio separato dai
crediti delle app.

## La sessione

Il progetto resta in sessione finché lavori. **Dopo 30 minuti di inattività la sessione
scade** e il progetto non è più in memoria; lo stesso succede quando il servizio viene
aggiornato.

A sessione scaduta l'app non lavora su un progetto vuoto: dice *«La sessione è scaduta e il
progetto non è più in memoria: riapri il file salvato. Non è stato scritto né addebitato
nulla»*. Riapri il tuo `.dhnx` e prosegui.

Due abitudini evitano di perdere lavoro:

- **salva** (Ctrl+S, o su GeoDropbox) ogni volta che hai finito un passaggio: i tempi
  scelti, i sismostrati;
- lavora sullo stesso progetto in **una sola scheda del browser**. Se il progetto cambia
  altrove, l'app lo segnala e non salva ciò che avevi a video: ricarica la pagina.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Downhole%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/downhole/docs/it/file.md).*
