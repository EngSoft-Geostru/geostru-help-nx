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

## Limitazioni attuali

- **Verifica del tirante stesso** (resistenza barra, bulbo, ancoraggio)
  **non è inclusa** in GDW. Da effettuare separatamente (Tiranti NX).
- **Stabilità globale Bishop**: i tiranti non concorrono al momento
  resistente. Per analisi rigorose globali, usare un altro strumento.
- **Verifiche interne fila per fila** con tiranti: l'effetto è applicato al
  muro completo, non si distribuisce per fila (TBD).

## Vedi anche

- [Verifiche esterne](verifiche.md) — ribaltamento, scorrimento, q_lim
- [Verifiche interne](verifiche-interne.md) — per fila (senza tiranti per ora)
- [Bishop globale](bishop.md) — limitazioni
