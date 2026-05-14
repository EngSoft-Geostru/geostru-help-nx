# Workflow completo

Caso realistico: versante con frattura persistente, falda alta in autunno, sisma di base e necessità di intervento. Tempo stimato: 30 minuti.

## Schema generale

```
 1. DATI GENERALI    →  Descrizione, sito, normativa
 2. GEOMETRIA        →  H, β, α, ψ, B, eventuale tension crack
 3. MATERIALE        →  γ, c, φ (Mohr-Coulomb sul piano)
 4. AZIONI           →  acqua, sisma, forza esterna
 5. CATALOGO         →  tipologie chiodi/tiranti/reti
 6. INTERVENTI       →  posizione · passo · inclinazione · tipologia
 7. CALCOLO          →  α critico opzionale, lettura FS
 8. VERIFICA NORM.   →  switch fra TA · NTC · EC7
 9. ESPORTAZIONE     →  Word (relazione) + DXF (sezione)
```

## Step 1 · Dati generali

Apri la card in alto **"Dati generali"** ed inserisci:

| Campo         | Esempio                          |
|---------------|----------------------------------|
| Descrizione   | Versante km 42+700 — SP 18 Bivio |
| Lat / Lon     | 41.5421 · 14.6712                |
| Alt (m)       | 720                              |
| Data          | 14/05/2026                       |
| Sito          | Comune di Castelpetroso (IS)     |
| Foto sito     | clic sul box → carica .jpg/.png  |
| Normativa     | NTC 2018 — A2+M2+R2              |

[Approfondisci la sezione Verifica →](verifica.md)

## Step 2 · Geometria

Schema convenzionale Hoek-Bray:

```
              ψ
        B────────────C
       /             |
      / β            |
     /               | H
    /     α          |
   /  ───────────────|
  O                  +
```

| Simbolo | Significato                                | Vincolo            | Esempio |
|---------|--------------------------------------------|--------------------|---------|
| H       | altezza versante [m]                       | > 0                | 25      |
| β       | inclinazione del fronte [°]                | 0 < β ≤ 90         | 65      |
| α       | inclinazione piano di rottura [°]          | 0 < α < β          | 40      |
| ψ       | inclinazione piano sommitale [°]           | ≥ 0                | 0       |
| B       | profondità del blocco (⟂ alla sezione) [m] | ≥ 0.1              | 5       |
| T       | distanza fessura di trazione dal ciglio    | > 0 (se TC attiva) | 2       |
| θ       | inclinazione della fessura [°]             | 0 < θ ≤ 90         | 90      |

Per attivare la **tension crack**, spunta il toggle "Fessura di trazione" e inserisci T e θ.

[Dettagli →](geometria.md)

## Step 3 · Materiale (Mohr-Coulomb)

| Simbolo | Significato                          | Esempio |
|---------|--------------------------------------|---------|
| γ       | peso volume blocco [kN/m³]           | 26      |
| c       | coesione sul piano [kPa]             | 40      |
| φ       | angolo d'attrito [°]                 | 32      |

I valori di γ<sub>φ'</sub> e γ<sub>c'</sub> applicati dipendono dall'approccio normativo scelto allo Step 1.

[Dettagli →](materiale.md)

## Step 4 · Azioni

### Acqua

Tre regimi modellabili:

- **Hw** — livello acqua al piede del versante (ristagno, falda di valle)
- **Zw** — acqua nella discontinuità (genera uplift U sul piano), con 4 forme di distribuzione: assente, max metà altezza, max al piede, max alla base della fessura
- **Zt** — acqua nella tension crack (genera V verticale)

[Dettagli →](acque.md)

### Sisma pseudostatico

| Simbolo | Significato                         | Esempio |
|---------|-------------------------------------|---------|
| αs = kh | coefficiente orizzontale [-]        | 0.12    |
| Ω       | direzione del sisma [°]             | 0       |

[Dettagli →](sisma.md)

### Forza esterna E

Convenzione **intuitiva** RockPlane NX:

- δ = 0° → orizzontale **verso valle** (destabilizzante, FS ↓)
- δ = +90° → verticale verso il basso (peso/surcharge)
- δ = −90° → verticale verso l'alto (tirante/uplift)
- δ = 180° → orizzontale verso monte (stabilizzante)

