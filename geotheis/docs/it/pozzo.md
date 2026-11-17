# Pozzo

La scheda **Pozzo** descrive l'opera e il punto in cui sta: posizione e coordinate, terreni attraversati, tipo di falda e quote,
geometria del pozzo, completamento e piezometri. A sinistra ci sono quattro riquadri, nell'ordine:

1. **Sito e coordinate**
2. **Stratigrafia**
3. **Pozzo e falda**, con quattro linguette: **Falda e quote**, **Schema di calcolo**, **Completamento**, **Lavoro**
4. **Piezometri**

A destra la **Sezione del pozzo** si ridisegna mentre scrivi.

Al calcolo servono pochi dati: il **tipo di falda**, le **quote** dell'acquifero, il **raggio del pozzo** e la **distanza** di
ogni piezometro. Gli altri dati servono al disegno, alla relazione e ai controlli sulla portata concedibile.

## Come si salvano i dati

Non c'è un pulsante «Salva» nei riquadri: ogni campo si salva da solo nella sessione. Una scelta, una casella o una tendina si
salvano subito; un testo dopo una breve pausa nella digitazione. Accanto al titolo del riquadro leggi lo stato: *Salvataggio…*,
*Salvato · hh:mm* oppure *Non salvato*.

- I numeri si scrivono con la virgola o con il punto decimale.
- Un valore che non è un numero resta in rosso con *Non è un numero leggibile: non salvato.*
- Spessori, distanze, diametri, raggio, profondità e lunghezze non possono essere negativi: un valore negativo resta in rosso con
  *Non può essere negativo: non salvato.* Le quote in m s.l.m. possono essere negative.
- Un campo vuoto è un dato non indicato, non uno zero.

!!! warning "Attenzione"
    *Salvato* vuol dire salvato nella sessione sul server, che scade dopo 30 minuti di inattività. Per conservare il progetto
    salvalo in un file `.geotheisnx` o su GeoDropbox: vedi [File e GeoDropbox](file.md).

## Sito e coordinate

Il riquadro mette il pozzo sulla mappa e ne dà le coordinate in tutti i sistemi. La posizione non entra nel calcolo dei parametri:
serve alla relazione (mappa, coordinate, pozzi vicini), alle distanze dei piezometri e al collegamento con le altre app NX.

### Mappa

Sopra la mappa:

- **Cerca un luogo (comune, via, località)** + **Cerca** centra la mappa sul luogo trovato. Il pozzo non si sposta: *Mappa centrata
  su …. Il pozzo non si è spostato: fai clic nel punto esatto per posizionarlo.*
- **Posizione GPS** posiziona il pozzo con il GPS del dispositivo e riporta la precisione dichiarata (±… m).
- **Un clic sulla mappa** sceglie che cosa fa il clic: **solo navigazione**, **posiziona il pozzo** oppure **posiziona il
  piezometro** (con la tendina del piezometro da posizionare).
- **Stradale** e **Satellite** cambiano la base cartografica.

Finché il pozzo non è sulla mappa il clic è già in modalità **posiziona il pozzo**; dopo il primo clic torna a **solo
navigazione**, così non sposti il pozzo per errore. Il pozzo e i piezometri si possono anche **trascinare** sulla mappa.

La legenda sotto la mappa riporta il **pozzo**, i **piezometri**, i **pozzi censiti ISPRA**, il cerchio tratteggiato del raggio di
ricerca dei pozzi vicini e, quando c'è, il cerchio del raggio d'azione: *R di progetto = … m*, con l'origine (*confermato*,
*proposto dal programma* o *presunto*).

### Posizione, comune e quota

Quando il pozzo è sulla mappa il riquadro **Pozzo** mostra la posizione in gradi sessagesimali e il sistema in cui le coordinate
sono state date. Il programma propone poi:

- **Comune**, **Provincia** e **Località** dal servizio Nominatim (OpenStreetMap), **solo nei campi vuoti**. Se il punto risulta in
  un altro comune compare *Dal punto risulta …* con il pulsante **Usa**. I tre campi si scrivono anche a mano.
