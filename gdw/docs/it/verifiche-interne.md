# Verifiche interne (fila per fila)

Oltre alle verifiche esterne globali del muro, GDW verifica la stabilità di
**ogni giunto orizzontale** tra una fila di gabbioni e quella superiore. Per
un muro di N file, ci sono N giunti da verificare (incluso quello tra fila 1
e fondazione/terreno).

## Quali verifiche

Ad ogni giunto i (dal basso, i = 0 è il giunto con la fondazione):

1. **Scorrimento parziale**: la porzione di muro sopra il giunto i non deve scorrere sul giunto.
2. **Ribaltamento parziale**: la stessa porzione non deve ribaltare attorno al lembo di valle del giunto.
3. **Tensioni σ_v, σ_m** sul giunto (lembo valle e monte): trazione/compressione del materiale.
4. **σ_max ≤ σ_adm** (solo per rete a doppia torsione): vedi sezione σ_adm sotto.

## Sezione di calcolo

Per ogni i, GDW:

1. Costruisce il **poligono parziale** del muro dalla fila i+1 alla sommità.
2. Calcola la spinta attiva su questa porzione (altezza = `(N − i) · h_gab`).
3. Calcola peso, baricentro, momenti.
4. Esegue le 4 verifiche sopra.

## Spinta parziale

Per i > 0 (giunti gabbione-gabbione):

- **Allineamento "a destra"**: la spinta è quella della stratigrafia (Coulomb completo) sull'altezza parziale.
- **Allineamento "a sinistra"**: la spinta è del **riempimento** a tergo (γ_riemp, φ_riemp), con δ = φ_riemp (contatto riempimento-gabbione).

Per i = 0 senza fondazione c.a.: spinta della stratigrafia + parametri del terreno di fondazione all'interfaccia.

## Verifica scorrimento/taglio parziale

Il check di scorrimento al giunto coincide con la verifica di **taglio
ammissibile** al giunto gabbione-gabbione:

$$
\tau_{adm} = N \cdot \tan(\varphi_g) + c_g \quad \Rightarrow \quad
FS_{scorr,i} = \frac{N_i \cdot \tan(\varphi_g) + c_g \cdot B_i}{\gamma_R \cdot F_{x,i}}
$$

con:

- N_i = peso parziale + componente verticale spinta = F_y,i (favorevole)
- φ_g = angolo attrito al giunto (per **rete DT** = 45° per default, per **ES** = formula 25·γ−10°)
- c_g = coesione apparente (per **DT** > 0 dal catalogo, per **ES** = 0)
- B_i = lunghezza del giunto (= base della fila i+1)
- F_x,i = forza orizzontale sollecitante

> **φ_g = 45°** è il valore raccomandato di letteratura per la doppia torsione: la
> coesione apparente già incorpora l'effetto del rivestimento e dell'orditura,
> quindi l'angolo di taglio interno gabbione-gabbione si assume di 45°
> indipendentemente dalla pietra. Se serve, è possibile passare alla modalità
> "manuale" e inserire un valore custom.

### Confronto DT vs ES

Per un giunto con N = 100 kN/m, F_x = 35 kN/m, B = 2 m:

| Rete | φ_g | c_g | R | FS (γ_R=1.1) |
|---|---|---|---|---|
| Elettrosaldata (γ=16) | 30° | 0 | 57.7 | 1.50 |
| **Doppia torsione 8×10** | **45°** | **3 kPa** | **106** | **2.75** |

→ La DT più che raddoppia il FS per via di φ_g maggiore + c_g.

## Verifica ribaltamento parziale

$$
FS_{rib,i} = \frac{M_{s,i}}{\gamma_R \cdot M_{r,i}}
$$

Stessa formula della verifica esterna, applicata alla porzione di muro sopra
il giunto, con pivot sul lembo di valle del giunto.

## Tensioni sul giunto

Le tensioni normali ai due lembi del giunto sono:

$$
\sigma_v = \frac{N}{B} \cdot (1 + 6e/B) \quad ; \quad \sigma_m = \frac{N}{B} \cdot (1 - 6e/B)
$$

con e = eccentricità della risultante dal baricentro del giunto. Per e < B/6,
σ_v e σ_m sono entrambe positive (giunto interamente compresso). Per e > B/6,
σ_v > 0 e σ_m < 0 (parzializzazione del giunto, parte del materiale in trazione
→ si "stacca" idealmente; la pressione si redistribuisce sulla larghezza utile).

