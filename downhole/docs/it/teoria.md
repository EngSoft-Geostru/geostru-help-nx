# Cenni teorici

Questa pagina riassume che cosa misura la prova down-hole e come Downhole NX passa dai tempi
alle velocità e ai moduli. Le formule sono le stesse del
[documento di validazione](validazione.md) e dei cenni teorici che puoi includere nella
relazione.

## La prova down-hole

La prova sismica in foro misura i **tempi di tragitto** delle onde di compressione (P) e di
taglio (S) fra una **sorgente in superficie**, a distanza d dall'asse di un foro di
sondaggio, e un **ricevitore** calato nel foro a profondità successive.

- La sorgente è una piastra battuta verticalmente, per generare onde P, e lateralmente nei
  due versi, per generare onde di taglio polarizzate orizzontalmente (SH). Di norma sta a
  1,5–2,5 m dalla bocca del foro.
- Il ricevitore è un geofono a tre componenti premuto contro la parete del foro; un
  sismografo multicanale registra, e un trigger sulla sorgente fissa l'istante zero.
- Il foro è rivestito con un tubo cementato alla parete, perché le onde arrivino al
  ricevitore senza il disturbo dell'intercapedine.
- Le misure si eseguono di norma a passo di 1 m, mantenendo costante l'orientamento del
  geofono.

A ogni profondità si registrano una battuta verticale e due battute orizzontali di verso
opposto. Fra le due registrazioni S la polarità dell'onda di taglio **si inverte**, quella
dell'onda P no: è così che si riconosce il primo arrivo dell'onda S. Dalle registrazioni si
leggono i tempi di primo arrivo T~p~ e T~s~ a ciascuna profondità z.

## Tempi corretti

Il percorso sorgente–ricevitore è inclinato. Per una ricezione a profondità z, con la
sorgente a distanza orizzontale d:

SR = √(z² + d²)

t~corr~ = t · z / SR

SR è la distanza sorgente–ricevitore, t il tempo misurato, t~corr~ il tempo che l'onda
impiegherebbe lungo la verticale. L'ipotesi è il **percorso rettilineo** in un mezzo a
strati orizzontali.

## Metodo diretto

Nel diagramma tempo corretto–profondità (**dromocrona**) un mezzo omogeneo è una retta, e la
sua pendenza è la velocità. I cambi di pendenza individuano i **sismostrati**. Per lo strato
fra le profondità z~1~ e z~2~:

V = (z~2~ − z~1~) / [t~corr~(z~2~) − t~corr~(z~1~)]

t~corr~(z) è interpolato linearmente fra le due ricezioni adiacenti alla base, e
dall'origine sopra la prima ricezione. La velocità dello strato è quindi la pendenza della
**corda** fra le due basi, non una retta ai minimi quadrati sui punti dello strato.

Se fra due basi il tempo corretto non cresce, lo strato non ha una velocità propria: copia i
parametri del precedente ed è marcato con un asterisco.

## Metodo intervallo

Per due ricezioni consecutive alle profondità z~1~ < z~2~:

V = (z~2~ − z~1~) / (t~corr,2~ − t~corr,1~)

Il primo intervallo va dal piano campagna, a tempo zero, alla prima ricezione.

Con un solo ricevitore i due tempi vengono da due battute diverse: sono velocità di
**pseudo-intervallo**, e l'errore di trigger entra per intero nella differenza. Dove
t~corr,2~ ≤ t~corr,1~ il metodo non è applicabile e l'intervallo resta senza valore («--»).

Per ogni sismostrato del metodo intervallo si riportano le **medie** dei valori degli
intervalli che contiene; la base dello strato coincide sempre con una profondità di misura.

## Parametri elastici dinamici

Con la densità ρ = γ / g e g = 9,80665 m/s²:

| Grandezza | Formula |
|---|---|
| Coefficiente di Poisson | ν = ½ · [(V~p~/V~s~)² − 2] / [(V~p~/V~s~)² − 1] |
| Modulo di taglio | G = ρ · V~s~² |
| Modulo edometrico | E~d~ = ρ · V~p~² |
| Modulo di Young | E = 2 · G · (1 + ν) |
| Modulo di compressibilità volumetrica | E~v~ = ρ · (V~p~² − 4/3 · V~s~²) |

