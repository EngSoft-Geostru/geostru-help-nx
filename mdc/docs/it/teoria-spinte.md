# Spinte e sisma

Le formule di questa pagina descrivono il modello di MDC NX; dove l'app si discosta dal programma desktop lo dice
[Validazione e limiti](validazione.md).

## Le fasi del calcolo

Per ogni combinazione il calcolo procede per fasi, come nel programma desktop:

1. **Fase I — paramento.** Le pressioni del terreno e dei sovraccarichi si calcolano sul paramento interno, diviso in strisce ai cambi di
   strato, di falda e di geometria. Con Coulomb la spinta è inclinata dell'angolo d'attrito terra-muro δ; con Rankine δ = 0. Da queste
   pressioni vengono le sollecitazioni del paramento.
2. **Fase II — piano virtuale.** Per le verifiche globali la superficie di spinta è la **verticale per l'estremo della suola di monte**: il
   terreno sopra la suola fa parte del sistema muro e pesa come forza stabilizzante. Sul piano virtuale la spinta è inclinata dell'angolo di
   resistenza del terreno. Con pesi, spinte, carichi e spinta passiva si calcolano il momento stabilizzante e quello ribaltante attorno allo
   spigolo di valle della base, poi scorrimento, ribaltamento e carico limite.
3. **Fase III — fondazione.** Le suole di valle e di monte e il dente, caricati dalle pressioni sul terreno e dai pesi sovrastanti, danno
   le sollecitazioni della fondazione.
4. **Fase IV — pali.** Solo per i muri su pali: le azioni della fase II vanno alla palificata (vedi
   [Sezioni in c.a., pali e tiranti](teoria-strutture.md)).

## Spinta attiva: Coulomb (Müller-Breslau)

Con α l'angolo del paramento sull'orizzontale (90° per un paramento verticale), φ′ l'angolo di resistenza al taglio, δ l'angolo d'attrito
terra-muro ed ε la pendenza del terrapieno:

$$K_a=\frac{\sin^2(\alpha+\varphi')}{\sin^2\alpha\,\sin(\alpha-\delta)\left[1+\sqrt{\dfrac{\sin(\varphi'+\delta)\,\sin(\varphi'-\varepsilon)}{\sin(\alpha-\delta)\,\sin(\alpha+\varepsilon)}}\right]^2}$$

Con paramento verticale, terrapieno orizzontale e δ = 0 si ritrova $K_a=\dfrac{1-\sin\varphi'}{1+\sin\varphi'}=\tan^2(45°-\varphi'/2)$.

**Rankine** nel programma è la stessa formula con δ = 0: la spinta è normale al paramento anche con terrapieno inclinato. Se ε supera φ′ il
radicando è negativo: il terrapieno è più ripido dell'angolo d'attrito e la formula non ha soluzione, quindi controlla profilo e parametri.

Il profilo del terrapieno a tratti si riduce a una **pendenza equivalente** ε, ricavata dal cuneo di rottura sul profilo vero.

## Spinta a riposo

$$K_0=1-\sin\varphi' \quad\text{(Jaky)}$$

con la correzione per il terrapieno inclinato del programma desktop, $K_0=(1-\sin\varphi')/(1-\sin\varepsilon)$.

## Pressioni

Lungo il paramento, a profondità z:

| Termine | Pressione |
|---|---|
| Terreno | $\sigma(z)=\sum_k K_k\,\gamma'_k\,\Delta z_k$: ogni strato sovrastante contribuisce con il proprio K e il proprio peso, alleggerito sotto falda |
| Sovraccarico q | $K\,q$, costante con la profondità |
| Coesione c′ | $-2\,c'\sqrt{K}$; le zone in trazione non spingono |
| Acqua | $\gamma_w\,(z-z_w)$ sotto la quota di falda, normale al paramento |

La componente orizzontale e quella verticale della spinta si ottengono con l'inclinazione δ (fase I) o φ′ (fase II).

## Spinta passiva

Davanti alla fondazione, sulla faccia di valle della suola (e del dente, se c'è), il terreno oppone la spinta passiva:

$$K_p=\frac{\sin^2(\alpha-\varphi')}{\sin^2\alpha\,\sin(\alpha+\delta)\left[1-\sqrt{\dfrac{\sin(\varphi'+\delta)\,\sin(\varphi'+\varepsilon)}{\sin(\alpha+\delta)\,\sin(\alpha+\varepsilon)}}\right]^2}$$

che per faccia verticale, piano orizzontale e δ = 0 vale $(1+\sin\varphi')/(1-\sin\varphi')$. Se ne usa la percentuale scelta nel passo
[Normativa e sisma](sisma.md); il terreno di ricoprimento sopra la suola non spinge.

## Azione sismica: Mononobe-Okabe

Con i coefficienti sismici k~h~ e k~v~ (vedi [Sisma](sisma.md)) l'angolo sismico è

$$\theta=\arctan\frac{k_h}{1-k_v}$$

e il coefficiente di spinta attiva in condizioni sismiche

$$K_{AE}=\frac{\sin^2(\alpha+\varphi'-\theta)}{\cos\theta\,\sin^2\alpha\,\sin(\alpha-\theta-\delta)\left[1+\sqrt{\dfrac{\sin(\varphi'+\delta)\,\sin(\varphi'-\varepsilon-\theta)}{\sin(\alpha-\theta-\delta)\,\sin(\alpha+\varepsilon)}}\right]^2}$$

La spinta totale è $E_d=\tfrac12(1+k_v)\,K_{AE}\,\gamma\,H^2$; l'**incremento sismico** rispetto alla statica,
$\Delta K=(1+k_v)K_{AE}-K_a$, si distribuisce sul paramento con la risultante a 2/3, 1/3 o 1/2 dell'altezza secondo l'opzione scelta.
Lo stesso incremento si applica ai sovraccarichi. Sotto falda l'angolo θ tiene conto del peso alleggerito del terreno.

Con la spinta a riposo l'incremento è $\Delta K=k_h$.

In condizioni sismiche anche la spinta passiva si riduce: K~PE~ di Mononobe-Okabe con δ = 0, moltiplicato per (1 − k~v~).

## Forze d'inerzia

Tutte le masse che si muovono con il muro ricevono una forza orizzontale k~h~·W e una verticale k~v~·W diretta verso l'alto (il verso sfavorevole), applicate nel baricentro:
paramento, fondazione, dente, terreno sopra la suola di monte fino al piano virtuale, sovraccarichi sopra la suola. Nelle sollecitazioni
del paramento entra l'inerzia del paramento stesso.

## Bibliografia

- Coulomb C.A. (1776), *Essai sur une application des règles de maximis et minimis à quelques problèmes de statique*.
- Müller-Breslau H. (1906), *Erddruck auf Stützmauern*, Kröner, Stuttgart.
- Rankine W.J.M. (1857), *On the stability of loose earth*, Phil. Trans. Royal Society.
- Jaky J. (1944), *The coefficient of earth pressure at rest*, Journal of the Society of Hungarian Architects and Engineers.
- Okabe S. (1926), *General theory of earth pressure*, Journal of the Japan Society of Civil Engineers.
- Mononobe N., Matsuo H. (1929), *On the determination of earth pressures during earthquakes*, World Engineering Congress, Tokyo.
- D.M. 17/01/2018, *Aggiornamento delle Norme tecniche per le costruzioni*, §6.5 e §7.11.6.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20MDC%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/mdc/docs/it/teoria-spinte.md).*
