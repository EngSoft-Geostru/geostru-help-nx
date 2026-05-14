# Forza esterna E

Carico **non sismico** applicato al cuneo: carico stradale, sovrastruttura, opere di consolidamento esterne, accidentali.

## Convenzione RockPlane NX

RockPlane adotta una convenzione **intuitiva per il progettista**:

| δ      | Direzione               | Effetto su FS | Caso tipico                          |
|--------|-------------------------|---------------|--------------------------------------|
| 0°     | Orizzontale verso valle | **↓ destabilizza** | Spinta orizzontale verso il vuoto    |
| +90°   | Verticale verso il basso | **↓ destabilizza** (con c>0) | Carico stradale, sovrastruttura      |
| −90°   | Verticale verso l'alto   | ↑ stabilizza  | Tirante che solleva, carico in trazione |
| 180°   | Orizzontale verso monte  | ↑ stabilizza  | Spinta da opera di sostegno          |

Matematicamente: $E_x = -E \cos \delta$, $E_y = -E \sin \delta$ nel math frame (X positivo verso monte).

## Parametri di input

| Simbolo | Nome esteso              | Unità  | Default |
|---------|--------------------------|--------|---------|
| E       | modulo della forza       | kN/m   | 0       |
| δ       | inclinazione (vedi sopra) | °      | 0       |
| Tipo    | Permanente (G) / Variabile (Q) | enum | Permanente |

## Tipo carico — coefficiente parziale applicato

La distinzione **Permanente / Variabile** determina quale γ NTC/EC7 viene applicato:

- **Permanente (γ<sub>G</sub>)**: peso di sovrastrutture cementate, muri esistenti, sovraccarichi non rimovibili. γ<sub>G</sub> = 1.00 (A2) o 1.35 (A1).
- **Variabile (γ<sub>Q</sub>)**: carichi accidentali, traffico stradale, neve, vento. γ<sub>Q</sub> = 1.30 (A2 NTC) o 1.50 (A1 EC7).

L'utente sceglie tramite radio button. Default = Permanente.

## Punto di applicazione

Nella formulazione planare LEM, E è applicata al **baricentro G** del cuneo come risultante. Il **punto di applicazione NON entra nel calcolo di FS** perché si scrive solo l'equilibrio di traslazione (eq. 26-30), non quello rotazionale.

Sul disegno 2D la freccia di E è disegnata partendo da G, leggermente offsettata se ha direzione verticale (per non sovrapporsi a W).

## Effetto sul calcolo

Le componenti di E entrano in F<sub>x</sub>/F<sub>y</sub>:

- Aumentano |S motore| se hanno componente lungo (−cos α, −sin α)
- Modificano N (positivamente se la componente verticale è verso il basso, negativamente se verso l'alto)
- Variano τ resistente di conseguenza

### Esempio: carico stradale sull'alto del fronte

| Caso                                              | E [kN/m] | δ   | Effetto su FS |
|---------------------------------------------------|----------|-----|---------------|
| Senza carico                                      | 0        | —   | FS<sub>0</sub> |
| Carico permanente solo (es. muretto)              | 100      | 90° | FS quasi invariato (c=0) o leggero ↓ (c>0) |
| Carico variabile orizzontale (es. spinta cordolo) | 200      | 0°  | FS ↓ visibile |
| Tirante esterno applicato                         | 300      | −60° | FS ↑           |

## Avvisi automatici

Se E è significativo (>1 kN/m), il materiale è a coesione nulla (c < 0.1 kPa), e δ è quasi verticale (|sin δ| > 0.97), compare un avviso:

> *"Carico E quasi verticale su materiale con c=0: FS non risente di E. N e S motore crescono nella stessa misura (W+E)·cos α e (W+E)·sin α → FS = tan φ / tan α (indipendente da E). Per vedere effetto di un sovraccarico verticale impostare c > 0."*

Questo è un risultato matematico noto (manuale Hoek-Bray) — non un bug del programma.

## Confronto con il sisma

| Aspetto          | Sisma (kh)           | Forza esterna E       |
|------------------|----------------------|------------------------|
| Origine          | accelerazione del suolo | carico applicato esterno |
| Magnitude       | k<sub>h</sub> · W (proporzionale a W) | E fisso (indipendente da W) |
| γ applicato     | γ<sub>E</sub> = 1.00 (NTC §3.2.4) | γ<sub>G</sub> o γ<sub>Q</sub> a scelta |
| Direzione       | dall'orizzontale (Ω) | dall'orizzontale (δ) |

Per modellare un **sisma combinato con carico stradale**, usa entrambi i blocchi (Sisma + Forza esterna) — le forze si sommano vettorialmente nell'equilibrio.

## Sul disegno 2D

Freccia colore **arancione bruciato** (#b45309) partente dal baricentro G, con:
- Lunghezza scalata al modulo, con minimo visibile (15% larghezza versante per modulo piccolo)
- Etichetta `E = X kN/m`
- Offset orizzontale se direzione vicina a verticale (per non sovrapporsi a W)
