---
title: Assistente AI
---

# Assistente AI

SRS NX integra un **assistente AI** sensibile al contesto: conosce sempre il
progetto aperto (substrato, parametri di input e risultati di verifica, se
presenti) e ti aiuta in tre modi. Aprilo dal pulsante **Assistente** nella
barra in alto.

## 1. Chat tecnica

Fai domande sul progetto aperto: l'assistente spiega perché una verifica non
è soddisfatta, cosa rappresenta un parametro, come interpretare FS₀ e
FS_des. Risponde citando i valori reali del progetto, non numeri inventati.
Dal menu dell'assistente puoi anche **contattare il supporto** e aprire un
ticket.

## 2. Imposta un progetto da una descrizione

Invece di compilare campo per campo, scrivi in linguaggio naturale il
problema che vuoi risolvere — geometria del pendio, terreno o roccia, tipo
di chiodo, malta, rete di facciata — e chiedi all'assistente di impostare il
progetto. L'assistente compila l'intera form (titolo, normativa, substrato,
parametri di pendio, ancoraggi, malta, rete) con un'unica azione.

**Esempio**: *"Pendio in terreno sabbioso a 35°, coltre di 1,5 m, φ' = 30°,
falda assente. Usa chiodi GEWI Ø25, malta R_ck 30, interasse 2×2 m e imposta
FS_des a 1,3."*

!!! warning "Rivedi sempre i valori impostati"
    L'assistente compila il progetto ma non lo verifica: controlla i valori
    prima di premere **Calcola**. L'operazione sovrascrive i campi del
    progetto aperto.

## 3. Coefficiente sismico da località

Chiedi all'assistente il coefficiente sismico per un sito — ad esempio *"qual
è il K_h per Bologna?"* — e riceverà lat/lon dal contesto o te le chiederà.
L'assistente si collega al servizio **GeoStru Parametri Sismici** e recupera
l'accelerazione al suolo **a_g**, il fattore di amplificazione **F₀** e il
periodo **T_C\*** per la località, quindi propone un coefficiente sismico
orizzontale **K_h** già pronto da inserire nella sezione
[Azione sismica](sismica.md).

!!! warning "Verifica l'amplificazione locale"
    Il K_h proposto assume amplificazione stratigrafica e topografica
    unitarie. Se la categoria di sottosuolo del sito o la sua morfologia
    comportano un'amplificazione significativa, aumenta il valore prima di
    usarlo in progetto.

## Azioni rapide

Il pannello dell'assistente propone alcune azioni rapide per iniziare senza
scrivere:

- **Imposta un progetto da una descrizione**
- **Trova il coefficiente sismico per una località**
- **Spiega i risultati delle verifiche**
- **Come scelgo il tipo di chiodo?**
- **Contatta il supporto**

![Assistente AI](img/srs-assistente.png)

!!! note "L'assistente consuma crediti NX"
    Ogni messaggio inviato all'assistente consuma crediti NX, come il
    calcolo e l'esportazione della relazione. La responsabilità del progetto
    resta comunque del progettista: l'assistente è un supporto, non sostituisce
    la verifica tecnica.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20SRS%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/srs/docs/it/assistente-ai.md).*
