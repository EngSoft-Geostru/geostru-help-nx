# Workflow completo — da progetto a relazione

Sequenza dettagliata input → calcolo → output per un progetto reale.

## 1. Dati progetto

Imposta:

- **Descrizione rilievo / sito / operatore / data** (testata della relazione)
- **Normativa**:
    - `NTC 2018 (statica)` → approccio A1·M1·R3 (default GeoStru)
    - `NTC 2018 (sismica)` → A2·M2·R3, abilita Kh/Kv e Mononobe-Okabe
- **Profondità falda** (opzionale, m dal piano campagna). Se vuota o 0 → niente falda.

## 2. Geometria del muro

Il muro è una pila di **gabbioni** disposti su `numFile` righe, dal basso verso l'alto. Per ogni fila imposti:

- **Numero di blocchi** (es. fila 1 = 3 blocchi, fila 5 = 1 blocco → muro a piramide)
- **Spostamento orizzontale** (m) — positivo verso valle (sinistra), negativo verso monte (destra)

L'**Allineamento** rapido (combo "A destra" / "A sinistra" / "Centrato" / "Personalizzato") imposta gli shift automaticamente.

L'**Inclinazione muro α** (0÷15°) ruota tutto il muro come corpo rigido attorno al piede di valle:

- α > 0 = top spostato verso monte ("battered toward soil")
- Effetto: Coulomb Ka aumenta, ma la **direzione** della spinta diventa δ+α → la componente verticale Sy stabilizza maggiormente. Net effect su FS: tipicamente positivo.

[Dettagli geometria →](geometria.md)
[Dettagli inclinazione muro →](inclinazione-muro.md)

## 3. Fondazione

- **Base B** (m): la fondazione è sempre **centrata** rispetto alla prima fila. Esubero ripartito 50/50 tra valle e monte.
- **Spessore valle h_v** (m): spessore minimo, lato a valle.
- **Inclinazione β** (0÷15°): la faccia INFERIORE inclina verso monte → spessore monte `h_m = h_v + B·tan(β)`.
- **Prima fila interrata**: checkbox. Se attiva, la prima fila è sotto piano campagna → attiva spinta passiva.

[Dettagli fondazione →](fondazione.md)

## 4. Gabbioni e rete

Sezione **Gabbioni**:

- **Tipologia** dal catalogo Maccaferri (1×1×1, 2×1×1, 1.5×1×1, ecc.) — auto-compila peso specifico e dimensioni
- **Modalità angolo attrito**: `auto` (formula 25·γ−10° per ES, fissato 45° per DT) o `manuale`

Sezione **Rete metallica**:

- **Tipologia maglia**:
    - **Doppia torsione (Maccaferri, default)** — catalogo con 7 modelli (6×8, 8×10, Zn / Zn+PVC). Verifica via σ_adm Gawac.
    - **Elettrosaldata (rigida)** — verifica classica trazione + punzonamento del filo singolo.

[Dettagli rete →](rete.md)

## 5. Stratigrafia

Sezione **Geotecnica**:

- **Terreno spingente**: stratigrafia multi-strato (n strati: descrizione, colore, altezza, γ, φ, c, γ_saturo).
- **Terreno di fondazione**: γ, φ, c.
- **Interfaccia alla base**: `terreno naturale` / `fondazione c.a./cls (δ=2/3 φ, c=0)` / `personalizzato`.

La spinta viene calcolata strato per strato; ad ogni transizione si compongono i contributi.

[Dettagli geotecnica →](geotecnica.md)

## 6. Sovraccarichi

Sezione **Sovraccarico**:

- **G permanente** (kN/m²) — es. peso di una pavimentazione
- **Q accidentale** (kN/m²) — es. carico veicolare
- **Posizione (ascissa iniziale e finale)** — distanza dal bordo superiore del muro lungo il terrapieno
- **Spinta aggiuntiva S** (kN/m) — forza esterna applicata orizzontalmente al muro (es. cavi, ancoraggi)

In combinazione sismica appare un alert giallo che ricorda di applicare il coefficiente Ψ₂ ai sovraccarichi variabili.

[Dettagli sovraccarichi →](sovraccarichi.md)

## 7. Sisma (se attivato)

Se Normativa = "NTC 2018 (sismica)":

- **k_h, k_v** vengono calcolati automaticamente da `UpdateNormativa` in base ai parametri sismici dell'app
- Il coefficiente A_S (γ_G sulle spinte) diventa 1.0 (combinazione fondamentale già amplificata)
- Mononobe-Okabe attivato in `CalculateMultiLayerThrust` con θ = atan(kh/(1−kv))
- Per il ribaltamento, kv prende segno opposto (NTC 7.11.7) e Ka viene ricalcolato

[Dettagli sisma →](sisma.md)

## 8. Calcola

Premi il bottone **Calcola** ⚡

Il calcolo esegue:

1. **Spinta attiva multi-strato** (Coulomb statico o MO sismico)
2. **Verifiche esterne**:
    - Ribaltamento: FS = Ms / (Mr · γ_R_rib)
    - Scorrimento (con base inclinata β): proiezione N⊥, T_drive su piano inclinato → FS = R / (F_drive · γ_R_scorr)
    - Capacità portante: Brinch-Hansen con N_q, N_γ, N_c
3. **Verifiche interne** ad ogni giunto fila-fila:
    - Scorrimento (con c_g per DT, con φ_g e c del terreno per fila 0 senza fondazione)
    - Ribaltamento parziale
    - σ_max valle/monte vs σ_adm (per DT, formula Gawac)

[Dettagli verifiche →](verifiche.md)

## 9. Stabilità globale (Bishop)

Sezione **Stabilità globale** in fondo:

- **N. conci**: 30÷200 (default 30)
- **Punto valle** (X,Y), **monte** (X,Y), **base** (X,Y): le 3 ascisse/quote che definiscono il cerchio. `auto` = scelte ragionevoli; modificabili a mano per esplorare cerchi alternativi.
- Premi **Stabilità globale** → calcolo Bishop semplificato; rendering del cerchio sulla sezione.

Validazione automatica: il cerchio deve passare SOTTO la fondazione (inclinata). Se attraversa muro/fondazione, errore esplicito.

[Dettagli Bishop →](bishop.md)

## 10. Output

- **Report Word `.docx`** (toolbar → Report): relazione completa con dati input, formule, tabelle, FS, disegni.
- **File `.gabbioni`** (File → Salva / Salva con nome…): progetto serializzato in formato testo a sezioni, backward-compatible.
- **Autosave nel browser**: il progetto è salvato in `localStorage` ogni 1.5 s. Se chiudi il browser senza salvare su file, alla riapertura ti viene proposto di ripristinare la bozza.

[Dettagli report →](report.md)
[Dettagli formato file →](formati.md)

---

## Sequenza tipica (riassunto)

1. Apri app → 2. Imposta normativa → 3. Geometria muro + fondazione → 4. Gabbioni + rete → 5. Stratigrafia → 6. Sovraccarichi → 7. (se sisma: nessuna azione, kh/kv auto) → 8. **Calcola** → 9. Stabilità globale → 10. **Report**

Tempo tipico:

- **Prima volta** su un progetto reale: 30÷45 min
- **Aggiornamento** di un progetto esistente: 5÷10 min
- **Esempio cliente caricato**: vede risultati in <1 min

---

*Domande? [Scrivici](mailto:info@geostru.ai?subject=Help%20GDW%20NX%20-%20Workflow).*
