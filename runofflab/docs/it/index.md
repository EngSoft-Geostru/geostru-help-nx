# Runoff Lab NX — Manuale utente

**Runoff Lab NX** è lo strumento web GeoStru per l'**analisi delle piogge intense**
e la **trasformazione afflusso-deflusso**. Da una serie pluviometrica annuale per
durate brevi (60′, 3h, 6h, 12h, 24h) ricavi:

- **Elaborazioni probabilistiche** (Gumbel, GEV, Pearson III, TCEV regionali);
- **Curve di pioggia IDF** \(h = a \cdot t^n\) per tempo di ritorno;
- **Pluviogrammi sintetici** (Chicago design storm);
- **Idrogrammi di piena** con il metodo SCS-CN.

[**Apri Runoff Lab NX**](https://nx.geostru.ai/runofflab/){ .md-button .md-button--primary }
[Quickstart in 5 minuti](quickstart.md){ .md-button }

---

## Per chi è pensato

- **Ingegneri idraulici** che dimensionano fognature, vasche di laminazione, sfioratori, opere di attraversamento.
- **Geologi** che redigono studi di compatibilità idraulica.
- **Progettisti** che servono comuni e enti per valutazioni di portata e tempo di ritorno.

## Cosa puoi fare

| Funzione | Descrizione |
|----------|-------------|
| **Stazione + serie** | Anagrafica stazione + valori annui massimi per durata. |
| **Elaborazioni** | Stima parametri delle distribuzioni Gumbel, GEV, Pearson III, TCEV (4 livelli). |
| **Test di adattamento** | Kolmogorov-Smirnov e χ² automatici. |
| **Curve di pioggia** | \(h = a \cdot t^n\) per ciascun T, con regressione log-log. |
| **Pluviogrammi** | Chicago design storm da una curva IDF. |
| **Idrogrammi SCS-CN** | Pioggia netta + idrogramma unitario + convoluzione. |
| **AI Import** | Estrazione automatica della serie da PDF annuali o tabelle Excel. |
| **Esempi pronti** | Tre stazioni della Calabria (Cosenza, Rende, Montalto) per esplorare. |
| **Salvataggio** | File `.hgstudy` (JSON), autosave automatico nel browser. |
| **Export** | Relazione PDF completa con grafici e tabelle. |
| **Multilingua** | IT, EN, DE, ES, RO (le elaborazioni TCEV usano dataset VA.PI., solo per l'Italia). |

## Come iniziare

1. Apri [`nx.geostru.ai/runofflab/`](https://nx.geostru.ai/runofflab/).
2. **Stazione**: inserisci l'anagrafica e per ogni durata i valori annuali (h<sub>max</sub> in mm).
3. **Elaborazioni**: scegli una famiglia (Gumbel / GEV / Pearson III / TCEV) → ottieni h(T) per T = 5, 10, 50, 100, 200 anni.
4. **Curve**: da un'elaborazione + T, calcola \(a\) e \(n\) della legge \(h = a t^n\).
5. **Pluviogrammi** / **Idrogrammi**: usa la curva per costruire ietogrammi sintetici e l'idrogramma di piena con SCS-CN.
6. *File → Esporta relazione PDF* per la documentazione.

[Vedi il workflow completo →](workflow.md)

## Capitoli del manuale

### Iniziare

- [**Quickstart in 5 minuti**](quickstart.md)
- [**Workflow completo**](workflow.md)

### Riferimento dei metodi

- [**Elaborazioni probabilistiche**](elaborazioni.md) — Gumbel, GEV, Pearson III, TCEV
- [**Curve di pioggia**](curve.md) — \(h = a t^n\) e tempo di ritorno
- [**Pluviogrammi sintetici**](pluviogrammi.md) — Chicago design storm
- [**Idrogrammi SCS-CN**](scs-cn.md) — Curve Number, Tlag, convoluzione

### Strumenti

- [**AI Import**](ai-import.md) — estrazione serie da PDF/Excel
- [**FAQ**](faq.md) — gotcha frequenti

---

*Hai trovato un errore o vuoi suggerire un contenuto?
[Scrivici](mailto:info@geostru.ai?subject=Help%20Runoff%20Lab%20NX) — grazie!*
