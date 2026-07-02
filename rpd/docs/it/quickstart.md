---
title: Guida rapida (5 minuti)
---

# Guida rapida (5 minuti)

In cinque minuti passi dall'apertura dell'app alla lettura di una verifica completa. Apri **[nx.geostru.ai/rpd](https://nx.geostru.ai/rpd/)** e segui i passi.

## 1. Dati generali

Nella scheda **Parametri**, sezione **Dati generali**, imposta:

- una **descrizione** del progetto (facoltativa);
- la **tipologia di strada** (definisce lo spettro di traffico);
- la **vita utile** in anni;
- l'**affidabilità R** (%) e gli **indici di servizio (PSI)** iniziale e finale — servono al metodo AASHTO.

## 2. Geometria e anteprima 2D/3D

Apri **Geometria e sezioni** e inserisci numero di corsie, larghezze, banchine e pendenze. Sulla destra la **anteprima della sezione trasversale** si aggiorna **in tempo reale**.

Con il toggle **2D / 3D** in alto al pannello passi dal disegno quotato al **modello tridimensionale** del rilevato.

!!! tip "Vedi mentre progetti"
    L'anteprima resta sempre visibile: ogni valore che cambi si riflette subito nel disegno, senza premere alcun pulsante.

## 3. Stratigrafia del pacchetto

In **Stratigrafia** definisci gli spessori (cm) e i coefficienti degli strati — **usura**, **collegamento**, **base**, **fondazione** — e, se serve, aggiungi una **geogriglia bitumata** di rinforzo. Ogni strato si può attivare o disattivare con l'interruttore accanto al nome.

## 4. Sottofondo e traffico

- In **Caratteristiche sottofondo** scegli il parametro (**CBR** o **Modulo resiliente**) e il suo valore.
- In **Traffico di progetto** inserisci il **TGM** (traffico giornaliero medio), il tasso di crescita e le percentuali di veicoli commerciali e di corsia.

## 5. Metodo di calcolo

Nella card **Metodo di calcolo** scegli tra:

- **Empirico — AASHTO 1993**
- **Razionale — Ivanov** (deflessione)
- **Razionale — Westergaard** (pavimentazioni rigide)

## 6. Risultati

Apri la scheda **Risultati**: il calcolo viene eseguito automaticamente. Vedrai il **fattore di sicurezza (FS)**, lo **Structural Number**, gli **assi ammissibili** e la tabella completa delle grandezze, con l'esito **Verificata** o **Non verificata**.

!!! note "Capire ogni valore"
    Passa il mouse su una riga dei risultati e clicca l'icona **✨ Spiega**: l'assistente AI ti spiega quel parametro usando i valori del *tuo* progetto.

## 7. Se non verifica: rientra con un click

Quando FS è minore di 1, compare la card **Come rientrare in verifica** con proposte concrete:

- aumentare lo spessore di **uno strato** (ogni chip è cliccabile: applica e ricalcola);
- oppure inserire una **geogriglia** con un certo **TBR**.

Dopo aver applicato una soluzione, la barra **Annulla e scegli un'altra soluzione** ti permette di tornare indietro e confrontare le alternative.

!!! tip "Ottimizzazione"
    Se invece il pacchetto è **sovradimensionato**, RPD NX propone di **ridurre** uno strato mantenendo la verifica — meno materiale, stessa sicurezza.

## 8. Relazione ed esportazione

Dal menu **Relazione** generi il documento di calcolo in **Word** o **PDF**; dal menu **Esporta** salvi il progetto (`.rpdnx`) o la **sezione** in SVG. Vedi [Formati file ed esportazione](formati.md).

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20RPD%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/rpd/docs/it/quickstart.md).*
