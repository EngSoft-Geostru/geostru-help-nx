# Cenni teorici

Questa pagina riassume la teoria delle prove di emungimento usata da GeoTheis NX: tipi di falda, regime stazionario e transitorio,
metodi della prova a portata costante e della prova a gradini, perdite di carico, raggio d'azione e pozzi singoli. Le formule sono
quelle del motore di calcolo. Come il programma sceglie e confronta i metodi è spiegato in [Risultati](risultati.md); il glossario
dei simboli è in [Glossario](glossario.md).

Notazione: Q portata, s abbassamento, r distanza dal pozzo, t tempo dall'inizio del pompaggio, t′ tempo dall'arresto della pompa,
T trasmissività, S coefficiente di immagazzinamento, K conducibilità idraulica (permeabilità), b spessore della falda confinata,
H~1~ spessore saturo della falda libera, r~w~ raggio del pozzo, R raggio d'azione. Il motore lavora in unità SI (m, s, m³/s, m²/s,
m/s); l/s, m³/h, minuti e valori al giorno sono solo presentazione.

## Tipi di falda

| Tipo (scheda Pozzo) | Descrizione | Spessore usato |
|---|---|---|
| **Libera** | falda freatica: la superficie dell'acqua è a pressione atmosferica e si abbassa pompando | H~1~ = livello statico − substrato |
| **In pressione** | falda confinata (artesiana): chiusa fra due strati impermeabili, il livello sale sopra il tetto dell'acquifero | b = tetto − substrato |
| **Semiconfinata, libera** | sotto uno strato semipermeabile che la alimenta, con superficie libera | b, come la confinata |
| **Semiconfinata, in pressione** | sotto uno strato semipermeabile che la alimenta, in pressione | b, come la confinata |

La **trasmissività** è la portata che attraversa una striscia di acquifero larga 1 m, per tutto lo spessore, sotto un gradiente
unitario: T = K·b in falda confinata, T = K·H~1~ in falda libera. Il **coefficiente di immagazzinamento** S è il volume d'acqua
rilasciato da una colonna di base unitaria per un abbassamento unitario del carico. In falda confinata S è piccolo (tipicamente
10⁻⁵–10⁻³) perché l'acqua viene dalla compressibilità dell'acqua e dello scheletro; in falda libera viene dal drenaggio dei pori e S si
avvicina alla porosità efficace (tipicamente 10⁻²–0,3).

In falda semiconfinata lo strato semipermeabile cede acqua all'acquifero quando il carico si abbassa (**drenanza**). La sua
resistenza idraulica c = spessore/permeabilità verticale del semipermeabile definisce il **fattore di drenanza** B = √(T·c).

## Regime stazionario e transitorio

Durante il pompaggio a portata costante il cono di depressione si allarga nel tempo: è il **regime transitorio**, descritto da
Theis, Cooper-Jacob e Hantush, che danno T e S. Se il cono smette di allargarsi (ricarica, drenanza, limiti alimentanti) gli
abbassamenti si stabilizzano: è il **regime stazionario** di Dupuit-Thiem, che dà T (o K) e il raggio d'azione R ma non S.

