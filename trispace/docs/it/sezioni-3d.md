# Sezioni 2D e vista 3D

Dopo aver triangolato la TIN, Trispace permette di visualizzare il terreno
in **sezione 2D** lungo una traccia + **vista 3D interattiva** della mesh.

## Sezione 2D

### Come crearla

1. Premi **S** (tool Sezione) o click su Sezione in toolbar
2. Status bar: *"Sezione: clicca punto iniziale"*
3. Click sul canvas → punto iniziale della traccia
4. Status bar: *"Sezione: clicca punto finale"*
5. Click → la traccia è disegnata sul canvas come linea tratteggiata
6. Si apre il **SectionPanel** in basso

### Cosa mostra il SectionPanel

- **Sezione 2D** del terreno lungo la traccia (sample della TIN)
- Asse orizzontale: distanza progressiva (m)
- Asse verticale: quota Z (m)
- **Esagerazione verticale** automatica (default 1:1, tipicamente 2:1 o 5:1
  per terreni poco accidentati)

### Esportare la sezione

Pulsante **"Esporta DXF"** nel SectionPanel: scarica una DXF AC1015 con
la sezione come polilinea.

### Sezioni multiple

Puoi tracciare **N sezioni** nella stessa sessione (tool S poi click 2 punti,
ripeti). Ogni sezione ha il proprio panel; cliccando sulla traccia nel
canvas torna in primo piano la sezione corrispondente.

## Vista 3D

### Apertura

Riga AI: `3d` o tab **3D** in alto a destra. Si apre il pannello View3D
sopra il canvas (overlay traslucido).

### Cosa vedi

Render Three.js della mesh:

- **Triangoli** della TIN con shading (calcolo normali per face)
- **Curve di livello** sovrapposte come linee 3D bianche
- **Cut/fill** colorato se hai calcolato i volumi
- **Punti quotati** come marker 3D

### Controlli

- **Drag (mouse)**: orbita attorno alla mesh
- **Scroll**: zoom
- **Drag right-click / Shift+drag**: pan
- **R**: reset vista (top-down)

### Colorazione

Toggle in toolbar 3D:

- **Shading** — grigio uniforme con illuminazione direzionale
- **Quota** — gradient da blu (basso) a rosso (alto)
- **Pendenza** — gradient verde→rosso secondo l'angolo
- **Cut/Fill** — solo se hai calcolato i volumi

### Performance

Three.js gestisce bene fino a ~100k triangoli con buona fluidità (60 FPS
su PC moderno). Oltre, considera di **decimare la mesh**:

- Comando: `decima mesh 50000` (target N triangoli)
- Algoritmo: edge collapse iterativo (mantiene la geometria, riduce
  il dettaglio)

## Sezioni 3D (taglio della mesh nello spazio)

Trispace al momento **non** supporta sezioni 3D vere (taglio della mesh
con un piano arbitrario nello spazio 3D). Solo sezioni 2D verticali lungo
una traccia in pianta.

Per sezioni 3D oblique → fuori scope, usa Rhinoceros / Blender / Civil 3D.

---

## Vedi anche

- [Mesh + curve](mesh-triangolazione.md) — generazione della TIN
- [Workflow completo](workflow.md) — sezioni e 3D nel ciclo intero
- [Esportazioni](esportazioni.md) — sezione DXF, mesh GeoJSON

---

*Pagina utile? [Scrivici](mailto:info@geostru.ai?subject=Help%20Trispace%20NX%20-%20Sezioni%203D).*
