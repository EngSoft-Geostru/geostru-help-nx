# Azione sismica

La verifica sismica è pseudo-statica con la formulazione di **Mononobe-Okabe**
(angolo di inerzia θ = arctan[k~h~/(1−k~v~)]).

## Coefficienti sismici

Puoi inserire k~h~ e k~v~ direttamente, oppure **importare un report GeoStru PS**
(.txt): il programma estrae a~g~, F₀, T~C~* per i 4 stati limite, categoria di
sottosuolo e topografica, e calcola per i **muri di sostegno** (NTC §7.11.6.2.1):

- a~max~ = S~S~ · S~T~ · a~g~
- k~h~ = **β~m~** · a~max~/g, con β~m~ = **0,38** (SLV/SLC) e **0,47** (SLO/SLD)
- k~v~ = ± 0,5 · k~h~

Lo **SLV** viene applicato subito; dalla tabellina puoi passare a un altro stato
limite. Le coordinate del sito vengono riportate nei Dati generali.

## Effetti sulla verifica

Con k~h~ > 0 il programma genera la combinazione sismica (vedi
[Normativa e combinazioni](combinazioni.md)); la stabilità globale passa ai
coefficienti sismici (γ~R2~ = 1,2, M2 unitari).
