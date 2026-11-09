# Sezioni in c.a., pali e tiranti

## Sezioni in cemento armato

Le sezioni sono rettangolari, larghe un metro, con due strati di armatura a distanza pari al copriferro dai bordi. Le verifica il
solutore delle sezioni in c.a. di GeoStru, lo stesso di MP NX.

### Presso-flessione allo SLU

Calcestruzzo con legame parabola-rettangolo ($\varepsilon_{c2}=0{,}2\,\%$, $\varepsilon_{cu}=0{,}35\,\%$,
$f_{cd}=\alpha_{cc}f_{ck}/\gamma_c$), acciaio bilineare. Il dominio M-N si costruisce per strisce sottili della sezione; la verifica
confronta il punto (N~Ed~, M~Ed~) con il dominio e restituisce il rapporto domanda/capacità.

Con le NTC 2018 il momento resistente è quello di **prima plasticizzazione**: il minore fra quello che porta l'acciaio allo snervamento e
quello che porta il calcestruzzo a una deformazione di compressione dello 0,2 %. È più basso del momento a rottura (circa il 10 % con sforzo
normale piccolo) e corrisponde alla verifica in campo sostanzialmente elastico che la norma chiede alle fondazioni in combinazione sismica;
il programma desktop lo applica a tutte le sezioni e a tutte le combinazioni, e MDC NX fa lo stesso.

### Taglio

Elementi senza armatura trasversale, NTC 2018 eq. (4.1.23):

$$V_{Rd}=\max\left\{\left[\frac{0{,}18\,k\,(100\rho_l f_{ck})^{1/3}}{\gamma_c}+0{,}15\,\sigma_{cp}\right]b_w d\;;\;\left(v_{min}+0{,}15\,\sigma_{cp}\right)b_w d\right\}$$

con $k=1+\sqrt{200/d}\le 2$ (d in mm), $\rho_l=A_{sl}/(b_w d)\le 0{,}02$, $\sigma_{cp}=N_{Ed}/A_c\le 0{,}2f_{cd}$,
$v_{min}=0{,}035\,k^{3/2}f_{ck}^{1/2}$.

### Esercizio

Tensioni con sezione fessurata (n = 15) e apertura delle fessure (Circolare 2019, C4.1.2.2.4):

$$w_k=s_{r,max}\,(\varepsilon_{sm}-\varepsilon_{cm})\qquad
\varepsilon_{sm}-\varepsilon_{cm}=\frac{\sigma_s-k_t\dfrac{f_{ctm}}{\rho_{eff}}(1+\alpha_e\rho_{eff})}{E_s}\ge 0{,}6\frac{\sigma_s}{E_s}$$

$$s_{r,max}=k_3c+k_1k_2k_4\frac{\phi}{\rho_{eff}}$$

con k~t~ = 0,6 per i carichi di breve durata e 0,4 per quelli di lunga durata, k~2~ = 0,5 per flessione, ρ~eff~ riferito all'area
efficace di calcestruzzo teso.

## Pali

### Azioni in testa

La forza orizzontale H, la forza verticale V e il momento M della fase II, per la quota di carico affidata ai pali, si riportano al
**baricentro delle teste dei pali**. Con il momento risultante si usa l'equilibrio di tutte le azioni; con il momento ribaltante (scelta
prudente) solo i contributi ribaltanti.

### Ripartizione: plinto rigido

Il plinto è un corpo rigido con tre spostamenti (u, w, θ). Ogni palo vi reagisce con una **rigidezza assiale** k~a~ e una **trasversale**
k~t~; l'equilibrio $\mathbf{K}\,\mathbf{d}=(H,V,M)$ dà gli spostamenti e quindi N, T (e M con la testa incastrata) di ogni fila. Con pali
verticali e rigidezza trasversale trascurabile si ritrova la ripartizione classica:

$$N_i=\frac{V}{n}+\frac{M\,s_i}{\sum s_j^2}\qquad T_i=\frac{H}{n}$$

- **Rigidezza assiale** (Randolph e Wroth): cedimento elastico del palo nel terreno con il modulo medio degli strati lungo il fusto, più
  l'accorciamento del palo.
- **Rigidezza trasversale** (Hetényi, palo lungo): con la lunghezza caratteristica $L_b=\sqrt[4]{4E_pI_p/(k\,D)}$, testa libera
  $k_t=2E_pI_p/L_b^3$.
