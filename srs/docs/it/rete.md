---
title: Rete di facciata
---

# Rete di facciata

La **rete di facciata** distribuisce sul pendio la reazione degli ancoraggi:
trattiene la coltre tra un chiodo e l'altro ed è verificata a trazione e a
punzonamento nella testa dell'ancoraggio. La sezione **Rete** ne definisce le
caratteristiche.

## Parametri

| Parametro | Descrizione | Unità |
|---|---|---|
| Maglia | Dimensione della maglia della rete (es. «6x8») | mm |
| Filo | Diametro del filo metallico (es. «2.70») | mm |
| I.25 γ_rete | Coefficiente riduttivo della resistenza della rete | — |
| I.23 R_tr | Resistenza a trazione unitaria della rete | kN/m |
| I.24 R_punz | Resistenza a punzonamento della rete | kN |
| Costo rete | Costo della rete, usato per la stima di costo | €/m² |

**Maglia** e **Filo** sono descrittivi (compaiono in relazione) e non entrano
direttamente nelle formule di verifica: i valori che contano per il calcolo
sono le due resistenze **R_tr** e **R_punz**, da ricavare dalla scheda tecnica
del produttore della rete.

## Come vengono usate

SRS applica il coefficiente **γ_rete** alle due resistenze caratteristiche per
ottenere le resistenze di progetto:

- **Resistenza a punzonamento di progetto** `R_punz,des = R_punz / γ_rete`
- **Resistenza a trazione di progetto** `R_tr,des = R_tr / γ_rete`

Queste resistenze di progetto sono confrontate, rispettivamente, con la
verifica **R.6 Punzonamento rete** e **R.7 Trazione rete** (vedi
[Verifiche](verifiche.md)). Con **γ_rete = 1,0** (valore predefinito) le
resistenze di progetto coincidono con quelle caratteristiche di catalogo.

!!! note "Sezione indipendente dalle altre verifiche"
    A differenza degli altri parametri della barra e della malta, i campi
    della rete non richiedono la validazione «campi verificati» delle altre
    sezioni: puoi modificarli e vedere l'effetto sulle verifiche R.6/R.7 senza
    dover reinserire l'intero progetto.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20SRS%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/srs/docs/it/rete.md).*
