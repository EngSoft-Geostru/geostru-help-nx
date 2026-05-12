# Geometria del muro

Il muro è una pila di **gabbioni** disposti su `numFile` righe orizzontali,
dal basso verso l'alto. Ogni fila può avere un numero diverso di blocchi e
uno spostamento personalizzato, permettendo di realizzare profili a piramide,
allineati a parete, a gradoni asimmetrici, ecc.

## Sistema di coordinate

- **X positivo verso monte (destra)** — verso il terrapieno
- **Y positivo verso l'alto**
- **Origine (0, 0)** = piede di valle del muro (bottom-left della fila 1)

## Campi principali

### Numero file

Numero di righe di gabbioni dal basso. Tipicamente 3÷6 per muri 3÷6 m. Massimo 20.

### Blocchi per fila

Per ogni fila imposti quanti gabbioni la compongono. Vincolo: il numero di
blocchi non può **aumentare** salendo (`blocchi[i+1] ≤ blocchi[i]`) — altrimenti
errore di validazione.

Esempi:

| Profilo | Blocchi (dal basso) | Forma |
|---|---|---|
| Piramide a destra | 5 · 4 · 3 · 2 · 1 | tutti i gradoni a sinistra (valle) |
| Verticale stretto | 2 · 2 · 1 · 1 | due gradoni asimmetrici |
| Trapezio simmetrico | 4 · 3 · 2 (con shift = +bg/2 per fila) | gradoni a destra E sinistra |

### Spostamento per fila

Spostamento orizzontale di ogni fila, in metri:

- **shift > 0** → fila spostata verso valle (sinistra)
- **shift < 0** → fila spostata verso monte (destra) — utile per battitura mascherata
- **shift = 0** → fila allineata a destra (caso più comune)

L'ascissa è applicata al **bordo destro** della fila: con `shift[i] = +0.5`, la fila `i` ha il bordo destro a `pDx − 0.5` invece che a `pDx`.

### Allineamento (combo rapida)

Imposta tutti gli shift in un colpo solo:

- **A destra** (default) — `shift[i] = 0`. Paramento verso monte verticale e flush. Gradoni verso valle.
- **A sinistra** — sposta le file superiori in modo che il paramento verso valle sia flush. Gradoni verso monte → attiva il **riempimento a tergo** (calcolo cambia: δ = φ, peso riempimento entra come stabilizzante).
- **Centrato** — gradoni simmetrici. Il paramento monte e valle sono entrambi battuti.
- **Personalizzato** — mantiene gli shift che hai impostato a mano.

### Prima fila interrata

Se attiva, la prima fila è interrata di `altGab` sotto il piano campagna a valle. Effetti:

- Disegno: la fila 1 appare sotto il livello terreno
- Calcolo: la **spinta passiva** del terreno di fondazione viene attivata sul lato di valle (riduce la spinta sollecitante)

## Allineamento automatico vs manuale

L'allineamento è una scorciatoia: appena modifichi a mano uno shift, la combo passa automaticamente a "Personalizzato".

!!! tip "Allineamento per applicazione"
    - **Muri stradali / regimazione idraulica**: tipicamente "A destra" (paramento verticale verso il fiume, gradoni verso il rilevato).
    - **Muri di sostegno con terreno disponibile a tergo**: "A sinistra" — sfrutta il peso del riempimento.
    - **Estetica / vista**: "Centrato" simmetrico.

## Gabbioni — proprietà

Sezione **Gabbioni**:

- **Tipologia**: combo che pesca dal catalogo `tipologie-gabbioni.json` (1×1×1, 2×1×1, 1.5×1×1, 1×0.5×1, ecc.). Selezionando una voce auto-compila peso specifico, base/altezza/profondità, peso filo.
- **Peso specifico γ_G** (kN/m³): tipicamente 14÷18 (dipende da grado di costipamento e tipo di pietrame).
- **Base × altezza × profondità**: dimensioni del singolo gabbione. La profondità è perpendicolare al disegno (z) e si usa per il peso/m. Standard: 1×1×1 m oppure 2×1×1 m.
- **Modalità angolo attrito gabbioni** (φ_g):
    - `auto` per **ES (elettrosaldata)** → φ_g = 25·γ−10° (formula gabbioni elettrosaldati)
    - `auto` per **DT (doppia torsione)** → φ_g = **45°** (valore di letteratura)
    - `manuale` → inserisci il valore sperimentale (tipico 26÷45°)

## Altezza totale muro

Letta in tempo reale sotto **Numero file**: `H = numFile × altezzaGabbione`.

## Base muro

Letta accanto al campo **Base fondazione**: `B_muro = blocchi[0] × baseGabbione`. La fondazione deve essere ≥ B_muro.

---

## Vedi anche

- [Inclinazione del muro α](inclinazione-muro.md) — battitura globale e suo effetto su Coulomb
- [Fondazione](fondazione.md) — base, spessore, inclinazione β
- [Rete metallica](rete.md) — scelta tra DT e ES, impatto su φ_g e c_g
