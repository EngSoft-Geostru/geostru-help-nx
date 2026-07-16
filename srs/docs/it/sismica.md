---
title: Azione sismica
---

# Azione sismica

SRS NX considera l'azione sismica con un approccio **pseudostatico**: un
unico coefficiente sismico orizzontale che rappresenta l'incremento delle
forze instabilizzanti dovuto al terremoto.

## Il coefficiente sismico K_h

Nella sezione **Parametri Sismici** imposta:

| Simbolo | Parametro | Unità |
|---|---|---|
| I.11 K_h | Coefficiente sismico orizzontale | — |

Con **K_h = 0** (valore predefinito) la verifica è puramente statica. Con
**K_h > 0** SRS introduce due forze aggiuntive nell'equilibrio del cuneo di
coltre:

- **Forza sismica orizzontale** `F_h = W · K_h`
- **Forza sismica verticale** `F_v = F_h / 2`

Entrambe entrano nel calcolo della forza di taglio resistente e di quella
agente (vedi [Pendio e substrato](pendio.md#come-srs-calcola-fs0)), riducendo
**FS₀** e aumentando la trazione richiesta all'ancoraggio.

## Effetto sul coefficiente γ_Q1

Quando K_h è diverso da zero, SRS applica il coefficiente parziale delle
azioni **γ_Q1** relativo alla condizione sismica (γ_Q1 = 1,0 sia per NTC 2018
sia per Eurocodice) invece di quello statico (γ_Q1 = 1,5). Questo coefficiente
moltiplica la forza di trazione e la forza di taglio di progetto
sull'ancoraggio (E.10, E.11). Vedi [Verifiche](verifiche.md).

## Come determinare K_h

Puoi calcolare K_h con qualunque metodo normativo di tua scelta a partire
dalla pericolosità sismica del sito (accelerazione al suolo a_g, categoria di
sottosuolo e topografica). In alternativa, l'**assistente AI** di SRS recupera
i parametri di pericolosità sismica NTC per una località e propone un valore
di K_h già pronto da rivedere e inserire. Vedi
[Assistente AI](assistente-ai.md#3-coefficiente-sismico-da-localita).

!!! warning "Verifica sempre l'amplificazione locale"
    Il coefficiente proposto dall'assistente assume amplificazione
    stratigrafica e topografica unitarie (S = S_S · S_T = 1). Se la categoria
    di sottosuolo o la morfologia del sito comportano un'amplificazione
    significativa, aumenta K_h di conseguenza prima di usarlo in progetto: la
    responsabilità della scelta resta del progettista.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20SRS%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/srs/docs/it/sismica.md).*