- **Testa incastrata**: la matrice di Hetényi aggiunge il momento d'incastro, che entra nella verifica del palo.

### Carico limite verticale

$$Q_{lim}=Q_p+Q_s\qquad Q_p=\frac{\pi D^2}{4}\left(\sigma'_{v,p}N_q+c\,N_c\right)\qquad Q_s=\pi D\sum_i\left(K\tan\delta\;\sigma'_{v,i}+\alpha\,c_i\right)\Delta l_i$$

N~q~ di Berezantzev in funzione di φ′ alla punta e del rapporto L/D, $N_c=\max\{(N_q-1)\cot\varphi';9\}$. I coefficienti K·tanδ e
l'adesione α dipendono dal tipo di palo (trivellato o battuto) e dalla coesione. Per i pali inclinati si usano la profondità vera della punta e
la lunghezza del fusto in ogni strato. La resistenza di progetto è

$$R_d=\frac{Q_p}{\xi\,\gamma_b}+\frac{Q_s}{\xi\,\gamma_s}$$

con ξ = max(ξ~3~, ξ~4~) dal numero di verticali indagate (NTC 2018 Tab. 6.4.IV) e γ~b~, γ~s~ della Tab. 6.4.II. Un palo teso conta solo la
resistenza laterale, ridotta al 70 %. L'efficienza del gruppo (Converse-Labarre), se scelta, moltiplica la resistenza:

$$E_g=1-\frac{\theta_L+\theta_F\,(m-1)/m}{90°}\qquad \theta=\arctan\frac{D}{i}$$

con i gli interassi nella fila e fra le file, m il numero di file, E~g~ fra 0,3 e 1.

### Carichi trasversali

Palo lungo su suolo elastico. Con modulo di reazione costante (Hetényi) spostamento in testa, rotazione e momenti lungo il fusto vengono
dalle soluzioni in forma chiusa con L~b~; con modulo crescente con la profondità (Matlock e Reese) dalla lunghezza relativa
$T=\sqrt[5]{E_pI_p/n_h}$ e dai coefficienti adimensionali A~y~, B~y~, A~m~, B~m~. La pressione sul terreno si confronta con la pressione
limite laterale.

### Sisma

Le azioni inerziali del muro arrivano ai pali già in H, V e M della combinazione sismica, senza ridurne la resistenza. Con sottosuolo D o E
le NTC 2018 chiedono di considerare anche i momenti da interazione cinematica: l'app lo ricorda.

## Tiranti

Il tirante agisce sul paramento con la forza di progetto per metro di muro $T/i$ (i interasse), inclinata dell'angolo α del tirante.
La resistenza dell'ancoraggio è la minore di tre:

| Resistenza | Da che cosa dipende |
|---|---|
| Bulbo nel terreno | diametro e lunghezza del bulbo, tensione efficace alla profondità del suo baricentro, φ′ e c′ dello strato, divisa per γ~R~·ξ~a~ (NTC 2018 Tab. 6.6.I e 6.6.III) |
| Aderenza malta-trefoli | $\pi\,n\,d_{tr}\,L_a\,\tau_{ad}$ |
| Acciaio | area dei trefoli per la resistenza di progetto, al netto delle cadute di tensione |

## Bibliografia

- Hetényi M. (1946), *Beams on Elastic Foundation*, University of Michigan Press.
- Matlock H., Reese L.C. (1960), *Generalized solutions for laterally loaded piles*, J. Soil Mech. Found. Div., ASCE, 86(SM5).
- Randolph M.F., Wroth C.P. (1978), *Analysis of deformation of vertically loaded piles*, J. Geotech. Eng. Div., ASCE, 104(GT12).
- Poulos H.G., Davis E.H. (1980), *Pile Foundation Analysis and Design*, Wiley.
- Berezantzev V.G., Khristoforov V.S., Golubkov V.N. (1961), *Load bearing capacity and deformation of piled foundations*, Proc. 5th ICSMFE, Parigi.
- Converse F.J., Labarre W.M., formula dell'efficienza dei gruppi di pali, in Bowles J.E., *Foundation Analysis and Design*.
- D.M. 17/01/2018 §4.1, §6.4.3, §6.6; Circolare 21/01/2019 n. 7, C4.1.2.2.4.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20MDC%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mdc/docs/it/teoria-strutture.md).*
