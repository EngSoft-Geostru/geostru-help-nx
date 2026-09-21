# Formati e file

## In uscita

| File | Cosa contiene | Dove |
|---|---|---|
| **Word (`.docx`)** | il fascicolo in forma di relazione: indice, capitoli, tabelle, tavole incorporate, fonti e portali; proprietà con autore e impronta di provenienza | **Scarica Word** nella pagina del fascicolo; anche in GeoDropbox |
| **Tavole (`.png`)** | 1000 × 1000 px di mappa più pannello, una per fonte cartografica | clic sulla tavola nella pagina del fascicolo |
| **`.atlante`** | il fascicolo completo (JSON) con le tavole dentro in base64: 5–9 MB | inviato a GeoDropbox nella cartella *Atlante NX*, accanto a PDF e Word; si reimporta come nuovo fascicolo ([GeoDropbox](geodropbox.md)) |
| **PDF delle indagini** | i documenti che hai caricato, come sono | dal nome del file nella sezione «Le tue indagini»; visibili solo a te |

## In entrata

| File | Uso | Limiti |
|---|---|---|
| **GeoJSON** (`.geojson`, `.json`) | perimetro del sito: `Polygon`, `MultiPolygon`, `Feature`, `FeatureCollection` (primo poligono) | WGS84 lon, lat; ≥ 3 vertici; ≤ 25 km² |
| **KML** (`.kml`) | perimetro: il primo `<Polygon>` | come sopra |
| **Testo** (`.txt`, `.csv`) | perimetro: una coppia lat, lon per riga | come sopra |
| **PDF** | indagini da analizzare | ≤ 12 MB, uno per volta, dieci per fascicolo |
| **`.atlante`** | reimporto di un fascicolo da GeoDropbox | prodotto da Atlante NX |

## Cosa non c'è (ancora)

- import del perimetro da **DXF**: in programma;
- esportazione delle **evidenze in CSV**: il `.atlante` è JSON e contiene tutto;
- le tavole in **PDF** o **DXF**: il Word le incorpora; la carta originale resta sul portale
  dell'ente, che il Word linka.

Il Word non è firmato digitalmente: la firma è del professionista che completa e consegna la
relazione.
