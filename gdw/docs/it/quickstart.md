# Quickstart — il tuo primo muro in 5 minuti

In 5 minuti vedi GDW NX al lavoro su un caso reale (muro 5 m a destra,
fondazione inclinata 10°, sisma assente). Niente da installare.

## 1. Apri l'app

Vai su [`nx.geostru.ai/gdw/`](https://nx.geostru.ai/gdw/) e fai login.

## 2. Carica l'esempio del cliente

In alto a destra clicca il **?** → tab **Risorse** → scarica
`esempio-muro-5m-fond-inclinata.gabbioni`. Poi **File → Apri…** e
seleziona il file.

In alternativa, imposta a mano questi valori:

| Sezione | Campo | Valore |
|---|---|---|
| Geometria | Numero file | **5** |
| Geometria | Blocchi per fila (dal basso) | **3 · 3 · 2 · 2 · 1** |
| Geometria | Allineamento | **A destra** |
| Geometria | Inclinazione muro α | 0° (per ora) |
| Fondazione | Base | **3.2 m** (esubero 0.1 m/lato) |
| Fondazione | Spessore valle h_v | **0.30 m** |
| Fondazione | Inclinazione β | **10°** (verso monte) |
| Geometria terreno | Inclinazione monte 1 | **25°**, lunghezza 8 m |
| Sisma | Normativa | **NTC 2018 (statica)** |
| Geotecnica spingente | γ, φ, c | **19 kN/m³ · 35° · 0** |
| Geotecnica fondazione | γ, φ, c | **19 kN/m³ · 32° · 0** |
| Gabbioni | Peso specifico, base, altezza, profondità | **16 kN/m³ · 1×1×1 m** |
| Rete | Tipologia | **Doppia torsione 8×10 Ø2.7** |

## 3. Calcola

Toolbar in alto → **Calcola** ⚡

In pochi secondi vedi:

- **3 FS principali**: ribaltamento, scorrimento (con base inclinata), capacità portante.
- **Verifiche interne fila per fila**: ribaltamento, scorrimento, e (per rete DT) σ_max ≤ σ_adm.
- **Disegno sezione** con strati, gabbioni, foundazione trapezoidale, diagramma pressioni attive.

!!! tip "Cosa è ogni numero?"
    Posiziona il mouse su qualsiasi badge ✓/✗ per il tooltip. Per le X rosse compare un popover con **consigli pratici** su come migliorare quella verifica (aumenta base, batti il muro, ecc.).

## 4. Sperimenta con l'inclinazione

Nella sezione **Geometria** prova a impostare **Inclinazione muro α = 8°**. Premi Calcola.

Vedrai:

- Il **preview SVG** si aggiorna in tempo reale con il muro inclinato verso monte (rotazione rigida)
- Il disegno principale **post-calcolo** mostra muro + fondazione + diagrammi tutti ruotati
- FS scorrimento e FS ribaltamento **migliorano** (la spinta viene proiettata su un piano inclinato, Sy verticale stabilizzante cresce)

[Vedi la teoria → Inclinazione del muro](inclinazione-muro.md)

## 5. Stabilità globale (Bishop)

In fondo alla pagina, sezione **Stabilità globale**:

- Lascia i 3 punti del cerchio su `auto` o impostali a mano (valle, monte, base)
- Premi il bottone **Stabilità globale**
- Vedi il cerchio critico sul disegno, FS, e log di calcolo

## 6. Esporta

Toolbar → **Report**:

- **Word `.docx`** — relazione tecnica completa con dati, calcoli, disegni, verifiche
- **File `.gabbioni`** (File → Salva con nome…) — progetto serializzato, riapribile

---

## Prossimi passi

- [**Workflow completo**](workflow.md) — un progetto reale dall'inizio alla fine.
- [**Inclinazione del muro**](inclinazione-muro.md) — quando e perché battere il muro verso monte.
- [**Rete a doppia torsione**](rete.md) — perché la DT cambia φ_g e introduce c_g.
- [**Stabilità globale Bishop**](bishop.md) — interpretazione del cerchio critico.

---

*Pagina utile? Hai dubbi? [Scrivici](mailto:info@geostru.ai?subject=Help%20GDW%20NX%20-%20Quickstart).*
