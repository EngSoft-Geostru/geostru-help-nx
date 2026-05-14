# Materiale (Mohr-Coulomb)

I parametri di resistenza al taglio sul piano di rottura sono modellati con il criterio classico di **Mohr-Coulomb**:

$$ \tau = c' + \sigma_n \cdot \tan \varphi' $$

dove τ è la resistenza al taglio mobilitata, σ<sub>n</sub> la tensione normale efficace sul piano, c' la coesione efficace e φ' l'angolo d'attrito efficace.

## Parametri di input

| Simbolo | Nome esteso                          | Unità  | Default | Note                                       |
|---------|--------------------------------------|--------|---------|--------------------------------------------|
| γ       | peso volume del blocco               | kN/m³  | 26      | Tipico per roccia integra (calcari, graniti) |
| c       | coesione sul piano di rottura        | kPa    | 0       | Spesso nulla su discontinuità persistente  |
| φ       | angolo d'attrito sul piano           | °      | 35      | Tipico 25°–45° per superfici di taglio    |

!!! note "Peso volume del blocco (non della roccia matrice)"
    Si usa γ del **cuneo come unità**, che può differire dalla roccia matrice se il blocco è alterato/fratturato. Per blocchi integri γ = 26-28 kN/m³ (calcari), 24-26 (arenarie), 26-28 (graniti).

## Coesione sulle discontinuità

Su superfici di taglio reali la coesione efficace è spesso **bassa o nulla**. Valori tipici da letteratura (Hoek-Bray):

| Tipo di discontinuità                                   | c' [kPa]    | φ' [°]   |
|---------------------------------------------------------|-------------|----------|
| Superficie persistente liscia (giunto piano)            | 0 – 5       | 20 – 30  |
| Superficie persistente rugosa (asperità di basso ordine)| 5 – 30      | 25 – 35  |
| Superficie con asperità di alto ordine non infrante     | 50 – 200    | 35 – 50  |
| Materiale di riempimento (argilla, silt)                | 0 – 50      | 10 – 25  |

Per casi di studio, si raccomanda di **partire conservativo** (c' bassa, φ' caratteristico minimo) e confrontare con i risultati di prove triassiali / direct shear se disponibili.

## Angolo d'attrito

φ' è l'angolo d'attrito **sul piano di rottura**, NON quello della roccia intatta. Per superfici di taglio:

- **Liscia** (giunto persistente sigillato): φ' ≈ φ<sub>basic</sub> della roccia matrice (es. 30° calcari, 35° graniti)
- **Rugosa** (asperità non infrante): φ' = φ<sub>basic</sub> + i  (criterio di Patton: i = angolo di dilatanza)
- **Riempita** (gouge / argilla): φ' tipico del riempimento, molto basso

Convenzionalmente in fase di pre-dimensionamento si usa il **basic friction angle** della roccia.

## Coefficienti parziali NTC / EC7

I valori inseriti in input sono **caratteristici** (X<sub>k</sub>). I valori di **progetto** (X<sub>d</sub>) usati nel calcolo dipendono dall'approccio normativo:

| Approccio                         | γ<sub>φ'</sub> | γ<sub>c'</sub> | γ<sub>γ</sub> | Valori di progetto usati |
|-----------------------------------|---------------:|---------------:|---------------:|--------------------------|
| Caratteristico (γ=1)              | 1.00           | 1.00           | 1.00           | tan φ' · c' · γ          |
| NTC 2018 (M2)                     | **1.25**       | **1.25**       | 1.00           | tan φ' / 1.25 · c' / 1.25 |
| EC7 DA1 Comb. 1 (M1)              | 1.00           | 1.00           | 1.00           | come caratteristico      |
| EC7 DA1 Comb. 2 (M2)              | 1.25           | 1.25           | 1.00           | come NTC                 |
| EC7 DA2 (M1)                      | 1.00           | 1.00           | 1.00           | come caratteristico      |
| EC7 DA3 (M2)                      | 1.25           | 1.25           | 1.00           | come NTC                 |

Il peso volume γ resta sempre invariato (γ<sub>γ</sub> = 1.00 in tutti gli approcci).

[Vedi tabella completa coefficienti applicati →](verifica.md)

## Esempio di lettura

Con input:
- c = 50 kPa
- φ = 30°
- Approccio NTC 2018

Il software calcola usando:
- c<sub>d</sub> = 50 / 1.25 = **40 kPa**
- tan φ<sub>d</sub> = tan 30° / 1.25 = 0.462 → φ<sub>d</sub> = **24.8°**

I valori "di calcolo" applicati sono sempre visibili nella scheda **"γ applicati"** sotto il selettore Normativa.
