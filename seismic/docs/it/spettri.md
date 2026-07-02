# Spettri di risposta

Dai parametri di base e dalle categorie, PS Advanced costruisce gli **spettri
di risposta** in accelerazione: la forma con cui l'azione sismica entra nelle
verifiche strutturali.

## Spettro elastico

Lo **spettro di risposta elastico** in accelerazione descrive l'accelerazione
massima di un oscillatore semplice al variare del suo periodo $T$. È definito
a tratti su quattro rami, con i periodi caratteristici:

$$ T_C = C_C \cdot T_C^* \qquad T_B = \frac{T_C}{3} \qquad T_D = 4\,\frac{a_g}{g} + 1.6 $$

| Ramo | Intervallo | Andamento |
|---|---|---|
| Crescente | $0 \le T < T_B$ | da $S \cdot a_g$ verso il plateau |
| Plateau | $T_B \le T < T_C$ | ordinata massima $S \cdot a_g \cdot \eta \cdot F_0$ |
| Velocità costante | $T_C \le T < T_D$ | decrescente $\propto T_C/T$ |
| Spostamento costante | $T \ge T_D$ | decrescente $\propto T_C T_D / T^2$ |

L'app disegna sia lo **spettro orizzontale** sia lo **spettro verticale**
(quest'ultimo con i propri parametri e $F_V$).

### Smorzamento e fattore $\eta$

Lo smorzamento viscoso $\xi$ (in %) modifica l'ordinata di picco tramite il
fattore $\eta$:

$$ \eta = \sqrt{\frac{10}{5 + \xi}} \ge 0.55 $$

Con lo smorzamento convenzionale $\xi = 5\%$ risulta $\eta = 1$. Puoi impostare
un valore diverso quando la verifica lo richiede.

## Spettro di progetto

Per gli **stati limite ultimi** l'azione elastica viene ridotta, per tener
conto della capacità dissipativa della struttura, tramite il **fattore di
comportamento** $q$. In pratica, nello spettro il fattore $\eta$ è sostituito
da $1/q$:

$$ S_d(T) = S_e(T) \cdot \frac{1}{q} \quad (\text{nel plateau e nei rami decrescenti}) $$

In PS Advanced imposti separatamente:

- **$q_h$** — fattore di comportamento **orizzontale** (default 1.5)
- **$q_v$** — fattore di comportamento **verticale** (default 1.5)

e scegli lo **stato limite di progetto** (tipicamente SLV). L'app traccia lo
spettro di progetto sovrapposto all'elastico.

!!! tip "Quale q usare"
    $q$ dipende dalla tipologia strutturale e dalla duttilità di progetto (vedi
    Cap. 7 NTC). Per le **verifiche geotecniche** allo SLV si adotta spesso
    $q = 1.5$; per le strutture il valore può essere sensibilmente maggiore. Il
    default 1.5 è cautelativo: adattalo al tuo caso.

## Esportazione degli spettri

I punti dello spettro (periodo, ordinata) confluiscono nel
[report PDF](formati.md) per lo stato limite selezionato, insieme ai parametri
e ai coefficienti. Rigenera gli spettri dopo ogni modifica di sito o parametri
prima di esportare.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20PS%20Advanced%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/seismic/docs/it/spettri.md).*
