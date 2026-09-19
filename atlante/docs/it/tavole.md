# Tavole

Le tavole sono composte dal server, una per fonte cartografica, e finiscono nella pagina del
fascicolo (cliccabili a piena risoluzione) e nel Word.

## Cosa contengono

- la **base**: mosaico di tile stradali o satellitari, secondo la fonte;
- il **livello** del servizio interrogato, con la sua opacità (le campiture piene sono
  semitrasparenti per lasciar leggere strade e toponimi);
- il **sito** (mirino), il **raggio** (cerchio tratteggiato, se rientra nel riquadro) e il
  **perimetro** (tratto pieno, se indicato);
- **barra di scala**, **nord**, **attribuzioni** dei dati;
- il **pannello**: titolo, Comune, coordinate, lato del riquadro, fonte e licenza, **legenda**
  del servizio (quando il servizio la fornisce e sta nel pannello), data di generazione e
  indirizzo dell'interrogazione.

| Tavola | Lato | Base |
|---|---|---|
| Inquadramento territoriale | 8 km | stradale |
| Ubicazione su immagine satellitare | 1 km | satellite |
| Tavola geologica 1:100.000 | 6 km | stradale |
| Tavola pericolosità da frana | 3 km | stradale |
| Tavola pericolosità idraulica | 3 km | stradale |
| Tavola microzonazione livello 1 | 2 km | stradale |

Con un perimetro il lato si allarga quanto serve perché l'area stia nel 70 % della tavola.

## Proiezione e scala

Le tavole sono in **Web Mercator (EPSG:3857)**, come le tile e come i servizi che le disegnano:
niente riproiezioni, niente sfasamenti. Il lato è in **metri a terra** e la barra di scala è
coerente con esso. Sono tavole di inquadramento: **non sostituiscono** la carta originale alla
sua scala, che resta da consultare sul portale dell'ente (link nel Word).

## Formati

PNG 1000 × 1000 px di mappa più il pannello; nel Word sono incorporate con didascalia e numero
di tavola. Nel file `.atlante` (GeoDropbox) viaggiano dentro il fascicolo.

!!! note "Se una tavola manca"
    Se il servizio non risponde, l'evidenza della tavola è «non disponibile» e il fascicolo si
    completa senza. **Rilancia** da *I miei fascicoli* quando l'ente è tornato su.
