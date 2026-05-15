# Risorse — file di esempio

Casi di studio pronti da scaricare e aprire nel software (menu **File → Apri da file…**). Sono utili per:

- **Familiarizzare** con i parametri tipici di un caso reale
- **Confrontare** i risultati di RockPlane NX con software legacy (SRS Geostru, RocPlane Rocscience)
- **Formazione** di nuovi utenti del software

## Come usare un esempio

1. Clicca sul link del file `.rockplane` qui sotto → scarica il file
2. Apri RockPlane NX da [nx.geostru.ai/rockplane/](https://nx.geostru.ai/rockplane/)
3. Menu **File → Apri da file…** e seleziona il file scaricato
4. Il progetto è subito caricato con tutti i parametri (geometria, materiale, acque, sisma, interventi, catalogo)
5. Modifica liberamente per esplorare il comportamento

## Esempi disponibili

### Zona 1 — Blocco 2 (parete in roccia carsica con TC e 5 file di chiodi)

[**📥 Scarica `zona-1-blocco-2.rockplane`**](samples/zona-1-blocco-2.rockplane)

**Caratteristiche del caso**:

| Parametro                | Valore       |
|--------------------------|--------------|
| Altezza versante H       | 11.31 m      |
| Inclinazione fronte β    | 70°          |
| Inclin. piano rottura α  | 15°          |
| Inclin. bench ψ          | 0° (orizzontale) |
| Profondità blocco B      | 8 m          |
| Tension crack            | T = 3 m, θ = 70° |
| Peso volume γ            | 22 kN/m³     |
| Coesione c               | 0 kPa        |
| Angolo d'attrito φ       | 38°          |
| Sisma kh                 | 0.08 (Ω = 0°) |
| Acqua nella TC (Zw)      | 10 m (max al piede) |
| Interventi               | 5 file di chiodi φ32, L=9m, Δ=15°, interasse 2.66 m |

**Geometria del cuneo calcolata**:
- Area: ~32.6 m² (per sezione)
- Peso: ~5740 kN (totale × B = 8 m)
- Baricentro G: (3.62, 5.87) m

**Origine**: caso documentato in una stampa legacy SRS Geostru, ricostruito in RockPlane NX per validare la coerenza tra il software desktop e la versione web NX. Utile come confronto numerico.

**Output atteso** (dopo aver aperto e ricalcolato):
- FS ≈ 1.6 con i 5 file di chiodi
- Senza chiodi (rimuovi gli interventi), FS scende verso 1.0–1.1 → la chiodatura è dimensionata correttamente.

---

### Blocco 7 — caso di validazione desktop (Barton-Bandis, 2 file di chiodi)

[**📥 Scarica `blocco-7.rockplane`**](samples/blocco-7.rockplane)

**Caratteristiche del caso**:

| Parametro                | Valore       |
|--------------------------|--------------|
| Altezza versante H       | 4.5 m        |
| Inclinazione fronte β    | 85° (quasi verticale) |
| Inclin. piano rottura α  | 45°          |
| Inclin. bench ψ          | 0°           |
| Profondità blocco B      | 4 m          |
| Tension crack            | no           |
| Criterio resistenza      | **Barton-Bandis** |
| Peso volume γ            | 22 kN/m³     |
| Coesione c               | 0 kPa        |
| Angolo d'attrito φ       | 38° (φb=32°) |
| JRC                      | 8            |
| JCS                      | 160 MPa      |
| Sisma kh                 | 0.08         |
| Acqua                    | nessuna      |
| Interventi               | 2 file di chiodi passivi φ32 in foro φ90, L=6 m, Δ=15°, passo orizz. 2 m, posizioni Yt=2.5 m e 4.0 m |
| Capacità singola         | 325 kN (tiro di progetto = η²·fy·A_gross) |

**Origine**: caso preso dalla **Validazione codice di calcolo desktop GeoStru RockPlane**. Riprodotto identicamente in RockPlane NX per il confronto numerico tra il software desktop e la versione web NX.

!!! note "Convenzione 'tirante passivo' nel desktop"
    Nel disegno del manuale di validazione desktop questi elementi sono etichettati come "tirante passivo", ma i tabulati li trattano come **chiodi** (analisi con chiodi). In RockPlane NX li modelliamo coerentemente come `ChiodoPassivo` con `TipoNtc = Chiodo`, comportamento di funzionamento del soil-nail (Variante A NTC §6.7).

**Output atteso** (dopo aver aperto e ricalcolato):
- FS ≈ 3.0 — il caso è sovra-dimensionato 2× rispetto al target NTC di 1.3 (margine ampio per geometria conservativa, fronte quasi verticale).
- I dimensionamenti delle resistenze sul singolo chiodo, se abilitato il calcolo NTC, devono allinearsi a:
  - **Forza limite ultima fondazione (Ta3)** ≈ 3360 kN (con σc = 30 MPa, π·90·6000·0.1σc / 2.16)
  - **Sfilamento acciaio-malta (Ta2)** ≈ 1622 kN (con τb = 2.69 N/mm², π·32·6000·τb)
  - **Resistenza ultima armatura (Ta1)** = 325 kN (= η²·fy·A_gross, con η=0.7, fy=826, D=32)

---

## Vuoi aggiungere un tuo caso?

Se hai un caso interessante che vuoi condividere come esempio (anonimizzato), scrivici a [info@geostru.ai](mailto:info@geostru.ai?subject=Esempio%20RockPlane%20NX) allegando il file `.rockplane` salvato dal software.

In roadmap: una libreria pubblica di esempi categorizzati per tipologia di failure, normativa applicata, e tipo di intervento.
