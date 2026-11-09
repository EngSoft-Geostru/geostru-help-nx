# Verifiche globali

Le verifiche globali riguardano il muro come corpo rigido e si fanno con le azioni della fase II (spinta sul piano virtuale, pesi del muro
e del terreno sopra la suola, carichi, spinta passiva), per ogni combinazione, con i parametri del terreno ridotti dai coefficienti M e le
resistenze divise per i coefficienti R. Per i muri su pali le sostituiscono le verifiche delle file di pali.

## Scorrimento

Il piano di scorrimento è la base della fondazione, oppure, con il dente, la linea che va dallo spigolo di valle al fondo del dente.
Proiettate le forze su quel piano (inclinato di α~b~):

$$T=F_x\cos\alpha_b+F_y\sin\alpha_b \qquad N=-F_x\sin\alpha_b+F_y\cos\alpha_b$$

$$F_{s,T}=\frac{\dfrac{N\tan\delta_b+c_a\,B}{\gamma_{R,sc}}+\dfrac{S_p}{\gamma_{R,v}}}{T}$$

con δ~b~ l'angolo d'attrito fondazione-terreno e c~a~ l'adesione (quelli dello strato di posa, o i valori scritti nel passo
[Normativa e sisma](sisma.md), ridotti con γ~φ~ e γ~c~), B la larghezza della base, S~p~ la spinta passiva a valle mobilitata (con la
percentuale di partecipazione scelta), γ~R,sc~ e γ~R,v~ i coefficienti di scorrimento e di resistenza del terreno a valle (NTC 2018 Tab.
6.5.I: 1,1 e 1,4 nella combinazione A1+M1+R3, 1,0 e 1,2 in quella sismica). È la forma che il motore usa e che la relazione stampa; il
programma desktop non divideva la spinta passiva per γ~R,v~.

## Ribaltamento

Attorno allo spigolo di valle della base:

$$F_{s,R}=\frac{M_{stab}}{\gamma_{R,rib}\;M_{rib}}$$

M~stab~ raccoglie i momenti dei pesi (muro, terreno sopra la suola, sovraccarichi stabilizzanti), della componente verticale della spinta e
della spinta passiva; M~rib~ quelli della componente orizzontale della spinta, dell'acqua, del sisma e dei carichi ribaltanti. Con le NTC
2018 la verifica sismica a ribaltamento usa β~m~ aumentato del 50 % (vedi [Sisma](sisma.md)).

## Eccentricità e pressioni sul terreno

Con N la risultante verticale e M il momento rispetto al centro della base, l'eccentricità è e = M/N. Con B la larghezza della base:

| Caso | Pressioni |
|---|---|
| $\lvert e\rvert\le B/6$ (risultante nel nocciolo) | trapezio: $\sigma_{max,min}=\dfrac{N}{B}\left(1\pm\dfrac{6e}{B}\right)$ |
| $\lvert e\rvert>B/6$ | triangolo parzializzato: $\sigma_{max}=\dfrac{2N}{3u}$, con u la distanza della risultante dal bordo compresso, su una lunghezza 3u |

Una risultante fuori dalla base (u ≤ 0) rende il muro non verificato. Con il magrone le pressioni si riportano anche alla base del magrone.

## Carico limite

### Vesic

Sulla larghezza efficace $B'=B-2e$ (Meyerhof), con D l'approfondimento del piano di posa, γ~1~ il peso del terreno sopra il piano di posa e
γ quello sotto:

$$q_{lim}=c'N_c\,s_c d_c i_c g_c+\gamma_1 D\,N_q\,s_q d_q i_q g_q+\tfrac12\gamma B' N_\gamma\,s_\gamma d_\gamma i_\gamma g_\gamma \qquad Q_{lim}=q_{lim}\,B'$$

$$N_q=e^{\pi\tan\varphi'}\tan^2\!\left(45°+\frac{\varphi'}{2}\right)\qquad N_c=(N_q-1)\cot\varphi'\qquad N_\gamma=2(N_q+1)\tan\varphi'$$

| Fattori | Espressione |
|---|---|
| Forma (muro di lunghezza L) | $s_q=1+\frac{B'}{L}\tan\varphi'$, $s_\gamma=1-0{,}4\frac{B'}{L}$, $s_c=1+\frac{B'}{L}\frac{N_q}{N_c}$; muro lungo: 1 |
| Profondità | $K=D/B'$ (o $\arctan(D/B')$ se D > B′); $d_c=1+0{,}4K$, $d_q=1+2\tan\varphi'(1-\sin\varphi')^2K$, $d_\gamma=1$ |
| Inclinazione del carico | $i_q=\left(1-\dfrac{H}{N+B'c'\cot\varphi'}\right)^m$, $i_\gamma=\left(1-\dfrac{H}{N+B'c'\cot\varphi'}\right)^{m+1}$, $i_c=i_q-\dfrac{1-i_q}{N_c\tan\varphi'}$, m = 2 per il muro |
| Pendio a valle (β) | $g_c=1-\beta/147°$, $g_q=g_\gamma=(1-\tan\beta)^2$ |

Con φ′ = 0 (condizioni non drenate, c′ = c~u~): N~c~ = 2 + π, N~q~ = 1, N~γ~ = 0. I fattori di forma, di profondità e d'inclinazione si possono
escludere nel passo [Normativa e sisma](sisma.md). Con la falda al piano di posa il terzo termine usa il peso alleggerito.

### Brinch Hansen

Stessa struttura, con $N_\gamma=1{,}5(N_q-1)\tan\varphi'$, $s_q=1+\frac{B'}{L}\sin\varphi'$, fattori d'inclinazione
$i_q=\left(1-\dfrac{0{,}5H}{N+B'c'\cot\varphi'}\right)^5$, $i_\gamma=\left(1-\dfrac{0{,}7H}{N+B'c'\cot\varphi'}\right)^5$ e di pendio
$g_q=g_\gamma=(1-0{,}5\tan\beta)^5$.

### Fattore di sicurezza

$$F_{s,Q}=\frac{Q_{lim}}{\gamma_{R,q}\,N}$$

con γ~R,q~ = 1,4 nella combinazione A1+M1+R3 e 1,2 in quella sismica delle NTC 2018.

## Bibliografia

- Vesic A.S. (1975), *Bearing capacity of shallow foundations*, in Winterkorn & Fang, *Foundation Engineering Handbook*, Van Nostrand Reinhold.
- Brinch Hansen J. (1970), *A revised and extended formula for bearing capacity*, Danish Geotechnical Institute, Bulletin 28.
- Meyerhof G.G. (1953), *The bearing capacity of foundations under eccentric and inclined loads*, Proc. 3rd ICSMFE, Zurigo.
- Bowles J.E. (1996), *Foundation Analysis and Design*, 5ª ed., McGraw-Hill.
- D.M. 17/01/2018, §6.4.2, §6.5.3.1.1, Tab. 6.2.I, 6.2.II, 6.5.I; §7.11.6.2.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20MDC%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mdc/docs/it/teoria-verifiche.md).*
