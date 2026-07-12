---
title: Domande frequenti
---

# Domande frequenti

## Il carico limite non coincide con un calcolo desktop. Perché?

Le cause più frequenti sono due, entrambe impostabili:

1. **Parametri nel cuneo** — «media pesata delle stratificazioni» oppure «metodo
   classico (strato di posa)» danno risultati diversi in stratigrafie non
   omogenee. Vedi [Fondazione e geometria](geometria.md#parametri-geotecnici-nel-cuneo-di-rottura).
2. **Altezza di incastro** — se il sovraccarico è `γ·H_F` (incastro parziale)
   invece di `γ·D`, il termine N_q cambia. Vedi
   [altezza di incastro](geometria.md#altezza-di-incastro-h_f).

Verifica inoltre di aver attivato gli **stessi metodi** e la stessa condizione
(drenata/non drenata).

## Quale metodo di calcolo devo usare?

Attiva più metodi e confrontali: il risultato che governa è la **resistenza di
progetto minima**. Meyerhof-Hanna è specifico per **terreni a due strati**;
Richards per le **condizioni sismiche**. Vedi [Capacità portante](carico-limite.md).

## I cedimenti sono calcolati con i carichi SLU?

No: i cedimenti si valutano con le combinazioni di **servizio (SLE)**. Assicurati
di avere almeno una combinazione SLE. Vedi [Cedimenti](cedimenti.md).

## Quando compare la verifica a scorrimento?

Solo quando la combinazione ha un'**azione orizzontale** (H_x o H_y ≠ 0). Senza
taglio la verifica non è necessaria. I parametri (adesione, δ, spinta passiva) si
impostano nella card **Verifica a scorrimento**, sopra la Falda.

## Il calcolo consuma crediti? E le anteprime?

Il **Calcola** e l'**esportazione della relazione** consumano crediti NX. Le
anteprime (sezione 2D, stato tensionale, spettro sismico, relazione HTML) sono
**gratuite** e si aggiornano in tempo reale.

## Posso importare la stratigrafia da una prova penetrometrica?

Sì. Da **Dynamic Probing NX** usa «Esporta per Loadcap» e in Loadcap premi
**Importa** nella card Stratigrafia. In alternativa, allega il file di prova
all'**assistente AI**, che ne ricava una bozza. Vedi
[Stratigrafia e falda](stratigrafia.md#incolla-e-importa).

## Come salvo e riapro un progetto?

Dal menu **File**: **Salva** genera un file **.lcnx**, **Apri** lo ricarica. Vedi
[Relazione ed esportazioni](relazione.md#salvataggio-e-geodropbox).

## In quali lingue è disponibile Loadcap NX?

L'interfaccia dell'app è disponibile in **italiano** e **inglese**.

---

Non hai trovato la risposta? [Scrivici](mailto:info@geostru.ai?subject=Help%20Loadcap%20NX) — rispondiamo in giornata.

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Loadcap%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/loadcap/docs/it/faq.md).*
