# GMS NX — Geomechanical Survey

**GMS NX** è il software web per il **rilievo strutturale di ammassi rocciosi**
e l'**analisi cinematica dei pendii**. Misuri le giaciture in campo (con bussola
o tramite l'app companion *GMS Compass*), inserisci il pendio, e ottieni in pochi
clic stereonet 2D/3D, famiglie di discontinuità, statistica Fisher, e i KPI di
stabilità di Markland (planare · ribaltamento · cuneo).

[**Apri GMS NX**](https://nx.geostru.ai/gms/){ .md-button .md-button--primary }
[Quickstart in 5 minuti](quickstart.md){ .md-button }

---

## Cosa fa, in sintesi

- **Input**: giaciture (immersione β / inclinazione α) di discontinuità rocciose. Manuale, da file (`.gms`, `.pol`, `.csv` eGEOCompass), da foto/PDF/Excel via AI, o da nuvole di punti 3D.
- **Calcolo**: proiezioni stereografiche (Schmidt-Lambert · Wulff, polare · equatoriale, emisfero inferiore · superiore), clustering automatico delle famiglie (k-means sferico), statistica Fisher (k, α₉₅, R̄), Cylindrical Best Fit (Woodcock K/C), test di Markland.
- **Output**: stereonet 2D/3D interattivo, isodensità Denness, stella di immersione, report Word `.docx`, stereonet DXF, giaciture CSV.

## Per chi

- **Geologi geomeccanici** che fanno rilievi di campo lungo linee di scansione (versanti, fronti di scavo, gallerie, falesie costiere).
- **Ingegneri geotecnici** che valutano la stabilità di pendii rocciosi prima di interventi (bullonature, gabbionate, reti).
- **Studi di consulenza** che producono pareri tecnici con report Word/DXF.

## Come iniziare

1. Apri [`nx.geostru.ai/gms/`](https://nx.geostru.ai/gms/).
2. Scegli un metodo di input: **rilievo da Compass** (tablet), **apri file**, **importa con AI**, o **dataset di esempio** per esplorare.
3. Imposta il pendio (Dip α / Dip-direction β / angolo d'attrito φ).
4. Premi **Calcola**.
5. Esporta in Word, DXF o CSV.

[Vedi il workflow completo →](workflow.md)

## Capitoli del manuale

### Iniziare

- [**Quickstart**](quickstart.md) — 5 minuti dal primo accesso al primo report.
- [**Workflow completo**](workflow.md) — sequenza dettagliata input → calcolo → export.

### Rilievo

- [**Cosa si misura**](rilievo.md) — guida al rilievo geomeccanico (β/α, parametri ISRM, indizi di scivolamento attivo).
- [**GMS Compass**](compass.md) — l'app web per misurare β/α dal tablet con i sensori del dispositivo.
- [**Trasferimento al PC**](trasferimento.md) — codice 8-caratteri, file `.gms`, anteprima diretta.

### Analisi

- [**Stereonet**](stereonet.md) — guida visuale al disco: cono d'attrito, ciclografica del pendio, poli, ciclografiche delle famiglie, α₉₅ Fisher, cunei.
- [**Famiglie di discontinuità**](famiglie.md) — k-means automatico vs famiglie attese (1-NN sferico).
- [**Test di Markland**](markland.md) — interpretazione dei KPI: planari (Hoek &amp; Bray), toppling (Goodman &amp; Bray), cunei.

### Import avanzato

- [**AI Import**](ai-import.md) — estrai giaciture da foto/PDF/Excel/testo libero usando Gemini.
- [**Nuvola di punti 3D**](nuvola-3d.md) — `.ply` / `.obj` / `.xyz` da Matterport, drone, LiDAR → estrazione automatica dei piani via RANSAC.

### Riferimento

- [**Esportazioni**](esportazioni.md) — Report Word, Stereonet DXF, Giaciture CSV.
- [**Glossario**](glossario.md) — definizioni dei termini chiave.
- [**Formati file**](formati.md) — tabella riassuntiva di tutti i formati supportati.
- [**FAQ**](faq.md)

---

*Hai trovato un errore in questa pagina? [Segnalacelo](mailto:info@geostru.ai?subject=Help%20GMS%20NX) — grazie!*
