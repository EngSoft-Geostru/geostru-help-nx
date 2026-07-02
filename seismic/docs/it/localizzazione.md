# Localizzazione del sito

La pericolosità sismica di base delle NTC dipende **esclusivamente dalla
posizione geografica** del sito. Individuare il punto con precisione è quindi
il passo più importante: uno spostamento di pochi chilometri può cambiare i
parametri, soprattutto vicino ai bordi delle zone a diversa pericolosità.

## I tre modi per indicare il sito

### Mappa

Muovi la mappa (pan e zoom) e **clicca** sul punto. Il marcatore si posiziona
e le coordinate WGS84 si aggiornano. È il metodo più immediato quando conosci
visivamente la posizione dell'opera.

### Indirizzo

Apri il **pannello di ricerca** e digita un indirizzo, un Comune o un toponimo.
Seleziona il risultato corretto: la mappa si centra e il marcatore si posiziona
automaticamente.

### Coordinate

Inserisci **latitudine** e **longitudine** manualmente. Il formato atteso è
**WGS84 in gradi decimali** (es. `41.9028`, `12.4964`).

!!! tip "Precisione delle coordinate"
    Usa almeno 4–5 decimali di grado. Un decimale in meno può spostare il
    punto di oltre un chilometro e, in prossimità di un confine di zona,
    cambiare i parametri interpolati.

## Datum e conversione delle coordinate

Il reticolo di riferimento è espresso in coordinate geografiche. Se disponi
delle coordinate in un **datum diverso** — tipicamente **ED50** — o in
**gradi/primi/secondi**, usa la **conversione integrata**: PS Advanced riporta
il punto a WGS84 (ed espone anche i valori ED50) prima di interrogare il
reticolo, così i parametri restano coerenti con la normativa.

## Isole minori

Alcune isole minori ricadono **fuori dal reticolo continentale**. Per questi
siti le NTC prevedono valori di pericolosità dedicati: seleziona l'**isola**
dall'elenco apposito invece di indicare un punto sulla mappa. L'app usa allora
il reticolo specifico dell'isola.

!!! note "Interpolazione sulle isole"
    Per i siti su reticolo dedicato puoi scegliere se **interpolare** tra i
    nodi disponibili oppure usare il nodo più rappresentativo, a seconda di
    come è definito il reticolo dell'isola.

## Cosa succede dopo la localizzazione

Fissato il punto, l'app individua i **quattro nodi** del reticolo che lo
racchiudono: sono la base dell'[interpolazione dei parametri
sismici](parametri.md#interpolazione). Da qui in avanti tutto il calcolo è
deterministico e ripetibile.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20PS%20Advanced%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/seismic/docs/it/localizzazione.md).*
