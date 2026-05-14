# Tiranti attivi

I **tiranti** (ground anchors) sono elementi di rinforzo **attivi**: vengono pretensionati (precarico) e applicano immediatamente la loro forza al cuneo, indipendentemente dallo spostamento. RockPlane li dimensiona secondo NTC 2018 §6.6.

## Capacità del singolo tirante

Tre limiti, sempre tutti calcolati:

| Limite                              | Simbolo         | Formula                          |
|-------------------------------------|-----------------|----------------------------------|
| Capacità acciaio (yield ridotto)    | R<sub>acciaio</sub> | A<sub>s</sub> · f<sub>yd</sub> · η          |
| Aderenza acciaio ↔ malta            | R<sub>aderenza</sub> | π · D · L<sub>bulbo</sub> · τ<sub>b</sub>     |
| Sfilamento bulbo                    | R<sub>estrazione</sub> | π · D<sub>bulbo</sub> · L<sub>bulbo</sub> · τ<sub>ult</sub> |

A differenza dei chiodi, per i tiranti **NTC §6.6 prescrive la catena di riduzioni**:

$$ R_k = \frac{R_{min}}{\xi}, \quad R_d = \frac{R_k}{\gamma_{Ra,t}} $$

con:
- R<sub>min</sub> = min(R<sub>acciaio</sub>, R<sub>aderenza</sub>, R<sub>estrazione</sub>)
- ξ = coefficiente di correlazione Tab. 6.6.III (funzione del **n. di prove di pull-out preventive**)
- γ<sub>Ra,t</sub> = 1.10 (provvisori) o 1.20 (permanenti)

## Tabella ξ NTC §6.6 Tab. 6.6.III

!!! warning "Attenzione alla terminologia"
    NTC distingue:
    - Tab. **6.4.IV** (pali): ξ in funzione del **n. di verticali di indagine geognostica**, scala 1.8 → 1.2
    - Tab. **6.6.III** (tiranti): ξ in funzione del **n. di prove di pull-out preventive**, scala 1.4 → 1.1
    
    RockPlane usa la Tab. 6.6.III. Il campo nell'UI si chiama esplicitamente *"N. prove pull-out"* per evitare confusione.

| n. prove di estrazione preventive | ξ |
|-----------------------------------:|--:|
| 0 (nessuna prova → fallback)       | 1.40 |
| 1                                  | 1.40 |
| 2                                  | 1.30 |
| 3                                  | 1.20 |
| ≥ 4                                | 1.10 |

## Parametri di input (catalogo tipologia)

### Geometria

| Simbolo                  | Significato                                | Unità | Default |
|--------------------------|--------------------------------------------|-------|---------|
| D (φ arm)                | diametro armatura totale (n.tre·D<sub>tref.</sub>) | mm    | 32      |
| L tot                    | lunghezza totale (libera + bulbo)          | m     | 8       |
| D<sub>foro</sub> (φ foro) | diametro foro                              | mm    | 150     |
| L libera                 | tratto libero (non ancorato)               | m     | 4       |
| L bulbo                  | tratto ancorato                            | m     | 4       |
| z<sub>med</sub>          | profondità media del bulbo                 | m     | 6       |

### Acciaio e aderenza

| Simbolo                  | Significato                              | Unità  | Default |
|--------------------------|------------------------------------------|--------|---------|
| f<sub>yd</sub>           | resistenza di calcolo acciaio (yield/γ<sub>s</sub>) | N/mm²  | 391     |
| η lavoro                 | tasso di lavoro (η fy)                   | %      | 90      |
| τ<sub>b</sub>            | aderenza acciaio ↔ cls                  | N/mm²  | 2       |

### Coefficienti NTC §6.6

| Campo                  | Significato                                 | Default |
|------------------------|---------------------------------------------|---------|
| N. prove pull-out      | n. prove preventive di estrazione           | 0       |
| γ<sub>Ra,t</sub>       | 1.10 (provvisori) / 1.20 (permanenti)       | 1.10    |
| FS sull'elemento       | FS aggiuntivo locale (oltre γ NTC, default 1.0) | 1.0   |

## Differenze chiodo vs tirante

