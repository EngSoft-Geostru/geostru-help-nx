# Formati file

GDW gestisce un unico formato di file progetto: il **`.gabbioni`**.

## File `.gabbioni`

File di testo a sezioni delimitate da intestazioni in parentesi quadre.
Ogni valore su una riga. Estensione `.gabbioni` (MIME registrato come
`application/octet-stream` per servire i sample).

### Versionamento

La prima riga `[Versione]` seguita da un intero indica la versione del
formato:

| Versione | Cosa è stato aggiunto |
|---|---|
| 1 | Formato iniziale |
| 2 | AngoloAttritoGabbioni |
| 3 | TipologiaGabbione |
| 4 | Descrizioni sovraccarico + Resistenza filo + Allungamento + ProfonditaFalda |
| 5 (corrente) | Stratigrafia multistrato + ColoriTerreni + nuovi campi rete e fondazione |

Il parser GDW è **backward-compatible**: file vecchi (versione 1÷4) si
caricano e i campi nuovi assumono i default.

### Struttura

```
[Versione]
5
[Dati progetto]
{Description}
{Address}
{Latitude}
{Longitude}
{Normativa}
{ProfonditaFalda}
[Geometria]
{NumeroFile}
{BlocchiPerFila[0]}
{ShiftPerFila[0]}
{BlocchiPerFila[1]}
{ShiftPerFila[1]}
...
{PrimaFilaInterrata 0/1}
{AngoloMonte1}
{LunghezzaMonte1}
{AngoloMonte2}
{LunghezzaMonte2}
{AngoloValle}
{LunghezzaValle}
[Gabbioni]
{PesoSpecificoBlocco}
{BaseGabbione}
{AltezzaGabbione}
{ProfonditGabbione}
{AngoloAttritoGabbioni}
{TipologiaGabbione}
[Fondazione]
{BaseFondazione}
{AltezzaFondazione}
[Sovraccarico]
{DescrizioneSovraccaricoPermanente}
{SovraccaricoPermanente}
{AscissaInizialeCaricPerm}
{AscissaFinaleCaricPerm}
{DescrizioneSovraccaricoAccidentale}
{SovraccaricoAccidentale}
{AscissaInizialeCaricAcc}
{AscissaFinaleCaricAcc}
{SpintaAggiuntiva}
[Rete elettrosaldata]
{DescrizioneRete}
{TipoRete}
{DiametroFilo}
{ResistenzaRottura}
{Allungamento}
{ResistenzaRete}
{ResistenzaRetePunzonamento}
[Geotecnica]
{PesoUnitVolumeTerrenoSpingente}
{AngoloResistenzaTaglio}
{PesoUnitVolumeFondazione}
{AngoloResistenzaTaglioFondazione}
{CoesioneFondazione}
{NomeTerrenoSpingente}
{ColoreTerrenoSpingente}
{NomeTerrenoFondazione}
{ColoreTerrenoFondazione}
[Stratigrafia]
{N strati}
{Strato[0].Descrizione}
{Strato[0].Colore}
{Strato[0].Altezza}
{Strato[0].AngoloResistenzaTaglio}
{Strato[0].PesoUnitVolume}
{Strato[0].PesoUnitVolumeSaturo}
{Strato[0].Coesione}
... (ripetuto per ogni strato)
[Coeff. Sicurezza]
{CoeffPartSpintaPassiva}
{APesoMuro}
{ASpintaTerreno}
{ASpintaFalda}
{ASpintaSismica}
{ASovraccarichiPermanenti}
{ASovraccarichiAccidentali}
{MGFi}
{MGC}
{MGCU}
{RQLim}
{RScorrimento}
{RSpintaPassiva}
{RRibaltamento}
{SpintaPassivaEsclusa 0/1}
[Sisma]
{Kh}
{Kv}
{APesoRiempimento}        ← aggiunto dopo Kv (backward-compat)
{TipoInterfacciaBase}     ← terreno / fondazione / custom
{ModoAngoloAttritoGabbioni} ← auto / manuale
{PhiInterfacciaCustom}    ← (vuoto se non custom)
{CInterfacciaCustom}      ← (vuoto se non custom)
{InclinazioneFondazione}  ← β fondazione in gradi
{TipoMaglia}              ← doppia_torsione / elettrosaldata
{CodiceMagliaDT}          ← codice catalogo (es. 8x10-2.7-zinc)
{PesoUnitarioRete}        ← kg/m² (per DT)
{CoesioneGabbione}        ← c_g in kPa (per DT)
```

### Note

- I **caratteri ACAPO** (newline) nelle descrizioni sono codificati come
  `[ACAPO]` (token letterale) per non rompere il formato a una riga per valore.
- I valori **numerici** sono in formato InvariantCulture (decimale con `.`).
- I campi **opzionali** in coda possono essere omessi → il parser usa i
  default. Lettura tolerante.

## Catalogo gabbioni

`wwwroot/catalogs/tipologie-gabbioni.json` — catalogo JSON con dimensioni e
pesi tipici delle scatole gabbione standard. Letto in client-side dal
`<select>` Tipologia.

Esempio:

```json
[
  {
    "code": "1x1x1-1000",
    "label": "1×1×1 m — 1000 kg",
    "L": 1, "B": 1, "H": 1, "weight": 1000,
    "mesh": "8x10", "wireDiameter": 2.7
  }
]
```

## Catalogo reti a doppia torsione

`wwwroot/catalogs/reti-doppia-torsione.json` — catalogo JSON con 7 modelli
di rete DT (6×8 e 8×10, zincatura forte e con PVC). Letto client-side.

Esempio:

```json
[
  {
    "code": "8x10-2.7-zinc",
    "label": "8×10 — Ø 2.7 mm (Forte zincatura)",
    "maglia": "8x10",
    "diametroFilo": 2.7,
    "rivestimento": "Zn forte",
    "pesoUnitario": 1.40,
    "resistenzaRete": 50,
    "resistenzaRottura": 350,
    "allungamento": 8,
    "coesioneGabbione": 3.0,
    "phiGabbione": 45
  }
]
```

## File di esempio scaricabili

Tab **Risorse** del modale `?` in alto a destra: scaricabili sample reali.
Attualmente disponibile:

- **`esempio-muro-5m-fond-inclinata.gabbioni`** — caso cliente: muro 5 m a
  destra, fondazione inclinata 10°, terrapieno 25°, NTC 2018 statica. Tutti
  i FS soddisfatti.

## Vedi anche

- [Quickstart](quickstart.md) — caricare e usare i sample
- [Rete metallica](rete.md) — catalogo reti DT
- [Geometria](geometria.md) — catalogo tipologie gabbioni
