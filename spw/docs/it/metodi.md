# Metodi di calcolo

Questa pagina spiega cosa fanno i metodi, quando usarli e quali limiti hanno. Non riporta le equazioni del motore. Per la teoria completa usa i riferimenti bibliografici in fondo.

## LEM: equilibrio limite

Il metodo all'equilibrio limite studia l'equilibrio della paratia sotto le azioni del terreno, dell'acqua, dei carichi e dei supporti. È rivolto soprattutto alla scelta o alla verifica dell'infissione e alle sollecitazioni di schemi semplici.

**Quando usarlo**

- per una valutazione dell'infissione;
- per paratie a sbalzo o con un ordine di supporti;
- per un confronto preliminare con il FEM.

**Ipotesi e limiti**

Il comportamento del terreno è rappresentato attraverso condizioni limite di spinta. Il metodo non descrive in modo completo la deformabilità della paratia e l'interazione con il terreno. Non è la scelta adatta quando gli spostamenti e la storia deformativa governano il progetto.

**Cosa restituisce**

- momento, taglio e sforzo normale lungo la paratia;
- l'infissione di progetto;
- le forze nei supporti.

Il LEM non calcola gli spostamenti: il diagramma della deformata indica «Dato non disponibile» e la verifica SLE resta non calcolata. Le opzioni FEM del passo Calcolo non hanno effetto.

## FEM: paratia su molle

Il metodo a elementi finiti rappresenta la paratia come un elemento flessionale e il terreno come un insieme di reazioni cedevoli. I tiranti, i puntoni e gli altri vincoli contribuiscono alla risposta secondo la loro rigidezza e la fase di installazione.

**Cosa restituisce**

- spostamenti lungo la paratia;
- momento, taglio e sforzo normale;
- pressioni e mobilitazione del terreno;
- forze nei supporti;
- risposta alle singole fasi e combinazioni.

**Analisi lineare e non lineare**

Nell'analisi lineare la risposta del terreno non cambia con il livello di spostamento. Quella non lineare limita la reazione quando il terreno raggiunge la condizione prevista dal modello. Serve quando vuoi rappresentare la mobilitazione della resistenza in modo più realistico.

**Discretizzazione e convergenza**

Il numero di elementi controlla il dettaglio lungo la paratia. Iterazioni massime e tolleranza controllano la convergenza. Il limite del tratto lineare, la riduzione della molla al fondo scavo e il cedimento associato al modulo di reazione descrivono la risposta del terreno.

Cambia questi dati con criterio. Un calcolo non convergente o con una discretizzazione inadeguata non è una base sufficiente per il progetto.

## Spinte del terreno

Le opzioni disponibili comprendono Coulomb, Müller–Breslau, Caquot–Kérisel, Rankine e la condizione a riposo di Jaky dove prevista.

- **Coulomb** considera l'equilibrio di un cuneo e l'attrito fra terreno e parete.
- **Müller–Breslau** è una formulazione della stessa famiglia per condizioni geometriche più generali.
- **Caquot–Kérisel** usa una trattazione e tabelle note per la spinta passiva e l'attrito terra-parete.
- **Rankine** è adatto alle ipotesi più semplici di parete e superficie del terreno.
- **Jaky** descrive la condizione di pressione a riposo nei casi previsti.

La scelta deve essere coerente con geometria, attrito terra-parete, drenaggio e spostamenti attesi. La resistenza passiva è particolarmente sensibile a queste ipotesi.

## Sisma

L'opzione **Mononobe–Okabe** estende il modello della spinta all'azione pseudo-statica. L'opzione **Strutture senza spostamenti** riguarda gli schemi per i quali non è ammesso il meccanismo deformativo associato alla spinta attiva.

Il punto della sovraspinta sismica può essere posto a un terzo, a metà oppure a due terzi dell'altezza secondo lo schema scelto.

I parametri del sito derivano da posizione, vita nominale, classe d'uso, sottosuolo e topografia. Per le paratie valgono le prescrizioni specifiche delle NTC 2018. Il modello sismico è applicato solo alle combinazioni che lo prevedono.

**Limiti:** controlla che il metodo sia compatibile con il tipo di terreno, la presenza d'acqua e gli spostamenti ammessi. Non estendere automaticamente un modello per pareti libere a una struttura fortemente vincolata.

## Falda, sifonamento e sollevamento

La falda modifica il peso efficace del terreno e introduce pressioni dell'acqua. Quote diverse a monte e a valle possono produrre un flusso attraverso il terreno.

- Il regime **idrostatico** considera i livelli senza descrivere il campo di flusso.
- Il regime di **filtrazione** rappresenta gli effetti del flusso con le approssimazioni dichiarate dal programma.
- La verifica **HYD · sifonamento** valuta la sicurezza contro l'erosione interna legata al flusso.
- La verifica **UPL · sollevamento** riguarda l'equilibrio del fondo scavo sotto la pressione dell'acqua.

Una combinazione idraulica può non avere diagrammi strutturali: in quel caso restituisce i fattori delle verifiche idrauliche. Controlla sempre i dati di permeabilità e il regime assegnato.

## Tiranti e puntoni

Un **tirante attivo** riceve un precarico. Un **tirante passivo** reagisce agli spostamenti successivi alla sua installazione. Lunghezza libera, bulbo, armatura, interasse e durata influenzano la risposta e le verifiche.

Un **puntone** lavora prevalentemente a compressione. La rigidezza può essere assegnata oppure proposta dai dati geometrici e del materiale.

Le verifiche dei tiranti comprendono lo sfilamento e la resistenza dell'acciaio. Per i puntoni è disponibile la verifica di resistenza; l'instabilità non è verificata e richiede un controllo separato.

## Verifiche strutturali e armature

Le verifiche STR riguardano flessione e taglio delle sezioni in c.a. e delle sezioni miste previste. Gli sforzi per metro di paratia sono riferiti all'elemento secondo interasse o larghezza.

Il progetto conserva le azioni concomitanti della stessa condizione. L'armatura esecutiva deriva dalle richieste lungo la paratia e dalle regole geometriche inserite.

Sono fuori dal perimetro attuale la verifica di instabilità dei puntoni, la stabilità globale, il carico limite verticale e le verifiche SLE delle sezioni.

## Bibliografia essenziale

- Blum, H., *Einspannungsverhältnisse bei Bohlwänden*, 1931.
- Coulomb, C. A., *Essai sur une application des règles de maximis et minimis*, 1776.
- Rankine, W. J. M., *On the Stability of Loose Earth*, 1857.
- Caquot, A.; Kérisel, J., *Tables for the Calculation of Passive Pressure, Active Pressure and Bearing Capacity of Foundations*, 1948.
- Mononobe, N.; Matsuo, H., 1929; Okabe, S., 1926, per il metodo pseudo-statico delle spinte.
- Winkler, E., *Die Lehre von der Elasticität und Festigkeit*, 1867, per il modello su reazioni cedevoli.
- NTC 2018, in particolare §6.5, §6.6 e §7.11.6.3.
- EN 1997-1, Eurocodice 7, per gli approcci alle verifiche geotecniche.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/spw/docs/it/metodi.md).*
