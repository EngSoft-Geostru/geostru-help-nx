# Cenni teorici

Questa pagina riassume la teoria su cui si basa SNL NX: le linee guida americane **FHWA-NHI-14-007** per le pareti chiodate e, per la verifica interna, il metodo del cuneo di **Sheahan & Ho (2003)**. Le ipotesi e i limiti del metodo sono elencati in [Validazione e limiti](validazione.md).

## Il soil nailing

Il soil nailing sostiene pendii e fronti di scavo inserendo nel terreno elementi di rinforzo, i **chiodi**, di solito barre d'acciaio in fori riempiti di malta. I chiodi sono **passivi**: non sono tesati e lavorano a trazione quando il terreno si deforma, trasferendo gli sforzi al terreno per attrito e aderenza lungo l'interfaccia.

In uno scavo la parete si costruisce **dall'alto verso il basso**:

1. si scava un gradino alto quanto l'interasse verticale dei chiodi;
2. si perfora il terreno, con una leggera inclinazione verso il basso;
3. si inserisce la barra e si riempie il foro di malta;
4. si posano i drenaggi e il primo strato di rivestimento (spritz-beton con rete) collegato alla testa dei chiodi;
5. si ripete fino alla quota finale, poi si completa il rivestimento.

Gli elementi da progettare sono quindi tre: il **terreno**, i **chiodi** e il **rivestimento**.

## Meccanismi di rottura

| Meccanismo | Che cosa succede | In SNL NX |
|---|---|---|
| Stabilità interna | un cuneo di terreno scivola su una superficie che taglia i chiodi | verifica a cuneo piano, per ogni fase di scavo |
| Stabilità globale | la superficie passa dietro o sotto i chiodi | **non calcolata**: serve un programma di stabilità dei pendii, come GeoStru Slope |
| Sfilamento | il chiodo si sfila dal terreno oltre la superficie di rottura | verifica per ogni chiodo e ogni fase |
| Rottura per trazione | la barra si rompe | verifica per ogni chiodo e ogni fase |
| Rivestimento | lo spritz-beton si rompe fra i chiodi | diagrammi di pressione, taglio e momento; la verifica della sezione è a parte |
| Scorrimento | il blocco chiodato scivola sulla base | equilibrio orizzontale del blocco di larghezza Bl |

## Fasi di scavo

Le fasi non si inseriscono: SNL NX ne crea una per chiodo, in ordine di profondità. Nella fase *i* sono già posati i chiodi fino all'*i*-esimo e lo scavo è arrivato a metà fra il chiodo *i* e il successivo; l'ultima fase arriva al piede della parete, alla profondità H.

Per ogni fase la superficie di rottura parte dal fondo dello scavo raggiunto, e la verifica interna, lo sfilamento e la rottura dei chiodi si ripetono con i soli chiodi già posati.

## Spinta attiva

La tensione orizzontale efficace attiva alla profondità *z* dipende dal coefficiente di spinta attiva Ka, dalla tensione verticale efficace σ'v, dalla coesione c' e dai carichi a monte:

$$
\sigma'_a(z) = K_a\,\sigma'_v(z) - 2\,c'\sqrt{K_a} \;\ge 0
$$

Ka si calcola strato per strato con la teoria di **Rankine** o di **Coulomb**; quest'ultima tiene conto dell'attrito δ fra parete e terreno, dell'inclinazione θ del paramento e dell'inclinazione ε del terreno a monte. Per ε = 0 e paramento verticale, Rankine dà il valore classico:

