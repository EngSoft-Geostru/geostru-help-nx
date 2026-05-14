# Modello teorico

RockPlane NX implementa il metodo dell'**equilibrio limite** (Limit Equilibrium Method, LEM) sul cuneo planare in roccia, secondo il manuale **Hoek-Bray** (1981) e la documentazione **Rocscience RocPlane**.

## Ipotesi del modello

1. **Rottura planare**: la superficie di scorrimento è una **singola discontinuità persistente** orientata in modo da soddisfare il *daylighting* (α < β).
2. **Cuneo bidimensionale**: si analizza una sezione tipo per metro di sviluppo lungo la cresta; il blocco è esteso ortogonalmente con profondità B.
3. **Corpo rigido**: il cuneo è trattato come corpo rigido. Le forze entrano nell'equilibrio come risultanti; il **punto di applicazione non è rilevante** (solo equilibrio di traslazione, non di rotazione).
4. **Mohr-Coulomb**: resistenza al taglio sul piano modellata con criterio lineare τ = c' + σ<sub>n</sub>·tan φ'.
5. **Acqua**: pressioni interstiziali u(s) note (analisi disaccoppiata flusso/equilibrio).
6. **Sisma**: forza inerziale **pseudostatica** k<sub>h</sub>·W applicata al baricentro.

## Riferimento cartesiano

```
                ψ
        B─────────────C  (sommità del piano)
       /│             │
      / │             │
     /  │             │
    /β  │             │ H
   /    │             │
  /     │             │
 O──────┴──────────────
 │ X→ verso monte
 │ Y↑ verticale
```

- O = (0, 0) — piede del versante
- X positivo = verso monte (intact rock)
- Y verticale positivo verso l'alto
- t̂ = (−cos α, −sin α) — direzione di scorrimento del cuneo (verso valle-basso)

## Geometria — Caso A (senza tension crack)

Equazioni (1)–(9) del manuale teorico:

$$ N = \frac{H}{\sin\beta} $$

$$ B_x = H \cdot \cot\beta, \quad B_y = H $$

$$ L = H \cdot \frac{1 - \cot\beta \cdot \tan\psi}{\sin\alpha - \cos\alpha \cdot \tan\psi} $$

$$ M = \frac{L \cdot \cos\alpha - H \cdot \cot\beta}{\cos\psi} $$

$$ C_x = L \cdot \cos\alpha, \quad C_y = L \cdot \sin\alpha $$

$$ A = \frac{1}{2} \cdot |B_x \cdot C_y - B_y \cdot C_x| $$

$$ W = \gamma \cdot A $$

## Geometria — Caso B (con tension crack)

Equazioni (11)–(18):

$$ C = B + (T, T \cdot \tan\psi) $$

$$ M = \frac{T}{\cos\psi} $$

$$ Q = \frac{C_y \cdot \cot\alpha - C_x}{\sin\theta \cdot \cot\alpha - \cos\theta} \quad \text{(eq. 17)} $$

$$ L = \frac{C_x - Q \cdot \cos\theta}{\cos\alpha} \quad \text{(eq. 15)} $$

$$ D = (L \cdot \cos\alpha, L \cdot \sin\alpha) \quad \text{(eq. 14)} $$

$$ A = \frac{1}{2}|B \times D| + \frac{1}{2}|(D - B) \times (C - B)| \quad \text{(eq. 18)} $$

## Equilibrio di traslazione (eq. 26–30)

### Forze attive sul cuneo

Le azioni esterne applicate al cuneo:

| Termine                | Origine                                    | Componenti                     |
|------------------------|--------------------------------------------|---------------------------------|
| W                      | peso del cuneo                             | $W_y = -\gamma_G \cdot W$        |
| E                      | forza esterna                              | $E_x = -\gamma_a \cdot E \cos\delta, E_y = -\gamma_a \cdot E \sin\delta$ |
| S sisma                | inerziale pseudostatica                    | $S_x = -k_h W \cos\Omega, S_y = -k_h W \sin\Omega$ |
| J                      | tiranti attivi                             | $J_x = F \cos\Delta, J_y = -F \sin\Delta$ |
| V                      | acqua nella tension crack                  | $V_x = -V \sin\theta, V_y = V \cos\theta$ |
| U<sub>p</sub>          | acqua ponded esterna                       | direzione ⟂ al fronte           |
| R1                     | rete corticale                             | direzione ⟂ al fronte, verso il cuneo |

### Risultanti

$$ F_x = E_x + S_x + J_x + V_x + U_{p,x} + R_{1,x} $$

$$ F_y = W_y + E_y + S_y + J_y + V_y + U_{p,y} + R_{1,y} $$

### Normale e taglio sul piano (eq. 28–29)

$$ N = -(F_y + K_y) \cdot \cos\alpha + (F_x + K_x) \cdot \sin\alpha - U \quad \text{(eq. 28)} $$

