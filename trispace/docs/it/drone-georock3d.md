# Drone → GEOROCK3D — wizard a 4 step

Il **wizard** di Trispace è dedicato al workflow specifico del passaggio
**rilievo drone / scanner 3D → GEOROCK3D** (analisi di caduta massi
GeoStru desktop). 4 step guidati, output formato `.txt` direttamente
caricabile in GEOROCK3D.

## Quando usarlo

Sei nel caso d'uso classico:

- Hai una **nuvola di punti LiDAR** o **fotogrammetria drone** del versante
  da analizzare per caduta massi
- Devi convertirla in un **DTM puntuale** della pendice (no vegetazione,
  no edifici, solo terreno)
- L'output deve andare in **GEOROCK3D** (modulo `Forms/ImportaPunti.cs`,
  formato `id;X;Y;Z` testuale)

Il wizard ti porta dalla nuvola raw al `.txt` pronto in 4 click.

## Apertura

Toolbar → **File → Wizard Drone → GEOROCK3D**, oppure riga AI
`wizard georock`, oppure si apre **automaticamente** quando fai drop di un
LAS e clicchi *"Vai al wizard"* nel pannello import LAS.

## Step 1 — Importa nuvola

Drop di un file `.las` o `.laz` nel wizard. Vedi:

- **Numero punti totali** (es. 1 850 000)
- **Range Z** (quota minima e massima)
- **Distribuzione classification ASPRS** (un istogramma che mostra quanti
  punti per classe)

Se la nuvola è già **classificata**, il wizard ti suggerisce automaticamente
*"Filtra solo classe 2 (Ground)"* — passa a Step 2.

Se la nuvola **non è classificata** (tutti in classe 0 o 1), salta direttamente
allo Step 3 (decimazione).

## Step 2 — Filter classification

Spunta le classi che vuoi mantenere:

- ✅ Ground (2) — **sempre**, è il terreno
- ❌ Vegetation (3, 4, 5) — togli, è rumore per GEOROCK3D
- ❌ Building (6) — togli
- ❌ Noise (7) — togli, sempre

Il contatore mostra in tempo reale **quanti punti restano** dopo il filter.
Tipicamente per una zona montana con vegetazione, scendi da 1.8M a 200-400k.

## Step 3 — Decima

GEOROCK3D **non ha bisogno** di milioni di punti — l'analisi caduta massi
funziona bene con 5 000 - 30 000 punti del DTM.

Il wizard offre 3 preset:

| Preset | Punti target | Quando usarlo |
|---|---|---|
| **Veloce** | 5 000 | Verifica preliminare di area |
| **Standard** | 15 000 | Caso comune, buon compromesso |
| **Dettaglio** | 30 000 | Versante critico, alta precisione |

Decimazione **voxel-grid uniforme**: divide lo spazio in celle e tiene un
punto per cella, garantendo distribuzione omogenea.

## Step 4 — Esporta

Output finale: file `.txt` di testo nel formato GEOROCK3D:

```
1;142.355;87.521;124.6
2;145.812;89.225;124.8
3;148.430;90.717;125.0
...
```

- **id** progressivo
- **X, Y** in coordinate metriche locali (East, North) — se la nuvola era
  georeferita le coordinate sono già metriche
- **Z** quota
- Separatore `;` (punto e virgola)
- Encoding ASCII

Click **Scarica `.txt`** → il browser scarica `cloud_decimato.txt`.

## Carica in GEOROCK3D

In **GEOROCK3D** desktop (versione Windows):

1. **File → Importa punti**
2. Seleziona il `.txt` esportato
3. GEOROCK3D legge i punti, calcola il DTM, ti porta nella scena 3D

Da lì procede con la simulazione caduta massi (parametri di lancio dei
blocchi, coefficienti di restituzione, raggio del blocco, ecc.) — ma quello
è il workflow di GEOROCK3D, vedi il suo manuale dedicato.

## Bypass del wizard

Se preferisci i comandi diretti:

1. Drop LAS → pannello import LAS standard
2. Filter classe 2 + decima 15000
3. Importa nel CAD
4. Riga AI: `esporta georock3d` → scarica `.txt`

Il risultato è identico al wizard, solo con più passaggi manuali.

## Limiti

- Il wizard funziona **solo con LAS** (non DXF, non CSV)
- L'output GEOROCK3D è **solo punti** — niente classification, niente colori
- GEOROCK3D si aspetta coordinate metriche: se la tua nuvola è in WGS84
  geografica (lat/lon), Trispace fa la conversione UTM automatica al drop

## Roadmap futura

Stiamo lavorando per:

- **Wizard dedicato per scanner Matterport** (`.glb` / `.obj` mesh →
  punti decimati)
- **Edit ground** dentro Trispace (rifinitura manuale dei punti scartati
  prima dell'export)
- **Volume di blocco di prova** stimato dalla mesh (input GEOROCK3D)

---

## Vedi anche

- [Importa file](importa.md) — formati LAS/LAZ in dettaglio
- [Mesh + curve](mesh-triangolazione.md) — generazione DTM dalla nuvola
- [Esportazioni](esportazioni.md) — altri formati di export

---

*Pagina utile? [Scrivici](mailto:info@geostru.ai?subject=Help%20Trispace%20NX%20-%20Drone%20GEOROCK3D).*
