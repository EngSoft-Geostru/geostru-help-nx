# Metodi di interpretazione

Questa pagina è il catalogo dei metodi che GeoTheis NX applica alle prove. Per ognuno trovi i dati che servono, le ipotesi, che cosa
restituisce e i limiti. Non scegli tu quali calcolare: il programma calcola **tutti** i metodi che i dati consentono e li mette a
confronto nella scheda [Risultati](risultati.md). Un metodo senza i dati necessari compare fra i *Non applicabili*, con il motivo.

Le formule sono riportate in forma breve. Le basi teoriche, le ipotesi per esteso e la bibliografia stanno in [Teoria](teoria.md);
come leggere grafici, affidabilità e proposte sta in [Risultati](risultati.md).

Notazione: Q portata, s abbassamento, r distanza dal pozzo, t tempo dall'inizio del pompaggio, t′ tempo dall'arresto, T
trasmissività (m²/s), K permeabilità (m/s), S coefficiente di immagazzinamento (adimensionale), R raggio d'azione (m), b spessore
dell'acquifero in pressione (tetto − substrato), H~1~ spessore saturo della falda libera (livello statico − substrato), r~w~ raggio
del pozzo, L lunghezza del filtro.

## Quali dati per quali metodi

| Dati inseriti | Metodi calcolati |
|---|---|
| Prova a gradini, 2 gradini validi | [Curva caratteristica (Jacob)](#curva-caratteristica-jacob-n-2) |
| Prova a gradini, 3 o più gradini validi | in più [Rorabaugh](#curva-caratteristica-rorabaugh-n-libero) |
| Prova a gradini con i piezometri | in più [distanza-abbassamento sui gradini](#distanza-abbassamento-sui-gradini-thiem), [Dupuit-Thiem per gradino](#dupuit-thiem-per-gradino), [Cooper-Jacob sulle stazioni di prova](#cooper-jacob-sulle-stazioni-di-prova) |
| Prova a gradini con la portata critica scelta e il raggio d'azione presunto | in più i [pozzi singoli](#pozzi-singoli) |
| Nessun gradino valido, **portata critica nota** completa (Q~c~, s~c~, R presunto) | [pozzi singoli](#pozzi-singoli) |
| Portata costante con il solo pozzo | [Cooper-Jacob](#cooper-jacob-abbassamento) e [risalita](#risalita-theis-retta-di-cooper-jacob) sul pozzo: T sì, S no |
| Portata costante con letture di pompaggio nei piezometri | in più [Theis (fitting automatico)](#theis-fitting-automatico); con almeno due piezometri a distanze diverse anche la [distanza-abbassamento](#distanza-abbassamento-cooper-jacob) |
| Abbassamenti stabilizzati | in più [Dupuit-Thiem (regime stazionario)](#dupuit-thiem-regime-stazionario) |
| Falda semiconfinata con letture nei piezometri | in più [Hantush (fitting automatico)](#hantush-fitting-automatico) |
| Ritocco della curva tipo, o punto salvato dal programma desktop | in più [Theis o Hantush (punto di coincidenza)](#theis-e-hantush-punto-di-coincidenza) |

Un gradino è valido se ha portata e abbassamento nel pozzo positivi. Le regole d'inserimento dei dati sono in [Prova](prove.md); il
tipo di falda e la penetrazione del pozzo si scelgono in [Pozzo](pozzo.md).

!!! note "Nota"
    Il tipo di falda decide molto: Hantush si calcola solo in falda **semiconfinata**; Dupuit-Thiem stazionario e i pozzi singoli non si
    calcolano in falda semiconfinata. Se il tipo di falda non è indicato, i metodi della portata costante assumono la falda in
    pressione e lo dicono in un avviso.

## Prova a gradini

I metodi della prova a gradini usano gli abbassamenti **a fine gradino**. Descrivono il pozzo (perdite, portata critica) meglio
dell'acquifero: i valori di T e K che ne escono sono indicativi rispetto alla prova a portata costante.

### Curva caratteristica (Jacob, n = 2)

*Jacob (1947); Walton (1962).*

- **Dati**: almeno 2 gradini validi a portate diverse.
- **Ipotesi**: l'abbassamento nel pozzo è la somma di una perdita lineare dell'acquifero e di una perdita quadratica del pozzo.

$$
s = B\,Q + C\,Q^2, \qquad \frac{s}{Q} = B + C\,Q
$$

B e C vengono dalla retta di s/Q contro Q ai minimi quadrati sui gradini validi.

- **Restituisce**: B (s/m²), C (s²/m⁵), R² della retta, efficienza del pozzo E = BQ/(BQ + CQ²), la portata critica proposta Q = B/C
  (efficienza 50 %), le condizioni del pozzo secondo Walton (C in min²/m⁵) e, quando hai scelto la portata critica Q~c~ sul grafico:
  Q~ott~ = 0,9·Q~c~, s~c~ = B·Q~c~ + C·Q~c~², la portata specifica critica Q~c~/s~c~ e l'efficienza alla portata ottimale.
- **Non restituisce** T, K, S, R.
- **Limiti**: con 2 soli gradini la retta passa per i punti e non c'è verifica di bontà; B o C non positivi indicano gradini troppo
  brevi o non a regime. È la base della [portata concedibile](risultati.md#portata-concedibile).

| C (min²/m⁵) | Condizioni del pozzo (Walton) |
|---|---|
| ≤ 0,5 | Correttamente progettato e sviluppato |
| 0,5 – 1 | Deterioramento moderato dovuto a intasamento |
| 1 – 4 | Deterioramento grave o intasamento |
| > 4 | Difficoltà a riportare il pozzo nelle condizioni originali |

### Curva caratteristica (Rorabaugh, n libero)

*Rorabaugh (1953).*

- **Dati**: almeno 3 gradini validi.
- **Ipotesi**: come Jacob, con l'esponente delle perdite del pozzo libero: s = B·Q + C·Qⁿ (con n = 2 si ritrova Jacob).
- **Restituisce**: B, C, n con l'intervallo al 95 %, lo scarto quadratico medio sugli abbassamenti.
- **Limiti**: con 3 gradini la curva passa esattamente per i punti; n fuori da 1,5–3,5 descrive i punti ma non ha il significato
  fisico di Rorabaugh. Il risultato è allora indicativo.

### Distanza-abbassamento sui gradini (Thiem)

*Thiem (1906).*

- **Dati**: gradini con gli abbassamenti nei piezometri; per ogni gradino almeno due piezometri con abbassamento che cala con la
  distanza.
- **Ipotesi**: per ogni gradino, retta di s contro log~10~ r (Thiem in distanza), come se a fine gradino il regime fosse stazionario.
- **Restituisce**: per gradino Δs per ciclo logaritmico, T = ln10·Q/(2π·Δs), K = T/b (T/H~1~ in falda libera) e R dove la retta dà
  s = 0; le medie sui gradini calcolati.
- **Limiti**: sempre indicativo (i gradini non sono a regime). In falda semiconfinata T si calcola come in falda in pressione, senza
  il drenaggio.

### Dupuit-Thiem per gradino

*Dupuit (1863); Thiem (1906).*

- **Dati**: gradini, pozzo **completo**, almeno un piezometro, falda **libera** o **in pressione**.
- **Ipotesi**: gli abbassamenti a fine gradino trattati come regime stazionario. Con due o più piezometri si usa la coppia dei
  piezometri 1 e 2; con uno solo la coppia pozzo – piezometro.
- **Restituisce**: T e K per gradino e le medie. In pressione T = Q·ln(r~b~/r~a~)/(2π·(s~a~ − s~b~)), K = T/b; in falda libera
  la formula di Dupuit, T = K·H~1~.
- **Limiti**: sempre indicativo. Con la coppia pozzo – piezometro l'abbassamento del pozzo comprende le perdite di carico e T risulta
  sottostimata.

### Cooper-Jacob sulle stazioni di prova

*Cooper & Jacob (1946).*

- **Dati**: gradini con il **Tempo** di fine gradino, pozzo completo, piezometri, falda **in pressione**.
- **Ipotesi**: retta di s/Q contro log~10~ t sui gradini, per piezometro.
- **Restituisce**: T, S (dalla distanza del piezometro) e K = T/b.
- **Limiti**: i gradini hanno portate diverse e la retta non tiene conto della sovrapposizione degli effetti: il risultato è
  indicativo e **non si usa mai per il progetto**.

### Pozzi singoli

*Dupuit (1863); Thiem (1906); Chiesa; Celico.*

- **Dati**: una coppia critica (Q~c~, s~c~) e un **raggio d'azione presunto R**; la geometria del pozzo (r~w~, filtro) e le quote
  dell'acquifero. La coppia è quella della prova a gradini (Q~c~ scelta sul grafico, s~c~ = B·Q~c~ + C·Q~c~²) oppure, senza gradini
  validi, la **portata critica nota** scritta in [Prova](prove.md#portata-critica-nota-senza-prova-a-gradini). R presunto si scrive in
  quel riquadro in entrambi i casi.
- **Ipotesi**: la coppia critica trattata come un regime stazionario. Falda **libera** o **in pressione**; serve sapere se il pozzo è
  completo o incompleto.
- **Restituisce**: T e K per ogni formula applicabile.
- **Limiti**: sempre indicativo (regime presunto, R presunto). Non si calcola in falda semiconfinata.

| Pozzo e falda | Formule calcolate |
|---|---|
| Completo, falda libera | Dupuit: K = Q·ln(R/r~w~)/(π·(H~1~² − H~2~²)), T = K·H~1~, con H~2~ = H~1~ − s |
| Completo, in pressione | Thiem: T = Q·ln(R/r~w~)/(2π·s), K = T/b |
| Incompleto, falda libera | Chiesa (p. 187), con la distanza fra il fondo del filtro e il substrato |
| Incompleto, in pressione | Chiesa formula 5 (tipo A) o 11 (tipi B e C), più Muskat, Kozeny, spessore infinito (Babushkin), Halek, Girinski, Zangar, «L/b − L/2r» |

I tipi del pozzo incompleto in pressione (Chiesa): **A** filtro staccato dal tetto che non arriva al substrato; **B** filtro attaccato
al tetto e più corto dello spessore; **C** filtro staccato dal tetto che arriva al substrato.

!!! warning "Attenzione"
    Muskat, Girinski, «L/b − L/2r» e la formula dei tipi B e C sono segnati **da verificare**: sono formule del programma desktop non
    ancora verificate sul testo di riferimento. Leggili come controllo, non come valore di progetto.

## Prova a portata costante

Tutti i metodi della portata costante richiedono la **Portata della prova**. Quelli sui piezometri richiedono la distanza r del
piezometro (scheda [Pozzo](pozzo.md)).

### Cooper-Jacob (abbassamento)

*Cooper & Jacob (1946); Kruseman & de Ridder (1994).*

- **Dati**: letture di pompaggio nel pozzo e/o nei piezometri.
- **Ipotesi**: approssimazione logaritmica di Theis, valida per u = r²S/(4Tt) < 0,05: retta di s contro log~10~ t sul tratto finale.
  Il programma sceglie da solo il tratto rettilineo; puoi cambiarlo (vedi
  [Intervallo di Cooper-Jacob](risultati.md#intervallo-di-cooper-jacob)).

$$
T = \frac{\ln 10\; Q}{4\pi\,\Delta s}, \qquad S = \frac{2{,}25\,T\,t_0}{r^2}
$$

- **Restituisce**: per serie T (con intervallo al 95 %), K, S, il tratto usato; le medie sui piezometri e R a fine pompaggio,
  R = √(2,25·T·t/S).
- **Limiti**: dal solo pozzo T sì (comprende l'effetto delle perdite sul tratto iniziale), S no: S dal pozzo non è affidabile e non
  entra nella media. Con meno di 3 punti nella retta la serie è indicativa. In falda libera vale per abbassamenti piccoli rispetto a
  H~1~; in falda semiconfinata solo prima che il drenaggio si faccia sentire.

### Risalita (Theis, retta di Cooper-Jacob)

*Theis (1935); Kruseman & de Ridder (1994).*

- **Dati**: letture di pompaggio e di risalita, istante dell'arresto della pompa.
- **Ipotesi**: abbassamento residuo s′ contro log~10~(t/t′), con t = t~arresto~ + t′; usa tutti i punti validi.
- **Restituisce**: T e K per serie e medi. Non dà S né R.
- **Limiti**: con il solo pozzo è indicativo. Una T di risalita lontana oltre il 30 % da quella di pompaggio chiede di controllare
  l'istante d'arresto e il tratto rettilineo. Il punto in cui la retta arriva a s′ = 0 dice qualcosa sull'acquifero: t/t′ ≈ 1
  recupero completo, molto oltre 1 ricarica, sotto 1 limite impermeabile o volume finito.

### Theis (fitting automatico)

*Theis (1935).*

- **Dati**: letture di pompaggio in almeno un piezometro (le letture del pozzo non entrano).
- **Ipotesi**: falda in pressione, omogenea, isotropa, illimitata; pozzo completo; portata costante.

$$
s = \frac{Q}{4\pi T}\,W(u), \qquad u = \frac{r^2 S}{4 T t}
$$

- **Restituisce**: per piezometro T e S con l'intervallo al 95 %, lo scarto tipico fra curva e dati; le medie sulle serie arrivate a
  convergenza e R(t) a fine pompaggio.
- **Come lavora**: minimi quadrati sui logaritmi degli abbassamenti (Levenberg-Marquardt), partendo da Cooper-Jacob. Il punto di
  coincidenza è un risultato, non un dato da scegliere.
- **Limiti**: affidabile con scarto tipico fino al 25 %, indicativo oltre, non affidabile se il fitting non arriva a convergenza.
  Servono più punti che parametri. In falda libera o semiconfinata e con pozzo incompleto si calcola con un avviso.

### Hantush (fitting automatico)

*Hantush & Jacob (1955); Hantush (1956).*

- **Dati**: falda **semiconfinata** (libera o in pressione), letture di pompaggio in almeno un piezometro.
- **Ipotesi**: come Theis, più il drenaggio da uno strato semipermeabile senza immagazzinamento; terzo parametro r/B.
- **Restituisce**: T, S, r/B per piezometro; il fattore di drenanza B = r/(r/B) e la resistenza idraulica c = B²/T dello strato
  semipermeabile; medie e R(t).
- **Limiti**: se r/B scende sotto 0,001 il drenaggio non si vede nei dati: il programma rifà il fitting con Theis e B e c non sono
  determinabili. Non considera l'immagazzinamento del semipermeabile.

### Theis e Hantush (punto di coincidenza)

- **Dati**: un punto di coincidenza per piezometro, che nasce dal **Ritocco** della curva tipo (vedi
  [Ritocco della curva tipo](risultati.md#ritocco-della-curva-tipo-theis-e-hantush)) o da un file del programma desktop.
- **Restituisce**: T = Q·W/(4π·s), S = 4·T·u·(t/r²); per Hantush anche B e c.
- **Limiti**: al massimo indicativo; non affidabile se la curva del punto sta lontana dai dati (scarto tipico oltre il 50 %) o dà
  S > 1. Non è mai proposto da solo: lo porti in uso con **Usa per il progetto**.

### Dupuit-Thiem (regime stazionario)

*Dupuit (1863); Thiem (1906).*

- **Dati**: **Abbassamenti stabilizzati** nei piezometri (scheda [Prova](prove.md#portata-della-prova-e-abbassamenti-stabilizzati)),
  pozzo **completo**, falda libera o in pressione; in falda libera H~1~.
- **Ipotesi**: regime stazionario. Con due o più piezometri, retta di s contro log~10~ r sui soli piezometri; R dove la retta dà s = 0.
  In falda libera la retta è su Z = s·(2H~1~ − s).
- **Restituisce**: T, K, R; con due o più piezometri e l'abbassamento stabilizzato nel pozzo anche l'abbassamento teorico alla parete e le **perdite di
  carico** del pozzo (misurato − teorico).
- **Limiti**: con un solo piezometro si usa la coppia pozzo – piezometro, e il risultato è indicativo. Non vale in falda semiconfinata
  (usare Hantush) né per il pozzo incompleto.

### Distanza-abbassamento (Cooper-Jacob)

*Cooper & Jacob (1946); Kruseman & de Ridder (1994).*

- **Dati**: almeno due piezometri a distanze diverse letti allo stesso tempo di pompaggio.
- **Ipotesi**: retta di s contro log~10~ r al tempo t; il programma usa l'ultima lettura di pompaggio in cui almeno due piezometri
  hanno un abbassamento. Il pozzo non entra.
- **Restituisce**: T = ln10·Q/(2π·Δs), r~0~ dove s = 0 (usato come R), S = 2,25·T·t/r~0~².
- **Limiti**: affidabile con 3 o più piezometri; con 2 la retta passa per i punti. A quel tempo u deve essere sotto 0,05 anche al
  piezometro più lontano.

## Grandezze derivate

- **K**: quella del metodo; se il metodo dà solo T, K = T/b in pressione e in falda semiconfinata, K = T/H~1~ in falda libera. Senza lo
  spessore K non si calcola.
- **R transitorio**: R(t) = √(2,25·T·t/S) a fine pompaggio, dai metodi che danno T e S.
- **Valore di progetto**, **portata concedibile** e **cono di depressione** non sono metodi: li ricava il programma dai metodi
  calcolati. Vedi [Valore di progetto](risultati.md#valore-di-progetto), [Portata concedibile](risultati.md#portata-concedibile) e
  [Cono di depressione](risultati.md#cono-di-depressione).

## Riepilogo

| Metodo | T | K | S | R | Altro | Affidabilità al meglio |
|---|---|---|---|---|---|---|
| Curva caratteristica (Jacob) | — | — | — | — | B, C, E, Q~c~, Q~ott~, s~c~, Walton | affidabile |
| Rorabaugh | — | — | — | — | B, C, n | affidabile |
| Distanza-abbassamento sui gradini | ✓ | ✓ | — | ✓ | per gradino | indicativo |
| Dupuit-Thiem per gradino | ✓ | ✓ | — | — | per gradino | indicativo |
| Cooper-Jacob sulle stazioni | ✓ | ✓ | ✓ | — | mai per il progetto | indicativo |
| Pozzi singoli | ✓ | ✓ | — | — | per formula | indicativo |
| Cooper-Jacob | ✓ | ✓ | ✓ (piezometri) | ✓ | tratto usato | affidabile |
| Risalita | ✓ | ✓ | — | — | t/t′ a s′ = 0 | affidabile |
| Theis (fitting) | ✓ | ✓ | ✓ | ✓ | intervalli al 95 % | affidabile |
| Hantush (fitting) | ✓ | ✓ | ✓ | ✓ | r/B, B, c | affidabile |
| Punto di coincidenza | ✓ | ✓ | ✓ | ✓ | B, c (Hantush) | indicativo |
| Dupuit-Thiem stazionario | ✓ | ✓ | — | ✓ | perdite del pozzo | affidabile |
| Distanza-abbassamento | ✓ | ✓ | ✓ | ✓ (r~0~) | tempo usato | affidabile |

I criteri completi di affidabilità e l'ordine con cui il programma sceglie il metodo da proporre sono in [Risultati](risultati.md).

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20GeoTheis%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/geotheis/docs/it/metodi.md).*
