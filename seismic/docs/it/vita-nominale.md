# Vita nominale e classe d'uso

Prima di leggere i parametri sismici devi dire all'app **per quanto tempo** e
con quale **importanza** l'opera deve resistere. Sono i due dati che, insieme
alla posizione, determinano l'azione sismica di progetto.

## Vita nominale $V_N$

La **vita nominale** è il numero di anni per cui l'opera, purché soggetta a
manutenzione, deve mantenere i livelli prestazionali di progetto. Le NTC ne
indicano i valori minimi per tipo di costruzione:

| Tipo di costruzione | $V_N$ (anni) |
|---|---|
| Opere provvisorie, provvisionali, strutture in fase costruttiva | ≤ 10 |
| Costruzioni con livelli di prestazione ordinari | ≥ 50 |
| Grandi opere, ponti, opere infrastrutturali e dighe di grandi dimensioni | ≥ 100 |

## Classe d'uso e coefficiente $C_U$

La **classe d'uso** riflette le conseguenze di un'interruzione d'uso o di un
collasso. A ciascuna classe corrisponde un **coefficiente d'uso** $C_U$:

| Classe d'uso | Descrizione sintetica | $C_U$ |
|---|---|---|
| **I** | Costruzioni con presenza solo occasionale di persone, agricole | 0.7 |
| **II** | Costruzioni con normali affollamenti, senza funzioni pubbliche critiche | 1.0 |
| **III** | Affollamenti significativi; industrie con attività pericolose per l'ambiente | 1.5 |
| **IV** | Funzioni pubbliche o strategiche importanti, anche in emergenza | 2.0 |

## Periodo di riferimento $V_R$

L'azione sismica si valuta sul **periodo di riferimento**:

$$ V_R = V_N \cdot C_U $$

!!! example "Esempio"
    Edificio ordinario ($V_N = 50$) di classe d'uso II ($C_U = 1.0$):
    $V_R = 50 \times 1.0 = 50$ anni. Lo stesso edificio come scuola (classe III,
    $C_U = 1.5$) avrebbe $V_R = 75$ anni, e quindi periodi di ritorno — e azione
    sismica — più severi.

## Dai $V_R$ ai periodi di ritorno $T_R$

Ogni **stato limite** è associato a una **probabilità di superamento**
$P_{V_R}$ nel periodo di riferimento. Il periodo di ritorno dell'azione sismica
si ricava da:

$$ T_R = -\frac{V_R}{\ln\left(1 - P_{V_R}\right)} $$

| Stato limite | Categoria | $P_{V_R}$ | Esempio con $V_R = 50$ anni |
|---|---|---|---|
| **SLO** | Esercizio | 81 % | $T_R \approx 30$ anni |
| **SLD** | Esercizio | 63 % | $T_R \approx 50$ anni |
| **SLV** | Ultimo | 10 % | $T_R \approx 475$ anni |
| **SLC** | Ultimo | 5 % | $T_R \approx 975$ anni |

PS Advanced calcola i $T_R$ effettivi dal tuo $V_R$ e, per ciascuno, interpola
dal reticolo i parametri $a_g$, $F_0$, $T_C^*$ descritti in
[Parametri sismici e stati limite](parametri.md).

!!! note "Limiti del reticolo"
    Il reticolo di riferimento è definito per periodi di ritorno tra **30 e
    2475 anni**. Per $V_R$ molto grandi o molto piccoli i $T_R$ vengono
    ricondotti a questo intervallo secondo le regole di normativa.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20PS%20Advanced%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/seismic/docs/it/vita-nominale.md).*
