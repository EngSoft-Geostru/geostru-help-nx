# Inclinazione del muro (α)

GDW supporta la **battitura globale del muro verso monte** (in inglese: "battered
wall"): l'intero corpo del muro viene inclinato di α (0÷15°) rispetto alla
verticale, ruotando come corpo rigido attorno al piede di valle.

## Convenzione

- **α > 0** = top del muro spostato **verso monte** (paramento interno inclinato
  dentro il terreno)
- **α = 0** = muro verticale (default storico)
- **Range**: 0÷15° (clamped)

```
α = 0                       α = 10° (verso monte)
                                 ╱─╲
                                ╱   ╲
   ┌──┐                       ╱─────╲
   │  │                      ╱       ╲
   ├──┤                     ╱─────────╲
   │  │                    ╱           ╲
   ├──┤                   ╱─────────────╲
   │  │                  ╱               ╲
   └──┘                 ─────────────────
   piede valle          piede valle (pivot della rotazione)
```

## Spostamento per fila

L'inclinazione si traduce in un **spostamento cumulativo** per ogni fila:

$$
\Delta = h_{gab} \cdot \tan(\alpha)
$$

dove `h_gab` è l'altezza del singolo gabbione. La fila `r` (dal basso, base = 0)
è spostata verso monte di `r · Δ` rispetto alla fila 0.

Esempio per `h_gab = 1 m`, `α = 10°`: Δ = 0.176 m per fila.

Il valore Δ è mostrato in tempo reale sotto il campo Inclinazione muro
("Spostamento per fila (calcolato): Δ = ...").

## Effetti sul calcolo

L'inclinazione del muro entra in **3 punti distinti** della formulazione:

### 1. Geometria (rotazione rigida)

Tutti gli elementi del muro (gabbioni + fondazione) ruotano di α attorno al
piede di valle. Conseguenze:

- **Baricentro globale del muro** ruotato → coordinata X aumenta verso monte (braccio stabilizzante maggiore).
- **Disegno**: il muro appare inclinato in sezione + nei preview SVG.

### 2. Formula di Coulomb (Ka)

L'angolo del paramento interno entra nella formula di Coulomb come **β**:

$$
K_a = \frac{\cos^2(\varphi - \beta - \theta)}{\cos^2 \beta \cdot \cos \theta \cdot \cos(\delta + \beta + \theta) \cdot \left[1 + \sqrt{\frac{\sin(\varphi+\delta)\sin(\varphi-\varepsilon-\theta)}{\cos(\delta+\beta+\theta)\cos(\varepsilon-\beta)}}\right]^2}
$$

con β = α (inclinazione del paramento). Per α > 0:

- `cos²(φ − β − θ)` cresce (avvicinandosi a 45°) → numeratore maggiore
- → **Ka aumenta** (es. da 0.36 a 0.47 per α 0→8°, +29%)

### 3. Direzione della spinta

La spinta totale `T` viene proiettata sul piano del paramento inclinato, con
angolo `δ + α` rispetto all'orizzontale:

$$
S_x = T \cdot \cos(\delta + \alpha) \quad ; \quad S_y = T \cdot \sin(\delta + \alpha)
$$

Effetto:

- **S_x diminuisce** rispetto al caso non corretto (cos cresce meno di Ka)
- **S_y aumenta** sensibilmente (sin di un angolo maggiore) → contributo verticale stabilizzante

## Esempio numerico

Muro 5 m, β_terreno (terrapieno) 25°, φ 35°, δ 23.3°:

| | α = 0° | α = 8° |
|---|---|---|
| Ka | 0.362 | **0.467** (+29%) |
| Spinta totale T (kN/m) | 85.9 | 110.8 |
| S_x = T · cos(δ+α) | 78.9 | 94.7 |
| S_y = T · sin(δ+α) | 34.0 | **57.6** (+70%) |
| FS_ribaltamento | 2.60 | **2.91** ✓ |
| FS_scorrimento | 1.85 | **2.45** ✓ |

→ Inclinare di 8° verso monte aumenta entrambi i FS principali. Il guadagno
viene dalla **componente verticale stabilizzante S_y** e dal **braccio del peso
muro** spostato verso monte. La spinta totale aumenta (Ka cresce), ma viene
"reindirizzata" in direzione più favorevole.

## Quando inclinare il muro

Ragionamenti pratici:

- **Muri alti (≥ 4 m)**: la battitura è quasi sempre utile (FS_rib migliora notevolmente).
- **Terreni con φ alto (≥ 35°)**: l'incremento Ka è modesto, S_y stabilizzante domina → benefico.
- **Terreni con φ basso (≤ 28°)**: l'incremento Ka è più sensibile, ma il muro è più "ribaltabile" → comunque benefico in genere.
- **Pratica costruttiva tipica**: 5÷8° per muri 3÷5 m.

## Cosa NON viene modificato

- **Fondazione**: ruota con il muro (corpo rigido) ma la sua inclinazione β della faccia inferiore è un parametro **separato** (vedi [Fondazione](fondazione.md)).
- **Stratigrafia**: rimane nelle posizioni assolute (non ruota).
- **Profilo terrapieno (monte)**: si attacca al top-right del muro ruotato e poi continua nella direzione originale (con angoli ε₁, ε₂ delle pendenze monte).
- **Sovraccarichi G/Q**: sono posizionati lungo il terrapieno (rispetto al top ruotato).

---

## Vedi anche

- [Geometria del muro](geometria.md) — file, blocchi, shift
- [Fondazione](fondazione.md) — inclinazione β della faccia inferiore (diversa da α)
- [Verifiche esterne](verifiche.md) — formula scorrimento con base inclinata