$$ S = -F_y \cdot \sin\alpha - F_x \cdot \cos\alpha \quad \text{(eq. 29)} $$

dove K<sub>x</sub>/K<sub>y</sub> sono i contributi dei chiodi passivi (vedi sotto) e U è la sottospinta uplift dell'acqua sul piano.

### Resistenza Mohr-Coulomb (eq. 30)

$$ \tau = \frac{c \cdot L}{\gamma_c} + N \cdot \frac{\tan\varphi}{\gamma_\varphi} + K_x \cos\alpha + K_y \sin\alpha + \tau_{rete} $$

### Fattore di sicurezza

$$ FS = \frac{\tau}{|S|}, \quad \text{verificato:} \quad FS \geq FS_{richiesto} = \gamma_R $$

## Chiodi passivi — interazione N-V Clouterre

Per chiodi passivi, la barra mobilita simultaneamente trazione T e taglio V al passaggio del piano. Criterio di Clouterre 1993 lineare:

$$ \frac{T}{T_{max}} + \frac{V}{V_{max}} \leq 1 $$

RockPlane calcola la modalità ottima che massimizza il contributo a τ resistente, considerando sia il contributo diretto (T·cos Φ + V·sin Φ) sia l'incremento di N che attiva attrito:

$$ \text{contrib}_{axial} = T_{max} \cdot (\cos\Phi + \sin\Phi \cdot \tan\varphi_{des}) $$

$$ \text{contrib}_{shear} = V_{max} \cdot (\sin\Phi - \cos\Phi \cdot \tan\varphi_{des}) $$

con Φ = α + Δ angolo bar-piano. Si sceglie la modalità con contributo maggiore (corner solution).

## Acqua sul piano — U uplift

La pressione interstiziale u(s) lungo il piano di rottura genera una sottospinta U normale al piano:

$$ U = \int_0^L u(s) \, ds $$

Quattro forme di distribuzione (vedi [Acque](acque.md)):
- Assente
- Triangolare con picco a metà altezza
- Triangolare con picco al piede (eq. 20 manuale, $u_{max} = \gamma_w \cdot Z_w$)
- Triangolare con picco alla base della fessura di trazione

## Ricerca α critico

Sweep dell'inclinazione del piano di rottura per individuare il valore che **minimizza FS**:

```
for α in [α_min, α_max] step 1°:
    compute FS(α)
refine around argmin α with step 0.05°
return α_critico
```

Dominio di sweep: α ∈ (max(0.5°, ψ+0.5°), β−0.5°) — cinematicamente ammissibile.

[Dettagli α critico →](alfa-critico.md)

## Coefficienti parziali — applicazione

| Approccio                | Su W (γ<sub>G</sub>) | Su E var. (γ<sub>Q</sub>) | Su tan φ' (γ<sub>φ'</sub>) | Su c' (γ<sub>c'</sub>) | FS richiesto |
|--------------------------|-----------------------|---------------------------|-----------------------------|--------------------------|--------------|
| Caratteristico           | 1.00                  | 1.00                      | 1.00                        | 1.00                     | 1.30 (default) |
| NTC 2018 A2+M2+R2        | 1.00                  | 1.30                      | 1.25                        | 1.25                     | 1.10         |
| EC7 DA1.C1               | 1.35                  | 1.50                      | 1.00                        | 1.00                     | 1.00         |
| EC7 DA1.C2               | 1.00                  | 1.30                      | 1.25                        | 1.25                     | 1.00         |
| EC7 DA2                  | 1.35                  | 1.50                      | 1.00                        | 1.00                     | 1.10         |
| EC7 DA3                  | 1.00                  | 1.30                      | 1.25                        | 1.25                     | 1.00         |

γ<sub>E</sub> (sisma) = 1.00 in tutti gli approcci (NTC §3.2.4 / EC8).

## Validazione

Il software è validato con **97 test automatici** (xUnit), di cui 12 benchmark con valori attesi da formula analitica. Esito: **97/97 PASSATI**. Vedi [Annex A nella relazione di calcolo](export.md) generata dal software.

## Riferimenti

- Hoek E., Bray J.W. — *Rock Slope Engineering*, 3rd ed., 1981
- Rocscience — *RocPlane Theory Manual*, Toronto
- Clouterre — *Recommandations Clouterre 1991/1993*
- FHWA — *Soil Nail Walls Reference Manual*, FHWA-NHI-09-035 (2009)
- Bustamante M., Doix B. — *Une méthode pour le calcul des tirants et des micropieux injectés*, 1985
- NTC 2018 — Decreto Ministeriale 17 gennaio 2018
- Circolare Ministeriale n. 7 del 21 gennaio 2019
- EN 1997-1 — Eurocodice 7
