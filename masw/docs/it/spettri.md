# Spettri e picking

## Calcolare lo spettro

Imposta **f min**, **f max**, **v min**, **v max** e **dv**, poi premi **Calcola**. In alto a destra vedi la frequenza
di Nyquist: **f max** deve restare sotto. Passi troppo fini su intervalli ampi vengono rifiutati con un messaggio.

La mappa ha la frequenza in ascissa e la velocità di fase in ordinata. Dove c'è un'onda vera si forma una **cresta**:
letta da sinistra a destra scende, ed è la curva di dispersione che cerchi.

![Spettro f-v](img/03-spettri.png)

**Colori** e **Livelli** cambiano solo il disegno, non il calcolo.

## Curva apparente e regressione

Sopra la mappa compaiono i massimi di ogni colonna: blu quelli usati, arancio quelli esclusi. La curva nera è il
polinomio di **Grado** scelto (da 2 a 10). I massimi uguali al minimo o al massimo della curva escono da soli dalla regressione.

Con **Escludi** trascini un rettangolo sui punti da togliere, con **Includi** li rimetti, **Reincludi tutti** azzera.

## Il picking

Il **picking** è la lista dei punti (f, v) che entrano nell'inversione. Ogni punto appartiene a un **Modo**: 0 è il
fondamentale, 1…4 sono i superiori.

| Strumento | Gesto |
|---|---|
| **Aggiungi** | clic sulla mappa; trascinando in verticale allarghi la barra di incertezza |
| **Sposta** | trascina un punto |
| **Elimina** | clic su un punto |
| **Automatico** | **N. punti** sulle creste della mappa, anche su più modi |
| **Nuova selezione** | svuota il picking, dopo conferma nella pagina |

Sotto il grafico leggi f, v e la lunghezza d'onda λ = v/f nel punto del cursore.

!!! warning "Il picking è una scelta tua"
    **Automatico** segue le creste della mappa, non la fisica. Va controllato sulla mappa: scambiare un modo superiore per il
    fondamentale sovrastima V~s~.

## La tabella

**Curva di dispersione** mostra i punti del modo corrente. Puoi correggere f, v e modo; Canc su una cella elimina la riga.
Incollando da Excel righe `f⇥v` o `f⇥v⇥modo` **sostituisci tutto il picking**. **Copia** porta i punti negli appunti.

## Modello sintetico

Scrivi un profilo a strati di prova e con **Mostra curve** vedi sopra la mappa le curve che produrrebbe. Serve a capire a
occhio se un profilo è plausibile.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20MASW%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/masw/docs/it/spettri.md).*
