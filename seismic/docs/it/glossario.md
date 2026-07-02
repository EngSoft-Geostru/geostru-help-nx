# Glossario

Termini e simboli usati in PS Advanced e nelle NTC 2018.

## Simboli principali

| Simbolo | Nome | Note |
|---|---|---|
| $a_g$ | Accelerazione orizzontale massima | su sito rigido (cat. A) e orizzontale (T1), in g |
| $F_0$ | Fattore di amplificazione dello spettro | valore massimo, $\ge 2.2$ |
| $T_C^*$ | Periodo di inizio del tratto a velocità costante | valore di riferimento, in s |
| $T_B, T_C, T_D$ | Periodi caratteristici dello spettro | $T_B = T_C/3$, $T_C = C_C T_C^*$ |
| $S_S$ | Coefficiente di amplificazione stratigrafica | dipende dalla categoria di sottosuolo |
| $C_C$ | Coefficiente su $T_C$ | $T_C = C_C \cdot T_C^*$ |
| $S_T$ | Coefficiente di amplificazione topografica | 1.0 – 1.4 |
| $S$ | Coefficiente complessivo | $S = S_S \cdot S_T$ |
| $a_{max}$ | Accelerazione massima al sito | $a_{max} = S \cdot a_g$ |
| $\eta$ | Fattore di modifica per lo smorzamento | $\eta = \sqrt{10/(5+\xi)} \ge 0.55$ |
| $q$ | Fattore di comportamento | riduce lo spettro elastico a quello di progetto |
| $k_h, k_v$ | Coefficienti sismici orizzontale/verticale | per verifiche pseudo-statiche |
| $\beta_s$ | Coefficiente di riduzione di $a_{max}$ | nel calcolo di $k_h$ |
| $V_N$ | Vita nominale | anni |
| $C_U$ | Coefficiente d'uso | 0.7 / 1.0 / 1.5 / 2.0 |
| $V_R$ | Periodo di riferimento | $V_R = V_N \cdot C_U$ |
| $T_R$ | Periodo di ritorno | dell'azione sismica, in anni |
| $P_{V_R}$ | Probabilità di superamento | nel periodo di riferimento |

## Stati limite

- **SLO** — Stato Limite di Operatività (esercizio).
- **SLD** — Stato Limite di Danno (esercizio).
- **SLV** — Stato Limite di salvaguardia della Vita (ultimo).
- **SLC** — Stato Limite di Collasso (ultimo).

## Altri termini

- **Reticolo di riferimento** — griglia nazionale di nodi su cui la
  pericolosità sismica di base è tabellata (studio INGV adottato dalle NTC).
- **Pericolosità sismica di base** — descrizione dell'azione sismica attesa su
  suolo rigido orizzontale, funzione della sola posizione geografica.
- **Categoria di sottosuolo** — classe (A–E) che descrive la rigidezza dei
  terreni nei primi 30 m ($V_{S,eq}$).
- **Categoria topografica** — classe (T1–T4) che descrive l'effetto morfologico
  del rilievo.
- **Spettro di risposta elastico** — accelerazione massima di un oscillatore
  elementare al variare del periodo, con smorzamento assegnato.
- **Spettro di progetto** — spettro elastico ridotto tramite il fattore di
  comportamento $q$.
- **Datum** — sistema di riferimento geodetico (es. WGS84, ED50) delle
  coordinate.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20PS%20Advanced%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/seismic/docs/it/glossario.md).*
