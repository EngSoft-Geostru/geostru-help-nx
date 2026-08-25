# Disegnare sulla mappa

Tre strumenti — punto, polilinea, poligono — e pochi gesti da ricordare.

## Gli strumenti

| Strumento | A cosa serve | Minimo |
|---|---|---|
| **Punto** | punti indipendenti: sondaggi, capisaldi, stazioni | 1 |
| **Polilinea** | un tracciato: strada, sezione, allineamento | 2 vertici |
| **Poligono** | un'area: perimetro di rilievo, area di mesh | 3 vertici |

Si scelgono dalla barra laterale o dal menu **Disegna**.

## I gesti

| Gesto | Effetto |
|---|---|
| clic sulla mappa | posa un vertice |
| doppio clic | posa l'ultimo vertice e **chiude** la geometria |
| **Invio** | chiude la geometria |
| **Esc** | annulla il disegno in corso |
| clic sul primo vertice (poligono) | chiude l'anello |

Mentre disegni, un segmento tratteggiato segue il cursore: mostra dove cadrà il
prossimo lato, e sul poligono anche il lato di chiusura. La barra di stato conta
i vertici e ricorda come chiudere.

!!! tip "Il doppio clic posa, non scarta"
    Facendo doppio clic su un punto nuovo, quel punto diventa l'ultimo vertice.
    Se invece fai doppio clic **sopra l'ultimo vertice già posato**, la geometria
    si chiude senza raddoppiarlo.

## Modificare ciò che hai disegnato

- **Trascina un vertice** per spostarlo: tabella, distanze e area si aggiornano.
- **Zoom su un punto** e **Elimina** sono i due pulsanti a fine riga nella
  tabella coordinate.
- Togliendo un vertice, i rimanenti vengono rinumerati: il tracciato non si
  scompone. Se scendi sotto il minimo (2 per una polilinea, 3 per un poligono) la
  geometria viene rimossa per intero.
- **Cancella** svuota la mappa. Non è annullabile: viene chiesta conferma.

## Disegnare senza cliccare

Non sei obbligato a disegnare a mano:

- **File › Apri** ricarica un progetto salvato (`.gmap`).
- **File › Carica esempio** apre un tracciato già pronto.
- **GeoDropbox** riapre un progetto dal cloud.
- L'**assistente AI** disegna al posto tuo: incollagli una lista di coordinate o
  allegagli un documento che le contiene, e le posa sulla mappa. Converte da solo
  gradi/primi/secondi, e quando l'ordine delle colonne è ambiguo dichiara quale
  ha assunto invece di indovinare in silenzio.

## Le misure

Il pannello **Misure** in barra laterale aggiorna in tempo reale punti, distanza
totale, area ed escursione delle quote. Gli stessi valori compaiono nella barra
di stato in basso: sono sempre lo stesso numero, calcolato una volta sola.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Maps%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/maps/docs/it/disegno.md).*
