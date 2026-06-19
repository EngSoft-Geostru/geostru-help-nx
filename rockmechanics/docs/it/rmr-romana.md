# Bieniawski & Romana — RMR e SMR

Le classificazioni di **Bieniawski (1976)** e **Romana (1985)** costituiscono il riferimento empirico più diffuso per caratterizzare un ammasso roccioso quando le informazioni dirette su resistenza e deformabilità sono scarse. La seconda deriva dalla prima, che per i versanti risultava troppo conservativa.

La classificazione di Bieniawski si basa su sei parametri rilevati in campagna o in laboratorio:

| | Parametro | Significato |
|---|---|---|
| **A1** | resistenza a compressione uniassiale $S_u$ | resistenza della roccia intatta |
| **A2** | Rock Quality Designation (RQD) | grado di fratturazione |
| **A3** | spaziatura delle discontinuità | dimensione dei blocchi |
| **A4** | condizioni delle discontinuità | persistenza, apertura, rugosità, alterazione, riempimento |
| **A5** | condizioni idrauliche | venute d'acqua |
| **A6** | orientamento delle discontinuità | correzione fronte/giunto |

Da questi si ricava il **Rock Mass Rating (RMR)** e, con le correzioni di Romana, lo **Slope Mass Rating (SMR)**. Nella pratica RMR è differenziato in:

$$ RMR_b = A1 + A2 + A3 + A4 + A5 \qquad RMR_c = RMR_b + A6 $$

ovvero **RMR di base** (senza orientamento) e **RMR corretto**.

## A1 — resistenza a compressione

