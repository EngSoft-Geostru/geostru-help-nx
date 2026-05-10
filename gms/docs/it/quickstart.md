# Quickstart — il tuo primo rilievo in 5 minuti

In 5 minuti vedi GMS NX al lavoro su un dataset di esempio. Niente da installare,
niente da scaricare.

## 1. Apri l'app

Vai su [`nx.geostru.ai/gms/`](https://nx.geostru.ai/gms/). Sull'empty-state (la
schermata che compare quando il progetto è vuoto) vedi 4 card:

- **Rilievo da Compass** — per chi parte dal tablet
- **Apri file** — per chi ha già un `.gms` o un `.csv`
- **Importa con AI** — per chi ha foto o PDF disordinati
- **Dataset di esempio**

Per il quickstart clicca **"Dataset di esempio"** → **"Caso pratico — pendio instabile"**.

## 2. Esplora i risultati

In pochi secondi GMS:

- Carica 33 giaciture distribuite in 5 famiglie note
- Calcola lo stereonet 2D
- Applica il test di Markland al pendio configurato (60° / 180° / φ 30°)

Vedi:

- **Banner risultati**: rosso *"Versante a rischio"* con KPI 14 planari, 5 toppling, 14 stabili, 2 cunei.
- **Stereonet 2D**: poli colorati per famiglia, ciclografica rossa del pendio, cono d'attrito tratteggiato arancione, ⊗ rossi sulle intersezioni cuneo instabili.
- **Tab Statistica**: tabella Fisher (k, α₉₅, Woodcock K/C), stella di immersione, isodensità.

!!! tip "Cosa è ogni elemento sullo stereonet?"
    Apri il modal `?` in alto a destra → tab **Help** → **Glossario stereonet**, oppure
    leggi la pagina [Stereonet](stereonet.md) di questo manuale.

## 3. Cambia la proiezione

In alto, nella toolbar dello stereonet, clicca:

- **3D** — vista tridimensionale interattiva (rotazione col mouse, zoom, pan)
- **Equiangolare** — stereo Wulff invece di Schmidt-Lambert
- **Cunei** (visibile solo in 3D) — vedi il *volume del cuneo* instabile materializzato come triangolo rosso semitrasparente

## 4. Esporta

Toolbar in alto → **Esporta ▾**:

- **Report Word (.docx)** — relazione tecnica con stereo + KPI + tabelle
- **Stereonet DXF** — vettoriale per il CAD
- **Giaciture CSV** — i dati in tabella

Il report Word si apre direttamente in Microsoft Word / LibreOffice / Google Docs.

## 5. Salva il progetto

**File → Salva con nome…** → scarica un file `.gms` (è un JSON) che puoi aprire
in seguito da **File → Apri**.

In alternativa, **File → Salva** memorizza una bozza nel browser (autosave attivo
mentre lavori).

---

## Prossimi passi

- [**Workflow completo**](workflow.md) — un progetto reale dall'inizio alla fine.
- [**GMS Compass**](compass.md) — misura β/α dal tablet in cantiere.
- [**AI Import**](ai-import.md) — fai una foto al taccuino, l'AI estrae le giaciture.
- [**Nuvola di punti 3D**](nuvola-3d.md) — estrai i piani da Matterport / LiDAR.

---

*Pagina utile? Hai dubbi? [Scrivici](mailto:info@geostru.ai?subject=Help%20GMS%20NX%20-%20Quickstart).*
