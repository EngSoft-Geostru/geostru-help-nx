# Domande frequenti

## Tracce e formati

**Quali file di tracce posso caricare?**
SEG-2 (`.sg2`, `.seg2`, `.dat`) e file di testo con le tracce in colonna (`.txt`, `.csv`).
Ogni file fino a 20 MB. Vedi [Tracce e scelta dei tempi](tracce.md#caricare-i-file).

**Il mio formato non è fra quelli. Che cosa faccio?**
Downhole NX non legge SEG-Y né i formati proprietari degli strumenti di acquisizione. Due
strade: esporta le tracce dal software dello strumento in SEG-2 o in testo, oppure leggi i
tempi altrove e inseriscili nella scheda [Misure](misure.md). L'elaborazione parte dai
tempi: le tracce non sono obbligatorie.

**Un file SEG-2 è rifiutato con «Formato dei dati SEG-2 non supportato».**
L'app legge i campioni SEG-2 a interi di 16 e 32 bit e in virgola mobile a 32 e 64 bit. La
codifica in virgola mobile a 20 bit non è letta: esporta il file in un'altra codifica.

**I file della battuta P e della battuta S hanno un numero diverso di canali.**
L'app avvisa e non li assembla: i canali si leggono per numero. Controlla **Canale onda P**
e **Canali per geofono**, o riesporta i file con lo stesso numero di canali.

**Ho un rilievo grande. Ci sono limiti?**
Un progetto tiene fino a 600 file, 400 righe di profondità e 64 canali. I file si caricano
a lotti: se il server respinge un caricamento perché troppo grande, carica meno file alla
volta. Nel file `.dhnx` le tracce entrano fino a 30 MB in tutto; oltre, il file porta i
riferimenti e le tracce si ricaricano alla riapertura. Tieni sempre i file originali. Vedi
[File](file.md#le-tracce-nel-file).

**Ho caricato i file ma il grafico è vuoto.**
Mancano le profondità. Scrivi quella delle prime due righe nella card **Profondità e file**:
le altre prendono il passo.

**Le profondità assegnate ai file sono sbagliate.**
Il raggruppamento segue l'ordine dei nomi. Controlla **Battute onda S** (1 o 2), correggi a
mano le celle, oppure premi **Raggruppa di nuovo** dopo aver cambiato le opzioni.

**Posso fidarmi dei tempi proposti?**
Come di una prima lettura fatta da un altro: vanno riguardati tutti sulle tracce. Sul
rilievo di prova la proposta sulle onde P è entro circa mezzo millisecondo dalla scelta a
mano; sulle onde S entro qualche millisecondo, con gli scarti più grandi alle prime
profondità. Parti dai tempi marcati
«?», ma guarda anche gli altri. Vedi [Proporre i tempi](tracce.md#proporre-i-tempi).

**Perché molti tempi S sono dubbi?**
Perché l'onda di taglio arriva dentro la coda delle onde P e il suo primo arrivo è meno
netto. L'app marca un tempo come dubbio quando si scosta dall'andamento delle profondità
vicine, quando non cresce con la profondità o quando il segnale è debole: sulle S succede
spesso. «Dubbio» non vuol dire sbagliato, vuol dire da guardare.

**Come tolgo il «?» da un tempo che ho controllato?**
Sceglilo tu: attiva **Tp** o **Ts** e fai clic sulla traccia, anche nello stesso punto.

**Far proporre tempi o sismostrati costa crediti?**
No, con i pulsanti della scheda è gratuito. Se lo chiedi all'assistente, paghi il messaggio.

## Misure e calcolo

**Ho solo le onde S (o solo le P). Posso elaborare?**
Sì. Lascia a zero i tempi dell'onda che non hai: zero vale «non misurato». Le colonne di
quell'onda escono «--»; con le sole S hai V~s~, G e V~s,eq~, mentre ν, E~d~, E ed E~v~
richiedono anche V~p~.

**A una profondità manca un tempo.**
Lascialo a zero. I due intervalli che toccano quella ricezione restano «--» per quell'onda;
nel metodo diretto i tempi alle basi degli strati si interpolano sulle ricezioni misurate.

**Che cosa significa «--»?**
«Non calcolabile», non zero: manca un tempo, il tempo corretto non cresce fra due ricezioni,
oppure V~p~ e V~s~ non danno un coefficiente di Poisson fra 0 e 0,5.

**Dov'è il pulsante «Calcola»?**
Non c'è. L'elaborazione si aggiorna a ogni modifica ed è gratuita.

**Sposto i sismostrati ma la V~s,eq~ non cambia. È un errore?**
No. Nel metodo diretto la somma dei tempi di attraversamento degli strati è il tempo
corretto delle onde S alla profondità H, dovunque siano le basi. Nel metodo intervallo la
V~s,eq~ è calcolata sugli intervalli di misura. Cambia solo se la prova è più corta di H:
lì l'ultimo strato viene prolungato, e la sua velocità dipende dalla base che gli sta sopra.
Vedi [Elaborazione](elaborazione.md#velocita-equivalente-vseq).

**I sismostrati proposti sono la stratigrafia del sito?**
No. Sono la suddivisione che meglio segue i tempi corretti, con le basi sulle profondità di
misura. Usali come punto di partenza e spostali dove la stratigrafia del sondaggio e la tua
lettura della dromocrona lo richiedono. Vedi
[Proporre i sismostrati](elaborazione.md#proporre-i-sismostrati).

**Ho messo 40 m come profondità finale e l'etichetta dice ancora «Vs,30».**
Con profondità finale di 30 m o più l'etichetta è **Vs,30**, ma il valore è quello fra le
due profondità scritte nella nota sotto il numero. Per la V~s,30~ lascia 0 e 30.

**La prova arriva a 20 m. Posso avere la V~s,30~?**
L'app prolunga l'ultimo strato fino a 30 m e lo dichiara a video e in relazione. È
un'ipotesi: valuta tu se la velocità dell'ultimo strato può essere estesa.

**Il programma mi dice la categoria di sottosuolo?**
No. La V~s,eq~ è un numero; la categoria richiede la profondità del substrato e resta al
progettista.

**Posso usare i moduli per i cedimenti?**
Non direttamente: sono moduli dinamici, a piccole deformazioni.

**Il peso di volume è misurato o stimato?**
Con l'interruttore acceso è stimato da una correlazione con V~s~ e profondità. Se hai
misure, spegnilo e scrivi γ nella tabella. Vedi
[Misure](misure.md#peso-di-volume-automatico-o-assegnato).

## Desktop

**Apro lo stesso progetto del desktop e i numeri sono diversi. Perché?**
Downhole NX corregge alcuni difetti di calcolo del programma desktop. Le differenze stanno
in punti precisi: velocità dell'ultimo strato, γ e moduli del metodo diretto, V~s,eq~ del
metodo intervallo e delle prove più corte di H. Tempi corretti e valori per intervallo
coincidono. La tabella completa, con ragione ed effetto, è in
[Validazione e differenze dal desktop](validazione.md#differenze-dal-programma-desktop).

**Posso salvare in `.dwhx` per riaprire nel desktop?**
No. Downhole NX apre i file del desktop ma salva solo in `.dhnx`.

**Aprendo un `.dwhx` non ritrovo le tracce.**
Il progetto del desktop non le contiene. Ricarica i file SEG-2 nella scheda Tracce.

## Sessione, file e crediti

**Ho lasciato l'app aperta e ora dice «La sessione è scaduta».**
Dopo 30 minuti di inattività il progetto non è più in memoria. Non è stato scritto né
addebitato nulla: riapri il tuo `.dhnx`. Salva spesso. Vedi [File](file.md#la-sessione).

**«Il progetto è stato modificato nel frattempo».**
L'assistente o un'altra scheda del browser hanno cambiato il progetto. Ricarica la pagina:
ciò che avevi a video non è stato salvato.

**Che cosa consuma crediti?**
**Genera Word**, **Esporta DXF** e ogni messaggio all'assistente. Tutto il resto è gratuito.

**Ho pagato un'operazione fallita?**
No. I crediti sono addebitati solo a operazione riuscita.

**In che lingua esce la relazione? Posso averla in PDF?**
Nella lingua dell'interfaccia: cambiala prima di generare. Il formato è Word; il PDF lo
ottieni dal tuo programma di scrittura.

**Funziona su tablet o con Safari?**
L'app è collaudata con i browser desktop basati su Chromium e finestre larghe almeno 900 px.
Il trascinamento a tocco e Safari non sono stati collaudati.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Downhole%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/downhole/docs/it/faq.md).*
