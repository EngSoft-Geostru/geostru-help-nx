# Classificazioni geomeccaniche — panoramica e parametri comuni

Nella progettazione geotecnica in roccia — sia per la stabilità di un versante sia per un'opera in sotterraneo — raramente si dispone di informazioni dettagliate sulle caratteristiche di resistenza e deformabilità dell'ammasso. Le **classificazioni geomeccaniche** sono metodi empirici che, a partire dal rilievo geostrutturale, restituiscono un indice di qualità dell'ammasso e i parametri caratteristici (coesione, angolo d'attrito, modulo di deformazione) necessari al calcolo.

Rock Mechanics NX implementa sei classificazioni, tutte alimentate dallo **stesso rilievo di discontinuità** (vedi [Workflow](workflow.md)):

| Classificazione | Indice | Campo d'applicazione tipico | Pagina |
|---|---|---|---|
| Barton (1974, rev. 2002) | Q | Opere in sotterraneo, caratterizzazione generale | [Barton](barton.md) |
| Bieniawski (1976) + Romana (1985) | RMR · SMR | Gallerie, fondazioni, **versanti** (SMR) | [Bieniawski & Romana](rmr-romana.md) |
| Jašarević & Kovačević (1996) | n → RMR | Ammassi carbonatici | [Jašarević](jasarevic.md) |
| Sen & Sadagah (2003) | RMR continuo | Versione semplificata di RMR | [Sen](sen.md) |
| Robertson (1988) | SRMR | **Solo versanti** in roccia tenera (RMR < 40) | [Robertson](robertson.md) |
| Singh & Göel (1999) | N → RMR · Q | Gallerie | [Singh & Goel](singh-goel.md) |

Molti metodi condividono gli stessi parametri di input. Per evitare ripetizioni, le definizioni e le tabelle comuni sono raccolte qui: le pagine dei singoli metodi vi rimandano.

---

## Resistenza a compressione uniassiale Su { #resistenza-a-compressione-uniassiale-su }

Il parametro `A1` di tutti i metodi derivati da RMR si ricava dalla **resistenza a compressione uniassiale** $S_u$ della roccia intatta. La si può determinare in tre modi.

### Prova Point Load Test

Portatile e di campo, fornisce l'**indice di carico puntuale** $I_s$, correlato a $S_u$ dalla:

$$ S_u = K \cdot I_s $$

L'ISRM consiglia $K = 24$, ma nella pratica il valore è largamente variabile. Palmström suggerisce di legare $K$ a $I_s$:

| $I_s$ (MPa) | K |
|---|---|
| < 3,5 | 14 |
| 3,5 – 6,0 | 16 |
| 6,0 – 10 | 20 |
| > 10 | 25 |

### Prova sclerometrica (martello di Schmidt)

Prova non distruttiva che misura la *durezza di rimbalzo* della roccia. Dall'indice di rimbalzo $R$ si ricava $S_u$ con la relazione di Irfan e Dearman (1978):

$$ S_u = 0{,}775 \cdot R + 21{,}3 $$

### Standard ISRM (stima speditiva)

In fase preliminare, in assenza di prove, $S_u$ si stima dalla risposta della roccia alla percussione col martello da geologo:

| Risposta della roccia | $S_u$ |
|---|---|
| Si incide con l'unghia o si sbriciola con le mani | 0,25 – 1 MPa |
| Si sbriciola sotto i colpi della punta; lastre sottili si rompono a mano | 1 – 5 MPa |
| La punta lascia deboli buchi; lastre sottili si rompono con forti pressioni | 5 – 25 MPa |
| La roccia si frattura con un colpo | 25 – 50 MPa |
| Si frattura dopo due-tre colpi | 50 – 100 MPa |
| Si scheggia solamente | > 200 MPa |

!!! tip "Quale metodo usare"
    Se disponi di prove Point Load o sclerometriche, conviene ricavare `A1` dalle equazioni dei grafici di Bieniawski (riportate nella pagina di ciascun metodo) anziché dalle tabelle a gradini: il risultato è continuo e meno soggettivo.

