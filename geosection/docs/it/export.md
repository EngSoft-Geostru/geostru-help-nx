# Export — formati di uscita

Una volta calcolata la sezione, esporti in 4 formati: **SVG**, **PNG**, **DXF**,
**PDF**. Si trovano nel menu *Elaborati* della topbar.

## SVG (Scalable Vector Graphics)

- Formato vettoriale, riapribile in **Inkscape**, **Illustrator**, browser.
- Mantiene tutte le geometrie come oggetti separati: poligoni stratigrafici,
  linee di contatto, sondaggi, etichette, retini.
- Dimensione tipica: 200-500 KB per una sezione standard.
- **Quando usarlo**: includere nella relazione editabile per ritocchi
  successivi (es. cambiare colori in Illustrator senza tornare in app).

## PNG

- Bitmap a risoluzione alta (default 200 dpi, configurabile fino a 600 dpi).
- Sfondo bianco o trasparente.
- **Quando usarlo**: anteprime, presentazioni PowerPoint, allegati email
  rapidi. Per la stampa formale preferisci PDF o DXF.

## DXF (AutoCAD)

- Formato CAD vettoriale standard, riapribile in **AutoCAD**, **DraftSight**,
  **BricsCAD**, **LibreCAD**, **QGIS**.
- Layer separati per: profilo topografico, contatti stratigrafici, falda,
  sondaggi, etichette, legenda, polygons-by-layer.
- Coordinate: in metri, sistema piano locale (X = ascissa progressiva sulla
  sezione, Y = quota assoluta in m s.l.m.).
- **Quando usarlo**: integrare la sezione in una tavola CAD del progetto
  (es. piano regolatore, progetto opera idraulica).

## PDF impaginato

- Pagina A4 / A3 / A2 / A1 (selezionabile) con cartiglio configurabile:
  - intestazione (titolo progetto, committente, data, scala);
  - sezione in scala metrica esatta (es. 1:200, 1:500, 1:1.000);
  - tabella terreni stratigrafici;
  - legenda in basso;
  - cartiglio aziendale (logo + dati studio).
- **Quando usarlo**: documento finale per la relazione tecnica o per allegato
  a pareri di sottosuolo.

## Configurazione cartiglio PDF

Il cartiglio si imposta in *File → Impostazioni progetto → Cartiglio*:

- **Logo**: carica PNG/JPG (consigliato 300×100 px).
- **Dati studio**: nome, indirizzo, P.IVA, geologo responsabile.
- **Dati progetto**: titolo opera, committente, comune, data, riferimenti.
- **Scala**: imposta `1:200`, `1:500`, `1:1.000` o custom.
- **Orientamento**: orizzontale o verticale.
- **Margini**: configurabili in mm.

I dati studio si salvano nelle preferenze del browser e vengono riutilizzati
per i progetti successivi.

## Coordinate e quote nei file esportati

Tutti i formati esportano la sezione con:
- **Origine** in basso-sinistra (x=0, y=quota minima).
- **X** crescente da sinistra a destra (ascissa progressiva sulla traccia).
- **Y** crescente verso l'alto (quota assoluta in m s.l.m.).
- Unità: **metri**.

Per i file DXF questo è importante perché altri software (es. AutoCAD Civil 3D)
si aspettano coordinate consistenti con il resto della tavola.

## Esempio di workflow stampa

1. Genera la sezione (vedi [Workflow](workflow.md)).
2. Configura il cartiglio (logo, scala 1:500, formato A3 orizzontale).
3. *Elaborati → PDF impaginato* → scarica il PDF.
4. Verifica la scala stampando una pagina di prova: misura una distanza nota
   sulla sezione e confronta con la scala del cartiglio.
5. Allega il PDF alla relazione tecnica.

Per una versione "vivente" (modificabile in CAD) esporta anche **DXF** sullo
stesso progetto e includilo nel pacchetto di consegna.
