# Esportazioni — Word, DXF, CSV

A fine analisi GMS NX produce 3 tipi di output, accessibili dal menu
**Esporta ▾** in toolbar:

- **Report Word (.docx)** — relazione tecnica completa
- **Stereonet DXF** — file vettoriale per il CAD (AutoCAD, BricsCAD,
  …)
- **Giaciture CSV** — i dati grezzi per analisi ulteriori

## Report Word (.docx)

Il **Report Word** è una relazione tecnica pre-impaginata, pronta per
essere consegnata o integrata in una perizia più ampia.

### Cosa contiene

1. **Frontespizio** con: titolo del progetto, descrizione del rilievo,
   sito, operatore, data, note (i campi compilati in *Dati progetto*).
2. **Riepilogo dati di input**:
   - tabella delle giaciture (β, α, famiglia, eventuali parametri
     ISRM se presenti)
   - parametri del pendio (α, β, φ)
3. **Stereonet 2D** in alta risoluzione (Schmidt-Lambert, emisfero
   inferiore), con poli colorati per famiglia, ciclografica del
   pendio, cono d'attrito, eventuali cunei `⊗`.
4. **Banner risultato** (verde / giallo / rosso) e **strip KPI** con i
   contatori (planari, toppling, stabili, cunei).
5. **Tabella statistica Fisher** per famiglia (n, β/α medi, k, α₉₅,
   R̄, Woodcock K/C dell'intero dataset).
6. **Note interpretative** (testo libero scritto da te in *Dati
   progetto* → `Note interpretative`).

### Apertura

Il file generato (`Report_GMS_AAAAMMGG_HHMM.docx`) si apre con:

- **Microsoft Word** (Office 2016+)
- **LibreOffice Writer**
- **Google Docs** (caricato su Drive)
- **Pages** (macOS)

!!! tip "Personalizzare il template"
    Il template usato è in
    `wwwroot/Templates/template_report_gms.docx` sul server. Se
    vuoi un layout aziendale diverso (logo, intestazione, font),
    contatta info@geostru.eu — possiamo configurare un template
    custom per il tuo studio.

### Tempo di generazione

5-15 secondi tipicamente. Se hai >100 giaciture o lo stereonet 3D
attivo, può arrivare a 30-40 secondi.

---

## Stereonet DXF

Il **DXF** è il formato vettoriale di scambio del mondo CAD. GMS
esporta lo stereonet completo (2D, Schmidt-Lambert) come DXF AutoCAD
2018 compatibile.

### Cosa contiene

Layer separati (uno per categoria):

- `RETICOLO_STEREO` — meridiani e paralleli stereografici
- `POLI_FAMIGLIA_1`, `POLI_FAMIGLIA_2`, … — un layer per famiglia
- `CICLOGRAFICA_PENDIO` — la ciclografica rossa del pendio
- `CICLOGRAFICA_FAMIGLIE` — ciclografiche dei piani medi
- `CONO_ATTRITO` — cerchio tratteggiato del cono d'attrito
- `CUNEI_INSTABILI` — i punti `⊗` dei cunei
- `ETICHETTE` — testo (numeri famiglie, β/α, etc.)

Tutti gli elementi sono in **coordinate disco unitario** (raggio 1):
basta scalare in CAD per portare lo stereonet alla dimensione
desiderata.

### Apertura

Compatibile con:

- **AutoCAD** (2018+, anche LT)
- **BricsCAD**
- **DraftSight**
- **LibreCAD** (gratuito)
- **QCAD** (gratuito)

!!! note "DXF tecnico, non grafico"
    Lo stereonet DXF è **vettoriale puro** — niente sfumature, niente
    immagini raster. È pensato per essere **modificato** in CAD
    (aggiungere annotazioni, cambiare colori, integrare in tavole
    tecniche). Per uno stereonet "estetico" da incollare in
    presentazione, usa lo screenshot della vista o esporta da
    PowerPoint il singolo riquadro del Report Word.

---

## Giaciture CSV

Il **CSV** è il formato tabellare universale: si apre in Excel,
LibreOffice Calc, Google Sheets, Python (pandas), R, MATLAB.

### Cosa contiene

Una riga per ogni giacitura, con colonne:

```
Id, DipDirection (β°), Dip (α°), Famiglia,
DistanzaProgressiva (m), Lunghezza (m), Apertura (mm),
Rugosita, Jrc, Riempimento, Alterazione,
Filtrazione, Schmidt, IndiceManuale,
Latitudine, Longitudine, Note
```

Separatore: **virgola**, encoding **UTF-8 BOM** (Excel lo apre
direttamente senza problemi di accenti).

### Quando ha senso

- **Analisi statistiche custom** in Python/R che GMS non fa (ANOVA su
  rugosità, regressioni JRC vs apertura, …)
- **Combinare con altri rilievi** (versanti vicini, profondità di
  carotaggio, mappature geologiche)
- **Archiviazione long-term** in formato leggibile da qualsiasi
  software, anche tra 20 anni quando GMS non esisterà più
- **Pivot in Excel** per riassunti rapidi (es: famiglia × rugosità,
  conta per riempimento, …)

---

## Esporta foto dei giunti

Se hai allegato foto ai singoli giunti (da Compass o caricate
manualmente), il **Report Word** include una pagina dedicata con il
catalogo delle foto, una per giunto.

Per esportare le foto **separatamente** (per archiviare nel cloud
aziendale, ad esempio), salva il progetto come `.gms` (è un JSON):
le foto sono dentro come stringhe base64 e puoi estrarle con uno
script Python.

---

## Salva il progetto (`.gms`)

Non è un'esportazione vera e propria, ma è importante: **File →
Salva con nome…** scarica un file `.gms` che è un **JSON con
*tutto***:

- giaciture + foto
- famiglie (manuali e automatiche)
- pendio + parametri
- metadati (descrizione, sito, operatore, data, note)
- risultati calcolati (stereonet cache, KPI Markland, statistica
  Fisher)

Il `.gms` è il **formato di interscambio nativo** di GMS NX. Ti
consente di:

- riaprire il progetto **identico** in futuro (anche da PC diverso,
  anche dopo aggiornamenti dell'app)
- condividerlo con un collega che ha il proprio GMS NX
- archiviare lo stato del rilievo per audit / revisione perizia

!!! warning "Niente cloud automatico"
    GMS NX **non salva automaticamente** sul cloud GeoStru. La
    funzione `File → Salva` memorizza solo una **bozza nel browser**
    (autosave attivo durante l'editing). Per la persistenza vera devi
    sempre **Salva con nome** e archiviare il `.gms` dove vuoi tu.

---

## Vedi anche

- [Workflow completo](workflow.md) — l'esportazione nel ciclo intero
- [Formati file](formati.md) — dettagli tecnici di tutti i formati
- [Glossario](glossario.md) — termini usati nel report

---

*Pagina utile? [Scrivici](mailto:info@geostru.ai?subject=Help%20GMS%20NX%20-%20Esportazioni).*