Ipotesi comuni ai metodi analitici: acquifero omogeneo, isotropo, di spessore costante ed estensione illimitata; flusso orizzontale
verso un pozzo completo; portata costante; pozzo di raggio trascurabile. Dove i tuoi dati se ne allontanano il programma calcola
comunque e lo dice con un avviso (vedi [Limiti](risultati.md#limiti)).

## Prova a portata costante

### Theis (1935)

Soluzione del regime transitorio in falda confinata:

$$
s = \frac{Q}{4\pi T}\,W(u), \qquad u = \frac{r^2 S}{4 T t}, \qquad W(u) = \int_u^\infty \frac{e^{-y}}{y}\,dy
$$

W(u) è la **funzione di pozzo** (l'integrale esponenziale E~1~). Il motore la calcola con le serie di Abramowitz & Stegun (5.1.11 per
u ≤ 1, frazione continua 5.1.22 per u > 1), con errore relativo dell'ordine di 10⁻¹⁵.

Il metodo classico sovrappone in scala bilogaritmica le letture s – t/r² alla curva tipo W(u) – 1/u e legge un **punto di
coincidenza** (W, u, s, t/r²):

$$
T = \frac{Q\,W}{4\pi s}, \qquad S = 4\,T\,u\,\frac{t}{r^2}
$$

GeoTheis NX fa la stessa sovrapposizione con un **fitting automatico** ai minimi quadrati (Levenberg-Marquardt) sui logaritmi degli
abbassamenti di ogni piezometro, e dà T e S con l'intervallo di confidenza al 95 %. Il punto di coincidenza resta disponibile come
ritocco (vedi [Risultati](risultati.md#ritocco-della-curva-tipo-theis-e-hantush)).

### Cooper-Jacob (1946)

Per u piccolo la serie di W(u) si riduce ai primi due termini, W(u) ≈ −0,5772 − ln u, e l'abbassamento cresce linearmente con il
logaritmo del tempo:

$$
s = \frac{2{,}303\,Q}{4\pi T}\,\log_{10}\frac{2{,}25\,T\,t}{r^2 S}
$$

Dalla retta s – log~10~ t, con Δs l'abbassamento per ciclo logaritmico e t~0~ il tempo a cui la retta dà s = 0:

$$
T = \frac{\ln 10\;Q}{4\pi\,\Delta s}, \qquad S = \frac{2{,}25\,T\,t_0}{r^2}
$$

L'approssimazione vale per **u < 0,05**. Il programma usa da solo il tratto finale con t > 11,25·t~0~ (cioè u < 0,05) e ricalcola t~0~
finché la scelta non cambia. Sul pozzo di emungimento T si ricava, S no: le perdite di carico del pozzo e il raggio effettivo incerto
falsano l'intercetta.

### Risalita (Theis 1935)

Dopo l'arresto la falda risale. Per sovrapposizione degli effetti (pompaggio che continua più un'immissione uguale dall'arresto),
l'abbassamento residuo s′ è:

$$
s' = \frac{2{,}303\,Q}{4\pi T}\,\log_{10}\frac{t}{t'}, \qquad t = t_{arresto} + t', \qquad T = \frac{\ln 10\;Q}{4\pi\,\Delta s'}
$$

con Δs′ l'abbassamento residuo per ciclo di t/t′. La risalita dà T ma non S. Se la retta arriva a s′ = 0 per t/t′ molto diverso da 1
la falda ha una ricarica (t/t′ > 1) o un limite impermeabile o un volume finito (t/t′ < 1).

### Hantush-Jacob (1955)

In falda semiconfinata, con lo strato semipermeabile senza immagazzinamento:

$$
s = \frac{Q}{4\pi T}\,W\!\left(u, \tfrac{r}{B}\right), \qquad W\!\left(u, \tfrac{r}{B}\right) = \int_u^\infty \frac{1}{y}\exp\!\left(-y - \frac{(r/B)^2}{4y}\right)dy, \qquad B = \sqrt{T c}
$$

Ai tempi brevi la curva segue Theis; ai tempi lunghi la drenanza la appiattisce verso il valore stazionario W(0, r/B) = 2·K~0~(r/B). Il
motore calcola W(u, r/B) con un'integrazione numerica (Gauss-Kronrod), non con la tabella di Hantush. Con un punto di coincidenza:
T = Q·W/(4π·s), S = 4·T·u·(t/r²), B = r/(r/B), c = B²/T. Il programma applica Hantush solo se la falda è semiconfinata; se il
fitting porta r/B sotto 10⁻³ la drenanza non si vede nei dati e il risultato coincide con Theis.

### Dupuit-Thiem, regime stazionario (Dupuit 1863; Thiem 1906)

Con gli abbassamenti stabilizzati dei piezometri:

$$
\text{falda confinata: } s_1 - s_2 = \frac{Q}{2\pi T}\ln\frac{r_2}{r_1}, \qquad T = \frac{\ln 10\;Q}{2\pi\,\Delta s}
$$

$$
\text{falda libera: } H_1^2 - h^2 = \frac{Q}{\pi K}\ln\frac{R}{r}, \qquad K = \frac{\ln 10\;Q}{\pi\,\Delta Z}, \qquad Z = s\,(2H_1 - s), \qquad T = K\,H_1
$$

dove Δs (o ΔZ) è la variazione per ciclo logaritmico di distanza sulla retta s – log~10~ r (o Z – log~10~ r) dei piezometri, e R è
la distanza a cui la retta dà s = 0. Con un solo piezometro la retta passa per il pozzo, e il risultato è indicativo.

### Distanza-abbassamento

Sulla stessa retta s – log~10~ r, ma con gli abbassamenti dei piezometri **allo stesso tempo t** del pompaggio (Cooper-Jacob in
distanza): T = ln10·Q/(2π·Δs), r~0~ dove s = 0, S = 2,25·T·t/r~0~². Servono almeno due piezometri a distanze diverse, e u piccolo anche
al piezometro più lontano.

## Prova a gradini di portata

Il pozzo si pompa a portate crescenti Q~1~, Q~2~, … per gradini di uguale durata; per ogni gradino si legge l'abbassamento a fine
gradino (cumulato dall'inizio della prova).

### Perdite di carico ed equazione di Jacob (1947)

L'abbassamento nel pozzo è la somma di una **perdita lineare dell'acquifero** (flusso laminare, BQ) e di una **perdita quadratica del
pozzo** (flusso turbolento nei filtri, nel dreno e vicino al pozzo, CQ²):

$$
s = B\,Q + C\,Q^2, \qquad \frac{s}{Q} = B + C\,Q
$$

B e C sono l'intercetta e la pendenza della retta dell'**abbassamento specifico** s/Q contro Q, ai minimi quadrati sui gradini validi.
s/Q (o il suo inverso Q/s, la **portata specifica**) dice quanto «rende» il pozzo.

L'**efficienza** del pozzo è la quota di abbassamento dovuta all'acquifero:

$$
E = \frac{B\,Q}{B\,Q + C\,Q^2}
$$

e cala al crescere della portata. Il programma la calcola alla portata di riferimento indicata nel progetto, altrimenti alla portata
ottimale.

### Portata critica e portata ottimale

La **portata critica** Q~c~ è la portata oltre la quale le perdite del pozzo crescono in modo sproporzionato rispetto al beneficio: la
scegli tu sulla curva caratteristica s(Q). Se non la scegli il programma propone Q = B/C, la portata a cui le perdite del pozzo
eguagliano quelle dell'acquifero (E = 50 %). La **portata ottimale** è Q~ott~ = 0,9·Q~c~, e l'**abbassamento critico** s~c~ è quello
della curva a Q~c~.

### Condizioni del pozzo (Walton 1962)

Classi sul coefficiente C espresso in min²/m⁵:

| C (min²/m⁵) | Condizione del pozzo |
|---|---|
| ≤ 0,5 | correttamente progettato e sviluppato |
| 0,5–1 | deterioramento moderato dovuto a intasamento |
| 1–4 | deterioramento grave o intasamento |
| > 4 | difficile riportare il pozzo alle condizioni originali |

### Rorabaugh (1953)

Generalizza Jacob con un esponente libero:

$$
s = B\,Q + C\,Q^n
$$

stimato ai minimi quadrati sugli abbassamenti (con n = 2 si ritrova Jacob). Servono almeno tre gradini; con tre la curva passa per i
punti. Valori di n fuori da 1,5–3,5 non hanno il significato fisico di Rorabaugh e il programma lo segnala.

### Metodi in distanza sui gradini

Con i piezometri gli abbassamenti di fine gradino danno anche:

- **retta di Thiem in distanza** per ogni gradino: s contro log~10~ r sui piezometri, T = ln10·Q/(2π·Δs), K = T/b (o T/H~1~ in falda
  libera), R dove s = 0;
- **Dupuit-Thiem per gradino**: la coppia di letture pozzo–P1 o P1–P2 come in regime stazionario;
- **Cooper-Jacob sulle stazioni di prova**: s/Q contro log~10~ t sui gradini, T = 2,30/(4π·Δ(s/Q)), S = 2,25·T·t~0~/r².

Gli abbassamenti di fine gradino non sono a regime: questi risultati sono **indicativi**, e l'ultimo non entra mai nella proposta.

## Raggio d'azione

Il raggio d'azione R è la distanza a cui l'abbassamento si annulla. GeoTheis NX lo ricava, in ordine di preferenza:

1. dalla **retta di Thiem** sugli abbassamenti stabilizzati dei piezometri (s = 0);
2. dal **raggio transitorio** di Cooper-Jacob a fine pompaggio, se S è noto:

$$
R(t) = 1{,}5\sqrt{\frac{T\,t}{S}} = \sqrt{\frac{2{,}25\,T\,t}{S}}
$$

3. dalla retta di Thiem in distanza sui gradini (indicativo).

R(t) cresce con la durata del pompaggio: non è una proprietà dell'acquifero ma dello stato della prova. Nei **pozzi singoli** R non si
calcola: è un valore **presunto** che indichi tu.

## Pozzi singoli

Quando c'è solo il pozzo, i **pozzi singoli** usano la coppia critica (Q~c~, s~c~) come se fosse un regime stazionario, con un raggio
d'azione presunto R. La coppia viene dalla prova a gradini o, senza gradini, dalla **portata critica nota** indicata nella scheda
[Prova](prove.md). I risultati sono **stime indicative**: non sostituiscono una prova con piezometri. Le falde semiconfinate non sono
trattate.

### Pozzo completo (Celico)

$$
\text{falda confinata (Thiem): } T = \frac{Q\,\ln(R/r_w)}{2\pi\,s}, \quad K = \frac{T}{b}
\qquad
\text{falda libera (Dupuit): } K = \frac{Q\,\ln(R/r_w)}{\pi\,(H_1^2 - H_2^2)}, \quad T = K\,H_1
$$

con H~2~ = H~1~ − s.

### Pozzo incompleto (pozzo parzialmente penetrante)

Se il filtro attraversa solo una parte dell'acquifero, le linee di flusso convergono anche in verticale verso il filtro e
l'abbassamento nel pozzo è maggiore di quello di un pozzo completo. Le formule correggono la geometria; L è la lunghezza del filtro.

**Falda libera** (Chiesa), con a la distanza fra il fondo del filtro e il substrato:

$$
K = \frac{Q\,\ln(R/r_w)}{\pi\left[(H_1 - a)^2 - (H_2 - a)^2\right]}\cdot\frac{1}{1 + (0{,}3 + 10\,r_w/H_1)\,\sin(1{,}8\,a/H_1)}, \qquad T = K\,H_1
$$

**Falda confinata** (Chiesa), secondo la posizione del filtro (D distanza dal tetto all'inizio del filtro):

- tipo A, filtro staccato dal tetto che non arriva al substrato: T = Q/(2π·s)·[ln(R/(2b)) + (b/L)·ln(2L/r~w~)];
- tipo B, filtro attaccato al tetto, più corto dello spessore, e tipo C, filtro staccato dal tetto che arriva al substrato:
  T = Q/(2π·s)·[ln(R/r~w~) + ξ/2], con ξ dalla tabella di Chiesa in funzione di b/r~w~ e L/b;
- K = T/b.

In falda confinata il programma calcola anche le formule specifiche (K da cui T = K·b, oppure T da cui K = T/b):

| Metodo | Formula |
|---|---|
| Kozeny (1933) | K = Q/(2π·s·L)·ln(R/r~w~) / [1 + 7·√(r~w~/(2L))·cos(π·L/(2b))] |
| Spessore infinito (Babushkin) | K = Q/(2π·s·L)·ln(2L/r~w~) |
| Halek | K = Q/(2π·s·L)·[ln(4(L/r~w~)/(L/R + √(1 + L²/R²))) + 1 − (R/L)(1 − √(1 + L²/R²))] |
| Zangar | K = Q/(2π·s·L)·ln(L/r~w~) |
| Muskat | T = Q/(2π·s)·[(b/2L)·(2·ln(4b/r~w~) − ln Γ) − ln(4b/R)] |
| Girinski | K = Q/(2π·s·L)·ln(1,6·L/r~w~), solo con L/r~w~ ≤ 5 |
| «L/b − L/2r» | T = Q/(2π·s)·ln((2/L)·(L/2r~w~) + 0,2/b) |

!!! warning "Attenzione"
    Quattro formule sono segnate **da verificare** sul testo di riferimento e restano come nel programma desktop: Muskat (valore di
    ln Γ), Girinski (il limite L/r~w~ ≤ 5 la esclude per qualunque filtro reale), «L/b − L/2r» (l'argomento del logaritmo non è
    adimensionale, quindi T dipende dall'unità di misura) e il termine ξ/2 dei tipi B e C. Usale solo come confronto.

## Cono di depressione

Il cono disegnato nella sezione del pozzo usa i valori di progetto in uso:

- con T, S e la durata del pompaggio, la curva di **Theis** (di **Hantush** se il valore viene da Hantush) a fine pompaggio, da r~w~ a
  R(t);
- altrimenti **Thiem** (falda confinata) o **Dupuit** (falda libera) fino al raggio d'azione R di progetto.

## Validità dei risultati

- Theis e Cooper-Jacob presuppongono la falda confinata. In falda libera valgono finché l'abbassamento è piccolo rispetto allo
  spessore saturo: il programma non applica la correzione di Jacob s′ = s − s²/(2H) né il modello di Neuman per il drenaggio
  ritardato.
- Hantush non considera l'immagazzinamento dello strato semipermeabile.
- Non sono modellati: immagazzinamento nel pozzo e skin, limiti alimentanti o impermeabili, anisotropia, portate variabili diverse
  dai gradini, interferenza di più pozzi.

Il riepilogo dei limiti è in [Risultati → Limiti](risultati.md#limiti); i controlli sul codice di calcolo sono in
[Validazione](validazione.md).

## Bibliografia

- Theis C.V. (1935). *The relation between the lowering of the piezometric surface and the rate and duration of discharge of a well
  using ground-water storage*. Transactions of the American Geophysical Union, 16(2), 519–524.
- Cooper H.H., Jacob C.E. (1946). *A generalized graphical method for evaluating formation constants and summarizing well-field
  history*. Transactions of the American Geophysical Union, 27(4), 526–534.
- Jacob C.E. (1947). *Drawdown test to determine effective radius of artesian well*. Transactions ASCE, 112, 1047–1070.
- Hantush M.S., Jacob C.E. (1955). *Non-steady radial flow in an infinite leaky aquifer*. Transactions of the American Geophysical
  Union, 36(1), 95–100.
- Hantush M.S. (1956). *Analysis of data from pumping tests in leaky aquifers*. Transactions of the American Geophysical Union, 37(6),
  702–714.
- Hantush M.S. (1964). *Hydraulics of wells*. In: Advances in Hydroscience, vol. 1, Academic Press.
- Rorabaugh M.I. (1953). *Graphical and theoretical analysis of step-drawdown test of artesian well*. Proceedings ASCE, 79, separate 362.
- Walton W.C. (1962). *Selected analytical methods for well and aquifer evaluation*. Illinois State Water Survey, Bulletin 49.
- Thiem G. (1906). *Hydrologische Methoden*. Leipzig, J.M. Gebhardt.
- Dupuit J. (1863). *Études théoriques et pratiques sur le mouvement des eaux dans les canaux découverts et à travers les terrains
  perméables*. 2ª ed., Paris, Dunod.
- Kozeny J. (1933). *Theorie und Berechnung der Brunnen*. Wasserkraft und Wasserwirtschaft, 28.
- Kruseman G.P., de Ridder N.A. (1994). *Analysis and Evaluation of Pumping Test Data*. 2ª ed., ILRI Publication 47, Wageningen.
- Chiesa G. *Idraulica delle acque di falda*. Palermo, Flaccovio.
- Celico P. *Prospezioni idrogeologiche*. Napoli, Liguori.
- Abramowitz M., Stegun I.A. (1964). *Handbook of Mathematical Functions*. National Bureau of Standards, Applied Mathematics Series 55.
- Marquardt D.W. (1963). *An algorithm for least-squares estimation of nonlinear parameters*. Journal of the SIAM, 11(2), 431–441.
- Moré J.J. (1978). *The Levenberg-Marquardt algorithm: implementation and theory*. Lecture Notes in Mathematics 630, Springer.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20GeoTheis%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/geotheis/docs/it/teoria.md).*
