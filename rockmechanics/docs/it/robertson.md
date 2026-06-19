# SRMR (Robertson)

Lo **Slope Rock Mass Rating** (SRMR, Robertson 1988) è applicabile **solo alla stabilità di versanti in roccia**. È derivato da RMR ed è stato sviluppato dallo studio di consulenza **Steffen Robertson & Kirsten**, che parte dalla constatazione che il sistema RMR, applicato in scavi di cava in ammassi teneri con $RMR < 40$, porta a una stima non corretta dei parametri di resistenza.

$$ SRMR = A_1 + A_2 + A_3 + A_4 $$

dove $A_1$ deriva dalla resistenza della roccia intatta, $A_2$ dall'RQD, $A_3$ dalla spaziatura delle discontinuità, $A_4$ dalle condizioni delle discontinuità.

### Valore di A1 (resistenza della roccia intatta)

Si ricava dall'indice di carico puntuale $I_s$ o dalla resistenza a compressione uniassiale $S_u$ (vedi [Resistenza a compressione uniassiale $S_u$](classificazioni.md#resistenza-a-compressione-uniassiale-su)).

| $I_s$ (MPa) | $S_u$ (MPa) | $A_1$ |
|---|---|---|
| > 10 | > 250 | 30 |
| 4–10 | 100–250 | 27 |
| 2–4 | 50–100 | 22 |
| 1–2 | 25–50 | 19 |
| (non applicabile, usare $S_u$) | 5–25 | 17 |
| — | 1–5 | 15 |
| — | 0,6–1 | 10 |
| — | 0,15–0,6 | 6 |
| — | 0,08–0,15 | 2 |
| — | 0,04–0,08 | 1 |
| — | < 0,04 | 0 |

### Valore di A2 (RQD)

L'RQD si ottiene dal recupero di carota o, in mancanza di carote di sondaggio, si stima dal rilievo delle discontinuità (vedi [RQD — Rock Quality Designation](classificazioni.md#rqd-rock-quality-designation)).

| RQD (%) | 90–100 | 75–90 | 50–75 | 25–50 | < 25 |
|---|---|---|---|---|---|
| $A_2$ | 20 | 17 | 13 | 8 | 3 |

### Valore di A3 (spaziatura)

| $s$ (m) | > 2 | 0,6–2 | 0,2–0,6 | 0,06–0,2 | < 0,06 |
|---|---|---|---|---|---|
| $A_3$ | 20 | 15 | 10 | 8 | 5 |

### Valore di A4 (condizioni delle discontinuità)

| Condizione | $A_4$ |
|---|---|
| Molto scabre, non continue, chiuse, pareti non alterate | 30 |
| Leggermente scabre, continue, apertura < 1 mm, pareti leggermente alterate | 25 |
| Leggermente scabre, continue, apertura < 1 mm, pareti alterate | 20 |
| Piane lisce, continue, apertura 1–5 mm, riempimento < 5 mm | 10 |
| Continue, apertura > 5 mm, riempimento > 5 mm (da applicare sempre se $S_u < 1$ MPa) | 0 |

!!! note "Il fattore idraulico"
    Il fattore legato alle condizioni idrauliche non viene considerato nel calcolo, perché la quantità d'acqua presente nell'ammasso non ne influenza direttamente la resistenza. Essendo però una forza destabilizzante, l'acqua va inserita come tale nella verifica di stabilità.

### Parametri caratteristici (SRMR < 40)

Per $SRMR < 40$ la rottura è funzione delle sole caratteristiche meccaniche dell'ammasso; Robertson attribuisce i seguenti valori, con un'ulteriore suddivisione in classi:

| SRMR | Classe | Coesione (kPa) | Angolo d'attrito (°) |
|---|---|---|---|
| 40–35 | IVa | 138 | 40 |
| 35–30 | IVa | 86 | 36 |
| 30–25 | IVb | 50–72 | 30–34 |
| 25–20 | IVb | 50–70 | 26–30 |
| 20–15 | Va | 50–60 | 24–27,5 |
| 15–5 | Vb | 14–50 | 21–24 |

Per gli inquadramenti bibliografici si rimanda alla [bibliografia](bibliografia.md).

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Rock%20Mechanics%20NX).*
