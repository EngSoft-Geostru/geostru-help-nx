# Esempio numerico svolto a mano

Ricostruzione **passo-passo** di un caso di riferimento per documentare la tracciabilità del calcolo di RockPlane NX. I valori sono ottenuti analiticamente con calcolatrice scientifica, indipendenti dal software, e confrontati con l'output del motore di calcolo.

Costituisce il **riferimento per audit normativi** e per chi vuole verificare manualmente la coerenza tra formule del manuale teorico (Hoek-Bray / RocPlane) e implementazione.

## 1. Dati di input del caso base

| Parametro                | Valore           |
|--------------------------|------------------|
| H · altezza versante     | 30 m             |
| β · inclinazione fronte  | 60°              |
| α · inclinazione piano   | 30°              |
| ψ · inclinazione bench   | 0°               |
| γ · peso volume          | 26 kN/m³         |
| c · coesione             | 50 kPa           |
| φ · angolo d'attrito     | 30°              |
| Approccio                | Caratteristico (γ = 1.0) |
| Acqua / Sisma / Interventi | Assenti |

## 2. Geometria

```
N = H / sin β = 30 / 0.86603 = 34.641 m
L = H / sin α = 30 / 0.50000 = 60.000 m
M = (L·cos α − H·cot β) / cos ψ = 34.641 m
A = ½·H²·(cot α − cot β) = ½·900·(1.732 − 0.577) = 519.62 m²
W = γ · A = 26 · 519.62 = 13 510.2 kN/m
```

## 3. Forze ed equilibrio

```
F_x = 0                    (no E, no sisma, no interventi)
F_y = W_y = −γ_G · W = −13 510.2 kN/m
N   = −F_y·cos α + F_x·sin α − U
    = 13 510.2 · 0.866 + 0 − 0 = 11 700.6 kN/m
S   = −F_y·sin α − F_x·cos α
    = 13 510.2 · 0.500 − 0     = 6 755.1 kN/m
```

## 4. Resistenza Mohr-Coulomb e FS

```
τ_res = c·L/γ_c + N·tan φ/γ_φ
      = 50·60 + 11 700.6 · 0.57735
      = 3 000 + 6 754.8 = 9 754.8 kN/m

FS    = τ_res / |S| = 9 754.8 / 6 755.1 = 1.4441
```

## 5. Confronto manuale ↔ software

| Grandezza      | A mano          | Software        | Δ            |
|----------------|-----------------|-----------------|--------------|
| N (normale)    | 11 700.6 kN/m   | 11 700.6 kN/m   | < 0.001 %    |
| S (taglio)     | 6 755.1 kN/m    | 6 755.1 kN/m    | < 0.001 %    |
| τ_res          | 9 754.8 kN/m    | 9 754.8 kN/m    | < 0.001 %    |
| **FS**         | **1.4441**      | **1.4441**      | **0.0000**   |

Coincidenza esatta alla quarta cifra decimale. La formulazione del software riproduce fedelmente la formula classica Hoek-Bray:

```
FS = (c·L + W·cos α·tan φ) / (W·sin α)
```

## 6. Estensione con sisma kh = 0.15

```
S_mod = k_h · W = 0.15 · 13 510.2 = 2 026.5 kN/m
F_x   = −2 026.5 kN/m       F_y = −13 510.2 kN/m
N     = 13 510.2·0.866 − 2 026.5·0.500 = 10 687.3 kN/m
S     = 13 510.2·0.500 + 2 026.5·0.866 =  8 510.1 kN/m
τ_res = 3 000 + 10 687.3 · 0.57735     =  9 170.0 kN/m
FS    = 9 170.0 / 8 510.1 = 1.078
```

Confronto col software: **FS = 1.0776**, coincidenza a 4 cifre.

## 7. Estensione con acqua nella discontinuità (uplift U)

Caso base + Z<sub>w</sub> = 10 m, distribuzione triangolare max al piede (eq. 20 del modello teorico).

