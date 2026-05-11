# Fondazione

La fondazione è centrata sotto la prima fila di gabbioni. Può essere
**orizzontale** (default) o **inclinata verso monte** (β > 0) per migliorare
la resistenza allo scorrimento.

## Geometria

La fondazione è un poligono trapezoidale con:

- **Top orizzontale**: dove poggia la prima fila del muro
- **Bottom inclinato** (se β > 0): il lato monte scende più in profondità del lato valle

```
                ┌─────────────────┐  ← top fondazione (= base muro)
               ╱                  │
              ╱                   │
        h_v  ╱                    │ h_m = h_v + B·tan(β)
            ╱                     │
           ╲_____________________╱   ← bottom fondazione inclinata
           valle             monte
```

## Campi

### Base (B_fond)

Larghezza orizzontale della fondazione, in metri. Vincolo: ≥ base muro
(`B_fond ≥ B_muro`). L'esubero `(B_fond − B_muro)` è ripartito **50/50** tra
valle e monte (fondazione centrata rispetto alla prima fila).

Sotto il campo Base, in tempo reale: **"base muro: X.XX m"** come riferimento.

### Spessore a valle (h_v)

Spessore della fondazione sul lato di valle (sinistra), in metri. Per
fondazioni orizzontali (β = 0) è lo spessore uniforme.

### Inclinazione fondazione (β)

Inclinazione della faccia inferiore della fondazione rispetto all'orizzontale,
in gradi. Range 0÷15°.

- **β = 0** → fondazione orizzontale (caso tradizionale)
- **β > 0** → faccia inferiore inclinata verso monte (il lato monte affonda di più)

Sotto il campo, in tempo reale: **"Spessore a monte (calcolato): h_m = h_v + B·tan(β) = X.XX m"**

### Prima fila interrata

Checkbox separato (sezione Geometria). Se attivo, la prima fila di gabbioni
è interrata di `altGab` sotto il piano campagna a valle. Attiva la **spinta
passiva** a valle:

$$
S_p = \tfrac{1}{2} \cdot \gamma_{fond} \cdot K_p \cdot H^2
$$

con H = altezza interrata. Riduce la spinta sollecitante orizzontale.

## Perché inclinare la fondazione

L'inclinazione β > 0 migliora la **resistenza allo scorrimento esterno**: la
spinta orizzontale, per far scorrere il muro verso valle, deve "salire" lungo
il piano inclinato.

La formula della verifica scorrimento con base inclinata (vedi [Verifiche
esterne](verifiche.md)):

$$
N_{\perp} = F_y \cdot \cos\beta + F_x \cdot \sin\beta
$$
$$
F_{drive} = F_x \cdot \cos\beta - F_y \cdot \sin\beta
$$
$$
FS_{scorr} = \frac{N_{\perp} \cdot \tan\varphi + c \cdot B/\cos\beta}{\gamma_R \cdot F_{drive}}
$$

Effetti:

- Per β > 0 e F_y > 0: F_drive diminuisce (Sy aiuta a "tenere fermo" il muro)
- N⊥ aumenta (la spinta orizzontale comprime la base) → resistenza per attrito maggiore
- La lunghezza reale del piano inclinato è B/cos(β) > B → coesione contribuisce di più

## Esempio numerico

Muro 5 m, B_fond = 3.2 m, h_v = 0.30 m, φ_fond = 32°, F_x = 95 kN/m, F_y = 240 kN/m:

| β | F_drive | N_⊥ | R = N_⊥·tanφ | FS_scorr (γ_R=1.1) |
|---|---|---|---|---|
| 0° | 95.0 | 240.0 | 149.9 | 1.43 |
| 5° | 73.7 | 247.3 | 154.5 | 1.91 |
| **10°** | **52.9** | **252.8** | **157.9** | **2.71** |
| 15° | 29.6 | 256.4 | 160.2 | 4.92 |

→ Una pendenza di 10° **quasi raddoppia** il FS scorrimento.

## Effetti collaterali

- **Disegno**: la fondazione è renderizzata come trapezio (4 vertici).
- **Bishop**: la quota più profonda della fondazione (lato monte = `wallBaseY − h_m`) è il limite che la superficie di scorrimento deve passare SOTTO. Validazione automatica: se il cerchio attraversa la fondazione, errore.
- **Carico limite**: la profondità della fondazione (per Brinch-Hansen) usa h_v (lato valle) come `D` di incastro — più conservativo.

## Limiti pratici di β

Tipicamente 5÷10° in pratica costruttiva:

- < 5° → effetto trascurabile
- > 10° → richiede preparazione accurata dello scavo (la base di scavo deve essere effettivamente inclinata)
- > 15° → fuori range GDW (richiede analisi specifiche e fondazione su roccia o palificata)

---

## Vedi anche

- [Geometria del muro](geometria.md) — base muro, allineamento
- [Verifiche esterne](verifiche.md) — formula scorrimento completa con β
- [Stabilità globale Bishop](bishop.md) — validazione cerchio sotto fondazione inclinata