---

## RQD — Rock Quality Designation { #rqd-rock-quality-designation }

Il **Rock Quality Designation** misura il grado di fratturazione dell'ammasso. Da sondaggio si calcola come percentuale di recupero riferita agli spezzoni di carota di lunghezza $\geq 100$ mm:

$$ RQD = 100 \cdot \frac{L_c}{L_t} $$

dove $L_c$ è la somma delle lunghezze degli spezzoni di carota > 100 mm e $L_t$ la lunghezza totale del tratto misurato.

In **mancanza di carote di sondaggio**, RQD si ricava dal rilievo delle discontinuità con la relazione di Palmström (1982):

$$ RQD = 115 - 3{,}3 \cdot J_v $$

dove $J_v$ è il numero di giunti per metro cubo di roccia (volumetric joint count).

In forma alternativa, dalla formula di Priest e Hudson (1981):

$$ RQD = 100 \cdot e^{-0{,}1\,\lambda} \cdot (0{,}1\,\lambda + 1) $$

con $\lambda$ numero medio di giunti per metro lineare.

!!! note "Valore minimo"
    Nelle classificazioni di Barton e Singh & Goel, se $RQD < 10$ si assume comunque $RQD = 10$.

---

## Spaziatura delle discontinuità { #spaziatura-delle-discontinuita }

La **spaziatura media** $s$ è la distanza media fra due discontinuità adiacenti della stessa famiglia. Determina il parametro `A3` di RMR (con equazioni specifiche per metodo) ed entra nelle tabelle di Robertson e Jašarević.

---

## Parametri della classificazione di Barton (Q)

I quattro parametri che seguono ($J_n$, $J_r$, $J_a$, $J_w$) e il fattore SRF sono comuni a **Barton**, **Singh & Goel** e, in forma derivata, alla utility [Crollo per evento sismico](utility.md). Le pagine relative rimandano alle tabelle qui sotto.

### Parametro J~n~ (Joint Set Number) { #jn }

Dipende dal numero di famiglie di giunti presenti nell'ammasso.

| Definizione | $J_n$ |
|---|---|
| Roccia massiva, nessuna o rare discontinuità | 0,5 – 1 |
| Una serie di discontinuità | 2 |
| Una serie di discontinuità + quelle random (casuali) | 3 |
| Due serie di discontinuità | 4 |
| Due serie di discontinuità + quelle random | 6 |
| Tre serie di discontinuità | 9 |
| Tre serie di discontinuità + quelle random | 12 |
| Quattro o più serie di discontinuità | 15 |
| Roccia completamente disgregata | 20 |

!!! note "Gallerie"
    In zona di imbocco $J_n$ va raddoppiato; in una zona di intersezione di due gallerie va triplicato.

### Parametro J~r~ (Joint Roughness Number) { #jr }

Dipende dalla rugosità della famiglia più sfavorevole.

| Definizione | $J_r$ |
|---|---|
| Giunti discontinui | 4 |
| Giunti scabri o irregolari, ondulati | 3 |
| Giunti lisci, ondulati | 2 |
| Giunti levigati, ondulati | 1,5 |
| Giunti scabri o irregolari, piani | 1,5 |
| Giunti lisci, piani | 1,0 |
| Giunti levigati, piani | 0,5 |
| Zone mineralizzate con minerali argillosi a riempire la discontinuità | 1,0 |
| Zone mineralizzate con sabbia, ghiaia, zone disgregate | 1,0 |

La descrizione si riferisce alle caratteristiche a piccola e media scala. Se la spaziatura media della famiglia principale supera 3 m, aumentare $J_r$ di 1. Per giunti piani e levigati con strie orientate nella direzione più sfavorevole, usare 0,5.

### Parametro J~a~ (Joint Alteration Number) { #ja }

Dipende dal grado di alterazione delle fratture, dallo spessore e dalla natura del riempimento, determinato sulla famiglia più sfavorevole.

**Giunti sostanzialmente chiusi** (apertura 1–3 mm) con pareti a contatto:

