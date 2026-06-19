# Utility

Due strumenti di supporto inclusi in Rock Mechanics NX: la stima della **forza d'impatto di un masso** su una struttura e la valutazione della **suscettibilità al crollo per evento sismico**.

## Forza d'impatto di un masso

La forza d'impatto di un masso su una struttura muraria o in calcestruzzo si valuta a partire dalle esperienze di McCarty & Carden (1962), Kar (1978) e Knight (1980), riprese da **Paronuzzi (1989)**.

### Grandezze in gioco

| Simbolo | Grandezza |
|---|---|
| $F$ | forza d'impatto (t) |
| $P$ | peso del masso (kg) |
| $m = P/g$ | massa del masso impattante |
| $g$ | accelerazione di gravità |
| $V$ | velocità d'impatto del masso (m/s) |
| $T$ | durata d'impatto (ms) |
| $z$ | penetrazione del masso nella struttura (cm) |
| $\sigma$ | resistenza a compressione della struttura (kPa) |
| $E_m$ | modulo d'elasticità del masso (kPa) |
| $E_s$ | modulo d'elasticità della struttura (kPa) |
| $d$ | diametro massimo del masso (cm) |
| $N$ | fattore di forma: 1 per masso appuntito, 0,72 per masso piatto |

### Procedimento

La massa impattante deriva dal peso del masso:

$$ m = \frac{P}{g} $$

La **forza d'impatto** $F$ è funzione della quantità di moto del masso ($m\,V$) dissipata nella **durata d'impatto** $T$. A sua volta $T$ dipende dalla **penetrazione** $z$ del masso nella struttura, e $z$ si ricava da una variabile $Z$ funzione della resistenza $\sigma$ della struttura, dei moduli elastici $E_m$ ed $E_s$, del diametro $d$ e del fattore di forma $N$.

Sul rapporto penetrazione/diametro si applica la regola:

- se $z/d > 2$ si assume $z = z$;
- se $z/d \leq 2$ si corregge $z$ secondo la relazione di Paronuzzi.

Si ricava infine la **sollecitazione massima** trasmessa alla struttura. La formulazione completa segue Paronuzzi (1989) — vedi [Bibliografia](bibliografia.md).

!!! tip "Dimensionamento delle difese"
    Per il progetto vero e proprio delle opere di difesa dalla caduta massi (barriere paramassi rigide ed elastiche) puoi usare le applicazioni dedicate di [Geoapp](geoapp.md).

## Previsione del crollo per evento sismico

Gli eventi sismici, anche di magnitudo bassa, sono riconosciuti tra le cause scatenanti dei fenomeni di crollo. La suscettibilità alle azioni sismiche è stata studiata da **Harp & Noble (1993)**, che propongono di classificare l'ammasso roccioso con una metodologia derivata dalla **Q di Barton**.

A partire dai rilievi geostrutturali si calcola un valore di **Q modificato**:

$$ Q = \frac{RQD}{J_n} \cdot \frac{J_r}{J_a} \cdot \frac{1}{A_F} $$

dove l'RQD è ricavato dal numero di giunti per metro cubo $J_v$ (vedi [RQD](classificazioni.md#rqd-rock-quality-designation)), $J_n$, $J_r$, $J_a$ sono i parametri di giunto della classificazione di Barton ([$J_n$](classificazioni.md#jn) · [$J_r$](classificazioni.md#jr) · [$J_a$](classificazioni.md#ja)) e $A_F$ è il **fattore di apertura** delle discontinuità.

### Fattore di apertura A~F~

| Apertura delle discontinuità | $A_F$ |
|---|---|
| Tutti i giunti sono chiusi | 1,0 |
| Maggioranza chiusi, alcuni aperti fino a 2 cm | 2,5 |
| Maggioranza chiusi, alcuni aperti fino a 5 cm | 5,0 |
| Più del 20% dei giunti con aperture fino a 20 cm | 7,5 |
| Più del 60% dei giunti con aperture fino a 20 cm | 10,0 |
| Giunti aperti più di 20 cm | 15,0 |

Se l'ammasso presenta blocchi liberi, $A_F$ va aumentato di 1; lo stesso se un giunto persistente è disposto a franapoggio.

### Classificazione della suscettibilità

Dal valore di Q così calcolato gli autori propongono la classificazione di suscettibilità al crollo per un evento sismico di magnitudo > 5:

| Q | Suscettibilità al crollo |
|---|---|
| < 0,1 | Molto alta |
| 0,1 – 1 | Alta |
| 1 – 9,99 | Media |
| > 10 | Bassa |

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Rock%20Mechanics%20NX).*
