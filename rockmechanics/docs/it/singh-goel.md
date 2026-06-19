# Singh & Goel — indice N

Singh e Göel (1999), per l'applicazione nel campo delle **gallerie**, propongono di calcolare il **Rock Mass Number** $N$ a partire dalla classificazione Q di Barton, escludendo l'effetto tensionale (cioè ponendo $SRF = 1$):

$$ N = \frac{RQD}{J_n} \cdot \frac{J_r}{J_a} \cdot J_w $$

In altri termini, $N$ è l'indice Q privato del fattore $SRF$: vedi la pagina [Barton](barton.md) per il calcolo completo di Q.

## Parametri di input

Gli indici $J_n$, $J_r$, $J_a$, $J_w$ sono definiti nelle tabelle comuni:

- [Parametro $J_n$](classificazioni.md#jn)
- [Parametro $J_r$](classificazioni.md#jr)
- [Parametro $J_a$](classificazioni.md#ja)
- [Parametro $J_w$](classificazioni.md#jw)

Per **RQD** prende il suo valore nominale; se $RQD < 10$ si assume comunque 10 (vedi [RQD](classificazioni.md#rqd-rock-quality-designation)).

## Coefficiente A1

Il parametro $A_1$ si ricava dalla **resistenza a compressione uniassiale** $S_u$ della roccia intatta, determinata con prova Point Load, sclerometro o standard ISRM: vedi [Resistenza a compressione uniassiale Su](classificazioni.md#resistenza-a-compressione-uniassiale-su).

L'app ricava $A_1$ dalle equazioni continue che interpolano i grafici di Bieniawski, suddivise per intervalli di $S_u$:

| Intervallo di $S_u$ (MPa) |
|---|
| $\leq 44{,}5$ |
| $44{,}5 - 93{,}75$ |
| $93{,}75 - 140$ |
| $140 - 180$ |
| $180 - 240$ |
| $> 240$ |

Oltre 240 MPa si assume $A_1 = 15$.

!!! tip "Equazioni continue"
    Se disponi di prove Point Load o sclerometriche, conviene ricavare $A_1$ dalle equazioni dei grafici di Bieniawski anziché dalle tabelle a gradini: il risultato è continuo e meno soggettivo.

## Coefficiente A6 (orientamento delle discontinuità)

Per l'orientamento delle discontinuità si applica il coefficiente di correzione $A_6$:

| Molto favorevole | Favorevole | Mediocre | Sfavorevole | Molto sfavorevole |
|---|---|---|---|---|
| 0 | −2 | −5 | −10 | −12 |

## Risultati derivati dal calcolo di N

Dal valore di $N$ si ottiene il **Rock Condition Rating** (Singh-Goel):

$$ RCR = 8\,\ln(N) + 30 $$

e da questo i valori corretto e di base dell'RMR:

$$ RMR_{corretto} = RCR + (A_1 + A_6) \qquad RMR_{base} = RCR + A_1 $$

Dalla relazione di Bieniawski $RMR = 9\,\ln(Q) + 44$ si ricava l'indice Q di Barton:

$$ Q = e^{\frac{RMR - 44}{9}} $$

e quindi lo Stress Reduction Factor e l'indice Q normalizzato:

$$ SRF = \frac{N}{Q} \qquad Q_c = Q \cdot \frac{\sigma_c}{100} $$

dove $\sigma_c$ è la resistenza a compressione monoassiale della roccia.

## Classi dell'ammasso

In funzione di $RMR_c$ l'ammasso è ripartito in cinque classi:

| $RMR_c$ | 100–81 | 80–61 | 60–41 | 40–21 | ≤ 20 |
|---|---|---|---|---|---|
| Classe | I | II | III | IV | V |
| Descrizione | Molto buono | Buono | Mediocre | Scadente | Molto scadente |

L'indice Q ricavato varia da 0,001 a 1000 ed è suddiviso in 9 classi:

| Q | Classe | Descrizione |
|---|---|---|
| 0,001 – 0,01 | IX | Eccezionalmente scadente |
| 0,01 – 0,1 | VIII | Estremamente scadente |
| 0,1 – 1 | VII | Molto scadente |
| 1 – 4 | VI | Scadente |
| 4 – 10 | V | Mediocre |
| 10 – 40 | IV | Buona |
| 40 – 100 | III | Molto buona |
| 100 – 400 | II | Estremamente buona |
| 400 – 1000 | I | Ottima |

## Parametri caratteristici

Dal valore di $RMR_b$ (Bieniawski) si derivano i parametri caratteristici di picco dell'ammasso:

$$ c_p\ [\text{kPa}] = 5\,RMR_b \qquad \varphi_p\ [°] = 0{,}5\,RMR_b + 5 \qquad E\ [\text{GPa}] = 1{,}5\,RMR_b - 100 $$

I valori residui di coesione e angolo d'attrito si ottengono introducendo nelle formule un $RMR_b$ modificato secondo $RMR_b^{res} = RMR_b - 0{,}2\,RMR_b$ (Priest, 1983).

La formula di $E$ vale per $RMR > 50$; per valori inferiori si usa l'espressione di Serafim e Pereira (1983):

$$ E\ [\text{GPa}] = 10^{\frac{RMR_b - 10}{40}} $$

In alternativa, come per [Barton](barton.md), si possono estrarre da N/Q le componenti attritiva e coesiva dell'ammasso:

$$ \varphi' = \arctan\!\left(\frac{J_r \cdot J_w}{J_a}\right) \qquad c' = \frac{RQD}{J_n} \cdot \frac{1}{SRF} \cdot \frac{\sigma_c}{100} $$

I riferimenti bibliografici sono raccolti nella pagina [Bibliografia](bibliografia.md).

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Rock%20Mechanics%20NX).*
