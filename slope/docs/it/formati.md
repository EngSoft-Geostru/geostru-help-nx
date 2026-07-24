---
title: Formati file ed esportazione — Slope NX
---

# Formati file ed esportazione

## File di progetto `.slope`

Il progetto si salva come file **`.slope`** (JSON): un file = un pendio, con profilo, contatti, materiali, falda, carichi, muri, maglia, normativa e risultati (i risultati si ricalcolano all'apertura). Salvi nel **browser** (bozza automatica) e come file con **Salva con nome**.

| Azione | Scorciatoia |
|---|---|
| Salva nel browser | ++ctrl+s++ |
| Salva con nome (`.slope`) | ++ctrl+shift+s++ |
| Apri file | ++ctrl+o++ |
| Nuovo progetto | ++ctrl+n++ |

## Import della geometria

- **DXF** — profilo topografico e, in versione multi-strato, profilo + interfacce + falda su layer separati.
- **Immagine raster** — una sezione da ricalcare (traccia il profilo sopra l'immagine).
- **AI** — carica il **PDF di una relazione** Slope desktop o descrivi il modello a parole: l'assistente ricostruisce geometria, materiali, falda e opere.

## Esportazione

- **Relazione Word** (`.docx`) — documento di calcolo con premessa, modello geotecnico, coefficienti, metodo, risultati e conclusioni, generato nella lingua dell'interfaccia.
- **Sezione** — la vista 2D quotata, con cartiglio opzionale.
- **GeoSection** — esporta la stratigrafia verso GeoSection NX per il log di sondaggio.

!!! tip "Cloud GeoStru"
    Con l'account GeoStru i progetti si salvano su **GeoDropbox** e sono accessibili dalle altre app NX.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Slope%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/slope/docs/it/formati.md).*
