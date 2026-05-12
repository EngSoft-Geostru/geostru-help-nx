# Tiranti / chiodi

GDW supporta l'aggiunta di **tiranti** o **chiodi** attivi che agiscono sulla
faccia del muro, contribuendo alla stabilità globale ed esterna riducendo
la spinta orizzontale e aggiungendo un contributo verticale stabilizzante.

## Quando usarli

- **Tiranti pre-tesi**: ancoraggi profondi nel terreno a monte (bulbo cementato
  o a iniezione). La forza di tiro Tp è una **forza attiva** trasmessa al muro.
- **Chiodi (soil nailing)**: passivi, ma per GDW il calcolo è semplificato e
  l'effetto è trattato analogamente al tirante (forza assiale costante).

## Input

Sezione **Tiranti / Chiodi** (menu Dati → Tiranti). Click su **"Aggiungi
tirante"** per ogni livello.

| Campo | Unità | Descrizione |
|---|---|---|
| **Y** | m | Distanza dell'ancoraggio dalla testa del muro (Y crescente verso il basso) |
| **β** | ° | Inclinazione del tirante rispetto all'orizzontale (positivo = punta verso il basso) |
| **L** | m | Lunghezza totale del tirante (l_libera + l_ancoraggio) |
| **Interasse** | m | Distanza orizzontale tra tiranti adiacenti su questa fila |
| **T_p** | kN | Tiro di progetto per **singolo** tirante |

> **Nota.** Tp è la forza per tirante. La forza per metro lineare di muro
> (utilizzata nel calcolo bidimensionale) è `Tp / Interasse`.

## Modello di calcolo

L'ancoraggio è schematizzato sulla **faccia monte (interna, lato terreno)**
del muro, alla quota Y misurata dalla sommità — conformemente alla pratica
di cantiere dei "gabbioni chiodati", dove **putrelle in acciaio** o piastre
ripartiscono il tiro sul paramento di monte (faccia verso il terreno).
La barra/trefolo prosegue nel terreno a monte con inclinazione β sotto
l'orizzontale fino al bulbo di ancoraggio.

Per ogni tirante con forza per metro lineare `Tp_m = Tp / Interasse`:

$$
H = T_{p,m} \cdot \cos(\beta) \quad \text{(verso monte)}
$$

$$
V = T_{p,m} \cdot \sin(\beta) \quad \text{(verso il basso)}
$$

### Effetto sulle azioni

Con ancoraggio sulla **faccia monte (X = B_muro)** rispetto al pivot di
ribaltamento (lembo valle, X = 0):

| Grandezza | Contributo |
|---|---|
| F_x (forza orizzontale agente) | **− H** (favorevole: riduce la spinta) |
| F_y (peso/verticale stabilizzante) | **+ V** (favorevole) |
| Momento stabilizzante M_s | **+ H · (H_muro − Y) + V · B_muro** (favorevole) |
| Momento ribaltante M_r | invariato |

Il contributo `V·B_muro` deriva dal fatto che la putrella applica anche
la componente verticale alla faccia monte, generando un momento
stabilizzante rispetto al lembo valle.

### Effetto sulle verifiche

- **Ribaltamento**: M_s aumenta, FS_rib migliora
- **Scorrimento**: F_x si riduce e fy aumenta, FS_scorr migliora drasticamente
- **Capacità portante (q_lim)**: F_y aumenta → eccentricità si riduce → q_lim migliora
- **Stabilità globale Bishop**: i tiranti **non sono ancora integrati** nel modulo Bishop (TBD)

## Visualizzazione

