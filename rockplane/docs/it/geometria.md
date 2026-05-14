# Geometria del cuneo

RockPlane lavora sul **cuneo bidimensionale** tra fronte del versante (slope face), piano sommitale (bench) e piano di rottura (failure plane), eventualmente delimitato da una fessura di trazione (tension crack).

## Schema convenzionale

Convenzione del manuale teorico Hoek-Bray (RocPlane):

```
                            C  (sommità del piano)
                           /|
              B───────────/ |
             /\          /  |
            / β\        / α |
           /    \      /    |  H
          /      \    /     |
         /        \  /      |
        /          \/       |
       O ──────────────────-+
       │ piede versante
       │ X positivo verso monte
       │ Y verticale
```

- **O** = (0, 0) — piede del versante (origine)
- **X positivo** = verso monte (rock intact)
- **Y positivo** = verticale verso l'alto
- Il cuneo scivola lungo OC nella direzione **(−cos α, −sin α)** (basso-valle)

## Parametri di input

| Simbolo | Nome esteso                                    | Unità | Vincolo            | Default |
|---------|------------------------------------------------|-------|--------------------|---------|
| H       | altezza del versante                            | m     | > 0                | 30      |
| β       | inclinazione del fronte                         | °     | 0 < β ≤ 90         | 60      |
| α       | inclinazione del piano di rottura              | °     | 0 < α < β          | 35      |
| ψ       | inclinazione del piano sommitale                | °     | ψ ≥ 0              | 0       |
| B       | profondità del blocco (⟂ alla sezione)          | m     | ≥ 0.1              | 5       |

!!! warning "Condizione cinematica"
    Il vincolo **α < β** (daylighting) è il prerequisito per la failure planare. Se α ≥ β, il software restituisce un errore "Cinematica non ammissibile".

## Tension crack (caso B)

Quando presente, sposta il vertice C in **D** e introduce una fessura di trazione che limita superiormente il piano di rottura.

```
              D────fessura────C  (sommità bench)
             /│              /
            / │             /
           /  │θ           /
          /───┘           /
         /  piano rottura
        /
       O
```

| Simbolo | Significato                                    | Vincolo            | Default |
|---------|------------------------------------------------|--------------------|---------|
| T       | distanza fessura dal ciglio B                  | > 0                | 0       |
| θ       | inclinazione della fessura dall'orizzontale    | 0 < θ ≤ 90         | 90 (verticale) |

Per attivare la fessura, spunta il toggle **"Fessura di trazione"** nella card Geometria. La presenza di Zt (acqua nella fessura) genera la forza **V** sulla TC.

## Output geometrici calcolati

Nel pannello destro **"Geometria calcolata"** vedrai:

| Simbolo  | Descrizione                                                  | Formula                                          |
|----------|--------------------------------------------------------------|--------------------------------------------------|
| N        | lunghezza fronte versante                                    | H / sin β                                        |
| L        | lunghezza piano di rottura                                   | H·(1 − cot β·tan ψ) / (sin α − cos α·tan ψ)      |
| M        | lunghezza piano sommitale                                    | (L·cos α − H·cot β) / cos ψ                      |
| Q        | lunghezza fessura di trazione                                | 0 (caso A) · da eq. (17) in caso B               |
| Area     | area del cuneo per metro                                     | ½·\|Bx·Cy − By·Cx\| (caso A)                     |
| Peso W   | peso per metro lineare di cresta                             | γ · Area                                         |

Sia "per sezione" che "totale × B" (per dimensionare interventi a metro lineare).

## Vincolo di profondità B

`B` è la **dimensione ortogonale alla sezione** disegnata (profondità in direzione della cresta). Tutti i calcoli interni di RockPlane lavorano "per metro" (kN/m); B serve a scalare i risultati a **forze totali** (kN).

!!! note "Quando ha senso usare B > 1"
    Quando il blocco roccioso è chiaramente delimitato lateralmente (es. due discontinuità subverticali isolano un cuneo di larghezza ~5 m), usare B = 5 m dà le forze totali sul blocco reale. Quando il fronte è esteso, B = 1 m e si ragiona "a corsia".

## Convenzione di orientamento

Il viewer 2D usa la convenzione **mirrorX=false** (X crescente da sinistra a destra). Il fronte del versante (slope face OB) è disegnato sulla **sinistra**, il piano di rottura (OC) sulla **destra-bassa**. Il cuneo OBC scivola verso il **basso-sinistra** (valle).

Vedi anche [Modello teorico](modello-teorico.md) per le equazioni complete (1)–(9).
