# Verifiche esterne

Le tre verifiche di stabilità del muro come corpo rigido. GDW le calcola tutte
ad ogni `Calcola` e le mostra come pannello risultati con badge ✓/✗.

## 1. Ribaltamento

Verifica che il muro non ribalti attorno al **piede di valle**.

### Formula

$$
FS_{rib} = \frac{M_s}{\gamma_R \cdot M_r}
$$

con:

$$
M_s = \gamma_W \cdot W \cdot x_g \,+\, \gamma_S \cdot S_y \cdot B_{back} \,+\, S_{q,y} \cdot B
$$

$$
M_r = \gamma_S \cdot M_{S,x} \,+\, \gamma_E \cdot F_{inerz} \cdot y_g \,+\, \gamma_W \cdot M_{falda} \,+\, S_{q,x} \cdot H/2
$$

dove:

- `W` = peso muro, `x_g` = baricentro X del muro (dal piede di valle)
- `S_x`, `S_y` = componenti spinta totale (terreno + sovraccarico) orizz. e vert.
- `S_{q,y}` = contributo verticale del sovraccarico (stabilizzante)
- `F_inerz` = forza inerziale sismica del muro, `y_g` = braccio rispetto al piede
- `M_{S,x}` = momento della spinta orizzontale del terreno (forza × baricentro spinta)
- `M_{falda}` = momento della spinta dell'acqua (forza × baricentro idrostatico)
- `S_{q,x}` = componente orizzontale del sovraccarico, braccio H/2

Verifica soddisfatta: **FS_rib ≥ 1.0** (γ_R_rib statico) o **≥ 1.2** (sismico).

### Effetto inclinazione muro α

Quando α > 0, il baricentro X del muro si sposta verso monte → M_s cresce.
Inoltre la spinta viene proiettata su δ+α (Sy aumenta, contribuisce a M_s).

## 2. Scorrimento (con base inclinata)

Verifica che il muro non scivoli lungo la base. **Formula generalizzata** per
base inclinata di angolo β (vedi [Fondazione](fondazione.md)).

### Proiezione su piano inclinato

Le forze globali F_x (orizzontale) e F_y (verticale, positivo verso il basso)
vengono proiettate sul piano inclinato di β:

$$
N_\perp = F_y \cdot \cos\beta + F_x \cdot \sin\beta
$$

$$
F_{drive} = F_x \cdot \cos\beta - F_y \cdot \sin\beta
$$

- **N_⊥** è la forza che comprime la base inclinata
- **F_drive** è la forza che tende a far scorrere il muro lungo il piano (verso valle)

### Resistenza

$$
R = N_\perp \cdot \tan(\varphi_g) + c_g \cdot \frac{B}{\cos\beta}
$$

dove:

- φ_g e c_g sono i parametri d'interfaccia (vedi [Geotecnica → Interfaccia alla base](geotecnica.md))
- B/cos(β) è la lunghezza reale del piano inclinato (maggiore di B)

### Fattore di sicurezza

$$
FS_{scorr} = \frac{R + R_{passiva}}{\gamma_R \cdot F_{drive}}
$$

R_passiva = spinta passiva ridotta (solo se prima fila interrata).

Verifica soddisfatta: **FS_scorr ≥ 1.0** (γ_R_scorr = 1.1).

### Casi limite

- Se F_drive ≤ 0 (β grande): la geometria stessa trattiene il muro → FS = sentinella (999).
- Se β = 0: la formula si riduce a F_drive = F_x, N_⊥ = F_y, R = F_y·tan(φ) + c·B → caso classico.

[Dettagli matematici nella conversazione di sviluppo →](inclinazione-muro.md)

## 3. Capacità portante (q_lim)

Verifica che il terreno di fondazione non collassi sotto il peso del muro.

### Formula Brinch-Hansen

$$
q_{lim} = c \cdot N_c \cdot s_c \cdot d_c \,+\, q_0 \cdot N_q \cdot s_q \cdot d_q \,+\, \tfrac{1}{2} \cdot \gamma \cdot B' \cdot N_\gamma \cdot s_\gamma \cdot d_\gamma
$$

con:

- N_q, N_γ, N_c = fattori di portanza (funzione di φ_fond)
- s_*, d_* = fattori di forma e profondità (semplificati per striscia infinita)
- q_0 = γ · D (sovraccarico laterale = pressione del terreno alla quota fondazione)
- B' = B − 2·e (larghezza effettiva, corretta per eccentricità di carico)

### Tensione applicata

$$
\sigma_{eff} = \frac{F_y}{B'}
$$

### Fattore di sicurezza

$$
FS_{qlim} = \frac{q_{lim}}{\gamma_{R3,qlim} \cdot \sigma_{eff}}
$$

Verifica soddisfatta: **FS_qlim ≥ 1.0** (γ_R = 2.3).

### Capacità portante in pratica

Generalmente q_lim è molto alta (~700 kPa per φ=32°, B=3 m) e σ_eff modesta
(~70 kPa) → FS spesso 8÷10. La verifica diventa critica solo per terreni
molto deboli (argille molli, riporti) o muri molto alti su base stretta.

## Visualizzazione

Pannello risultati mostra:

- **Tre coppie** Mr/Ms o R/F_drive o σ/q_lim e relativi FS
- **Badge ✓/✗** colorato
- **Popover** sui ✗ rossi con consigli pratici (aumenta base, batti il muro, ecc.)

## Vedi anche

- [Verifiche interne](verifiche-interne.md) — fila per fila
- [Inclinazione del muro](inclinazione-muro.md) — formula scorrimento con α
- [Fondazione](fondazione.md) — β della base inclinata
- [Coefficienti NTC](coefficienti.md) — γ_R3, γ_M
