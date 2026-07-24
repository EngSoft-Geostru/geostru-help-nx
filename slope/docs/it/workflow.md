---
title: Flusso di lavoro completo — Slope NX
---

# Flusso di lavoro completo

Questa pagina segue un progetto reale dall'inizio all'esportazione, toccando anche le opzioni avanzate. Segui i pannelli **Input → Analisi → Output** nell'ordine.

## 1. Dati generali

In **Input → Dati generali** compili committente, oggetto, progettista, data e coordinate (lat/lon). Questi campi popolano il **cartiglio** del disegno e l'intestazione della relazione. La card **Formato e scala** definisce foglio, scala orizzontale ed esagerazione verticale.

## 2. Geometria

- **Profilo topografico**: la linea di terreno, per punti (X, Z), disegnata, importata da DXF o ricalcata da un'immagine. Estendi il profilo ai lati con **Estendi profilo** quando serve spazio a valle/monte (utile per la stabilità globale dei muri).
- **Contatti stratigrafici**: le interfacce tra strati. Ogni contatto è il **fondo** di uno strato; la regione sotto l'ultimo contatto è il **substrato**.
- **Quota base del dominio**: il fondo orizzontale del modello. In automatico è ricavata dal profilo; puoi fissarla a mano.

## 3. Materiali

In **Materiali geotecnici** definisci i terreni: γ, γ<sub>sat</sub>, c′, φ′, c<sub>u</sub>, φ<sub>u</sub> e, nei parametri avanzati, permeabilità, modulo elastico, parametri di roccia e retino ISO. Assegna un materiale a ogni regione con un **doppio-click** sul poligono: la regione prende il **colore del materiale**, così l'assegnazione è visibile a colpo d'occhio.

## 4. Falda e carichi

- **Falda**: la linea piezometrica. Sotto falda i conci usano il peso saturo e alla base si sottrae la pressione neutra (in condizioni drenate). In un invaso, l'acqua sopra il piano campagna è trattata come carico/alleggerimento secondo la permeabilità dello strato.
- **Carichi distribuiti**: bande di carico permanente (→ γ<sub>G</sub>) o accidentale (→ γ<sub>Q</sub>). Si trascinano in posizione sulla sezione e incrementano il peso dei conci nel loro intervallo.

## 5. Normativa e coefficienti

Nel pannello **Analisi → Normativa e verifica** scegli **NTC 2018**, **EC7-EC8** o **Utente** e la combinazione. I coefficienti parziali dei gruppi **M** (materiali) e **R** (resistenza) riducono i parametri e/o l'FS. Vedi **[Normativa e coefficienti parziali](normativa.md)**.

## 6. Azione sismica

Attiva **Analisi sismica** per l'approccio pseudostatico. Puoi inserire k<sub>h</sub>/k<sub>v</sub> a mano oppure calcolarli secondo NTC da categoria di suolo, topografia, vita nominale e a<sub>g</sub>. Vedi **[Azione sismica](sismica.md)**.

## 7. Opere di sostegno

Aggiungi **muri in c.a.** o **gabbioni** dal pannello **Opere di sostegno**. Il muro si trascina in posizione; il suo peso entra nei conci e la superficie critica non lo attraversa. Con il **raccordo** attivo, il **rinterro** dietro il muro è modellato come terreno vero nel calcolo. Vedi **[Opere di sostegno](muri.md)**.

## 8. Metodo e superficie

- **Condizione di analisi**: drenata o non drenata.
- **Metodo**: Bishop, Fellenius, Janbu, Spencer, Morgenstern-Price. Vedi **[Metodi di calcolo](metodi.md)**.
- **Forma della superficie**: *Circolari* (maglia dei centri, con **Auto-posiziona maglia**) o *Generica* (per punti o ricerca automatica).
- **Conci**, **raggi per centro** e **FS limite di progetto** rifiniscono la ricerca e il giudizio.

## 9. Calcolo e risultati

Premi **Calcola**. La **Sezione 2D** mostra la superficie critica e la maglia colorata per FS; **Output** riporta il verdetto e le prime N superfici. Se il calcolo non riesce, un **riquadro azionabile** spiega la causa (es. maglia fuori dal pendio, analisi non drenata senza c<sub>u</sub>) e offre pulsanti per risolvere.

Chiedi all'**AI** di **spiegare il risultato** o di **trovare l'intervento** (drenaggio) per l'FS obiettivo.

## 10. Viste, relazione ed export

Passa a **Modello 3D** per l'estrusione, a **Tensioni** per i diagrammi lungo la superficie, a **Relazione** per il documento. Da lì scarichi la **relazione Word** ed esporti la sezione. Vedi **[Formati file ed esportazione](formati.md)**.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Slope%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/slope/docs/it/workflow.md).*