$S_u$ si ricava da Point Load Test, sclerometro o stima ISRM: vedi [parametri comuni](classificazioni.md#resistenza-a-compressione-uniassiale-su).

Dallo Standard ISRM, Bieniawski (1989) attribuisce ad A1:

| $S_u$ (MPa) | > 200 | 100–200 | 50–100 | 25–50 | 5–25 | 1–5 | < 1 |
|---|---|---|---|---|---|---|---|
| **A1** | 15 | 12 | 7 | 4 | 2 | 1 | 0 |

Se si dispone di $S_u$ da Point Load o sclerometro, l'app ricava A1 dalle **equazioni continue** che interpolano i grafici originali di Bieniawski, per intervalli di $S_u$: ≤ 44,5 · 44,5–93,75 · 93,75–140 · 140–180 · 180–240 · > 240 MPa (oltre 240 MPa, $A1 = 15$). Il risultato è continuo e meno soggettivo della lettura a gradini.

## A2 — RQD

RQD si ricava da carote di sondaggio o, in loro mancanza, dal numero di discontinuità (Palmström, Priest-Hudson): vedi [RQD](classificazioni.md#rqd-rock-quality-designation). A2 si ottiene poi dalle equazioni che interpolano i grafici di Bieniawski, per intervalli di RQD (≤ 26,5 · 26,5–39 · … · > 90 %).

## A3 — spaziatura

Calcolata la spaziatura media $s$ (distanza media fra discontinuità adiacenti), A3 si ricava dalle equazioni di Bieniawski per intervalli di $s$: ≤ 0,2 · 0,2–0,4 · 0,4–0,66 · 0,66–0,94 · 0,94–1,6 · 1,6–2,0 · > 2,0 m.

## A4 — condizioni delle discontinuità { #a4-condizioni-delle-discontinuita }

Leggere A4 dalle tavole di Bieniawski è soggettivo. Conviene sommare cinque sotto-parametri:

$$ A4 = v_1 + v_2 + v_3 + v_4 + v_5 $$

**$v_1$ — Persistenza del giunto**

| Persistenza (m) | ≤ 1 | 1–3 | 3–10 | 10–20 | > 20 |
|---|---|---|---|---|---|
| $v_1$ | 6 | 4 | 2 | 1 | 0 |

**$v_2$ — Apertura del giunto**

| Apertura (mm) | Completamente chiuso | < 0,1 | 0,1–1 | 1–5 | > 5 |
|---|---|---|---|---|---|
| $v_2$ | 6 | 5 | 4 | 1 | 0 |

**$v_3$ — Rugosità del giunto**

| Rugosità | Molto rugosa | Rugosa | Leggermente rugosa | Liscia | Levigata |
|---|---|---|---|---|---|
| $v_3$ | 6 | 5 | 3 | 1 | 0 |

**$v_4$ — Alterazione delle pareti**

| Alterazione | Non alterate | Leggermente | Mediamente | Molto alterate | Decomposte |
|---|---|---|---|---|---|
| $v_4$ | 6 | 5 | 3 | 1 | 0 |

**$v_5$ — Riempimento delle discontinuità**

| Riempimento | Assente | Compatto < 5 mm | Compatto > 5 mm | Soffice < 5 mm | Soffice > 5 mm |
|---|---|---|---|---|---|
| $v_5$ | 6 | 4 | 2 | 2 | 0 |

## A5 — condizioni idrauliche { #a5-condizioni-idrauliche }

Riferite a un fronte di 10 m:

| Venute su 10 m | Nessuna | < 10 l/min | 10–25 l/min | 25–125 l/min | > 125 l/min |
|---|---|---|---|---|---|
| Condizione | Asciutta | Umida | Bagnata | Deboli venute | Forti venute |
| **A5** | 15 | 10 | 7 | 4 | 0 |

## A6 — orientamento delle discontinuità { #a6-orientamento-delle-discontinuita }

Coefficiente di correzione secondo l'opera:

| Applicazione | Molto favorevole | Favorevole | Mediocre | Sfavorevole | Molto sfavorevole |
|---|---|---|---|---|---|
| Gallerie | 0 | −2 | −5 | −10 | −12 |
| Fondazioni | 0 | −2 | −7 | −15 | −25 |

!!! warning "Versanti"
    Per i versanti A6 secondo Bieniawski è troppo conservativo: nel calcolo si usa la metodologia di Romana (SMR, sotto).

## Classi RMR e parametri caratteristici

Dal valore di $RMR_c$ si identificano 5 classi:

| $RMR_c$ | 100–81 | 80–61 | 60–41 | 40–21 | ≤ 20 |
|---|---|---|---|---|---|
| Classe | I | II | III | IV | V |
| Descrizione | Molto buono | Buono | Mediocre | Scadente | Molto scadente |

Dal $RMR_b$ si derivano i parametri caratteristici (Bieniawski):

$$ c_p\ [\text{kPa}] = 5 \cdot RMR_b \qquad \varphi_p\ [°] = 0{,}5 \cdot RMR_b + 5 \qquad E\ [\text{GPa}] = 2 \cdot RMR_b - 100 $$

I valori **residui** di coesione e attrito si ottengono con un $RMR_b$ ridotto secondo Priest (1983):

$$ RMR_b^{res} = RMR_b - 0{,}2 \cdot RMR_b $$

La formula di $E$ vale per $RMR > 50$; per valori inferiori si usa **Serafim e Pereira (1983)**:

$$ E = 10^{\frac{RMR - 10}{40}} \quad [\text{GPa}] $$

Il **GSI** (Geological Strength Index) si ricava da:

$$ GSI = RMR - 5 $$

con RMR calcolato sui primi quattro parametri e condizioni idrauliche asciutte ($A5 = 15$); valido per $RMR > 23$.

## Slope Mass Rating (SMR, Romana 1985)

Romana aggiunge a $RMR_b$ fattori di aggiustamento per l'orientamento relativo fra discontinuità e fronte, più un fattore per il metodo di scavo:

$$ SMR = RMR_b + (F_1 \cdot F_2 \cdot F_3) + F_4 $$

- **$F_1$** dipende dal parallelismo fra immersione del fronte e dei giunti;
- **$F_2$** è riferito all'inclinazione del giunto (rottura planare);
- **$F_3$** mantiene le relazioni di Bieniawski per l'inclinazione fronte/giunto;
- **$F_4$** corregge per il metodo di scavo (empirico).

Le condizioni verificate sono **rotture planari** e **per ribaltamento (toppling)**; il metodo è stato esteso anche alle rotture **a cuneo** (Anbalagan et al.).

### Fattore F~1~

| caso (Planare $\alpha_j-\alpha_f$ · Toppling $\alpha_j-\alpha_f-180°$ · Cuneo $\alpha_i-\alpha_f$) | $F_1$ |
|---|---|
| > 30° | 0,15 |
| 30°–20° | 0,40 |
| 20°–10° | 0,70 |
| 10°–5° | 0,85 |
| < 5° | 1,00 |

### Fattore F~2~

| Planare $\beta_j$ · Cuneo $\beta_i$ | $F_2$ (planare/cuneo) | $F_2$ (toppling) |
|---|---|---|
| < 20° | 0,15 | 1,00 |
| 20°–30° | 0,40 | 1,00 |
| 30°–35° | 0,70 | 1,00 |
| 35°–45° | 0,85 | 1,00 |
| > 45° | 1,00 | 1,00 |

### Fattore F~3~

| Planare/Cuneo $\beta_j-\beta_f$ | Toppling $\beta_j+\beta_f$ | $F_3$ |
|---|---|---|
| > 10° | < 110° | 0 |
| 10°–0° | 110°–120° | −6 |
| 0° | > 120° | −25 |
| 0°–(−10°) | — | −50 |
| < −10° | — | −60 |

### Fattore F~4~ (metodo di scavo)

| Metodo | $F_4$ |
|---|---|
| Scarpata naturale | +15 |
| Abbattimento con pretaglio | +10 |
| Abbattimento controllato | +8 |
| Abbattimento normale | 0 |
| Abbattimento non controllato | −8 |

dove $\alpha_j$ = immersione del giunto, $\alpha_i$ = immersione della retta di intersezione (cuneo), $\alpha_f$ = immersione del fronte, $\beta_j$ = inclinazione del giunto, $\beta_i$ = inclinazione della retta di intersezione, $\beta_f$ = inclinazione del fronte.

### Classi SMR

| SMR | 100–81 | 80–61 | 60–41 | 40–21 | 21–0 |
|---|---|---|---|---|---|
| Classe | I | II | III | IV | V |
| Descrizione | Molto buona | Buona | Mediocre | Scadente | Molto scadente |
| Stabilità | Sicuramente stabile | Stabile | Parzialmente stabile | Instabile | Sicuramente instabile |
| Modo di rottura | Assente | Possibili blocchi | Lungo piani o per cunei | Lungo piani o su grandi cunei | Su grandi piani o rototraslazionale |
| Stabilizzazione | Nessuna | Occasionale | Sistematica | Estesa | Riprofilare la scarpata |

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Rock%20Mechanics%20NX).*