| Aspetto                | Chiodo §6.7 (Variante A)         | Tirante §6.6                          |
|------------------------|------------------------------------|---------------------------------------|
| Pretensionamento       | No (passivo)                       | Sì (precarico)                        |
| η acciaio              | Forzato a 100%                     | Tasso di lavoro variabile (90% default) |
| Sezione armatura       | D − 4 (sezione netta filettatura)  | D pieno                               |
| Lunghezza efficace     | L totale                           | Solo L bulbo                          |
| ξ (Tab. 6.6.III)       | Non applicato (ξ=1)                | Applicato                             |
| γ<sub>Ra,t</sub>       | Non applicato (γ=1)                | Applicato                             |
| R taglio (Tresca)      | Calcolato (Clouterre N-V)          | Non rilevante                         |

## UI catalogo

Identica ai chiodi:

- **Modalità manuale** (footer ambra): inserisci F [kN] singolo tirante
- **Modalità NTC** (footer verde): spunti "Calcola Resistenza di progetto", il software calcola la catena completa R<sub>acciaio</sub> → R<sub>aderenza</sub> → R<sub>estrazione</sub> → R<sub>min</sub> → R<sub>k</sub> → R<sub>d</sub>

Nel pannello destro, breakdown completo con tutti i 3 limiti, i coefficienti applicati, e la R<sub>d</sub> finale.

## Intervento posizionato

| Campo              | Significato                                                |
|--------------------|------------------------------------------------------------|
| Tipo               | Chiodo attivo (cioè TIRANTE attivo)                        |
| Tipologia          | codice del catalogo (es. A_200)                            |
| Posizione (Y)      | quota verticale sul fronte [m]                             |
| Passo orizzontale  | interasse ⟂ alla sezione [m]                              |
| Inclinazione Δ     | sotto-orizzontale, verso la roccia [°]                    |
| Etichetta          | label visibile sul disegno                                 |

**Forza per metro** applicata = CapacitàSingola / PassoOrizzontale.

## Esempio numerico

| Parametro                                    | Valore        |
|----------------------------------------------|---------------|
| Tirante temporaneo, 4 trefoli φ0.6"           |              |
| D, L bulbo, D<sub>foro</sub>                  | 32, 4m, 150mm |
| f<sub>yd</sub>, η, τ<sub>b</sub>             | 391, 90, 2    |
| Ancoraggio in roccia, σ<sub>c</sub> = 30 MPa |              |
| 0 prove pull-out, γ<sub>Ra,t</sub> = 1.10    |              |
| Passo orizzontale = 2.5 m                    |              |

Risultati attesi (catena):
- R<sub>acciaio</sub> = π·32²/4 · 391 · 0.9 = **283 kN**
- R<sub>aderenza</sub> = π·32·4000·2 = **804 kN**
- R<sub>estrazione</sub> = π·150·4000·3 = **5655 kN** (roccia compatta)
- R<sub>min</sub> = **283 kN** (governa l'acciaio)
- R<sub>k</sub> = 283 / 1.40 = **202 kN**
- R<sub>d</sub> = 202 / 1.10 = **184 kN**
- Forza per metro = 184 / 2.5 = **73.5 kN/m**

## Verifiche NTC §6.6 esplicite

Per ogni tipologia il pannello mostra (stile SRS):

| Codice | Verifica                              | R<sub>i</sub> ≥ E<sub>d</sub> | R/E   | Esito |
|--------|---------------------------------------|-------------------------------|-------|-------|
| R.2    | Trazione armatura                     | 283 ≥ 184 kN                  | 1.54  | ✓     |
| R.3    | Sfilamento barra ↔ malta             | 804 ≥ 184 kN                  | 4.37  | ✓     |
| R.4    | Sfilamento bulbo ↔ roccia            | 5655 ≥ 184 kN                 | 30.7  | ✓     |

Con E<sub>d</sub> = R<sub>d</sub> (valore di progetto usato nell'equilibrio).

## Riferimenti

- NTC 2018 §6.6, Tab. 6.6.III
- EN 1537 — Esecuzione di lavori geotecnici speciali · Tiranti di ancoraggio
- Bustamante-Doix 1985
