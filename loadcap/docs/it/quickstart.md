---
title: Guida rapida (5 minuti)
---

# Guida rapida (5 minuti)

In cinque minuti passi dall'apertura dell'app alla lettura di una verifica di
capacità portante con i cedimenti. Apri **[nx.geostru.ai/loadcap](https://nx.geostru.ai/loadcap/)**
e segui i passi.

!!! tip "Parti da un esempio"
    Il modo più veloce per prendere confidenza è caricare un **progetto di
    esempio**: menu **?** (in alto) → scheda **Risorse** → scegli, ad esempio,
    *Plinto — NTC 2018*. La form si compila da sola e puoi calcolare subito. Vedi
    [Progetti di esempio](esempi.md).

## 1. Dati generali

Nella scheda **Parametri**, sezione **Dati generali**, imposta una **descrizione**
del progetto e la **normativa** di riferimento (NTC 2018, Eurocodice, oppure
*Libera* per campi tutti liberi).

## 2. Geometria della fondazione

In **Tipo e geometria** scegli la tipologia — **trave rovescia, plinto, platea,
circolare** — e inserisci le dimensioni: base **B**, lunghezza **L**, altezza
**H**, profondità del piano di posa **D**. Sulla destra la **anteprima della
sezione** si aggiorna in tempo reale. Vedi [Fondazione e geometria](geometria.md).

## 3. Stratigrafia e falda

In **Stratigrafia** definisci gli strati (spessore, peso di volume **γ**, angolo
di attrito **φ′**, coesione **c′**, e i parametri di deformabilità). Puoi
**incollare** una tabella da Excel o **importare** una stratigrafia da Dynamic
Probing NX. Nella card **Falda** indichi presenza e profondità dal piano campagna.
Vedi [Stratigrafia e falda](stratigrafia.md).

## 4. Carichi e combinazioni

In **Carichi di progetto** inserisci le combinazioni. Per ognuna scegli
l'**approccio** (che precompila i coefficienti parziali) e i carichi al piano di
posa: pressione **q** oppure **N** con eventuali momenti **Mx/My** e tagli
**Hx/Hy**. Le combinazioni SLU servono al carico limite, quelle **SLE** ai
cedimenti. Vedi [Carichi e combinazioni](carichi.md).

## 5. Metodi di calcolo

Nella card **Metodi di calcolo** attiva i metodi da confrontare (Terzaghi,
Meyerhof, Hansen, Vesic, Brinch-Hansen, Meyerhof-Hanna). Il metodo che governa è
quello con la **resistenza di progetto minima**.

## 6. Calcola

Premi **Calcola** nella barra in alto. Il calcolo consuma crediti NX.

!!! note "Anteprime senza addebito"
    Le anteprime (sezione 2D, stato tensionale, spettro sismico, relazione HTML)
    si aggiornano **gratuitamente**: gli crediti si consumano solo con **Calcola**
    e con l'esportazione della relazione.

## 7. Risultati

Apri **Carico limite**: per ogni combinazione vedi, per ciascun metodo, il carico
limite **q_lim**, la resistenza di progetto **R_d = q_lim / γ_R,v**, la tensione
di esercizio, il **fattore di sicurezza** e l'esito **Verificata / Non
verificata**. Dove è presente un'azione orizzontale compare anche la **verifica a
scorrimento**. Vedi [Capacità portante](carico-limite.md).

## 8. Cedimenti

La scheda **Cedimenti** mostra, per la combinazione di servizio (SLE)
selezionata, i cedimenti **elastici** ed **edometrici** per strato, l'eventuale
stima di **Burland & Burbidge** e il **decorso nel tempo**. Vedi
[Cedimenti](cedimenti.md).

## 9. Relazione ed esportazione

Dal menu **Relazione** generi il documento di calcolo in **Word** o **PDF**; dal
menu **File** salvi il progetto (`.lcnx`). Vedi
[Relazione ed esportazioni](relazione.md).

!!! tip "L'assistente AI"
    Il pulsante **Assistente AI** in alto ti spiega i risultati, riempie la form
    da una relazione o da un file di prova, e fa una **revisione geotecnica** del
    progetto. Vedi [Assistente AI](assistente-ai.md).

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Loadcap%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/loadcap/docs/it/quickstart.md).*
