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

## Vuoi aggiungere un tuo caso?

Se hai un caso interessante che vuoi condividere come esempio (anonimizzato), scrivici a [info@geostru.ai](mailto:info@geostru.ai?subject=Esempio%20RockPlane%20NX) allegando il file `.rockplane` salvato dal software.

In roadmap: una libreria pubblica di esempi categorizzati per tipologia di failure, normativa applicata, e tipo di intervento.
