# Domande frequenti

## Tracce e formati

**Quali file di tracce posso caricare?**
SEG-2, SEG-Y, SU (Seismic Unix), Ambrogeo (`.dta`), SARA Doremi (`.drm`), Dolang e ASCII con
le tracce in colonna, fino a 64 MB per file e 512 tracce per progetto. I progetti `.mswx` di
Easy-MASW desktop si aprono con **File → Apri…**. Vedi [Tracce](tracce.md#importa-tracce).

**Il mio formato non è fra quelli. Che cosa faccio?**
Esporta le tracce dal software dello strumento in SEG-2, SEG-Y o in un file di testo con una
colonna per traccia. Se hai già la curva di dispersione, puoi anche incollarla direttamente
nella tabella del picking.

**Ho registrato due stendimenti sfalsati di mezzo passo. Come li unisco?**
Carica il primo, poi scegli **Interponi** in **Aggiungi** e carica il secondo: le tracce si
alternano. Poi dimezza dx nella card **Acquisizione**.

**Ho più colpi sulla stessa geometria. Posso sommarli?**
Sì: carica il primo, poi scegli **Somma** e carica gli altri, uno alla volta. Le tracce si
sommano campione per campione (stacking).

**Una traccia è rumorosa o morta.**
Togli la spunta **Usa nello spettro** nella sua riga: lo spettro la ignora, e la fase tiene
conto della posizione reale degli altri geofoni.

**Ho caricato il file sbagliato.**
**Annulla** (Ctrl+Z) nella card **Tracce** torna allo stato precedente. Per ricominciare da
capo c'è **Rimuovi tutte**.

## Spettro e picking

**La mappa è tutta rossa alle basse frequenze.**
Ogni colonna è normalizzata al suo massimo: dove il segnale è scarso anche il rumore
diventa «rosso». Alza **f min** al limite inferiore utile dei geofoni (spesso 3–5 Hz) e
ricalcola.

**Il picking automatico ha saltato un tratto, o ha messo un tratto sul modo sbagliato.**
È normale: segue le creste che vede. Completa a mano con **Aggiungi**, sposta i punti con
**Sposta**, cambia il modo di un punto dalla tabella. Il [modello sintetico](spettri.md#modello-sintetico)
aiuta a capire quale cresta è il fondamentale e guida l'assegnazione automatica dei modi.

**Come capisco se una cresta è un modo superiore?**
Un modo superiore sta a velocità più alte del fondamentale alla stessa frequenza e compare di
solito alle frequenze alte, dove il fondamentale perde energia. Il confronto con le curve del
modello sintetico e un salto brusco della cresta verso l'alto sono gli indizi più utili.

**Quanto in profondità arriva l'indagine?**
Dell'ordine di metà della lunghezza d'onda più lunga del picking affidabile. Muovi il cursore
sulla mappa: la riga in fondo riporta λ = v/f.

**Ho perso il picking per un errore.**
**Annulla** (Ctrl+Z) torna indietro fino a 100 modifiche, finché non cambi scheda.

## Inversione

**Da dove parto con il modello iniziale?**
Da **Proponi strati**: spessori dalle lunghezze d'onda del picking e V~s~ dalla curva. Poi
eventualmente aggiusta i limiti dove hai informazioni (un sondaggio, la profondità della
falda).

**Ogni volta che rifaccio l'inversione il profilo cambia un po'.**
È atteso: la ricerca parte da punti casuali e l'inversione non è unica. Se profili diversi
hanno misfit simili, il picking non basta a distinguerli: confronta le soluzioni con
**Ordina per** e scegli la più plausibile.

**Che cosa vuol dire «Modi da visualizzare»?**
Quante curve teoriche disegnare per la soluzione a video. Non cambia il calcolo:
l'inversione usa sempre tutti i modi del picking.

**L'inversione si è fermata a metà.**
Se hai chiuso la pagina o premuto **Interrompi**, la corsa non è consegnata e non è
addebitata. Se hai cambiato picking o strati durante il calcolo, il risultato è stato
scartato, senza addebito. Rilancia.

**Il pulsante Calcola inversione dice che il calcolo è troppo lungo.**
Il prodotto di iterazioni, punti di picking e strati ha un tetto: riduci uno dei tre.

## Categoria e risultati

**La categoria non compare: «La velocità cade esattamente sul limite fra due categorie».**
V~s,eq~ è esattamente 100, 360 o 800 m/s, un valore che la tabella delle NTC non assegna a
nessuna fascia. Controlla il modello: basta una differenza minima negli strati.

**Perché il desktop dava E e MASW NX dà C sullo stesso progetto?**
Un difetto di arrotondamento del desktop nel calcolo di H: con H = 29,999998 m invece di 30 il
sito risultava con substrato entro 30 m. Vedi
[Differenze dal programma desktop](validazione.md#differenze-dal-programma-desktop).

**Posso usare G~0~ o E per un calcolo di cedimenti?**
Non direttamente: sono moduli dinamici a piccole deformazioni. Vanno ridotti in funzione del
livello di deformazione dell'opera.

**NSPT o Qc compaiono come N/D.**
La V~s~ dello strato porta la correlazione fuori dal suo campo (NSPT oltre 100, Qc oltre
5 000 kPa). Il semispazio non ha correlazioni perché non ha una profondità media.

**Il peso di volume è in kN/m³ ma nella tabella dei parametri vedo 1800.**
A video i pesi sono in kN/m³; la tabella dei parametri riporta la densità ρ in kg/m³, quella
che entra nelle formule dei moduli (17,65 kN/m³ ↔ 1 800 kg/m³).

## Relazione, file e crediti

**La relazione esce in inglese.**
È scritta nella lingua dell'interfaccia: cambia lingua dal selettore in alto e rigenerala.

**Ho generato due volte la stessa relazione. Ho pagato due volte?**
No: lo stesso documento, con gli stessi dati e la stessa lingua, non si ripaga.

**Ho chiuso il browser e il progetto non c'è più.**
Il progetto vive in sessione per 30 minuti dall'ultima attività. Riapri il `.maswnx` salvato,
o il progetto da GeoDropbox. Vedi [File](file.md).

**Il file salvato non contiene le tracce.**
I campioni superano i 30 MB: il file porta solo i riferimenti alle tracce sul server. Tieni
sempre i file originali dello strumento per ricaricarle.

**Quanto costa un'inversione o una relazione?**
I prezzi sono nel listino su [geostru.ai](https://www.geostru.ai/). Un'operazione che non va a
buon fine non costa nulla. Vedi [Crediti](relazione.md#crediti).

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20MASW%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/masw/docs/it/faq.md).*
