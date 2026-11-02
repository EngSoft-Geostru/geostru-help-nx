# Validazione e differenze dal desktop

Il punto **10.2 delle NTC 2018** chiede al **progettista** di valutare l'affidabilità del
codice di calcolo che usa. È un giudizio tuo; il nostro compito è darti il materiale per
formarlo: campi d'impiego e limiti, basi teoriche, casi di prova risolti e ripetibili.

Questa pagina ne è la sintesi, valida per il **motore di calcolo dalla versione 1.1.0** (la
versione è stampata nel blocco «Codice di calcolo» di ogni relazione). È una
**validazione**, fatta da chi sviluppa il programma e verificabile da chiunque: nessun ente
terzo è coinvolto.

Se arrivi da Easy-MASW desktop e vuoi sapere perché un numero è cambiato, vai a
[Differenze dal programma desktop](#differenze-dal-programma-desktop).

## Campi d'impiego e limiti

MASW NX elabora prove **MASW attive**: una sorgente in linea con uno stendimento di geofoni a
passo costante. Dalle tracce calcola lo spettro f-v, ricava la curva di dispersione delle
onde di Rayleigh (picking, fino a 5 modi) e ne inverte un profilo di V~s~ a strati
piano-paralleli; dal profilo ricava V~s,eq~, H, categoria di sottosuolo (NTC 2018, NTC 2008)
e parametri geotecnici stimati.

**Limiti**

- Il modello è **1D a strati orizzontali e omogenei**: variazioni laterali, topografia e
  pendenze degli strati non sono rappresentate.
- L'inversione è **stocastica e non unica**: profili diversi riproducono la stessa curva. Il
  misfit misura l'accordo con il picking, non la verità del profilo. Due corse danno
  soluzioni un po' diverse.
- La **profondità d'indagine** è dell'ordine di λ/2 della lunghezza d'onda più lunga letta
  con affidabilità: sotto, il profilo è estrapolato. In particolare il semispazio e una
  V~s,eq~ su 30 m richiedono energia alle basse frequenze.
- Il **picking** è una scelta dell'operatore, e il risultato ne dipende: modi superiori
  scambiati per il fondamentale sovrastimano V~s~. Il picking automatico è una proposta: sopra
  i 20 Hz il modo fondamentale dell'esempio del desktop non forma una cresta nella mappa e va
  completato a mano.
- ρ è il valore che si assegna agli strati (nel desktop il «peso di volume» è usato come
  densità in kg/m³); ν è assunto. La curva è debolmente sensibile a entrambi.
- **G~0~, E~d~, M~0~, E sono moduli dinamici a piccole deformazioni.** NSPT (Ohta e Goto) e
  Qc (Jamiolkowski) sono correlazioni empiriche invertite da V~s~, indicative.
- Non sono trattati: la vista f-k e ReMi/f-p del desktop, le sorgenti passive, le onde di
  Love, l'inversione congiunta con l'HVSR, la categoria secondo l'Eurocodice 8.

## Basi teoriche

Le formule, con la bibliografia, sono nella pagina [Cenni teorici](teoria.md): spettro f-v
(phase-shift, Park, Miller e Xia), problema diretto (Thomson-Haskell-Dunkin, motore
verificato a precisione macchina sul desktop), inversione (Nelder e Mead), V~s,eq~ (NTC 2018
§3.2.2), parametri elastici, Ohta e Goto, Jamiolkowski, funzione di trasferimento SH con
smorzamento dell'1 %.

## Casi di prova

Due gruppi: casi con riferimento **in forma chiusa**, che chiunque può rifare a mano o con un
foglio di calcolo, e il confronto con **Easy-MASW desktop** su dieci progetti. Sono ripetuti
in automatico a ogni versione del programma.

### Forme chiuse

| Caso | Dati | Atteso | MASW NX |
|---|---|---|---|
| Spettro di un'onda sintetica | 24 geofoni a 1 m, f = 20 Hz, v = 200 m/s | cresta a 200 ± 10 m/s, massimo di colonna 1 | ok |
| V~s,eq~ senza substrato | 10 m a 200 + 20 m a 400 m/s | 30 / (0,05 + 0,05) = 300 m/s, H = 30 m | 300 |
| Substrato a 20 m | 10 m a 200, 10 m a 400, poi V~s~ 900 m/s | 20 / 0,075 = 266,67 m/s, categoria E | 266,67, E |
| Substrato entro 3 m | 2 m a 200, poi V~s~ 900 m/s | V~s,eq~ = 900 m/s, categoria A | 900, A |
| Piano di posa che taglia lo strato | 10 m a 200, poi 400 m/s; posa a 4 m | 30 / (0,03 + 0,06) = 333,33 m/s | 333,33 |
| Trasferimento, strato omogeneo | H = 10 m, V~s~ = 300 m/s, f = 3,75 Hz | 1 / \|cos(π/4)\| = 1,414 | 1,41 |
| Trasferimento su substrato | H = 20 m, V~s~ = 200 m/s | prima risonanza V~s~/4H = 2,5 Hz | 2,5 Hz |
| Inversione di un profilo noto | 150 / 300 / 600 m/s, curva sintetica | misfit < 0,01, V~s1~ entro il 5 % | ok |
| Filtro passa-basso | taglio 60 Hz, attenuazione a 70 Hz, 20 dB, campionamento 2 000 Hz | passa a 10 Hz, ≤ 0,11 a 70 Hz | ok |

### Confronto con Easy-MASW desktop

I valori di riferimento sono stati generati il 29/10/2026 con le librerie di calcolo del
desktop sui suoi dieci progetti di esempio. Il confronto fra due implementazioni nostre **non
dimostra la correttezza del metodo**, che è affidata alle forme chiuse: dimostra che il
porting non ha cambiato il calcolo.

| Esempio | Tracce | Campioni | dt [s] | dx [m] | Mappa v×f | Picking | Misfit desktop | V~s,eq~ [m/s] | H [m] | Cat. desktop |
|---|---|---|---|---|---|---|---|---|---|---|
| DefaultExample | 24/24 | 5120 | 0,0005 | 1 | 799×180 | 30 | 0,07952 | 290,99 | 30 | C |
| NTC2018 3amasw | 24/24 | 2048 | 0,001 | 1 | 1999×123 | 27 | 0,17238 | 288,27 | 14,78 | E |
| geostru001 | 24/24 | 7651 | 0,000131 | 1 | 1550×74 | 38 | 0,12270 | 330,36 | 30 | C |
| geostru002 | 24/24 | 7651 | 0,000131 | 1 | 1599×74 | 39 | 0,16853 | 299,51 | 30 | E (vedi sotto) |
| geostru003 | 24/24 | 7651 | 0,000131 | 1 | 1550×74 | 40 | 0,12260 | 327,48 | 30 | C |
| geostru004 | 24/24 | 1000 | 0,001 | 2 | 1750×60 | 32 | – | – | – | – |
| geostru005 | 12/12 | 8000 | 0,00025 | 2,5 | 1799×202 | 20 | 0,07401 | 392,42 | 8,25 | B |
| geostru006 | 12/12 | 8000 | 0,00025 | 2,5 | 5999×120 | 15 | – | – | – | – |
| geostru007 | 11/12 | 2500 | 0,0002 | 5 | 4900×55 | 17 | 0,02713 | 1229,20 | 0 | A |
| geostru008 | 12/12 | 8000 | 0,00025 | 2,5 | 1199×120 | 15 | 0,00825 | 340,51 | 30 | C |

Il trattino indica i progetti salvati senza inversione.

Esito dei confronti, su tutti gli esempi che hanno il dato:

| Grandezza | Tolleranza | Esito |
|---|---|---|
| Mappa f-v contro quella salvata | 1·10⁻⁹ | entro tolleranza su 10 esempi |
| Curva dei massimi | esatta su v, 1·10⁻¹² su f | identica a quella ricalcolata dal desktop |
| Coefficienti della regressione | 1·10⁻⁶ relativo | coincidono |
| Misfit del modello del desktop | 1·10⁻¹² | coincide |
| Errore % del modello del desktop | 1·10⁻⁹ | coincide |
| Curve teoriche del modello del desktop | 1·10⁻⁹ relativo | coincidono |
| Corsa con seme fisso | misfit 1·10⁻¹², V~s~ 1·10⁻⁹ | identica |
| V~s,eq~, H, categoria (riproducendo il desktop) | 1·10⁻⁹ / 1·10⁻⁵ / esatta | coincidono |

**Commenti agli scarti**

- In 4 esempi la curva v salvata nel file differisce di 1 m/s da quella ricalcolata dallo
  stesso desktop: viene da una versione precedente del programma. Il confronto si fa con
  quella ricalcolata.
- La categoria «rimasta» nel file del desktop non è un riferimento: può essere di NTC 2008 o
  di un modello precedente. Si usa quella ricalcolata.
- In geostru007 il desktop calcola V~s,eq~ sul modello salvato negli strati (1 229,2 m/s), che
  non è la soluzione migliore (V~s1~ = 1 230,7 m/s): MASW NX usa la soluzione scelta a video.

## Differenze dal programma desktop

Il principio è la **parità prima**: MASW NX riproduce il calcolo del desktop, e corregge solo
i difetti dichiarati qui. Il kernel sa ancora riprodurre il desktop alla lettera; i test lo
usano per dimostrare che gli scarti sono le correzioni e non altro.

### Correzioni

| Difetto del desktop | Effetto | MASW NX |
|---|---|---|
| Quote sommate in precisione singola nel calcolo di H | geostru002: H = 29,999998 m, categoria **E** invece di **C** | somme in doppia precisione, tolleranza 10⁻⁶ sui 30 m: **C** |
| Campioni SEG-Y in formato IBM letti come IEEE | ampiezze errate | conversione corretta |
| Traccia deselezionata in mezzo allo stendimento | le successive si avvicinano di un dx: spettro falsato | la fase usa la posizione reale del geofono; identico sugli esempi |
| Quote dei sei strati di default incoerenti con gli spessori | stima iniziale delle V~s~ su profondità sbagliate | quote cumulate |

### Riprodotti per fedeltà

Da rivedere, ma lasciati come nel desktop perché i risultati restino confrontabili:

- l'**etichetta di frequenza** delle colonne della mappa è sfasata fino a un passo di
  frequenza df (meno di 0,5 Hz sugli esempi, sotto la risoluzione di lettura);
- nel filtro dei massimi k~min~ = k~max~ / n~f~;
- una V~s,eq~ esattamente pari a 100, 360 o 800 m/s non cade in nessuna fascia: l'app lo
  dichiara invece di scegliere.

## Versioni del motore

| Versione | Data | Cosa cambia nei risultati |
|---|---|---|
| 1.0.0 | 30/10/2026 | Prima versione pubblicata. |
| 1.1.0 | 31/10/2026 | Picking automatico sulle **creste** della mappa f-v, anche su più modi; modello iniziale **proposto dal picking** invece dei sei strati fissi 4-5-6-7-8 m (la stessa regola è nel desktop); stima delle V~s~ iniziali con λ/2 su v~min~, v e v~max~ e Poisson di default 0,2, allineati al desktop corretto (prima si dimezzava solo v~min~ e si partiva da 0,3). |

Il calcolo dello spettro e l'inversione non cambiano: a parità di picking e di strati
iniziali i risultati della 1.0.0 si riproducono. Sull'esempio del desktop (DefaultExample,
1 000 iterazioni), con il picking e gli strati del file, MASW NX dà **misfit 0,0796** ed
**errore 0,204 %**, contro 0,080 e 0,206 % del desktop.

Cambia il punto di partenza quando l'utente non scrive gli strati: con il picking automatico
e gli strati fissi del desktop l'errore era del **2,28 %**, con gli strati proposti dello
**0,13–0,22 %** su tre semi diversi. Limite: sopra i 20 Hz il modo fondamentale dell'esempio
non forma una cresta nella mappa, quindi il picking automatico non lo raggiunge e va
completato a mano.

## Riproducibilità

I casi di prova sono test automatici del codice sorgente, ripetuti a ogni versione; i
progetti e i risultati attesi sono archiviati con il codice. Il documento di validazione
completo è disponibile su richiesta a [info@geostru.ai](mailto:info@geostru.ai).

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20MASW%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/masw/docs/it/validazione.md).*
