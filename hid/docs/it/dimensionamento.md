# Dimensionamento dell'invaso

## Ietogramma di progetto

Lo ietogramma distribuisce nel tempo l'altezza di pioggia data dalla curva.

| Tipo | Quando usarlo |
|---|---|
| **Chicago** | Il più diffuso: picco posizionabile con il coefficiente r |
| **Uniforme** | Intensità costante per tutta la durata |
| **Sifalda** | Tre tratti, forma trapezia |
| **Triangolare** | Salita e discesa lineari |

Per il Chicago il **coefficiente di posizione r** indica dove cade il picco: 0,4
significa al 40 % della durata.

![Ietogramma e depurazione](img/05-depurazione-piogge.png)

## Depurazione delle piogge

Trasforma la pioggia lorda in pioggia netta, cioè quella che diventa deflusso.

- **Percentuale** — moltiplica per il coefficiente di deflusso φ della superficie.
  È il modello più semplice e il più usato.
- **Horton** — infiltrazione decrescente nel tempo secondo la classe di suolo.
- **SCS-CN** — metodo del curve number, con condizione di umidità antecedente
  AMC I, II o III.

!!! warning "Lombardia"
    Il metodo SCS-CN non è ammesso dal regolamento regionale.

## Idrogramma

Trasforma la pioggia netta in portata:

- **Corrivazione** — usa il tempo di corrivazione della superficie.
- **Nash** — cascata di n serbatoi lineari con costante K, per bacini più
  articolati.

## Laminazione

L'invaso viene instradato passo per passo risolvendo il bilancio di massa fra
portata entrante, portata uscente dall'organo di scarico e volume accumulato. Il
massimo del volume è il risultato della procedura dettagliata.

![Calcoli e verifiche](img/06-calcoli-verifiche.png)

## Le verifiche finali

| Verifica | Condizione |
|---|---|
| Altezza utile | H di progetto ≥ altezza richiesta |
| Volume utile | V di progetto ≥ volume ammissibile |
| Tempo di svuotamento | T ≤ tempo ammesso (di norma 48 h) |

Il tempo di svuotamento è calcolato solo per gli scarichi a portata costante e
per l'infiltrazione costante: per gli altri organi la portata dipende dal
battente e varia durante lo svuotamento.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
