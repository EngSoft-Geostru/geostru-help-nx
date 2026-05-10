# Quickstart — la tua prima curva IDF in 5 minuti

In 5 minuti vedi Hydrogeo NX al lavoro su una stazione pluviometrica reale.

## 1. Apri l'app

Vai su [`nx.geostru.ai/hydrogeo/`](https://nx.geostru.ai/hydrogeo/).

## 2. Cerca una stazione

3 modi:

- **Mappa interattiva**: zoom sulla zona di interesse, click sui marker
  delle stazioni
- **Filtro per provincia**: dropdown in alto, scegli la provincia
- **Ricerca per nome**: digita "Roma", "Pisa", "Cosenza"…

Ogni stazione ha un **badge** con: codice ISPRA, fonte dati, anni di
osservazione, numero massimo di durate disponibili.

## 3. Visualizza i dati di intensità

Click sulla stazione → si apre il **pannello dati**:

- **Tabella delle massime annue** per durata (1h, 3h, 6h, 12h, 24h, …)
- **Anno** di osservazione + **valore** in mm
- **Grafico** delle massime annuali nel tempo

I dati sono presi dagli Annali Idrologici ISPRA o dal portale regionale,
**senza modifiche**.

## 4. Statistica: Gumbel EV1

Sezione **Analisi statistica** → click **Calcola Gumbel EV1**.

Hydrogeo:

1. Calcola **media** e **scarto quadratico medio** delle massime annue
2. Stima i **parametri** di Gumbel (α, u)
3. Calcola le **altezze di pioggia** per i tempi di ritorno standard
   (T = 2, 5, 10, 20, 50, 100, 200, 500, 1000 anni)
4. Verifica la **bontà del fit** con test di adattamento (Kolmogorov-Smirnov)

Output:

- **Tabella altezze di pioggia h(d, T)** in mm
- **Grafico carta probabilistica** (Gumbel paper) con i punti osservati
- **Stime per T = 100 anni** per ciascuna durata

## 5. Curva IDF

Sezione **Curva IDF** → seleziona il **tempo di ritorno** (es. T = 100 anni)
→ click **Genera curva IDF**.

Output:

- **Curva i = a · d^(n-1)** con parametri **a** e **n** stimati per minimi
  quadrati
- **Grafico** intensità i (mm/h) vs durata d (h), scala log-log
- **Tabella valori di i** per durate notevoli

La curva IDF è **l'input principale** per il calcolo idraulico (sfioratori,
fognature, vasche di laminazione).

## 6. Esporta

Toolbar → **Esporta**:

- **CSV** — tabella altezze di pioggia
- **Excel** — `.xlsx` con statistica + grafici
- **PDF** — relazione tecnica impaginata
- **PLV GeoStru** — formato standard di interscambio per software di
  calcolo idraulico (Idroclima, RunoffLab, software esterni che leggono PLV)

---

## Prossimi passi

- [**Workflow completo**](workflow.md) — analisi multi-stazione, TCEV, esposizioni
- [**FAQ**](faq.md) — domande sulle stazioni e i dati

---

*Pagina utile? [Scrivici](mailto:info@geostru.ai?subject=Help%20Hydrogeo%20NX%20-%20Quickstart).*