Il coefficiente di Poisson è accettato solo se 0 < ν < 0,5, cioè con V~p~/V~s~ > √2:
altrimenti ν ed E escono «--». Anche E~v~ esce «--» se risulta negativo.

!!! warning "Sono moduli dinamici"
    I moduli sono a piccole deformazioni. Non vanno usati in un calcolo di cedimenti senza
    una legge di decadimento con il livello deformativo.

## Peso di volume dalla correlazione

Quando il peso di volume non è assegnato alle misure, è stimato da una correlazione empirica
con V~s~ [m/s] e con la profondità media z [m] dello strato o dell'intervallo; γ è in kN/m³.

Per V~s~ < 800 m/s:

γ = [1 + 1 / (0,614 + 58,7 · (log~10~ z + 1,095) / V~s~)] · 9,80665

Per V~s~ ≥ 800 m/s:

γ = 0,8 · log~10~ V~s~ · 9,80665

La prima ha la forma della correlazione proposta per i terreni saturi da Burns e Mayne
(1996) a partire da misure con il cono sismico. È una **stima**: se disponi di misure,
assegnale alla tabella della scheda [Misure](misure.md#peso-di-volume-automatico-o-assegnato).

Esempio: V~s~ = 200 m/s, z = 5 m → γ = 18,41 kN/m³. Per V~s~ = 1 000 m/s, γ = 23,54 kN/m³ a
qualunque profondità.

## Velocità equivalente

V~s,eq~ = (H − z~0~) / Σ (h~i~ / V~s,i~)

sui tratti compresi fra la profondità iniziale z~0~ e la profondità H, con h~i~ spessore e
V~s,i~ velocità del tratto. Per le NTC 2018 (§3.2.2) z~0~ è il piano di posa della
fondazione e H la profondità del substrato, 30 m se più profondo: in quel caso è la
V~s,30~.

- Nel **metodo diretto** i tratti sono i sismostrati.
- Nel **metodo intervallo** i tratti sono gli **intervalli di misura**, con o senza
  sismostrati. La media aritmetica delle velocità d'intervallo di uno strato non è la
  velocità dello strato (che è spessore diviso tempo), e non può entrare nella formula.
- Se la prova è più corta di H, l'ultimo tratto è prolungato fino a H e l'app lo dichiara.

Una conseguenza utile come controllo: nel metodo diretto Σ h~i~/V~s,i~ è il tempo corretto
delle onde S alla profondità H. La V~s,eq~ quindi **non dipende da dove si pongono gli
strati**, e i due metodi danno lo stesso valore, a meno degli arrotondamenti.

## Proposte automatiche

Le proposte dei tempi di arrivo e dei sismostrati **non fanno parte del calcolo**: producono
dati di ingresso, tempi e basi degli strati, che accetti, correggi o scarti. Una volta
accettati, il calcolo è quello dei paragrafi precedenti.

### Tempi di arrivo delle onde P

Sul canale verticale, fra l'inizio del registro e il massimo della traccia, si cerca
l'istante k che rende minimo il **criterio di Akaike**:

AIC(k) = k · ln σ²(x~1~…x~k~) + (n − k) · ln σ²(x~k+1~…x~n~)

dove σ² è la varianza dei campioni prima e dopo k. Il minimo è il punto in cui la traccia
passa dal rumore al segnale.

### Tempi di arrivo delle onde S

Sui canali orizzontali l'onda di taglio è preceduta dalla coda delle onde P. Per questo:

1. si costruisce la componente orizzontale di massima energia; con due battute di verso
   opposto si lavora sulla loro differenza, in cui le onde P si cancellano;
2. si applica un filtro passa-basso a 150 Hz, senza sfasamento;
3. si individua il picco dell'onda di taglio e si applica lo stesso criterio nella finestra
   di 1,25 periodi che lo precede.

Poi si guarda il profilo intero. Un tempo che si scosta di oltre 3 ms dalla retta robusta
(Theil–Sen) dei tempi alle profondità vicine viene ricercato attorno al valore atteso e
marcato **dubbio**. È dubbio anche un tempo che non cresce con la profondità, o letto su una
traccia con rapporto segnale/rumore basso.

Il filtro senza sfasamento allarga il treno d'onda da entrambi i lati: sulle S la proposta
può anticipare l'arrivo di qualche millisecondo.

### Sismostrati

Si considerano tutte le suddivisioni con le basi su profondità di misura e almeno due
intervalli per strato. Con una ricerca esaustiva (programmazione dinamica) si sceglie quella
la cui spezzata, che nel metodo diretto unisce i tempi corretti alle basi, ha il minimo
scarto quadratico dai tempi corretti di P e S.

Il numero di strati m è quello che rende minimo

N · ln(RSS / N) + 1,5 · (2m − 1) · ln N

con N numero dei tempi e RSS somma degli scarti quadratici, mai inferiore all'incertezza di
lettura (0,3 ms per tempo). Il secondo termine fa pagare ogni strato in più: senza, la
suddivisione migliore avrebbe uno strato per ogni coppia di intervalli.

Quanto valgono le proposte su dati reali è in
[Validazione](validazione.md#caso-8-le-proposte-automatiche).

## Arrotondamenti

Il calcolo procede su valori arrotondati, come il programma desktop da cui deriva: tempi
corretti a 4 decimali di millisecondo, velocità e pesi di volume a 2 decimali, ν
d'intervallo a 4, tempi alle basi degli strati a 2 decimali di millisecondo.

L'effetto è piccolo ma visibile su strati sottili e veloci: 0,01 ms su uno strato di 2 m a
2 000 m/s (1 ms di attraversamento) è l'1 % della velocità.

## Limiti del metodo

- **La qualità del risultato è quella dei tempi di arrivo.** L'app può proporli, ma una
  proposta non è una lettura: vanno sempre riguardati sulle tracce, a partire da quelli
  marcati come dubbi. Lo stesso vale per i sismostrati proposti: sono la suddivisione che
  meglio segue i tempi, non un'interpretazione geologica. La velocità d'intervallo è sensibile a errori anche piccoli quando l'intervallo è
  corto; il metodo diretto media su più ricezioni ed è più stabile, ma dipende dalla scelta
  dei sismostrati.
- **Percorsi rettilinei.** Con forti contrasti di velocità vicino alla superficie il
  percorso reale è rifratto e i tempi corretti delle prime ricezioni sono approssimati.
  L'effetto cresce con d e si esaurisce in profondità (Kim et al., 2004). Il primo
  intervallo, dal piano campagna alla prima ricezione, è il valore più sensibile.
- **Nessuna correzione** per l'inclinazione del foro né per la quota della sorgente rispetto
  al piano campagna.
- **La classificazione del sottosuolo resta al progettista**: la V~s,eq~ è un numero, e per
  attribuire la categoria serve la profondità del substrato, che la prova da sola non sempre
  raggiunge.

## Bibliografia

- Akaike H. (1974), *A new look at the statistical model identification*, IEEE Transactions
  on Automatic Control, 19(6). Per l'uso sui primi arrivi: Maeda N. (1985), *A method for
  reading and checking phase times in auto-processing system of seismic wave data*, Zisin,
  38.
- ASTM D7400, *Standard Test Methods for Downhole Seismic Testing*.
- Auld B. (1977), *Cross-hole and down-hole Vs by mechanical impulse*, Journal of the
  Geotechnical Engineering Division, ASCE, 103(GT12).
- Burns S.E., Mayne P.W. (1996), *Small- and high-strain measurements of in-situ soil
  properties using the seismic cone penetrometer*, Transportation Research Record 1548.
- Carrara E., Rapolla A., Roberti N., *Le indagini geofisiche per lo studio del sottosuolo:
  metodi geoelettrici e sismici*, Liguori.
- Kim D.S., Bang E.S., Kim W.C. (2004), *Evaluation of various downhole data reduction
  methods for obtaining reliable Vs profiles*, Geotechnical Testing Journal, 27(6).
- Kramer S.L. (1996), *Geotechnical Earthquake Engineering*, Prentice Hall.
- D.M. 17/01/2018, *Norme tecniche per le costruzioni*, §3.2.2.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Downhole%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/downhole/docs/it/teoria.md).*