- **Preview SVG** (Sovraccarico): ogni tirante è disegnato come linea marrone
  che parte dalla faccia valle del muro a quota Y, scende all'angolo β fino al
  bulbo (ellisse all'estremità). Pallino nero = piastra di ancoraggio.
- **Disegno sezione (server)**: stessa rappresentazione SkiaSharp, con
  etichetta `Tᵢ = Tp kN` accanto a ogni linea.
- **Lunghezza visiva troncata**: se L > 1.5 × H_muro la linea è troncata e
  marcata con due trattini `//` prima del bulbo (la L reale viene comunque
  considerata nel calcolo).

## Esempio numerico

Muro H=5 m, B_muro = 3 m, tirante con Y=1, β=15°, Interasse=1 m, Tp=100 kN:

- Tp_m = 100 / 1 = 100 kN/m
- H = 100 · cos(15°) = 96.6 kN/m
- V = 100 · sin(15°) = 25.9 kN/m
- ΔM_s = H · (H_muro − Y) + V · B_muro
- ΔM_s = 96.6 · (5 − 1) + 25.9 · 3 = 386.4 + 77.7 = **464 kNm/m**

Se senza tirante FS_scorr = 1.2 con F_x = 80 kN/m e R = 96 kN/m:

- Con tirante: F_x' = 80 − 96.6 = −16.6 kN/m (negativo → coesione/tirante
  annulla la spinta orizzontale → FS_scorr = ∞, GDW segnala "verificato")

## Tiranti e verifiche interne

**I tiranti non entrano nelle verifiche interne fila per fila.** Il loro
effetto è considerato solo nella **verifica esterna** della stabilità
complessiva del muro.

### Perché

La verifica di scorrimento del singolo giunto è una verifica **locale di
interfaccia gabbione-gabbione**: vuole misurare se l'attrito + la coesione
apparente c_g lungo quel giunto sono sufficienti a impedire lo scorrimento
di una porzione di muro sull'altra.

Il tirante:

- Non agisce **lungo** il giunto: è una forza puntuale applicata in
  corrispondenza della putrella, distinta dall'interfaccia.
- È **meccanicamente vincolato** al gabbione che attraversa (barra
  filettata, bulloni, rete): la modalità di rottura nelle vicinanze
  dell'ancoraggio non è "scorrimento sul giunto" ma rottura della
  connessione meccanica (che si verifica separatamente sul dimensionamento
  del tirante stesso, fuori da GDW).

Includere il tirante nell'equilibrio del giunto interno conduce, nei casi
di gabbione singolo sopra l'ancoraggio, a `F_x` negativo e a un "Verificato
per trazione" semanticamente fuorviante: l'attrito-coesione del giunto non
è il meccanismo che impedisce la rottura, l'ancoraggio meccanico lo è.

### Conseguenze pratiche

- **FS_rib e FS_scorr per ogni fila** sono calcolati come se i tiranti non
  ci fossero. Sono indicatori della **frizione interna** del paramento.
- La **stabilità globale** del muro con tiranti è valutata dalle FS
  esterne (FS_rib, FS_scorr, FS_q_lim) che invece **includono** il tiro
  con tutti i suoi contributi (H, V, ΔM_s = H·braccio + V·B).
- Se un giunto interno risulta non verificato **anche senza tiranti**, è
  un segnale che il muro andrebbe ridimensionato (più gabbioni, shift
  inferiore, c_g maggiore), non che basta aggiungere un altro tirante.

> **Dimensionamento del tirante stesso.** GDW non verifica la resistenza
> della barra/trefolo, della putrella, del bulbo né della connessione alla
> rete. Sono verifiche da effettuare con strumenti dedicati (Tiranti NX,
> codici locali).

## Limitazioni attuali

- **Verifica del tirante stesso** (resistenza barra, bulbo, ancoraggio)
  **non è inclusa** in GDW. Da effettuare separatamente (Tiranti NX).
- **Stabilità globale Bishop**: i tiranti non concorrono al momento
  resistente. Per analisi rigorose globali, usare un altro strumento.

## Vedi anche

- [Verifiche esterne](verifiche.md) — ribaltamento, scorrimento, q_lim
- [Verifiche interne](verifiche-interne.md) — per fila (senza tiranti per ora)
- [Bishop globale](bishop.md) — limitazioni
