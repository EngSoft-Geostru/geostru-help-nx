# α critico (sweep)

Strumento di analisi parametrica per trovare l'**inclinazione α del piano di rottura che minimizza FS**, a parità di tutto il resto. Utile quando l'orientazione reale del giunto persistente non è conosciuta con precisione (dati geomeccanici scarsi).

## Come si usa

1. Nella card **Geometria del cuneo**, accanto al campo `α · inclinaz. piano rottura`, c'è un piccolo bottone **`α crit`**.
2. Clicca → il software esegue uno **sweep** automatico dell'inclinazione α nel range cinematicamente ammissibile.
3. Compare un banner blu sotto la riga geometrica:
   ```
   α crit ≈ 50.75° · FS_min = 0.944 (richiesto ≥ 1.10) · range [0.5°…69.5°]
   ```
4. Il campo α viene **aggiornato** al valore critico → il calcolo prosegue con quell'angolo come default.
5. Cambia colore del banner in base all'esito: 🟢 verde se FS<sub>min</sub> ≥ FS<sub>req</sub>, 🟡 giallo se ≥ 1.0, 🔴 rosso se < 1.0.

## Algoritmo

```
1. dominio = (max(0.5°, ψ+0.5°), β−0.5°)        ← cinematicamente ammissibile
2. sweep_coarse: α ∈ dominio, step 1°
3. argmin = α che minimizza FS sul sweep coarse
4. refine_local: α ∈ [argmin−1°, argmin+1°], step 0.05°
5. argmin_final = α che minimizza FS nel range raffinato
6. ritorna (argmin_final, FS_min)
```

Precisione finale: **0.05°** sull'angolo critico.

## Risultato

Il banner mostra:

| Campo                    | Significato                                              |
|--------------------------|----------------------------------------------------------|
| α crit ≈ X.XX°           | inclinazione del piano che minimizza FS                  |
| FS_min = X.XXX           | valore di FS al punto critico                            |
| richiesto ≥ X.XX         | FS soglia dell'approccio normativo selezionato           |
| range [X.X°…X.X°]        | dominio di sweep esplorato                               |

## Quando il minimo è interno e quando al bordo

A seconda dei parametri:

### Pure friction (c = 0)

$$ FS = \frac{\tan\varphi}{\tan\alpha} $$

Monotonicamente decrescente in α. Il minimo è **al bordo superiore** del dominio (α → β−0.5°), dove FS tende al valore più basso (perché tan α massimo).

Esempio: c=0, φ=35°, β=70° → α_crit ≈ 69.5°, FS_min = tan 35°/tan 69.5° ≈ 0.22.

### Con coesione (c > 0)

$$ FS = \frac{c \cdot L}{W \cdot \sin\alpha} + \frac{\tan\varphi}{\tan\alpha} $$

Il termine di coesione cresce all'aumentare di α (perché W cala più velocemente di L), mentre l'attrito decresce. C'è quindi un **minimo INTERNO** al dominio.

Esempio: c=50, φ=30°, β=70° → α_crit ≈ 50.75°, FS_min ≈ 0.94.

L'α critico in questo caso si stima con la formula approssimata $\alpha_{crit} \approx (\beta + \varphi) / 2$ (per c moderato), modulata dal peso relativo del termine coesivo.

## Interpretazione pratica

L'α critico è la **giacitura più sfavorevole** per la stabilità del pendio, dato il set di parametri di input. Serve per:

- **Studi parametrici**: capire la sensibilità di FS rispetto all'orientazione del giunto.
- **Backanalisi**: se conosci l'evento di rottura ma non l'esatta giacitura del piano, l'α critico ti dà la stima più conservativa.
- **Dimensionamento robusto**: progettare gli interventi per il caso α_crit (non per il valore nominale α inserito), così la verifica resta soddisfatta anche con incertezza geomeccanica.

## Limiti

- Il sweep varia solo α; β, ψ, c, φ, H restano fissi. Per varie le combinazioni serve un'analisi multi-parametro esterna.
- L'α critico è valido solo per **questa specifica geometria del versante**. Cambiando H o β si sposta.
- Se il dominio cinematico è degenere (β troppo piccolo, ψ vicino a β), il sweep può non trovare un minimo significativo. Compare allora un avviso.

## Su versanti reali

Il sweep è **istantaneo** (< 200 ms per il caso tipico) anche con geometria complessa e tutti gli interventi attivi. Puoi usarlo come "controllo finale" prima di esportare la relazione: ti dice il margine di sicurezza del tuo dimensionamento rispetto a un'incertezza sull'orientazione del giunto.

## Esempio numerico

| Parametri                                            | α_crit  | FS_min |
|------------------------------------------------------|--------:|-------:|
| H=30, β=70°, c=0, φ=30°                              | 69.50°  | 0.22   |
| H=30, β=70°, c=50, φ=30°                             | 50.75°  | 0.94   |
| H=30, β=70°, c=50, φ=30°, kh=0.15                    | 45.20°  | 0.69   |
| H=30, β=55°, c=20, φ=30°, ψ=5°                       | 43.65°  | 0.91   |
