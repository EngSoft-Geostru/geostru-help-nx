# Terreni, sovraccarico e parametri

## I tre terreni

| Terreno | Parametri | Ruolo |
|---|---|---|
| **Rinforzato** (rilevato strutturale) | γ~t~, φ~t~, δ (attrito terreno-rinforzo) | azioni interne e peso dell'opera |
| **Spingente** (a tergo) | γ~t~, φ~t~, c′ | spinta attiva (Coulomb, δ = ⅔φ) |
| **Di fondazione** | γ~t~, φ~t~, φ~f~, c′ | scorrimento e capacità portante |

Il coefficiente di attrito per scorrimento f~b~ = tan δ / tan φ~t~ è sincronizzato con δ
(valore cautelativo tipico 0,6).

## Sovraccarico

Striscia di carico sul terrapieno definita da q [kN/m²] e ascisse x~in~/x~fin~ misurate
dal vertice superiore. L'incremento di tensione sui rinforzi è valutato con Boussinesq.

La **tipologia di sovraccarico** determina i coefficienti di combinazione:

| Tipologia | γ~Q~ statica | ψ₂ sismica |
|---|---|---|
| Permanente strutturale | 1,3 | 1,0 |
| Permanente non strutturale | 1,5 | 1,0 |
| Folla compatta | 1,5 | 0,6 |
| Traffico stradale | 1,5 | 0,0 |
| Ferroviario | 1,5 | 0,0 |
| Edifici | 1,5 | 0,3 |

## Coordinate del sito

Latitudine, longitudine e altitudine compaiono nella testata della relazione e si
compilano automaticamente importando un report GeoStru PS.
