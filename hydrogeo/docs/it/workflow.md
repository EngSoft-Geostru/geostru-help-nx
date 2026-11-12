# Il lavoro completo

Un caso reale, dal sito del progetto alla curva di possibilità pluviometrica e al
dimensionamento delle opere.

```text
Atlante NX          Hydrogeo NX                     Runoff Lab NX               HID NX
──────────          ───────────                     ─────────────               ──────
sito del progetto → stazioni vicine → massimi    → distribuzioni di         → laminazione per
                    scheda e rilevanza   annui      probabilità, curva         l'invarianza
                                                    h = a·tⁿ, ietogrammi       idraulica
```

## 1. Il sito

Se usi [Atlante NX](https://help.nx.geostru.ai/atlante/it/), il collegamento a Hydrogeo NX
apre la mappa **centrata sul sito** e lo segna con il segnaposto «Sito (Atlante NX)».
Altrimenti parti dal nome del comune o dalle coordinate.

## 2. Le stazioni candidate

Chiedi all'assistente le stazioni attorno al sito, con un raggio e una lunghezza minima
della serie:

```text
Pluviometri entro 20 km da 43.11, 12.39 con almeno 20 anni di dati
```

Puoi filtrare anche per regione, provincia, bacino, fonte, strumento e quota. Vedi
[Assistente AI](assistente.md).

## 3. La scelta della stazione

Per ogni candidata apri la scheda e confronta:

- **distanza e quota** rispetto al sito, e se sta nello **stesso bacino**;
- **anni di dati** e **periodo**: una serie lunga e recente è preferibile;
- **rilevanza**: buona da 20 anni in su, media da 10 a 20, bassa sotto i 10;
- **tipi di dati**: per i massimi per durata serve la voce «Pioggia oraria».

Alcune stazioni hanno solo piogge giornaliere e nessuna serie di massimi per durata: vanno
bene per le precipitazioni mensili, non per la curva di possibilità pluviometrica.

## 4. I dati

Sblocca la stazione e controlla le [tabelle](dati.md): gli anni mancanti, i trattini nelle
durate brevi degli anni più vecchi, gli eventi estremi. I valori sono quelli pubblicati dalla
fonte, senza correzioni.

## 5. L'esportazione

Dal menu **Esporta** scegli il formato: CSV o Excel per i tuoi calcoli, **PDF Report** da
allegare alla relazione, **PLV GeoStru** per i software desktop GeoStru. Vedi
[Esportazioni e formati](formati.md).

## 6. La statistica

In [Runoff Lab NX](https://help.nx.geostru.ai/runofflab/it/) usa **Importa → Da Hydrogeo
NX…**, cerca la stazione per nome e importala: le serie dei massimi per durata arrivano
nello studio senza passare da un file. Lì adatti Gumbel, GEV, Pearson III o TCEV e ottieni la
curva h = a·tⁿ.

## 7. Il progetto

I parametri **a** e **n** della curva sono i dati di pioggia che
[HID NX](https://help.nx.geostru.ai/hid/it/) chiede per dimensionare le opere di laminazione
richieste dall'invarianza idraulica.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Hydrogeo%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/hydrogeo/docs/it/workflow.md).*
