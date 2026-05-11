# Report e disegni

Il report Word `.docx` è l'output principale di GDW: relazione tecnica completa
pronta per essere consegnata al committente.

## Generare il report

Toolbar in alto → bottone **Report** (icona Word).

Il report viene generato in pochi secondi e scaricato automaticamente come
`Report_GDW_YYYYMMDD_HHmmss.docx`.

## Contenuto del report

### Sezione 1 — Dati progetto

- Descrizione del rilievo, sito, operatore, data
- Normativa applicata (NTC 2018 statica/sismica)
- Coordinate GPS (se inserite)
- Mappa statica del sito (Google Maps, se attivato)

### Sezione 2 — Geometria

- Tabella **gabbioni** (dimensioni, peso specifico, n. file, blocchi/fila)
- Tabella **fondazione** (base, spessore valle/monte, inclinazione β)
- Tabella **terrapieno** (inclinazioni ε₁, ε₂, lunghezze)
- Inclinazione muro α se > 0
- **Disegno sezione** (PNG generato da SkiaSharp, ad alta risoluzione)

### Sezione 3 — Materiali

- Tabella **rete** (tipologia DT/ES, maglia, diametro filo, resistenza, c_g se DT)
- Tabella **stratigrafia** (strato per strato: descrizione, γ, φ, c, γ_sat)
- Profondità falda
- Interfaccia alla base

### Sezione 4 — Carichi

- Sovraccarichi G/Q (valori, posizioni, Ψ₂ se sismica)
- Spinta aggiuntiva S
- Combinazione sismica con k_h, k_v (se attiva)

### Sezione 5 — Coefficienti di sicurezza

- Tabella **A1·M1·R3** (o A2·M2·R3 sismico)
- Valori usati nel calcolo

### Sezione 6 — Spinta attiva

- Ka (Coulomb statico o Mononobe-Okabe sismico)
- Componenti S_x, S_y, S_falda, S_q
- Spinta totale, momento ribaltante
- **Diagramma pressioni σ_h(z)** per strato

### Sezione 7 — Verifiche esterne

- Ribaltamento: M_s, M_r, FS, verifica
- Scorrimento: F_x, F_y, β, R, F_drive, FS, verifica
- Capacità portante: N_q, N_γ, N_c, q_lim, σ_eff, FS, verifica

### Sezione 8 — Verifiche interne (fila per fila)

Una tabella per ogni fila:

- σ_v, σ_m al lembo valle/monte
- Eccentricità e e punto di azzeramento (se parzializzata)
- FS_rib, FS_scorr parziali
- σ_max ≤ σ_adm (per rete DT)
- Badge ✓/✗

### Sezione 9 — Stabilità globale (se eseguita)

- 3 punti del cerchio, centro, raggio
- N. conci
- FS_Bishop
- Log dei conci principali (opzionale, attivo con DebugCalcolo)
- Disegno della superficie circolare

### Sezione 10 — Note e firma

- Firma dell'operatore
- Note tecniche libere
- Riferimenti normativi

## Disegno della sezione (PNG)

Il disegno della sezione viene generato lato server con **SkiaSharp** (libreria
2D) ad alta qualità. Mostra:

- Profilo del terreno (valle, muro, monte)
- Strati colorati con stratigrafia
- Riempimento a tergo (se allineamento a sinistra)
- Gabbioni (rettangoli ruotati se α > 0)
- Fondazione (trapezoidale se β > 0)
- Diagramma pressioni attive (campiture verticali)
- Tensioni interne tra gabbioni (bande verdi tratteggiate)
- Tensione fondazione (banda rossa)
- Quote (altezza totale, base, spessori)
- Etichette delle file (I, II, III, ...)
- Spinta totale come freccia + punto di applicazione

## Anteprima schema

Sopra la sezione COEFFICIENTI c'è un bottone **Anteprima schema** che genera
solo il disegno (senza il resto del report). Utile per verificare la geometria
prima di lanciare il calcolo completo.

## Debug log

Sezione **Debug** (visibile se `DebugCalcolo: true` in `appsettings.json`):

- Stampa di tutti i parametri intermedi del calcolo principale
- Per ogni fila, dettaglio delle verifiche interne (Ka, δ, M_s, M_r, F_drive, ecc.)
- Log Bishop (conci, iterazioni)

Utile per:

- Validare manualmente il calcolo confrontando con un foglio Excel
- Capire perché una verifica fallisce
- Reportare problemi al supporto tecnico

## Esportazione file progetto

**File → Salva** (o **Salva con nome…**) → scarica un file `.gabbioni`
(formato testo a sezioni, vedi [Formati file](formati.md)).

Il file include tutti i parametri input e può essere riaperto con **File →
Apri**. Backward-compatible: file più vecchi (versione 1, 2, 3, ...) si
caricano correttamente; i campi nuovi assumono i default.

## Autosave nel browser

GDW salva automaticamente lo stato del form in `localStorage` ogni 1.5 s
mentre lavori. Se chiudi accidentalmente il browser o crashi:

- Alla riapertura della pagina, un banner giallo propone "Bozza non salvata
  trovata — Ripristina / Scarta"
- Ripristina recupera tutti i campi compilati
- Lo snapshot scade dopo 7 giorni se non usato

L'autosave è separato dal salvataggio su file `.gabbioni`. Salva comunque
periodicamente su file per persistenza definitiva.

## Vedi anche

- [Formati file](formati.md) — struttura del `.gabbioni`
- [Quickstart](quickstart.md) — primo report in 5 minuti