| Definizione | $J_a$ |
|---|---|
| Giunti sigillati o mineralizzati | 0,75 |
| Giunti non alterati o con lievi ossidazioni | 1 |
| Giunti leggermente alterati o con spalmature di materiale non plastico | 2 |
| Giunti con spalmature limose, frazione argillosa limitata non plastica | 3 |
| Spalmature di minerali a bassa resistenza attritiva (argille, miche, talco, grafite, clorite, gesso) | 4 |

**Giunti mediamente aperti** (< 5 mm), riempimento che mantiene il contatto fra le pareti in caso di scorrimento:

| Definizione | $J_a$ |
|---|---|
| Riempimento sabbioso | 4 |
| Riempimento argilloso non plastico, molto sovraconsolidato | 6 |
| Riempimento argilloso plastico, mediamente sovraconsolidato | 8 |
| Riempimento argilloso rigonfiante | 8 – 12 * |

**Giunti aperti** (> 5 mm), nessun contatto fra le pareti in caso di scorrimento:

| Definizione | $J_a$ |
|---|---|
| Zone o fasce di argilla limosa o sabbiosa non plastica | 5 |
| Zone o fasce di roccia disgregata | 6 |
| Zone o fasce di argilla non plastica | 6 |
| Zone o fasce di argilla plastica rigonfiante | 8 |
| Zone o fasce di argilla rigonfiante | 12 |
| Zone continue molto spesse di argilla non plastica | 10 |
| Zone continue molto spesse di argilla plastica non rigonfiante | 13 |
| Zone continue molto spesse di argilla plastica rigonfiante | 13 – 20 * |

\* Il valore dipende dalla percentuale della frazione argillosa rigonfiante e dalla possibilità che venga a contatto con l'acqua.

### Parametro J~w~ (Joint Water Number) { #jw }

Dipende dalle condizioni idrogeologiche.

| Definizione | $J_w$ |
|---|---|
| Acqua assente o scarsa, localmente < 5 l/min | 1 |
| Afflusso medio con occasionale dilavamento del riempimento | 0,66 |
| Afflusso forte o ad alta pressione in rocce compatte con discontinuità aperte senza riempimento | 0,5 |
| Venute forti o ad alta pressione con dilavamento del riempimento | 0,33 |
| Venute eccezionalmente forti subito dopo l'avanzamento, a diminuire nel tempo | 0,2 – 0,1 |
| Venute eccezionalmente forti subito dopo l'avanzamento, costanti nel tempo | 0,1 – 0,05 |

Negli ultimi quattro casi, con sistemi di drenaggio efficaci $J_w$ va riportato a 1 o 0,66. Per una caratterizzazione lontana dall'influenza dello scavo, con $RQD/J_n$ sufficientemente basso (0,5 – 25), si possono assumere i valori di $J_w$ (1,0 – 0,66 – 0,5 – 0,33) in funzione delle altezze di ricoprimento (0–5; 5–25; 25–250; > 250 m).

### Fattore SRF (Stress Reduction Factor) { #srf }

Funzione dello stato tensionale in rocce massive o del disturbo tettonico. Si veda la tabella completa nella pagina [Barton](barton.md#srf), che ne distingue i quattro contesti (zone di debolezza, ammasso competente, ammasso spingente, ammasso rigonfiante).

---

## Confronto fra le classificazioni

- **Barton (Q)** e **Singh & Goel (N)** muovono dagli stessi indici di giunto; N è Q privato dell'effetto tensionale (SRF = 1).
- **Bieniawski (RMR)** è il riferimento da cui derivano **Romana (SMR)**, **Jašarević (n)** e **Sen**, legati da correlazioni empiriche del tipo $RMR = f(\text{indice})$.
- **Romana (SMR)** e **Robertson (SRMR)** sono pensati per i **versanti**: il primo aggiunge a RMR fattori di orientamento fronte/giunto, il secondo è una scala dedicata a rocce tenere.

Per i legami fra Q e RMR la relazione di Bieniawski più usata è:

$$ RMR = 9 \cdot \ln(Q) + 44 $$

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20Rock%20Mechanics%20NX).*