GDW mostra σ_v e σ_m con dimensioni in **kPa**, e indica il **punto di
azzeramento** (distanza dal piede di valle dove σ = 0, se la giunzione è
parzializzata).

## σ_adm (solo per rete a doppia torsione)

**σ_adm = tensione normale ammissibile al giunto** tra due file di gabbioni.
Rappresenta il limite oltre il quale la rete metallica al contatto cede
(snervamento dei fili o apertura della "bocca" della cassa). Dipende da:
tipo maglia (8×10, 6×8 …), Ø filo, rivestimento, peso specifico del
riempimento γ_G. Tipicamente per 8×10 Ø 2.7 Zn forte vale 100÷300 kPa
secondo le tabelle del fornitore.

### Input dell'utente (campo editabile)

σ_adm è un **campo editabile** sotto "Coesione apparente" (visibile solo per
rete DT). Convenzioni:

| Valore inserito | Comportamento |
|---|---|
| **Vuoto** | GDW propone un default empirico (formula sotto) come stima iniziale |
| **= 0** | Verifica al giunto **omessa** (nessun badge ✓/✗ accanto alla riga σ_v · σ_m) |
| **> 0** | Valore di progetto, rispettato così com'è |

### Default empirico

Quando σ_adm non è inserito, GDW propone il valore di una formula empirica
di letteratura tecnica per gabbioni a doppia torsione:

$$
\sigma_{adm}\,[\text{tf/m}^2] = 50 \cdot \gamma_G[\text{tf/m}^3] - 30
$$

Convertita in kPa moltiplicando per 9.81:

$$
\sigma_{adm}\,[\text{kPa}] = (50 \cdot \gamma_G[\text{tf/m}^3] - 30) \cdot 9.81
$$

Per γ_G = 16 kN/m³ → γ_G = 1.63 tf/m³ → σ_adm ≈ **506 kPa**.

> **Nota storica.** Versioni precedenti di GDW omettevano il fattore 9.81 e
> producevano σ_adm dell'ordine di 50 kPa, troppo basso e causa di falsi
> negativi. La formula è stata allineata alla letteratura tecnica (tf/m² → kPa).

### Verifica

$$
\sigma_{max} = \max(|\sigma_v|, |\sigma_m|) \leq \sigma_{adm}
$$

Per rete elettrosaldata σ_adm non è applicabile (la formula empirica è specifica
per la DT). GDW non mostra il badge σ_adm per ES.

[Dettagli sulla rete DT →](rete.md)

## Verifica fila 0 (giunto base muro-fondazione)

Caso speciale:

- **Con fondazione c.a./cls** (h_v > 0): il giunto base muro/fondazione usa l'**attrito gabbione-cls** (`φ_g`) + **coesione gabbione** c_g (DT) o 0 (ES).
- **Senza fondazione** (h_v = 0): il giunto è muro/terreno → usa **φ_fond** e c_fond del terreno di fondazione.

Per cambiarlo: combo "Interfaccia alla base" (terreno / fondazione c.a. δ=2/3 φ / personalizzato).

## Visualizzazione

Pannello risultati → sezione **Verifiche interne**:

- Una riga per ogni fila (I, II, III, ...)
- 4 colonne: FS_rib · FS_scorr · σ_v · σ_m + badge ✓/✗ a destra
- Per ogni ✗ rosso: popover con consigli (riduci shift, aumenta blocchi della fila, ancora i gabbioni, ...)
- Quando attiva la DT: extra badge ✓/✗ per σ_max ≤ σ_adm

Sul disegno della sezione:

- Bande **verdi tratteggiate** orizzontali ad ogni giunto: trapezio tensione σ_v → σ_m
- Banda **rossa** sul giunto base (i = 0): trapezio tensione fondazione
- Pallino rosso/verde nel punto di azzeramento σ = 0 (se giunto parzializzato)

## Vedi anche

- [Rete metallica (DT vs ES)](rete.md) — φ_g, c_g, σ_adm
- [Verifiche esterne](verifiche.md) — calcolo globale
- [Geotecnica](geotecnica.md) — interfaccia alla base
