# Stereonet — glossario visuale

Lo **stereonet** (o reticolo stereografico) è la rappresentazione
bidimensionale dell'orientazione 3D dei piani di discontinuità: ogni
piano diventa un punto (il **polo**) o una linea curva (la
**ciclografica**) sul disco.

Questa pagina spiega *cosa* vedi sul disco di GMS NX e *come*
interpretarlo.

## Anatomia del disco

```
                 N (0°)
                  │
                  │
         NW ┌─────┼─────┐ NE
            │           │
     W ─────┤  ◯  ◯  ◯  ├───── E (90°)
            │           │
         SW └─────┼─────┘ SE
                  │
                  │
                 S (180°)
```

- **Cerchio esterno** — orizzontale (inclinazione 0°)
- **Centro del cerchio** — verticale (inclinazione 90°)
- **N, E, S, W** — Nord, Est, Sud, Ovest
- **Reticolo curvo interno** — meridiani e paralleli stereografici, a
  passo 10° o 20° (configurabile)

## Tipi di proiezione

Toolbar dello stereonet → toggle proiezione:

### Schmidt-Lambert (equiarea, default)

La proiezione **conserva le aree**: la densità dei poli sul disco
corrisponde alla densità reale dei piani. È la proiezione standard per
l'**analisi statistica** (isodensità Denness, k-means).

### Wulff (equiangola)

La proiezione **conserva gli angoli**: i meridiani sono archi di
cerchio. Più adatta per la **costruzione geometrica** classica
(intersezioni a mano, ribaltamenti).

### Polare ↔ Equatoriale

Il toggle commuta il reticolo di sfondo:

- **Equatoriale** — meridiani verticali, paralleli orizzontali
- **Polare** — reticolo a "clessidra" o "occhio" (tipico di alcuni
  software desktop italiani)

!!! warning "Nomenclatura GMS"
    In GMS web la nomenclatura *Polare/Equatoriale* è invertita
    rispetto alla matematica standard, **per parità con il GMS desktop
    GeoStru**. Se conosci la convenzione accademica, ricordati che qui
    "Polare" produce il reticolo "occhio" (non il reticolo polare
    classico).

### Emisfero inferiore (default) ↔ superiore

Ai sensi delle convenzioni di geologia strutturale, lo standard è
**emisfero inferiore**: i poli puntano verso il basso, le ciclografiche
mostrano l'intersezione del piano con l'emisfero inferiore della sfera.
L'emisfero superiore è disponibile per chi viene da campi diversi
(cristallografia, geofisica) o per confronti con plot pubblicati in
quella convenzione.

## Elementi grafici

### 1. Polo di un piano (puntino)

Un **piano** è rappresentato sul disco come un singolo punto: il
**polo**, ovvero il punto in cui la **normale al piano** interseca
l'emisfero inferiore.

- **Posizione del polo**:
  - distanza dal centro proporzionale a `(90° - α)`
    (polo al centro = piano orizzontale, polo sul cerchio = piano
    verticale)
  - azimut a partire dal Nord = `β + 180°`

GMS colora i poli **per famiglia** (verde / blu / arancio / viola / …)
secondo la classificazione automatica (k-means) o manuale.

### 2. Ciclografica del pendio (curva rossa)

La **ciclografica** è la proiezione 2D del piano di un piano stesso.
Per il **pendio** è disegnata in **rosso pieno**, con un'etichetta
`Pendio α/β°`.

I cinematismi instabili coincidono con i poli/intersezioni che cadono
**all'interno** della ciclografica del pendio (zona pericolosa di
Markland).

### 3. Ciclografiche delle famiglie (curve colorate)

Per ogni famiglia (manuale o k-means), GMS disegna la ciclografica del
**piano medio** (vettore di Fisher) in colore famiglia. La ciclografica
è marcata sul cerchio esterno con un piccolo trattino orientato
all'azimut β della famiglia.

### 4. Cono d'attrito (cerchio tratteggiato arancione)

Il **cono d'attrito** è un cerchio centrato nel disco di raggio
proporzionale a `(90° - φ)`. Tutti i poli **al di fuori del cono**
hanno inclinazione minore di φ ⇒ attrito sufficiente per la stabilità.
I poli **all'interno del cono** sono potenzialmente instabili (dip > φ).

### 5. α₉₅ Fisher (cerchietti tratteggiati)

Per ogni famiglia, attorno al polo medio Fisher viene disegnato un
piccolo **cerchio tratteggiato** di raggio `α₉₅`: è il **cono di
confidenza al 95%** in cui ricade il polo medio. Più stretto = più
serrato il cluster.

### 6. Cunei (⊗ rossi sulle intersezioni)

Per ogni coppia di famiglie GMS calcola l'**intersezione** dei due
piani (= retta di intersezione, rappresentata da un punto sullo
stereonet). Se la retta di intersezione:

- ha **plunge > φ** (più verticale dell'attrito) **e**
- il suo **trend** cade nel quadrante del pendio

allora il cuneo è **instabile** e GMS marca il punto con `⊗` rosso.
Vedi [Markland](markland.md) per il dettaglio.

### 7. Vista 3D (modalità *3D*)

Toggle **3D** in toolbar:

- La sfera unitaria viene mostrata in Three.js, con orbita libera
  (mouse / touch).
- I **piani** diventano **dischi semitrasparenti** della famiglia.
- Il **pendio** è un piano arancione semi-trasparente.
- I **cunei instabili** sono **prismi triangolari rossi**: la base è
  il triangolo formato dai 2 piani che si intersecano, il vertice
  scende lungo la retta di intersezione.

## Layer attivabili

Toolbar dello stereonet → menu **Layer**:

- **Poli singoli** — on/off
- **Ciclografiche pendio** — on/off
- **Ciclografiche famiglie** — on/off
- **Cono d'attrito** — on/off
- **α₉₅ Fisher** — on/off
- **Isodensità (Denness)** — on/off, scala di colori
- **Stella di immersione** — on/off (rosa polare delle β)
- **Cunei** — on/off (solo 3D)

---

## Letture consigliate

Per approfondire la geometria stereografica:

- **Goodman R.E. (1989)** — *Introduction to Rock Mechanics*, 2nd ed.
- **Hoek E. & Bray J.W. (1981)** — *Rock Slope Engineering*
- **Lisle R.J. & Leyshon P.R. (2004)** — *Stereographic Projection
  Techniques for Geologists and Civil Engineers*

---

## Vedi anche

- [Famiglie di discontinuità](famiglie.md) — k-means + Fisher
- [Test di Markland](markland.md) — interpretazione cinematica
- [Workflow completo](workflow.md) — lo stereonet nel ciclo intero

---

*Pagina utile? [Scrivici](mailto:info@geostru.ai?subject=Help%20GMS%20NX%20-%20Stereonet).*
