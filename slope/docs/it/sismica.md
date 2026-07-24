---
title: Azione sismica — Slope NX
---

# Azione sismica

Slope NX include l'azione sismica con l'**approccio pseudostatico**: al peso di ogni concio si aggiungono una forza orizzontale k<sub>h</sub>·W e una verticale k<sub>v</sub>·W, dove k<sub>h</sub> e k<sub>v</sub> sono i **coefficienti sismici**.

Attiva **Analisi sismica** nel pannello **Analisi → Metodo e parametri**.

## Coefficienti manuali o da NTC

Puoi inserire k<sub>h</sub> e k<sub>v</sub> **a mano** (utile per EC/LRFD/Utente), oppure calcolarli secondo **NTC** dal pannello sismico:

- **Categoria di sottosuolo** (A–E) e **categoria topografica** (T1–T4).
- **Classe d'uso** e **vita nominale** (V<sub>N</sub>) → periodo di riferimento.
- Parametri di pericolosità: a<sub>g</sub>/g (SLV), F<sub>0</sub>, T<sub>C</sub>*.

Il calcolo restituisce a<sub>max</sub>, il coefficiente di riduzione β e i coefficienti k<sub>h</sub> = β·a<sub>max</sub>/g e k<sub>v</sub> = ±0,5·k<sub>h</sub> (secondo i coefficienti di normativa per terreni e opere).

## Import da GeoStru PS

Se hai già calcolato la pericolosità con **GeoStru Spectra** (o strumento equivalente), puoi **importare** il file di parametri sismici (`.txt`) e Slope NX compila k<sub>h</sub>/k<sub>v</sub> automaticamente.

!!! note "Soglia in condizioni sismiche"
    Con i parametri caratteristici (metodo tradizionale) i valori di riferimento dell'FS scendono a **1,1÷1,3** in presenza di sisma. Con i coefficienti parziali agli stati limite la verifica resta soddisfatta per FS ≥ 1,0.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Slope%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/slope/docs/it/sismica.md).*
