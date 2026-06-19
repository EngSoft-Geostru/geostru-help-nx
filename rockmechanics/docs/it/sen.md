# RMR modificato (Sen)

**Sen e Sadagah (2003)** modificano la determinazione dell'RMR proposta da Bieniawski **senza modificarne la classificazione**. Invece di leggere i punteggi $A1$, $A2$, $A3$ dalle tabelle a gradini, propongono di calcolare l'RMR con un'**equazione continua semplificata** a partire dai soli parametri di RQD, resistenza della roccia $S_u$ (MPa) e spaziatura $s$ (m), esprimendo le condizioni idrauliche in funzione della portata $G$.

I coefficienti di Bieniawski per la **condizione delle discontinuità** (A4) e per l'**orientamento** (A6) sono mantenuti invariati. Il risultato è un RMR continuo, meno soggettivo della lettura per intervalli.

## Parametri di input

I parametri entrano direttamente nell'equazione, senza passare per i punteggi a gradini.

- **$S_u$** — resistenza a compressione uniassiale (MPa), da Point Load Test ($S_u = K\,I_s$), sclerometro ($S_u = 0{,}775\,R + 21{,}3$) o stima ISRM: vedi [resistenza a compressione](classificazioni.md#resistenza-a-compressione-uniassiale-su).
- **RQD** — Rock Quality Designation, da carote di sondaggio o, in loro mancanza, dal numero medio di giunti: vedi [RQD](classificazioni.md#rqd-rock-quality-designation).
- **$s$** — spaziatura media delle discontinuità (m).
- **$G$** — portata che esprime le condizioni idrauliche.

I coefficienti $A4$, $A5$ e $A6$ restano quelli di Bieniawski. Le relative tabelle sono già riportate nella pagina di Bieniawski:

- [A4 — condizioni delle discontinuità](rmr-romana.md#a4-condizioni-delle-discontinuita) (sotto-parametri $v_1$–$v_5$);
- [A5 — condizioni idrauliche](rmr-romana.md#a5-condizioni-idrauliche);
- [A6 — orientamento delle discontinuità](rmr-romana.md#a6-orientamento-delle-discontinuita).

## Calcolo di RMR corretto

L'RMR corretto si ottiene direttamente dall'equazione continua:

$$ RMR_c = 0{,}2\,RQD + 15\log(s) + 0{,}075\,S_u - 2{,}9\log(G) + 34 + (A_5 + A_6) $$

dove $s$ è la spaziatura (m), $S_u$ la resistenza in MPa e $G$ la portata che esprime le condizioni idrauliche.

Qualora manchi un sondaggio da cui derivare RQD, si introduce il **numero medio di giunti** $n$ e l'equazione diventa:

$$ RMR_c = 20\,(1 + 0{,}1n)\,e^{-0{,}1n} - 15\log(n) + 0{,}075\,S_u - 2{,}9\log(G) + 34 + (A_5 + A_6) $$

## Classi dell'ammasso

Dal valore di $RMR_c$ si identificano 5 classi, le stesse di Bieniawski:

| $RMR_c$ | 100–81 | 80–61 | 60–41 | 40–21 | ≤ 20 |
|---|---|---|---|---|---|
| Classe | I | II | III | IV | V |
| Descrizione | Molto buono | Buono | Mediocre | Scadente | Molto scadente |

## Parametri caratteristici

Dal $RMR_c$ si derivano coesione e angolo d'attrito dell'ammasso (Sen et al.):

$$ c\ [\text{kPa}] = 3{,}625 \cdot RMR_c $$

$$ \varphi\ [°] = 25\,(1 + 0{,}01\,RMR_c)\ \text{ per } RMR_c > 20; \qquad \varphi = 1{,}5\,RMR_c\ \text{ per } RMR_c < 20 $$

Per i legami fra le diverse classificazioni e i riferimenti bibliografici, vedi la [bibliografia](bibliografia.md).

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Rock%20Mechanics%20NX).*
