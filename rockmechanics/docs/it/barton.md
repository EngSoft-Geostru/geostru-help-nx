# Barton — indice Q

Sviluppata nel 1974 al **Norwegian Geotechnical Institute** essenzialmente per le opere in sotterraneo, la classificazione di Barton è stata poi estesa a campi diversi; nel 2002 lo stesso Barton ne ha proposto una revisione complessiva.

## Calcolo dell'indice Q

$$ Q = \frac{RQD}{J_n} \cdot \frac{J_r}{J_a} \cdot \frac{J_w}{SRF} $$

dove i sei indici sono:

- **RQD** — Rock Quality Designation, tiene conto della suddivisione della massa rocciosa;
- **$J_n$** — Joint Set Number, dipende dal numero di famiglie di giunti;
- **$J_r$** — Joint Roughness Number, dipende dalla rugosità della famiglia più sfavorevole;
- **$J_a$** — Joint Alteration Number, dipende dal grado di alterazione e dal riempimento, sulla famiglia più sfavorevole;
- **$J_w$** — Joint Water Number, dipende dalle condizioni idrogeologiche;
- **SRF** — Stress Reduction Factor, funzione dello stato tensionale o del disturbo tettonico.

I tre rapporti hanno un significato fisico: $RQD/J_n$ è legato alla **dimensione dei blocchi**, $J_r/J_a$ alla **resistenza al taglio** fra i blocchi, $J_w/SRF$ allo **stato tensionale attivo**.

Di recente Q è stato **normalizzato** rispetto alla resistenza a compressione monoassiale della roccia $\sigma_c$:

$$ Q_c = Q \cdot \frac{\sigma_c}{100} $$

## Parametri di input

I parametri $J_n$, $J_r$, $J_a$, $J_w$ sono definiti nelle tabelle comuni:

- [Parametro $J_n$](classificazioni.md#jn)
- [Parametro $J_r$](classificazioni.md#jr)
- [Parametro $J_a$](classificazioni.md#ja)
- [Parametro $J_w$](classificazioni.md#jw)

Per **RQD** prende il suo valore nominale; se $RQD < 10$ si assume comunque 10 (vedi [RQD](classificazioni.md#rqd-rock-quality-designation)).

## Fattore SRF (Stress Reduction Factor) { #srf }

### Zone di debolezza intersecanti lo scavo

| Definizione | SRF |
|---|---|
| Diverse zone di debolezza con argilla o roccia chimicamente disgregata, roccia circostante molto allentata | 10 |
| Singole zone di debolezza con argilla o roccia disgregata (copertura ≤ 50 m) | 5 |
| Singole zone di debolezza con argilla o roccia disgregata (copertura > 50 m) | 2,5 |
| Fasce di taglio multiple in roccia competente, rilassamento della roccia circostante | 7,5 |
| Fascia di taglio singola in roccia competente (copertura ≤ 50 m) | 5 |
| Fascia di taglio singola in roccia competente (copertura > 50 m) | 2,5 |
| Zone intensamente fratturate con intersezione di discontinuità aperte e continue | 5 |

Se le zone di debolezza influenzano ma non intersecano direttamente lo scavo, SRF va ridotto del 25–50%.

### Ammasso competente con problemi di tensioni geostatiche

| Definizione | $\sigma_c/\sigma_1$ | $\sigma_\theta/\sigma_c$ | SRF |
|---|---|---|---|
| Basso campo tensionale, prossimità della superficie | > 200 | < 0,01 | 2,5 |
| Condizioni tensionali favorevoli | 200 – 10 | 0,01 – 0,3 | 1 |
| Campo tensionale alto (favorevole in calotta, sfavorevole ai piedritti) | 10 – 5 | 0,3 – 0,5 | 0,5 – 2 |
| Moderati colpi di tensione dopo più di un'ora, roccia massiva | 5 – 3 | 0,5 – 0,65 | 5 – 50 |
| Colpi di tensione quasi immediati, roccia massiva | 3 – 2 | 0,65 – 1 | 50 – 400 |

dove $\sigma_c$ è la resistenza a compressione della roccia, $\sigma_\theta$ la massima tensione tangenziale al contorno dello scavo, $\sigma_1$ e $\sigma_3$ le tensioni principali maggiore e minore.

Se $\sigma_1/\sigma_3$ è compreso fra 5 e 10, ridurre $\sigma_c$ a $0{,}75\,\sigma_c$; se > 10, ridurre a $0{,}5\,\sigma_c$. Se la profondità della calotta dal piano campagna è inferiore alla larghezza dello scavo, Barton suggerisce SRF = 5. Le ultime tre righe valgono per rocce molto dure e massive, con $RQD/J_n$ fra 50 e 200.

### Ammasso spingente (squeezing)

| Definizione | SRF |
|---|---|
| Ammasso moderatamente spingente | 5 – 10 |
| Ammasso fortemente spingente | 10 – 20 |

### Ammasso rigonfiante (swelling)

| Definizione | SRF |
|---|---|
| Ammasso moderatamente rigonfiante | 5 – 10 |
| Ammasso fortemente rigonfiante | 10 – 15 |

!!! note "Caratterizzazione lontano dallo scavo"
    Per caratterizzare l'ammasso lontano dall'influenza dello scavo si possono assumere i valori di SRF (5 – 2,5 – 1,0 – 0,5) in funzione delle altezze di ricoprimento (0–5; 5–25; 25–250; > 250 m).

## Classi dell'ammasso

L'indice Q varia da 0,001 a 1000 ed è suddiviso in 9 classi:

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

## Parametri caratteristici dell'ammasso

Da Q si estrapolano due componenti di resistenza:

**Componente attritiva** (approssimazione dell'angolo d'attrito dell'ammasso):

$$ \varphi' = \arctan\!\left(\frac{J_r \cdot J_w}{J_a}\right) $$

**Componente coesiva** (approssimazione della coesione dell'ammasso):

$$ c' = \frac{RQD}{J_n} \cdot \frac{1}{SRF} \cdot \frac{\sigma_c}{100} $$

Il **modulo di deformazione statico** dell'ammasso si determina in accordo con l'espressione di **Serafim e Pereira (1983)** derivata da RMR, ricavando l'RMR equivalente con $RMR = 9\ln(Q) + 44$:

$$ E_m = 10^{\frac{RMR - 10}{40}} \quad [\text{GPa}] $$

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Rock%20Mechanics%20NX).*
