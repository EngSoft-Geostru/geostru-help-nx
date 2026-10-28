# Validazione e differenze dal desktop

Il punto **10.2 delle NTC 2018** chiede al **progettista** di valutare l'affidabilità del
codice di calcolo che usa. È un giudizio tuo; il nostro compito è darti il materiale per
formarlo: campi d'impiego e limiti, basi teoriche, casi di prova risolti e ripetibili.

Questa pagina ne è la sintesi. È una **validazione**, fatta da chi sviluppa il programma e
verificabile da chiunque: nessun ente terzo è coinvolto.

Se arrivi dal programma desktop e vuoi sapere perché un numero è cambiato, vai a
[Differenze dal programma desktop](#differenze-dal-programma-desktop).

## Campi d'impiego e limiti

Downhole NX elabora la **prova sismica in foro**: una sorgente in superficie, a distanza d
dall'asse del foro, e un ricevitore calato a profondità successive. Dai tempi di primo
arrivo delle onde P e S calcola:

- la distanza sorgente–ricevitore e i **tempi corretti** per l'obliquità del percorso;
- con il **metodo diretto**, per ogni sismostrato definito sulla dromocrona: V~p~, V~s~,
  peso di volume, coefficiente di Poisson, G, E~d~, E, E~v~;
- con il **metodo intervallo**, gli stessi parametri fra due ricezioni consecutive e le loro
  medie per sismostrato;
- la **velocità equivalente** V~s,eq~ fra una profondità iniziale e una profondità H
  (V~s,30~ con H = 30 m).

**Limiti**

- **La qualità del risultato è quella dei tempi di arrivo.** L'app può proporli, ma una
  proposta non è una lettura: vanno sempre riguardati sulle tracce, a partire da quelli che
  l'app stessa marca come dubbi. Lo stesso vale per i sismostrati proposti: sono la
  suddivisione che meglio segue i tempi, non un'interpretazione geologica.
- Assume **percorsi rettilinei** fra sorgente e ricevitore. Con forti contrasti di velocità
  vicino alla superficie il percorso reale è rifratto e i tempi corretti delle prime
  ricezioni sono approssimati; l'effetto cresce con d e si esaurisce in profondità.
- Con un solo ricevitore le velocità del metodo intervallo sono di **pseudo-intervallo**: i
  due tempi vengono da due battute diverse e l'errore di trigger entra per intero nella
  differenza.
- Il peso di volume automatico viene da una **correlazione empirica**: è una stima. Se hai
  misure, assegnale alla tabella.
- I moduli sono **dinamici, a piccole deformazioni**: non sono i moduli di un calcolo di
  cedimenti.
- **Non attribuisce la categoria di sottosuolo**.
- Non corregge per l'inclinazione del foro né per la quota della sorgente rispetto al piano
  campagna.
- Legge tracce SEG-2, di testo e gli archivi ZIP del piezocono sismico (esportazioni RAV o
  SPAS); non assembla file P e S con un numero diverso di canali. Il riconoscimento
  automatico dell'acquisizione è un aiuto alla lettura dei file, non entra nel calcolo e va
  controllato sulle tracce.

## Basi teoriche

Le formule, con la bibliografia, sono nella pagina [Cenni teorici](teoria.md): tempi
corretti, metodo diretto, metodo intervallo, parametri elastici, correlazione del peso di
volume, velocità equivalente, proposte automatiche, arrotondamenti.

## Casi di prova

Nove casi, ripetuti in automatico a ogni versione del programma. I primi cinque hanno un
riferimento **in forma chiusa**, che chiunque può rifare a mano; il sesto è il confronto
con il programma desktop; il settimo riguarda gli ingressi anomali; l'ottavo le proposte
automatiche; il nono è una prova reale con le tracce, confrontata con il desktop.

| Caso | Oggetto | Riferimento | Esito |
|---|---|---|---|
| 1 | Mezzo omogeneo, V~p~ = 1 500 e V~s~ = 300 m/s, d = 3 m, 20 ricezioni | tempi esatti del percorso rettilineo | V~s~ d'intervallo 299,98 ÷ 300,02 (≤ 0,01 %); V~p~ ≤ 0,03 %; V~s,eq~ = 300,0 |
| 2 | Due strati: 0–8 m a 600 / 200 m/s, 8–20 m a 1 800 / 450 m/s | forma chiusa | V~s~ 200,0 e 450,0; V~p~ 600,0 e 1 800 ± 3; V~s,eq~ = 300,0 |
| 3 | Parametri elastici con γ = 19,6133 kN/m³, V~s~ = 200, V~p~ = 400 m/s | calcolo a mano | ν = 0,3333; G = 80,00; E~d~ = 320,00; E = E~v~ = 213,33 MPa |
| 4 | Peso di volume dalla correlazione | calcolo a mano | 18,405 kN/m³ (V~s~ = 200 m/s, z = 5 m); 23,536 (V~s~ = 1 000 m/s) |
| 5 | V~s,eq~ di una colonna nota: 0–10 m a 200, 10–30 m a 400 m/s | calcolo a mano | 300,00 fra 0 e 30 m; 333,33 fra 5 e 30 m; 200,00 fra 0 e 10 m |
| 6 | Esempio del programma desktop | programma desktop | vedi sotto |
| 7 | Ingressi anomali | comportamento atteso | vedi sotto |
| 8 | Proposte automatiche dei tempi e dei sismostrati | letture dell'operatore, profili noti | vedi sotto |
| 9 | Prova reale con tracce SEG-2, un file per profondità (esempio `ex-tracce-seg2.dhnx`) | programma desktop | vedi sotto |

Gli scarti dei casi 1 e 2 sono l'effetto degli arrotondamenti: tempi corretti a 4 decimali di
millisecondo, tempi alle basi a 2. Su un intervallo di 1 m a 1 500 m/s valgono ± 0,2 m/s.

**Controllo di coerenza (caso 5).** Nel metodo diretto la somma dei tempi di attraversamento
è il tempo corretto delle onde S a H: la V~s,eq~ non può dipendere da dove si pongono gli
strati. Sull'esempio esce 242,86 m/s con uno strato, con cinque strati e nel metodo
intervallo, con o senza sismostrati.

### Caso 6 — l'esempio del desktop

È il progetto che apri con **File → Apri l'esempio**: 30 ricezioni ogni metro da 1 a 30 m,
d = 2,6 m, peso di volume automatico, cinque sismostrati con le basi salvate dal desktop
(5,04 – 10,30 – 17,78 – 25,32 – 30,11 m).

**Tempi corretti e metodo intervallo** coincidono con il desktop fino all'ultima cifra
stampata, su tutte le 30 righe. Per esempio, primo intervallo (0–1 m): V~p~ = 348,21 e
V~s~ = 163,09 m/s, γ = 20,71 kN/m³, ν = 0,3595, G = 56,17, E~d~ = 256,06, E = 152,73,
E~v~ = 181,17 MPa.

**Metodo diretto.** Rimettendo nel calcolo le convenzioni del desktop, Downhole NX
restituisce esattamente i numeri del desktop: questo dimostra che gli scarti qui sotto sono
le correzioni dichiarate, e nient'altro.

| Strato | Base [m] | V~p~ [m/s] | V~s~ [m/s] | γ NX | γ desktop | G NX [MPa] | G desktop |
|---|---|---|---|---|---|---|---|
| 1 | 5,04 | 367,35 | 182,74 | 18,77 | 18,04 | 63,90 | 61,42 |
| 2 | 10,30 | 482,57 | 209,31 | 18,19 | 18,54 | 81,28 | 82,81 |
| 3 | 17,78 | 1 108,15 | 202,00 | 17,56 | 18,07 | 73,04 | 75,20 |
| 4 | 25,32 | 1 702,03 | 337,21 | 19,27 | 20,05 | 223,39 | 232,49 |
| 5 | **30,00** | **1 181,82** | **409,45** | 19,84 | 21,17 | 339,12 | 379,20 |

Nel desktop lo strato 5 ha base 30,11 m, V~p~ = 1 209,60 e V~s~ = 419,07 m/s.
**V~s,30~ = 242,86 m/s** contro 243,37 del desktop (−0,2 %).

Gli scarti sono due, entrambi voluti:

1. **Ultimo strato.** Il desktop pone la base dell'ultimo strato alla distanza inclinata
   dell'ultima ricezione (30,11 m = √(30² + 2,6²)) invece che alla sua profondità (30 m).
   Con lo stesso tempo lo strato risulta più spesso, e la sua velocità è sovrastimata del
   2,3 %.
2. **Peso di volume.** Il desktop passa alla correlazione lo spessore dello strato al posto
   della profondità. Downhole NX usa la profondità media. I pesi cambiano da −6 % a +4 %, e
   con essi G, E~d~, E, E~v~, che ne dipendono linearmente. Velocità e ν non cambiano.

### Caso 7 — ingressi anomali

| Ingresso | Comportamento |
|---|---|
| Profondità doppia, fuori ordine o non positiva | Nessun calcolo; l'errore indica la riga |
| Prova di sole onde S (T~p~ = 0 ovunque) | Colonne P «--»; V~s~, G e V~s,eq~ calcolate |
| Un tempo mancante a una ricezione | I due intervalli che la toccano restano «--» per quell'onda; i tempi alle basi si interpolano sulle ricezioni misurate |
| Tempo corretto decrescente | Intervallo «--», avviso con il numero della ricezione |
| V~p~ ≤ V~s~, o V~p~/V~s~ ≤ √2 | ν ed E «--» (ed E~v~ se negativo) |
| Tempo alla base decrescente fra due basi (metodo diretto) | Lo strato assume i parametri del precedente ed è marcato «\*» |

### Caso 8 — le proposte automatiche

Le proposte non entrano nel calcolo: qui si misura quanto si avvicinano a ciò che sceglie
una persona.

**Tempi di arrivo, su un rilievo reale.** 18 profondità da 1 a 18 m, registrazioni SEG-2 a
tre canali campionate a 64 µs. Il confronto è con i tempi scelti a mano dall'operatore.

| Onda | Scarto dalla scelta a mano | Tempi marcati dubbi |
|---|---|---|
| P | mediano 0,3 ms, massimo 1,4 ms | 4 su 18 |
| S | mediano 1,4 ms, massimo 5,3 ms | 10 su 18, fra cui tutti quelli oltre 4,5 ms |

Sulle P la proposta coincide con la lettura dell'operatore entro l'incertezza della lettura
stessa; i tempi dubbi sono quelli che non crescono rispetto alla profondità precedente, per
mezzo millisecondo o meno.

Sulle S lo scarto è di qualche millisecondo, su tempi di 40–110 ms, e oltre metà delle
proposte è marcata dubbia. Alle prime due profondità l'onda di taglio è coperta dal treno
delle P; fra 6 e 11 m il treno d'onda cambia forma, e lì anche i tempi dell'operatore sono
irregolari (74,5 – 75,8 – 77,5 – 84,9 ms). A 18 m lo scarto è 4,2 ms e il tempo **non** è
marcato: un tempo non dubbio non è per questo giusto. Per questo le proposte sulle S si
controllano una per una.

**Tempi di arrivo, su tracce sintetiche** (onde smorzate con arrivo noto, su rumore): P
entro 0,6 ms; S entro +3 / −6 ms. L'anticipo viene dal filtro senza sfasamento, che allarga
il treno d'onda da entrambi i lati.

**Sismostrati, su profili a strati noti** (tempi esatti di tre e di cinque strati, anche
con 0,5 ms di rumore sui tempi): le basi sono ritrovate esattamente, entro un metro con il
rumore, senza strati in più.

**Sismostrati, sull'esempio del caso 6**: la proposta è 6 – 12 – 18 – 27 – 30 m, con scarto
0,57 ms; l'interprete aveva scelto 5,04 – 10,30 – 17,78 – 25,32 – 30 m. Le basi proposte
stanno sulle profondità di misura, una ogni metro: la differenza è entro due ricezioni. La
V~s,30~ è la stessa, 242,86 m/s, come deve (caso 5).

### Caso 9 — prova reale con tracce SEG-2

È l'esempio `ex-tracce-seg2.dhnx`, che si scarica dal pulsante **?**, scheda **Risorse**: 31
file SEG-2 a tre canali (un verticale e due orizzontali), uno per profondità da 1 a 31 m,
con tutte le battute nello stesso file e la profondità letta dal nome (`1m ps.sg2` …
`31m ps.sg2`). Tempi scelti sulle tracce, d = 1,5 m, peso di volume automatico, H = 30 m.
Sismostrati del metodo diretto con basi 10 – 25 – 31 m, del metodo intervallo con basi
7 – 31 m.

È un caso difficile, ed è per questo che sta qui: molti tempi non crescono con la
profondità. Il metodo intervallo segnala il **tempo corretto decrescente** alle ricezioni 5,
6, 7, 9, 12, 14, 15, 17, 19, 20, 24, 28, 30, 31 e lì non dà velocità («--»); le medie per
strato usano solo gli intervalli calcolabili.

| Metodo | Strato | V~p~ [m/s] | V~s~ [m/s] | γ [kN/m³] | ν | G [MPa] | E~d~ [MPa] | E [MPa] | E~v~ [MPa] |
|---|---|---|---|---|---|---|---|---|---|
| diretto | 0–10 m | 396,51 | 188,64 | 18,17 | 0,35 | 65,94 | 291,34 | 178,54 | 203,42 |
| diretto | 10–25 m | 1 218,52 | 1 029,51 | 23,64 | -- | 2 554,46 | 3 578,51 | -- | 172,56 |
| diretto | 25–31 m | 335,01 | 1 065,72 | 23,75 | -- | 2 750,94 | 271,84 | -- | -- |
| intervallo (medie) | 0–7 m | 324,07 | 173,99 | 18,32 | 0,39 | 68,49 | 362,10 | 224,54 | 344,81 |
| intervallo (medie) | 7–31 m | 1 178,20 | 841,46 | 21,31 | 0,46 | 3 162,57 | 1 852,46 | 631,42 | 5 618,78 |

**V~s,30~ del metodo diretto = 415,10 m/s. V~s,30~ del metodo intervallo: non
calcolabile.** Sugli intervalli di misura c'è almeno un tratto senza V~s~ (il tempo corretto
delle S non cresce), e la V~s,eq~ non si calcola saltando i tratti: l'app scrive «--». Nel
metodo diretto lo stesso tempo entra nella spezzata e la V~s,eq~ resta definita. Qui H = 30 m
cade dentro lo strato 25–31 m, quindi il valore dipende dalla base a 25 m: con una base a 30 m
sarebbe 406,45 m/s, cioè 30 m diviso il tempo corretto delle S a 30 m.

