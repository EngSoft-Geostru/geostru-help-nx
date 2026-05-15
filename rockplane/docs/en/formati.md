# File formats — `.rockplane`

The native project file extension is `.rockplane`. Internally it is plain **JSON**, human-readable and editable in any text editor.

## Top-level structure

```json
{
  "versione": "1.0",
  "titolo": "Project description",
  "committente": "Client name",
  "sito": "Site location",
  "data": "2026-05-15",
  "note": "Free-text notes",
  "professionista": {...},
  "localizzazione": {"latitudine": ..., "longitudine": ..., "altitudine": ...},
  "immagineSito": "data:image/png;base64,...",
  "geometria": {...},
  "materiale": {...},
  "acqua": {...},
  "forzaEsterna": {...},
  "sisma": {...},
  "verifica": {...},
  "catalogo": [...],
  "catalogoReti": [...],
  "interventi": [...]
}
```

## Schema

### geometria
| Field | Type | Notes |
|---|---|---|
| h, beta, alfa, psi | number | slope dimensions in m and ° |
| b | number | block depth |
| conTensionCrack | bool | TC enabled |
| t, theta | number | only if conTensionCrack |

### materiale
| Field | Notes |
|---|---|
| gamma | unit weight kN/m³ |
| criterio | 0 = Mohr-Coulomb, 1 = Barton-Bandis |
| coesione, phi | MC parameters |
| phiB, jrc, jcs | BB parameters |

### acqua
| Field | Notes |
|---|---|
| gammaW | 9.81 |
| hwPonded | water level at toe |
| versantePervious | hydrostatic connection |
| zwPiano | water depth in the joint |
| distribuzione | 0=none, 1=mid, 2=toe, 3=crack base |

### sisma
| Field | Notes |
|---|---|
| alfaS | kh coefficient |
| omega | direction ° |

### forzaEsterna
| Field | Notes |
|---|---|
| modulo | magnitude kN/m |
| delta | inclination ° |
| tipo | 0=permanent, 1=variable |

### verifica
| Field | Notes |
|---|---|
| approccio | 0-5 (Characteristic, NTC, EC7 DA1C1/C2, DA2, DA3) |
| fsRichiestoCaratteristico | required FS for Characteristic only |

### catalogo (array of nail/anchor types)
See [chiodi.md](chiodi.md) and [tiranti.md](tiranti.md) for fields.

### catalogoReti (array of mesh types)
See [reti.md](reti.md).

### interventi (array of installed reinforcement)
Each item: `{tipo, tipologiaCodice, posizione, passoOrizzontale, inclinazione, forza, etichetta}`

## Persistence

- **Save** (Ctrl+S): overwrites the open file if the FileSystemFileHandle is available (Chrome/Edge), otherwise behaves like Save As.
- **Save as** (Ctrl+Shift+S): always shows the picker.
- **Open from file** (Ctrl+O): loads a `.rockplane` file.
- **New project** (Ctrl+N): resets to defaults (asks for confirmation if there are unsaved changes).

## Cross-version compatibility

The format is **forward-compatible**: any extra fields are ignored on load. The version is in `versione`. Future additions will maintain backward compatibility through default fallbacks.
