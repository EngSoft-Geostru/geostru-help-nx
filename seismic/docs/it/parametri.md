# Parametri sismici e stati limite

Sono il cuore del calcolo: per ogni stato limite, i tre parametri che
descrivono la pericolosità sismica di base del sito.

## I tre parametri di base

| Parametro | Unità | Significato |
|---|---|---|
| $a_g$ | g | accelerazione orizzontale massima attesa su **sito di riferimento rigido** (categoria A) e superficie orizzontale (T1) |
| $F_0$ | – | valore massimo del **fattore di amplificazione** dello spettro in accelerazione orizzontale ($F_0 \ge 2.2$) |
| $T_C^*$ | s | periodo di inizio del tratto a **velocità costante** dello spettro in accelerazione orizzontale |

Da questi tre valori — insieme a categoria di sottosuolo e topografia —
derivano l'intero [spettro di risposta](spettri.md) e i
[coefficienti sismici](coefficienti.md).

## I quattro stati limite

Le NTC definiscono quattro stati limite, due di esercizio e due ultimi:

- **SLO** — Stato Limite di Operatività (esercizio)
- **SLD** — Stato Limite di Danno (esercizio)
- **SLV** — Stato Limite di salvaguardia della Vita (ultimo)
- **SLC** — Stato Limite di Collasso (ultimo)

A ciascuno corrisponde un [periodo di ritorno $T_R$](vita-nominale.md#dai-v_r-ai-periodi-di-ritorno-t_r)
crescente e quindi un'azione sismica via via più severa. PS Advanced mostra i
tre parametri per **tutti e quattro** gli stati limite in un'unica scheda.

## Interpolazione { #interpolazione }

Il reticolo di riferimento fornisce $a_g$, $F_0$, $T_C^*$ solo su una **griglia
di nodi** e solo per **nove periodi di ritorno** tabellati (30, 50, 72, 101,
140, 201, 475, 975, 2475 anni). Il sito reale quasi mai coincide con un nodo o
con un $T_R$ tabellato, quindi serve una doppia interpolazione.

### Nello spazio (i 4 nodi)

L'app individua i **quattro nodi** del reticolo che racchiudono il punto e ne
combina i valori pesandoli con le distanze dal sito. La formula di normativa
usa la media pesata sull'inverso delle distanze:

$$ p = \frac{\sum_{i=1}^{4} \dfrac{p_i}{d_i}}{\sum_{i=1}^{4} \dfrac{1}{d_i}} $$

dove $p_i$ è il parametro al nodo $i$ e $d_i$ la distanza del sito dal nodo.

### Nel tempo (i periodi di ritorno)

Per il $T_R$ del tuo stato limite l'app interpola tra i due periodi tabellati
che lo racchiudono, in scala **logaritmica**:

$$ \log p = \log p_1 + \left(\log p_2 - \log p_1\right)\,
\frac{\log T_R - \log T_{R1}}{\log T_{R2} - \log T_{R1}} $$

!!! note "Perché i valori possono differire da altre fonti"
    Piccole differenze rispetto ad altri strumenti dipendono quasi sempre da:
    coordinate leggermente diverse, datum non convertito, oppure arrotondamenti
    intermedi. PS Advanced interpola direttamente i nodi ufficiali del reticolo
    con le formule dell'Allegato alle NTC.

## Lettura della scheda

Per ogni stato limite la scheda riporta $T_R$, $a_g$ (in g), $F_0$ e $T_C^*$
(in s). Sono questi i valori che finiscono nel [report](formati.md) e che
alimentano [spettri](spettri.md) e [coefficienti](coefficienti.md).

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20PS%20Advanced%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/seismic/docs/it/parametri.md).*
