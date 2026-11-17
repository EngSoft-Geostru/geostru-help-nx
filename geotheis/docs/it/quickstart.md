# Guida rapida (5 minuti)

Arrivi ai risultati e all'anteprima della relazione con l'esempio **CELICO**, che il programma ha già pronto: un pozzo completo in
falda confinata con prova a gradini, prova a portata costante con risalita e due piezometri. Non devi scrivere nessun dato. Con i
tuoi dati i passi sono gli stessi: li trovi per esteso nel [Flusso di lavoro](workflow.md).

## 1. Apri l'esempio

Apri [nx.geostru.ai/geotheis](https://nx.geostru.ai/geotheis/). Nella barra in alto apri il menu **File**: sotto **Apri…** c'è
l'elenco **Esempi con prove**. Scegli **CELICO**, il primo.

Se il progetto a video ha modifiche che non sono in un file, il programma te lo dice: *Il progetto ha modifiche che non sono in un
file: se continui, andranno perse.* Scegli **Salva prima** oppure **Continua senza salvare**.

L'app torna alla scheda **Pozzo** con la striscia *Esempio «CELICO» aperto: è un file del programma desktop, letto come un .wtax.*
Sotto, **Altre note dell'importazione** elenca ciò che il lettore dei file del desktop ha notato: leggile quando apri un tuo
`.wtax`.

!!! note "Nota"
    Gli esempi sono i file del programma desktop GeoTheis. I dati di CELICO sono costruiti per provare il calcolo, non descrivono
    un acquifero reale.

## 2. Guarda il pozzo

Nella scheda **Pozzo** scorri i riquadri a sinistra; a destra la **Sezione del pozzo** è già disegnata.

- **Sito e coordinate**: CELICO non ha una posizione geografica, quindi il pozzo non è sulla mappa. Con un tuo pozzo fai clic sulla
  mappa nel punto del pozzo.
- **Stratigrafia**: gli strati dal piano campagna verso il basso.
- **Pozzo e falda**, linguetta **Falda e quote**: tipo di falda **In pressione**, penetrazione **Completo**, quote in m s.l.m.
  (piano campagna 98, livello statico 93, tetto 91, substrato 84). Nella linguetta **Schema di calcolo** il **Raggio del pozzo**
  r~w~ = 0,5 m.
- **Piezometri**: P1 a 23,5 m e P2 a 42,4 m dall'asse del pozzo.

Sopra la sezione sposta i due cursori **Portata Q** e **Tempo t**: il cono di depressione si muove con loro.

Premi **Prova** in fondo alla pagina.

## 3. Guarda la prova

La scheda **Prova** ha due riquadri:

- **Prova a gradini di portata**: 3 gradini, una riga per gradino con il tempo, la portata e gli abbassamenti nel pozzo e nei
  piezometri;
- **Portata costante e risalita**: la **Portata della prova**, gli **Abbassamenti stabilizzati**, le letture di **Pompaggio** e di
  **Risalita**.

Le portate sono in l/s e i tempi in h:mm:ss. Per vedere le portate di CELICO in m³/h, come nel file del desktop, cambia **Portate
in**: cambia solo la presentazione. Dettagli in [Prove](prove.md).

Premi **Risultati**.

## 4. Leggi i risultati

La scheda **Risultati** calcola da sola tutti i metodi che i dati consentono.

1. In **Risultati della prova** leggi le due colonne: **Metodi calcolati** e **Non applicabili ai dati**, ognuno con il suo motivo.
2. Nel riquadro **Valore di progetto** il programma propone **Theis (fitting automatico)**, con la motivazione: concorda con
   Cooper-Jacob. Il raggio d'azione R = 76,5 m viene dalla retta di Thiem sui piezometri.
3. Nel riquadro **Portata concedibile** trovi Q~c~, Q~ott~ e la portata proposta. In CELICO la proposta è più bassa di
   0,9·Q~c~ perché il livello dinamico non deve scendere sotto il tetto della falda in pressione: la motivazione lo dice.
4. Il **Confronto fra i metodi** segnala che i metodi della prova a gradini danno T molto più alte di quelli della portata
   costante. Apri le linguette dei metodi per vedere i grafici.

Se la proposta ti convince premi **Conferma la proposta**. Tutto ciò che fai in questa scheda è gratuito. La scheda è spiegata in
[Risultati](risultati.md).

Premi **Relazione**.

## 5. Guarda l'anteprima della relazione

La scheda **Relazione** mostra che cosa entra nel documento e, sotto, l'**Anteprima**: è lo stesso testo del Word, con
un'impaginazione indicativa. L'anteprima è gratuita.

**Genera Word** scarica la relazione e consuma crediti; **DXF del pozzo** scarica la sezione del pozzo in DXF, sempre a crediti.
Vedi [Relazione](relazione.md).

## 6. Salva

Il progetto è in sessione e scade dopo 30 minuti di inattività. Per tenerlo usa **File** → **Salva con nome…**: scarichi un file
`.geotheisnx` che riapri con **File** → **Apri…**. In alternativa salvalo su **GeoDropbox**. Vedi [File e GeoDropbox](file.md).

## Passi successivi

Per un tuo pozzo parti da **File** → **Nuovo progetto** e segui il [Flusso di lavoro](workflow.md). I campi della scheda Pozzo
sono descritti in [Pozzo](pozzo.md).

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20GeoTheis%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/geotheis/docs/it/quickstart.md).*
