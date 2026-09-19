# Perimetro del sito

Un punto descrive un intorno; un **perimetro** descrive il sedime dell'opera. Se lo indichi, le
fonti vengono interrogate sull'intera area e le tavole lo disegnano.

## Disegnare

Sulla mappa di **Nuovo fascicolo**, controllo **Perimetro** in alto a sinistra:

1. **Disegna**: il cursore diventa un mirino. Clicca i vertici uno alla volta; la linea
   tratteggiata segue i clic.
2. Chiudi **sul primo vertice** (ha il suggerimento «Chiudi il perimetro») oppure con **doppio
   clic**, oppure con il pulsante che nel frattempo è diventato **Chiudi**.
3. **Esc** annulla il disegno in corso. **Cancella** toglie il perimetro.

Nel modulo compare «*N* vertici · area». Se il punto del sito è fuori dal perimetro (o manca),
viene spostato al centro dell'area: puoi sempre trascinarlo.

## Importare

**Importa** accetta:

- **GeoJSON** (`.geojson`, `.json`): `Polygon`, `MultiPolygon` (il primo), `Feature` o
  `FeatureCollection` (il primo poligono). Coordinate WGS84 lon, lat.
- **KML** (`.kml`): il primo `<Polygon>`.
- **Testo** (`.txt`, `.csv`): una coppia **lat, lon** per riga, separata da virgola, punto e
  virgola o spazio.

Servono almeno tre vertici, in Italia, e un'area fino a **25 km²**.

## Cosa cambia nelle interrogazioni

| Fonte | Con il perimetro |
|---|---|
| Carte ISPRA (geologia, litologia, sismicità, faglie, perforazioni), Corine | interrogazione **per poligono**: una richiesta, tutti gli elementi che intersecano l'area. Nella sintesi: «*N* elementi nel perimetro» |
| Microzonazione (WebMS) | filtro spaziale sul WFS: tutte le zone che toccano il perimetro |
| Pericolosità PAI, IFFI (IdroGEO), catasto | il servizio risponde solo al punto: si campionano **fino a 9 punti interni** (centro + griglia) e si tengono gli elementi distinti. Il catasto elenca le particelle per foglio |
| Eventi INGV, parametri NTC, indicatori del Comune | dal punto e dal Comune, come senza perimetro |
| Tavole | il riquadro si allarga finché il perimetro sta nel 70 % della tavola; il perimetro è disegnato a tratto pieno e citato nel pannello |

!!! warning "Campionamento"
    Su IdroGEO e catasto un perimetro grande può contenere più elementi di quanti nove punti
    intercettino. La sintesi lo dice («*N* elementi su 9 punti campionati»): per un lotto
    ordinario è più che sufficiente, per un'area vasta usa anche la tavola.

Nel Word il perimetro compare nella tabella di ubicazione, nel metodo e nelle tavole; nel testo
dell'assistente come dato del sito.
