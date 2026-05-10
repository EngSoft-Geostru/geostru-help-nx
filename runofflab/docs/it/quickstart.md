# Quickstart — il tuo primo idrogramma in 5 minuti

In 5 minuti vedi Runoff Lab NX al lavoro su un bacino di esempio.

## 1. Apri l'app

Vai su [`nx.geostru.ai/runofflab/`](https://nx.geostru.ai/runofflab/).

## 2. Carica un dataset di esempio

**Studio → Carica esempio** → scegli un caso pronto (bacino tipico di
collina mediterranea, ~10 km²).

L'app pre-popola:

- **Curva di pioggia** IDF già parametrizzata
- **Bacino** con area, CN, Tlag stimati
- **Tempo di ritorno** T = 100 anni

## 3. Esamina la curva di pioggia

Tab **Curva di pioggia**. Vedi:

- **Equazione IDF** `i = a · d^(n-1)` con valori di a e n
- **Grafico log-log** dell'intensità vs durata
- **Tempo di ritorno** scelto

## 4. Esamina il bacino

Tab **Bacino**. Parametri principali:

| Campo | Esempio |
|---|---|
| **Area** A | 10.5 km² |
| **CN** (SCS Curve Number) | 75 (terreno medio) |
| **Tlag** (tempo di lag) | 3.2 h |
| **Tc** (tempo di corrivazione) | 5.5 h |

Sotto, il **wizard CN/Tlag** se vuoi ricalcolare i parametri:

- Da **Geologia** + **Copertura del suolo** (libreria SCS)
- Da **Lunghezza del corso** + **Pendenza** (formule Kirpich, Giandotti, …)

## 5. Esegui calcolo

Tab **Idrogramma** → click **Esegui**.

Runoff Lab calcola in 1-2 secondi:

1. **Ietogramma di progetto** (alternating block method o triangolare)
2. **Pioggia netta** (con metodo SCS-CN)
3. **Idrogramma unitario** (UH metodo SCS)
4. **Convoluzione** ietogramma × UH → **idrogramma di piena Q(t)**

Output:

- **Grafico Q vs t** (l'idrogramma)
- **Q_max** (portata di picco) in m³/s
- **t_p** (tempo del picco) in ore
- **Volume totale** scaricato in 10⁶ m³

## 6. Esporta

Toolbar → **Esporta**:

- **PDF** — relazione tecnica con curve, parametri, idrogramma
- **CSV** — Q(t) tabellare per analisi successive
- **Excel** — `.xlsx` con tutte le tabelle
- **PLV GeoStru** — dati di input pluviometrici (interscambio Hydrogeo)

---

## Prossimi passi

- [**Workflow completo**](workflow.md) — i 4 tipi di curve + AI import
- [**FAQ**](faq.md) — domande sulla trasformazione

---

*Pagina utile? [Scrivici](mailto:info@geostru.ai?subject=Help%20Runoff%20Lab%20NX%20-%20Quickstart).*
