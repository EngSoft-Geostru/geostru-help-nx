# Prova

La scheda **Prova** raccoglie le misure della prova di emungimento: la **prova a gradini di portata**, la **prova a portata costante**
con la **risalita**, gli **abbassamenti stabilizzati** e, se non hai la prova a gradini, la **portata critica nota** del pozzo. Ogni
valore che scrivi si salva da solo; i [Risultati](risultati.md) si aggiornano con i dati nuovi.

La scheda ha due riquadri:

1. **Prova a gradini di portata**, con il pannello per incollare i gradini e il riquadro *Portata critica nota (senza prova a gradini)*;
2. **Portata costante e risalita**, con la portata della prova, gli abbassamenti stabilizzati, le letture di pompaggio e quelle di
   risalita.

Non servono tutte e due le prove. Quali metodi si calcolano con quali dati lo trovi nel [catalogo dei metodi](metodi.md#quali-dati-per-quali-metodi).

!!! note "Nota"
    I piezometri si inseriscono nella scheda **Pozzo** (nome e distanza r dall'asse del pozzo): vedi [Pozzo](pozzo.md). Ogni
    piezometro aggiunge una colonna **s** *nome* in tutte le tabelle di questa scheda; passando col mouse sull'intestazione vedi la
    sua distanza. Se togli un piezometro, spariscono anche le sue letture.

## Unità, tempi e numeri

In testa a ogni riquadro scegli come leggere e scrivere le tabelle:

| Comando | Scelte | Predefinita |
|---|---|---|
| **Tempi in** | h:mm:ss, s, min, h | h:mm:ss |
| **Portate in** | l/s, m³/h, l/min, m³/s | l/s |

È una preferenza di chi guarda, non un dato del progetto: vale per questo browser e si ricorda. Cambiandola, il programma salva
prima ciò che hai scritto, poi ricarica la pagina con i valori convertiti. Il calcolo lavora sempre in secondi e m³/s.

Regole comuni a tutte le tabelle:

- **Tempi.** Si scrivono come `1:30:00`, `90 min`, `2h` o come numero nell'unità scelta. `8:20` vale 8 h 20 min (convenzione
  dell'orologio, non minuti e secondi). Sono accettate anche le sigle `1h30m15s`, `1h 30'`, `45 min`, `90 s`, `2 g` o `2d`, e `30"`
  per i secondi. Con **Tempi in** h:mm:ss un numero senza sigla vale **minuti**.
- **Abbassamenti** in m, positivi verso il basso. Una cella vuota è una misura non fatta, non uno zero.
- **Numeri.** Virgola o punto decimale vanno bene entrambi; sono accettati il meno tipografico «−» e la notazione esponenziale
  (`1,2E-03`).
- Una riga lasciata del tutto vuota non si salva.

Un valore che non si legge resta a video segnato in rosso e **non si salva**: sotto il campo compare il motivo (*Non è un numero
leggibile: non salvato.* oppure *Non può essere negativo: non salvato.*). Portate, abbassamento critico e raggio presunto non
possono essere negativi; un tempo negativo non si legge.

## Prova a gradini di portata

Una riga per gradino: la **lettura di fine gradino**, con il tempo dall'inizio della prova e gli abbassamenti **cumulati** (quelli
misurati a fine gradino rispetto al livello statico, non l'incremento del solo gradino).

| Colonna | Unità | Significato |
|---|---|---|
| **#** | — | numero del gradino |
| **Data** | testo | data della lettura, testo libero (al più 40 caratteri); non entra nel calcolo |
| **Tempo** | unità di **Tempi in** | tempo dall'inizio della prova alla lettura di fine gradino |
| **Portata** | unità di **Portate in** | portata del gradino; non negativa |
| **s pozzo** | m | abbassamento nel pozzo di emungimento a fine gradino |
| **s** *piezometro* | m | abbassamento nel piezometro a fine gradino (una colonna per piezometro) |

**Aggiungi gradino** aggiunge una riga; la **×** a destra la toglie. **Incolla da Excel o CSV** apre il pannello descritto più sotto.

Un gradino è **valido** se ha portata e abbassamento nel pozzo entrambi positivi. Solo i gradini validi entrano nella curva
caratteristica:

- con **2** gradini validi a portate diverse si calcolano B e C (curva caratteristica di Jacob);
- con **3** o più si calcola anche Rorabaugh (esponente n libero);
- gli abbassamenti nei piezometri servono ai metodi in distanza sui gradini e alle stazioni di prova.

Il **Tempo** serve solo a Cooper-Jacob sulle stazioni di prova. La **portata critica** non si scrive qui: si sceglie sulla curva
caratteristica nei [Risultati](risultati.md#portata-concedibile).

!!! tip "Suggerimento"
    Scrivi i gradini in ordine di portata crescente, come sono stati eseguiti. Se il datalogger registra una lettura al minuto, non
    copiarle a mano: incollale con **Raggruppa le letture in gradini** e il programma tiene l'ultima lettura di ogni portata.

## Portata critica nota (senza prova a gradini)

Se non c'è la prova a gradini ma conosci la portata critica del pozzo (da prove in aree vicine o dal collaudo), indicala qui con il
suo abbassamento critico. Il metodo dei **pozzi singoli** ricava T e K dalla geometria del pozzo, da Q~c~ e s~c~ e dal raggio d'azione
presunto.

| Campo | Unità | Significato |
|---|---|---|
| **Portata critica Qc** | unità di **Portate in** | portata critica dichiarata |
| **Abbassamento critico sc** | m | abbassamento nel pozzo alla portata critica |
| **Raggio d'azione presunto R** | m | raggio d'azione da assumere; vale anche per i pozzi singoli della prova a gradini |

Servono tutti e tre i valori. Sono valori dichiarati, non misurati: i pozzi singoli li usano come un regime stazionario e danno
valori **indicativi**; la relazione dice che Q~c~ e s~c~ sono indicati da te. Con la portata critica nota il programma propone anche
la portata concedibile (0,9·Q~c~): vedi [Portata concedibile](risultati.md#portata-concedibile).

La pastiglia accanto al titolo dice lo stato:

- **in uso senza gradini**: non ci sono gradini validi, la portata critica nota si usa;
- **non usata: vale la prova**: c'è almeno un gradino valido. Vale la portata critica della prova a gradini, scelta sul grafico s(Q)
  nei Risultati. **Portata critica Qc** e **Abbassamento critico sc** restano salvati ma in sola lettura; **Raggio d'azione
  presunto R** resta modificabile, perché serve ai pozzi singoli anche con la prova a gradini.

!!! warning "Attenzione"
    I pozzi singoli non si calcolano in falda semiconfinata, né se nella scheda **Pozzo** non hai indicato se il pozzo è completo o
    incompleto. La portata concedibile dalla portata critica nota, invece, si propone comunque.

## Portata costante e risalita

### Portata della prova e abbassamenti stabilizzati

| Campo | Unità | Significato |
|---|---|---|
| **Portata della prova** (Q) | unità di **Portate in** | portata costante del pompaggio; non negativa |
| **Abbassamenti stabilizzati** → **s pozzo** | m | abbassamento a regime nel pozzo |
| **Abbassamenti stabilizzati** → **s** *piezometro* | m | abbassamento a regime in ciascun piezometro |

Senza **Portata della prova** positiva nessun metodo della portata costante si calcola, anche se le letture ci sono. Gli abbassamenti
stabilizzati (*a regime, per Dupuit-Thiem*) servono al metodo di Dupuit-Thiem in regime stazionario e al raggio d'azione dalla retta
di Thiem; un piezometro con abbassamento stabilizzato nullo si esclude (è oltre il raggio d'azione o non ha risentito).

### Pompaggio

Le letture durante il pompaggio: **t** dall'inizio del pompaggio, **s pozzo** e **s** di ogni piezometro, in m. **Aggiungi lettura**
aggiunge una riga, la **×** la toglie.

- Le letture nei **piezometri** danno T **e** S (Theis, Cooper-Jacob, distanza-abbassamento, Hantush in falda semiconfinata).
- Le letture nel solo **pozzo** danno T; S dal pozzo non è affidabile.
- Per la distanza-abbassamento servono almeno due piezometri a distanze diverse letti **allo stesso tempo**.

Le letture con tempo o abbassamento mancanti, nulli o negativi non entrano nelle rette e nei fitting (un logaritmo di zero non esiste).

### Risalita

Dopo l'arresto della pompa: **t′** dall'arresto e l'**abbassamento residuo** s′ nel pozzo e nei piezometri.

L'istante dell'arresto serve a calcolare t/t′ con t = t~arresto~ + t′:

- **Pompa ferma all'ultima lettura di pompaggio** (spunta, predefinita): l'arresto è il tempo dell'ultima lettura di pompaggio, mostrato
  fra parentesi;
- togli la spunta e scrivi **Arresto della pompa, dall'inizio** se la pompa si è fermata dopo l'ultima lettura.

La risalita si calcola solo se ci sono anche le letture di pompaggio. Un abbassamento residuo nullo si esclude dalla retta.

!!! example "Esempio"
    Pompaggio di 8 ore con l'ultima lettura a `7:55:00` e la pompa spenta alle `8:00:00`: togli la spunta e scrivi `8:00:00` in
    **Arresto della pompa, dall'inizio**. Le letture di risalita partono da t′ = `0:00:30`, `0:01:00`… dall'arresto, non dall'inizio
    della prova.

## Dati da verificare

Sotto il titolo dei due riquadri può comparire la striscia **Dati da verificare**. Non blocca il salvataggio: segnala un dato
probabilmente sbagliato.

| Avviso | Dove | Cosa controllare |
|---|---|---|
| *Le letture di pompaggio non sono in ordine di tempo (riga …)* | pompaggio | un tempo battuto male; i calcoli usano comunque i tempi |
| *Tempi di pompaggio ripetuti (righe …)* | pompaggio | righe doppie |
| *Abbassamento di … m alla riga …: non è un valore fisicamente possibile.* | gradini, pompaggio | oltre 1 000 m: errore di battitura o unità |
| *Abbassamento di … m alla riga …: il livello scenderebbe sotto il substrato …* | gradini, pompaggio | abbassamento nel pozzo oltre livello statico − substrato; controlla anche le quote in [Pozzo](pozzo.md) |
| *L'arresto della pompa indicato viene prima dell'ultima lettura di pompaggio* | risalita | l'istante dell'arresto |

## Incollare da Excel o CSV

Ogni tabella ha il pulsante **Incolla da Excel o CSV**: si apre un pannello sotto la tabella (*Incolla i gradini*, *Incolla le
letture di pompaggio*, *Incolla le letture di risalita*). Copia le colonne dal foglio di calcolo o dal file del datalogger e
incollale nel riquadro di testo.

1. Incolla il testo, **con la riga d'intestazione** se ce l'hai.
2. Se serve, imposta le opzioni (tabella sotto).
3. Premi **Anteprima**: il programma mostra come ha letto il testo e non scrive nulla.
4. Controlla l'anteprima e, nella colonna **Va a**, a quale serie va ogni colonna di misura (**Pozzo**, un piezometro o
   **— ignora —**). Cambiando una scelta l'anteprima si rifà.
5. Premi **Sostituisci le letture** (la tabella diventa quella incollata) oppure **Aggiungi alle letture** (le letture si aggiungono a
   quelle esistenti e si riordinano per tempo). La pagina si ricarica con i dati nuovi.

| Opzione | Scelte | Quando serve |
|---|---|---|
| **I tempi sono** | *da riconoscere*, *tempi trascorsi*, *ore dell'orologio* | se il riconoscimento automatico sbaglia |
| **Unità dei tempi numerici** | *dall'intestazione*, s, min, h | tempi scritti come numeri senza unità nell'intestazione |
| **Unità delle portate** | *dall'intestazione*, l/s, m³/h, l/min, m³/s | solo per i gradini, se l'intestazione non ha l'unità |
| **Inizio del pompaggio** (per la risalita **Arresto della pompa**) | ora, o data e ora (es. `08:30`, `12/03/2026 08:30`) | tempi come ore dell'orologio; nascosto con *tempi trascorsi* |
| **Livello statico** | m, stesso riferimento delle colonne di livelli | colonne di livelli (profondità dell'acqua) invece che di abbassamenti |
| **Raggruppa le letture in gradini** | spunta | solo per i gradini: una lettura per riga del datalogger |

L'anteprima mostra il numero di letture (e, per i gradini, di gradini), come ha letto i tempi, il contenuto e l'unità di ogni colonna,
le **prime righe come verranno salvate** (tempo in h:mm:ss e nell'unità della tabella) e gli avvisi.

!!! example "Esempio"
    Letture di pompaggio con tempi in minuti, il pozzo e un piezometro:

    ```text
    t (min)	s pozzo (m)	s P1 (m)
    1	0,42	0,05
    2	0,58	0,09
    ```

    Gradini dal datalogger, con data e ora:

    ```text
    Data	Ora	Q (l/s)	s pozzo (m)	s P1 (m)
    12/03/2026	10:00	2	0,85	0,21
    ```

### Come legge il testo

- **Separatore**: tabulazione (copia da Excel), poi punto e virgola, poi spazi o virgola. Con la virgola come separatore il decimale
  deve essere il punto.
- **Intestazione**: le righe prima della prima riga di dati. Righe di testo in mezzo ai dati si ignorano, con un avviso.
- **Celle**: numeri, ore (`h:mm` o `h:mm:ss`), date (`gg/mm/aaaa`, `gg-mm-aaaa`, `gg.mm.aaaa`, `aaaa-mm-gg` e varianti) o data e ora
  nella stessa cella.
- **Colonne**, dall'intestazione: *portata* (Q, portata, flow… o un'unità come l/s), *tempo* (t, tempo, time, ora, orario, trascorso,
  durata…), *data*, *livello* (livello, profondità, soggiacenza, depth, level…; si trasformano in abbassamenti), altrimenti
  *abbassamento*. Senza intestazione la prima colonna di numeri è il tempo e le altre sono abbassamenti.
- **Unità** dall'intestazione: per i tempi s, min, h (anche secondi, minuti, ore); per le portate l/s, m³/h (anche mc/h), l/min,
  m³/s; per gli abbassamenti cm e mm, altrimenti m. Senza unità i tempi sono in **minuti** e le portate in **l/s**, con un avviso.
- **Ore dell'orologio contro tempi trascorsi** (*da riconoscere*): con una data sono ore dell'orologio; poi decide l'intestazione
  (*trascorso*, *durata* contro *ora*, *orario*); i numeri semplici sono tempi trascorsi; valori `h:mm:ss` sono ore dell'orologio se
  tornano indietro (mezzanotte) o se la prima lettura è oltre un'ora con passo fitto (08:30, 08:31…).
- **Ore dell'orologio**: il tempo trascorso è l'ora meno l'**Inizio del pompaggio**. Senza data, un'ora minore della precedente è il
  giorno dopo. Le letture prima dell'inizio si scartano, con un avviso.
- **Livelli**: s = L − L~0~, con L~0~ il **Livello statico** indicato; altrimenti l'ultima lettura a pompa ferma (prima dell'inizio),
  altrimenti la prima lettura. L'avviso dice quale.
- **Serie**: una colonna va al piezometro il cui nome o sigla sta nell'intestazione, oppure al pozzo con *pozzo*, *well* o *PW*; le
  altre, nell'ordine, al pozzo e ai piezometri liberi.

!!! warning "Attenzione"
    Con le ore dell'orologio **devi** indicare l'**Inizio del pompaggio** (o l'**Arresto della pompa** per la risalita). L'anteprima,
    senza, assume la prima lettura come inizio e lo dice; la conferma invece si rifiuta: la prima lettura diventerebbe t = 0 con un
    abbassamento già misurato, che non è possibile.

!!! tip "Suggerimento"
    Incolla sempre la riga d'intestazione con le unità (`t (min)`, `Q (l/s)`, `s P1 (m)`). Senza intestazione e senza colonna di date
    una colonna di portate non si riconosce e verrebbe letta come abbassamento.

**Raggruppa le letture in gradini.** Il datalogger registra una lettura per riga. Con la spunta, per ogni tratto a portata costante
resta l'ultima lettura prima del cambio di portata, come nel programma desktop; i tratti a portata nulla si scartano. Senza spunta
ogni riga incollata diventa un gradino.

Per le letture di pompaggio, se il testo ha una colonna di portata con un solo valore e la **Portata della prova** è vuota, la portata
si scrive anche lì.

## Domande frequenti

**Ho scritto `90` nel tempo e vedo `1:30:00`.**
Con **Tempi in** h:mm:ss un numero vale minuti. Scrivi `90 s` se intendevi secondi, oppure cambia **Tempi in**.

**Perché un gradino non entra nella curva caratteristica?**
Gli mancano la portata o l'abbassamento nel pozzo, o uno dei due non è positivo. Il programma lo dice negli avvisi della curva
caratteristica nei [Risultati](risultati.md).

**La risalita non si calcola.**
Servono la **Portata della prova**, le letture di pompaggio e l'istante dell'arresto: lascia la spunta **Pompa ferma all'ultima lettura di pompaggio** o scrivi
l'arresto.

**I piezometri non compaiono nelle tabelle.**
Si aggiungono nella scheda [Pozzo](pozzo.md), con la loro distanza dal pozzo.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20GeoTheis%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/geotheis/docs/it/prove.md).*
