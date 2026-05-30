# Dynamic Probing NX

> Elaborazione di **prove penetrometriche dinamiche** (DPL · DPM · DPH · DPSH) e **SPT in foro** — stratigrafia automatica, correlazioni geotecniche, categoria di sottosuolo NTC 2018, portanza di fondazioni superficiali e profonde, valori caratteristici EC7 / NTC §6.2.2.

[**Apri l'app**](https://nx.geostru.ai/dynprobe/){ .md-button .md-button--primary }
[Guida rapida (5 minuti)](quickstart.md){ .md-button }

---

## In sintesi

- **Cosa fa**: legge le letture di campo di una prova dinamica continua o di una serie di prove SPT in foro, restituisce la stratigrafia interpretata con i parametri geotecnici caratteristici e le verifiche di portanza, il tutto conforme alle normative vigenti (NTC 2018, NTC 2008, EC8, Eurocodice 7).
- **Per chi**: geologi e ingegneri geotecnici che devono elaborare sondaggi dinamici, classificare il profilo stratigrafico e produrre la relazione di calcolo.
- **In quanti minuti**: 5 (caso con file .dypx di esempio) → 30 (caso reale completo con stratigrafia, correlazioni e portanza).

## Workflow tipico

1. Apri l'app: `nx.geostru.ai/dynprobe/`
2. Crea un nuovo file oppure importa un `.dypx` dal desktop GeoStru o un CSV da datalogger.
3. Vai in **Dati generali** e completa le informazioni del sito (nome, coordinate, strumento, committente).
4. Inserisci (o controlla) le **letture colpi** nel tab Letture: l'app le visualizza subito nel grafico N/profondità.
5. Passa alla **Stratigrafia interpretata**: definisci il numero di strati, i limiti e il tipo di terreno (coesivo / incoerente). L'app calcola N_SPT medio per strato con il metodo scelto.
6. Consulta le **Correlazioni geotecniche** — per ogni strato, tabella con i parametri derivati (Cu, φ, Mo, Ey, Vs, γ …).
7. Verifica la **Categoria di sottosuolo** secondo NTC 2018 / NTC 2008 / EC8.
8. Se necessario, calcola la **Portanza** di una fondazione superficiale o profonda (palo infisso Meyerhof).
9. Leggi i **Valori caratteristici** EC7 / NTC §6.2.2 nella tab dedicata.
10. Esporta la **relazione Word** (Report) o il file di progetto `.dprobe`.

## Capitoli del manuale

| Capitolo | Contenuto |
|---|---|
| [Guida rapida](quickstart.md) | Dal caricamento del file al primo risultato in 5 minuti |
| [Strumenti](strumenti.md) | DPL, DPM, DPH, DPSH, SPT in foro — come inserirli e i parametri rilevanti |
| [Stratigrafia interpretata](stratigrafia.md) | Come definire gli strati, i 7 metodi di aggregazione N_SPT |
| [Correlazioni geotecniche](correlazioni.md) | Parametri derivati per terreni coesivi e incoerenti, autori di riferimento |
| [Categoria di sottosuolo](categoria.md) | NTC 2018, NTC 2008, EC8 — input, logica di calcolo, lettura del risultato |
| [Portanza fondazioni](portanze.md) | Fondazioni superficiali (6 metodi) e profonde (Meyerhof palo infisso) |
| [Valori caratteristici](caratter.md) | EC7 §2.4.5.2 / NTC §6.2.2 — normale, lognormale, Student-t |
| [Esportazione e report](export.md) | Relazione Word, AGS4, GeoSection, planimetria, KMZ |
| [Formato file](formati.md) | `.dprobe` (JSON NX) · `.dypx` (desktop) · CSV datalogger |
| [Risorse e esempi](risorse.md) | File di esempio scaricabili |
| [FAQ](faq.md) | Domande frequenti |
