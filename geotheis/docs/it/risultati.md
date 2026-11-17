# Risultati

La scheda **Risultati** interpreta la prova. Il programma guarda quali dati ci sono nel progetto (prova a gradini, prova a portata
costante, risalita, piezometri, abbassamenti stabilizzati), calcola **tutti** i metodi che quei dati consentono, li mette a
confronto e ti propone il **valore di progetto** di trasmissività (T), permeabilità (K), coefficiente di immagazzinamento (S) e
raggio d'azione (R), più la **portata concedibile**. Ogni proposta è motivata e resta una proposta finché non la confermi.

La scheda serve dopo aver inserito il pozzo e almeno una prova. Se non hai la prova a gradini ma conosci la portata critica del
pozzo (da prove in aree vicine o dal collaudo), puoi indicarla nella scheda **Prova**, riquadro *Portata critica nota*: con la
geometria del pozzo basta per i metodi dei **pozzi singoli**, che danno T e K indicativi. Non devi lanciare un calcolo: i risultati si aggiornano da soli a
ogni modifica dei dati o delle scelte, e consultarli non consuma crediti.

## Com'è fatta la scheda

Dall'alto in basso:

1. **Risultati della prova**: i dati disponibili (in pastiglie), il *Riassunto del calcolo, per esteso*, gli avvisi generali e due
   colonne: **Metodi calcolati** (con l'affidabilità e il segno *proposto*) e **Non applicabili ai dati** (con il motivo). In alto a
   destra scegli l'unità di T e K: m²/s oppure **al giorno** (m²/g, m/g).
2. **Valore di progetto** e **Portata concedibile**, affiancati, ognuno con lo stato *da confermare* o *confermato/confermata*.
3. **Confronto fra i metodi**: la tabella di T, K, S, R per metodo, con gli scarti oltre soglia evidenziati.
4. **Metodi, parametri e grafici**: una linguetta per ogni metodo calcolato, con valori, avvisi, grafici e scelte.

Ogni metodo porta un giudizio di affidabilità:

| Pastiglia | Significato |
|---|---|
| **affidabile** | il metodo si applica ai dati e il risultato li descrive bene |
| **indicativo** | il risultato ha un'ipotesi debole (gradini non a regime, un solo piezometro, curva lontana dai dati…): leggilo come stima |
| **non affidabile** | il risultato non va usato (fitting non arrivato a convergenza, S dal pozzo, S > 1…) |
| **da verificare** | formula del programma desktop non ancora verificata sul testo di riferimento |

Il nome di un metodo, nelle colonne e nella tabella del confronto, è un collegamento: porta alla sua linguetta.

## Valore di progetto

Il riquadro dice da quale metodo vengono i valori in uso (*Il programma propone:* oppure *In uso i valori confermati:*), mostra T, K,
S e R e, finché sono proposti, la **motivazione**: perché quel metodo, se concorda con il secondo metodo disponibile, da dove vengono S
e R.

- **Conferma la proposta** conferma insieme T, K, S, R **e** la portata concedibile proposta.
- **Usa un altro metodo…** (menu) prende T, K e S dal metodo che scegli; lo stesso fa **Usa per il progetto** nella linguetta di un metodo.
- **Torna alla proposta** toglie le conferme: tornano in uso i valori proposti.

Se hai confermato e nel frattempo i dati cambiano, il riquadro ti avvisa: *Con i dati attuali il programma proporrebbe…*. I valori
in uso alimentano la relazione e il cono di depressione.

Di norma il programma preferisce i metodi transitori sui piezometri (in falda semiconfinata Hantush, altrimenti Theis, poi
Cooper-Jacob) ai metodi di regime e a quelli della prova a gradini, come indicato da Kruseman & de Ridder (1994): dal solo pozzo di
emungimento si ricava T, ma non S.

## Portata concedibile

Il riquadro mostra in grande la portata proposta (o quella confermata) e sotto: **Qc** (portata critica, in rosso; *Qc proposta* se
non l'hai ancora scelta), **Qott** (portata ottimale, in verde), **Q max provata** e **s previsto**, l'abbassamento nel pozzo alla
portata proposta. Segue la motivazione ed eventuali avvisi sul livello dinamico.

Con la prova a gradini la regola è quella del programma desktop: la portata concedibile è la **portata ottimale Q~ott~ = 0,9·Q~c~**,
mai oltre la portata massima provata (oltre, la curva caratteristica è un'estrapolazione). La proposta rispetta anche i vincoli sul
livello dinamico: se 0,9·Q~c~ porterebbe il livello sotto il tetto della falda in pressione o troppo vicino all'aspirazione della
pompa, il programma propone la portata che li rispetta, ricavata dalla curva caratteristica. Senza prova a gradini la portata critica
non si determina e si propone la portata della prova a portata costante, l'unica di cui si conosce il comportamento del pozzo.
Senza nessuna prova, con la **portata critica nota** indicata nella scheda Prova, si propone 0,9·Q~c~ di quella portata, e la
motivazione dice che Q~c~ è indicata da te e non ricavata da una prova: è un valore da confermare con una prova.

Comandi (portate in l/s):

- **Portata di esercizio** + **Conferma**: conferma il valore scritto; **Conferma la proposta** conferma quello del programma.
- **Portata critica Qc** + **Imposta**, oppure **Sul grafico** e un clic sulla curva caratteristica alla portata critica (Esc per
  annullare). **Togli** rimuove la scelta e torna la proposta. Compaiono solo se c'è la prova a gradini.

## Confronto fra i metodi

La tabella riporta per ogni metodo calcolato la **media** di T, K, S e R e l'affidabilità; la riga del metodo proposto è evidenziata.
**Mostra anche le singole serie** aggiunge una riga per piezometro (o pozzo, o gradino). Una cella colorata segnala uno *scarto oltre
la soglia rispetto a un altro metodo*; sotto la tabella, **Scarti da verificare** spiega ogni scarto con il controllo che conviene fare.

Lo scarto fra due valori è

$$
\text{scarto} = \frac{\max(a, b)}{\min(a, b)} - 1
$$

e le soglie di avviso sono **30 %** per T e K, **100 %** per S e R (S e R si stimano per ordine di grandezza).

!!! tip "Suggerimento"
    Uno scarto oltre soglia non si risolve facendo la media: dice che almeno un metodo è fuori dalle sue ipotesi. Apri le linguette
    dei due metodi, guarda i grafici e scegli quello i cui punti seguono la curva o la retta.

## Metodi, parametri e grafici

Ogni metodo calcolato ha una linguetta (il bersaglio indica quello in uso). Dentro trovi il riferimento bibliografico, l'affidabilità,
T, K, S, R, gli avvisi del metodo, i grafici, le scelte per serie e, chiuso in *Parametri, serie e note del metodo*, l'elenco
completo dei parametri (con l'intervallo di confidenza al 95 % passando col mouse sul valore), la tabella per serie e le note.

| Grafico | Metodo | Assi |
|---|---|---|
| Curva caratteristica s–Q | curva caratteristica | Q (l/s), s (m) verso il basso; Q~c~ in rosso, Q~ott~ in verde, zona oltre la portata critica |
| Abbassamento specifico s/Q–Q | curva caratteristica | Q (l/s), s/Q (m per l/s), retta s/Q = B + C·Q |
| Curva di Rorabaugh | Rorabaugh | s = BQ + CQⁿ a confronto con n = 2 |
| Cooper-Jacob · *serie* | Cooper-Jacob | t (min) in scala logaritmica, s (m); retta, tratto usato |
| Risalita · *serie* | risalita | t/t′ in scala logaritmica, s′ (m) |
| Theis · *serie*, Hantush · *serie* | curve tipo | t (min) e s (m) in scala bilogaritmica; curva del fitting e, se c'è, curva del punto di coincidenza tratteggiata |
| Distanza-abbassamento, Dupuit-Thiem, gradini in distanza | metodi in distanza | r (m) in scala logaritmica, s (m) verso il basso, R |

Ogni grafico si scarica in PNG con il pulsante accanto al titolo.

## Come si usa, passo passo

1. Apri **Risultati** dopo aver inserito il pozzo e le prove. Leggi le due colonne: se un metodo che ti aspetti è fra i *Non
   applicabili*, il motivo ti dice quale dato manca.
2. Guarda il **Confronto**. Se ci sono *Scarti da verificare*, apri le linguette dei metodi coinvolti.
3. Nei grafici controlla che i punti usati (pieni) seguano la retta o la curva. Escludi le letture anomale con un clic, o restringi
   l'intervallo di Cooper-Jacob.
4. Se lavori con la prova a gradini, scegli la **portata critica** sulla curva caratteristica.
5. Rileggi le motivazioni e premi **Conferma la proposta**, oppure scegli un altro metodo o scrivi la portata di esercizio.
6. Passa alla relazione: riporta i valori in uso e le scelte fatte.

## Scelte sui grafici

Le scelte non toccano le letture del progetto: cambiano solo l'interpretazione e si salvano nel file. Sotto i grafici, per ogni serie,
un riquadro *Punti, intervalli e ritocco* mostra i punti usati sul totale, quanti ne hai esclusi a mano e il criterio con cui il
programma ha scelto i punti.

### Escludere un punto

Un clic su un punto lo esclude dal calcolo (diventa vuoto); un clic su un punto escluso a mano lo rimette. **Rimetti tutti** annulla le
esclusioni della serie. Vale per Cooper-Jacob, risalita, Theis, Hantush e, sulla curva caratteristica, per i gradini: un gradino escluso
esce da B, C e dalla coppia critica, ma resta numerato.

### Intervallo di Cooper-Jacob

La retta di Cooper-Jacob vale solo per tempi abbastanza lunghi (u < 0,05). Il programma propone da solo il tratto finale rettilineo;
puoi sostituirlo con un intervallo tuo:

- scrivi **Da t** e **a t** in minuti e premi **Applica l'intervallo**; per la risalita i campi sono **Da t′** e **a t′**;
- oppure **Sul grafico**: clicca l'inizio e poi la fine dell'intervallo (Esc per annullare);
- **Torna al tratto proposto** toglie il tuo intervallo.

Lo stesso intervallo si può impostare sulle serie di Theis e Hantush, per limitare il fitting a un tratto della prova. Un punto vuoto
che non hai escluso tu è fuori dal tratto usato: per riprenderlo cambia l'intervallo.

### Ritocco della curva tipo (Theis e Hantush)

Il fitting automatico trova T e S (e r/B per Hantush) che fanno seguire alla curva tipo tutte le letture del piezometro. Se vuoi
imporre un valore, ad esempio S da un'altra prova:

1. nella riga **Ritocco della curva tipo** della serie, i campi **T (m²/s)** e **S** partono dai valori del fitting;
2. scrivi i valori da tenere fissi e **lascia vuoto** quello che il programma deve adattare ai dati;
3. premi **Ritocca**: la curva del ritocco compare tratteggiata accanto a quella del fitting, e nell'elenco dei metodi compare
   *Theis (punto di coincidenza)* o *Hantush (punto di coincidenza)* con il suo scarto dai dati.

**Torna al fitting** toglie il ritocco. Il ritocco non diventa il valore di progetto da solo: se vuoi usarlo, premi **Usa per il
progetto** nella sua linguetta.

## Cono di depressione

Sotto il valore di progetto una riga riassume il cono di depressione che la scheda di disegno traccia nella sezione del pozzo: con
quali valori (proposti o confermati, e di quale metodo), a quale portata e fino a quale raggio. La portata del cono è quella di
esercizio in uso (confermata, o la concedibile proposta); senza, quella della prova a portata costante.

- Se si conoscono T, S e la durata del pompaggio: curva di **Theis** (di **Hantush** se il valore viene da Hantush con B) al tempo di
  fine pompaggio, fino al raggio d'azione transitorio R(t).
- Altrimenti: **Thiem** (falda confinata) o **Dupuit** (falda libera) fino al raggio d'azione R di progetto.

## Basi teoriche

Notazione: Q portata, s abbassamento, r distanza dal pozzo, t tempo dall'inizio del pompaggio, t′ tempo dall'arresto, T
trasmissività, S coefficiente di immagazzinamento, K conducibilità idraulica, b spessore della falda confinata, H~1~ spessore saturo
della falda libera, r~w~ raggio del pozzo, R raggio d'azione. Il calcolo è in unità SI (m, s, m³/s, m²/s, m/s); l/s, minuti e valori
al giorno sono solo presentazione.

**Theis (1935).** Falda confinata, omogenea, isotropa, di estensione illimitata; pozzo completo; portata costante.

$$
s = \frac{Q}{4\pi T}\,W(u), \qquad u = \frac{r^2 S}{4 T t}, \qquad W(u) = \int_u^\infty \frac{e^{-y}}{y}\,dy
$$

**Cooper-Jacob (1946).** Approssimazione logaritmica di Theis, valida per u < 0,05. Dalla retta s – log~10~ t, con Δs l'abbassamento
per ciclo logaritmico e t~0~ il tempo a cui la retta dà s = 0:

$$
s = \frac{2{,}303\,Q}{4\pi T}\,\log_{10}\frac{2{,}25\,T\,t}{r^2 S}, \qquad T = \frac{\ln 10\; Q}{4\pi\,\Delta s}, \qquad S = \frac{2{,}25\,T\,t_0}{r^2}
$$

**Risalita (Theis 1935).** Abbassamento residuo s′ contro log~10~(t/t′), con t = t~arresto~ + t′:

$$
s' = \frac{2{,}303\,Q}{4\pi T}\,\log_{10}\frac{t}{t'}, \qquad T = \frac{\ln 10\; Q}{4\pi\,\Delta s'}
$$

**Hantush-Jacob (1955).** Falda semiconfinata con strato semipermeabile senza immagazzinamento; B fattore di drenanza, c resistenza
idraulica del semipermeabile:

$$
s = \frac{Q}{4\pi T}\,W\!\left(u, \tfrac{r}{B}\right), \qquad W\!\left(u, \tfrac{r}{B}\right) = \int_u^\infty \frac{1}{y}\exp\!\left(-y - \frac{(r/B)^2}{4y}\right)dy, \qquad B = \sqrt{T c}
$$

**Fitting delle curve tipo.** È il confronto in scala bilogaritmica fra dati e curva tipo, fatto ai minimi quadrati (Levenberg-Marquardt:
Marquardt 1963, Moré 1978) sui logaritmi degli abbassamenti. Lo scarto tipico fra dati e curva è 10^RMSE − 1, con RMSE sui logaritmi in
base 10. Con il punto di coincidenza (W, u, s, t/r²): T = Q·W/(4π·s), S = 4·T·u·(t/r²); per Hantush in più B = r/(r/B), c = B²/T.

**Dupuit-Thiem, regime stazionario (Dupuit 1863; Thiem 1906).** Retta degli abbassamenti stabilizzati dei piezometri contro log~10~ r;
R è la distanza a cui la retta dà s = 0.

$$
\text{falda confinata: } s_1 - s_2 = \frac{Q}{2\pi T}\ln\frac{r_2}{r_1}, \quad T = \frac{\ln 10\; Q}{2\pi\,\Delta s}
\qquad
\text{falda libera: } H_1^2 - h^2 = \frac{Q}{\pi K}\ln\frac{R}{r}, \quad K = \frac{\ln 10\; Q}{\pi\,\Delta Z}
$$

con Z = s·(2H~1~ − s) e T = K·H~1~.

**Distanza-abbassamento.** Stessa retta s – log~10~ r, sugli abbassamenti dei piezometri allo stesso tempo t: T = ln10·Q/(2π·Δs), r~0~
dove s = 0, S = 2,25·T·t/r~0~².

**Curva caratteristica (Jacob 1947).** Perdite lineari dell'acquifero (BQ) e quadratiche del pozzo (CQ²), dalla retta di s/Q contro Q
sui gradini; efficienza del pozzo E:

$$
s = B\,Q + C\,Q^2, \qquad \frac{s}{Q} = B + C\,Q, \qquad E = \frac{B\,Q}{B\,Q + C\,Q^2}
$$

La portata critica Q~c~ si sceglie sulla curva; se manca, il programma propone Q = B/C, dove le perdite del pozzo eguagliano quelle
dell'acquifero (E = 50 %). Portata ottimale Q~ott~ = 0,9·Q~c~.

**Rorabaugh (1953).** Esponente libero: s = B·Q + C·Qⁿ, stimato ai minimi quadrati sugli abbassamenti; con n = 2 si ritrova Jacob.

**Condizioni del pozzo (Walton 1962).** Classi sul coefficiente C espresso in min²/m⁵: fino a 0,5 correttamente progettato e
sviluppato; fino a 1 deterioramento moderato dovuto a intasamento; fino a 4 deterioramento grave o intasamento; oltre, difficoltà a
riportare il pozzo nelle condizioni originali.

**Raggio d'azione transitorio.** Dalla retta di Cooper-Jacob con s = 0:

$$
R(t) = 1{,}5\sqrt{\frac{T\,t}{S}} = \sqrt{\frac{2{,}25\,T\,t}{S}}
$$

**Pozzi singoli.** Usano la coppia critica (Q~c~, s~c~) della prova a gradini come regime stazionario e un raggio d'azione presunto
(formule di Dupuit-Thiem e Celico per il pozzo completo; Chiesa, Celico, Muskat, Kozeny e altre per il pozzo incompleto): sono stime
indicative.

Il dettaglio di algoritmi, casi di prova e confronti con il programma desktop è nel documento di [validazione](validazione.md).

### Bibliografia

- Theis C.V. (1935). *The relation between the lowering of the piezometric surface and the rate and duration of discharge of a well
  using ground-water storage*. Transactions of the American Geophysical Union, 16(2), 519–524.
- Cooper H.H., Jacob C.E. (1946). *A generalized graphical method for evaluating formation constants and summarizing well-field
  history*. Transactions of the American Geophysical Union, 27(4), 526–534.
- Jacob C.E. (1947). *Drawdown test to determine effective radius of artesian well*. Transactions ASCE, 112, 1047–1070.
- Hantush M.S., Jacob C.E. (1955). *Non-steady radial flow in an infinite leaky aquifer*. Transactions of the American Geophysical
  Union, 36(1), 95–100.
- Hantush M.S. (1956). *Analysis of data from pumping tests in leaky aquifers*. Transactions of the American Geophysical Union, 37(6),
  702–714.
- Rorabaugh M.I. (1953). *Graphical and theoretical analysis of step-drawdown test of artesian well*. Proceedings ASCE, 79, separate 362.
- Walton W.C. (1962). *Selected analytical methods for well and aquifer evaluation*. Illinois State Water Survey, Bulletin 49.
- Thiem G. (1906). *Hydrologische Methoden*. Leipzig, J.M. Gebhardt.
- Dupuit J. (1863). *Études théoriques et pratiques sur le mouvement des eaux dans les canaux découverts et à travers les terrains
  perméables*. 2ª ed., Paris, Dunod.
- Kruseman G.P., de Ridder N.A. (1994). *Analysis and Evaluation of Pumping Test Data*. 2ª ed., ILRI Publication 47, Wageningen.
- Chiesa G. *Idraulica delle acque di falda*. Palermo, Flaccovio.
- Celico P. *Prospezioni idrogeologiche*. Napoli, Liguori.
- Marquardt D.W. (1963). *An algorithm for least-squares estimation of nonlinear parameters*. Journal of the SIAM, 11(2), 431–441.
- Moré J.J. (1978). *The Levenberg-Marquardt algorithm: implementation and theory*. Lecture Notes in Mathematics 630, Springer.

## Esempio

!!! example "Esempio CELICO"
    Apri l'esempio **CELICO** dall'elenco degli esempi: pozzo completo in falda confinata (r~w~ = 0,5 m, b = 7 m, H~1~ = 9 m), 3
    gradini a 766,8 / 939,6 / 1 054,8 m³/h con s = 3,74 / 5,12 / 6,13 m, piezometri P1 a 23,5 m e P2 a 42,4 m, prova a portata costante
    di 150 m³/h per 30 000 s con 18 letture di pompaggio e 16 di risalita, abbassamenti stabilizzati, portata critica scelta nel file
    Q~c~ = 1 099,56 m³/h.

    - Il programma calcola 12 metodi e propone **Theis (fitting automatico)**, che concorda con Cooper-Jacob.
    - Fitting di Theis: T = 4,34·10⁻³ m²/s e S = 7,03·10⁻³ su P1; T = 1,08·10⁻² m²/s e S = 5,40·10⁻³ su P2. Cooper-Jacob:
      4,231·10⁻³ m²/s e 7,32·10⁻³ su P1, 1,058·10⁻² m²/s e 5,61·10⁻³ su P2.
    - R di progetto = 76,5 m, dalla retta di Thiem sui piezometri a regime.
    - Curva caratteristica: B = 2,3894·10⁻³ h/m², C = 3,2486·10⁻⁶ h²/m⁵, efficienza 42,64 % alla portata ottimale.
    - Portata concedibile: 0,9·Q~c~ (circa 275 l/s) porterebbe il livello dinamico sotto il tetto della falda confinata, quindi il
      programma propone la portata più bassa che tiene il livello sul tetto.
    - Il confronto segnala che i metodi della prova a gradini (T ≈ 5·10⁻² m²/s) sono lontani da quelli della portata costante
      (4–11·10⁻³ m²/s).

    I dati di CELICO sono costruiti (le letture di P2 sono quelle di P1 × 0,4): servono a provare il calcolo, non descrivono un
    acquifero reale.

## Limiti

- **Theis e Cooper-Jacob** presuppongono falda confinata, omogenea, isotropa e illimitata, pozzo completo di raggio trascurabile,
  portata costante. In falda libera e con pozzo incompleto il programma calcola comunque, con un avviso, ma **senza** la correzione di
  Jacob s′ = s − s²/(2H) e senza il modello di Neuman: il risultato vale per abbassamenti piccoli rispetto allo spessore saturo.
- **Hantush** si calcola solo in falda semiconfinata e non considera l'immagazzinamento dello strato semipermeabile.
- **S dal pozzo di emungimento non è affidabile** (perdite di carico, raggio effettivo incerto): per S servono le letture in un
  piezometro.
- I metodi della **prova a gradini** sui piezometri e i **pozzi singoli** sono indicativi: usano abbassamenti a fine gradino, non a
  regime, o un raggio d'azione presunto. Cinque formule dei pozzi incompleti (Halek, Muskat, Girinski, «L/b − L/2r», tipi B e C di Chiesa)
  sono segnate *da verificare*.
- Non sono modellati: immagazzinamento nel pozzo e skin, derivata dell'abbassamento, drenaggio ritardato in falda libera, limiti
  alimentanti o impermeabili (pozzi immagine), anisotropia, portate variabili diverse dai gradini, interferenza di più pozzi.
- Le proposte sono un aiuto alla decisione: il valore di progetto lo sceglie e lo firma il progettista.

## Domande frequenti

**Perché un metodo è fra i «Non applicabili»?**
Mancano i dati che richiede: il motivo è scritto accanto al nome (ad esempio letture nei piezometri, abbassamenti stabilizzati, almeno
due piezometri a distanze diverse, falda semiconfinata per Hantush).

**Theis e Cooper-Jacob danno valori diversi: quale uso?**
Se lo scarto è entro il 30 % la scelta è indifferente e il programma propone Theis. Oltre, controlla nel grafico di Cooper-Jacob che
il tratto usato sia davvero rettilineo e a tempi lunghi.

**Ho escluso un punto per errore.**
Un secondo clic sul punto lo rimette; **Rimetti tutti** annulla tutte le esclusioni della serie.

**Il ritocco non cambia il valore di progetto.**
È voluto: il ritocco compare come metodo a sé (*punto di coincidenza*). Per usarlo premi **Usa per il progetto** nella sua linguetta.

**Perché la portata concedibile è minore di 0,9·Q~c~?**
Perché 0,9·Q~c~ supera la portata massima provata, oppure porterebbe il livello dinamico sotto il tetto della falda in pressione o
sotto l'aspirazione della pompa. La motivazione dice quale dei casi.

**Posso vedere T in m²/giorno?**
Sì: in alto a destra nella scheda, **T e K in** → **al giorno**. Cambia solo la presentazione; i campi del ritocco restano in m²/s.

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20GeoTheis%20NX) o apri una [Pull Request](https://github.com/EngSoft-Geostru/geostru-help-nx/edit/main/geotheis/docs/it/risultati.md).*
