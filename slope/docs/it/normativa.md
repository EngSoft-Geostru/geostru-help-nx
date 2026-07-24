---
title: Normativa e coefficienti parziali — Slope NX
---

# Normativa e coefficienti parziali

Slope NX verifica la stabilità secondo tre riferimenti, selezionabili nel pannello **Analisi → Normativa e verifica**.

| Normativa | Approccio |
|---|---|
| **NTC 2018** (D.M. 17/01/2018) | Coefficienti parziali agli stati limite (SLU). |
| **EC7-EC8** (EN 1997) | Design Approach con coefficienti parziali. |
| **Utente** | Coefficienti liberi definiti dal progettista. |

## Coefficienti parziali

I coefficienti sono raggruppati:

- **Gruppo M — materiali**: riducono i parametri di resistenza di progetto:
  $$ \tan\varphi'_d = \frac{\tan\varphi'_k}{\gamma_{\varphi'}}, \quad c'_d = \frac{c'_k}{\gamma_{c'}}, \quad c_{u,d} = \frac{c_{u,k}}{\gamma_{cu}} $$
- **Gruppo R — resistenza globale**: divide l'FS finale ($FS_d = FS/\gamma_R$).
- **Gruppo A — azioni**: γ<sub>G</sub> sulle permanenti, γ<sub>Q</sub> sulle accidentali.

## Principio della sorgente unica

Nella stabilità dei pendii le azioni permanenti derivano dal **peso proprio del terreno**: sono, allo stesso tempo, azione instabilizzante e origine della resistenza (attrito). Per il **principio della sorgente unica** i coefficienti del gruppo A **non modificano** il fattore di sicurezza. La verifica dipende quindi dai coefficienti **M** ed **R**.

!!! note "Come leggere l'FS"
    Applicando i coefficienti parziali (Stati Limite), il margine è già incorporato in γ<sub>R</sub>: la verifica è soddisfatta per **FS ≥ 1,0**. Con i **parametri caratteristici** (metodo tradizionale, nessuna riduzione) i valori di riferimento sono **FS ≈ 1,3÷1,5** in condizioni statiche e **1,1÷1,3** in condizioni sismiche.

L'**FS limite di progetto** impostato nel pannello Analisi non entra nel calcolo: governa solo il **giudizio** (sotto soglia l'FS è segnalato in rosso).

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Slope%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/slope/docs/it/normativa.md).*
