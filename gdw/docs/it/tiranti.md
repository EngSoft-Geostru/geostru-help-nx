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

L'ancoraggio è schematizzato sulla **faccia valle (esterna)** del muro, alla
quota Y misurata dalla sommità. La barra/trefolo attraversa il muro e si
inflessa nel terreno a monte con inclinazione β sotto l'orizzontale fino al
bulbo di ancoraggio.

Per ogni tirante con forza per metro lineare `Tp_m = Tp / Interasse`:

$$
H = T_{p,m} \cdot \cos(\beta) \quad \text{(verso monte)}
$$

$$
V = T_{p,m} \cdot \sin(\beta) \quad \text{(verso il basso)}
$$

### Effetto sulle azioni

| Grandezza | Contributo |
|---|---|
| F_x (forza orizzontale agente) | **− H** (favorevole: riduce la spinta) |
| F_y (peso/verticale stabilizzante) | **+ V** (favorevole) |
| Momento stabilizzante M_s | **+ H · (H_muro − Y)** (favorevole) |
| Momento ribaltante M_r | invariato (V applicato a X=0 → braccio nullo) |

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

Muro H=5 m, tirante con Y=1, β=15°, Interasse=1 m, Tp=100 kN:

- Tp_m = 100 / 1 = 100 kN/m
- H = 100 · cos(15°) = 96.6 kN/m
- V = 100 · sin(15°) = 25.9 kN/m
- ΔM_s = 96.6 · (5 − 1) = 386 kNm/m

Se senza tirante FS_scorr = 1.2 con F_x = 80 kN/m e R = 96 kN/m:

- Con tirante: F_x' = 80 − 96.6 = −16.6 kN/m (negativo → coesione/tirante
  annulla la spinta orizzontale → FS_scorr = ∞, GDW segnala "verificato")

## Verifiche interne fila per fila con tiranti

L'ancoraggio del tirante è schematizzato come **forza concentrata al livello
Y** sulla faccia valle del muro. Per le verifiche interne (giunti orizzontali
tra file di gabbioni) GDW applica il filtro:

> **Un tirante contribuisce al giunto solo se la sua ancoraggio è SOPRA il
> giunto** (Y_anchor < altezzaParziale_sopra_giunto).

In altre parole:

- **Giunti sopra l'ancoraggio**: nessun contributo del tirante (la forza
  agisce sulla porzione di muro sotto il giunto).
- **Giunti sotto l'ancoraggio**: il tirante contribuisce con H, V e ΔM_s
  (la forza è trasmessa attraverso il giunto verso il basso).

### Esempio

Muro H=5 m (5 file da h=1 m), tirante ancorato a Y=1.5 m (fra fila 4 e 3
dall'alto).

| Giunto | Posizione | altezzaParziale | Y_anchor < altezzaParziale? | Tirante applicato? |
|---|---|---|---|---|
| Sopra fila 5 | 1 m dalla testa | 1.0 m | 1.5 < 1.0 ? **NO** | ✗ |
| Sopra fila 4 | 2 m dalla testa | 2.0 m | 1.5 < 2.0 ? **SÌ** | ✓ |
| Sopra fila 3 | 3 m dalla testa | 3.0 m | 1.5 < 3.0 ? **SÌ** | ✓ |
| Sopra fila 2 | 4 m dalla testa | 4.0 m | 1.5 < 4.0 ? **SÌ** | ✓ |
| Base (sopra fila 1) | 5 m dalla testa | 5.0 m | 1.5 < 5.0 ? **SÌ** | ✓ |

→ La fila più alta (#5, sopra l'ancoraggio) **non** beneficia del tirante.
Le file 4, 3, 2 e la base beneficiano.

> **Nota di modellazione.** Il modello assume che il tirante sia ancorato
> con **piastra o putrelle di ferro** che redistribuiscono il tiro alla
> singola fila a quota Y. Per ancoraggi che attraversano più file
> (putrella alta più gabbioni), il modello distribuisce comunque l'intera
> forza al livello Y. Per analisi più raffinate (distribuzione su più
> file) è consigliabile inserire più tiranti "fittizi" alle quote dei
> diversi punti di contatto della putrella.

## Limitazioni attuali

- **Verifica del tirante stesso** (resistenza barra, bulbo, ancoraggio)
  **non è inclusa** in GDW. Da effettuare separatamente (Tiranti NX).
- **Stabilità globale Bishop**: i tiranti non concorrono al momento
  resistente. Per analisi rigorose globali, usare un altro strumento.

## Vedi anche

- [Verifiche esterne](verifiche.md) — ribaltamento, scorrimento, q_lim
- [Verifiche interne](verifiche-interne.md) — per fila (senza tiranti per ora)
- [Bishop globale](bishop.md) — limitazioni
