# RSL III A NX

**RSL III A NX** applica l'**Ordinanza n. 55 del 24/04/2018** del Commissario straordinario per la ricostruzione (sisma 2016), Allegato 1 e
Appendice 1. Nei comuni con uno studio di **Microzonazione Sismica di livello 3 (MS3)** il progettista deve controllare se lo spettro di
risposta dello studio è più severo di quello che darebbe l'**approccio semplificato** delle NTC 2018. RSL III A NX fa questo controllo e lo
mette in una relazione Word.

Il lavoro è breve: un file (lo spettro MS3), i parametri sismici del sito, la categoria di sottosuolo e due periodi dell'edificio. Il resto
lo calcola il server, a ogni modifica.

## Che cosa fa

1. **Regolarizza** lo spettro MS3 nella forma a quattro tratti delle NTC (Appendice 1): T~A~, SA~m~, T~V~, SV~m~, T~B~, T~C~, T~D~, a~max~, F~0~.
2. Calcola lo **spettro semplificato NTC 2018** del sito per **T~R~ = 475 anni**, η = 1, componente orizzontale.
3. **Confronta** i due spettri nell'intervallo **[T~min~, 2·T~max~]** con le due condizioni dell'Ordinanza: supero puntuale oltre il 30 %
   e supero dell'integrale oltre il 20 %.
4. Dà l'**esito**: approccio semplificato utilizzabile, approfondimenti necessari, oppure confronto non effettuabile (2·T~max~ > 1,1 s).
5. Produce la **relazione Word** con il testo dell'Ordinanza, i dati, i grafici, i parametri e il valore delle due condizioni.

## A chi serve

Ai progettisti e ai geologi che lavorano alla ricostruzione nei territori del sisma 2016 e devono decidere, per un edificio, se usare lo
spettro di norma o se servono approfondimenti e, eventualmente, un'analisi di risposta sismica locale (con GeoStru RSL III).

## Le quattro schede

| Scheda | Che cosa fai |
|---|---|
| [Sito](sito.md) | dati generali, posizione sulla carta, parametri a~g~, F~0~, T~c~* |
| [Spettro MS3](spettro-ms3.md) | import del file dello studio, regolarizzazione |
| [Confronto](confronto.md) | categorie, T~min~ e T~max~, grafico, condizioni, esito |
| [Relazione](relazione.md) | anteprima e Word |

Inizia dalla [Guida rapida](quickstart.md). Prima di usare l'esito in un progetto leggi [Validazione e limiti](validazione.md).

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20RSL%20III%20A%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/rsl3a/docs/it/index.md).*