- La **Quota del terreno dal DTM**: TINITALY (INGV) a 10 m; se non risponde, Copernicus GLO-90 a 90 m, meno precisa.

Sotto la quota del DTM c'è la **Quota del piano campagna (dato del progetto)**, cioè il campo **Piano campagna** della linguetta
**Falda e quote**, con la differenza dal DTM. La quota del DTM è solo una proposta: il dato di rilievo del progetto vince e cambia
solo se premi **Usa la quota del DTM**. Se un servizio non risponde, **Riprova quota e comune** ripete la richiesta.

!!! note "Nota"
    La quota del DTM è un valore medio della cella del modello. Per una livellazione serve il rilievo.

### Coordinate da inserire

Per posizionare un punto dalle coordinate:

1. **Punto**: il **Pozzo** o uno dei piezometri;
2. **Sistema**: uno dei sistemi della tabella sotto;
3. **Est (m)** e **Nord (m)**, oppure **Longitudine** e **Latitudine** per i sistemi geografici;
4. **Posiziona**.

| Sistema | EPSG |
|---|---|
| WGS84 geografiche | 4326 |
| WGS84 / UTM fuso 32N, 33N, 34N | 32632, 32633, 32634 |
| ETRS89 / UTM fuso 32N, 33N, 34N | 25832, 25833, 25834 |
| RDN2008 / UTM fuso 32N, 33N, 34N | 6707, 6708, 6709 |
| Roma40 / Gauss-Boaga fuso Ovest, fuso Est | 3003, 3004 |
| ED50 / UTM fuso 32N, 33N, 34N | 23032, 23033, 23034 |
| Roma40 (Monte Mario) geografiche, Greenwich | 4265 |
| ED50 geografiche | 4230 |

Per i sistemi geografici puoi scrivere gradi decimali o gradi primi secondi (ad esempio `38°04'08" N`). Il sistema d'origine resta
nel progetto e la relazione lo riporta.

Il programma controlla le coordinate prima di posizionare il punto:

- *Est maggiore di Nord: sembrano scambiati. In Italia il Nord vale da 4 a 5,2 milioni di metri.*
- *Il punto è fuori dall'Italia: controlla sistema e cifre delle coordinate.*
- *Il punto è a più di 9° dal meridiano centrale del sistema: la conversione perde precisione (oltre il centimetro).*

### Il pozzo in tutti i sistemi

La tabella riporta il pozzo in ogni sistema, con **Est / Lon**, **Nord / Lat** e la **Trasformazione** di datum usata. In testa ci
sono i sistemi del fuso in cui cade il pozzo; gli altri stanno in **Fusi vicini e altri sistemi**, segnati *fuori fuso* o *oltre il
limite di precisione*.

La conversione usa 7 parametri EPSG: l'errore è dell'ordine del metro, fino a qualche metro (Sicilia e Sardegna hanno parametri
propri; ED50 fino a circa 10 m). La conversione ufficiale IGM usa i grigliati.

### Posizione dei piezometri

La tabella confronta, per ogni piezometro, la distanza scritta nel riquadro **Piezometri** (**r scritta**) con quella che risulta
dalle coordinate (**r dalle coordinate**), con l'**Azimut** da nord e lo **Stato**:

| Stato | Significato |
|---|---|
| **non sulla mappa** | il piezometro non ha coordinate |
| **manca il pozzo** | il piezometro è sulla mappa ma il pozzo no: posiziona prima il pozzo |
| **r da completare** | non c'era una distanza scritta: il programma la scrive dalle coordinate |
| **coerente** | le due distanze differiscono al più di 1 m |
| **da scegliere** | le due distanze differiscono di più di 1 m: scegli tu quale vale |

Con lo stato **da scegliere** hai due pulsanti:

- **Usa r dalle coordinate**: la distanza del piezometro diventa quella calcolata;
- **Sposta alla r scritta**: il piezometro si sposta sulla mappa alla distanza scritta, sullo stesso azimut.