**Confronto con il programma desktop** (calcolo eseguito sugli stessi dati): tempi
corretti, valori dei 31 intervalli, medie per strato dei due metodi e le due V~s,eq~
coincidono fino all'ultima cifra. Una versione precedente del desktop, con il metodo
intervallo selezionato, mostrava una V~s,30~ di circa 416 m/s: era il valore del metodo
diretto, rimasto nella casella che i due metodi condividevano. Downhole NX mostra sempre la
V~s,eq~ del metodo selezionato, qui «--».

### Ripetere i casi

Il caso 6 si ripete aprendo l'esempio (**File → Apri l'esempio**) e leggendo le tabelle
della scheda Elaborazione; sullo stesso esempio **Proponi sismostrati** dà la suddivisione
del caso 8. Il caso 9 si ripete aprendo `ex-tracce-seg2.dhnx` con **File → Apri…**. I casi
1–5 si rifanno a mano con le formule dei [Cenni teorici](teoria.md): inserisci le misure
nella scheda Misure e confronta.

## Differenze dal programma desktop

Downhole NX **non riproduce** alcuni comportamenti del programma desktop Downhole, perché
sono difetti di calcolo. Chi confronta un vecchio elaborato con uno nuovo trova qui la
ragione di ogni scarto.

| Programma desktop | Downhole NX | Perché | Effetto |
|---|---|---|---|
| Base dell'ultimo sismostrato alla distanza inclinata SR | Alla profondità dell'ultima ricezione | SR è una distanza lungo il raggio, non una profondità | Velocità dell'ultimo strato e V~s,eq~ (esempio: −2,3 % e −0,2 %) |
| γ del metodo diretto dalla correlazione applicata allo **spessore** dello strato | Dalla **profondità media** dello strato | La correlazione è in funzione della profondità; il desktop stesso usa la profondità nel metodo intervallo | γ e moduli del metodo diretto (esempio: γ da −6 % a +4 %) |
| Sismostrato d'intervallo con la base non coincidente con una ricezione: a ogni strato la media dell'intero profilo | Base agganciata alla ricezione più vicina | Lo strato deve mediare i suoi intervalli, non tutti | Medie per strato del metodo intervallo |
| V~s,eq~ del metodo intervallo dalla V~s~ **media aritmetica** dei sismostrati | Sugli **intervalli di misura** | La media aritmetica delle velocità non è la velocità dello strato: sovrastima la V~s,eq~ e la fa dipendere da dove sono i confini | V~s,eq~ del metodo intervallo più bassa, a favore di sicurezza, e uguale a quella del metodo diretto (esempio: 265,81 → 242,86 m/s, −9 %) |
| ν della riga precedente quando V~p~ ≤ V~s~; E = 2·G senza ν; E~v~ negativo stampato | «--» | Un valore non calcolabile non è un dato di prova | Righe anomale |
| Strati che non raggiungono H: H diviso il tempo degli strati esistenti | Ultimo strato esteso fino a H, e dichiarato | La formula richiede tratti che coprano tutto lo spessore fra z~0~ e H | V~s,eq~ delle prove più corte di H |
| Numeratore della V~s,eq~ troncato all'intero | H − z~0~ | 25,5 m non sono 25 m | V~s,eq~ quando H − z~0~ non è intero |
| Tempo mancante trattato come zero | Intervallo «--» | Un tempo non misurato non è un tempo nullo | Prove con ricezioni incomplete |

