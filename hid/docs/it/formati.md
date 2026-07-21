# Formati file

## Progetto `.hid`

HID salva il progetto in un file `.hid`, che è JSON leggibile con qualunque
editor di testo.

```json
{
  "schemaVersion": 2,
  "name": "Esempio 9.4 — Procedura dettagliata",
  "general": { "country": "IT", "region": "", "regulationVersion": "rr-2017" },
  "surfaces": [ { "description": "Area impermeabile", "areaM2": 4000, "runoffPost": 0.95 } ],
  "rainfall": { "kind": "twoParameters", "a": 35.04, "n": 0.421 }
}
```

Il campo `schemaVersion` protegge dall'apertura di file prodotti da versioni più
recenti dell'app: se il numero è più alto di quello supportato, HID rifiuta il
file invece di leggerlo male.

!!! note "Nota"
    Gli input richiesti dalla normativa vivono in un dizionario
    `jurisdictionInputs`. È così che aggiungere il supporto per un nuovo paese non
    cambia il formato del file: i progetti già salvati restano leggibili.

## Salvataggio e apertura

- **Salva** scarica il `.hid` sul tuo computer.
- **Apri** carica un `.hid` esistente.
- **GeoDropbox** salva e riapre il progetto dallo spazio cloud GeoStru,
  raggiungibile dalla stessa barra degli strumenti.

## Relazione di calcolo

Dal menu **Relazione** scegli il formato:

| Formato | Estensione | Note |
|---|---|---|
| Word | `.docx` | Sempre disponibile |
| PDF | `.pdf` | Richiede il convertitore lato server |
| Word 97 | `.doc` | Richiede il convertitore lato server |

Se PDF e Word 97 non compaiono nel menu, il convertitore non è disponibile su
quel server: usa il formato Word.

La relazione contiene riferimenti normativi, dati generali, superfici scolanti,
curva pluviometrica, parametri idrologici, ietogramma, dimensionamento, sistema
di scarico, verifiche finali e idrogramma, con i grafici incorporati.

!!! tip "Suggerimento"
    La relazione esce nella lingua selezionata nella barra degli strumenti. Cambia
    lingua prima di generarla se la consegni a un ente straniero.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20HID%20NX).*