```
u_max = γ_w · Z_w = 9.81 · 10 = 98.1 kPa
s_wet = Z_w / sin α = 10 / 0.5 = 20.0 m
U     = ½ · u_max · s_wet = ½ · 98.1 · 20 = 981.0 kN/m
N_eff = 11 700.6 − 981.0 = 10 719.6 kN/m
S     = 6 755.1 kN/m   (invariato)
τ_res = 3 000 + 10 719.6 · 0.57735 = 9 188.4 kN/m
FS    = 9 188.4 / 6 755.1 = 1.360
```

Confronto col software: **FS = 1.3603** e **U = 981.0 kN/m**. Coincidenza esatta.

## 8. Estensione con chiodo passivo (Clouterre N-V)

Caso base + chiodo passivo F = 500 kN/m, Δ = 15° sotto-orizzontale.

```
K_x = F · cos Δ  =  500 · 0.96593 =  482.96 kN/m
K_y = −F · sin Δ = −500 · 0.25882 = −129.41 kN/m
N   = 13 639.6 · 0.866 + 482.96 · 0.500 = 12 054.2 kN/m
S   = 6 755.1 kN/m   (invariato — K passiva non entra in S motore)

contrib_K = K_x · cos α + K_y · sin α = 353.7 kN/m
τ_res     = 3 000 + 12 054.2 · 0.57735 + 353.7 = 10 314.5 kN/m
FS        = 10 314.5 / 6 755.1 = 1.527
```

**Verifica Clouterre** — Φ = α + Δ = 45°:

| Modalità | Contributo |
|---|---|
| Assiale  | T_max·(cos Φ + sin Φ · tan φ) = **557.6** |
| Taglio   | V_max·(sin Φ − cos Φ · tan φ) = **74.8**  |

Vince la modalità **assiale** → la forza applicata corrisponde alle componenti K calcolate. Confronto col software: **FS = 1.5267**.

## 9. Estensione con tirante attivo

Caso base + tirante con precarico F = 500 kN/m, Δ = 20°.

Il tirante entra come **AZIONE (J)** nelle risultanti F_x, F_y, non nella resistenza.

```
J_x = F · cos Δ  =  500 · 0.93969 =  469.85 kN/m
J_y = −F · sin Δ = −500 · 0.34202 = −171.01 kN/m
F_x = 469.85 kN/m       F_y = −13 681.2 kN/m
N   = 13 681.2 · 0.866 + 469.85 · 0.500 = 12 082.8 kN/m
S   = 13 681.2 · 0.500 − 469.85 · 0.866 =  6 433.6 kN/m  (ridotto)
τ_res = 3 000 + 12 082.8 · 0.57735 = 9 977.4 kN/m
FS    = 9 977.4 / 6 433.6 = 1.551
```

Confronto col software: **FS = 1.5506**, coincidenza a 3 cifre.

!!! tip "Tirante attivo vs chiodo passivo (a parità di F = 500 kN/m, Δ ≈ 15-20°)"
    - **Tirante attivo** (F=1.551): riduce S motore direttamente (forza pre-applicata).
    - **Chiodo passivo** (F=1.527): agisce attraverso τ resistente (mobilitato durante lo scorrimento).
    Il tirante è leggermente più efficace per la stessa forza F.

## 10. Riepilogo

| Caso       | Aggiunta al base                | FS     | Test interno |
|------------|---------------------------------|--------|--------------|
| 1–5        | caso base a secco               | 1.4441 | T03          |
| 6          | sisma k_h = 0.15                | 1.078  | T04          |
| 7          | acqua Z_w = 10 m, max al piede  | 1.360  | T05          |
| 8          | chiodo passivo F = 500, Δ = 15° | 1.527  | T07          |
| 9          | tirante attivo F = 500, Δ = 20° | 1.551  | T06          |

Tutti i casi coincidono **a 3-4 cifre decimali** con l'output del software, confermando la tracciabilità dei calcoli per ciascun meccanismo modellato (peso W, sisma S, acqua U, interventi J/K).

---

*Per la suite completa di 97 test automatici di regressione, vedi il [README del repository](https://github.com/EngSoft-Geostru) o contatta il team GeoStru.*
