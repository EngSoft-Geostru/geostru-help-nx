# Formati file supportati

Tabella riassuntiva di tutti i formati che GMS NX legge e scrive,
con dettagli tecnici e raccomandazioni d'uso.

## In sintesi

| Formato | Lettura | Scrittura | Uso |
|---|:---:|:---:|---|
| `.gms` | ✅ | ✅ | **Formato nativo**, JSON con tutto il progetto |
| `.csv` (eGEOCompass) | ✅ | — | Export dell'app Android eGEOCompass |
| `.csv` / `.txt` (generico) | ✅ | ✅ | CSV con header `Imm,Incl,Note` o equivalente |
| `.docx` | — | ✅ | **Report Word** |
| `.dxf` | — | ✅ | **Stereonet vettoriale** per CAD |
| `.ply` (ASCII) | ✅ | — | Nuvole di punti 3D |
| `.obj` | ✅ | — | Vertici di mesh 3D |
| `.xyz` / `.txt` (3 colonne) | ✅ | — | Nuvole di punti grezze |
| `.jpg` / `.png` / `.pdf` / `.xlsx` | ✅ (via AI) | — | AI Import: estrazione automatica giaciture |

---

## `.gms` — formato nativo

JSON UTF-8 con tutto il progetto. Schema sintetico:

```json
{
  "version": "1.0",
  "metadata": {
    "descrizione": "Versante S, falesia di Bianco — luglio 2026",
    "sito": "Bianco (RC), versante litorale",
    "operatore": "Mario Rossi",
    "data": "2026-07-15",
    "note": "..."
  },
  "lineaScansione": {
    "latIniziale": 38.0931,
    "lonIniziale": 16.1456,
    "azimut": 230.0,
    "lunghezza": 25.0
  },
  "giunti": [
    {
      "id": 1,
      "dipDirection": 165,
      "dip": 72,
      "famiglia": 1,
      "distanzaProgressiva": 0.5,
      "lunghezza": 2.5,
      "apertura": 5,
      "rugosita": "rugoso ondulato",
      "jrc": 12,
      "riempimento": "calcite",
      "alterazione": "W2",
      "filtrazione": "umido",
      "schmidt": 45,
      "indiceManuale": 4,
      "latitudine": 38.0930,
      "longitudine": 16.1457,
      "note": "...",
      "foto": "data:image/jpeg;base64,/9j/..."
    }
  ],
  "famiglie": [...],
  "pendio": { "alpha": 60, "beta": 180, "phi": 30 },
  "risultati": { ... }
}
```

**Vantaggi**:

- **Self-contained** (incluse foto in base64)
- **Human-readable** (JSON formattato)
- **Idempotente**: aprire e risalvare non perde nulla
- **Long-term**: leggibile da qualsiasi linguaggio anche tra 20 anni

**Quando usarlo**: archiviazione di progetto, condivisione tra colleghi
con GMS NX, backup completo.

---

## `.csv` eGEOCompass

Export dell'app Android **eGEOCompass** (rilievo geomeccanico mobile).
Formato fisso strutturato con header noto, GMS lo riconosce
automaticamente da:

- presenza colonne `Posizione`, `Direz`, `Inclin`, `RQD`, `Spaziatura`,
  `Resistenza`, …
- separatore `;`
- encoding UTF-8

GMS importa: distanza progressiva, β, α, parametri ISRM, note.

---

## `.csv` / `.txt` generico

CSV "qualsiasi" con header riconoscibile. GMS accetta nomi colonna
in italiano e inglese:

| GMS si aspetta | Nome accettato (case-insensitive) |
|---|---|
| `DipDirection` | `Imm`, `Immersione`, `β`, `Beta`, `DipDirection`, `DipDir`, `Direction`, `Direz` |
| `Dip` | `Incl`, `Inclinazione`, `α`, `Alpha`, `Dip`, `Inclin` |
| `DistanzaProgressiva` | `Dist`, `Distanza`, `Progressive`, `Progr` |
| `Lunghezza` | `Lung`, `Lunghezza`, `Length`, `Persistence`, `Persistenza` |
| `Famiglia` | `Fam`, `Family`, `Set`, `JointSet` |
| `Note` | `Note`, `Notes`, `Comment`, `Commento` |

Separatore: virgola `,`, punto e virgola `;` o tab. Encoding: UTF-8
(consigliato) o ANSI Windows-1252.

**Esempio minimo**:

```csv
Imm,Incl,Note
165,72,giunto principale stratificazione
178,68,
180,71,riempimento calcite
```

---

## `.docx` (Report Word)

Output. Generato con **DocumentFormat.OpenXml** a partire dal
template `Templates/template_report_gms.docx`. Compatibile con:

- Microsoft Word 2016+
- LibreOffice Writer 6+
- Google Docs (caricato su Drive)
- Pages (macOS)

Le immagini (stereonet) sono PNG embedded a 300 DPI.

---

## `.dxf` (Stereonet vettoriale)

Output. Versione **AutoCAD 2018**. Generato dal `DxfWriter` interno
(porting C# del vecchio `ClassDXF` VB.NET).

Layer: vedi pagina [Esportazioni](esportazioni.md). Coordinate in
disco unitario (raggio 1) — scalare a piacere in CAD.

---

## `.ply` (Polygon File Format)

**Solo ASCII**. Formato standard per fotogrammetria e LiDAR.

Header tipico riconosciuto da GMS:

```
ply
format ascii 1.0
element vertex 1350
property float x
property float y
property float z
end_header
0.123 4.567 8.901
...
```

GMS legge **solo i vertici** (posizione X Y Z); ignora colore,
normali, alpha, e tutte le proprietà delle facce. Le facce vengono
ignorate (RANSAC lavora sul punto, non sulla mesh).

**Conversione PLY binario → ASCII**: in CloudCompare, *File → Save as
→ PLY → ASCII*.

---

## `.obj` (Wavefront OBJ)

Letto in modalità "vertex-only". GMS legge tutte le righe `v X Y Z` e
ignora `vn`, `vt`, `f` (facce).

Utile se hai una mesh chiusa (es. modello CAD) e vuoi estrarre i
piani principali.

---

## `.xyz` / `.txt` (3 colonne)

Formato grezzo: una riga per punto, 3 valori separati da spazio o
tab.

```
0.123 4.567 8.901
0.124 4.566 8.903
...
```

Encoding ASCII / UTF-8. Eventuali righe di header (commenti `#` o
testo) vengono saltate.

---

## `.jpg` / `.png` / `.pdf` / `.xlsx` (via AI Import)

Non sono formati "nativi" di GMS, ma vengono accettati come **input
all'AI Import Wizard** (Gemini Flash 2.5 con responseSchema
strutturato).

Vedi [AI Import](ai-import.md) per il workflow completo.

---

## Limiti di dimensione

| Tipologia | Limite |
|---|---|
| `.gms` | 100 MB (incluse foto base64) |
| `.csv` / `.txt` | 5 MB |
| `.ply` / `.obj` / `.xyz` | 60 MB |
| File AI Import (foto/PDF/Excel) | 20 MB per file, batch totale 60 MB |
| Numero giaciture per progetto | nessun limite hard, prestazioni ottime fino a ~500 |

---

## Vedi anche

- [Esportazioni](esportazioni.md) — uso pratico di Word/DXF/CSV
- [Nuvola 3D](nuvola-3d.md) — dettagli su PLY/OBJ/XYZ
- [AI Import](ai-import.md) — formati non strutturati

---

*Formato mancante o non chiaro? [Scrivici](mailto:info@geostru.ai?subject=Help%20GMS%20NX%20-%20Formati).*
