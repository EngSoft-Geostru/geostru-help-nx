# RSL III — Risposta sismica locale 1D

**RSL III** è il software web GeoStru per l'**analisi della risposta sismica
locale** (Site Response Analysis, SRA) di colonne 1D di terreno. A partire
dalla **stratigrafia** del sito (spessori, Vs, ρ, curve di degradazione G/Gmax-γ
e ξ-γ) e da un **accelerogramma di input** alla bedrock, calcola con schema
**lineare equivalente** (Idriss-Seed iterativo) la propagazione delle onde S
verso la superficie, restituendo lo **spettro di risposta**, i profili di
γ_max / a_max e i **fattori di amplificazione ICMS** per la microzonazione
sismica di Livello 3 (ICMS 2008/2018).

[**Apri RSL III**](https://nx.geostru.ai/rsl/){ .md-button .md-button--primary }
[Quickstart in 5 minuti](quickstart.md){ .md-button }

---

## Cosa fa, in sintesi

- **Input**: stratigrafia (spessore, Vs, ρ, curve dinamiche), accelerogramma
  alla bedrock (reale o sintetico), tipologia di analisi
- **Calcolo**: schema lineare equivalente con iterazioni successive, fino a
  convergenza di γ_eff (deformazione effettiva = 65% di γ_max)
- **Output**:
  - **Spettro di risposta** alla superficie (PSA o SA)
  - **Spettro di Fourier** input/output
  - **Profili** lungo la verticale: γ_max, a_max, σ_max
  - **Fattori di amplificazione ICMS**: FA, FH, FT (per zonazione sismica
    di livello 3)
- **Modalità multi-sito**: confronto tra colonne diverse (con uno o più
  accelerogrammi), spettro medio + statistica

## Per chi

- **Geologi** che producono studi di **microzonazione sismica** (ICMS Livello
  2 o 3) per i Comuni
- **Ingegneri sismici** che dimensionano edifici e opere strutturali
  con accelerogramma di sito invece dello spettro NTC standard
- **Studi di consulenza** che integrano l'analisi SRA in una relazione
  geotecnica per l'edilizia in zona sismica

## Come iniziare

1. Apri [`nx.geostru.ai/rsl/`](https://nx.geostru.ai/rsl/)
2. Carica un esempio o definisci la stratigrafia
3. Carica un accelerogramma (o usa uno di esempio)
4. Premi **Esegui calcolo**
5. Esamina spettro di risposta + profili + ICMS
6. Esporta il **Report Word**

[Vedi il workflow completo →](workflow.md)

## Capitoli del manuale

### Iniziare

- [**Quickstart**](quickstart.md) — 5 minuti dal primo accesso al primo report
- [**Workflow completo**](workflow.md) — sequenza dettagliata input → calcolo
  → export

### Input

- [**Dati di input**](dati-input.md) — stratigrafia, curve di degradazione,
  accelerogramma di input, parametri di iterazione

### Calcolo

- [**Metodo lineare equivalente**](metodo.md) — schema iterativo Idriss-Seed,
  funzione di trasferimento, convergenza, limiti del modello

### Output

- [**Fattori di amplificazione (ICMS)**](icms.md) — FA, FH, FT per la
  microzonazione sismica di Livello 3, conformità ICMS 2008/2018

### Riferimento

- [**FAQ**](faq.md) — domande frequenti

---

*Hai trovato un errore o vuoi suggerire un contenuto?
[Scrivici](mailto:info@geostru.ai?subject=Help%20RSL%20III) — grazie!*
