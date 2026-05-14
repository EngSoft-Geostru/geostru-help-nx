# Legenda e simbologia geologica

La sezione GeoSection NX viene generata con una **legenda automatica** che
elenca tutti gli strati presenti, raggruppati per codice. Puoi personalizzare
colori, retini, ordine.

## Generazione automatica

Ogni strato distinto presente nei sondaggi (campo `layer` in CSV / `LITH_CODE`
in AGS4) genera una **voce di legenda** con:

- **Codice strato** (sigla, max 8 caratteri);
- **Descrizione** (presa dalla prima occorrenza nei sondaggi);
- **Colore** assegnato automaticamente (palette di 16 colori standard);
- **Retino** (pieno per default);
- **Spessore medio** calcolato dai sondaggi (informativo).

La legenda compare **a destra della sezione** nel layout standard, ma può
essere spostata in basso o disattivata da *Layout → Legenda*.

## Personalizzazione

Pannello *Legenda → Modifica*:

| Campo | Cosa fa |
|---|---|
| **Colore** | Click sul quadrato → colorpicker; oppure digita codice esadecimale |
| **Retino** | Selezione tra i retini standard ISO/UNI: punteggiato (sabbia), trattini orizzontali (argilla), triangolini (ghiaia), ondulato (limo), zig-zag (calcare), losanghe (gesso) |
| **Descrizione** | Editabile (default = primo testo letto dal sondaggio) |
| **Ordine** | Trascina per riordinare; influisce sulla legenda stampata |
| **Visibilità** | Checkbox: nascondi voci di legenda non utili (es. terreno vegetale superficiale) |

## Aggiunta voci manuali

Per voci che non sono nei sondaggi ma che vuoi documentare in legenda
(es. "Substrato roccioso ipotizzato"):

1. *Legenda → Aggiungi voce*.
2. Codice + descrizione + colore + retino.
3. La voce appare in legenda ma **non genera poligoni** sulla sezione —
   resta puramente documentativa.

## Simbologia ISO/UNI standard

I retini disponibili seguono [UNI 8842](https://www.uni.com/) e
[ISO 14689](https://www.iso.org/standard/72048.html):

| Retino | Litotipo tipico |
|---|---|
| Punteggio fitto | Sabbia |
| Punteggio rado + trattini | Sabbia limosa |
| Trattini orizzontali | Argilla / Limo argilloso |
| Trattini incrociati | Limo |
| Triangolini | Ghiaia |
| Mattoncini | Argilla compatta / Marna |
| Zig-zag | Calcare |
| Losanghe | Gesso |
| Vuoto bianco | Riporto / antropico |
| Croci | Substrato cristallino (graniti, gneiss) |

I retini sono renderizzati come pattern SVG: scalano correttamente in stampa
PDF e DXF (fino a 1:1.000 senza pixelatura).

## Salvataggio dello stile come template

Lo stile della legenda fa parte del file `.geosection`: salvando il progetto
salvi anche colori/retini/ordine. Per riusarlo su altri progetti:

1. *File → Salva con nome* → salva un progetto "template".
2. Sui nuovi progetti: *File → Apri template stile* (carica solo la legenda
   senza dati).

Utile per studi tecnici che vogliono uniformare la presentazione delle sezioni
geologiche tra i diversi pareri.