$$
K_a = \tan^2\!\left(45^\circ - \frac{\varphi'}{2}\right)
$$

I carichi a monte aggiungono una tensione orizzontale: il carico uniforme in proporzione a Ka, la striscia e il carico lineare con le soluzioni del semispazio elastico per una parete rigida.

## Forza nei chiodi

Ogni chiodo raccoglie la spinta della sua **zona d'influenza**: la fascia di parete che va da metà fra il chiodo e quello sopra (o dalla testa) a metà fra il chiodo e quello sotto (o al piede). L'altezza della fascia è l'interasse verticale Sv del chiodo, la sua larghezza l'interasse orizzontale Sh. La forza nel chiodo è la risultante della pressione totale sulla zona, riportata nella direzione del chiodo:

$$
F_i = \frac{k_n\,S_h}{\cos\alpha_i}\int_{z_a}^{z_b} \sigma_h(z)\,dz
$$

dove σh è la somma della tensione efficace attiva, della pressione dell'acqua e, in sisma, dell'incremento sismico; kn (tipicamente 0,85) tiene conto che il chiodo non raccoglie tutta la spinta. Con il terreno stratificato la pressione cambia salto e pendenza alle interfacce: per questo si integra sulla zona invece di usare il valore al centro.

## Verifica di stabilità interna

Per ogni fase si considera il cuneo di terreno delimitato dal paramento, dal terreno a monte e da una superficie piana che parte dal fondo dello scavo con inclinazione β sull'orizzontale. β è assegnata oppure vale 45° + φ̄'/2. L'equilibrio delle forze sul cuneo (Sheahan & Ho, 2003) dà il fattore di sicurezza:

$$
FS = \frac{\bar c'\,L_s + \left[(W(1+k_v)+Q)\cos\beta - k_h W\sin\beta - U\right]\tan\bar\varphi' + S}{\left[(W(1+k_v)+Q)\sin\beta + k_h W\cos\beta\right]\gamma_R}
$$

con

$$
S = \frac{1}{S_h}\sum_i R_i\left[\cos(\beta+\alpha_i) + \sin(\beta+\alpha_i)\tan\bar\varphi'\right], \qquad R_i = \min(R_{T,i},\,R_{PO,i})
$$

- W peso del cuneo, Q risultante dei carichi sul cuneo, U spinta dell'acqua sulla superficie;
- Ls lunghezza della superficie di rottura;
- c̄' e φ̄' medie pesate sugli spessori degli strati scavati nella fase;
- Ri resistenza del chiodo *i* che la superficie attraversa: il minimo fra rottura e sfilamento (FHWA);
- γR il coefficiente R delle verifiche interne.

La verifica è soddisfatta se FS ≥ 1.

## Sfilamento

Il chiodo si sfila quando la forza supera la resistenza della parte oltre la superficie di rottura, lunga **Le** (lunghezza efficace):

$$
R_{PO} = \frac{\pi\,D\,L_e\,\tau_{lim}}{\xi}, \qquad FS_{PO} = \frac{R_{PO}}{F\,\gamma_{R,PO}}
$$

D è il diametro del foro, ξ il fattore di correlazione, τlim la resistenza tangenziale limite all'interfaccia. τlim cresce con la tensione verticale al centro del tratto efficace, con il coefficiente di interazione K e con l'attrito dello strato in cui si trova il bulbo, e comprende un'aderenza legata alla coesione. La lunghezza efficace cambia da una fase all'altra, perché la superficie di rottura scende con lo scavo.

## Rottura per trazione

$$
R_T = \frac{\pi\,d_c^2}{4}\,f_y, \qquad FS_T = \frac{R_T}{F\,\gamma_{R,T}}
$$

dc è il diametro della barra, fy la resistenza dell'acciaio.

## Scorrimento

Lo scorrimento è un caso particolare della stabilità globale: il blocco chiodato, largo **Bl**, scivola sul terreno di fondazione. Si impone l'equilibrio orizzontale, non quello alla rotazione:

$$
FS = \frac{R_s}{\gamma_R\left[P_{a,h} + Q_h + \Delta P_{aE} + \Delta Q_{hE} + U_1\right]}
$$

$$
R_s = c'_f\,B_l + \left(W + P_{a,v} + Q - U_2\right)\tan\varphi'_f
$$

- Pa spinta del terreno sul lato interno del blocco, alto H1, con componenti orizzontale e verticale;
- Qh spinta orizzontale dei carichi a monte;
- ΔPaE e ΔQhE incrementi sismici;
- U1 spinta dell'acqua sul lato interno, U2 sottospinta alla base;
- c'f e φ'f parametri del terreno di fondazione.

Bl si sceglie nel passo Calcolo: uguale a H, assegnata, oppure automatica dalla proiezione del primo chiodo. La verifica è soddisfatta se FS > 1.

## Rivestimento

Il rivestimento si schematizza come una trave lungo il paramento caricata dalla pressione totale del terreno e appoggiata sui chiodi, le cui reazioni sono le forze nei chiodi. SNL NX ne traccia pressione, taglio e momento per metro di parete. I diagrammi sono indicativi: la verifica della sezione in calcestruzzo armato e della testa del chiodo si fa a parte.

## Sisma

L'azione sismica è **pseudostatica**, con i coefficienti kh e kv del progetto. In sisma la spinta si calcola con il coefficiente **KaE di Mononobe-Okabe**, e l'incremento rispetto alla spinta statica entra nella forza dei chiodi e nello scorrimento con il proprio coefficiente A. Nella verifica interna il peso del cuneo si moltiplica per (1 + kv) e si aggiunge la forza orizzontale kh·W.

Dai parametri del sito l'app propone

$$
k_h = \beta_m\,\frac{a_{max}}{g}, \qquad k_v = \pm 0{,}5\,k_h
$$

con amax = SS·ST·ag allo SLV e βm = 0,38 se non lo cambi. La proposta è un aiuto: la scelta di kh e kv resta del progettista.

## Coefficienti parziali

Le norme associano a ogni verifica un approccio diverso. Per le NTC 2018 il riferimento è:

| Verifica | NTC 2018 | Riferimento |
|---|---|---|
| Scorrimento | A1 + M1 + R3 | §6.5.3.1.1 |
| Sfilamento (il chiodo come un ancoraggio) | A1 + M1 + R3 | §6.6.2 |
| Stabilità interna (come un fronte di scavo) | A2 + M2 + R2 | §6.8.2 |
| Rottura dei chiodi | A1 + M1 + R1 oppure A2 + M2 + R1 | §6.5.3.1.2 |

In condizioni sismiche i riferimenti sono al §7.11. Per l'Eurocodice 7 valgono gli approcci di progetto DA1 (combinazioni 1 e 2), DA2 e DA3 dell'EN 1997-1.

SNL NX usa **una sola combinazione** per progetto: gli stessi coefficienti A e M per tutte le verifiche e un coefficiente R per ciascuna (rottura, sfilamento, scorrimento, verifiche interne). Scegliendo la normativa vengono caricati:

| Normativa | A, M | R rottura | R interne | R scorrimento | R sfilamento | ξ |
|---|---|---|---|---|---|---|
| NTC 2018, opera permanente | 1 | 1 | 1,1 | 1,1 | 1,2 | 1 |
| NTC 2018, opera provvisoria | 1 | 1 | 1,1 | 1,1 | 1,1 | 1 |
| Eurocodice 7 | 1 | 1 | 1 | 1 | 1 | 1 |
| Utente | liberi | | | | | |

I coefficienti si possono cambiare a mano nel passo Calcolo, e il coefficiente A di ogni carico si scrive nel passo Carichi. Per rispettare alla lettera approcci diversi per verifiche diverse si calcola il progetto più volte, una per combinazione.

## Bibliografia

- Lazarte C.A., Robinson H., Gómez J.E., Baxter A., Cadden A., Berg R. (2015). *Geotechnical Engineering Circular No. 7 — Soil Nail Walls Reference Manual*, FHWA-NHI-14-007. Federal Highway Administration.
- Sheahan T.C., Ho C.L. (2003). *Simplified trial wedge method for soil nailed wall analysis*. Journal of Geotechnical and Geoenvironmental Engineering, 129(2), 117-124.
- Rankine W.J.M. (1857). *On the stability of loose earth*. Philosophical Transactions of the Royal Society of London, 147.
- Coulomb C.A. (1776). *Essai sur une application des règles de maximis et minimis à quelques problèmes de statique relatifs à l'architecture*.
- Okabe S. (1926). *General theory of earth pressure*. Journal of the Japanese Society of Civil Engineers, 12(1).
- Mononobe N., Matsuo H. (1929). *On the determination of earth pressures during earthquakes*. Proc. World Engineering Congress, Tokyo.
- Terzaghi K. (1943). *Theoretical Soil Mechanics*. Wiley.
- Poulos H.G., Davis E.H. (1974). *Elastic Solutions for Soil and Rock Mechanics*. Wiley.
- D.M. 17/01/2018, *Aggiornamento delle Norme tecniche per le costruzioni*; Circolare n. 7 del 21/01/2019.
- EN 1997-1:2004, *Eurocodice 7 — Progettazione geotecnica — Parte 1: Regole generali*.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/snl/docs/it/teoria.md).*
