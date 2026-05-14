# Approccio normativo

RockPlane consente di scegliere l'**approccio di verifica**: calcolo caratteristico (γ=1) per controlli numerici, NTC 2018 italiano, o uno dei quattro Eurocodice 7 Design Approaches.

## Selettore

In alto, nella card **"Dati generali"**, c'è il selettore "Normativa". Cambia in tempo reale i coefficienti applicati al calcolo.

## Tabella coefficienti

| Approccio                     | γ<sub>G</sub> | γ<sub>Q</sub> | γ<sub>φ'</sub> | γ<sub>c'</sub> | γ<sub>R</sub> | FS<sub>req</sub> | Set     |
|-------------------------------|--------------:|--------------:|---------------:|---------------:|--------------:|------------------:|---------|
| **Calcolo caratteristico (γ=1)** | 1.00       | 1.00          | 1.00           | 1.00           | 1.00          | **1.30** (modificabile) | TA      |
| **NTC 2018 — A2+M2+R2**        | 1.00          | **1.30**      | **1.25**       | **1.25**       | **1.10**      | 1.10              | A2+M2+R2 |
| EC7 DA1 Comb. 1 (A1+M1+R1)    | **1.35**      | **1.50**      | 1.00           | 1.00           | 1.00          | 1.00              | A1+M1+R1 |
| EC7 DA1 Comb. 2 (A2+M2+R2)    | 1.00          | 1.30          | 1.25           | 1.25           | 1.00          | 1.00              | A2+M2+R2 |
| EC7 DA2 (A1+M1+R2)            | **1.35**      | **1.50**      | 1.00           | 1.00           | **1.10**      | 1.10              | A1+M1+R2 |
| EC7 DA3 (A2+M2+R3)            | 1.00          | 1.30          | 1.25           | 1.25           | 1.00          | 1.00              | A2+M2+R3 |

γ<sub>E</sub> (sisma) = 1.00 in tutti gli approcci.

## Chip dei coefficienti applicati

Sotto il selettore, una barra di chip mostra in tempo reale i valori effettivi:

```
γ APPLICATI:  γG 1.00   γQ 1.30   γφ' 1.25   γc' 1.25   γR 1.10   FSreq 1.10
```

- Chip **verde** = valore unitario (1.00) → coefficiente "neutro"
- Chip **bianco** = valore > 1 → riduzione/amplificazione applicata

## Come scegliere l'approccio

### Calcolo caratteristico (γ=1)

**Quando**: pre-dimensionamento, confronto con letteratura, verifiche numeriche, didattica. NON usare per progettazione esecutiva.

**Cosa significa**: tutti i coefficienti unitari (γ<sub>G</sub>, γ<sub>Q</sub>, γ<sub>φ'</sub>, γ<sub>c'</sub>, γ<sub>R</sub>). FS richiesto è quello classico (1.30 default, modificabile). Il calcolo produce l'**FS caratteristico**.

**FS richiesto modificabile**: nella stessa card puoi cambiare FS<sub>req</sub> (es. 1.50 per casi conservativi, 1.20 per casi temporanei).

### NTC 2018 (Approccio 1 Combinazione 2)

**Quando**: progettazione in Italia. È la combinazione prescritta da NTC §6.8.2 per stabilità pendii naturali.

**Cosa fa**: γ<sub>φ'</sub>=γ<sub>c'</sub>=1.25 (riduce i parametri di resistenza), γ<sub>R</sub>=1.10 (amplifica FS richiesto a 1.10), γ<sub>Q</sub>=1.30 (amplifica le azioni variabili). γ<sub>G</sub> resta a 1.00.

**Nota fronti di scavo**: per fronti di scavo NTC §6.8 prescrive γ<sub>R</sub>=1.20 invece di 1.10. RockPlane attualmente usa solo 1.10; per gli scavi vai a 1.20 manualmente impostando l'approccio "Caratteristico" e FS<sub>req</sub> = 1.20 / 1.0 = 1.20.

### EC7 DA3

**Quando**: progettazione internazionale. È l'approccio raccomandato dall'EN 1997-1 per stabilità globale.

**Cosa fa**: come NTC 2018 ma γ<sub>R</sub>=1.00 (e FS<sub>req</sub>=1.00).

### EC7 DA2

**Quando**: progettazione internazionale per fondazioni e opere di sostegno.

**Cosa fa**: γ<sub>G</sub>=1.35 (amplifica W, comprese le pressioni interstiziali ridotte attraverso N), γ<sub>R</sub>=1.10. Materiali con γ=1.

### EC7 DA1 Comb. 1 e Comb. 2

**Quando**: doppia verifica DA1 (entrambe le combinazioni devono essere soddisfatte).

**C1**: amplifica le azioni (γ<sub>G</sub>=1.35) ma non riduce i materiali. Critico per il dimensionamento strutturale (acciaio dei chiodi, sezione armatura).

**C2**: amplifica un po' le variabili (γ<sub>Q</sub>=1.30), riduce i materiali (γ<sub>φ'</sub>=γ<sub>c'</sub>=1.25). Critico per la stabilità geotecnica.

## Effetto di γ<sub>G</sub> sull'analisi

Con γ<sub>G</sub>=1.35 (DA1.C1, DA2), il peso W del cuneo viene **amplificato di 1.35x** nell'equilibrio:

- |S motore| aumenta di 1.35x (W·sin α amplificato)
- N aumenta di 1.35x → attrito aumenta di 1.35x
- Coesione c·L resta invariata

Effetto netto su FS:
- Caso **puro attrito (c=0)**: FS = tan φ/tan α invariato (W si cancella)
- Caso **con coesione (c>0)**: FS scende (la coesione "non si scala", il suo contributo diventa relativamente più piccolo)

## Effetto di γ<sub>φ'</sub>/γ<sub>c'</sub> su FS

Con γ=1.25 (NTC, DA1.C2, DA3):

- tan φ ridotto di 1.25 → contributo attritivo a τ scende di 1.25
- c ridotto di 1.25 → contributo coesivo a τ scende di 1.25
- FS scende **proporzionalmente**: FS<sub>NTC</sub> = FS<sub>caratteristico</sub> / 1.25 nel caso puro attrito

## Esempio comparativo

Parametri base: H=30, β=60°, α=30°, γ=26, c=50, φ=30°.

| Approccio                    | FS    | Δ vs caratteristico |
|------------------------------|------:|---------------------|
| Caratteristico               | 1.4441 | —                  |
| NTC 2018                     | 1.1553 | −0.29 (−20%)        |
| EC7 DA1.C1                   | 1.3290 | −0.12 (−8%)         |
| EC7 DA1.C2                   | 1.1553 | −0.29 (−20%)        |
| EC7 DA2                      | 1.3290 | −0.12 (−8%)         |
| EC7 DA3                      | 1.1553 | −0.29 (−20%)        |

Per progettazione in Italia: **NTC 2018** è la combinazione di riferimento. Per progettazione strutturale armature: anche **DA1.C1** (γ<sub>G</sub>=1.35) per dimensionare l'acciaio.

## Riferimenti

- NTC 2018 §6.2.4.1, §6.8.2, §6.8.6, Tab. 6.2.I, 6.2.II, 6.8.I
- Circolare Ministeriale n. 7/2019
- EN 1997-1, Annex A
- ISO 22476-3 — Geotechnical investigation and testing
