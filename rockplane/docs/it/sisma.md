# Sisma pseudostatico

L'analisi sismica è condotta in **pseudostatica** secondo NTC 2018 §3.2 / §7.11.3 e EN 1998 (Eurocodice 8), applicando al cuneo una forza inerziale proporzionale al peso W.

## Formulazione

Per pendii naturali (NTC §7.11.3), la forza sismica orizzontale è:

$$ S_h = k_h \cdot W $$

dove `k_h = β_s · a_max / g` con:
- a<sub>max</sub> = accelerazione massima di sito da spettro NTC
- g = 9.81 m/s² (accelerazione di gravità)
- β<sub>s</sub> = coefficiente di riduzione tabellato (NTC Tab. 7.11.I, generalmente 0.18-0.32)

Opzionalmente si considera una componente verticale:

$$ S_v = k_v \cdot W \quad \text{con} \quad k_v = \pm 0.5 \cdot k_h $$

## Parametri di input

| Simbolo  | Nome esteso                                | Unità | Default |
|----------|--------------------------------------------|-------|---------|
| α<sub>s</sub> = k<sub>h</sub> | coefficiente sismico orizz. | -     | 0       |
| Ω        | direzione del sisma (dall'orizzontale)     | °     | 0       |

!!! note "Convenzione di Ω"
    Ω = 0° → forza orizzontale verso valle (destabilizzante).
    Ω = 90° → forza verticale verso il basso (additiva a W).
    Ω = −90° → forza verticale verso l'alto (riduce N effettiva).

## Componenti applicate

Dalla formulazione del manuale teorico (eq. 26-27), il modulo S<sub>modulo</sub> = W · α<sub>s</sub> · γ<sub>E</sub> viene scomposto:

$$ S_x = -S_{modulo} \cdot \cos \Omega, \quad S_y = -S_{modulo} \cdot \sin \Omega $$

con γ<sub>E</sub> = 1.0 (NTC §3.2.4, EC8).

!!! warning "Peso usato nel calcolo S"
    Il peso W usato per calcolare S = k<sub>h</sub>·W è il peso **caratteristico** (γ<sub>G</sub> non applicato sul termine sismico). Questa è la prassi NTC §7.11.3: l'azione sismica si valuta sul peso effettivo, non sul peso di calcolo amplificato.

## Effetto sul calcolo

Il sisma orizzontale (Ω = 0):
- Aumenta |F<sub>x</sub>| → aumenta |S motore| → riduce FS
- Riduce N → riduce attrito mobilitato → riduce τ → riduce FS

Tipico decremento di FS al variare di k<sub>h</sub>:

| k<sub>h</sub> | Δ FS per α=30°, β=60°, c=50, φ=30°, H=30 |
|---------------|------------------------------------------|
| 0.05          | −0.10                                    |
| 0.10          | −0.20                                    |
| 0.15          | −0.30                                    |
| 0.20          | −0.40                                    |

## Wizard sismico NTC (in roadmap)

In una versione futura del software, sarà possibile calcolare automaticamente k<sub>h</sub> a partire da:
- Zona sismica del Comune (lat/lon dalla card Dati generali)
- Categoria di sottosuolo (A, B, C, D, E)
- Classe d'uso (II/III/IV)
- Vita nominale (50/75/100 anni)

Per ora il progettista inserisce manualmente k<sub>h</sub> ricavato da analisi di pericolosità sismica del sito.

## Avvisi e diagnostica

Se k<sub>h</sub> è impostato e il blocco scende sotto FS = 1.0, compare un avviso esplicito nella sezione "Avvisi" del pannello risultati.

## Quando il sisma non è governante

Se la verifica è già **non soddisfatta** in condizioni statiche (FS < FS<sub>req</sub>), il sisma non è il problema principale — serve un intervento di consolidamento di base.

Se al contrario in statica FS >> FS<sub>req</sub> ma in dinamica scende sotto la soglia, il sisma è governante e l'intervento deve dimensionarsi per quello.

## Riferimenti

- NTC 2018 §3.2, §7.11.3, Tab. 7.11.I
- EN 1998-5 (Eurocodice 8 — fondazioni, opere di sostegno, aspetti geotecnici)
- Newmark N.M. (1965) — Effects of earthquakes on dams and embankments