**Togli dalla mappa** toglie le coordinate del piezometro; la distanza scritta resta. Una distanza già scritta non si sovrascrive
mai senza una tua scelta.

Un piezometro si posiziona in tre modi: clic sulla mappa in modalità **posiziona il piezometro**, coordinate in **Coordinate da
inserire**, oppure **Da distanza e azimut**: scegli il piezometro, scrivi **Distanza dal pozzo (m)** e **Azimut da nord (°)** e premi
**Posiziona**. Distanze e azimut si calcolano sull'ellissoide WGS84 (formule di Vincenty).

### Pozzi censiti nei dintorni

Il riquadro **Pozzi censiti nei dintorni (ISPRA, L. 464/84)** cerca le perforazioni dell'archivio nazionale entro il **Raggio (m)**
scelto (da 50 a 2 000 m, 500 m all'apertura). La ricerca parte quando posizioni il pozzo; **Cerca** la ripete. La tabella riporta
**Distanza**, **Opera**, **Profondità**, **Acqua**, **Stratigrafia**, **Comune** e il collegamento alla **Scheda** ISPRA.

!!! warning "Attenzione"
    L'archivio L. 464/84 è incompleto: «nessun pozzo censito» non vuol dire «nessun pozzo». I pozzi fuori archivio stanno nei
    catasti e nei geoportali regionali.

### Controlla con una seconda fonte

In **Controlla con una seconda fonte** scrivi le coordinate dello stesso pozzo prese da un'altra fonte (relazione, GPS di una foto,
catasto), con il loro **Sistema** e una **Soglia (m)** (10 m all'apertura), e premi **Confronta**. Il programma dice se le due
posizioni stanno entro la soglia. Se lo scarto è fra 40 e 300 m, tipico della differenza fra datum (Roma40 o ED50 contro WGS84),
aggiunge che una delle due coordinate potrebbe essere stata scritta nel sistema sbagliato. Il confronto non modifica il progetto.

### Collegamenti con le altre app NX

**Fascicolo del sito con Atlante**, in alto nel riquadro, apre Atlante NX sul punto del pozzo: geologia, vincoli, pericolosità e
tavole con i riferimenti.

Se arrivi a GeoTheis NX da un'altra app NX (Atlante, Hydrogeo, Maps) con un punto, compare una striscia che propone la posizione:
**Usa questo punto** o **Ignora**. Se il pozzo ha già una posizione diversa, la striscia dice a quanti metri sta il nuovo punto. Il
punto non si applica mai da solo.

## Stratigrafia

Gli strati si danno **dal piano campagna verso il basso**, uno per riga, con il loro spessore. La stratigrafia **non entra nel
calcolo**: serve al disegno della sezione e alla relazione.

| Colonna | Unità | Che cosa scrivi |
|---|---|---|
| **Terreno** | — | il terreno dal catalogo; decide il retino del disegno |
| **Descrizione** | — | testo libero (fino a 400 caratteri) |
| **Spessore** | m | spessore dello strato, non negativo |
| **Da – a** | m | profondità di tetto e letto dello strato: la calcola il programma dagli spessori |
| **Colore** | — | spunta la casella per usare un colore proprio al posto del retino del terreno |

I terreni del catalogo sono: Sabbia pulita, Sabbia limosa, Sabbia argillosa, Sabbia limoso-argillosa, Sabbia ghiaiosa, Ghiaia
sabbiosa, Ghiaia, Limo, Limo sabbioso, Limo argilloso, Limo sabbioso-argilloso, Argilla, Terreni organici, Roccia, Altro.

**Aggiungi strato** aggiunge una riga in fondo; la **×** a destra la toglie. In testa al riquadro leggi il numero di strati e lo
spessore totale.

Se apri un file del programma desktop con un terreno che non è nel catalogo, la riga mostra *dal desktop: «…»* e il terreno è
**Altro**: scegli il terreno più vicino perché il disegno usi il retino giusto.

## Pozzo e falda

Il riquadro ha quattro linguette. Si apre sull'ultima che hai usato.

### Falda e quote

**Tipo di falda** decide quali metodi di calcolo si applicano. Finché non lo scegli compare *Il tipo di falda non è ancora scelto:
serve a decidere quali metodi di calcolo si applicano.*, e nei Risultati i metodi assumono la falda confinata.

| Scelta | Significato |
|---|---|
| **Libera** | freatica: la superficie dell'acqua è a pressione atmosferica e si abbassa pompando |
| **In pressione** | artesiana (confinata): chiusa fra due strati impermeabili, il livello sale sopra il tetto dell'acquifero |
| **Semiconfinata, libera** | sotto uno strato semipermeabile che la alimenta; superficie libera (nel desktop «semilibera») |
| **Semiconfinata, in pressione** | sotto uno strato semipermeabile che la alimenta; in pressione (nel desktop «semiartesiana») |

Il metodo di Hantush si calcola solo con una falda semiconfinata. Vedi [Metodi](metodi.md).

**Penetrazione del pozzo**:

- **Completo**: i filtri attraversano tutto lo spessore dell'acquifero;
- **Incompleto**: i filtri ne attraversano solo una parte; servono **Filtro – substrato** (TSI) e, in pressione, **Cieco fra filtro
  e substrato** (LC), nella linguetta **Schema di calcolo**.

**Costruzione**: **Trivellato** oppure **A scavo (grande diametro)**. Cambia il disegno del pozzo.

**Quote**, in m s.l.m., come nel programma desktop:

| Campo | Sigla | Quando compare | Che cosa è |
|---|---|---|---|
| **Piano campagna** | PC | sempre | quota del terreno al pozzo |
| **Bocca del pozzo** | QTF | sempre | quota della testa del tubo |
| **Livello statico** | LS | sempre | quota del livello dell'acqua a riposo |
| **Tetto impermeabile** | TI | falda in pressione (anche semiconfinata) o non scelta | quota del tetto dell'acquifero confinato |
| **Substrato impermeabile** | SI | sempre | quota della base dell'acquifero |
| **Tetto del semipermeabile** | TSP | falde semiconfinate | quota del tetto dello strato semipermeabile |
| **Letto del semipermeabile** | LSP | falde semiconfinate | quota della base dello strato semipermeabile |

Si mostrano solo le quote che servono al tipo di falda scelto; le altre restano salvate. Dalle quote il programma ricava:

$$
H_1 = LS - SI \qquad b = TI - SI
$$

dove H~1~ è lo spessore saturo (falda libera) e b lo spessore della falda confinata. Le quote servono anche ai controlli sulla
portata concedibile: con la falda in pressione il livello dinamico non deve scendere sotto il tetto. Vedi [Risultati](risultati.md).

### Schema di calcolo

Lo schema è la geometria che usano le formule dei **pozzi singoli**, come nel programma desktop. Resta un dato esplicito, distinto
dal completamento disegnato: le due cose possono non coincidere.

| Campo | Sigla | Unità | Quando compare | Che cosa è |
|---|---|---|---|---|
| **Raggio del pozzo** | r~w~ | m | sempre | raggio usato nel calcolo (non il diametro) |
| **Profondità totale** | — | m | sempre | dal piano campagna, per il disegno |
| **Cieco fra bocca e filtro** | LFC | m | sempre | lunghezza del tubo cieco sopra il filtro, misurata dalla bocca del pozzo |
| **Lunghezza del filtro** | LTF | m | sempre | lunghezza del tratto filtrante |
| **Filtro – substrato** | TSI | m | pozzo incompleto | distanza fra il fondo del filtro e il substrato |
| **Cieco fra filtro e substrato** | LC | m | pozzo incompleto in pressione (anche semiconfinata) | tratto cieco sotto il filtro |

Il raggio del pozzo serve anche all'abbassamento nel pozzo e al cono di depressione.

**Proponi il completamento dallo schema** compila la colonna cieca, il filtro e la perforazione della linguetta **Completamento** a
partire dallo schema; intercapedine, avampozzo, pompa e livelli restano come sono. Servono la quota del piano campagna, quella della
bocca e la lunghezza del filtro. Se la colonna c'è già, il programma chiede conferma: *La colonna e la perforazione attuali saranno
sostituite da quelle proposte dallo schema.* → **Sostituisci** o **Annulla**.

### Completamento

Il completamento descrive il pozzo **come è stato costruito**, per il disegno e la relazione. Le profondità sono in m dal piano
campagna, positive verso il basso; i diametri in mm. Ogni tabella ha il suo pulsante **Aggiungi tratto** (o **Aggiungi livello**) e
la **×** per togliere la riga.

**Perforazione**: un tratto per diametro di perforazione.

| Colonna | Unità |
|---|---|
| **Da**, **A** | m dal p.c. |
| **Diametro** | mm |

**Colonna: cieco, filtri, decantatore**: i tratti della colonna di rivestimento, anche con più filtri.

| Colonna | Unità | Note |
|---|---|---|
| **Tipo** | — | **Cieco**, **Filtro** o **Decantatore** |
| **Da**, **A** | m dal p.c. | |
| **Ø esterno** | mm | diametro esterno del tubo |
| **Parete** | mm | spessore della parete |
| **Materiale** | — | testo libero |
| **Tipo di filtro** | — | solo per i tratti **Filtro** |
| **Luce** | mm | apertura del filtro, solo per i tratti **Filtro** |

**Intercapedine**: lo spazio fra perforazione e colonna.

| Colonna | Unità | Note |
|---|---|---|
| **Tipo** | — | **Cementazione**, **Tampone impermeabile** o **Dreno** (proposto per una riga nuova) |
| **Da**, **A** | m dal p.c. | |
| **Materiale o nota** | — | testo libero |

**Avampozzo** e **Pompa** si attivano con la loro casella; senza spunta i campi restano ma non si usano.

| Avampozzo | Unità |
|---|---|
| **Profondità del fondo** | m |
| **Diametro** | mm |

| Pompa | Unità | Note |
|---|---|---|
| **Profondità dell'aspirazione** | m dal p.c. | entra nel controllo della portata concedibile |
| **Portata nominale** | l/s | |
| **Potenza** | kW | |
| **Descrizione** | — | testo libero |

La profondità dell'aspirazione non è solo un dato del disegno: la portata concedibile proposta tiene l'aspirazione almeno 1 m sotto
il livello dinamico. Vedi [Risultati](risultati.md).

**Livelli misurati**: le misure di livello nel pozzo, per il disegno e la relazione.

| Colonna | Unità | Note |
|---|---|---|
| **Tipo** | — | **Statico** o **Dinamico** |
| **Profondità** | m dal p.c. | |
| **Data** | — | testo libero |
| **Nota** | — | testo libero |

!!! note "Nota"
    Il livello statico che usa il calcolo è la quota **Livello statico** (LS) della linguetta **Falda e quote**, in m s.l.m. I
    livelli misurati del completamento servono al disegno e alla relazione.

### Lavoro

I dati del lavoro vanno nella relazione; nessuno entra nel calcolo.

| Campo | Note |
|---|---|
| **Committente** | |
| **Opera o uso del pozzo** | ad esempio irriguo, industriale, acquedotto |
| **Data della prova** | testo libero |
| **Ditta esecutrice** | |
| **Tecnico responsabile** | |
| **Descrizione** | testo libero |
| **Note** | testo libero |

## Piezometri

Un piezometro per riga. La **distanza r dall'asse del pozzo** è l'unico dato del piezometro che entra nel calcolo; quote e filtro
servono al disegno.

| Colonna | Unità | Che cosa è |
|---|---|---|
| **Nome** | — | il nome che compare in tabelle, grafici e relazione (fino a 40 caratteri) |
| **Distanza** | m | distanza r dall'asse del pozzo, non negativa |
| **Quota p.c.** | m s.l.m. | quota del piano campagna al piezometro |
| **Quota bocca** | m s.l.m. | quota della testa del piezometro |
| **Profondità** | m | profondità del piezometro |
| **Filtro da**, **Filtro a** | m | tratto filtrante |
| **Mappa** | — | *posizionato* se il piezometro ha le coordinate, altrimenti — |

Accanto al nome c'è un identificativo (P1, P2…) che il programma assegna da solo: le letture della prova sono legate a questo, non
alla riga della tabella. Se lasci il nome vuoto, prende l'identificativo.

**Aggiungi piezometro** aggiunge una riga. La **×** toglie il piezometro dopo una conferma: *Togliere …? Si perdono anche le sue
letture nella prova.* Le letture degli altri piezometri restano al loro posto.

La posizione sulla mappa si dà nel riquadro **Sito e coordinate**. Se il pozzo e il piezometro sono sulla mappa, la distanza si
ricava dalle coordinate solo quando non l'hai scritta tu; altrimenti scegli tu quale vale (vedi [Posizione dei
piezometri](#posizione-dei-piezometri)).

Senza piezometri compare *Nessun piezometro: la prova si elabora sul solo pozzo.* Dal solo pozzo di emungimento si ricava T, ma
non S in modo affidabile. Vedi [Metodi](metodi.md).

## Dati da verificare

Dopo ogni salvataggio il programma controlla che i dati del riquadro **Pozzo e falda** stiano in piedi. Se qualcosa non torna,
in testa al riquadro compare la striscia **Dati da verificare**. Non è un rifiuto: i dati restano salvati e il calcolo procede.

| Avviso | Quando |
|---|---|
| *Il livello statico è … m sopra il piano campagna: è un pozzo artesiano zampillante? Altrimenti verificare le quote.* | LS > PC |
| *Il substrato impermeabile è alla quota del livello statico o più in alto: la falda non avrebbe spessore saturo. Verificare le quote.* | SI ≥ LS |
| *Il tetto dell'acquifero non è sopra il substrato: lo spessore b = TI − SI sarebbe nullo o negativo. Verificare le quote.* | falda in pressione, TI ≤ SI |
| *Il tetto dell'acquifero è sopra il piano campagna: verificare le quote.* | falda non libera, TI > PC |
| *Il tetto dello strato semipermeabile non è sopra il suo letto: verificare le quote.* | falda semiconfinata, TSP ≤ LSP |
| *Il raggio del pozzo è nullo: serve per l'abbassamento nel pozzo e per il cono di depressione.* | r~w~ = 0 |
| *Raggio del pozzo di … m: è il raggio, non il diametro? (in metri)* | r~w~ > 5 m |
| *La bocca del pozzo è più di 5 m sotto il piano campagna: verificare le quote.* | QTF < PC − 5 m |

Gli stessi controlli, per le letture, compaiono nella scheda Prova. Vedi [Prove](prove.md).

## Sezione del pozzo

A destra della scheda la **Sezione del pozzo** si compone sul server a ogni salvataggio: stratigrafia con i retini, perforazione,
colonna con filtri e decantatore, intercapedine, avampozzo, pompa, livelli, tetto e substrato dell'acquifero, strato
semipermeabile, piezometri e cono di depressione. I piezometri sono proiettati sul piano della sezione alla loro distanza dal
pozzo; la larghezza del pozzo è fuori scala e la nota sotto il disegno dice di quanto.

Comandi:

- **Portata Q** e **Tempo t**: due cursori che muovono il cono di depressione. Funzionano quando ci sono T e S (o i risultati della
  prova).
- **Distanze**: scala **Log** o **Lineare** per le distanze dal pozzo.
- Rotella per lo zoom, trascina per spostare; **Adatta** (o doppio clic sul disegno) torna alla vista intera.
- **PNG**: immagine della sezione, gratuita.
- **DXF**: la sezione in DXF, in metri, a layer. Consuma crediti; se il DXF non si genera non si paga.

Il cono si disegna con i valori di progetto in uso e la portata di esercizio, come spiegato in [Risultati](risultati.md#cono-di-depressione).

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20GeoTheis%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/geotheis/docs/it/pozzo.md).*
