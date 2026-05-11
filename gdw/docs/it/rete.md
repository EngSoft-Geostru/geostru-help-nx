# Rete metallica

GDW supporta **due tipologie di rete** per i gabbioni, con calcoli e verifiche
diverse:

1. **Rete a doppia torsione (DT) — Maccaferri** (default)
2. **Rete elettrosaldata (ES) — rigida**

La scelta si fa dal combo **Tipologia di maglia** in cima alla sezione Rete.

## Differenze sostanziali

| Aspetto | DT (Maccaferri) | ES (elettrosaldata) |
|---|---|---|
| Filosofia | Maglia esagonale flessibile, intessuta | Pannello rigido, fili saldati ai nodi |
| Comportamento | Si deforma e si adatta a cedimenti | Rigida; rotture localizzate possibili |
| Verifica primaria | **σ_max ≤ σ_adm** Maccaferri Gawac | **FS_punzonamento** del filo singolo |
| φ_g (attrito gabbione-gabbione) | **45°** fissato | 25·γ−10° (tipicamente 26÷32°) |
| c_g (coesione apparente) | **> 0** (dalla rete intessuta) | 0 |
| Cataloghi tipici | Maccaferri (6×8, 8×10, Zn / Zn+PVC) | Reti di produzione locale (5×20, 10×10, ecc.) |

## Rete a doppia torsione (Maccaferri)

### Catalogo

GDW include un catalogo con 7 modelli reali dalla scheda tecnica Maccaferri/GSI:

| Codice | Maglia | Diametro filo | Rivestimento | Peso (kg/m²) | Resistenza (kN/m) | c_g (kPa) |
|---|---|---|---|---|---|---|
| `6x8-2.2-zinc` | 6×8 | Ø 2.2 mm | Zn forte | 1.30 | 37 | 2.0 |
| `6x8-2.7-zinc` | 6×8 | Ø 2.7 mm | Zn forte | 1.80 | 50 | 3.0 |
| **`8x10-2.7-zinc`** | **8×10** | **Ø 2.7 mm** | Zn forte | **1.40** | **50** | **3.0** |
| `8x10-3.0-zinc` | 8×10 | Ø 3.0 mm | Zn forte | 1.75 | 50 | 4.0 |
| `6x8-2.2-pvc` | 6×8 | Ø 2.2/3.2 mm | ZnAl + PVC | 1.56 | 37 | 2.5 |
| `8x10-2.7-pvc` | 8×10 | Ø 2.7/3.7 mm | ZnAl + PVC | 2.16 | 50 | 3.5 |
| `8x10-3.0-pvc` | 8×10 | Ø 3.0/4.0 mm | ZnAl + PVC | 2.10 | 60 | 4.5 |

Selezionare un modello dal combo auto-compila peso unitario, resistenza rete e
c_g.

Lo **standard pratico** Maccaferri per muri di sostegno è la **8×10 Ø 2.7 mm**
(filo zincato forte oppure con rivestimento PVC se in ambiente aggressivo).

### Coesione apparente c_g

La rete a doppia torsione intessuta conferisce al gabbione una **coesione
apparente** c_g (formula empirica Gawac):

$$
c_g \approx 0.15 \cdot P_u
$$

dove P_u è il peso della rete. Nella pratica i valori da catalogo sono
calibrati direttamente (vedi tabella sopra). c_g entra nelle verifiche di
scorrimento ad ogni **giunto gabbione-gabbione** (i > 0) e all'interfaccia
muro-fondazione (i = 0 se c'è la fondazione c.a.).

### σ ammissibile (Maccaferri Gawac)

Per ogni fila del muro, la pressione normale massima sulla sezione del giunto
viene confrontata con un valore ammissibile empirico:

$$
\sigma_{adm} = 50 \cdot \gamma_G[\text{tf/m}^3] - 30 \quad [\text{kPa}]
$$

con γ_G peso specifico del gabbione. GDW converte automaticamente da kN/m³ a
tf/m³ (γ_tf = γ_kN/m³ ÷ 9.81). Per γ_G = 16 kN/m³: σ_adm ≈ 51.5 kPa.

La verifica è **σ_max ≤ σ_adm** per ogni fila, con σ_max = max(σ_v, σ_m) delle
tensioni al lembo valle/monte. Il badge ✓/✗ accanto a "Tensioni fila X" indica
l'esito.

### Punzonamento

Per la DT **non si verifica il punzonamento**: la maglia flessibile distribuisce
il carico localizzato del pietrame senza rotture concentrate. Il campo
`FSPunzonamento` è vuoto nei risultati.

## Rete elettrosaldata

### Parametri

Quando si seleziona "Elettrosaldata":

- **Resistenza rete (trazione)** in kN/m — resistenza ultima del pannello a trazione
- **Resistenza al punzonamento** in N — carico massimo locale per non rompere il singolo filo
- Catalogo: non fornito (i pannelli sono di produzione locale)

### Verifica trazione

$$
FS_{rete} = \frac{R_{rete}}{S_{tot,x}}
$$

Confronta la resistenza a trazione del pannello con la spinta orizzontale
totale. Conservativo (assume che il pannello sia teso uniformemente).

### Verifica punzonamento

$$
FS_{punz} = \frac{R_{punz}}{F_{locale}}
$$

con F_locale = peso pietra critica × coefficiente di posa ÷ fili in contatto.
GDW assume:

- Peso pietra critica: 0.2 kN (~20 kg)
- Coefficiente dinamico di posa: 1.5 (caduta dall'alto)
- Fili in contatto: 1 (conservativo)

→ F_locale = 0.2 × 1.5 / 1 = 0.30 kN. Per R_punz = 60 N → FS = 60/0.30 = 200 (ampiamente verificato).

## Quale scegliere

Per **muri di sostegno**:

- **DT** (default GDW): pratica corrente per Maccaferri e simili. Si deforma in caso di cedimenti del terreno → riduce il rischio di collasso fragile. c_g aumenta FS interni.
- **ES**: applicazioni dove la rigidità è richiesta (es. muri sismicamente sensibili dove la deformabilità non è desiderata, oppure produzione locale economica).

Per **opere paramassi**:

- Quasi sempre DT (la flessibilità è essenziale per assorbire energia di impatto).

---

## Vedi anche

- [Verifiche interne](verifiche-interne.md) — σ_max vs σ_adm, scorrimento con c_g
- [Geometria del muro](geometria.md) — modalità angolo attrito gabbioni (auto / manuale)
- [Formati file](formati.md) — campi rete persistiti nel `.gabbioni`
