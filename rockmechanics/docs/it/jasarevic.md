# Jašarević & Kovačević — indice n

Sviluppato da **Jašarević e Kovačević (1996)** sulle formazioni carbonatiche della Croazia, questo metodo ha un'evidente derivazione dal sistema RMR. La procedura è semplice: si attribuiscono almeno tre coefficienti numerici relativi a proprietà **geomeccaniche** dell'ammasso roccioso e almeno altrettanti relativi a proprietà **geologico-ingegneristiche**. Ad ogni proprietà assegni un valore $n_i$ variabile da 1 a 5.

## Tabella di attribuzione dei coefficienti

A sinistra trovi le proprietà geomeccaniche, a destra quelle geologico-ingegneristiche; l'ultima colonna riporta il coefficiente $n_i$.

| $S_u$ (MPa) | $I_{s\perp}$ (MPa) | $I_{s\parallel}$ (MPa) | $V_p$ (km/s) | $V_p/V_0$ | $\alpha$ | Acqua | RQD (%) | $J_v$ | $S$ (cm) | Giunti (JRC) | $n_i$ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| > 130 | > 5,7 | > 0,8 | > 6,5 | > 0,8 | 70–90 | A | > 65 | 1–2 | > 50 | 16–20 | 1 |
| 100–130 | 5,3–5,7 | 0,7–0,8 | 4,7–6,5 | 0,6–0,8 | 0–20 | U | 45–65 | 2–5 | 20–50 | 12–16 | 2 |
| 70–100 | 4,7–5,3 | 0,6–0,7 | 3,0–4,7 | 0,4–0,6 | 20–35 | B | 35–45 | 5–10 | 10–20 | 8–12 | 3 |
| 40–70 | 4,3–4,7 | 0,5–0,6 | 1,2–3,0 | 0,2–0,4 | 35–50 | S | 25–35 | 10–15 | 6–10 | 4–8 | 4 |
| < 40 | < 4,3 | < 0,5 | < 1,2 | < 0,2 | 50–70 | F | < 25 | > 15 | < 6 | < 4 o riempiti | 5 |

dove:

- **$S_u$** = resistenza a compressione uniassiale della roccia intatta (vedi [Resistenza a compressione uniassiale $S_u$](classificazioni.md#resistenza-a-compressione-uniassiale-su));
- **$I_{s\perp}$** = indice point load misurato perpendicolarmente alla discontinuità principale;
- **$I_{s\parallel}$** = indice point load misurato parallelamente alla discontinuità principale;
- **$V_p$** = velocità sismica delle onde longitudinali;
- **$V_0$** = velocità sismica di riferimento (roccia intatta);
- **$\alpha$** = inclinazione della discontinuità più sfavorevole;
- **Acqua** = A: assente — U: umido — B: bagnato — S: deboli venute — F: forti venute;
- **RQD** = grado di fratturazione dell'ammasso (vedi [RQD](classificazioni.md#rqd-rock-quality-designation));
- **$J_v$** = numero di giunti per m³;
- **$S$** = spaziatura delle discontinuità.

!!! note "Valori non univoci"
    Se i valori non ricadono in un'unica riga, prendi il coefficiente numerico intermedio: ad esempio, per $J_v$ compreso fra 5 e 15 si assume $n_i = 3{,}5$.

## Calcolo dell'indice n

L'indice n è la media dei coefficienti assegnati:

$$ n = \frac{1}{N_T}\sum_{i=1}^{N_T} n_i $$

dove $N_T$ è il numero delle proprietà considerate (minimo 6) nell'attribuzione dei coefficienti.

## Correlazione con RMR

Gli autori suggeriscono la seguente correlazione fra l'indice n e l'RMR corretto:

$$ RMR_c = 110 - 20\,n $$

Dal valore di $RMR_c$ derivi la classe e la qualità dell'ammasso, in analogia con la scala di Bieniawski:

| $RMR_c$ | 100–81 | 80–61 | 60–41 | 40–21 | ≤ 20 |
|---|---|---|---|---|---|
| Classe | I | II | III | IV | V |
| Descrizione | Molto buono | Buono | Mediocre | Scadente | Pessimo |

## Parametri caratteristici dell'ammasso

Da $RMR_c$ ricavi i parametri di resistenza e deformabilità dell'ammasso.

**Coesione** (Sen):

$$ c\ [\text{kPa}] = 3{,}625 \cdot RMR_c $$

**Angolo d'attrito** (Sen):

$$ \varphi\ [°] = 25\,(1 + 0{,}01\,RMR_c)\quad \text{per } RMR_c > 20 $$

$$ \varphi\ [°] = 1{,}5\,RMR_c\quad \text{per } RMR_c < 20 $$

**Modulo di deformazione** (Jašarević & Kovačević):

$$ E\ [\text{MPa}] = \exp(4{,}407 + 0{,}081 \cdot RMR_c) $$

Gli autori ritengono questa espressione di $E$ più corretta rispetto a quella di **Serafim e Pereira (1983)**:

$$ E\ [\text{GPa}] = 10^{\frac{RMR_b - 10}{40}} $$

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Rock%20Mechanics%20NX).*
