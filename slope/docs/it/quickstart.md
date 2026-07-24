---
title: Guida rapida — Slope NX
---

# Guida rapida (5 minuti)

Verifichiamo un pendio dall'inizio alla lettura del fattore di sicurezza. Ti servono solo il browser e il profilo del versante.

## 1. Apri l'app

Vai su **[nx.geostru.ai/slope](https://nx.geostru.ai/slope/)**. Puoi lavorare subito come ospite; per salvare sul cloud accedi con l'account GeoStru.

Trovi tre schede a sinistra — **Input**, **Analisi**, **Output** — e a destra le viste **Sezione 2D**, **Modello 3D**, **Tensioni**, **Relazione**.

## 2. Disegna il profilo topografico

Nel pannello **Input → Profilo topografico** inserisci i vertici del terreno (X, Z) nella tabella, oppure premi **Disegna** e clicca i punti sulla sezione. In alternativa importa un **DXF** o un'immagine da ricalcare.

!!! tip "Parti da un esempio"
    Non hai un profilo a portata di mano? Apri il modale **?** in alto e, nel tab **Risorse**, carica uno **scenario di esempio** (rilevato, invaso, muro): è già pronto per il calcolo.

## 3. Assegna i materiali

In **Materiali geotecnici** premi **+ Aggiungi materiale** e imposta i parametri: peso di volume γ, saturo γ<sub>sat</sub>, coesione efficace c′, angolo di attrito φ′ e, per l'analisi non drenata, la coesione non drenata c<sub>u</sub>.

Il pendio senza contatti è un **unico strato** (il substrato). Per più strati traccia i **contatti stratigrafici** e assegna a ciascuna regione il suo materiale con un **doppio-click** sul poligono.

## 4. Falda, carichi e sismica (se servono)

- **Falda**: disegna la linea piezometrica in *Water table line*.
- **Carichi**: aggiungi un carico distribuito e trascinalo in posizione sulla sezione.
- **Sismica**: nel pannello **Analisi** attiva l'analisi sismica e calcola k<sub>h</sub>/k<sub>v</sub> secondo NTC.

## 5. Scegli metodo e normativa

Nel pannello **Analisi**:

- **Condizione di analisi**: *Drenata* (tensioni efficaci) o *Non drenata* (tensioni totali). I nuovi progetti partono in Drenata.
- **Metodo di calcolo**: Bishop, Fellenius, Janbu, Spencer o Morgenstern-Price.
- **Normativa**: NTC 2018, EC7-EC8 o Utente, con i coefficienti parziali della combinazione.

## 6. Definisci la superficie e calcola

Scegli la forma della superficie:

- **Circolari** → premi **Ricerca automatica**: la maglia dei centri si posiziona da sola sopra il pendio.
- **Generica** → assegna i punti o avvia la ricerca automatica.

Premi **Calcola**. In pochi istanti vedi la **superficie critica in rosso** e l'**FS minimo**; nella scheda **Output** trovi le prime superfici in ordine di FS.

!!! tip "Esplora la maglia"
    Passa il mouse sui nodi della maglia per vedere l'FS di ogni centro. **Click** fissa la superficie, **doppio-click** o **Esc** ferma l'esplorazione.

## 7. Leggi e documenta

- Apri **Output** per il verdetto (FS ≥ soglia = verificato) e, con un click, chiedi all'**AI** di spiegare il risultato o di **trovare l'intervento** (es. drenaggio) per raggiungere l'FS di progetto.
- Apri **Relazione** per l'anteprima del documento e scaricala in **Word**.

Fatto: hai verificato il tuo primo pendio. Per il quadro completo prosegui con il **[Flusso di lavoro completo](workflow.md)**.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Slope%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/slope/docs/it/quickstart.md).*
