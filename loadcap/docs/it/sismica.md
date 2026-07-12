---
title: Azione sismica
---

# Azione sismica

Loadcap NX riduce la capacità portante in condizioni sismiche tenendo conto sia
dell'effetto **cinematico** (sul terreno) sia dell'effetto **inerziale** (sulla
struttura). La card **Azione sismica** si adatta alla normativa scelta.

## Con NTC 2018: pericolosità completa

Con normativa **NTC 2018**, la card espone la pericolosità sismica di sito:

- **Localizzazione** (lat/lon WGS84), **vita nominale V_N** e **classe d'uso**;
- la tabella dei **quattro stati limite** (SLO, SLD, SLV, SLC) con `a_g`, `F_0`,
  `T_C*`;
- la **categoria di sottosuolo** (A…E) e la **categoria topografica** (T1…T4),
  che determinano i coefficienti di amplificazione S_S, C_C, S_T;
- lo **spettro di risposta** elastico, tracciato in tempo reale.

Da questi dati Loadcap ricava i **coefficienti sismici**:

- **k_h** (terreno) e **k_v** = ±0,5·k_h;
- **k_hi** (struttura) = `S_e(T₁) / q`, con periodo `T₁ = c₁·H^¾`.

!!! tip "Importa da GeoStru PS"
    Il pulsante **Importa da GeoStru PS** legge il file di testo esportato dal
    servizio di pericolosità sismica GeoStru e compila automaticamente
    localizzazione, categorie e i quattro stati limite.

### Terreno e struttura: due effetti distinti

In condizioni sismiche entrano in gioco due riduzioni della capacità portante:

- **Effetto cinematico (terreno)** — dovuto all'accelerazione che attraversa il
  terreno di fondazione; dipende da **k_h**.
- **Effetto inerziale (struttura)** — dovuto alle forze d'inerzia trasmesse dalla
  sovrastruttura; dipende da **k_hi**, legato al periodo proprio della struttura
  T₁ e al fattore di comportamento q.

Il metodo **Cascone-Maugeri** combina i due contributi in un fattore correttivo
sul termine N_γ. Il pannello dedicato nella card spiega la differenza tra i due
coefficienti e come vengono calcolati.

!!! note "Periodo proprio T₁"
    T₁ è calcolato come `c₁·H^¾` (c₁ = 0,085 acciaio · 0,075 c.a. · 0,050 altre
    strutture) oppure può essere **assegnato** direttamente.

## Con Eurocodice / altre norme: coefficienti diretti

Con Eurocodice 8 o normative diverse dalle NTC, la card mostra i **coefficienti
sismici diretti**: inserisci k_h, k_v, a_g e k_hi ricavati dalla norma di
riferimento (niente spettro né import GeoStru PS). Loadcap li applica ai fattori
di capacità portante.

## Effetto sul calcolo

Quando l'azione sismica è attiva, i fattori di capacità portante (in particolare
N_γ) si riducono e, di conseguenza, si riduce il carico limite. La
[relazione geotecnica](relazione.md) riporta la sezione «Pericolosità e azioni
sismiche» con la tabella degli stati limite e i coefficienti applicati.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Loadcap%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/loadcap/docs/it/sismica.md).*