**Che cosa non cambia.** Tempi corretti, valori per intervallo di misura (salvo le righe
anomale della tabella) e V~p~, V~s~, ν dei sismostrati del metodo diretto diversi dall'ultimo
coincidono con il desktop.

**Scelte del desktop mantenute.** Sono scelte di metodo, non difetti:

- la velocità di strato del metodo diretto è la corda fra i tempi alle due basi, non una
  retta ai minimi quadrati;
- il primo intervallo va dal piano campagna, a tempo zero, alla prima ricezione: con la
  prima ricezione superficiale e d grande è il valore più sensibile all'ipotesi di percorso
  rettilineo;
- lo strato con tempo alla base decrescente copia il precedente;
- la correlazione del peso di volume e gli arrotondamenti intermedi.

!!! tip "Confrontare un vecchio elaborato"
    Apri il `.dwhx` con **File → Apri…** e confronta per primi i tempi corretti e la tabella
    del metodo intervallo: devono coincidere. Poi cerca le differenze dove la tabella qui
    sopra le prevede: ultimo strato, γ e moduli del metodo diretto, V~s,eq~.

## Versione

Questa pagina vale per il **motore di calcolo 1.2.0** (ottobre 2026). La versione del motore
è distinta da quella dell'app: cambia solo quando può cambiare un risultato o la lettura dei
dati, ed è stampata nel blocco **Codice di calcolo** di ogni relazione (vedi
[Relazione](relazione.md#il-blocco-codice-di-calcolo)). La versione dell'app è nella barra
di stato in basso e nel pulsante **?**, scheda **Versione**.

| Motore | Che cosa è cambiato |
|---|---|
| 1.0.0 | Prima emissione: calcolo (casi 1–7) e proposte automatiche dei tempi e dei sismostrati (caso 8). |
| 1.1.0 | Lettura delle tracce: archivio ZIP del piezocono sismico, profondità dal nome del file («1m ps», «12,5 m P»). Il metodo intervallo non dà la V~s,eq~ quando un intervallo ha il tempo corretto non crescente (caso 9). Gli altri risultati, a parità di misure, non cambiano. |
| 1.2.0 | Riconoscimento dell'acquisizione al caricamento (terne P/S1/S2, canale P, canali di trigger, verso della registrazione); un numero nudo con zeri a sinistra nel nome («001.DAT») non è più preso per profondità. Il calcolo non cambia: a parità di misure i casi 1–9 danno gli stessi numeri. |

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Downhole%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/downhole/docs/it/validazione.md).*