| Simbolo | Significato                  | Tipo carico    | Esempio |
|---------|------------------------------|----------------|---------|
| E       | modulo [kN/m]                | Permanente / Variabile | 200     |
| δ       | inclinazione [°]             |                | 90      |

[Dettagli →](forze-esterne.md)

## Step 5 · Catalogo tipologie

Lo step **"Interventi"** ha 3 sotto-cataloghi:

1. **Chiodi / Tiranti** — tipologie con dimensionamento NTC opzionale
2. **Reti** — corticale + caging con dimensionamento dei nodi
3. **Interventi posizionati** — istanze concrete con posizione e passo

Per ogni tipologia di chiodo/tirante puoi:

- **Inserire F manuale** (kN della capacità singola, footer ambra ↓)
- **Calcolare R<sub>d</sub> da NTC** spuntando "Calcola Resistenza di progetto" (footer verde ↓): inserisci geometria armatura, materiale malta, ancoraggio, e il software calcola la catena R_min → R_k → R_d secondo NTC §6.6 (tirante) o §6.7 (chiodo, Variante A SoilNail).

[Dettagli chiodi →](chiodi.md) · [Dettagli tiranti →](tiranti.md) · [Dettagli reti →](reti.md)

## Step 6 · Interventi sul cuneo

Per ogni intervento posizionato:

| Campo            | Significato                                       |
|------------------|---------------------------------------------------|
| Tipologia        | codice catalogato (es. A_200, B, C…)             |
| Posizione        | quota verticale Y sul fronte [m]                  |
| Passo            | interasse orizzontale ⟂ sezione [m]               |
| Inclinazione Δ   | sotto-orizzontale, verso la roccia [°]            |
| Etichetta        | label visibile sul disegno                        |

I chiodi/tiranti compaiono sul viewer 2D con linea che attraversa il piano e bulbo evidenziato.

## Step 7 · Calcolo

Il software ricalcola **automaticamente** ad ogni modifica (debounce 150 ms). Sul pannello destro vedi:

- **FATTORE DI SICUREZZA** in grande (color-coded)
- **Geometria calcolata**: L · M · Q · A · W (per metro e totale × B)
- **Forze sul piano**: N · S · τ · U · V
- **Resistenze di progetto · chiodi / tiranti**: breakdown per ogni tipologia con verifiche stile NTC §6.6
- **Avvisi**: messaggi importanti (es. cinematica non ammissibile, FS < 1, comportamento atteso per c=0)

### Cerca l'α critico

Click sul bottone **`α crit`** accanto al campo α → sweep automatico per trovare l'inclinazione del piano che minimizza FS. Utile per verificare il caso peggiore quando l'inclinazione reale del piano non è conosciuta con precisione.

[Dettagli α critico →](alfa-critico.md)

## Step 8 · Verifica normativa

Cambia normativa nel selettore in alto. Le chip dei coefficienti applicati si aggiornano subito; l'FS richiede 100 ms (round-trip backend).

[Dettagli verifica →](verifica.md)

## Step 9 · Esportazione

Menu **File → Esporta**:

- **Word (.docx)** — relazione di calcolo completa, ~10-15 pagine
- **DXF** — sezione 2D quotata, importabile in AutoCAD/Civil3D

[Dettagli export →](export.md)

---

## Caso esempio — versante con tutto

| Parametro                                    | Valore       |
|----------------------------------------------|--------------|
| H · β · α · ψ                                | 25 · 65° · 40° · 0° |
| γ · c · φ                                    | 26 · 40 · 32 |
| Tension crack                                | T=2m · θ=90° |
| Acqua Zw (max al piede)                      | 5 m          |
| Sisma kh                                     | 0.12         |
| Carico stradale E permanente δ=90°           | 30 kN/m      |
| Chiodi passivi B (φ32) ogni 2.5m a quota 10 m | F=120 kN     |
| Rete corticale q                             | 50 kN/m²     |
| Normativa                                    | NTC 2018     |

Risultato atteso (indicativo): FS ≈ 1.05–1.15, verifica **non soddisfatta** (FS<sub>req</sub> = 1.10), serve aggiungere una seconda riga di chiodi a quota più alta o aumentare il passo della rete.

[Vai al modello teorico per capire la matematica →](modello-teorico.md)
