# Flusso di lavoro

Un progetto completo, nell'ordine delle quattro schede: **Pozzo** → **Prova** → **Risultati** → **Relazione**. Ogni campo si salva
da solo nella sessione mentre scrivi e il calcolo si aggiorna a ogni modifica: non c'è un pulsante «Calcola». Puoi tornare a una
scheda precedente in qualsiasi momento; i risultati seguono i dati.

## 0. Inizia un progetto

Dal menu **File**:

- **Nuovo progetto** svuota la sessione;
- **Apri…** riapre un file `.geotheisnx` di GeoTheis NX oppure un `.wtax` del programma desktop. Con un `.wtax` compare *Progetto
  del programma desktop aperto: controlla i dati prima di calcolare.*, con le note dell'importazione;
- **Esempi con prove** e **Pozzi singoli (portata critica nota)** aprono gli esempi del programma desktop.

Se il progetto a video ha modifiche che non sono in un file, il programma chiede prima se salvarle. Scrivi il **Nome del
progetto** in testa alla pagina (ad esempio *Pozzo P1 — Az. agricola Rossi*): dà il nome al file e alla relazione.

## 1. Scheda Pozzo

I riquadri sono quattro, a sinistra; a destra la **Sezione del pozzo** si ridisegna a ogni salvataggio. Tutti i campi sono
descritti in [Pozzo](pozzo.md).

1. **Sito e coordinate** — Cerca il comune o la via, poi fai clic nel punto esatto del pozzo, oppure usa **Posizione GPS** o scrivi
   le coordinate in uno dei sistemi offerti (WGS84, UTM, Gauss-Boaga, ED50). Il programma propone il comune e la quota del terreno
   dal modello digitale (DTM): la quota del piano campagna del progetto cambia solo se premi **Usa la quota del DTM**. Controlla i
   **Pozzi censiti nei dintorni** (archivio ISPRA). Se hai le coordinate del pozzo da un'altra fonte, confrontale in **Controlla
   con una seconda fonte**.
2. **Stratigrafia** — Uno strato per riga, dal piano campagna verso il basso: terreno, descrizione, spessore. Serve al disegno e
   alla relazione, non al calcolo.
3. **Pozzo e falda** — Quattro linguette:
    - **Falda e quote**: **Tipo di falda**, **Penetrazione del pozzo**, **Costruzione** e le quote in m s.l.m. Il tipo di falda
      decide quali metodi si applicano: sceglilo sempre.
    - **Schema di calcolo**: raggio del pozzo, profondità, cieco fra bocca e filtro, lunghezza del filtro e, per i pozzi incompleti,
      i dati verso il substrato. È ciò che usano le formule.
    - **Completamento**: perforazione, colonna (cieco, filtri, decantatore), intercapedine, avampozzo, pompa, livelli misurati. Per
      partire in fretta premi **Proponi il completamento dallo schema** nella linguetta **Schema di calcolo**.
    - **Lavoro**: committente, opera, data della prova, ditta esecutrice, tecnico, descrizione e note per la relazione.
4. **Piezometri** — Nome e **Distanza** r dall'asse del pozzo per ogni piezometro: la distanza è l'unico dato del piezometro che
   entra nel calcolo. Le quote e il filtro servono al disegno. Senza piezometri la prova si elabora sul solo pozzo, e S non si
   ricava in modo affidabile.

Se qualcosa non torna (livello statico sopra il piano campagna, tetto sotto il substrato, raggio di 5 m…) compare la striscia
**Dati da verificare**. Non blocca nulla: ti chiede di controllare.

## 2. Scheda Prova

Due riquadri, descritti in [Prove](prove.md):

1. **Prova a gradini di portata** — Una riga per gradino, con la lettura di fine gradino: tempo dall'inizio della prova, portata e
   abbassamenti cumulati nel pozzo e nei piezometri. Scegli le unità in **Tempi in** e **Portate in**. Con **Incolla da Excel o
   CSV** copi le colonne da un foglio di calcolo o dal datalogger.
2. **Portata costante e risalita** — **Portata della prova**, **Abbassamenti stabilizzati** (a regime, per Dupuit-Thiem), letture di
   **Pompaggio** (t dall'inizio del pompaggio) e di **Risalita** (t′ dall'arresto della pompa), nel pozzo e nei piezometri.

Se non hai la prova a gradini ma conosci la portata critica del pozzo, compila il riquadro **Portata critica nota (senza prova a
gradini)**: insieme alla geometria del pozzo serve ai metodi dei pozzi singoli, che danno T e K indicativi.

## 3. Scheda Risultati

1. Leggi **Metodi calcolati** e **Non applicabili ai dati**: un metodo che manca ha il motivo scritto accanto.
2. Controlla il **Confronto fra i metodi** e gli **Scarti da verificare**.
3. Apri le linguette dei metodi. Sui grafici escludi le letture anomale con un clic, restringi l'intervallo di Cooper-Jacob,
   ritocca la curva tipo di Theis o Hantush se serve.
4. Con la prova a gradini scegli la **portata critica** sulla curva caratteristica.
5. Conferma il **Valore di progetto** (T, K, S, R) e la **Portata concedibile**, oppure scegli un altro metodo o scrivi la portata di
   esercizio.

Tutto è gratuito. I dettagli sono in [Risultati](risultati.md); i metodi e le loro ipotesi in [Metodi](metodi.md).

## 4. Scheda Relazione

1. Leggi **Che cosa entra nella relazione**: ogni voce dice se il dato c'è (posizione, stratigrafia, gradini, portata costante,
   piezometri).
2. Controlla l'**Anteprima**, gratuita: è lo stesso testo del Word.
3. **Genera Word** per scaricare la relazione, **DXF del pozzo** per la sezione in DXF: entrambi consumano crediti.
4. In **Prosegui con le altre app NX** invia il pozzo a GeoDropbox, apri la sezione in CAD Tools o il fascicolo del sito in
   Atlante.

Vedi [Relazione](relazione.md).

## 5. Salva

Il progetto vive in sessione e scade dopo 30 minuti di inattività. Salvalo con **File** → **Salva** (Ctrl+S) o **Salva con nome…**
(Ctrl+Shift+S) in un file `.geotheisnx`, oppure su **GeoDropbox**. Vedi [File e GeoDropbox](file.md).

!!! tip "Suggerimento"
    L'**Assistente** in alto legge il progetto e i risultati e può inserire dati per te: letture incollate, stratigrafia,
    piezometri, coordinate del pozzo. Ogni messaggio consuma crediti. Vedi [Assistente](assistente.md).

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20GeoTheis%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/geotheis/docs/it/workflow.md).*
