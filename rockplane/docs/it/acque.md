# Acque

RockPlane modella **tre regimi idraulici** distinti che possono coesistere sullo stesso versante.

## Hw — acqua esterna al piede (ponded)

Livello idrostatico **esterno** al versante (lago, ristagno, falda di valle che lambisce il piede). Genera una spinta orizzontale sul fronte del versante.

| Simbolo | Significato                          | Unità | Default |
|---------|--------------------------------------|-------|---------|
| Hw      | livello acqua al piede               | m     | 0       |
| γw      | peso volume dell'acqua               | kN/m³ | 9.81    |

**Effetto sul cuneo**: forza U<sub>p</sub> normale al fronte (direzione +sin β, −cos β), che entra come azione attiva nei termini F<sub>x</sub>/F<sub>y</sub> dell'equilibrio. Può essere **stabilizzante** (preme contro il fronte → aumenta N) o **destabilizzante** se associata ad acqua interna (vedi sotto).

Sul disegno 2D, compare il simbolo CAD **∇** con l'etichetta `Hw = X.XX m` al livello indicato.

## Zw — acqua nella discontinuità (uplift sul piano)

Acqua **interna** alla frattura, che genera pressione interstiziale `u(s)` distribuita lungo il piano di rottura e quindi una sottospinta **U** normale al piano.

| Simbolo       | Significato                          | Unità | Default |
|---------------|--------------------------------------|-------|---------|
| Zw            | acqua nella discontinuità            | m     | 0       |
| Distribuzione | forma di u(s) sul piano              | enum  | Assente |

### Forme di distribuzione disponibili

| Valore | Descrizione                                                                                                |
|--------|------------------------------------------------------------------------------------------------------------|
| Assente | Nessuna pressione (anche se Zw > 0 nessuna sottospinta calcolata; usato per disattivare il termine)         |
| Triangolare · max a metà altezza | u = 0 al piede e in cima, picco a metà — caso classico Hoek-Bray con drenaggio bilanciato |
| Triangolare · max al piede | u = γw·Zw al piede, 0 in cima (eq. 20 manuale) — caso conservativo con drenaggio in sommità         |
| Triangolare · max alla base della fessura | u = picco al piede della TC, 0 al piede del piano — quando la TC è il principale ingresso d'acqua |

**Effetto sul cuneo**: la sottospinta **U** riduce la tensione normale efficace sul piano → riduce l'attrito mobilitato → FS diminuisce. È l'effetto destabilizzante più rilevante in molti casi pratici.

Sul disegno 2D, il piano di rottura mostra una sovrapposizione blu con freccette di pressione perpendicolari al piano, lunghezza proporzionale alla pressione locale, e una linea che chiude il poligono triangolare della distribuzione.

## Versante pervio

Toggle opzionale: se attivo, **acqua esterna (Hw) e acqua nella frattura (Zw) sono idraulicamente connesse**, cioè Zw = Hw al piede e segue la stessa quota. In questo caso anche con Zw=0 il software usa Hw come livello di sottospinta sul piano (distribuzione "max al piede").

Tipico per ammassi rocciosi molto fratturati con buona conduttività idraulica.

## Zt — acqua nella tension crack

Quando la fessura di trazione è attiva e contiene acqua (es. dopo piogge intense), genera una forza **V** sulla TC.

Direzione: perpendicolare alla TC, entrante nel cuneo. Componenti:
$$ V_x = -V \cdot \sin \theta, \quad V_y = +V \cdot \cos \theta $$

Il livello di acqua nella TC è derivato automaticamente da Zw: se Zw supera il piede della fessura (Dy), Zt = Zw − Dy con clamp a Cy.

## Sommario delle azioni idrauliche

| Termine | Origine          | Direzione                          | Effetto su FS |
|---------|------------------|------------------------------------|---------------|
| U<sub>p</sub> (ponded) | Hw esterna  | ⟂ al fronte, verso monte           | stabilizzante (di solito) |
| U (uplift sul piano)    | Zw interna  | ⟂ al piano, verso il cuneo         | **destabilizzante** |
| V (TC)                  | Zt nella TC | ⟂ alla TC, verso il cuneo          | **destabilizzante** |

## Coefficienti parziali NTC

NTC §6.2.2: le **pressioni interstiziali u** non sono moltiplicate da γ<sub>G</sub>; entrano nel calcolo come grandezze caratteristiche. RockPlane segue questa convenzione.

## Sul disegno 2D

- **∇** simbolo CAD per Hw
- Linea orizzontale tratteggiata blu al livello Hw
- Overlay blu spesso sul tratto bagnato del piano (per Zw > 0)
- Poligono triangolare con freccette perpendicolari per la distribuzione di pressione
- Etichetta `Zw = X.XX m` sopra il picco della distribuzione
- Per Zt: overlay sulla TC con freccette perpendicolari + label Zt

## Esempio pratico

| Caso                                                | Hw  | Zw  | Distribuzione         | Effetto su FS atteso |
|-----------------------------------------------------|-----|-----|-----------------------|----------------------|
| Versante asciutto (estate)                          | 0   | 0   | Assente               | massimo              |
| Versante con falda stabile bassa                    | 0   | 5   | Max al piede          | Δ FS ≈ −5%           |
| Versante post-pioggia con drenaggio                 | 0   | 10  | Max a metà altezza    | Δ FS ≈ −7%           |
| Lago di valle + acqua intrappolata in frattura      | 8   | 15  | Max al piede          | Δ FS ≈ −10%          |
| Tension crack riempita + pioggia                    | 0   | 25  | Max base TC           | Δ FS ≈ −15%          |
