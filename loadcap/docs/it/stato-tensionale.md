---
title: Stato tensionale e modello 3D
---

# Stato tensionale e modello 3D

Le schede **Stato tensionale** e **Modello 3D** mostrano come il carico si diffonde
nel terreno e come si distribuisce la pressione al contatto. Le anteprime si
generano **senza consumare crediti**.

## Bulbo delle tensioni

Il **bulbo delle tensioni** rappresenta le isolinee dell'incremento di tensione
verticale Δσ prodotto dalla fondazione, calcolato con la soluzione di **Boussinesq**
(fattori di Newmark/Fadum). Il bulbo parte dal **piano di posa** (profondità D) ed
è disegnato dentro la sezione stratigrafica reale, con gli strati colorati e la
falda.

Con il **selettore di combinazione** scegli il carico da rappresentare: la
pressione q assegnata, oppure quella ricavata da N e dall'eccentricità.

## Mappa dei colori

La **mappa dei colori** è la stessa grandezza del bulbo resa come **heatmap** a
gradiente continuo (dal blu al rosso al crescere di Δσ), con la legenda della
tensione verticale. Aiuta a leggere a colpo d'occhio la zona di influenza del
carico.

## Pressioni di contatto al piano di posa

Il diagramma delle **pressioni di contatto** mostra come reagisce il terreno
sotto la fondazione, in funzione dell'eccentricità del carico:

- **e ≤ B/6** — diagramma **trapezio** (tutta la base reagisce): σ_max e σ_min;
- **B/6 < e < B/2** — diagramma **triangolare** (reazione parzializzata);
- **e ≥ B/2** — **ribaltamento**.

Il diagramma riporta σ_max, σ_min, l'eccentricità e l'esito.

## Modello 3D

La scheda **Modello 3D** mostra la fondazione incassata nel terreno stratificato.
Comandi disponibili:

- **modalità di vista** — Solido, Trasparente (per vedere la fondazione incassata)
  e Scavo (terreno a cornice attorno all'impronta);
- **Bulbo 3D** — il campo Δσ come gusci translucidi impilati sotto la fondazione;
- **Piano di sezione mobile** — uno slider muove una fetta colorata lungo la
  lunghezza L, per vedere come il bulbo cambia sezione per sezione;
- **Ruota** — rotazione automatica del modello.

!!! note "Il bulbo è un campo 3D"
    Le viste 2D del bulbo sono sezioni dello stesso solido tridimensionale: il
    modello 3D lo rende esplicito.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Loadcap%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/loadcap/docs/it/stato-tensionale.md).*
