---
title: Fondazione e geometria
---

# Fondazione e geometria

La card **Tipo e geometria** definisce la forma e la posa della fondazione. La
**anteprima della sezione**, sulla destra, si aggiorna in tempo reale a ogni
modifica, senza consumare crediti.

## Tipologie di fondazione

| Tipologia | Descrizione | Dimensioni di calcolo |
|---|---|---|
| **Trave rovescia** | Fondazione nastriforme continua | B (larghezza), L (lunghezza) |
| **Plinto** | Fondazione isolata rettangolare | B × L |
| **Platea** | Fondazione a piastra estesa | B × L |
| **Circolare** | Fondazione circolare | raggio R (in calcolo B = L = 2R) |

La scelta della tipologia adatta i fattori di forma e di profondità e il disegno
della sezione (per trave e plinto viene rappresentato anche il pilastro; platea e
circolare sono disegnate con lo scavo).

## Parametri geometrici

| Simbolo | Campo | Significato |
|---|---|---|
| **B** | Base | Larghezza della fondazione [m] |
| **L** | Lunghezza | Dimensione ortogonale alla sezione [m] |
| **H** | Altezza | Spessore/altezza del corpo di fondazione [m] |
| **D** | Profondità del piano di posa | Profondità del piano di appoggio dal piano campagna [m] |
| **R** | Raggio | Solo per fondazione circolare [m] |

### Altezza di incastro H_F

L'**altezza di incastro H_F** definisce il sovraccarico litostatico effettivo al
piano di posa. Quando la fondazione non è completamente confinata dal terreno
(per esempio un plinto con scavo di lavoro non rinterrato), il sovraccarico
laterale che stabilizza il meccanismo di rottura non vale `γ·D`, ma solo
`γ·H_F`.

- Spunta **« = profondità di posa »** per l'**incastro pieno**: il sovraccarico è
  `γ·D` (comportamento standard).
- Togli la spunta e inserisci **H_F < D** per un **incastro parziale**: il
  sovraccarico si riduce a `γ·H_F`, a favore di sicurezza.

!!! note "Effetto sul carico limite"
    L'altezza di incastro agisce solo sul **termine di sovraccarico** (fattore
    N_q). I **fattori di profondità** continuano a usare la profondità reale D.

## Condizione di analisi: drenata o non drenata

- **Drenata** (tensioni efficaci): si usano φ′ e c′. È la condizione tipica per i
  terreni granulari e per le verifiche a lungo termine.
- **Non drenata** (tensioni totali): φ = 0 e c = c_u. È la condizione di breve
  termine per i terreni coesivi saturi.

## Parametri geotecnici nel cuneo di rottura

L'opzione **Parametri di calcolo** stabilisce come si ricavano i valori di φ′,
c′ e γ usati nella formula:

- **Media pesata delle stratificazioni** — media dei parametri degli strati
  interessati dal cuneo di rottura, pesata sugli spessori;
- **Metodo classico (strato di posa)** — si usano i parametri dello strato su cui
  poggia la fondazione.

!!! tip "Confronto col desktop"
    Nei confronti con calcoli desktop, verifica che questa opzione sia impostata
    allo stesso modo: media pesata e strato di posa possono dare carichi limite
    sensibilmente diversi in stratigrafie non omogenee.

## Fondazione su pendio

Se la fondazione è prossima a un pendio, imposta l'**inclinazione del pendio β**
[°] e la **distanza fondazione–pendio**. Il carico limite si riduce di
conseguenza (fattori di riduzione sulla capacità portante). La sezione mostra la
scarpata sul lato del pendio.

!!! note "Convenzione"
    In Loadcap NX il pendio è rappresentato **a destra** della fondazione, con β
    positiva a scendere.

## Colore e rappresentazione

Il **colore** della fondazione è personalizzabile e si riflette sia
nell'anteprima 2D sia nel [modello 3D](stato-tensionale.md).

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Loadcap%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/loadcap/docs/it/geometria.md).*
