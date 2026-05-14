# Formati file

## .rockplane (JSON)

Il file di progetto è un **JSON UTF-8 indentato** con estensione `.rockplane`. È umano-leggibile e versionabile (git-friendly).

### Struttura

```json
{
  "versione": "1.0",
  "titolo": "Versante SS-18 km 42",
  "committente": "ANAS S.p.A.",
  "sito": "Castelpetroso (IS)",
  "data": "2026-05-14",
  "note": "",
  "professionista": {
    "nome": "...",
    "cognome": "...",
    "email": "...",
    "telefono": "...",
    "partitaIva": "..."
  },
  "localizzazione": {
    "latitudine": 41.5421,
    "longitudine": 14.6712,
    "altitudine": 720
  },
  "immagineSito": "data:image/jpeg;base64,...",
  "geometria": {
    "h": 25, "beta": 65, "alfa": 40, "psi": 0,
    "b": 5,
    "conTensionCrack": true, "t": 2, "theta": 90
  },
  "materiale": { "gamma": 26, "coesione": 40, "phi": 32 },
  "acqua": {
    "gammaW": 9.81,
    "hwPonded": 0, "versantePervious": false,
    "zwPiano": 5, "distribuzione": 2
  },
  "forzaEsterna": { "modulo": 30, "delta": 90, "tipo": 0 },
  "sisma": { "alfaS": 0.12, "omega": 0 },
  "verifica": { "approccio": 1, "fsRichiestoCaratteristico": 1.3 },
  "catalogo": [ /* tipologie chiodi/tiranti */ ],
  "catalogoReti": [ /* tipologie reti */ ],
  "interventi": [ /* interventi posizionati */ ]
}
```

### Campi chiave

| Campo                     | Tipo    | Significato                                          |
|---------------------------|---------|------------------------------------------------------|
| `versione`                | string  | Versione del formato file (compatibilità)            |
| `titolo`                  | string  | Descrizione progetto (alias: `descrizione`)          |
| `professionista`          | object  | Anagrafica utente                                    |
| `localizzazione`          | object  | Lat/Lon/Alt                                          |
| `immagineSito`            | string  | Foto sito in base64 (data URL)                       |
| `geometria.b`             | number  | Profondità blocco ⟂ alla sezione                    |
| `verifica.approccio`      | int 0-5 | 0=Caratteristico, 1=NTC2018, 2-5=EC7 DA              |

### Enum

```
verifica.approccio:
  0 = Caratteristico (γ=1)
  1 = NTC 2018 — A2+M2+R2
  2 = EC7 DA1 Comb. 1
  3 = EC7 DA1 Comb. 2
  4 = EC7 DA2
  5 = EC7 DA3

acqua.distribuzione:
  0 = Assente
  1 = Triangolare · max a metà altezza
  2 = Triangolare · max al piede
  3 = Triangolare · max alla base della fessura

forzaEsterna.tipo:
  0 = Permanente (γG)
  1 = Variabile (γQ)

intervento.tipo:
  0 = Chiodo attivo (tirante)
  1 = Chiodo passivo
  2 = Rete corticale
  3 = Rete caging

catalogo[].tipoNtc:
  0 = Chiodo · NTC §6.7 (Variante A SoilNail)
  1 = Tirante temporaneo · NTC §6.6 (γRa,t=1.10)
  2 = Tirante permanente · NTC §6.6 (γRa,t=1.20)

catalogoReti[].categoria:
  0 = Corticale aderente
  1 = Pannello a fune (caging)
```

### Compatibilità retroattiva

Campi rinominati nel formato 1.0+:

- `descrizione` → ora `titolo` (entrambi accettati in lettura)
- `operatore` → ora `professionista.nome + cognome` (compat shim)
- `fsRichiestoTa` → ora `fsRichiestoCaratteristico` (compat shim)
- `nrVerticaliIndagine` → ora `nrProveEstrazione` (compat shim, valori migrati)

File salvati con versioni precedenti **continuano a caricarsi** correttamente.

## .docx (relazione)

Standard **Office Open XML** (.docx), generato con DocumentFormat.OpenXml. Compatibile con:

- Microsoft Word 2010+
- LibreOffice Writer
- WPS Office
- Google Docs (upload)

Vedi [Esportazione →](export.md) per il contenuto.

## .dxf (sezione 2D)

Standard **AutoCAD DXF** (ASCII), versione **AC1027** (AutoCAD 2013+). Compatibile con:

- AutoCAD 2013+
- Civil3D
- BricsCAD
- ZWCAD
- LibreCAD
- QCAD

Vedi [Esportazione →](export.md) per il contenuto e i layer.

## Note di portabilità

- **Immagini incorporate**: l'immagine del sito è salvata come **data URL base64 inline** nel JSON. Per progetti con foto grandi (>1 MB) il file `.rockplane` cresce; valuta di non includere la foto se condividi il file via email.
- **Locale numerica**: i numeri nel JSON usano sempre punto decimale (`.`), non virgola (`,`), indipendentemente dal locale del sistema.
- **Encoding**: UTF-8 senza BOM. Caratteri italiani (è, ù, ° …) supportati nativamente.
