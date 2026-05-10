# Workflow completo

Sequenza di un'analisi afflusso-deflusso reale, dalla curva di pioggia
all'idrogramma di piena.

## Schema generale

```
INPUT                              CALCOLO                  OUTPUT
─────                              ───────                  ──────
1. Curva di pioggia              5. Ietogramma             7. Idrogramma Q(t)
   - IDF tradizionale              progetto                8. Q_max, t_p, V
   - VAPI                        6. Pioggia netta          9. Report PDF
   - PLV (da Hydrogeo)             (SCS-CN)                10. CSV / Excel / PLV
   - Custom                      7. Convoluzione UH
2. Bacino (area, CN, Tlag)
3. Tempo di ritorno T
4. Metodo trasformazione
```

## 1. Curva di pioggia (4 modi)

### A. Curva IDF tradizionale

Parametri **a**, **n** della formula `i = a · d^(n-1)`. Inseriti a mano o
da letteratura (atlante IDF locale).

### B. VAPI (Valutazione delle Piene in Italia)

Metodo statistico nazionale: parametri territoriali standardizzati
basati sulla zonazione VAPI. Selezioni la **zona** (es. ZONA 1 — Sicilia
orientale) e il **tempo di ritorno** → curva IDF generata
automaticamente.

### C. PLV da Hydrogeo NX

Esporti un `.plv` da [Hydrogeo NX](https://help.nx.geostru.ai/hydrogeo/it/)
(analisi statistica di una stazione pluviometrica reale) → carichi in
Runoff Lab → la curva IDF viene popolata con i dati statistici della
stazione.

**Workflow consigliato per studi rigorosi**.

### D. Curva custom

Inserisci i parametri a mano. Utile per:

- Curve da letteratura specifiche del sito
- Ricostruzione di studi storici
- Sensibilità su parametri di prova

## 2. Definisci il bacino

### Parametri principali

| Campo | Significato | Range tipico |
|---|---|---|
| **Area** A | superficie (km²) | 0.1 - 10 000 |
| **CN** | Curve Number SCS, indice di permeabilità | 30 (impermeabile) - 100 (urbano) |
| **Tlag** | tempo di lag, ritardo Q vs pioggia | 0.5 - 24 h |
| **Tc** | tempo di corrivazione, durata critica | 1 - 48 h |
| **Pendenza media** | (per stime indirette di Tc) | 0.1° - 30° |

### Wizard CN

Stima automatica del CN da:

- **Tipo idrologico di suolo** (A/B/C/D — da geologia)
- **Copertura del suolo** (urbana, agricola, boschiva, …)
- **Stato di umidità antecedente** AMC (II default; I per asciutto, III per saturo)

Tabelle SCS standard (TR-55) integrate nella libreria.

### Wizard Tlag/Tc

Stima automatica da:

- **Lunghezza del corso d'acqua principale** (m)
- **Pendenza media** del bacino
- **Formula** scelta:
  - **Kirpich** (1940) — per bacini piccoli/medi (< 200 ha)
  - **Giandotti** (1934) — Italia, 0.1 - 1000 km²
  - **Pasini** — per pianure
  - **Ventura** — bacini medi
  - **SCS Lag** — formula americana

### AI Import

Trascina un PDF di studio idrogeologico esistente (preventivo, parere
tecnico, relazione di compatibilità). L'AI:

- Riconosce i parametri del bacino dal testo
- Estrae area, CN, Tlag, lunghezza, pendenza
- Pre-popola i campi
- Indica le **fonti** (pagine del PDF) per verifica

## 3. Tempo di ritorno T

Standard: T = 2, 5, 10, 20, 50, 100, 200, 500, 1000 anni.

Scelta dipende dall'opera (vedi [FAQ](faq.md)).

## 4. Metodo di trasformazione

### SCS Curve Number (default per Italia)

1. Calcolo della **pioggia netta** dalla pioggia lorda con la formula
   SCS-CN: `Pe = (P - Ia)² / (P - Ia + S)` con `S = 25400/CN - 254`
2. **Ietogramma di pioggia netta** (alternating block method)
3. **Idrogramma unitario SCS** (curva sintetica)
4. **Convoluzione** → idrogramma totale

### Metodo cinematico (Razionale)

Per bacini piccoli (< 5 km²):

$$
Q_{\max} = c \cdot i_{T_c} \cdot A
$$

con `c` coefficiente di deflusso, `i_Tc` intensità di pioggia per durata
Tc.

### Idrogramma unitario triangolare (Mockus)

Alternativa al SCS-UH, con forma triangolare semplificata. Parametri:
tempo al picco e tempo totale.

## 5. Idrogramma di piena

Output del calcolo:

- **Grafico Q(t)** — portata in m³/s vs tempo in ore
- **Q_max** (m³/s) — portata di picco
- **t_p** (h) — tempo dal'inizio della pioggia al picco
- **Volume totale** (10⁶ m³) — integrale di Q(t)
- **Volumi cumulati** Q(t) integrato

## 6. Esporta

Toolbar **Esporta**:

| Formato | Uso |
|---|---|
| **PDF** | Relazione tecnica con tabelle + grafici |
| **CSV** | Q(t) tabellare per analisi |
| **Excel** | Stessa tabella + grafici |
| **PLV** | Dati pluviometrici di interscambio (input per altri software) |

---

## Schema riassuntivo

```mermaid
flowchart TD
    A{Curva di pioggia} -->|IDF a,n| B[Curva]
    A -->|VAPI zona| B
    A -->|PLV Hydrogeo| B
    A -->|Custom| B
    C{Bacino} -->|Manuale| D[A, CN, Tlag]
    C -->|Wizard| D
    C -->|AI PDF| D
    B & D --> E[Tempo di ritorno T]
    E --> F{Metodo}
    F -->|SCS-CN| G[Convoluzione UH]
    F -->|Cinematico| H[Q_max razionale]
    F -->|IUH triangolare| I[Mockus]
    G & H & I --> J[Idrogramma Q(t)]
    J --> K[Esporta PDF/CSV/PLV]
```

---

*Pagina utile? [Scrivici](mailto:info@geostru.ai?subject=Help%20Runoff%20Lab%20NX%20-%20Workflow).*
