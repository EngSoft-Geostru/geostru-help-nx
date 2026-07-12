---
title: Assistente AI
---

# Assistente AI

Loadcap NX integra un **assistente AI** sensibile al contesto: conosce sempre il
progetto aperto (tipologia, geometria, stratigrafia, combinazioni e risultati) e
ti aiuta in tre modi. Aprilo dal pulsante **Assistente AI** nella barra in alto.

## 1. Compila da documento

Invece di trascrivere a mano stratigrafia e parametri, **allega un documento alla
chat** e chiedi di importarlo: l'assistente estrae i dati e compila la form.

**Formati accettati**: relazione geologica o geotecnica (`.pdf`, `.txt`), tabelle
(`.csv`, `.tsv`, `.xlsx`, `.xls`), file di prova penetrometrica (`.edp`,
`.dprobe`), progetti (`.json`).

1. Allega il file (icona graffetta) e scrivi *"compila la form da questo
   documento"*.
2. L'assistente estrae ciò che trova — anche solo la **stratigrafia**, se il
   documento non contiene la geometria della fondazione.
3. La form si aggiorna e l'assistente riassume in una riga cosa ha compilato.
4. **Rivedi sempre** i valori importati prima di calcolare.

Per **dati penetrometrici grezzi** (numero di colpi, resistenza) l'assistente
costruisce una **bozza** di stratigrafia (segmentazione per andamento del rifiuto,
φ′ da correlazione di Peck, γ e c′ tipici), dichiarandola come bozza da verificare.

!!! warning "Salva prima di importare"
    L'import **sovrascrive** il progetto aperto. Se hai modifiche non salvate,
    Loadcap le segnala con un **pallino sul pulsante File** e chiede conferma. Usa
    **File → Salva** per conservare il lavoro corrente.

!!! tip "Dal dato di prova"
    Per una stratigrafia rigorosa da prove in sito, preferisci l'export da
    **Dynamic Probing NX** alla bozza da dati grezzi.

## 2. Revisione geotecnica

Un controllo automatico di coerenza del progetto, in **sola lettura**: la revisione
non modifica nulla, produce solo un referto. Avviala dall'azione **Revisione
geotecnica** nel menu dell'assistente, oppure scrivi *"controlla i parametri"*.
L'assistente esamina:

- **plausibilità dei parametri** per tipo di terreno (φ′, c′, c_u, γ, E coerenti
  con N_SPT);
- **coerenza dell'analisi** drenata/non drenata, falda, altezza di incastro;
- **geometria e carichi** (D/B, presenza di combinazioni SLU e SLE, coerenza con
  la convenzione dei segni);
- **risultati** (metodo che governa, adeguatezza di FS, ordine di grandezza dei
  cedimenti).

Il referto è una **checklist** con indicatori OK / attenzione / problema e un
verdetto complessivo, riferito ai numeri reali del progetto.

## 3. Chat tecnica

Oltre alle due funzioni sopra, l'assistente risponde a domande sul progetto:
spiega perché un metodo governa, confronta gli approcci, interpreta carico limite
e cedimenti con un **parere dell'ingegnere**, e all'occorrenza **apre un ticket di
supporto**.

L'assistente **non lancia il calcolo** (è il pulsante **Calcola**, che consuma
crediti) e non inventa numeri: cita i valori del progetto o dichiara che un dato
manca.

!!! note "Responsabilità del progettista"
    L'assistente AI è un supporto: verifica sempre i dati importati e il referto
    della revisione. La responsabilità del calcolo resta del progettista.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Loadcap%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/loadcap/docs/it/assistente-ai.md).*
